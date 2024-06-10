'''
# AWS CloudFormation Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.
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
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnCustomResource(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnCustomResource",
):
    '''In a CloudFormation template, you use the ``AWS::CloudFormation::CustomResource`` or ``Custom:: *String*`` resource type to specify custom resources.

    Custom resources provide a way for you to write custom provisioning logic in CloudFormation template and have CloudFormation run it during a stack operation, such as when you create, update or delete a stack. For more information, see `Custom resources <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources.html>`_ .
    .. epigraph::

       If you use the `VPC endpoints <https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html>`_ feature, custom resources in the VPC must have access to CloudFormation -specific Amazon Simple Storage Service ( Amazon S3 ) buckets. Custom resources must send responses to a presigned Amazon S3 URL. If they can't send responses to Amazon S3 , CloudFormation won't receive a response and the stack operation fails. For more information, see `Setting up VPC endpoints for AWS CloudFormation <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-vpce-bucketnames.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-customresource.html
    :cloudformationResource: AWS::CloudFormation::CustomResource
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudformation as cloudformation
        
        cfn_custom_resource = cloudformation.CfnCustomResource(self, "MyCfnCustomResource",
            service_token="serviceToken"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        service_token: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param service_token: .. epigraph:: Only one property is defined by AWS for a custom resource: ``ServiceToken`` . All other properties are defined by the service provider. The service token that was given to the template developer by the service provider to access the service, such as an Amazon SNS topic ARN or Lambda function ARN. The service token must be from the same Region in which you are creating the stack. Updates aren't supported.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0a3b106ffbe7fa1289a8e834aa35f1789994087e265fc54556841046e49661f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCustomResourceProps(service_token=service_token)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d68a034cdb94c769aad71e0c0e32ff9640cb173daa74beb6268d30e7cc5c090f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__32da455611d85f4cddbdd6732b28aef10c806d245ec5102a182879612f90a78c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

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
    @jsii.member(jsii_name="serviceToken")
    def service_token(self) -> builtins.str:
        '''.. epigraph::

   Only one property is defined by AWS for a custom resource: ``ServiceToken`` .'''
        return typing.cast(builtins.str, jsii.get(self, "serviceToken"))

    @service_token.setter
    def service_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77951bc16957122471cd48666095011465879476219c4b12cf6a7c2684f5587e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceToken", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnCustomResourceProps",
    jsii_struct_bases=[],
    name_mapping={"service_token": "serviceToken"},
)
class CfnCustomResourceProps:
    def __init__(self, *, service_token: builtins.str) -> None:
        '''Properties for defining a ``CfnCustomResource``.

        :param service_token: .. epigraph:: Only one property is defined by AWS for a custom resource: ``ServiceToken`` . All other properties are defined by the service provider. The service token that was given to the template developer by the service provider to access the service, such as an Amazon SNS topic ARN or Lambda function ARN. The service token must be from the same Region in which you are creating the stack. Updates aren't supported.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-customresource.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudformation as cloudformation
            
            cfn_custom_resource_props = cloudformation.CfnCustomResourceProps(
                service_token="serviceToken"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f766b9f5ea2582bff4d2cb33b19a38fbdabfbe380c61d04a056e8e0d2a00b54a)
            check_type(argname="argument service_token", value=service_token, expected_type=type_hints["service_token"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "service_token": service_token,
        }

    @builtins.property
    def service_token(self) -> builtins.str:
        '''.. epigraph::

   Only one property is defined by AWS for a custom resource: ``ServiceToken`` .

        All other properties are defined by the service provider.

        The service token that was given to the template developer by the service provider to access the service, such as an Amazon SNS topic ARN or Lambda function ARN. The service token must be from the same Region in which you are creating the stack.

        Updates aren't supported.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-customresource.html#cfn-cloudformation-customresource-servicetoken
        '''
        result = self._values.get("service_token")
        assert result is not None, "Required property 'service_token' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCustomResourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnHookDefaultVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnHookDefaultVersion",
):
    '''The ``HookDefaultVersion`` resource specifies the default version of the hook.

    The default version of the hook is used in CloudFormation operations for this AWS account and AWS Region .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hookdefaultversion.html
    :cloudformationResource: AWS::CloudFormation::HookDefaultVersion
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudformation as cloudformation
        
        cfn_hook_default_version = cloudformation.CfnHookDefaultVersion(self, "MyCfnHookDefaultVersion",
            type_name="typeName",
            type_version_arn="typeVersionArn",
            version_id="versionId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        type_name: typing.Optional[builtins.str] = None,
        type_version_arn: typing.Optional[builtins.str] = None,
        version_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param type_name: The name of the hook. You must specify either ``TypeVersionArn`` , or ``TypeName`` and ``VersionId`` .
        :param type_version_arn: The version ID of the type configuration. You must specify either ``TypeVersionArn`` , or ``TypeName`` and ``VersionId`` .
        :param version_id: The version ID of the type specified. You must specify either ``TypeVersionArn`` , or ``TypeName`` and ``VersionId`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b8bde9f1f98ed0500179dfc97dcadf56e8ff1be4dde185bebd99abe71d79167)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnHookDefaultVersionProps(
            type_name=type_name,
            type_version_arn=type_version_arn,
            version_id=version_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d3cffde5405816d6a41ef681bf2c43df8b5bde2710721ee16254bf382423108)
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
            type_hints = typing.get_type_hints(_typecheckingstub__50c67f0fb346e88146ee0ab601fd70c28799c458260663e325a155a6150756f9)
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
        '''The Amazon Resource Number (ARN) of the activated extension, in this account and Region.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="typeName")
    def type_name(self) -> typing.Optional[builtins.str]:
        '''The name of the hook.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeName"))

    @type_name.setter
    def type_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c985f39fb842ecd8d503cc1ff86e00864e1fc45b5962d3fc9c66a7b136ac654a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeName", value)

    @builtins.property
    @jsii.member(jsii_name="typeVersionArn")
    def type_version_arn(self) -> typing.Optional[builtins.str]:
        '''The version ID of the type configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeVersionArn"))

    @type_version_arn.setter
    def type_version_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8fff96e0ddbd71a4aa46a88a0873bb65a9aad21cdec8f8be8016c745e513d99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeVersionArn", value)

    @builtins.property
    @jsii.member(jsii_name="versionId")
    def version_id(self) -> typing.Optional[builtins.str]:
        '''The version ID of the type specified.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionId"))

    @version_id.setter
    def version_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9f9bb2d06c69bb7ef45feaaed611f94d81b89f367a377c829ab1e52ed8d53a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versionId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnHookDefaultVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "type_name": "typeName",
        "type_version_arn": "typeVersionArn",
        "version_id": "versionId",
    },
)
class CfnHookDefaultVersionProps:
    def __init__(
        self,
        *,
        type_name: typing.Optional[builtins.str] = None,
        type_version_arn: typing.Optional[builtins.str] = None,
        version_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnHookDefaultVersion``.

        :param type_name: The name of the hook. You must specify either ``TypeVersionArn`` , or ``TypeName`` and ``VersionId`` .
        :param type_version_arn: The version ID of the type configuration. You must specify either ``TypeVersionArn`` , or ``TypeName`` and ``VersionId`` .
        :param version_id: The version ID of the type specified. You must specify either ``TypeVersionArn`` , or ``TypeName`` and ``VersionId`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hookdefaultversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudformation as cloudformation
            
            cfn_hook_default_version_props = cloudformation.CfnHookDefaultVersionProps(
                type_name="typeName",
                type_version_arn="typeVersionArn",
                version_id="versionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86e582779d0fb8b475195467d988078f1c65515c6a403bf9dc6b5ef8aced149f)
            check_type(argname="argument type_name", value=type_name, expected_type=type_hints["type_name"])
            check_type(argname="argument type_version_arn", value=type_version_arn, expected_type=type_hints["type_version_arn"])
            check_type(argname="argument version_id", value=version_id, expected_type=type_hints["version_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if type_name is not None:
            self._values["type_name"] = type_name
        if type_version_arn is not None:
            self._values["type_version_arn"] = type_version_arn
        if version_id is not None:
            self._values["version_id"] = version_id

    @builtins.property
    def type_name(self) -> typing.Optional[builtins.str]:
        '''The name of the hook.

        You must specify either ``TypeVersionArn`` , or ``TypeName`` and ``VersionId`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hookdefaultversion.html#cfn-cloudformation-hookdefaultversion-typename
        '''
        result = self._values.get("type_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type_version_arn(self) -> typing.Optional[builtins.str]:
        '''The version ID of the type configuration.

        You must specify either ``TypeVersionArn`` , or ``TypeName`` and ``VersionId`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hookdefaultversion.html#cfn-cloudformation-hookdefaultversion-typeversionarn
        '''
        result = self._values.get("type_version_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_id(self) -> typing.Optional[builtins.str]:
        '''The version ID of the type specified.

        You must specify either ``TypeVersionArn`` , or ``TypeName`` and ``VersionId`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hookdefaultversion.html#cfn-cloudformation-hookdefaultversion-versionid
        '''
        result = self._values.get("version_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnHookDefaultVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnHookTypeConfig(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnHookTypeConfig",
):
    '''The ``HookTypeConfig`` resource specifies the configuration of a hook.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hooktypeconfig.html
    :cloudformationResource: AWS::CloudFormation::HookTypeConfig
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudformation as cloudformation
        
        cfn_hook_type_config = cloudformation.CfnHookTypeConfig(self, "MyCfnHookTypeConfig",
            configuration="configuration",
        
            # the properties below are optional
            configuration_alias="configurationAlias",
            type_arn="typeArn",
            type_name="typeName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        configuration: builtins.str,
        configuration_alias: typing.Optional[builtins.str] = None,
        type_arn: typing.Optional[builtins.str] = None,
        type_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param configuration: Specifies the activated hook type configuration, in this AWS account and AWS Region . You must specify either ``TypeName`` and ``Configuration`` or ``TypeARN`` and ``Configuration`` .
        :param configuration_alias: Specifies the activated hook type configuration, in this AWS account and AWS Region . Defaults to ``default`` alias. Hook types currently support default configuration alias. Default: - "default"
        :param type_arn: The Amazon Resource Number (ARN) for the hook to set ``Configuration`` for. You must specify either ``TypeName`` and ``Configuration`` or ``TypeARN`` and ``Configuration`` .
        :param type_name: The unique name for your hook. Specifies a three-part namespace for your hook, with a recommended pattern of ``Organization::Service::Hook`` . You must specify either ``TypeName`` and ``Configuration`` or ``TypeARN`` and ``Configuration`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1aa75e15214f256047fa6d0b79cceb9720316dd5d5524cca649ba63b4b4613e3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnHookTypeConfigProps(
            configuration=configuration,
            configuration_alias=configuration_alias,
            type_arn=type_arn,
            type_name=type_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64d031e26b8bd0eeb56b31d7de08efef921b07640fe30239018c4b9b54f75af3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__152138584317142b159bc64a674adbec428e62f1899b9285a49a4b8e3bb752bd)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrConfigurationArn")
    def attr_configuration_arn(self) -> builtins.str:
        '''The Amazon Resource Number (ARN) of the activated hook type configuration, in this account and Region.

        :cloudformationAttribute: ConfigurationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConfigurationArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="configuration")
    def configuration(self) -> builtins.str:
        '''Specifies the activated hook type configuration, in this AWS account and AWS Region .'''
        return typing.cast(builtins.str, jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3847791ddd5530d8a9d2144538417d1a4cf5fb909bd613d41c5905e02d37bb9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuration", value)

    @builtins.property
    @jsii.member(jsii_name="configurationAlias")
    def configuration_alias(self) -> typing.Optional[builtins.str]:
        '''Specifies the activated hook type configuration, in this AWS account and AWS Region .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configurationAlias"))

    @configuration_alias.setter
    def configuration_alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__649cdf62ea09d9e4b72042f283c05b766e052006f59f2d05f9a6d2eab2ea396a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationAlias", value)

    @builtins.property
    @jsii.member(jsii_name="typeArn")
    def type_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Number (ARN) for the hook to set ``Configuration`` for.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeArn"))

    @type_arn.setter
    def type_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b787dd89e7baba7e0a6ac2766dafcb836d4d6e45724a95c5ca1fdbd30ebd66b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeArn", value)

    @builtins.property
    @jsii.member(jsii_name="typeName")
    def type_name(self) -> typing.Optional[builtins.str]:
        '''The unique name for your hook.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeName"))

    @type_name.setter
    def type_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84b67709252725d1f5ed0113558f6ddd94c0f17e7aadee85cf241f59a8eb5585)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeName", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnHookTypeConfigProps",
    jsii_struct_bases=[],
    name_mapping={
        "configuration": "configuration",
        "configuration_alias": "configurationAlias",
        "type_arn": "typeArn",
        "type_name": "typeName",
    },
)
class CfnHookTypeConfigProps:
    def __init__(
        self,
        *,
        configuration: builtins.str,
        configuration_alias: typing.Optional[builtins.str] = None,
        type_arn: typing.Optional[builtins.str] = None,
        type_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnHookTypeConfig``.

        :param configuration: Specifies the activated hook type configuration, in this AWS account and AWS Region . You must specify either ``TypeName`` and ``Configuration`` or ``TypeARN`` and ``Configuration`` .
        :param configuration_alias: Specifies the activated hook type configuration, in this AWS account and AWS Region . Defaults to ``default`` alias. Hook types currently support default configuration alias. Default: - "default"
        :param type_arn: The Amazon Resource Number (ARN) for the hook to set ``Configuration`` for. You must specify either ``TypeName`` and ``Configuration`` or ``TypeARN`` and ``Configuration`` .
        :param type_name: The unique name for your hook. Specifies a three-part namespace for your hook, with a recommended pattern of ``Organization::Service::Hook`` . You must specify either ``TypeName`` and ``Configuration`` or ``TypeARN`` and ``Configuration`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hooktypeconfig.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudformation as cloudformation
            
            cfn_hook_type_config_props = cloudformation.CfnHookTypeConfigProps(
                configuration="configuration",
            
                # the properties below are optional
                configuration_alias="configurationAlias",
                type_arn="typeArn",
                type_name="typeName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef5f9608def2c7b14e7449a6bceadbd90b6e5242e86707d305d4923d050f8f9a)
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument configuration_alias", value=configuration_alias, expected_type=type_hints["configuration_alias"])
            check_type(argname="argument type_arn", value=type_arn, expected_type=type_hints["type_arn"])
            check_type(argname="argument type_name", value=type_name, expected_type=type_hints["type_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration": configuration,
        }
        if configuration_alias is not None:
            self._values["configuration_alias"] = configuration_alias
        if type_arn is not None:
            self._values["type_arn"] = type_arn
        if type_name is not None:
            self._values["type_name"] = type_name

    @builtins.property
    def configuration(self) -> builtins.str:
        '''Specifies the activated hook type configuration, in this AWS account and AWS Region .

        You must specify either ``TypeName`` and ``Configuration`` or ``TypeARN`` and ``Configuration`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hooktypeconfig.html#cfn-cloudformation-hooktypeconfig-configuration
        '''
        result = self._values.get("configuration")
        assert result is not None, "Required property 'configuration' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration_alias(self) -> typing.Optional[builtins.str]:
        '''Specifies the activated hook type configuration, in this AWS account and AWS Region .

        Defaults to ``default`` alias. Hook types currently support default configuration alias.

        :default: - "default"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hooktypeconfig.html#cfn-cloudformation-hooktypeconfig-configurationalias
        '''
        result = self._values.get("configuration_alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Number (ARN) for the hook to set ``Configuration`` for.

        You must specify either ``TypeName`` and ``Configuration`` or ``TypeARN`` and ``Configuration`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hooktypeconfig.html#cfn-cloudformation-hooktypeconfig-typearn
        '''
        result = self._values.get("type_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type_name(self) -> typing.Optional[builtins.str]:
        '''The unique name for your hook.

        Specifies a three-part namespace for your hook, with a recommended pattern of ``Organization::Service::Hook`` .

        You must specify either ``TypeName`` and ``Configuration`` or ``TypeARN`` and ``Configuration`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hooktypeconfig.html#cfn-cloudformation-hooktypeconfig-typename
        '''
        result = self._values.get("type_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnHookTypeConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnHookVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnHookVersion",
):
    '''The ``HookVersion`` resource publishes new or first hook version to the AWS CloudFormation registry.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hookversion.html
    :cloudformationResource: AWS::CloudFormation::HookVersion
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudformation as cloudformation
        
        cfn_hook_version = cloudformation.CfnHookVersion(self, "MyCfnHookVersion",
            schema_handler_package="schemaHandlerPackage",
            type_name="typeName",
        
            # the properties below are optional
            execution_role_arn="executionRoleArn",
            logging_config=cloudformation.CfnHookVersion.LoggingConfigProperty(
                log_group_name="logGroupName",
                log_role_arn="logRoleArn"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        schema_handler_package: builtins.str,
        type_name: builtins.str,
        execution_role_arn: typing.Optional[builtins.str] = None,
        logging_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnHookVersion.LoggingConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param schema_handler_package: A URL to the Amazon S3 bucket containing the hook project package that contains the necessary files for the hook you want to register. For information on generating a schema handler package for the resource you want to register, see `submit <https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-submit.html>`_ in the *CloudFormation CLI User Guide for Extension Development* . .. epigraph:: The user registering the resource must be able to access the package in the S3 bucket. That's, the user must have `GetObject <https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html>`_ permissions for the schema handler package. For more information, see `Actions, Resources, and Condition Keys for Amazon S3 <https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazons3.html>`_ in the *AWS Identity and Access Management User Guide* .
        :param type_name: The unique name for your hook. Specifies a three-part namespace for your hook, with a recommended pattern of ``Organization::Service::Hook`` . .. epigraph:: The following organization namespaces are reserved and can't be used in your hook type names: - ``Alexa`` - ``AMZN`` - ``Amazon`` - ``ASK`` - ``AWS`` - ``Custom`` - ``Dev``
        :param execution_role_arn: The Amazon Resource Name (ARN) of the task execution role that grants the hook permission.
        :param logging_config: Contains logging configuration information for an extension.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__291bd220d9e7cd7e2d0ca851a8919b3ac012e0d7a45a664cf291d6381de23d73)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnHookVersionProps(
            schema_handler_package=schema_handler_package,
            type_name=type_name,
            execution_role_arn=execution_role_arn,
            logging_config=logging_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19d9ff1b2b94a1214e3523199f203ce84bb6818d8221d1c9c8864607fd68ed54)
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
            type_hints = typing.get_type_hints(_typecheckingstub__373bbf4ceb7d1c3f9739457d175b6e990bef886865f570c651e71104ae299479)
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
        '''The Amazon Resource Name (ARN) of the hook.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrIsDefaultVersion")
    def attr_is_default_version(self) -> _IResolvable_da3f097b:
        '''Whether the specified hook version is set as the default version.

        :cloudformationAttribute: IsDefaultVersion
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrIsDefaultVersion"))

    @builtins.property
    @jsii.member(jsii_name="attrTypeArn")
    def attr_type_arn(self) -> builtins.str:
        '''The Amazon Resource Number (ARN) assigned to this version of the hook.

        :cloudformationAttribute: TypeArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTypeArn"))

    @builtins.property
    @jsii.member(jsii_name="attrVersionId")
    def attr_version_id(self) -> builtins.str:
        '''The ID of this version of the hook.

        :cloudformationAttribute: VersionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVersionId"))

    @builtins.property
    @jsii.member(jsii_name="attrVisibility")
    def attr_visibility(self) -> builtins.str:
        '''The scope at which the resource is visible and usable in CloudFormation operations.

        Valid values include:

        - ``PRIVATE`` : The resource is only visible and usable within the account in which it's registered. CloudFormation marks any resources you register as ``PRIVATE`` .
        - ``PUBLIC`` : The resource is publicly visible and usable within any Amazon account.

        :cloudformationAttribute: Visibility
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVisibility"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="schemaHandlerPackage")
    def schema_handler_package(self) -> builtins.str:
        '''A URL to the Amazon S3 bucket containing the hook project package that contains the necessary files for the hook you want to register.'''
        return typing.cast(builtins.str, jsii.get(self, "schemaHandlerPackage"))

    @schema_handler_package.setter
    def schema_handler_package(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0efb96dfc84b17d40a50018cd6d23e3c296865fd07b6996b365c17a092ce873c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaHandlerPackage", value)

    @builtins.property
    @jsii.member(jsii_name="typeName")
    def type_name(self) -> builtins.str:
        '''The unique name for your hook.'''
        return typing.cast(builtins.str, jsii.get(self, "typeName"))

    @type_name.setter
    def type_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30df538b23952e625e940e55d9e80b1642e22eea6fc3b3850d26f16b544d134d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeName", value)

    @builtins.property
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the task execution role that grants the hook permission.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleArn"))

    @execution_role_arn.setter
    def execution_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cb4f09410ca3ef9c85888607e8ac924121a6fe32ab21f62e93aa2cc02b1130a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="loggingConfig")
    def logging_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnHookVersion.LoggingConfigProperty"]]:
        '''Contains logging configuration information for an extension.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnHookVersion.LoggingConfigProperty"]], jsii.get(self, "loggingConfig"))

    @logging_config.setter
    def logging_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnHookVersion.LoggingConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b1199d24d006c1117662bdfbc72f2cbbbd5b4d4138b339988fd36100745a337)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loggingConfig", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudformation.CfnHookVersion.LoggingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group_name": "logGroupName", "log_role_arn": "logRoleArn"},
    )
    class LoggingConfigProperty:
        def __init__(
            self,
            *,
            log_group_name: typing.Optional[builtins.str] = None,
            log_role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``LoggingConfig`` property type specifies logging configuration information for an extension.

            :param log_group_name: The Amazon CloudWatch Logs group to which CloudFormation sends error logging information when invoking the extension's handlers.
            :param log_role_arn: The Amazon Resource Name (ARN) of the role that CloudFormation should assume when sending log entries to CloudWatch Logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-hookversion-loggingconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudformation as cloudformation
                
                logging_config_property = cloudformation.CfnHookVersion.LoggingConfigProperty(
                    log_group_name="logGroupName",
                    log_role_arn="logRoleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c3186540a164984c66b6fb1ac418c16e60743db883585e9275304381fae9a1cf)
                check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
                check_type(argname="argument log_role_arn", value=log_role_arn, expected_type=type_hints["log_role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if log_group_name is not None:
                self._values["log_group_name"] = log_group_name
            if log_role_arn is not None:
                self._values["log_role_arn"] = log_role_arn

        @builtins.property
        def log_group_name(self) -> typing.Optional[builtins.str]:
            '''The Amazon CloudWatch Logs group to which CloudFormation sends error logging information when invoking the extension's handlers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-hookversion-loggingconfig.html#cfn-cloudformation-hookversion-loggingconfig-loggroupname
            '''
            result = self._values.get("log_group_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def log_role_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the role that CloudFormation should assume when sending log entries to CloudWatch Logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-hookversion-loggingconfig.html#cfn-cloudformation-hookversion-loggingconfig-logrolearn
            '''
            result = self._values.get("log_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnHookVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "schema_handler_package": "schemaHandlerPackage",
        "type_name": "typeName",
        "execution_role_arn": "executionRoleArn",
        "logging_config": "loggingConfig",
    },
)
class CfnHookVersionProps:
    def __init__(
        self,
        *,
        schema_handler_package: builtins.str,
        type_name: builtins.str,
        execution_role_arn: typing.Optional[builtins.str] = None,
        logging_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHookVersion.LoggingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnHookVersion``.

        :param schema_handler_package: A URL to the Amazon S3 bucket containing the hook project package that contains the necessary files for the hook you want to register. For information on generating a schema handler package for the resource you want to register, see `submit <https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-submit.html>`_ in the *CloudFormation CLI User Guide for Extension Development* . .. epigraph:: The user registering the resource must be able to access the package in the S3 bucket. That's, the user must have `GetObject <https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html>`_ permissions for the schema handler package. For more information, see `Actions, Resources, and Condition Keys for Amazon S3 <https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazons3.html>`_ in the *AWS Identity and Access Management User Guide* .
        :param type_name: The unique name for your hook. Specifies a three-part namespace for your hook, with a recommended pattern of ``Organization::Service::Hook`` . .. epigraph:: The following organization namespaces are reserved and can't be used in your hook type names: - ``Alexa`` - ``AMZN`` - ``Amazon`` - ``ASK`` - ``AWS`` - ``Custom`` - ``Dev``
        :param execution_role_arn: The Amazon Resource Name (ARN) of the task execution role that grants the hook permission.
        :param logging_config: Contains logging configuration information for an extension.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hookversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudformation as cloudformation
            
            cfn_hook_version_props = cloudformation.CfnHookVersionProps(
                schema_handler_package="schemaHandlerPackage",
                type_name="typeName",
            
                # the properties below are optional
                execution_role_arn="executionRoleArn",
                logging_config=cloudformation.CfnHookVersion.LoggingConfigProperty(
                    log_group_name="logGroupName",
                    log_role_arn="logRoleArn"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a9bb2ef202f6ed27272b4d9787339d2a26c63beb648e39f3c4977200bcc65b1)
            check_type(argname="argument schema_handler_package", value=schema_handler_package, expected_type=type_hints["schema_handler_package"])
            check_type(argname="argument type_name", value=type_name, expected_type=type_hints["type_name"])
            check_type(argname="argument execution_role_arn", value=execution_role_arn, expected_type=type_hints["execution_role_arn"])
            check_type(argname="argument logging_config", value=logging_config, expected_type=type_hints["logging_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "schema_handler_package": schema_handler_package,
            "type_name": type_name,
        }
        if execution_role_arn is not None:
            self._values["execution_role_arn"] = execution_role_arn
        if logging_config is not None:
            self._values["logging_config"] = logging_config

    @builtins.property
    def schema_handler_package(self) -> builtins.str:
        '''A URL to the Amazon S3 bucket containing the hook project package that contains the necessary files for the hook you want to register.

        For information on generating a schema handler package for the resource you want to register, see `submit <https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-submit.html>`_ in the *CloudFormation CLI User Guide for Extension Development* .
        .. epigraph::

           The user registering the resource must be able to access the package in the S3 bucket. That's, the user must have `GetObject <https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html>`_ permissions for the schema handler package. For more information, see `Actions, Resources, and Condition Keys for Amazon S3 <https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazons3.html>`_ in the *AWS Identity and Access Management User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hookversion.html#cfn-cloudformation-hookversion-schemahandlerpackage
        '''
        result = self._values.get("schema_handler_package")
        assert result is not None, "Required property 'schema_handler_package' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type_name(self) -> builtins.str:
        '''The unique name for your hook.

        Specifies a three-part namespace for your hook, with a recommended pattern of ``Organization::Service::Hook`` .
        .. epigraph::

           The following organization namespaces are reserved and can't be used in your hook type names:

           - ``Alexa``
           - ``AMZN``
           - ``Amazon``
           - ``ASK``
           - ``AWS``
           - ``Custom``
           - ``Dev``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hookversion.html#cfn-cloudformation-hookversion-typename
        '''
        result = self._values.get("type_name")
        assert result is not None, "Required property 'type_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the task execution role that grants the hook permission.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hookversion.html#cfn-cloudformation-hookversion-executionrolearn
        '''
        result = self._values.get("execution_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnHookVersion.LoggingConfigProperty]]:
        '''Contains logging configuration information for an extension.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hookversion.html#cfn-cloudformation-hookversion-loggingconfig
        '''
        result = self._values.get("logging_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnHookVersion.LoggingConfigProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnHookVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnMacro(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnMacro",
):
    '''The ``AWS::CloudFormation::Macro`` resource is a CloudFormation resource type that creates a CloudFormation macro to perform custom processing on CloudFormation templates.

    For more information, see `Using AWS CloudFormation macros to perform custom processing on templates <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html
    :cloudformationResource: AWS::CloudFormation::Macro
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudformation as cloudformation
        
        cfn_macro = cloudformation.CfnMacro(self, "MyCfnMacro",
            function_name="functionName",
            name="name",
        
            # the properties below are optional
            description="description",
            log_group_name="logGroupName",
            log_role_arn="logRoleArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        function_name: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param function_name: The Amazon Resource Name (ARN) of the underlying AWS Lambda function that you want AWS CloudFormation to invoke when the macro is run.
        :param name: The name of the macro. The name of the macro must be unique across all macros in the account.
        :param description: A description of the macro.
        :param log_group_name: The CloudWatch Logs group to which AWS CloudFormation sends error logging information when invoking the macro's underlying AWS Lambda function.
        :param log_role_arn: The ARN of the role AWS CloudFormation should assume when sending log entries to CloudWatch Logs .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__459b4551acd819b198938843c729caa68cfe3bcc1ac16be0f4fd2dcd90f33831)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMacroProps(
            function_name=function_name,
            name=name,
            description=description,
            log_group_name=log_group_name,
            log_role_arn=log_role_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e79976b6be80cc0b5afd2b70e48da1b0c8e9d3428ef7477627dbe51024a9c253)
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
            type_hints = typing.get_type_hints(_typecheckingstub__86ff8044429c96b4c0bd2cfb5a521df919f8d44b6c475424ccb71b25a5a27bfd)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

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
    @jsii.member(jsii_name="functionName")
    def function_name(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the underlying AWS Lambda function that you want AWS CloudFormation to invoke when the macro is run.'''
        return typing.cast(builtins.str, jsii.get(self, "functionName"))

    @function_name.setter
    def function_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b0da3fdeddad952c3d568e3ccfa62b9e1071259fd408795b5efbd74d57e4638)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionName", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the macro.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d90b36bce3c84920d31c840cdf1935d477a088ab2099260661fa84ff8a860aed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the macro.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d119fc672e810bdbbc903e1fd3131af02cfeee73b8d1f69b91281fd849867947)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> typing.Optional[builtins.str]:
        '''The CloudWatch Logs group to which AWS CloudFormation sends error logging information when invoking the macro's underlying AWS Lambda function.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2549852c1e5490496427fcb72c16723fec532a2e82b6f7266d106b423891194)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="logRoleArn")
    def log_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the role AWS CloudFormation should assume when sending log entries to CloudWatch Logs .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logRoleArn"))

    @log_role_arn.setter
    def log_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f243639cffd7e9711e024007e213cfd4f0a728fdffd3d87d4544108f9615424)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logRoleArn", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnMacroProps",
    jsii_struct_bases=[],
    name_mapping={
        "function_name": "functionName",
        "name": "name",
        "description": "description",
        "log_group_name": "logGroupName",
        "log_role_arn": "logRoleArn",
    },
)
class CfnMacroProps:
    def __init__(
        self,
        *,
        function_name: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnMacro``.

        :param function_name: The Amazon Resource Name (ARN) of the underlying AWS Lambda function that you want AWS CloudFormation to invoke when the macro is run.
        :param name: The name of the macro. The name of the macro must be unique across all macros in the account.
        :param description: A description of the macro.
        :param log_group_name: The CloudWatch Logs group to which AWS CloudFormation sends error logging information when invoking the macro's underlying AWS Lambda function.
        :param log_role_arn: The ARN of the role AWS CloudFormation should assume when sending log entries to CloudWatch Logs .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudformation as cloudformation
            
            cfn_macro_props = cloudformation.CfnMacroProps(
                function_name="functionName",
                name="name",
            
                # the properties below are optional
                description="description",
                log_group_name="logGroupName",
                log_role_arn="logRoleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42b23a370c2b5c33d49b7f892f41cb61bdad8c6efe4c078d5d357c872fd866b6)
            check_type(argname="argument function_name", value=function_name, expected_type=type_hints["function_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            check_type(argname="argument log_role_arn", value=log_role_arn, expected_type=type_hints["log_role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "function_name": function_name,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if log_group_name is not None:
            self._values["log_group_name"] = log_group_name
        if log_role_arn is not None:
            self._values["log_role_arn"] = log_role_arn

    @builtins.property
    def function_name(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the underlying AWS Lambda function that you want AWS CloudFormation to invoke when the macro is run.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-functionname
        '''
        result = self._values.get("function_name")
        assert result is not None, "Required property 'function_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the macro.

        The name of the macro must be unique across all macros in the account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the macro.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_group_name(self) -> typing.Optional[builtins.str]:
        '''The CloudWatch Logs group to which AWS CloudFormation sends error logging information when invoking the macro's underlying AWS Lambda function.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-loggroupname
        '''
        result = self._values.get("log_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the role AWS CloudFormation should assume when sending log entries to CloudWatch Logs .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-logrolearn
        '''
        result = self._values.get("log_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMacroProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnModuleDefaultVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnModuleDefaultVersion",
):
    '''Specifies the default version of a module.

    The default version of the module will be used in CloudFormation operations for this account and Region.

    To register a module version, use the ``[``AWS::CloudFormation::ModuleVersion``](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduleversion.html)`` resource.

    For more information using modules, see `Using modules to encapsulate and reuse resource configurations <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/modules.html>`_ and `Registering extensions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html#registry-register>`_ in the *AWS CloudFormation User Guide* . For information on developing modules, see `Developing modules <https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/modules.html>`_ in the *AWS CloudFormation CLI User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduledefaultversion.html
    :cloudformationResource: AWS::CloudFormation::ModuleDefaultVersion
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudformation as cloudformation
        
        cfn_module_default_version = cloudformation.CfnModuleDefaultVersion(self, "MyCfnModuleDefaultVersion",
            arn="arn",
            module_name="moduleName",
            version_id="versionId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        arn: typing.Optional[builtins.str] = None,
        module_name: typing.Optional[builtins.str] = None,
        version_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param arn: The Amazon Resource Name (ARN) of the module version to set as the default version. Conditional: You must specify either ``Arn`` , or ``ModuleName`` and ``VersionId`` .
        :param module_name: The name of the module. Conditional: You must specify either ``Arn`` , or ``ModuleName`` and ``VersionId`` .
        :param version_id: The ID for the specific version of the module. Conditional: You must specify either ``Arn`` , or ``ModuleName`` and ``VersionId`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c99a91d0140bd9a8f50bc3d072ae8da722981d1a5fcb2663b4fac493489b2cb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnModuleDefaultVersionProps(
            arn=arn, module_name=module_name, version_id=version_id
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d83f9976a4a99125758d72c5d97e0b8bc18b132214c023e9e853759dbce1d4a4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__96e84170f59bacf8bbda0fc4d70222b46dbd510ff329e31a72d532819620ac0e)
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
    @jsii.member(jsii_name="arn")
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the module version to set as the default version.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arn"))

    @arn.setter
    def arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1951b46878047a0bebb4baa53659dd9872ccb6a4bb32a494795339c0571ba62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arn", value)

    @builtins.property
    @jsii.member(jsii_name="moduleName")
    def module_name(self) -> typing.Optional[builtins.str]:
        '''The name of the module.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "moduleName"))

    @module_name.setter
    def module_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b448aa45d5a1bdb97e2a01807f61b189d67e11631eacdc0cbdba01fc0ca8b5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "moduleName", value)

    @builtins.property
    @jsii.member(jsii_name="versionId")
    def version_id(self) -> typing.Optional[builtins.str]:
        '''The ID for the specific version of the module.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionId"))

    @version_id.setter
    def version_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2565d831587a784d43e20ccbd403e1a5b0a41c68a6ea34925b2361aed7757b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versionId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnModuleDefaultVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "module_name": "moduleName",
        "version_id": "versionId",
    },
)
class CfnModuleDefaultVersionProps:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        module_name: typing.Optional[builtins.str] = None,
        version_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnModuleDefaultVersion``.

        :param arn: The Amazon Resource Name (ARN) of the module version to set as the default version. Conditional: You must specify either ``Arn`` , or ``ModuleName`` and ``VersionId`` .
        :param module_name: The name of the module. Conditional: You must specify either ``Arn`` , or ``ModuleName`` and ``VersionId`` .
        :param version_id: The ID for the specific version of the module. Conditional: You must specify either ``Arn`` , or ``ModuleName`` and ``VersionId`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduledefaultversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudformation as cloudformation
            
            cfn_module_default_version_props = cloudformation.CfnModuleDefaultVersionProps(
                arn="arn",
                module_name="moduleName",
                version_id="versionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f3ea65dfbd0cb512b468da1b9fb9627d1355ed7f5434478a08a635f804f77fc)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument module_name", value=module_name, expected_type=type_hints["module_name"])
            check_type(argname="argument version_id", value=version_id, expected_type=type_hints["version_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if module_name is not None:
            self._values["module_name"] = module_name
        if version_id is not None:
            self._values["version_id"] = version_id

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the module version to set as the default version.

        Conditional: You must specify either ``Arn`` , or ``ModuleName`` and ``VersionId`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduledefaultversion.html#cfn-cloudformation-moduledefaultversion-arn
        '''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def module_name(self) -> typing.Optional[builtins.str]:
        '''The name of the module.

        Conditional: You must specify either ``Arn`` , or ``ModuleName`` and ``VersionId`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduledefaultversion.html#cfn-cloudformation-moduledefaultversion-modulename
        '''
        result = self._values.get("module_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_id(self) -> typing.Optional[builtins.str]:
        '''The ID for the specific version of the module.

        Conditional: You must specify either ``Arn`` , or ``ModuleName`` and ``VersionId`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduledefaultversion.html#cfn-cloudformation-moduledefaultversion-versionid
        '''
        result = self._values.get("version_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModuleDefaultVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnModuleVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnModuleVersion",
):
    '''Registers the specified version of the module with the CloudFormation service.

    Registering a module makes it available for use in CloudFormation templates in your AWS account and Region.

    To specify a module version as the default version, use the ``[``AWS::CloudFormation::ModuleDefaultVersion``](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduledefaultversion.html)`` resource.

    For more information using modules, see `Using modules to encapsulate and reuse resource configurations <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/modules.html>`_ and `Registering extensions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html#registry-register>`_ in the *CloudFormation User Guide* . For information on developing modules, see `Developing modules <https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/modules.html>`_ in the *CloudFormation CLI User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduleversion.html
    :cloudformationResource: AWS::CloudFormation::ModuleVersion
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudformation as cloudformation
        
        cfn_module_version = cloudformation.CfnModuleVersion(self, "MyCfnModuleVersion",
            module_name="moduleName",
            module_package="modulePackage"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        module_name: builtins.str,
        module_package: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param module_name: The name of the module being registered.
        :param module_package: A URL to the S3 bucket containing the package that contains the template fragment and schema files for the module version to register. .. epigraph:: The user registering the module version must be able to access the module package in the S3 bucket. That's, the user needs to have `GetObject <https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html>`_ permissions for the package. For more information, see `Actions, Resources, and Condition Keys for Amazon S3 <https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazons3.html>`_ in the *AWS Identity and Access Management User Guide* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50da97e251a6b1bacc1202d70f10c857ca74139ea4e8bcc35b2ff47e8b8b2729)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnModuleVersionProps(
            module_name=module_name, module_package=module_package
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8f07b3edeecaaa60f70d40c8955ccee2de0a5b10eab7df6791cee814a719762)
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
            type_hints = typing.get_type_hints(_typecheckingstub__93f33fd2a94ced47dcfc85eb2d6054254d607a4b79fcf6223d2366514e67189d)
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
        '''The Amazon Resource Name (ARN) of the extension.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrDescription")
    def attr_description(self) -> builtins.str:
        '''The description of the extension.

        :cloudformationAttribute: Description
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDescription"))

    @builtins.property
    @jsii.member(jsii_name="attrDocumentationUrl")
    def attr_documentation_url(self) -> builtins.str:
        '''The URL of a page providing detailed documentation for this module.

        :cloudformationAttribute: DocumentationUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDocumentationUrl"))

    @builtins.property
    @jsii.member(jsii_name="attrIsDefaultVersion")
    def attr_is_default_version(self) -> _IResolvable_da3f097b:
        '''Whether the specified extension version is set as the default version.

        This applies only to private extensions you have registered in your account, and extensions published by AWS . For public third-party extensions, whether they are activated in your account, CloudFormation returns ``null`` .

        :cloudformationAttribute: IsDefaultVersion
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrIsDefaultVersion"))

    @builtins.property
    @jsii.member(jsii_name="attrSchema")
    def attr_schema(self) -> builtins.str:
        '''The schema that defines the extension.

        For more information about extension schemas, see `Resource Provider Schema <https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html>`_ in the *CloudFormation CLI User Guide* .

        :cloudformationAttribute: Schema
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSchema"))

    @builtins.property
    @jsii.member(jsii_name="attrTimeCreated")
    def attr_time_created(self) -> builtins.str:
        '''When the specified private extension version was registered or activated in your account.

        :cloudformationAttribute: TimeCreated
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTimeCreated"))

    @builtins.property
    @jsii.member(jsii_name="attrVersionId")
    def attr_version_id(self) -> builtins.str:
        '''The ID of this version of the module.

        :cloudformationAttribute: VersionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVersionId"))

    @builtins.property
    @jsii.member(jsii_name="attrVisibility")
    def attr_visibility(self) -> builtins.str:
        '''The scope at which the extension is visible and usable in CloudFormation operations.

        Valid values include:

        - ``PRIVATE`` : The extension is only visible and usable within the account in which it is registered. AWS CloudFormation marks any extensions you register as ``PRIVATE`` .
        - ``PUBLIC`` : The extension is publicly visible and usable within any AWS account.

        :cloudformationAttribute: Visibility
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVisibility"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="moduleName")
    def module_name(self) -> builtins.str:
        '''The name of the module being registered.'''
        return typing.cast(builtins.str, jsii.get(self, "moduleName"))

    @module_name.setter
    def module_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5ddab8adf20df5c0b192a1c24dff5f7d64b2e7e20fefec44ae32c6caeab6ce1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "moduleName", value)

    @builtins.property
    @jsii.member(jsii_name="modulePackage")
    def module_package(self) -> builtins.str:
        '''A URL to the S3 bucket containing the package that contains the template fragment and schema files for the module version to register.'''
        return typing.cast(builtins.str, jsii.get(self, "modulePackage"))

    @module_package.setter
    def module_package(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d720948c279cd9b12fc9a1cce3d68bd4e92be8876552138cf8bc30bce71b233f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modulePackage", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnModuleVersionProps",
    jsii_struct_bases=[],
    name_mapping={"module_name": "moduleName", "module_package": "modulePackage"},
)
class CfnModuleVersionProps:
    def __init__(
        self,
        *,
        module_name: builtins.str,
        module_package: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnModuleVersion``.

        :param module_name: The name of the module being registered.
        :param module_package: A URL to the S3 bucket containing the package that contains the template fragment and schema files for the module version to register. .. epigraph:: The user registering the module version must be able to access the module package in the S3 bucket. That's, the user needs to have `GetObject <https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html>`_ permissions for the package. For more information, see `Actions, Resources, and Condition Keys for Amazon S3 <https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazons3.html>`_ in the *AWS Identity and Access Management User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduleversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudformation as cloudformation
            
            cfn_module_version_props = cloudformation.CfnModuleVersionProps(
                module_name="moduleName",
                module_package="modulePackage"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08386807944526883f9a2a3af6d7b270292ea388802a7d26e4ebe78b66b8aa38)
            check_type(argname="argument module_name", value=module_name, expected_type=type_hints["module_name"])
            check_type(argname="argument module_package", value=module_package, expected_type=type_hints["module_package"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "module_name": module_name,
            "module_package": module_package,
        }

    @builtins.property
    def module_name(self) -> builtins.str:
        '''The name of the module being registered.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduleversion.html#cfn-cloudformation-moduleversion-modulename
        '''
        result = self._values.get("module_name")
        assert result is not None, "Required property 'module_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def module_package(self) -> builtins.str:
        '''A URL to the S3 bucket containing the package that contains the template fragment and schema files for the module version to register.

        .. epigraph::

           The user registering the module version must be able to access the module package in the S3 bucket. That's, the user needs to have `GetObject <https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html>`_ permissions for the package. For more information, see `Actions, Resources, and Condition Keys for Amazon S3 <https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazons3.html>`_ in the *AWS Identity and Access Management User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduleversion.html#cfn-cloudformation-moduleversion-modulepackage
        '''
        result = self._values.get("module_package")
        assert result is not None, "Required property 'module_package' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModuleVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnPublicTypeVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnPublicTypeVersion",
):
    '''Tests and publishes a registered extension as a public, third-party extension.

    CloudFormation first tests the extension to make sure it meets all necessary requirements for being published in the CloudFormation registry. If it does, CloudFormation then publishes it to the registry as a public third-party extension in this Region. Public extensions are available for use by all CloudFormation users.

    - For resource types, testing includes passing all contracts tests defined for the type.
    - For modules, testing includes determining if the module's model meets all necessary requirements.

    For more information, see `Testing your public extension prior to publishing <https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-testing>`_ in the *CloudFormation CLI User Guide* .

    If you don't specify a version, CloudFormation uses the default version of the extension in your account and Region for testing.

    To perform testing, CloudFormation assumes the execution role specified when the type was registered.

    An extension must have a test status of ``PASSED`` before it can be published. For more information, see `Publishing extensions to make them available for public use <https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-publish.html>`_ in the *CloudFormation CLI User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html
    :cloudformationResource: AWS::CloudFormation::PublicTypeVersion
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudformation as cloudformation
        
        cfn_public_type_version = cloudformation.CfnPublicTypeVersion(self, "MyCfnPublicTypeVersion",
            arn="arn",
            log_delivery_bucket="logDeliveryBucket",
            public_version_number="publicVersionNumber",
            type="type",
            type_name="typeName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        arn: typing.Optional[builtins.str] = None,
        log_delivery_bucket: typing.Optional[builtins.str] = None,
        public_version_number: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        type_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param arn: The Amazon Resource Number (ARN) of the extension. Conditional: You must specify ``Arn`` , or ``TypeName`` and ``Type`` .
        :param log_delivery_bucket: The S3 bucket to which CloudFormation delivers the contract test execution logs. CloudFormation delivers the logs by the time contract testing has completed and the extension has been assigned a test type status of ``PASSED`` or ``FAILED`` . The user initiating the stack operation must be able to access items in the specified S3 bucket. Specifically, the user needs the following permissions: - GetObject - PutObject For more information, see `Actions, Resources, and Condition Keys for Amazon S3 <https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html>`_ in the *AWS Identity and Access Management User Guide* .
        :param public_version_number: The version number to assign to this version of the extension. Use the following format, and adhere to semantic versioning when assigning a version number to your extension: ``MAJOR.MINOR.PATCH`` For more information, see `Semantic Versioning 2.0.0 <https://docs.aws.amazon.com/https://semver.org/>`_ . If you don't specify a version number, CloudFormation increments the version number by one minor version release. You cannot specify a version number the first time you publish a type. AWS CloudFormation automatically sets the first version number to be ``1.0.0`` .
        :param type: The type of the extension to test. Conditional: You must specify ``Arn`` , or ``TypeName`` and ``Type`` .
        :param type_name: The name of the extension to test. Conditional: You must specify ``Arn`` , or ``TypeName`` and ``Type`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdf2194d5c024c7904a7b498046de219f29aca0dc247850eeb368cc6e8de6e80)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPublicTypeVersionProps(
            arn=arn,
            log_delivery_bucket=log_delivery_bucket,
            public_version_number=public_version_number,
            type=type,
            type_name=type_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b8e80bbf83093dbb7c5669cba4eb3df0f24e04ad66ac14f184f58bc8c80cdaa)
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
            type_hints = typing.get_type_hints(_typecheckingstub__24c9fd4ba1a836eec8198800f5120b3dd3a490a47fb73c5b6f9bda3dc4509f77)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrPublicTypeArn")
    def attr_public_type_arn(self) -> builtins.str:
        '''The Amazon Resource Number (ARN) assigned to the public extension upon publication.

        :cloudformationAttribute: PublicTypeArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPublicTypeArn"))

    @builtins.property
    @jsii.member(jsii_name="attrPublisherId")
    def attr_publisher_id(self) -> builtins.str:
        '''The publisher ID of the extension publisher.

        This applies only to public third-party extensions. For private registered extensions, and extensions provided by AWS , CloudFormation returns ``null`` .

        :cloudformationAttribute: PublisherId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPublisherId"))

    @builtins.property
    @jsii.member(jsii_name="attrTypeVersionArn")
    def attr_type_version_arn(self) -> builtins.str:
        '''The Amazon Resource Number (ARN) assigned to this version of the extension.

        :cloudformationAttribute: TypeVersionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTypeVersionArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Number (ARN) of the extension.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arn"))

    @arn.setter
    def arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef7377cb03089af40e51eb3ff0d703af316eb40432079d1af709f52cd1ddc8d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arn", value)

    @builtins.property
    @jsii.member(jsii_name="logDeliveryBucket")
    def log_delivery_bucket(self) -> typing.Optional[builtins.str]:
        '''The S3 bucket to which CloudFormation delivers the contract test execution logs.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logDeliveryBucket"))

    @log_delivery_bucket.setter
    def log_delivery_bucket(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87da3449532bb7cc8ef07cf37320b48e158d2074ac9402065fe2f31b61fe3936)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logDeliveryBucket", value)

    @builtins.property
    @jsii.member(jsii_name="publicVersionNumber")
    def public_version_number(self) -> typing.Optional[builtins.str]:
        '''The version number to assign to this version of the extension.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicVersionNumber"))

    @public_version_number.setter
    def public_version_number(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7c6d97beb345173cfda1fd73e5d035568d8ecfbbd833964b8b7a8126f4bc159)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicVersionNumber", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of the extension to test.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "type"))

    @type.setter
    def type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__563ec7c1482c5079e1e9794b3bd4743da435c16cc7a741b9962b2a18f2695515)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="typeName")
    def type_name(self) -> typing.Optional[builtins.str]:
        '''The name of the extension to test.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeName"))

    @type_name.setter
    def type_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ff64f615236770a749da8c076614d45c7535c8fced5b15461275638cb12afc8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeName", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnPublicTypeVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "log_delivery_bucket": "logDeliveryBucket",
        "public_version_number": "publicVersionNumber",
        "type": "type",
        "type_name": "typeName",
    },
)
class CfnPublicTypeVersionProps:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        log_delivery_bucket: typing.Optional[builtins.str] = None,
        public_version_number: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        type_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnPublicTypeVersion``.

        :param arn: The Amazon Resource Number (ARN) of the extension. Conditional: You must specify ``Arn`` , or ``TypeName`` and ``Type`` .
        :param log_delivery_bucket: The S3 bucket to which CloudFormation delivers the contract test execution logs. CloudFormation delivers the logs by the time contract testing has completed and the extension has been assigned a test type status of ``PASSED`` or ``FAILED`` . The user initiating the stack operation must be able to access items in the specified S3 bucket. Specifically, the user needs the following permissions: - GetObject - PutObject For more information, see `Actions, Resources, and Condition Keys for Amazon S3 <https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html>`_ in the *AWS Identity and Access Management User Guide* .
        :param public_version_number: The version number to assign to this version of the extension. Use the following format, and adhere to semantic versioning when assigning a version number to your extension: ``MAJOR.MINOR.PATCH`` For more information, see `Semantic Versioning 2.0.0 <https://docs.aws.amazon.com/https://semver.org/>`_ . If you don't specify a version number, CloudFormation increments the version number by one minor version release. You cannot specify a version number the first time you publish a type. AWS CloudFormation automatically sets the first version number to be ``1.0.0`` .
        :param type: The type of the extension to test. Conditional: You must specify ``Arn`` , or ``TypeName`` and ``Type`` .
        :param type_name: The name of the extension to test. Conditional: You must specify ``Arn`` , or ``TypeName`` and ``Type`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudformation as cloudformation
            
            cfn_public_type_version_props = cloudformation.CfnPublicTypeVersionProps(
                arn="arn",
                log_delivery_bucket="logDeliveryBucket",
                public_version_number="publicVersionNumber",
                type="type",
                type_name="typeName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18efb861dce8210d36272fd882e9481ecf1f7ad199bf2bf34fdd66aa24a64bc7)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument log_delivery_bucket", value=log_delivery_bucket, expected_type=type_hints["log_delivery_bucket"])
            check_type(argname="argument public_version_number", value=public_version_number, expected_type=type_hints["public_version_number"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument type_name", value=type_name, expected_type=type_hints["type_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if log_delivery_bucket is not None:
            self._values["log_delivery_bucket"] = log_delivery_bucket
        if public_version_number is not None:
            self._values["public_version_number"] = public_version_number
        if type is not None:
            self._values["type"] = type
        if type_name is not None:
            self._values["type_name"] = type_name

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Number (ARN) of the extension.

        Conditional: You must specify ``Arn`` , or ``TypeName`` and ``Type`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html#cfn-cloudformation-publictypeversion-arn
        '''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_delivery_bucket(self) -> typing.Optional[builtins.str]:
        '''The S3 bucket to which CloudFormation delivers the contract test execution logs.

        CloudFormation delivers the logs by the time contract testing has completed and the extension has been assigned a test type status of ``PASSED`` or ``FAILED`` .

        The user initiating the stack operation must be able to access items in the specified S3 bucket. Specifically, the user needs the following permissions:

        - GetObject
        - PutObject

        For more information, see `Actions, Resources, and Condition Keys for Amazon S3 <https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html>`_ in the *AWS Identity and Access Management User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html#cfn-cloudformation-publictypeversion-logdeliverybucket
        '''
        result = self._values.get("log_delivery_bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_version_number(self) -> typing.Optional[builtins.str]:
        '''The version number to assign to this version of the extension.

        Use the following format, and adhere to semantic versioning when assigning a version number to your extension:

        ``MAJOR.MINOR.PATCH``

        For more information, see `Semantic Versioning 2.0.0 <https://docs.aws.amazon.com/https://semver.org/>`_ .

        If you don't specify a version number, CloudFormation increments the version number by one minor version release.

        You cannot specify a version number the first time you publish a type. AWS CloudFormation automatically sets the first version number to be ``1.0.0`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html#cfn-cloudformation-publictypeversion-publicversionnumber
        '''
        result = self._values.get("public_version_number")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of the extension to test.

        Conditional: You must specify ``Arn`` , or ``TypeName`` and ``Type`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html#cfn-cloudformation-publictypeversion-type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type_name(self) -> typing.Optional[builtins.str]:
        '''The name of the extension to test.

        Conditional: You must specify ``Arn`` , or ``TypeName`` and ``Type`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html#cfn-cloudformation-publictypeversion-typename
        '''
        result = self._values.get("type_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPublicTypeVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnPublisher(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnPublisher",
):
    '''Registers your account as a publisher of public extensions in the CloudFormation registry.

    Public extensions are available for use by all CloudFormation users.

    For information on requirements for registering as a public extension publisher, see `Registering your account to publish CloudFormation extensions <https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-prereqs>`_ in the *CloudFormation CLI User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publisher.html
    :cloudformationResource: AWS::CloudFormation::Publisher
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudformation as cloudformation
        
        cfn_publisher = cloudformation.CfnPublisher(self, "MyCfnPublisher",
            accept_terms_and_conditions=False,
        
            # the properties below are optional
            connection_arn="connectionArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        accept_terms_and_conditions: typing.Union[builtins.bool, _IResolvable_da3f097b],
        connection_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param accept_terms_and_conditions: Whether you accept the `Terms and Conditions <https://docs.aws.amazon.com/https://cloudformation-registry-documents.s3.amazonaws.com/Terms_and_Conditions_for_AWS_CloudFormation_Registry_Publishers.pdf>`_ for publishing extensions in the CloudFormation registry. You must accept the terms and conditions in order to register to publish public extensions to the CloudFormation registry. The default is ``false`` .
        :param connection_arn: If you are using a Bitbucket or GitHub account for identity verification, the Amazon Resource Name (ARN) for your connection to that account. For more information, see `Registering your account to publish CloudFormation extensions <https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-prereqs>`_ in the *CloudFormation CLI User Guide* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98c7559405984ded6c9804bd442f72ad08edd6b60ad34619af070342a90bb1f0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPublisherProps(
            accept_terms_and_conditions=accept_terms_and_conditions,
            connection_arn=connection_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e45513940f140496d5e61d36d1bb3dcff4cc290fc725da5edc058e51f674e78)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a9eee79f0a68d58a80234313f91421f270b156d5bcb8358b8f2ffa4491e86e61)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrIdentityProvider")
    def attr_identity_provider(self) -> builtins.str:
        '''The type of account used as the identity provider when registering this publisher with CloudFormation.

        :cloudformationAttribute: IdentityProvider
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdentityProvider"))

    @builtins.property
    @jsii.member(jsii_name="attrPublisherId")
    def attr_publisher_id(self) -> builtins.str:
        '''The ID of the extension publisher.

        :cloudformationAttribute: PublisherId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPublisherId"))

    @builtins.property
    @jsii.member(jsii_name="attrPublisherProfile")
    def attr_publisher_profile(self) -> builtins.str:
        '''The URL to the publisher's profile with the identity provider.

        :cloudformationAttribute: PublisherProfile
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPublisherProfile"))

    @builtins.property
    @jsii.member(jsii_name="attrPublisherStatus")
    def attr_publisher_status(self) -> builtins.str:
        '''Whether the publisher is verified.

        Currently, all registered publishers are verified.

        :cloudformationAttribute: PublisherStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPublisherStatus"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="acceptTermsAndConditions")
    def accept_terms_and_conditions(
        self,
    ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Whether you accept the `Terms and Conditions <https://docs.aws.amazon.com/https://cloudformation-registry-documents.s3.amazonaws.com/Terms_and_Conditions_for_AWS_CloudFormation_Registry_Publishers.pdf>`_ for publishing extensions in the CloudFormation registry. You must accept the terms and conditions in order to register to publish public extensions to the CloudFormation registry.'''
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], jsii.get(self, "acceptTermsAndConditions"))

    @accept_terms_and_conditions.setter
    def accept_terms_and_conditions(
        self,
        value: typing.Union[builtins.bool, _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32926bab93b08cf2b9ba45201d6c17771f4ee56bd0d6ae22c80302acbe88d711)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceptTermsAndConditions", value)

    @builtins.property
    @jsii.member(jsii_name="connectionArn")
    def connection_arn(self) -> typing.Optional[builtins.str]:
        '''If you are using a Bitbucket or GitHub account for identity verification, the Amazon Resource Name (ARN) for your connection to that account.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionArn"))

    @connection_arn.setter
    def connection_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6543e2603954d96b676b1b073989fa0cd07d298228cd8b4ced57c2fbea3bb0c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionArn", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnPublisherProps",
    jsii_struct_bases=[],
    name_mapping={
        "accept_terms_and_conditions": "acceptTermsAndConditions",
        "connection_arn": "connectionArn",
    },
)
class CfnPublisherProps:
    def __init__(
        self,
        *,
        accept_terms_and_conditions: typing.Union[builtins.bool, _IResolvable_da3f097b],
        connection_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnPublisher``.

        :param accept_terms_and_conditions: Whether you accept the `Terms and Conditions <https://docs.aws.amazon.com/https://cloudformation-registry-documents.s3.amazonaws.com/Terms_and_Conditions_for_AWS_CloudFormation_Registry_Publishers.pdf>`_ for publishing extensions in the CloudFormation registry. You must accept the terms and conditions in order to register to publish public extensions to the CloudFormation registry. The default is ``false`` .
        :param connection_arn: If you are using a Bitbucket or GitHub account for identity verification, the Amazon Resource Name (ARN) for your connection to that account. For more information, see `Registering your account to publish CloudFormation extensions <https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-prereqs>`_ in the *CloudFormation CLI User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publisher.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudformation as cloudformation
            
            cfn_publisher_props = cloudformation.CfnPublisherProps(
                accept_terms_and_conditions=False,
            
                # the properties below are optional
                connection_arn="connectionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b41681bff4816c257b59b8947cb33afcd9050c71509e0ec07b569e949d0a9ce)
            check_type(argname="argument accept_terms_and_conditions", value=accept_terms_and_conditions, expected_type=type_hints["accept_terms_and_conditions"])
            check_type(argname="argument connection_arn", value=connection_arn, expected_type=type_hints["connection_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "accept_terms_and_conditions": accept_terms_and_conditions,
        }
        if connection_arn is not None:
            self._values["connection_arn"] = connection_arn

    @builtins.property
    def accept_terms_and_conditions(
        self,
    ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Whether you accept the `Terms and Conditions <https://docs.aws.amazon.com/https://cloudformation-registry-documents.s3.amazonaws.com/Terms_and_Conditions_for_AWS_CloudFormation_Registry_Publishers.pdf>`_ for publishing extensions in the CloudFormation registry. You must accept the terms and conditions in order to register to publish public extensions to the CloudFormation registry.

        The default is ``false`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publisher.html#cfn-cloudformation-publisher-accepttermsandconditions
        '''
        result = self._values.get("accept_terms_and_conditions")
        assert result is not None, "Required property 'accept_terms_and_conditions' is missing"
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

    @builtins.property
    def connection_arn(self) -> typing.Optional[builtins.str]:
        '''If you are using a Bitbucket or GitHub account for identity verification, the Amazon Resource Name (ARN) for your connection to that account.

        For more information, see `Registering your account to publish CloudFormation extensions <https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-prereqs>`_ in the *CloudFormation CLI User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publisher.html#cfn-cloudformation-publisher-connectionarn
        '''
        result = self._values.get("connection_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPublisherProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnResourceDefaultVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnResourceDefaultVersion",
):
    '''Specifies the default version of a resource.

    The default version of a resource will be used in CloudFormation operations.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourcedefaultversion.html
    :cloudformationResource: AWS::CloudFormation::ResourceDefaultVersion
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudformation as cloudformation
        
        cfn_resource_default_version = cloudformation.CfnResourceDefaultVersion(self, "MyCfnResourceDefaultVersion",
            type_name="typeName",
            type_version_arn="typeVersionArn",
            version_id="versionId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        type_name: typing.Optional[builtins.str] = None,
        type_version_arn: typing.Optional[builtins.str] = None,
        version_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param type_name: The name of the resource. Conditional: You must specify either ``TypeVersionArn`` , or ``TypeName`` and ``VersionId`` .
        :param type_version_arn: The Amazon Resource Name (ARN) of the resource version. Conditional: You must specify either ``TypeVersionArn`` , or ``TypeName`` and ``VersionId`` .
        :param version_id: The ID of a specific version of the resource. The version ID is the value at the end of the Amazon Resource Name (ARN) assigned to the resource version when it's registered. Conditional: You must specify either ``TypeVersionArn`` , or ``TypeName`` and ``VersionId`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3bf93b0b355aca5fb2cff6cd3ed10d995f75d3a89763b8aa05fb433f97856e9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResourceDefaultVersionProps(
            type_name=type_name,
            type_version_arn=type_version_arn,
            version_id=version_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9192b3f3f31f165283a9fef249de629eb55fb220ac568bb8c262f9f73a38647e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d693a992f8c1ba2af4ed78de5cada3f1d685f17f43921a70e1bfd549f9ac4f35)
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
        '''The Amazon Resource Name (ARN) of the resource.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="typeName")
    def type_name(self) -> typing.Optional[builtins.str]:
        '''The name of the resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeName"))

    @type_name.setter
    def type_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__718a57bf8de77237fcb8e3a281903144964b40256824b54d8e49919e59709642)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeName", value)

    @builtins.property
    @jsii.member(jsii_name="typeVersionArn")
    def type_version_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the resource version.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeVersionArn"))

    @type_version_arn.setter
    def type_version_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab644f676b15f7bed54dcb226d419de1039e4a54d60778895c53f964cc22e036)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeVersionArn", value)

    @builtins.property
    @jsii.member(jsii_name="versionId")
    def version_id(self) -> typing.Optional[builtins.str]:
        '''The ID of a specific version of the resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionId"))

    @version_id.setter
    def version_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61966d72d6d53857a7d4531e87d5aa75dd4e47794020bd350a8ad18c4a375b39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versionId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnResourceDefaultVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "type_name": "typeName",
        "type_version_arn": "typeVersionArn",
        "version_id": "versionId",
    },
)
class CfnResourceDefaultVersionProps:
    def __init__(
        self,
        *,
        type_name: typing.Optional[builtins.str] = None,
        type_version_arn: typing.Optional[builtins.str] = None,
        version_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnResourceDefaultVersion``.

        :param type_name: The name of the resource. Conditional: You must specify either ``TypeVersionArn`` , or ``TypeName`` and ``VersionId`` .
        :param type_version_arn: The Amazon Resource Name (ARN) of the resource version. Conditional: You must specify either ``TypeVersionArn`` , or ``TypeName`` and ``VersionId`` .
        :param version_id: The ID of a specific version of the resource. The version ID is the value at the end of the Amazon Resource Name (ARN) assigned to the resource version when it's registered. Conditional: You must specify either ``TypeVersionArn`` , or ``TypeName`` and ``VersionId`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourcedefaultversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudformation as cloudformation
            
            cfn_resource_default_version_props = cloudformation.CfnResourceDefaultVersionProps(
                type_name="typeName",
                type_version_arn="typeVersionArn",
                version_id="versionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__846c1092e850e7f3b08a0c0fcc29b8cda8aa8f909b3c1479b1ddc873dd053222)
            check_type(argname="argument type_name", value=type_name, expected_type=type_hints["type_name"])
            check_type(argname="argument type_version_arn", value=type_version_arn, expected_type=type_hints["type_version_arn"])
            check_type(argname="argument version_id", value=version_id, expected_type=type_hints["version_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if type_name is not None:
            self._values["type_name"] = type_name
        if type_version_arn is not None:
            self._values["type_version_arn"] = type_version_arn
        if version_id is not None:
            self._values["version_id"] = version_id

    @builtins.property
    def type_name(self) -> typing.Optional[builtins.str]:
        '''The name of the resource.

        Conditional: You must specify either ``TypeVersionArn`` , or ``TypeName`` and ``VersionId`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourcedefaultversion.html#cfn-cloudformation-resourcedefaultversion-typename
        '''
        result = self._values.get("type_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type_version_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the resource version.

        Conditional: You must specify either ``TypeVersionArn`` , or ``TypeName`` and ``VersionId`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourcedefaultversion.html#cfn-cloudformation-resourcedefaultversion-typeversionarn
        '''
        result = self._values.get("type_version_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_id(self) -> typing.Optional[builtins.str]:
        '''The ID of a specific version of the resource.

        The version ID is the value at the end of the Amazon Resource Name (ARN) assigned to the resource version when it's registered.

        Conditional: You must specify either ``TypeVersionArn`` , or ``TypeName`` and ``VersionId`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourcedefaultversion.html#cfn-cloudformation-resourcedefaultversion-versionid
        '''
        result = self._values.get("version_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourceDefaultVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnResourceVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnResourceVersion",
):
    '''Registers a resource version with the CloudFormation service.

    Registering a resource version makes it available for use in CloudFormation templates in your AWS account , and includes:

    - Validating the resource schema.
    - Determining which handlers, if any, have been specified for the resource.
    - Making the resource available for use in your account.

    For more information on how to develop resources and ready them for registration, see `Creating Resource Providers <https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-types.html>`_ in the *CloudFormation CLI User Guide* .

    You can have a maximum of 50 resource versions registered at a time. This maximum is per account and per Region.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.html
    :cloudformationResource: AWS::CloudFormation::ResourceVersion
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudformation as cloudformation
        
        cfn_resource_version = cloudformation.CfnResourceVersion(self, "MyCfnResourceVersion",
            schema_handler_package="schemaHandlerPackage",
            type_name="typeName",
        
            # the properties below are optional
            execution_role_arn="executionRoleArn",
            logging_config=cloudformation.CfnResourceVersion.LoggingConfigProperty(
                log_group_name="logGroupName",
                log_role_arn="logRoleArn"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        schema_handler_package: builtins.str,
        type_name: builtins.str,
        execution_role_arn: typing.Optional[builtins.str] = None,
        logging_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResourceVersion.LoggingConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param schema_handler_package: A URL to the S3 bucket containing the resource project package that contains the necessary files for the resource you want to register. For information on generating a schema handler package for the resource you want to register, see `submit <https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-submit.html>`_ in the *CloudFormation CLI User Guide* . .. epigraph:: The user registering the resource must be able to access the package in the S3 bucket. That is, the user needs to have `GetObject <https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html>`_ permissions for the schema handler package. For more information, see `Actions, Resources, and Condition Keys for Amazon S3 <https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazons3.html>`_ in the *AWS Identity and Access Management User Guide* .
        :param type_name: The name of the resource being registered. We recommend that resource names adhere to the following pattern: *company_or_organization* :: *service* :: *type* . .. epigraph:: The following organization namespaces are reserved and can't be used in your resource names: - ``Alexa`` - ``AMZN`` - ``Amazon`` - ``AWS`` - ``Custom`` - ``Dev``
        :param execution_role_arn: The Amazon Resource Name (ARN) of the IAM role for CloudFormation to assume when invoking the resource. If your resource calls AWS APIs in any of its handlers, you must create an *`IAM execution role <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html>`_* that includes the necessary permissions to call those AWS APIs, and provision that execution role in your account. When CloudFormation needs to invoke the resource type handler, CloudFormation assumes this execution role to create a temporary session token, which it then passes to the resource type handler, thereby supplying your resource type with the appropriate credentials.
        :param logging_config: Logging configuration information for a resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d66096cd07e25c1ed44a33ad186a98806441d15023da1aa1c7a94d39edcd36a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResourceVersionProps(
            schema_handler_package=schema_handler_package,
            type_name=type_name,
            execution_role_arn=execution_role_arn,
            logging_config=logging_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60549a7ad1c7eb301947c17673ebac8d626aa6340213be58c05eeae19db04fba)
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
            type_hints = typing.get_type_hints(_typecheckingstub__36a7bf18163fba789ff5e275f0ade4a58d9b2f895051061d8838ce4a1b9b1e7f)
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
        '''The Amazon Resource Name (ARN) of the extension.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrIsDefaultVersion")
    def attr_is_default_version(self) -> _IResolvable_da3f097b:
        '''Whether the specified extension version is set as the default version.

        This applies only to private extensions you have registered in your account, and extensions published by AWS . For public third-party extensions, whether they are activated in your account, CloudFormation returns ``null`` .

        :cloudformationAttribute: IsDefaultVersion
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrIsDefaultVersion"))

    @builtins.property
    @jsii.member(jsii_name="attrProvisioningType")
    def attr_provisioning_type(self) -> builtins.str:
        '''For resource type extensions, the provisioning behavior of the resource type.

        AWS CloudFormation determines the provisioning type during registration, based on the types of handlers in the schema handler package submitted.

        Valid values include:

        - ``FULLY_MUTABLE`` : The resource type includes an update handler to process updates to the type during stack update operations.
        - ``IMMUTABLE`` : The resource type doesn't include an update handler, so the type can't be updated and must instead be replaced during stack update operations.
        - ``NON_PROVISIONABLE`` : The resource type doesn't include all the following handlers, and therefore can't actually be provisioned.
        - create
        - read
        - delete

        :cloudformationAttribute: ProvisioningType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProvisioningType"))

    @builtins.property
    @jsii.member(jsii_name="attrTypeArn")
    def attr_type_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the extension.

        :cloudformationAttribute: TypeArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTypeArn"))

    @builtins.property
    @jsii.member(jsii_name="attrVersionId")
    def attr_version_id(self) -> builtins.str:
        '''The ID of a specific version of the extension.

        The version ID is the value at the end of the Amazon Resource Name (ARN) assigned to the extension version when it is registered.

        If you specify a ``VersionId`` , ``DescribeType`` returns information about that specific extension version. Otherwise, it returns information about the default extension version.

        :cloudformationAttribute: VersionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVersionId"))

    @builtins.property
    @jsii.member(jsii_name="attrVisibility")
    def attr_visibility(self) -> builtins.str:
        '''The scope at which the extension is visible and usable in CloudFormation operations.

        Valid values include:

        - ``PRIVATE`` : The extension is only visible and usable within the account in which it is registered. AWS CloudFormation marks any extensions you register as ``PRIVATE`` .
        - ``PUBLIC`` : The extension is publicly visible and usable within any AWS account.

        :cloudformationAttribute: Visibility
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVisibility"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="schemaHandlerPackage")
    def schema_handler_package(self) -> builtins.str:
        '''A URL to the S3 bucket containing the resource project package that contains the necessary files for the resource you want to register.'''
        return typing.cast(builtins.str, jsii.get(self, "schemaHandlerPackage"))

    @schema_handler_package.setter
    def schema_handler_package(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6453c003449eb4a7a620fb123fab02f5fe5eda20f32be06eedb8b960f14e5712)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaHandlerPackage", value)

    @builtins.property
    @jsii.member(jsii_name="typeName")
    def type_name(self) -> builtins.str:
        '''The name of the resource being registered.'''
        return typing.cast(builtins.str, jsii.get(self, "typeName"))

    @type_name.setter
    def type_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0d9e6b661355ce1ff1ffffe546827ed841f6351c4e62546fec58209ff877652)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeName", value)

    @builtins.property
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the IAM role for CloudFormation to assume when invoking the resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleArn"))

    @execution_role_arn.setter
    def execution_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f0b504fce536426ab9358d45f97b10ff78e173eefae7559f1499cca14b266df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="loggingConfig")
    def logging_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceVersion.LoggingConfigProperty"]]:
        '''Logging configuration information for a resource.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceVersion.LoggingConfigProperty"]], jsii.get(self, "loggingConfig"))

    @logging_config.setter
    def logging_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceVersion.LoggingConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3815df35f78faddb4478e4806caabc98c6e3b931d83cb9b1f05419da5399cb86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loggingConfig", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudformation.CfnResourceVersion.LoggingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group_name": "logGroupName", "log_role_arn": "logRoleArn"},
    )
    class LoggingConfigProperty:
        def __init__(
            self,
            *,
            log_group_name: typing.Optional[builtins.str] = None,
            log_role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Logging configuration information for a resource.

            :param log_group_name: The Amazon CloudWatch logs group to which CloudFormation sends error logging information when invoking the type's handlers.
            :param log_role_arn: The ARN of the role that CloudFormation should assume when sending log entries to CloudWatch logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-resourceversion-loggingconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudformation as cloudformation
                
                logging_config_property = cloudformation.CfnResourceVersion.LoggingConfigProperty(
                    log_group_name="logGroupName",
                    log_role_arn="logRoleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c68df5722a00d70d4751ceb1afcfb299c59a8b40faaeb3723d5c834184072cdf)
                check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
                check_type(argname="argument log_role_arn", value=log_role_arn, expected_type=type_hints["log_role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if log_group_name is not None:
                self._values["log_group_name"] = log_group_name
            if log_role_arn is not None:
                self._values["log_role_arn"] = log_role_arn

        @builtins.property
        def log_group_name(self) -> typing.Optional[builtins.str]:
            '''The Amazon CloudWatch logs group to which CloudFormation sends error logging information when invoking the type's handlers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-resourceversion-loggingconfig.html#cfn-cloudformation-resourceversion-loggingconfig-loggroupname
            '''
            result = self._values.get("log_group_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def log_role_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the role that CloudFormation should assume when sending log entries to CloudWatch logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-resourceversion-loggingconfig.html#cfn-cloudformation-resourceversion-loggingconfig-logrolearn
            '''
            result = self._values.get("log_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnResourceVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "schema_handler_package": "schemaHandlerPackage",
        "type_name": "typeName",
        "execution_role_arn": "executionRoleArn",
        "logging_config": "loggingConfig",
    },
)
class CfnResourceVersionProps:
    def __init__(
        self,
        *,
        schema_handler_package: builtins.str,
        type_name: builtins.str,
        execution_role_arn: typing.Optional[builtins.str] = None,
        logging_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceVersion.LoggingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnResourceVersion``.

        :param schema_handler_package: A URL to the S3 bucket containing the resource project package that contains the necessary files for the resource you want to register. For information on generating a schema handler package for the resource you want to register, see `submit <https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-submit.html>`_ in the *CloudFormation CLI User Guide* . .. epigraph:: The user registering the resource must be able to access the package in the S3 bucket. That is, the user needs to have `GetObject <https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html>`_ permissions for the schema handler package. For more information, see `Actions, Resources, and Condition Keys for Amazon S3 <https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazons3.html>`_ in the *AWS Identity and Access Management User Guide* .
        :param type_name: The name of the resource being registered. We recommend that resource names adhere to the following pattern: *company_or_organization* :: *service* :: *type* . .. epigraph:: The following organization namespaces are reserved and can't be used in your resource names: - ``Alexa`` - ``AMZN`` - ``Amazon`` - ``AWS`` - ``Custom`` - ``Dev``
        :param execution_role_arn: The Amazon Resource Name (ARN) of the IAM role for CloudFormation to assume when invoking the resource. If your resource calls AWS APIs in any of its handlers, you must create an *`IAM execution role <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html>`_* that includes the necessary permissions to call those AWS APIs, and provision that execution role in your account. When CloudFormation needs to invoke the resource type handler, CloudFormation assumes this execution role to create a temporary session token, which it then passes to the resource type handler, thereby supplying your resource type with the appropriate credentials.
        :param logging_config: Logging configuration information for a resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudformation as cloudformation
            
            cfn_resource_version_props = cloudformation.CfnResourceVersionProps(
                schema_handler_package="schemaHandlerPackage",
                type_name="typeName",
            
                # the properties below are optional
                execution_role_arn="executionRoleArn",
                logging_config=cloudformation.CfnResourceVersion.LoggingConfigProperty(
                    log_group_name="logGroupName",
                    log_role_arn="logRoleArn"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76ca3cbb367679516480c68e4d53a4abc20cb7d02f8a591754eb2f715e9c58e7)
            check_type(argname="argument schema_handler_package", value=schema_handler_package, expected_type=type_hints["schema_handler_package"])
            check_type(argname="argument type_name", value=type_name, expected_type=type_hints["type_name"])
            check_type(argname="argument execution_role_arn", value=execution_role_arn, expected_type=type_hints["execution_role_arn"])
            check_type(argname="argument logging_config", value=logging_config, expected_type=type_hints["logging_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "schema_handler_package": schema_handler_package,
            "type_name": type_name,
        }
        if execution_role_arn is not None:
            self._values["execution_role_arn"] = execution_role_arn
        if logging_config is not None:
            self._values["logging_config"] = logging_config

    @builtins.property
    def schema_handler_package(self) -> builtins.str:
        '''A URL to the S3 bucket containing the resource project package that contains the necessary files for the resource you want to register.

        For information on generating a schema handler package for the resource you want to register, see `submit <https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-submit.html>`_ in the *CloudFormation CLI User Guide* .
        .. epigraph::

           The user registering the resource must be able to access the package in the S3 bucket. That is, the user needs to have `GetObject <https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html>`_ permissions for the schema handler package. For more information, see `Actions, Resources, and Condition Keys for Amazon S3 <https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazons3.html>`_ in the *AWS Identity and Access Management User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.html#cfn-cloudformation-resourceversion-schemahandlerpackage
        '''
        result = self._values.get("schema_handler_package")
        assert result is not None, "Required property 'schema_handler_package' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type_name(self) -> builtins.str:
        '''The name of the resource being registered.

        We recommend that resource names adhere to the following pattern: *company_or_organization* :: *service* :: *type* .
        .. epigraph::

           The following organization namespaces are reserved and can't be used in your resource names:

           - ``Alexa``
           - ``AMZN``
           - ``Amazon``
           - ``AWS``
           - ``Custom``
           - ``Dev``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.html#cfn-cloudformation-resourceversion-typename
        '''
        result = self._values.get("type_name")
        assert result is not None, "Required property 'type_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the IAM role for CloudFormation to assume when invoking the resource.

        If your resource calls AWS APIs in any of its handlers, you must create an *`IAM execution role <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html>`_* that includes the necessary permissions to call those AWS APIs, and provision that execution role in your account. When CloudFormation needs to invoke the resource type handler, CloudFormation assumes this execution role to create a temporary session token, which it then passes to the resource type handler, thereby supplying your resource type with the appropriate credentials.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.html#cfn-cloudformation-resourceversion-executionrolearn
        '''
        result = self._values.get("execution_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnResourceVersion.LoggingConfigProperty]]:
        '''Logging configuration information for a resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.html#cfn-cloudformation-resourceversion-loggingconfig
        '''
        result = self._values.get("logging_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnResourceVersion.LoggingConfigProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourceVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnStack(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnStack",
):
    '''The ``AWS::CloudFormation::Stack`` resource nests a stack as a resource in a top-level template.

    You can add output values from a nested stack within the containing template. You use the `GetAtt <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html>`_ function with the nested stack's logical name and the name of the output value in the nested stack in the format ``Outputs. *NestedStackOutputName*`` .
    .. epigraph::

       We strongly recommend that updates to nested stacks are run from the parent stack.

    When you apply template changes to update a top-level stack, CloudFormation updates the top-level stack and initiates an update to its nested stacks. CloudFormation updates the resources of modified nested stacks, but doesn't update the resources of unmodified nested stacks. For more information, see `CloudFormation stack updates <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks.html>`_ .
    .. epigraph::

       You must acknowledge IAM capabilities for nested stacks that contain IAM resources. Also, verify that you have cancel update stack permissions, which is required if an update rolls back. For more information about IAM and CloudFormation , see `Controlling access with AWS Identity and Access Management <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html>`_ . > A subset of ``AWS::CloudFormation::Stack`` resource type properties listed below are available to customers using AWS CloudFormation , AWS CDK , and AWS Cloud Control API to configure.

       - ``NotificationARNs``
       - ``Parameters``
       - ``Tags``
       - ``TemplateURL``
       - ``TimeoutInMinutes``

       These properties can be configured only when using AWS Cloud Control API . This is because the below properties are set by the parent stack, and thus cannot be configured using AWS CloudFormation or AWS CDK but only AWS Cloud Control API .

       - ``Capabilities``
       - ``Description``
       - ``DisableRollback``
       - ``EnableTerminationProtection``
       - ``RoleARN``
       - ``StackName``
       - ``StackPolicyBody``
       - ``StackPolicyURL``
       - ``StackStatusReason``
       - ``TemplateBody``

       Customers that configure ``AWS::CloudFormation::Stack`` using AWS CloudFormation and AWS CDK can do so for nesting a CloudFormation stack as a resource in their top-level template.

       These read-only properties can be accessed only when using AWS Cloud Control API .

       - ``ChangeSetId``
       - ``CreationTime``
       - ``LastUpdateTime``
       - ``Outputs``
       - ``ParentId``
       - ``RootId``
       - ``StackId``
       - ``StackStatus``

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stack.html
    :cloudformationResource: AWS::CloudFormation::Stack
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudformation as cloudformation
        
        cfn_stack = cloudformation.CfnStack(self, "MyCfnStack",
            notification_arns=["notificationArns"],
            parameters={
                "parameters_key": "parameters"
            },
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            template_url="templateUrl",
            timeout_in_minutes=123
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        notification_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        template_url: typing.Optional[builtins.str] = None,
        timeout_in_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param notification_arns: The Amazon Simple Notification Service (Amazon SNS) topic ARNs to publish stack related events. You can find your Amazon SNS topic ARNs using the Amazon SNS console or your Command Line Interface (CLI).
        :param parameters: The set value pairs that represent the parameters passed to CloudFormation when this nested stack is created. Each parameter has a name corresponding to a parameter defined in the embedded template and a value representing the value that you want to set for the parameter. .. epigraph:: If you use the ``Ref`` function to pass a parameter value to a nested stack, comma-delimited list parameters must be of type ``String`` . In other words, you can't pass values that are of type ``CommaDelimitedList`` to nested stacks. Conditional. Required if the nested stack requires input parameters. Whether an update causes interruptions depends on the resources that are being updated. An update never causes a nested stack to be replaced.
        :param tags: Key-value pairs to associate with this stack. AWS CloudFormation also propagates these tags to the resources created in the stack. A maximum number of 50 tags can be specified.
        :param template_url: Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that's located in an Amazon S3 bucket. For more information, see `Template anatomy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html>`_ . Whether an update causes interruptions depends on the resources that are being updated. An update never causes a nested stack to be replaced.
        :param timeout_in_minutes: The length of time, in minutes, that CloudFormation waits for the nested stack to reach the ``CREATE_COMPLETE`` state. The default is no timeout. When CloudFormation detects that the nested stack has reached the ``CREATE_COMPLETE`` state, it marks the nested stack resource as ``CREATE_COMPLETE`` in the parent stack and resumes creating the parent stack. If the timeout period expires before the nested stack reaches ``CREATE_COMPLETE`` , CloudFormation marks the nested stack as failed and rolls back both the nested stack and parent stack. Updates aren't supported.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b03b296829d4f2eb356ceeb892ed7d61908e69c4949bd797def9d9980897a1a1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStackProps(
            notification_arns=notification_arns,
            parameters=parameters,
            tags=tags,
            template_url=template_url,
            timeout_in_minutes=timeout_in_minutes,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca2eeeb5a2fc247c87aa885f14161d88b2b7db47ce5a176bee9ba83f61e8447d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6d5f666653aae50479803ed71839253ef19c348c5240cb3bebb449b6e150d007)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrChangeSetId")
    def attr_change_set_id(self) -> builtins.str:
        '''Returns the unique ID of the change set.

        :cloudformationAttribute: ChangeSetId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrChangeSetId"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''Returns The time at which the stack was created.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdateTime")
    def attr_last_update_time(self) -> builtins.str:
        '''Returns the time the stack was last updated.

        This will only be returned if the stack has been updated at least once.

        :cloudformationAttribute: LastUpdateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdateTime"))

    @builtins.property
    @jsii.member(jsii_name="attrOutputs")
    def attr_outputs(self) -> _IResolvable_da3f097b:
        '''Returns a list of output structures.

        :cloudformationAttribute: Outputs
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrOutputs"))

    @builtins.property
    @jsii.member(jsii_name="attrParentId")
    def attr_parent_id(self) -> builtins.str:
        '''For nested stacks--stacks created as resources for another stack--returns the stack ID of the direct parent of this stack.

        For the first level of nested stacks, the root stack is also the parent stack.

        For more information, see `Working with Nested Stacks <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html>`_ in the *AWS CloudFormation User Guide* .

        :cloudformationAttribute: ParentId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrParentId"))

    @builtins.property
    @jsii.member(jsii_name="attrRootId")
    def attr_root_id(self) -> builtins.str:
        '''For nested stacks--stacks created as resources for another stack--returns the stack ID of the top-level stack to which the nested stack ultimately belongs.

        For more information, see `Working with Nested Stacks <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html>`_ in the *AWS CloudFormation User Guide* .

        :cloudformationAttribute: RootId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRootId"))

    @builtins.property
    @jsii.member(jsii_name="attrStackId")
    def attr_stack_id(self) -> builtins.str:
        '''Returns the unique identifier of the stack.

        :cloudformationAttribute: StackId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStackId"))

    @builtins.property
    @jsii.member(jsii_name="attrStackStatus")
    def attr_stack_status(self) -> builtins.str:
        '''Returns a success or failure message associated with the stack status.

        :cloudformationAttribute: StackStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStackStatus"))

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
    @jsii.member(jsii_name="notificationArns")
    def notification_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Amazon Simple Notification Service (Amazon SNS) topic ARNs to publish stack related events.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "notificationArns"))

    @notification_arns.setter
    def notification_arns(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d66d5e1fe390793c13ae8f3762505ddcb7c4e44a03b219a7d65987bc8ac48d68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationArns", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''The set value pairs that represent the parameters passed to CloudFormation when this nested stack is created.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26855905eda83610dba6ef5eae36ae6d595846a274f432b31c16b01c431139bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Key-value pairs to associate with this stack.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3dd6f2b6a16bc08db2d10b1a6eff5f64991fe724d61645874b4235a7f2816089)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="templateUrl")
    def template_url(self) -> typing.Optional[builtins.str]:
        '''Location of file containing the template body.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateUrl"))

    @template_url.setter
    def template_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3db469b6ac2b6930a53773a7067f28dcbe494d1c4c0aa67dc9ab276d28d07904)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateUrl", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutInMinutes")
    def timeout_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''The length of time, in minutes, that CloudFormation waits for the nested stack to reach the ``CREATE_COMPLETE`` state.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutInMinutes"))

    @timeout_in_minutes.setter
    def timeout_in_minutes(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c9f0cec1de29739b017def3b496f6e5bf888854e8a565ee7e2a8695868506eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutInMinutes", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudformation.CfnStack.OutputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "description": "description",
            "export_name": "exportName",
            "output_key": "outputKey",
            "output_value": "outputValue",
        },
    )
    class OutputProperty:
        def __init__(
            self,
            *,
            description: typing.Optional[builtins.str] = None,
            export_name: typing.Optional[builtins.str] = None,
            output_key: typing.Optional[builtins.str] = None,
            output_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The Output data type.

            :param description: User defined description associated with the output.
            :param export_name: The name of the export associated with the output.
            :param output_key: The key associated with the output.
            :param output_value: The value associated with the output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stack-output.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudformation as cloudformation
                
                output_property = cloudformation.CfnStack.OutputProperty(
                    description="description",
                    export_name="exportName",
                    output_key="outputKey",
                    output_value="outputValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a4b95d92bea1984ce15e37fa304b047ed771a4f764d414ffac328157423828dc)
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument export_name", value=export_name, expected_type=type_hints["export_name"])
                check_type(argname="argument output_key", value=output_key, expected_type=type_hints["output_key"])
                check_type(argname="argument output_value", value=output_value, expected_type=type_hints["output_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if description is not None:
                self._values["description"] = description
            if export_name is not None:
                self._values["export_name"] = export_name
            if output_key is not None:
                self._values["output_key"] = output_key
            if output_value is not None:
                self._values["output_value"] = output_value

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''User defined description associated with the output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stack-output.html#cfn-cloudformation-stack-output-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def export_name(self) -> typing.Optional[builtins.str]:
            '''The name of the export associated with the output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stack-output.html#cfn-cloudformation-stack-output-exportname
            '''
            result = self._values.get("export_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def output_key(self) -> typing.Optional[builtins.str]:
            '''The key associated with the output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stack-output.html#cfn-cloudformation-stack-output-outputkey
            '''
            result = self._values.get("output_key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def output_value(self) -> typing.Optional[builtins.str]:
            '''The value associated with the output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stack-output.html#cfn-cloudformation-stack-output-outputvalue
            '''
            result = self._values.get("output_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnStackProps",
    jsii_struct_bases=[],
    name_mapping={
        "notification_arns": "notificationArns",
        "parameters": "parameters",
        "tags": "tags",
        "template_url": "templateUrl",
        "timeout_in_minutes": "timeoutInMinutes",
    },
)
class CfnStackProps:
    def __init__(
        self,
        *,
        notification_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        template_url: typing.Optional[builtins.str] = None,
        timeout_in_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``CfnStack``.

        :param notification_arns: The Amazon Simple Notification Service (Amazon SNS) topic ARNs to publish stack related events. You can find your Amazon SNS topic ARNs using the Amazon SNS console or your Command Line Interface (CLI).
        :param parameters: The set value pairs that represent the parameters passed to CloudFormation when this nested stack is created. Each parameter has a name corresponding to a parameter defined in the embedded template and a value representing the value that you want to set for the parameter. .. epigraph:: If you use the ``Ref`` function to pass a parameter value to a nested stack, comma-delimited list parameters must be of type ``String`` . In other words, you can't pass values that are of type ``CommaDelimitedList`` to nested stacks. Conditional. Required if the nested stack requires input parameters. Whether an update causes interruptions depends on the resources that are being updated. An update never causes a nested stack to be replaced.
        :param tags: Key-value pairs to associate with this stack. AWS CloudFormation also propagates these tags to the resources created in the stack. A maximum number of 50 tags can be specified.
        :param template_url: Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that's located in an Amazon S3 bucket. For more information, see `Template anatomy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html>`_ . Whether an update causes interruptions depends on the resources that are being updated. An update never causes a nested stack to be replaced.
        :param timeout_in_minutes: The length of time, in minutes, that CloudFormation waits for the nested stack to reach the ``CREATE_COMPLETE`` state. The default is no timeout. When CloudFormation detects that the nested stack has reached the ``CREATE_COMPLETE`` state, it marks the nested stack resource as ``CREATE_COMPLETE`` in the parent stack and resumes creating the parent stack. If the timeout period expires before the nested stack reaches ``CREATE_COMPLETE`` , CloudFormation marks the nested stack as failed and rolls back both the nested stack and parent stack. Updates aren't supported.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stack.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudformation as cloudformation
            
            cfn_stack_props = cloudformation.CfnStackProps(
                notification_arns=["notificationArns"],
                parameters={
                    "parameters_key": "parameters"
                },
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                template_url="templateUrl",
                timeout_in_minutes=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4da59ffe076e92fe1011ac29ca869d93a69d1442f3b7a0d1c765cca951d09b20)
            check_type(argname="argument notification_arns", value=notification_arns, expected_type=type_hints["notification_arns"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument template_url", value=template_url, expected_type=type_hints["template_url"])
            check_type(argname="argument timeout_in_minutes", value=timeout_in_minutes, expected_type=type_hints["timeout_in_minutes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if notification_arns is not None:
            self._values["notification_arns"] = notification_arns
        if parameters is not None:
            self._values["parameters"] = parameters
        if tags is not None:
            self._values["tags"] = tags
        if template_url is not None:
            self._values["template_url"] = template_url
        if timeout_in_minutes is not None:
            self._values["timeout_in_minutes"] = timeout_in_minutes

    @builtins.property
    def notification_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Amazon Simple Notification Service (Amazon SNS) topic ARNs to publish stack related events.

        You can find your Amazon SNS topic ARNs using the Amazon SNS console or your Command Line Interface (CLI).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stack.html#cfn-cloudformation-stack-notificationarns
        '''
        result = self._values.get("notification_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''The set value pairs that represent the parameters passed to CloudFormation when this nested stack is created.

        Each parameter has a name corresponding to a parameter defined in the embedded template and a value representing the value that you want to set for the parameter.
        .. epigraph::

           If you use the ``Ref`` function to pass a parameter value to a nested stack, comma-delimited list parameters must be of type ``String`` . In other words, you can't pass values that are of type ``CommaDelimitedList`` to nested stacks.

        Conditional. Required if the nested stack requires input parameters.

        Whether an update causes interruptions depends on the resources that are being updated. An update never causes a nested stack to be replaced.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stack.html#cfn-cloudformation-stack-parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Key-value pairs to associate with this stack.

        AWS CloudFormation also propagates these tags to the resources created in the stack. A maximum number of 50 tags can be specified.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stack.html#cfn-cloudformation-stack-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def template_url(self) -> typing.Optional[builtins.str]:
        '''Location of file containing the template body.

        The URL must point to a template (max size: 460,800 bytes) that's located in an Amazon S3 bucket. For more information, see `Template anatomy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html>`_ .

        Whether an update causes interruptions depends on the resources that are being updated. An update never causes a nested stack to be replaced.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stack.html#cfn-cloudformation-stack-templateurl
        '''
        result = self._values.get("template_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''The length of time, in minutes, that CloudFormation waits for the nested stack to reach the ``CREATE_COMPLETE`` state.

        The default is no timeout. When CloudFormation detects that the nested stack has reached the ``CREATE_COMPLETE`` state, it marks the nested stack resource as ``CREATE_COMPLETE`` in the parent stack and resumes creating the parent stack. If the timeout period expires before the nested stack reaches ``CREATE_COMPLETE`` , CloudFormation marks the nested stack as failed and rolls back both the nested stack and parent stack.

        Updates aren't supported.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stack.html#cfn-cloudformation-stack-timeoutinminutes
        '''
        result = self._values.get("timeout_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStackProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnStackSet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnStackSet",
):
    '''The ``AWS::CloudFormation::StackSet`` enables you to provision stacks into AWS accounts and across Regions by using a single CloudFormation template.

    In the stack set, you specify the template to use, in addition to any parameters and capabilities that the template requires.
    .. epigraph::

       Run deployments to nested StackSets from the parent stack, not directly through the StackSet API.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html
    :cloudformationResource: AWS::CloudFormation::StackSet
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudformation as cloudformation
        
        # managed_execution: Any
        
        cfn_stack_set = cloudformation.CfnStackSet(self, "MyCfnStackSet",
            permission_model="permissionModel",
            stack_set_name="stackSetName",
        
            # the properties below are optional
            administration_role_arn="administrationRoleArn",
            auto_deployment=cloudformation.CfnStackSet.AutoDeploymentProperty(
                enabled=False,
                retain_stacks_on_account_removal=False
            ),
            call_as="callAs",
            capabilities=["capabilities"],
            description="description",
            execution_role_name="executionRoleName",
            managed_execution=managed_execution,
            operation_preferences=cloudformation.CfnStackSet.OperationPreferencesProperty(
                failure_tolerance_count=123,
                failure_tolerance_percentage=123,
                max_concurrent_count=123,
                max_concurrent_percentage=123,
                region_concurrency_type="regionConcurrencyType",
                region_order=["regionOrder"]
            ),
            parameters=[cloudformation.CfnStackSet.ParameterProperty(
                parameter_key="parameterKey",
                parameter_value="parameterValue"
            )],
            stack_instances_group=[cloudformation.CfnStackSet.StackInstancesProperty(
                deployment_targets=cloudformation.CfnStackSet.DeploymentTargetsProperty(
                    account_filter_type="accountFilterType",
                    accounts=["accounts"],
                    accounts_url="accountsUrl",
                    organizational_unit_ids=["organizationalUnitIds"]
                ),
                regions=["regions"],
        
                # the properties below are optional
                parameter_overrides=[cloudformation.CfnStackSet.ParameterProperty(
                    parameter_key="parameterKey",
                    parameter_value="parameterValue"
                )]
            )],
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            template_body="templateBody",
            template_url="templateUrl"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        permission_model: builtins.str,
        stack_set_name: builtins.str,
        administration_role_arn: typing.Optional[builtins.str] = None,
        auto_deployment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStackSet.AutoDeploymentProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        call_as: typing.Optional[builtins.str] = None,
        capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        execution_role_name: typing.Optional[builtins.str] = None,
        managed_execution: typing.Any = None,
        operation_preferences: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStackSet.OperationPreferencesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStackSet.ParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        stack_instances_group: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStackSet.StackInstancesProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        template_body: typing.Optional[builtins.str] = None,
        template_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param permission_model: Describes how the IAM roles required for stack set operations are created. - With ``SELF_MANAGED`` permissions, you must create the administrator and execution roles required to deploy to target accounts. For more information, see `Grant Self-Managed Stack Set Permissions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html>`_ . - With ``SERVICE_MANAGED`` permissions, StackSets automatically creates the IAM roles required to deploy to accounts managed by AWS Organizations .
        :param stack_set_name: The name to associate with the stack set. The name must be unique in the Region where you create your stack set. .. epigraph:: The ``StackSetName`` property is required.
        :param administration_role_arn: The Amazon Resource Number (ARN) of the IAM role to use to create this stack set. Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account. Use customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account. For more information, see `Prerequisites: Granting Permissions for Stack Set Operations <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html>`_ in the *AWS CloudFormation User Guide* . *Minimum* : ``20`` *Maximum* : ``2048``
        :param auto_deployment: [ ``Service-managed`` permissions] Describes whether StackSets automatically deploys to AWS Organizations accounts that are added to a target organization or organizational unit (OU).
        :param call_as: [Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account. By default, ``SELF`` is specified. Use ``SELF`` for stack sets with self-managed permissions. - To create a stack set with service-managed permissions while signed in to the management account, specify ``SELF`` . - To create a stack set with service-managed permissions while signed in to a delegated administrator account, specify ``DELEGATED_ADMIN`` . Your AWS account must be registered as a delegated admin in the management account. For more information, see `Register a delegated administrator <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html>`_ in the *AWS CloudFormation User Guide* . Stack sets with service-managed permissions are created in the management account, including stack sets that are created by delegated administrators. *Valid Values* : ``SELF`` | ``DELEGATED_ADMIN``
        :param capabilities: The capabilities that are allowed in the stack set. Some stack set templates might include resources that can affect permissions in your AWS account —for example, by creating new AWS Identity and Access Management ( IAM ) users. For more information, see `Acknowledging IAM Resources in AWS CloudFormation Templates <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities>`_ .
        :param description: A description of the stack set. *Minimum* : ``1`` *Maximum* : ``1024``
        :param execution_role_name: The name of the IAM execution role to use to create the stack set. If you don't specify an execution role, AWS CloudFormation uses the ``AWSCloudFormationStackSetExecutionRole`` role for the stack set operation. *Minimum* : ``1`` *Maximum* : ``64`` *Pattern* : ``[a-zA-Z_0-9+=,.@-]+``
        :param managed_execution: Describes whether StackSets performs non-conflicting operations concurrently and queues conflicting operations. When active, StackSets performs non-conflicting operations concurrently and queues conflicting operations. After conflicting operations finish, StackSets starts queued operations in request order. .. epigraph:: If there are already running or queued operations, StackSets queues all incoming operations even if they are non-conflicting. You can't modify your stack set's execution configuration while there are running or queued operations for that stack set. When inactive (default), StackSets performs one operation at a time in request order.
        :param operation_preferences: The user-specified preferences for how AWS CloudFormation performs a stack set operation.
        :param parameters: The input parameters for the stack set template.
        :param stack_instances_group: A group of stack instances with parameters in some specific accounts and Regions.
        :param tags: Key-value pairs to associate with this stack. AWS CloudFormation also propagates these tags to supported resources in the stack. You can specify a maximum number of 50 tags. If you don't specify this parameter, AWS CloudFormation doesn't modify the stack's tags. If you specify an empty value, AWS CloudFormation removes all associated tags.
        :param template_body: The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes. You must include either ``TemplateURL`` or ``TemplateBody`` in a StackSet, but you can't use both. Dynamic references in the ``TemplateBody`` may not work correctly in all cases. It's recommended to pass templates containing dynamic references through ``TemplateUrl`` instead.
        :param template_url: Location of file containing the template body. The URL must point to a template that's located in an Amazon S3 bucket or a Systems Manager document. For more information, go to `Template Anatomy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html>`_ in the AWS CloudFormation User Guide. Conditional: You must specify only one of the following parameters: ``TemplateBody`` , ``TemplateURL`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d9c85250c99fa8473d88e65c23c7c33031b75b34da26e2bece38ee28bd4570d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStackSetProps(
            permission_model=permission_model,
            stack_set_name=stack_set_name,
            administration_role_arn=administration_role_arn,
            auto_deployment=auto_deployment,
            call_as=call_as,
            capabilities=capabilities,
            description=description,
            execution_role_name=execution_role_name,
            managed_execution=managed_execution,
            operation_preferences=operation_preferences,
            parameters=parameters,
            stack_instances_group=stack_instances_group,
            tags=tags,
            template_body=template_body,
            template_url=template_url,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9afdd61cd9e49c077776e3c47082aee5db8792a3554b6cea078228185d569d6a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e04deb7ddb1fd06f6839d126c919fa0cce705f8816507397905c57e8dd9fb641)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrStackSetId")
    def attr_stack_set_id(self) -> builtins.str:
        '''The ID of the stack that you're creating.

        :cloudformationAttribute: StackSetId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStackSetId"))

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
    @jsii.member(jsii_name="permissionModel")
    def permission_model(self) -> builtins.str:
        '''Describes how the IAM roles required for stack set operations are created.'''
        return typing.cast(builtins.str, jsii.get(self, "permissionModel"))

    @permission_model.setter
    def permission_model(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af07bb659e1916cfa80a5d7739b21b36137879be79a124fe5e7e5c4b846c0d79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionModel", value)

    @builtins.property
    @jsii.member(jsii_name="stackSetName")
    def stack_set_name(self) -> builtins.str:
        '''The name to associate with the stack set.'''
        return typing.cast(builtins.str, jsii.get(self, "stackSetName"))

    @stack_set_name.setter
    def stack_set_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2170c9fd24e7b05da9100bc462024b7ef6f36eefa874a1721b6ca5397bc20040)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stackSetName", value)

    @builtins.property
    @jsii.member(jsii_name="administrationRoleArn")
    def administration_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Number (ARN) of the IAM role to use to create this stack set.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "administrationRoleArn"))

    @administration_role_arn.setter
    def administration_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33df1da68b9c62c99e1841856f4e201c8673ded83161a46959a6d5be71752562)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "administrationRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="autoDeployment")
    def auto_deployment(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStackSet.AutoDeploymentProperty"]]:
        '''[ ``Service-managed`` permissions] Describes whether StackSets automatically deploys to AWS Organizations accounts that are added to a target organization or organizational unit (OU).'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStackSet.AutoDeploymentProperty"]], jsii.get(self, "autoDeployment"))

    @auto_deployment.setter
    def auto_deployment(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStackSet.AutoDeploymentProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54972dd81830154ffcce6337f1843df37216b662ea86b869d79741b5fb9a365f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoDeployment", value)

    @builtins.property
    @jsii.member(jsii_name="callAs")
    def call_as(self) -> typing.Optional[builtins.str]:
        '''[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "callAs"))

    @call_as.setter
    def call_as(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e37b8025b5d58e66ec74873bd5eca7e1c4982e35f5495263ae5ce603d1a59b16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "callAs", value)

    @builtins.property
    @jsii.member(jsii_name="capabilities")
    def capabilities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The capabilities that are allowed in the stack set.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "capabilities"))

    @capabilities.setter
    def capabilities(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__457467a4ee010a847f5a2f2eb373eb377a8870a7bb69910d54b5b28dfcb498c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capabilities", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the stack set.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a32b31569df72cb9c92223c05aae5461caf7d1b5669b21d2dd4487ac16d68be9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="executionRoleName")
    def execution_role_name(self) -> typing.Optional[builtins.str]:
        '''The name of the IAM execution role to use to create the stack set.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleName"))

    @execution_role_name.setter
    def execution_role_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f336a94333318f89c159203981959dd1aa89598228f5e8eff09903e2d7e979cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRoleName", value)

    @builtins.property
    @jsii.member(jsii_name="managedExecution")
    def managed_execution(self) -> typing.Any:
        '''Describes whether StackSets performs non-conflicting operations concurrently and queues conflicting operations.'''
        return typing.cast(typing.Any, jsii.get(self, "managedExecution"))

    @managed_execution.setter
    def managed_execution(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30ba7de0572ec3972439a2234107f74e54796d853ad6a78e334871adc49c4a4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedExecution", value)

    @builtins.property
    @jsii.member(jsii_name="operationPreferences")
    def operation_preferences(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStackSet.OperationPreferencesProperty"]]:
        '''The user-specified preferences for how AWS CloudFormation performs a stack set operation.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStackSet.OperationPreferencesProperty"]], jsii.get(self, "operationPreferences"))

    @operation_preferences.setter
    def operation_preferences(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStackSet.OperationPreferencesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2de21d60faf97e0417df4f6303d7a41a79560cd81bde48a6dc39d8691c07faec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operationPreferences", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStackSet.ParameterProperty"]]]]:
        '''The input parameters for the stack set template.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStackSet.ParameterProperty"]]]], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStackSet.ParameterProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ce7162bef5c53321e37524df11a58f9e340a790ef5107072f3d51f53e536408)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="stackInstancesGroup")
    def stack_instances_group(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStackSet.StackInstancesProperty"]]]]:
        '''A group of stack instances with parameters in some specific accounts and Regions.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStackSet.StackInstancesProperty"]]]], jsii.get(self, "stackInstancesGroup"))

    @stack_instances_group.setter
    def stack_instances_group(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStackSet.StackInstancesProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__968f546c0d5d9567cdb455e2836771e7127fd2fd09a1168bff825cbffc5698b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stackInstancesGroup", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Key-value pairs to associate with this stack.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd51501bb9559b68fef458b291af8ba7df88b39b9154b44b83c19b21f0d65c10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="templateBody")
    def template_body(self) -> typing.Optional[builtins.str]:
        '''The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateBody"))

    @template_body.setter
    def template_body(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43c92b7fcde86d072f3926d26396619d841d2e70e1e98fbdac9e78b9ea67ef8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateBody", value)

    @builtins.property
    @jsii.member(jsii_name="templateUrl")
    def template_url(self) -> typing.Optional[builtins.str]:
        '''Location of file containing the template body.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateUrl"))

    @template_url.setter
    def template_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a294c8f5426fcf440746cb77033834a63ea811fbda12ac428bfda3503123c28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateUrl", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudformation.CfnStackSet.AutoDeploymentProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enabled": "enabled",
            "retain_stacks_on_account_removal": "retainStacksOnAccountRemoval",
        },
    )
    class AutoDeploymentProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            retain_stacks_on_account_removal: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''[ ``Service-managed`` permissions] Describes whether StackSets automatically deploys to AWS Organizations accounts that are added to a target organizational unit (OU).

            :param enabled: If set to ``true`` , StackSets automatically deploys additional stack instances to AWS Organizations accounts that are added to a target organization or organizational unit (OU) in the specified Regions. If an account is removed from a target organization or OU, StackSets deletes stack instances from the account in the specified Regions.
            :param retain_stacks_on_account_removal: If set to ``true`` , stack resources are retained when an account is removed from a target organization or OU. If set to ``false`` , stack resources are deleted. Specify only if ``Enabled`` is set to ``True`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-autodeployment.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudformation as cloudformation
                
                auto_deployment_property = cloudformation.CfnStackSet.AutoDeploymentProperty(
                    enabled=False,
                    retain_stacks_on_account_removal=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6d35ac6b73134a404538c458ab31c0ee390b738200afdd1d40919aa276c32879)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument retain_stacks_on_account_removal", value=retain_stacks_on_account_removal, expected_type=type_hints["retain_stacks_on_account_removal"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if retain_stacks_on_account_removal is not None:
                self._values["retain_stacks_on_account_removal"] = retain_stacks_on_account_removal

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If set to ``true`` , StackSets automatically deploys additional stack instances to AWS Organizations accounts that are added to a target organization or organizational unit (OU) in the specified Regions.

            If an account is removed from a target organization or OU, StackSets deletes stack instances from the account in the specified Regions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-autodeployment.html#cfn-cloudformation-stackset-autodeployment-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def retain_stacks_on_account_removal(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If set to ``true`` , stack resources are retained when an account is removed from a target organization or OU.

            If set to ``false`` , stack resources are deleted. Specify only if ``Enabled`` is set to ``True`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-autodeployment.html#cfn-cloudformation-stackset-autodeployment-retainstacksonaccountremoval
            '''
            result = self._values.get("retain_stacks_on_account_removal")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoDeploymentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudformation.CfnStackSet.DeploymentTargetsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "account_filter_type": "accountFilterType",
            "accounts": "accounts",
            "accounts_url": "accountsUrl",
            "organizational_unit_ids": "organizationalUnitIds",
        },
    )
    class DeploymentTargetsProperty:
        def __init__(
            self,
            *,
            account_filter_type: typing.Optional[builtins.str] = None,
            accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
            accounts_url: typing.Optional[builtins.str] = None,
            organizational_unit_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The AWS OrganizationalUnitIds or Accounts for which to create stack instances in the specified Regions.

            :param account_filter_type: Limit deployment targets to individual accounts or include additional accounts with provided OUs. The following is a list of possible values for the ``AccountFilterType`` operation. - ``INTERSECTION`` : StackSets deploys to the accounts specified in ``Accounts`` parameter. - ``DIFFERENCE`` : StackSets excludes the accounts specified in ``Accounts`` parameter. This enables user to avoid certain accounts within an OU such as suspended accounts. - ``UNION`` : StackSets includes additional accounts deployment targets. This is the default value if ``AccountFilterType`` is not provided. This enables user to update an entire OU and individual accounts from a different OU in one request, which used to be two separate requests. - ``NONE`` : Deploys to all the accounts in specified organizational units (OU).
            :param accounts: The names of one or more AWS accounts for which you want to deploy stack set updates. *Pattern* : ``^[0-9]{12}$``
            :param accounts_url: Returns the value of the ``AccountsUrl`` property.
            :param organizational_unit_ids: The organization root ID or organizational unit (OU) IDs to which StackSets deploys. *Pattern* : ``^(ou-[a-z0-9]{4,32}-[a-z0-9]{8,32}|r-[a-z0-9]{4,32})$``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-deploymenttargets.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudformation as cloudformation
                
                deployment_targets_property = cloudformation.CfnStackSet.DeploymentTargetsProperty(
                    account_filter_type="accountFilterType",
                    accounts=["accounts"],
                    accounts_url="accountsUrl",
                    organizational_unit_ids=["organizationalUnitIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d8ae80f4aea46a54e6a8f1bdc756aca7c5711e62043011e42a2452c61211e289)
                check_type(argname="argument account_filter_type", value=account_filter_type, expected_type=type_hints["account_filter_type"])
                check_type(argname="argument accounts", value=accounts, expected_type=type_hints["accounts"])
                check_type(argname="argument accounts_url", value=accounts_url, expected_type=type_hints["accounts_url"])
                check_type(argname="argument organizational_unit_ids", value=organizational_unit_ids, expected_type=type_hints["organizational_unit_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if account_filter_type is not None:
                self._values["account_filter_type"] = account_filter_type
            if accounts is not None:
                self._values["accounts"] = accounts
            if accounts_url is not None:
                self._values["accounts_url"] = accounts_url
            if organizational_unit_ids is not None:
                self._values["organizational_unit_ids"] = organizational_unit_ids

        @builtins.property
        def account_filter_type(self) -> typing.Optional[builtins.str]:
            '''Limit deployment targets to individual accounts or include additional accounts with provided OUs.

            The following is a list of possible values for the ``AccountFilterType`` operation.

            - ``INTERSECTION`` : StackSets deploys to the accounts specified in ``Accounts`` parameter.
            - ``DIFFERENCE`` : StackSets excludes the accounts specified in ``Accounts`` parameter. This enables user to avoid certain accounts within an OU such as suspended accounts.
            - ``UNION`` : StackSets includes additional accounts deployment targets.

            This is the default value if ``AccountFilterType`` is not provided. This enables user to update an entire OU and individual accounts from a different OU in one request, which used to be two separate requests.

            - ``NONE`` : Deploys to all the accounts in specified organizational units (OU).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-deploymenttargets.html#cfn-cloudformation-stackset-deploymenttargets-accountfiltertype
            '''
            result = self._values.get("account_filter_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def accounts(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The names of one or more AWS accounts for which you want to deploy stack set updates.

            *Pattern* : ``^[0-9]{12}$``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-deploymenttargets.html#cfn-cloudformation-stackset-deploymenttargets-accounts
            '''
            result = self._values.get("accounts")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def accounts_url(self) -> typing.Optional[builtins.str]:
            '''Returns the value of the ``AccountsUrl`` property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-deploymenttargets.html#cfn-cloudformation-stackset-deploymenttargets-accountsurl
            '''
            result = self._values.get("accounts_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def organizational_unit_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The organization root ID or organizational unit (OU) IDs to which StackSets deploys.

            *Pattern* : ``^(ou-[a-z0-9]{4,32}-[a-z0-9]{8,32}|r-[a-z0-9]{4,32})$``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-deploymenttargets.html#cfn-cloudformation-stackset-deploymenttargets-organizationalunitids
            '''
            result = self._values.get("organizational_unit_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeploymentTargetsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudformation.CfnStackSet.ManagedExecutionProperty",
        jsii_struct_bases=[],
        name_mapping={"active": "active"},
    )
    class ManagedExecutionProperty:
        def __init__(
            self,
            *,
            active: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Describes whether StackSets performs non-conflicting operations concurrently and queues conflicting operations.

            :param active: When ``true`` , StackSets performs non-conflicting operations concurrently and queues conflicting operations. After conflicting operations finish, StackSets starts queued operations in request order. .. epigraph:: If there are already running or queued operations, StackSets queues all incoming operations even if they are non-conflicting. You can't modify your stack set's execution configuration while there are running or queued operations for that stack set. When ``false`` (default), StackSets performs one operation at a time in request order.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-managedexecution.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudformation as cloudformation
                
                managed_execution_property = cloudformation.CfnStackSet.ManagedExecutionProperty(
                    active=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a88c5840453701ae68e49d722949e1be2f17144e28858beff6801effcf65385a)
                check_type(argname="argument active", value=active, expected_type=type_hints["active"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if active is not None:
                self._values["active"] = active

        @builtins.property
        def active(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When ``true`` , StackSets performs non-conflicting operations concurrently and queues conflicting operations.

            After conflicting operations finish, StackSets starts queued operations in request order.
            .. epigraph::

               If there are already running or queued operations, StackSets queues all incoming operations even if they are non-conflicting.

               You can't modify your stack set's execution configuration while there are running or queued operations for that stack set.

            When ``false`` (default), StackSets performs one operation at a time in request order.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-managedexecution.html#cfn-cloudformation-stackset-managedexecution-active
            '''
            result = self._values.get("active")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ManagedExecutionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudformation.CfnStackSet.OperationPreferencesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "failure_tolerance_count": "failureToleranceCount",
            "failure_tolerance_percentage": "failureTolerancePercentage",
            "max_concurrent_count": "maxConcurrentCount",
            "max_concurrent_percentage": "maxConcurrentPercentage",
            "region_concurrency_type": "regionConcurrencyType",
            "region_order": "regionOrder",
        },
    )
    class OperationPreferencesProperty:
        def __init__(
            self,
            *,
            failure_tolerance_count: typing.Optional[jsii.Number] = None,
            failure_tolerance_percentage: typing.Optional[jsii.Number] = None,
            max_concurrent_count: typing.Optional[jsii.Number] = None,
            max_concurrent_percentage: typing.Optional[jsii.Number] = None,
            region_concurrency_type: typing.Optional[builtins.str] = None,
            region_order: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The user-specified preferences for how AWS CloudFormation performs a stack set operation.

            For more information on maximum concurrent accounts and failure tolerance, see `Stack set operation options <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stackset-ops-options>`_ .

            :param failure_tolerance_count: The number of accounts, per Region, for which this operation can fail before AWS CloudFormation stops the operation in that Region. If the operation is stopped in a Region, AWS CloudFormation doesn't attempt the operation in any subsequent Regions. Conditional: You must specify either ``FailureToleranceCount`` or ``FailureTolerancePercentage`` (but not both).
            :param failure_tolerance_percentage: The percentage of accounts, per Region, for which this stack operation can fail before AWS CloudFormation stops the operation in that Region. If the operation is stopped in a Region, AWS CloudFormation doesn't attempt the operation in any subsequent Regions. When calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds *down* to the next whole number. Conditional: You must specify either ``FailureToleranceCount`` or ``FailureTolerancePercentage`` , but not both.
            :param max_concurrent_count: The maximum number of accounts in which to perform this operation at one time. This is dependent on the value of ``FailureToleranceCount`` . ``MaxConcurrentCount`` is at most one more than the ``FailureToleranceCount`` . Note that this setting lets you specify the *maximum* for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling. Conditional: You must specify either ``MaxConcurrentCount`` or ``MaxConcurrentPercentage`` , but not both.
            :param max_concurrent_percentage: The maximum percentage of accounts in which to perform this operation at one time. When calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, CloudFormation sets the number as one instead. Note that this setting lets you specify the *maximum* for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling. Conditional: You must specify either ``MaxConcurrentCount`` or ``MaxConcurrentPercentage`` , but not both.
            :param region_concurrency_type: The concurrency type of deploying StackSets operations in Regions, could be in parallel or one Region at a time.
            :param region_order: The order of the Regions where you want to perform the stack operation. .. epigraph:: ``RegionOrder`` isn't followed if ``AutoDeployment`` is enabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-operationpreferences.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudformation as cloudformation
                
                operation_preferences_property = cloudformation.CfnStackSet.OperationPreferencesProperty(
                    failure_tolerance_count=123,
                    failure_tolerance_percentage=123,
                    max_concurrent_count=123,
                    max_concurrent_percentage=123,
                    region_concurrency_type="regionConcurrencyType",
                    region_order=["regionOrder"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0c87217399b0eaf825f9406bd82cc941cf4d39fbdd459a48905d7fb072775ff9)
                check_type(argname="argument failure_tolerance_count", value=failure_tolerance_count, expected_type=type_hints["failure_tolerance_count"])
                check_type(argname="argument failure_tolerance_percentage", value=failure_tolerance_percentage, expected_type=type_hints["failure_tolerance_percentage"])
                check_type(argname="argument max_concurrent_count", value=max_concurrent_count, expected_type=type_hints["max_concurrent_count"])
                check_type(argname="argument max_concurrent_percentage", value=max_concurrent_percentage, expected_type=type_hints["max_concurrent_percentage"])
                check_type(argname="argument region_concurrency_type", value=region_concurrency_type, expected_type=type_hints["region_concurrency_type"])
                check_type(argname="argument region_order", value=region_order, expected_type=type_hints["region_order"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if failure_tolerance_count is not None:
                self._values["failure_tolerance_count"] = failure_tolerance_count
            if failure_tolerance_percentage is not None:
                self._values["failure_tolerance_percentage"] = failure_tolerance_percentage
            if max_concurrent_count is not None:
                self._values["max_concurrent_count"] = max_concurrent_count
            if max_concurrent_percentage is not None:
                self._values["max_concurrent_percentage"] = max_concurrent_percentage
            if region_concurrency_type is not None:
                self._values["region_concurrency_type"] = region_concurrency_type
            if region_order is not None:
                self._values["region_order"] = region_order

        @builtins.property
        def failure_tolerance_count(self) -> typing.Optional[jsii.Number]:
            '''The number of accounts, per Region, for which this operation can fail before AWS CloudFormation stops the operation in that Region.

            If the operation is stopped in a Region, AWS CloudFormation doesn't attempt the operation in any subsequent Regions.

            Conditional: You must specify either ``FailureToleranceCount`` or ``FailureTolerancePercentage`` (but not both).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-operationpreferences.html#cfn-cloudformation-stackset-operationpreferences-failuretolerancecount
            '''
            result = self._values.get("failure_tolerance_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def failure_tolerance_percentage(self) -> typing.Optional[jsii.Number]:
            '''The percentage of accounts, per Region, for which this stack operation can fail before AWS CloudFormation stops the operation in that Region.

            If the operation is stopped in a Region, AWS CloudFormation doesn't attempt the operation in any subsequent Regions.

            When calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds *down* to the next whole number.

            Conditional: You must specify either ``FailureToleranceCount`` or ``FailureTolerancePercentage`` , but not both.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-operationpreferences.html#cfn-cloudformation-stackset-operationpreferences-failuretolerancepercentage
            '''
            result = self._values.get("failure_tolerance_percentage")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_concurrent_count(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of accounts in which to perform this operation at one time.

            This is dependent on the value of ``FailureToleranceCount`` . ``MaxConcurrentCount`` is at most one more than the ``FailureToleranceCount`` .

            Note that this setting lets you specify the *maximum* for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.

            Conditional: You must specify either ``MaxConcurrentCount`` or ``MaxConcurrentPercentage`` , but not both.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-operationpreferences.html#cfn-cloudformation-stackset-operationpreferences-maxconcurrentcount
            '''
            result = self._values.get("max_concurrent_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_concurrent_percentage(self) -> typing.Optional[jsii.Number]:
            '''The maximum percentage of accounts in which to perform this operation at one time.

            When calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, CloudFormation sets the number as one instead.

            Note that this setting lets you specify the *maximum* for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.

            Conditional: You must specify either ``MaxConcurrentCount`` or ``MaxConcurrentPercentage`` , but not both.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-operationpreferences.html#cfn-cloudformation-stackset-operationpreferences-maxconcurrentpercentage
            '''
            result = self._values.get("max_concurrent_percentage")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def region_concurrency_type(self) -> typing.Optional[builtins.str]:
            '''The concurrency type of deploying StackSets operations in Regions, could be in parallel or one Region at a time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-operationpreferences.html#cfn-cloudformation-stackset-operationpreferences-regionconcurrencytype
            '''
            result = self._values.get("region_concurrency_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def region_order(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The order of the Regions where you want to perform the stack operation.

            .. epigraph::

               ``RegionOrder`` isn't followed if ``AutoDeployment`` is enabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-operationpreferences.html#cfn-cloudformation-stackset-operationpreferences-regionorder
            '''
            result = self._values.get("region_order")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OperationPreferencesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudformation.CfnStackSet.ParameterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "parameter_key": "parameterKey",
            "parameter_value": "parameterValue",
        },
    )
    class ParameterProperty:
        def __init__(
            self,
            *,
            parameter_key: builtins.str,
            parameter_value: builtins.str,
        ) -> None:
            '''The Parameter data type.

            :param parameter_key: The key associated with the parameter. If you don't specify a key and value for a particular parameter, AWS CloudFormation uses the default value that's specified in your template.
            :param parameter_value: The input value associated with the parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-parameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudformation as cloudformation
                
                parameter_property = cloudformation.CfnStackSet.ParameterProperty(
                    parameter_key="parameterKey",
                    parameter_value="parameterValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6d3c6f69647df803bb89120866192359ca951dfdc391e1d2dea7337c4d579728)
                check_type(argname="argument parameter_key", value=parameter_key, expected_type=type_hints["parameter_key"])
                check_type(argname="argument parameter_value", value=parameter_value, expected_type=type_hints["parameter_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "parameter_key": parameter_key,
                "parameter_value": parameter_value,
            }

        @builtins.property
        def parameter_key(self) -> builtins.str:
            '''The key associated with the parameter.

            If you don't specify a key and value for a particular parameter, AWS CloudFormation uses the default value that's specified in your template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-parameter.html#cfn-cloudformation-stackset-parameter-parameterkey
            '''
            result = self._values.get("parameter_key")
            assert result is not None, "Required property 'parameter_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def parameter_value(self) -> builtins.str:
            '''The input value associated with the parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-parameter.html#cfn-cloudformation-stackset-parameter-parametervalue
            '''
            result = self._values.get("parameter_value")
            assert result is not None, "Required property 'parameter_value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudformation.CfnStackSet.StackInstancesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "deployment_targets": "deploymentTargets",
            "regions": "regions",
            "parameter_overrides": "parameterOverrides",
        },
    )
    class StackInstancesProperty:
        def __init__(
            self,
            *,
            deployment_targets: typing.Union[_IResolvable_da3f097b, typing.Union["CfnStackSet.DeploymentTargetsProperty", typing.Dict[builtins.str, typing.Any]]],
            regions: typing.Sequence[builtins.str],
            parameter_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStackSet.ParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Stack instances in some specific accounts and Regions.

            :param deployment_targets: The AWS ``OrganizationalUnitIds`` or ``Accounts`` for which to create stack instances in the specified Regions.
            :param regions: The names of one or more Regions where you want to create stack instances using the specified AWS accounts .
            :param parameter_overrides: A list of stack set parameters whose values you want to override in the selected stack instances.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-stackinstances.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudformation as cloudformation
                
                stack_instances_property = cloudformation.CfnStackSet.StackInstancesProperty(
                    deployment_targets=cloudformation.CfnStackSet.DeploymentTargetsProperty(
                        account_filter_type="accountFilterType",
                        accounts=["accounts"],
                        accounts_url="accountsUrl",
                        organizational_unit_ids=["organizationalUnitIds"]
                    ),
                    regions=["regions"],
                
                    # the properties below are optional
                    parameter_overrides=[cloudformation.CfnStackSet.ParameterProperty(
                        parameter_key="parameterKey",
                        parameter_value="parameterValue"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ecf8c5916c31e05ceede29df4b44ba37bf9563fb737793cde100e1a327788558)
                check_type(argname="argument deployment_targets", value=deployment_targets, expected_type=type_hints["deployment_targets"])
                check_type(argname="argument regions", value=regions, expected_type=type_hints["regions"])
                check_type(argname="argument parameter_overrides", value=parameter_overrides, expected_type=type_hints["parameter_overrides"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "deployment_targets": deployment_targets,
                "regions": regions,
            }
            if parameter_overrides is not None:
                self._values["parameter_overrides"] = parameter_overrides

        @builtins.property
        def deployment_targets(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnStackSet.DeploymentTargetsProperty"]:
            '''The AWS ``OrganizationalUnitIds`` or ``Accounts`` for which to create stack instances in the specified Regions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-stackinstances.html#cfn-cloudformation-stackset-stackinstances-deploymenttargets
            '''
            result = self._values.get("deployment_targets")
            assert result is not None, "Required property 'deployment_targets' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnStackSet.DeploymentTargetsProperty"], result)

        @builtins.property
        def regions(self) -> typing.List[builtins.str]:
            '''The names of one or more Regions where you want to create stack instances using the specified AWS accounts .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-stackinstances.html#cfn-cloudformation-stackset-stackinstances-regions
            '''
            result = self._values.get("regions")
            assert result is not None, "Required property 'regions' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def parameter_overrides(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStackSet.ParameterProperty"]]]]:
            '''A list of stack set parameters whose values you want to override in the selected stack instances.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-stackinstances.html#cfn-cloudformation-stackset-stackinstances-parameteroverrides
            '''
            result = self._values.get("parameter_overrides")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStackSet.ParameterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StackInstancesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnStackSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "permission_model": "permissionModel",
        "stack_set_name": "stackSetName",
        "administration_role_arn": "administrationRoleArn",
        "auto_deployment": "autoDeployment",
        "call_as": "callAs",
        "capabilities": "capabilities",
        "description": "description",
        "execution_role_name": "executionRoleName",
        "managed_execution": "managedExecution",
        "operation_preferences": "operationPreferences",
        "parameters": "parameters",
        "stack_instances_group": "stackInstancesGroup",
        "tags": "tags",
        "template_body": "templateBody",
        "template_url": "templateUrl",
    },
)
class CfnStackSetProps:
    def __init__(
        self,
        *,
        permission_model: builtins.str,
        stack_set_name: builtins.str,
        administration_role_arn: typing.Optional[builtins.str] = None,
        auto_deployment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStackSet.AutoDeploymentProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        call_as: typing.Optional[builtins.str] = None,
        capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        execution_role_name: typing.Optional[builtins.str] = None,
        managed_execution: typing.Any = None,
        operation_preferences: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStackSet.OperationPreferencesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStackSet.ParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        stack_instances_group: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStackSet.StackInstancesProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        template_body: typing.Optional[builtins.str] = None,
        template_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnStackSet``.

        :param permission_model: Describes how the IAM roles required for stack set operations are created. - With ``SELF_MANAGED`` permissions, you must create the administrator and execution roles required to deploy to target accounts. For more information, see `Grant Self-Managed Stack Set Permissions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html>`_ . - With ``SERVICE_MANAGED`` permissions, StackSets automatically creates the IAM roles required to deploy to accounts managed by AWS Organizations .
        :param stack_set_name: The name to associate with the stack set. The name must be unique in the Region where you create your stack set. .. epigraph:: The ``StackSetName`` property is required.
        :param administration_role_arn: The Amazon Resource Number (ARN) of the IAM role to use to create this stack set. Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account. Use customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account. For more information, see `Prerequisites: Granting Permissions for Stack Set Operations <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html>`_ in the *AWS CloudFormation User Guide* . *Minimum* : ``20`` *Maximum* : ``2048``
        :param auto_deployment: [ ``Service-managed`` permissions] Describes whether StackSets automatically deploys to AWS Organizations accounts that are added to a target organization or organizational unit (OU).
        :param call_as: [Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account. By default, ``SELF`` is specified. Use ``SELF`` for stack sets with self-managed permissions. - To create a stack set with service-managed permissions while signed in to the management account, specify ``SELF`` . - To create a stack set with service-managed permissions while signed in to a delegated administrator account, specify ``DELEGATED_ADMIN`` . Your AWS account must be registered as a delegated admin in the management account. For more information, see `Register a delegated administrator <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html>`_ in the *AWS CloudFormation User Guide* . Stack sets with service-managed permissions are created in the management account, including stack sets that are created by delegated administrators. *Valid Values* : ``SELF`` | ``DELEGATED_ADMIN``
        :param capabilities: The capabilities that are allowed in the stack set. Some stack set templates might include resources that can affect permissions in your AWS account —for example, by creating new AWS Identity and Access Management ( IAM ) users. For more information, see `Acknowledging IAM Resources in AWS CloudFormation Templates <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities>`_ .
        :param description: A description of the stack set. *Minimum* : ``1`` *Maximum* : ``1024``
        :param execution_role_name: The name of the IAM execution role to use to create the stack set. If you don't specify an execution role, AWS CloudFormation uses the ``AWSCloudFormationStackSetExecutionRole`` role for the stack set operation. *Minimum* : ``1`` *Maximum* : ``64`` *Pattern* : ``[a-zA-Z_0-9+=,.@-]+``
        :param managed_execution: Describes whether StackSets performs non-conflicting operations concurrently and queues conflicting operations. When active, StackSets performs non-conflicting operations concurrently and queues conflicting operations. After conflicting operations finish, StackSets starts queued operations in request order. .. epigraph:: If there are already running or queued operations, StackSets queues all incoming operations even if they are non-conflicting. You can't modify your stack set's execution configuration while there are running or queued operations for that stack set. When inactive (default), StackSets performs one operation at a time in request order.
        :param operation_preferences: The user-specified preferences for how AWS CloudFormation performs a stack set operation.
        :param parameters: The input parameters for the stack set template.
        :param stack_instances_group: A group of stack instances with parameters in some specific accounts and Regions.
        :param tags: Key-value pairs to associate with this stack. AWS CloudFormation also propagates these tags to supported resources in the stack. You can specify a maximum number of 50 tags. If you don't specify this parameter, AWS CloudFormation doesn't modify the stack's tags. If you specify an empty value, AWS CloudFormation removes all associated tags.
        :param template_body: The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes. You must include either ``TemplateURL`` or ``TemplateBody`` in a StackSet, but you can't use both. Dynamic references in the ``TemplateBody`` may not work correctly in all cases. It's recommended to pass templates containing dynamic references through ``TemplateUrl`` instead.
        :param template_url: Location of file containing the template body. The URL must point to a template that's located in an Amazon S3 bucket or a Systems Manager document. For more information, go to `Template Anatomy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html>`_ in the AWS CloudFormation User Guide. Conditional: You must specify only one of the following parameters: ``TemplateBody`` , ``TemplateURL`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudformation as cloudformation
            
            # managed_execution: Any
            
            cfn_stack_set_props = cloudformation.CfnStackSetProps(
                permission_model="permissionModel",
                stack_set_name="stackSetName",
            
                # the properties below are optional
                administration_role_arn="administrationRoleArn",
                auto_deployment=cloudformation.CfnStackSet.AutoDeploymentProperty(
                    enabled=False,
                    retain_stacks_on_account_removal=False
                ),
                call_as="callAs",
                capabilities=["capabilities"],
                description="description",
                execution_role_name="executionRoleName",
                managed_execution=managed_execution,
                operation_preferences=cloudformation.CfnStackSet.OperationPreferencesProperty(
                    failure_tolerance_count=123,
                    failure_tolerance_percentage=123,
                    max_concurrent_count=123,
                    max_concurrent_percentage=123,
                    region_concurrency_type="regionConcurrencyType",
                    region_order=["regionOrder"]
                ),
                parameters=[cloudformation.CfnStackSet.ParameterProperty(
                    parameter_key="parameterKey",
                    parameter_value="parameterValue"
                )],
                stack_instances_group=[cloudformation.CfnStackSet.StackInstancesProperty(
                    deployment_targets=cloudformation.CfnStackSet.DeploymentTargetsProperty(
                        account_filter_type="accountFilterType",
                        accounts=["accounts"],
                        accounts_url="accountsUrl",
                        organizational_unit_ids=["organizationalUnitIds"]
                    ),
                    regions=["regions"],
            
                    # the properties below are optional
                    parameter_overrides=[cloudformation.CfnStackSet.ParameterProperty(
                        parameter_key="parameterKey",
                        parameter_value="parameterValue"
                    )]
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                template_body="templateBody",
                template_url="templateUrl"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd7c69ee686d407257fcf95f6bae23045d509b43b119884d9c3094d637a82501)
            check_type(argname="argument permission_model", value=permission_model, expected_type=type_hints["permission_model"])
            check_type(argname="argument stack_set_name", value=stack_set_name, expected_type=type_hints["stack_set_name"])
            check_type(argname="argument administration_role_arn", value=administration_role_arn, expected_type=type_hints["administration_role_arn"])
            check_type(argname="argument auto_deployment", value=auto_deployment, expected_type=type_hints["auto_deployment"])
            check_type(argname="argument call_as", value=call_as, expected_type=type_hints["call_as"])
            check_type(argname="argument capabilities", value=capabilities, expected_type=type_hints["capabilities"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument execution_role_name", value=execution_role_name, expected_type=type_hints["execution_role_name"])
            check_type(argname="argument managed_execution", value=managed_execution, expected_type=type_hints["managed_execution"])
            check_type(argname="argument operation_preferences", value=operation_preferences, expected_type=type_hints["operation_preferences"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument stack_instances_group", value=stack_instances_group, expected_type=type_hints["stack_instances_group"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument template_body", value=template_body, expected_type=type_hints["template_body"])
            check_type(argname="argument template_url", value=template_url, expected_type=type_hints["template_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "permission_model": permission_model,
            "stack_set_name": stack_set_name,
        }
        if administration_role_arn is not None:
            self._values["administration_role_arn"] = administration_role_arn
        if auto_deployment is not None:
            self._values["auto_deployment"] = auto_deployment
        if call_as is not None:
            self._values["call_as"] = call_as
        if capabilities is not None:
            self._values["capabilities"] = capabilities
        if description is not None:
            self._values["description"] = description
        if execution_role_name is not None:
            self._values["execution_role_name"] = execution_role_name
        if managed_execution is not None:
            self._values["managed_execution"] = managed_execution
        if operation_preferences is not None:
            self._values["operation_preferences"] = operation_preferences
        if parameters is not None:
            self._values["parameters"] = parameters
        if stack_instances_group is not None:
            self._values["stack_instances_group"] = stack_instances_group
        if tags is not None:
            self._values["tags"] = tags
        if template_body is not None:
            self._values["template_body"] = template_body
        if template_url is not None:
            self._values["template_url"] = template_url

    @builtins.property
    def permission_model(self) -> builtins.str:
        '''Describes how the IAM roles required for stack set operations are created.

        - With ``SELF_MANAGED`` permissions, you must create the administrator and execution roles required to deploy to target accounts. For more information, see `Grant Self-Managed Stack Set Permissions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html>`_ .
        - With ``SERVICE_MANAGED`` permissions, StackSets automatically creates the IAM roles required to deploy to accounts managed by AWS Organizations .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-permissionmodel
        '''
        result = self._values.get("permission_model")
        assert result is not None, "Required property 'permission_model' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stack_set_name(self) -> builtins.str:
        '''The name to associate with the stack set.

        The name must be unique in the Region where you create your stack set.
        .. epigraph::

           The ``StackSetName`` property is required.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-stacksetname
        '''
        result = self._values.get("stack_set_name")
        assert result is not None, "Required property 'stack_set_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def administration_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Number (ARN) of the IAM role to use to create this stack set.

        Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account.

        Use customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account. For more information, see `Prerequisites: Granting Permissions for Stack Set Operations <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html>`_ in the *AWS CloudFormation User Guide* .

        *Minimum* : ``20``

        *Maximum* : ``2048``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-administrationrolearn
        '''
        result = self._values.get("administration_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auto_deployment(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStackSet.AutoDeploymentProperty]]:
        '''[ ``Service-managed`` permissions] Describes whether StackSets automatically deploys to AWS Organizations accounts that are added to a target organization or organizational unit (OU).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-autodeployment
        '''
        result = self._values.get("auto_deployment")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStackSet.AutoDeploymentProperty]], result)

    @builtins.property
    def call_as(self) -> typing.Optional[builtins.str]:
        '''[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.

        By default, ``SELF`` is specified. Use ``SELF`` for stack sets with self-managed permissions.

        - To create a stack set with service-managed permissions while signed in to the management account, specify ``SELF`` .
        - To create a stack set with service-managed permissions while signed in to a delegated administrator account, specify ``DELEGATED_ADMIN`` .

        Your AWS account must be registered as a delegated admin in the management account. For more information, see `Register a delegated administrator <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html>`_ in the *AWS CloudFormation User Guide* .

        Stack sets with service-managed permissions are created in the management account, including stack sets that are created by delegated administrators.

        *Valid Values* : ``SELF`` | ``DELEGATED_ADMIN``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-callas
        '''
        result = self._values.get("call_as")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def capabilities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The capabilities that are allowed in the stack set.

        Some stack set templates might include resources that can affect permissions in your AWS account —for example, by creating new AWS Identity and Access Management ( IAM ) users. For more information, see `Acknowledging IAM Resources in AWS CloudFormation Templates <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-capabilities
        '''
        result = self._values.get("capabilities")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the stack set.

        *Minimum* : ``1``

        *Maximum* : ``1024``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def execution_role_name(self) -> typing.Optional[builtins.str]:
        '''The name of the IAM execution role to use to create the stack set.

        If you don't specify an execution role, AWS CloudFormation uses the ``AWSCloudFormationStackSetExecutionRole`` role for the stack set operation.

        *Minimum* : ``1``

        *Maximum* : ``64``

        *Pattern* : ``[a-zA-Z_0-9+=,.@-]+``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-executionrolename
        '''
        result = self._values.get("execution_role_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def managed_execution(self) -> typing.Any:
        '''Describes whether StackSets performs non-conflicting operations concurrently and queues conflicting operations.

        When active, StackSets performs non-conflicting operations concurrently and queues conflicting operations. After conflicting operations finish, StackSets starts queued operations in request order.
        .. epigraph::

           If there are already running or queued operations, StackSets queues all incoming operations even if they are non-conflicting.

           You can't modify your stack set's execution configuration while there are running or queued operations for that stack set.

        When inactive (default), StackSets performs one operation at a time in request order.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-managedexecution
        '''
        result = self._values.get("managed_execution")
        return typing.cast(typing.Any, result)

    @builtins.property
    def operation_preferences(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStackSet.OperationPreferencesProperty]]:
        '''The user-specified preferences for how AWS CloudFormation performs a stack set operation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-operationpreferences
        '''
        result = self._values.get("operation_preferences")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStackSet.OperationPreferencesProperty]], result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStackSet.ParameterProperty]]]]:
        '''The input parameters for the stack set template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStackSet.ParameterProperty]]]], result)

    @builtins.property
    def stack_instances_group(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStackSet.StackInstancesProperty]]]]:
        '''A group of stack instances with parameters in some specific accounts and Regions.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-stackinstancesgroup
        '''
        result = self._values.get("stack_instances_group")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStackSet.StackInstancesProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Key-value pairs to associate with this stack.

        AWS CloudFormation also propagates these tags to supported resources in the stack. You can specify a maximum number of 50 tags.

        If you don't specify this parameter, AWS CloudFormation doesn't modify the stack's tags. If you specify an empty value, AWS CloudFormation removes all associated tags.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def template_body(self) -> typing.Optional[builtins.str]:
        '''The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes.

        You must include either ``TemplateURL`` or ``TemplateBody`` in a StackSet, but you can't use both. Dynamic references in the ``TemplateBody`` may not work correctly in all cases. It's recommended to pass templates containing dynamic references through ``TemplateUrl`` instead.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-templatebody
        '''
        result = self._values.get("template_body")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template_url(self) -> typing.Optional[builtins.str]:
        '''Location of file containing the template body.

        The URL must point to a template that's located in an Amazon S3 bucket or a Systems Manager document. For more information, go to `Template Anatomy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html>`_ in the AWS CloudFormation User Guide.

        Conditional: You must specify only one of the following parameters: ``TemplateBody`` , ``TemplateURL`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-templateurl
        '''
        result = self._values.get("template_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStackSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnTypeActivation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnTypeActivation",
):
    '''Activates a public third-party extension, making it available for use in stack templates.

    For more information, see `Using public extensions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html>`_ in the *AWS CloudFormation User Guide* .

    Once you have activated a public third-party extension in your account and Region, use `SetTypeConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html>`_ to specify configuration properties for the extension. For more information, see `Configuring extensions at the account level <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-private.html#registry-set-configuration>`_ in the *CloudFormation User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html
    :cloudformationResource: AWS::CloudFormation::TypeActivation
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudformation as cloudformation
        
        cfn_type_activation = cloudformation.CfnTypeActivation(self, "MyCfnTypeActivation",
            auto_update=False,
            execution_role_arn="executionRoleArn",
            logging_config=cloudformation.CfnTypeActivation.LoggingConfigProperty(
                log_group_name="logGroupName",
                log_role_arn="logRoleArn"
            ),
            major_version="majorVersion",
            public_type_arn="publicTypeArn",
            publisher_id="publisherId",
            type="type",
            type_name="typeName",
            type_name_alias="typeNameAlias",
            version_bump="versionBump"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        auto_update: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        execution_role_arn: typing.Optional[builtins.str] = None,
        logging_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTypeActivation.LoggingConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        major_version: typing.Optional[builtins.str] = None,
        public_type_arn: typing.Optional[builtins.str] = None,
        publisher_id: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        type_name: typing.Optional[builtins.str] = None,
        type_name_alias: typing.Optional[builtins.str] = None,
        version_bump: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param auto_update: Whether to automatically update the extension in this account and Region when a new *minor* version is published by the extension publisher. Major versions released by the publisher must be manually updated. The default is ``true`` .
        :param execution_role_arn: The name of the IAM execution role to use to activate the extension.
        :param logging_config: Specifies logging configuration information for an extension.
        :param major_version: The major version of this extension you want to activate, if multiple major versions are available. The default is the latest major version. CloudFormation uses the latest available *minor* version of the major version selected. You can specify ``MajorVersion`` or ``VersionBump`` , but not both.
        :param public_type_arn: The Amazon Resource Number (ARN) of the public extension. Conditional: You must specify ``PublicTypeArn`` , or ``TypeName`` , ``Type`` , and ``PublisherId`` .
        :param publisher_id: The ID of the extension publisher. Conditional: You must specify ``PublicTypeArn`` , or ``TypeName`` , ``Type`` , and ``PublisherId`` .
        :param type: The extension type. Conditional: You must specify ``PublicTypeArn`` , or ``TypeName`` , ``Type`` , and ``PublisherId`` .
        :param type_name: The name of the extension. Conditional: You must specify ``PublicTypeArn`` , or ``TypeName`` , ``Type`` , and ``PublisherId`` .
        :param type_name_alias: An alias to assign to the public extension, in this account and Region. If you specify an alias for the extension, CloudFormation treats the alias as the extension type name within this account and Region. You must use the alias to refer to the extension in your templates, API calls, and CloudFormation console. An extension alias must be unique within a given account and Region. You can activate the same public resource multiple times in the same account and Region, using different type name aliases.
        :param version_bump: Manually updates a previously-activated type to a new major or minor version, if available. You can also use this parameter to update the value of ``AutoUpdate`` . - ``MAJOR`` : CloudFormation updates the extension to the newest major version, if one is available. - ``MINOR`` : CloudFormation updates the extension to the newest minor version, if one is available.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c6ab9cbd4089f894248d56e57228ffda7ba7040649f1b2a30619e7d6d8fa2da)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTypeActivationProps(
            auto_update=auto_update,
            execution_role_arn=execution_role_arn,
            logging_config=logging_config,
            major_version=major_version,
            public_type_arn=public_type_arn,
            publisher_id=publisher_id,
            type=type,
            type_name=type_name,
            type_name_alias=type_name_alias,
            version_bump=version_bump,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d5bc985834dd5f202878644c36e7ab6b7bf99a018897f4d87ea2dba352b2f9c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__914c29e9a170178c1633d20abf19b57ac4b1384e5d98682f2dd2bb11af6ea35c)
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
        '''The Amazon Resource Name (ARN) of the activated extension, in this account and Region.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="autoUpdate")
    def auto_update(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to automatically update the extension in this account and Region when a new *minor* version is published by the extension publisher.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "autoUpdate"))

    @auto_update.setter
    def auto_update(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__965115beba4ff920767d3418867400c3fd2ac96db01883321c6c58d5ab95a498)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoUpdate", value)

    @builtins.property
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''The name of the IAM execution role to use to activate the extension.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleArn"))

    @execution_role_arn.setter
    def execution_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a49fb47b67bc614aa9baf1d224495a6bc1a6997d82a0ae245716b03323c87265)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="loggingConfig")
    def logging_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTypeActivation.LoggingConfigProperty"]]:
        '''Specifies logging configuration information for an extension.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTypeActivation.LoggingConfigProperty"]], jsii.get(self, "loggingConfig"))

    @logging_config.setter
    def logging_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTypeActivation.LoggingConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3128499025f0cd2b7cf69908cd1f677dfc787d78e3535ffe73a474814a4b44fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loggingConfig", value)

    @builtins.property
    @jsii.member(jsii_name="majorVersion")
    def major_version(self) -> typing.Optional[builtins.str]:
        '''The major version of this extension you want to activate, if multiple major versions are available.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "majorVersion"))

    @major_version.setter
    def major_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38f8706cb79c5fd813aff12ec0f140cfb9aa2315caede10ee25f7f47dd78c003)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "majorVersion", value)

    @builtins.property
    @jsii.member(jsii_name="publicTypeArn")
    def public_type_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Number (ARN) of the public extension.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicTypeArn"))

    @public_type_arn.setter
    def public_type_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d050fccc0fa6945488b52ac4b66b02df3b594ccc1f8d6446fb525502ca9e7de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicTypeArn", value)

    @builtins.property
    @jsii.member(jsii_name="publisherId")
    def publisher_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the extension publisher.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publisherId"))

    @publisher_id.setter
    def publisher_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9cefe914744511413a9e642e1cf63c419c6f76b4c92191c407331b86a63c051)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publisherId", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[builtins.str]:
        '''The extension type.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "type"))

    @type.setter
    def type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__144866ce8961352d18fd3ad5118c42037c4c674e65d3bfc13355b9888adc5aa3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="typeName")
    def type_name(self) -> typing.Optional[builtins.str]:
        '''The name of the extension.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeName"))

    @type_name.setter
    def type_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1a840170c400b898f200b23a279ac119e0face0b6d7213a6def5a0d4a00c612)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeName", value)

    @builtins.property
    @jsii.member(jsii_name="typeNameAlias")
    def type_name_alias(self) -> typing.Optional[builtins.str]:
        '''An alias to assign to the public extension, in this account and Region.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeNameAlias"))

    @type_name_alias.setter
    def type_name_alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f04f5a2572901ffbb8e50214df14dda5fe5d944383b6714bcb6bfd48b65422a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeNameAlias", value)

    @builtins.property
    @jsii.member(jsii_name="versionBump")
    def version_bump(self) -> typing.Optional[builtins.str]:
        '''Manually updates a previously-activated type to a new major or minor version, if available.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionBump"))

    @version_bump.setter
    def version_bump(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71a2627c4d88ecd7f57252757b759fe753ac0e5b057ee9efe42f8f9d42160c44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versionBump", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudformation.CfnTypeActivation.LoggingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group_name": "logGroupName", "log_role_arn": "logRoleArn"},
    )
    class LoggingConfigProperty:
        def __init__(
            self,
            *,
            log_group_name: typing.Optional[builtins.str] = None,
            log_role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains logging configuration information for an extension.

            :param log_group_name: The Amazon CloudWatch Logs group to which CloudFormation sends error logging information when invoking the extension's handlers.
            :param log_role_arn: The Amazon Resource Name (ARN) of the role that CloudFormation should assume when sending log entries to CloudWatch Logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-typeactivation-loggingconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudformation as cloudformation
                
                logging_config_property = cloudformation.CfnTypeActivation.LoggingConfigProperty(
                    log_group_name="logGroupName",
                    log_role_arn="logRoleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f2a386677ea85f60b0913a70653efb6a455d9cd0cf61f935a088386c753aeea7)
                check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
                check_type(argname="argument log_role_arn", value=log_role_arn, expected_type=type_hints["log_role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if log_group_name is not None:
                self._values["log_group_name"] = log_group_name
            if log_role_arn is not None:
                self._values["log_role_arn"] = log_role_arn

        @builtins.property
        def log_group_name(self) -> typing.Optional[builtins.str]:
            '''The Amazon CloudWatch Logs group to which CloudFormation sends error logging information when invoking the extension's handlers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-typeactivation-loggingconfig.html#cfn-cloudformation-typeactivation-loggingconfig-loggroupname
            '''
            result = self._values.get("log_group_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def log_role_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the role that CloudFormation should assume when sending log entries to CloudWatch Logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-typeactivation-loggingconfig.html#cfn-cloudformation-typeactivation-loggingconfig-logrolearn
            '''
            result = self._values.get("log_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnTypeActivationProps",
    jsii_struct_bases=[],
    name_mapping={
        "auto_update": "autoUpdate",
        "execution_role_arn": "executionRoleArn",
        "logging_config": "loggingConfig",
        "major_version": "majorVersion",
        "public_type_arn": "publicTypeArn",
        "publisher_id": "publisherId",
        "type": "type",
        "type_name": "typeName",
        "type_name_alias": "typeNameAlias",
        "version_bump": "versionBump",
    },
)
class CfnTypeActivationProps:
    def __init__(
        self,
        *,
        auto_update: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        execution_role_arn: typing.Optional[builtins.str] = None,
        logging_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTypeActivation.LoggingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        major_version: typing.Optional[builtins.str] = None,
        public_type_arn: typing.Optional[builtins.str] = None,
        publisher_id: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        type_name: typing.Optional[builtins.str] = None,
        type_name_alias: typing.Optional[builtins.str] = None,
        version_bump: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnTypeActivation``.

        :param auto_update: Whether to automatically update the extension in this account and Region when a new *minor* version is published by the extension publisher. Major versions released by the publisher must be manually updated. The default is ``true`` .
        :param execution_role_arn: The name of the IAM execution role to use to activate the extension.
        :param logging_config: Specifies logging configuration information for an extension.
        :param major_version: The major version of this extension you want to activate, if multiple major versions are available. The default is the latest major version. CloudFormation uses the latest available *minor* version of the major version selected. You can specify ``MajorVersion`` or ``VersionBump`` , but not both.
        :param public_type_arn: The Amazon Resource Number (ARN) of the public extension. Conditional: You must specify ``PublicTypeArn`` , or ``TypeName`` , ``Type`` , and ``PublisherId`` .
        :param publisher_id: The ID of the extension publisher. Conditional: You must specify ``PublicTypeArn`` , or ``TypeName`` , ``Type`` , and ``PublisherId`` .
        :param type: The extension type. Conditional: You must specify ``PublicTypeArn`` , or ``TypeName`` , ``Type`` , and ``PublisherId`` .
        :param type_name: The name of the extension. Conditional: You must specify ``PublicTypeArn`` , or ``TypeName`` , ``Type`` , and ``PublisherId`` .
        :param type_name_alias: An alias to assign to the public extension, in this account and Region. If you specify an alias for the extension, CloudFormation treats the alias as the extension type name within this account and Region. You must use the alias to refer to the extension in your templates, API calls, and CloudFormation console. An extension alias must be unique within a given account and Region. You can activate the same public resource multiple times in the same account and Region, using different type name aliases.
        :param version_bump: Manually updates a previously-activated type to a new major or minor version, if available. You can also use this parameter to update the value of ``AutoUpdate`` . - ``MAJOR`` : CloudFormation updates the extension to the newest major version, if one is available. - ``MINOR`` : CloudFormation updates the extension to the newest minor version, if one is available.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudformation as cloudformation
            
            cfn_type_activation_props = cloudformation.CfnTypeActivationProps(
                auto_update=False,
                execution_role_arn="executionRoleArn",
                logging_config=cloudformation.CfnTypeActivation.LoggingConfigProperty(
                    log_group_name="logGroupName",
                    log_role_arn="logRoleArn"
                ),
                major_version="majorVersion",
                public_type_arn="publicTypeArn",
                publisher_id="publisherId",
                type="type",
                type_name="typeName",
                type_name_alias="typeNameAlias",
                version_bump="versionBump"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02e5c1de4d531856b94f268082510ca5202a92506b87b8752473c8ee205e52df)
            check_type(argname="argument auto_update", value=auto_update, expected_type=type_hints["auto_update"])
            check_type(argname="argument execution_role_arn", value=execution_role_arn, expected_type=type_hints["execution_role_arn"])
            check_type(argname="argument logging_config", value=logging_config, expected_type=type_hints["logging_config"])
            check_type(argname="argument major_version", value=major_version, expected_type=type_hints["major_version"])
            check_type(argname="argument public_type_arn", value=public_type_arn, expected_type=type_hints["public_type_arn"])
            check_type(argname="argument publisher_id", value=publisher_id, expected_type=type_hints["publisher_id"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument type_name", value=type_name, expected_type=type_hints["type_name"])
            check_type(argname="argument type_name_alias", value=type_name_alias, expected_type=type_hints["type_name_alias"])
            check_type(argname="argument version_bump", value=version_bump, expected_type=type_hints["version_bump"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if auto_update is not None:
            self._values["auto_update"] = auto_update
        if execution_role_arn is not None:
            self._values["execution_role_arn"] = execution_role_arn
        if logging_config is not None:
            self._values["logging_config"] = logging_config
        if major_version is not None:
            self._values["major_version"] = major_version
        if public_type_arn is not None:
            self._values["public_type_arn"] = public_type_arn
        if publisher_id is not None:
            self._values["publisher_id"] = publisher_id
        if type is not None:
            self._values["type"] = type
        if type_name is not None:
            self._values["type_name"] = type_name
        if type_name_alias is not None:
            self._values["type_name_alias"] = type_name_alias
        if version_bump is not None:
            self._values["version_bump"] = version_bump

    @builtins.property
    def auto_update(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to automatically update the extension in this account and Region when a new *minor* version is published by the extension publisher.

        Major versions released by the publisher must be manually updated.

        The default is ``true`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-autoupdate
        '''
        result = self._values.get("auto_update")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''The name of the IAM execution role to use to activate the extension.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-executionrolearn
        '''
        result = self._values.get("execution_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTypeActivation.LoggingConfigProperty]]:
        '''Specifies logging configuration information for an extension.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-loggingconfig
        '''
        result = self._values.get("logging_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTypeActivation.LoggingConfigProperty]], result)

    @builtins.property
    def major_version(self) -> typing.Optional[builtins.str]:
        '''The major version of this extension you want to activate, if multiple major versions are available.

        The default is the latest major version. CloudFormation uses the latest available *minor* version of the major version selected.

        You can specify ``MajorVersion`` or ``VersionBump`` , but not both.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-majorversion
        '''
        result = self._values.get("major_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_type_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Number (ARN) of the public extension.

        Conditional: You must specify ``PublicTypeArn`` , or ``TypeName`` , ``Type`` , and ``PublisherId`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-publictypearn
        '''
        result = self._values.get("public_type_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def publisher_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the extension publisher.

        Conditional: You must specify ``PublicTypeArn`` , or ``TypeName`` , ``Type`` , and ``PublisherId`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-publisherid
        '''
        result = self._values.get("publisher_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The extension type.

        Conditional: You must specify ``PublicTypeArn`` , or ``TypeName`` , ``Type`` , and ``PublisherId`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type_name(self) -> typing.Optional[builtins.str]:
        '''The name of the extension.

        Conditional: You must specify ``PublicTypeArn`` , or ``TypeName`` , ``Type`` , and ``PublisherId`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-typename
        '''
        result = self._values.get("type_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type_name_alias(self) -> typing.Optional[builtins.str]:
        '''An alias to assign to the public extension, in this account and Region.

        If you specify an alias for the extension, CloudFormation treats the alias as the extension type name within this account and Region. You must use the alias to refer to the extension in your templates, API calls, and CloudFormation console.

        An extension alias must be unique within a given account and Region. You can activate the same public resource multiple times in the same account and Region, using different type name aliases.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-typenamealias
        '''
        result = self._values.get("type_name_alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_bump(self) -> typing.Optional[builtins.str]:
        '''Manually updates a previously-activated type to a new major or minor version, if available.

        You can also use this parameter to update the value of ``AutoUpdate`` .

        - ``MAJOR`` : CloudFormation updates the extension to the newest major version, if one is available.
        - ``MINOR`` : CloudFormation updates the extension to the newest minor version, if one is available.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-versionbump
        '''
        result = self._values.get("version_bump")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTypeActivationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnWaitCondition(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnWaitCondition",
):
    '''.. epigraph::

   For Amazon EC2 and Auto Scaling resources, we recommend that you use a ``CreationPolicy`` attribute instead of wait conditions.

    Add a CreationPolicy attribute to those resources, and use the cfn-signal helper script to signal when an instance creation process has completed successfully.

    You can use a wait condition for situations like the following:

    - To coordinate stack resource creation with configuration actions that are external to the stack creation.
    - To track the status of a configuration process.

    For these situations, we recommend that you associate a `CreationPolicy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-creationpolicy.html>`_ attribute with the wait condition so that you don't have to use a wait condition handle. For more information and an example, see `Creating wait conditions in a template <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-waitcondition.html>`_ . If you use a CreationPolicy with a wait condition, don't specify any of the wait condition's properties.
    .. epigraph::

       If you use the `VPC endpoints <https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html>`_ feature, resources in the VPC that respond to wait conditions must have access to CloudFormation , specific Amazon Simple Storage Service ( Amazon S3 ) buckets. Resources must send wait condition responses to a presigned Amazon S3 URL. If they can't send responses to Amazon S3 , CloudFormation won't receive a response and the stack operation fails. For more information, see `Setting up VPC endpoints for AWS CloudFormation <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-vpce-bucketnames.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-waitcondition.html
    :cloudformationResource: AWS::CloudFormation::WaitCondition
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudformation as cloudformation
        
        cfn_wait_condition = cloudformation.CfnWaitCondition(self, "MyCfnWaitCondition",
            count=123,
            handle="handle",
            timeout="timeout"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        count: typing.Optional[jsii.Number] = None,
        handle: typing.Optional[builtins.str] = None,
        timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param count: The number of success signals that CloudFormation must receive before it continues the stack creation process. When the wait condition receives the requisite number of success signals, CloudFormation resumes the creation of the stack. If the wait condition doesn't receive the specified number of success signals before the Timeout period expires, CloudFormation assumes that the wait condition has failed and rolls the stack back. Updates aren't supported.
        :param handle: A reference to the wait condition handle used to signal this wait condition. Use the ``Ref`` intrinsic function to specify an ```AWS::CloudFormation::WaitConditionHandle`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitconditionhandle.html>`_ resource. Anytime you add a ``WaitCondition`` resource during a stack update, you must associate the wait condition with a new WaitConditionHandle resource. Don't reuse an old wait condition handle that has already been defined in the template. If you reuse a wait condition handle, the wait condition might evaluate old signals from a previous create or update stack command. Updates aren't supported.
        :param timeout: The length of time (in seconds) to wait for the number of signals that the ``Count`` property specifies. ``Timeout`` is a minimum-bound property, meaning the timeout occurs no sooner than the time you specify, but can occur shortly thereafter. The maximum time that can be specified for this property is 12 hours (43200 seconds). Updates aren't supported.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce6d60b6ac749d18fca5dd7948ac2a2143d40eef9dfa145f8afe1fb96a266cc0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnWaitConditionProps(count=count, handle=handle, timeout=timeout)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbea3ac73e2857d7e5439505b35641ad3a1d82ae84b9c9fae4ec23885b587432)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9355797c322f45e4189d31249927b0add2172d39b8f35028fc0c2954d0662b44)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrData")
    def attr_data(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: Data
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrData"))

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
    @jsii.member(jsii_name="count")
    def count(self) -> typing.Optional[jsii.Number]:
        '''The number of success signals that CloudFormation must receive before it continues the stack creation process.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "count"))

    @count.setter
    def count(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f72ce605058a768f3b5b4608d9ff5b9ec1abcc36e9f578b72cb22f432151c841)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="handle")
    def handle(self) -> typing.Optional[builtins.str]:
        '''A reference to the wait condition handle used to signal this wait condition.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "handle"))

    @handle.setter
    def handle(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__825e58b6fc35f0721569d4eaecf5d1915523e2d56d37b948995ee3134c45357d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "handle", value)

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> typing.Optional[builtins.str]:
        '''The length of time (in seconds) to wait for the number of signals that the ``Count`` property specifies.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__799f86ffa4f6f7c4bc18416df8f001b73de4fd1b78efe3be99d762c2b90c1fe7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value)


@jsii.implements(_IInspectable_c2943556)
class CfnWaitConditionHandle(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnWaitConditionHandle",
):
    '''.. epigraph::

   For Amazon EC2 and Auto Scaling resources, we recommend that you use a ``CreationPolicy`` attribute instead of wait conditions.

    Add a ``CreationPolicy`` attribute to those resources, and use the cfn-signal helper script to signal when an instance creation process has completed successfully.
    .. epigraph::

       For more information, see `Deploying applications on Amazon EC2 with AWS CloudFormation <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/deploying.applications.html>`_ .

    The ``AWS::CloudFormation::WaitConditionHandle`` type has no properties. When you reference the ``WaitConditionHandle`` resource by using the ``Ref`` function, AWS CloudFormation returns a presigned URL. You pass this URL to applications or scripts that are running on your Amazon EC2 instances to send signals to that URL. An associated ``AWS::CloudFormation::WaitCondition`` resource checks the URL for the required number of success signals or for a failure signal.
    .. epigraph::

       Anytime you add a ``WaitCondition`` resource during a stack update or update a resource with a wait condition, you must associate the wait condition with a new ``WaitConditionHandle`` resource. Don't reuse an old wait condition handle that has already been defined in the template. If you reuse a wait condition handle, the wait condition might evaluate old signals from a previous create or update stack command. > Updates aren't supported for this resource.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-waitconditionhandle.html
    :cloudformationResource: AWS::CloudFormation::WaitConditionHandle
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudformation as cloudformation
        
        cfn_wait_condition_handle = cloudformation.CfnWaitConditionHandle(self, "MyCfnWaitConditionHandle")
    '''

    def __init__(self, scope: _constructs_77d1e7e8.Construct, id: builtins.str) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b515e1607be0202e6a5a547c6593ee2b77d461f4ffe8f5d824a7ec8fd3822a97)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnWaitConditionHandleProps()

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e5a0c006ed96f200b7e8d3a22789239eafb7b6a44d96630bcb2f839051f64ac)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fac51adf50f1e69f50b22b703890060df479a7e66c5118fead502297e26019f3)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''A unique identifier for the resource.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnWaitConditionHandleProps",
    jsii_struct_bases=[],
    name_mapping={},
)
class CfnWaitConditionHandleProps:
    def __init__(self) -> None:
        '''Properties for defining a ``CfnWaitConditionHandle``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-waitconditionhandle.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudformation as cloudformation
            
            cfn_wait_condition_handle_props = cloudformation.CfnWaitConditionHandleProps()
        '''
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWaitConditionHandleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudformation.CfnWaitConditionProps",
    jsii_struct_bases=[],
    name_mapping={"count": "count", "handle": "handle", "timeout": "timeout"},
)
class CfnWaitConditionProps:
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        handle: typing.Optional[builtins.str] = None,
        timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnWaitCondition``.

        :param count: The number of success signals that CloudFormation must receive before it continues the stack creation process. When the wait condition receives the requisite number of success signals, CloudFormation resumes the creation of the stack. If the wait condition doesn't receive the specified number of success signals before the Timeout period expires, CloudFormation assumes that the wait condition has failed and rolls the stack back. Updates aren't supported.
        :param handle: A reference to the wait condition handle used to signal this wait condition. Use the ``Ref`` intrinsic function to specify an ```AWS::CloudFormation::WaitConditionHandle`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitconditionhandle.html>`_ resource. Anytime you add a ``WaitCondition`` resource during a stack update, you must associate the wait condition with a new WaitConditionHandle resource. Don't reuse an old wait condition handle that has already been defined in the template. If you reuse a wait condition handle, the wait condition might evaluate old signals from a previous create or update stack command. Updates aren't supported.
        :param timeout: The length of time (in seconds) to wait for the number of signals that the ``Count`` property specifies. ``Timeout`` is a minimum-bound property, meaning the timeout occurs no sooner than the time you specify, but can occur shortly thereafter. The maximum time that can be specified for this property is 12 hours (43200 seconds). Updates aren't supported.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-waitcondition.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudformation as cloudformation
            
            cfn_wait_condition_props = cloudformation.CfnWaitConditionProps(
                count=123,
                handle="handle",
                timeout="timeout"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae4f065be2a042359e82699c38e1fd0e59e979184753fcfc6c0e7ddff00fd2dd)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument handle", value=handle, expected_type=type_hints["handle"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if count is not None:
            self._values["count"] = count
        if handle is not None:
            self._values["handle"] = handle
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''The number of success signals that CloudFormation must receive before it continues the stack creation process.

        When the wait condition receives the requisite number of success signals, CloudFormation resumes the creation of the stack. If the wait condition doesn't receive the specified number of success signals before the Timeout period expires, CloudFormation assumes that the wait condition has failed and rolls the stack back.

        Updates aren't supported.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-waitcondition.html#cfn-cloudformation-waitcondition-count
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def handle(self) -> typing.Optional[builtins.str]:
        '''A reference to the wait condition handle used to signal this wait condition.

        Use the ``Ref`` intrinsic function to specify an ```AWS::CloudFormation::WaitConditionHandle`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitconditionhandle.html>`_ resource.

        Anytime you add a ``WaitCondition`` resource during a stack update, you must associate the wait condition with a new WaitConditionHandle resource. Don't reuse an old wait condition handle that has already been defined in the template. If you reuse a wait condition handle, the wait condition might evaluate old signals from a previous create or update stack command.

        Updates aren't supported.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-waitcondition.html#cfn-cloudformation-waitcondition-handle
        '''
        result = self._values.get("handle")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout(self) -> typing.Optional[builtins.str]:
        '''The length of time (in seconds) to wait for the number of signals that the ``Count`` property specifies.

        ``Timeout`` is a minimum-bound property, meaning the timeout occurs no sooner than the time you specify, but can occur shortly thereafter. The maximum time that can be specified for this property is 12 hours (43200 seconds).

        Updates aren't supported.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-waitcondition.html#cfn-cloudformation-waitcondition-timeout
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWaitConditionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCustomResource",
    "CfnCustomResourceProps",
    "CfnHookDefaultVersion",
    "CfnHookDefaultVersionProps",
    "CfnHookTypeConfig",
    "CfnHookTypeConfigProps",
    "CfnHookVersion",
    "CfnHookVersionProps",
    "CfnMacro",
    "CfnMacroProps",
    "CfnModuleDefaultVersion",
    "CfnModuleDefaultVersionProps",
    "CfnModuleVersion",
    "CfnModuleVersionProps",
    "CfnPublicTypeVersion",
    "CfnPublicTypeVersionProps",
    "CfnPublisher",
    "CfnPublisherProps",
    "CfnResourceDefaultVersion",
    "CfnResourceDefaultVersionProps",
    "CfnResourceVersion",
    "CfnResourceVersionProps",
    "CfnStack",
    "CfnStackProps",
    "CfnStackSet",
    "CfnStackSetProps",
    "CfnTypeActivation",
    "CfnTypeActivationProps",
    "CfnWaitCondition",
    "CfnWaitConditionHandle",
    "CfnWaitConditionHandleProps",
    "CfnWaitConditionProps",
]

publication.publish()

def _typecheckingstub__c0a3b106ffbe7fa1289a8e834aa35f1789994087e265fc54556841046e49661f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    service_token: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d68a034cdb94c769aad71e0c0e32ff9640cb173daa74beb6268d30e7cc5c090f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32da455611d85f4cddbdd6732b28aef10c806d245ec5102a182879612f90a78c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77951bc16957122471cd48666095011465879476219c4b12cf6a7c2684f5587e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f766b9f5ea2582bff4d2cb33b19a38fbdabfbe380c61d04a056e8e0d2a00b54a(
    *,
    service_token: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b8bde9f1f98ed0500179dfc97dcadf56e8ff1be4dde185bebd99abe71d79167(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    type_name: typing.Optional[builtins.str] = None,
    type_version_arn: typing.Optional[builtins.str] = None,
    version_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d3cffde5405816d6a41ef681bf2c43df8b5bde2710721ee16254bf382423108(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50c67f0fb346e88146ee0ab601fd70c28799c458260663e325a155a6150756f9(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c985f39fb842ecd8d503cc1ff86e00864e1fc45b5962d3fc9c66a7b136ac654a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8fff96e0ddbd71a4aa46a88a0873bb65a9aad21cdec8f8be8016c745e513d99(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9f9bb2d06c69bb7ef45feaaed611f94d81b89f367a377c829ab1e52ed8d53a0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86e582779d0fb8b475195467d988078f1c65515c6a403bf9dc6b5ef8aced149f(
    *,
    type_name: typing.Optional[builtins.str] = None,
    type_version_arn: typing.Optional[builtins.str] = None,
    version_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1aa75e15214f256047fa6d0b79cceb9720316dd5d5524cca649ba63b4b4613e3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    configuration: builtins.str,
    configuration_alias: typing.Optional[builtins.str] = None,
    type_arn: typing.Optional[builtins.str] = None,
    type_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64d031e26b8bd0eeb56b31d7de08efef921b07640fe30239018c4b9b54f75af3(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__152138584317142b159bc64a674adbec428e62f1899b9285a49a4b8e3bb752bd(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3847791ddd5530d8a9d2144538417d1a4cf5fb909bd613d41c5905e02d37bb9a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__649cdf62ea09d9e4b72042f283c05b766e052006f59f2d05f9a6d2eab2ea396a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b787dd89e7baba7e0a6ac2766dafcb836d4d6e45724a95c5ca1fdbd30ebd66b1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84b67709252725d1f5ed0113558f6ddd94c0f17e7aadee85cf241f59a8eb5585(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef5f9608def2c7b14e7449a6bceadbd90b6e5242e86707d305d4923d050f8f9a(
    *,
    configuration: builtins.str,
    configuration_alias: typing.Optional[builtins.str] = None,
    type_arn: typing.Optional[builtins.str] = None,
    type_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__291bd220d9e7cd7e2d0ca851a8919b3ac012e0d7a45a664cf291d6381de23d73(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    schema_handler_package: builtins.str,
    type_name: builtins.str,
    execution_role_arn: typing.Optional[builtins.str] = None,
    logging_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHookVersion.LoggingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19d9ff1b2b94a1214e3523199f203ce84bb6818d8221d1c9c8864607fd68ed54(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__373bbf4ceb7d1c3f9739457d175b6e990bef886865f570c651e71104ae299479(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0efb96dfc84b17d40a50018cd6d23e3c296865fd07b6996b365c17a092ce873c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30df538b23952e625e940e55d9e80b1642e22eea6fc3b3850d26f16b544d134d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cb4f09410ca3ef9c85888607e8ac924121a6fe32ab21f62e93aa2cc02b1130a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b1199d24d006c1117662bdfbc72f2cbbbd5b4d4138b339988fd36100745a337(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnHookVersion.LoggingConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3186540a164984c66b6fb1ac418c16e60743db883585e9275304381fae9a1cf(
    *,
    log_group_name: typing.Optional[builtins.str] = None,
    log_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a9bb2ef202f6ed27272b4d9787339d2a26c63beb648e39f3c4977200bcc65b1(
    *,
    schema_handler_package: builtins.str,
    type_name: builtins.str,
    execution_role_arn: typing.Optional[builtins.str] = None,
    logging_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHookVersion.LoggingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__459b4551acd819b198938843c729caa68cfe3bcc1ac16be0f4fd2dcd90f33831(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    function_name: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    log_group_name: typing.Optional[builtins.str] = None,
    log_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e79976b6be80cc0b5afd2b70e48da1b0c8e9d3428ef7477627dbe51024a9c253(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86ff8044429c96b4c0bd2cfb5a521df919f8d44b6c475424ccb71b25a5a27bfd(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b0da3fdeddad952c3d568e3ccfa62b9e1071259fd408795b5efbd74d57e4638(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d90b36bce3c84920d31c840cdf1935d477a088ab2099260661fa84ff8a860aed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d119fc672e810bdbbc903e1fd3131af02cfeee73b8d1f69b91281fd849867947(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2549852c1e5490496427fcb72c16723fec532a2e82b6f7266d106b423891194(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f243639cffd7e9711e024007e213cfd4f0a728fdffd3d87d4544108f9615424(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42b23a370c2b5c33d49b7f892f41cb61bdad8c6efe4c078d5d357c872fd866b6(
    *,
    function_name: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    log_group_name: typing.Optional[builtins.str] = None,
    log_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c99a91d0140bd9a8f50bc3d072ae8da722981d1a5fcb2663b4fac493489b2cb(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    arn: typing.Optional[builtins.str] = None,
    module_name: typing.Optional[builtins.str] = None,
    version_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d83f9976a4a99125758d72c5d97e0b8bc18b132214c023e9e853759dbce1d4a4(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96e84170f59bacf8bbda0fc4d70222b46dbd510ff329e31a72d532819620ac0e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1951b46878047a0bebb4baa53659dd9872ccb6a4bb32a494795339c0571ba62(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b448aa45d5a1bdb97e2a01807f61b189d67e11631eacdc0cbdba01fc0ca8b5a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2565d831587a784d43e20ccbd403e1a5b0a41c68a6ea34925b2361aed7757b1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f3ea65dfbd0cb512b468da1b9fb9627d1355ed7f5434478a08a635f804f77fc(
    *,
    arn: typing.Optional[builtins.str] = None,
    module_name: typing.Optional[builtins.str] = None,
    version_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50da97e251a6b1bacc1202d70f10c857ca74139ea4e8bcc35b2ff47e8b8b2729(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    module_name: builtins.str,
    module_package: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8f07b3edeecaaa60f70d40c8955ccee2de0a5b10eab7df6791cee814a719762(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93f33fd2a94ced47dcfc85eb2d6054254d607a4b79fcf6223d2366514e67189d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5ddab8adf20df5c0b192a1c24dff5f7d64b2e7e20fefec44ae32c6caeab6ce1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d720948c279cd9b12fc9a1cce3d68bd4e92be8876552138cf8bc30bce71b233f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08386807944526883f9a2a3af6d7b270292ea388802a7d26e4ebe78b66b8aa38(
    *,
    module_name: builtins.str,
    module_package: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdf2194d5c024c7904a7b498046de219f29aca0dc247850eeb368cc6e8de6e80(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    arn: typing.Optional[builtins.str] = None,
    log_delivery_bucket: typing.Optional[builtins.str] = None,
    public_version_number: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
    type_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b8e80bbf83093dbb7c5669cba4eb3df0f24e04ad66ac14f184f58bc8c80cdaa(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24c9fd4ba1a836eec8198800f5120b3dd3a490a47fb73c5b6f9bda3dc4509f77(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef7377cb03089af40e51eb3ff0d703af316eb40432079d1af709f52cd1ddc8d9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87da3449532bb7cc8ef07cf37320b48e158d2074ac9402065fe2f31b61fe3936(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7c6d97beb345173cfda1fd73e5d035568d8ecfbbd833964b8b7a8126f4bc159(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__563ec7c1482c5079e1e9794b3bd4743da435c16cc7a741b9962b2a18f2695515(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ff64f615236770a749da8c076614d45c7535c8fced5b15461275638cb12afc8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18efb861dce8210d36272fd882e9481ecf1f7ad199bf2bf34fdd66aa24a64bc7(
    *,
    arn: typing.Optional[builtins.str] = None,
    log_delivery_bucket: typing.Optional[builtins.str] = None,
    public_version_number: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
    type_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98c7559405984ded6c9804bd442f72ad08edd6b60ad34619af070342a90bb1f0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    accept_terms_and_conditions: typing.Union[builtins.bool, _IResolvable_da3f097b],
    connection_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e45513940f140496d5e61d36d1bb3dcff4cc290fc725da5edc058e51f674e78(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9eee79f0a68d58a80234313f91421f270b156d5bcb8358b8f2ffa4491e86e61(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32926bab93b08cf2b9ba45201d6c17771f4ee56bd0d6ae22c80302acbe88d711(
    value: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6543e2603954d96b676b1b073989fa0cd07d298228cd8b4ced57c2fbea3bb0c6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b41681bff4816c257b59b8947cb33afcd9050c71509e0ec07b569e949d0a9ce(
    *,
    accept_terms_and_conditions: typing.Union[builtins.bool, _IResolvable_da3f097b],
    connection_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3bf93b0b355aca5fb2cff6cd3ed10d995f75d3a89763b8aa05fb433f97856e9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    type_name: typing.Optional[builtins.str] = None,
    type_version_arn: typing.Optional[builtins.str] = None,
    version_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9192b3f3f31f165283a9fef249de629eb55fb220ac568bb8c262f9f73a38647e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d693a992f8c1ba2af4ed78de5cada3f1d685f17f43921a70e1bfd549f9ac4f35(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__718a57bf8de77237fcb8e3a281903144964b40256824b54d8e49919e59709642(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab644f676b15f7bed54dcb226d419de1039e4a54d60778895c53f964cc22e036(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61966d72d6d53857a7d4531e87d5aa75dd4e47794020bd350a8ad18c4a375b39(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__846c1092e850e7f3b08a0c0fcc29b8cda8aa8f909b3c1479b1ddc873dd053222(
    *,
    type_name: typing.Optional[builtins.str] = None,
    type_version_arn: typing.Optional[builtins.str] = None,
    version_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d66096cd07e25c1ed44a33ad186a98806441d15023da1aa1c7a94d39edcd36a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    schema_handler_package: builtins.str,
    type_name: builtins.str,
    execution_role_arn: typing.Optional[builtins.str] = None,
    logging_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceVersion.LoggingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60549a7ad1c7eb301947c17673ebac8d626aa6340213be58c05eeae19db04fba(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36a7bf18163fba789ff5e275f0ade4a58d9b2f895051061d8838ce4a1b9b1e7f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6453c003449eb4a7a620fb123fab02f5fe5eda20f32be06eedb8b960f14e5712(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0d9e6b661355ce1ff1ffffe546827ed841f6351c4e62546fec58209ff877652(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f0b504fce536426ab9358d45f97b10ff78e173eefae7559f1499cca14b266df(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3815df35f78faddb4478e4806caabc98c6e3b931d83cb9b1f05419da5399cb86(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnResourceVersion.LoggingConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c68df5722a00d70d4751ceb1afcfb299c59a8b40faaeb3723d5c834184072cdf(
    *,
    log_group_name: typing.Optional[builtins.str] = None,
    log_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76ca3cbb367679516480c68e4d53a4abc20cb7d02f8a591754eb2f715e9c58e7(
    *,
    schema_handler_package: builtins.str,
    type_name: builtins.str,
    execution_role_arn: typing.Optional[builtins.str] = None,
    logging_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceVersion.LoggingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b03b296829d4f2eb356ceeb892ed7d61908e69c4949bd797def9d9980897a1a1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    notification_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    template_url: typing.Optional[builtins.str] = None,
    timeout_in_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca2eeeb5a2fc247c87aa885f14161d88b2b7db47ce5a176bee9ba83f61e8447d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d5f666653aae50479803ed71839253ef19c348c5240cb3bebb449b6e150d007(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d66d5e1fe390793c13ae8f3762505ddcb7c4e44a03b219a7d65987bc8ac48d68(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26855905eda83610dba6ef5eae36ae6d595846a274f432b31c16b01c431139bd(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dd6f2b6a16bc08db2d10b1a6eff5f64991fe724d61645874b4235a7f2816089(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3db469b6ac2b6930a53773a7067f28dcbe494d1c4c0aa67dc9ab276d28d07904(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c9f0cec1de29739b017def3b496f6e5bf888854e8a565ee7e2a8695868506eb(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4b95d92bea1984ce15e37fa304b047ed771a4f764d414ffac328157423828dc(
    *,
    description: typing.Optional[builtins.str] = None,
    export_name: typing.Optional[builtins.str] = None,
    output_key: typing.Optional[builtins.str] = None,
    output_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4da59ffe076e92fe1011ac29ca869d93a69d1442f3b7a0d1c765cca951d09b20(
    *,
    notification_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    template_url: typing.Optional[builtins.str] = None,
    timeout_in_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d9c85250c99fa8473d88e65c23c7c33031b75b34da26e2bece38ee28bd4570d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    permission_model: builtins.str,
    stack_set_name: builtins.str,
    administration_role_arn: typing.Optional[builtins.str] = None,
    auto_deployment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStackSet.AutoDeploymentProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    call_as: typing.Optional[builtins.str] = None,
    capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    execution_role_name: typing.Optional[builtins.str] = None,
    managed_execution: typing.Any = None,
    operation_preferences: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStackSet.OperationPreferencesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStackSet.ParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    stack_instances_group: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStackSet.StackInstancesProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    template_body: typing.Optional[builtins.str] = None,
    template_url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9afdd61cd9e49c077776e3c47082aee5db8792a3554b6cea078228185d569d6a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e04deb7ddb1fd06f6839d126c919fa0cce705f8816507397905c57e8dd9fb641(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af07bb659e1916cfa80a5d7739b21b36137879be79a124fe5e7e5c4b846c0d79(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2170c9fd24e7b05da9100bc462024b7ef6f36eefa874a1721b6ca5397bc20040(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33df1da68b9c62c99e1841856f4e201c8673ded83161a46959a6d5be71752562(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54972dd81830154ffcce6337f1843df37216b662ea86b869d79741b5fb9a365f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStackSet.AutoDeploymentProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e37b8025b5d58e66ec74873bd5eca7e1c4982e35f5495263ae5ce603d1a59b16(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__457467a4ee010a847f5a2f2eb373eb377a8870a7bb69910d54b5b28dfcb498c0(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a32b31569df72cb9c92223c05aae5461caf7d1b5669b21d2dd4487ac16d68be9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f336a94333318f89c159203981959dd1aa89598228f5e8eff09903e2d7e979cc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30ba7de0572ec3972439a2234107f74e54796d853ad6a78e334871adc49c4a4c(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2de21d60faf97e0417df4f6303d7a41a79560cd81bde48a6dc39d8691c07faec(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStackSet.OperationPreferencesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ce7162bef5c53321e37524df11a58f9e340a790ef5107072f3d51f53e536408(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStackSet.ParameterProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__968f546c0d5d9567cdb455e2836771e7127fd2fd09a1168bff825cbffc5698b0(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStackSet.StackInstancesProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd51501bb9559b68fef458b291af8ba7df88b39b9154b44b83c19b21f0d65c10(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43c92b7fcde86d072f3926d26396619d841d2e70e1e98fbdac9e78b9ea67ef8b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a294c8f5426fcf440746cb77033834a63ea811fbda12ac428bfda3503123c28(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d35ac6b73134a404538c458ab31c0ee390b738200afdd1d40919aa276c32879(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    retain_stacks_on_account_removal: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8ae80f4aea46a54e6a8f1bdc756aca7c5711e62043011e42a2452c61211e289(
    *,
    account_filter_type: typing.Optional[builtins.str] = None,
    accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
    accounts_url: typing.Optional[builtins.str] = None,
    organizational_unit_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a88c5840453701ae68e49d722949e1be2f17144e28858beff6801effcf65385a(
    *,
    active: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c87217399b0eaf825f9406bd82cc941cf4d39fbdd459a48905d7fb072775ff9(
    *,
    failure_tolerance_count: typing.Optional[jsii.Number] = None,
    failure_tolerance_percentage: typing.Optional[jsii.Number] = None,
    max_concurrent_count: typing.Optional[jsii.Number] = None,
    max_concurrent_percentage: typing.Optional[jsii.Number] = None,
    region_concurrency_type: typing.Optional[builtins.str] = None,
    region_order: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d3c6f69647df803bb89120866192359ca951dfdc391e1d2dea7337c4d579728(
    *,
    parameter_key: builtins.str,
    parameter_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecf8c5916c31e05ceede29df4b44ba37bf9563fb737793cde100e1a327788558(
    *,
    deployment_targets: typing.Union[_IResolvable_da3f097b, typing.Union[CfnStackSet.DeploymentTargetsProperty, typing.Dict[builtins.str, typing.Any]]],
    regions: typing.Sequence[builtins.str],
    parameter_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStackSet.ParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd7c69ee686d407257fcf95f6bae23045d509b43b119884d9c3094d637a82501(
    *,
    permission_model: builtins.str,
    stack_set_name: builtins.str,
    administration_role_arn: typing.Optional[builtins.str] = None,
    auto_deployment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStackSet.AutoDeploymentProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    call_as: typing.Optional[builtins.str] = None,
    capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    execution_role_name: typing.Optional[builtins.str] = None,
    managed_execution: typing.Any = None,
    operation_preferences: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStackSet.OperationPreferencesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStackSet.ParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    stack_instances_group: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStackSet.StackInstancesProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    template_body: typing.Optional[builtins.str] = None,
    template_url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c6ab9cbd4089f894248d56e57228ffda7ba7040649f1b2a30619e7d6d8fa2da(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    auto_update: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    execution_role_arn: typing.Optional[builtins.str] = None,
    logging_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTypeActivation.LoggingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    major_version: typing.Optional[builtins.str] = None,
    public_type_arn: typing.Optional[builtins.str] = None,
    publisher_id: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
    type_name: typing.Optional[builtins.str] = None,
    type_name_alias: typing.Optional[builtins.str] = None,
    version_bump: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d5bc985834dd5f202878644c36e7ab6b7bf99a018897f4d87ea2dba352b2f9c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__914c29e9a170178c1633d20abf19b57ac4b1384e5d98682f2dd2bb11af6ea35c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__965115beba4ff920767d3418867400c3fd2ac96db01883321c6c58d5ab95a498(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a49fb47b67bc614aa9baf1d224495a6bc1a6997d82a0ae245716b03323c87265(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3128499025f0cd2b7cf69908cd1f677dfc787d78e3535ffe73a474814a4b44fc(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTypeActivation.LoggingConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38f8706cb79c5fd813aff12ec0f140cfb9aa2315caede10ee25f7f47dd78c003(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d050fccc0fa6945488b52ac4b66b02df3b594ccc1f8d6446fb525502ca9e7de(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9cefe914744511413a9e642e1cf63c419c6f76b4c92191c407331b86a63c051(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__144866ce8961352d18fd3ad5118c42037c4c674e65d3bfc13355b9888adc5aa3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1a840170c400b898f200b23a279ac119e0face0b6d7213a6def5a0d4a00c612(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f04f5a2572901ffbb8e50214df14dda5fe5d944383b6714bcb6bfd48b65422a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71a2627c4d88ecd7f57252757b759fe753ac0e5b057ee9efe42f8f9d42160c44(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2a386677ea85f60b0913a70653efb6a455d9cd0cf61f935a088386c753aeea7(
    *,
    log_group_name: typing.Optional[builtins.str] = None,
    log_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02e5c1de4d531856b94f268082510ca5202a92506b87b8752473c8ee205e52df(
    *,
    auto_update: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    execution_role_arn: typing.Optional[builtins.str] = None,
    logging_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTypeActivation.LoggingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    major_version: typing.Optional[builtins.str] = None,
    public_type_arn: typing.Optional[builtins.str] = None,
    publisher_id: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
    type_name: typing.Optional[builtins.str] = None,
    type_name_alias: typing.Optional[builtins.str] = None,
    version_bump: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce6d60b6ac749d18fca5dd7948ac2a2143d40eef9dfa145f8afe1fb96a266cc0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    count: typing.Optional[jsii.Number] = None,
    handle: typing.Optional[builtins.str] = None,
    timeout: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbea3ac73e2857d7e5439505b35641ad3a1d82ae84b9c9fae4ec23885b587432(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9355797c322f45e4189d31249927b0add2172d39b8f35028fc0c2954d0662b44(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f72ce605058a768f3b5b4608d9ff5b9ec1abcc36e9f578b72cb22f432151c841(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__825e58b6fc35f0721569d4eaecf5d1915523e2d56d37b948995ee3134c45357d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__799f86ffa4f6f7c4bc18416df8f001b73de4fd1b78efe3be99d762c2b90c1fe7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b515e1607be0202e6a5a547c6593ee2b77d461f4ffe8f5d824a7ec8fd3822a97(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e5a0c006ed96f200b7e8d3a22789239eafb7b6a44d96630bcb2f839051f64ac(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fac51adf50f1e69f50b22b703890060df479a7e66c5118fead502297e26019f3(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae4f065be2a042359e82699c38e1fd0e59e979184753fcfc6c0e7ddff00fd2dd(
    *,
    count: typing.Optional[jsii.Number] = None,
    handle: typing.Optional[builtins.str] = None,
    timeout: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
