'''
# AWS::SystemsManagerSAP Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_systemsmanagersap as systemsmanagersap
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for SystemsManagerSAP construct libraries](https://constructs.dev/search?q=systemsmanagersap)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::SystemsManagerSAP resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SystemsManagerSAP.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::SystemsManagerSAP](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SystemsManagerSAP.html).

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
class CfnApplication(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_systemsmanagersap.CfnApplication",
):
    '''An SAP application registered with AWS Systems Manager for SAP.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-systemsmanagersap-application.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_systemsmanagersap as systemsmanagersap
        
        cfn_application = systemsmanagersap.CfnApplication(self, "MyCfnApplication",
            application_id="applicationId",
            application_type="applicationType",
        
            # the properties below are optional
            credentials=[systemsmanagersap.CfnApplication.CredentialProperty(
                credential_type="credentialType",
                database_name="databaseName",
                secret_id="secretId"
            )],
            instances=["instances"],
            sap_instance_number="sapInstanceNumber",
            sid="sid",
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
        application_id: builtins.str,
        application_type: builtins.str,
        credentials: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplication.CredentialProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        instances: typing.Optional[typing.Sequence[builtins.str]] = None,
        sap_instance_number: typing.Optional[builtins.str] = None,
        sid: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_id: The ID of the application.
        :param application_type: The type of the application.
        :param credentials: The credentials of the SAP application.
        :param instances: The Amazon EC2 instances on which your SAP application is running.
        :param sap_instance_number: The SAP instance number of the application.
        :param sid: The System ID of the application.
        :param tags: The tags on the application.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9271c1fe4df837d944d62ed41ed4e1f7b01ee290ee0cedef450b7d3b63dd216)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationProps(
            application_id=application_id,
            application_type=application_type,
            credentials=credentials,
            instances=instances,
            sap_instance_number=sap_instance_number,
            sid=sid,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15a497d637abd8065bbb16e179dbb14e650a0d40e3b2d0ff21c9e6117f62d46d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e314ab0ac8f39d15430971791f3c7cd85e16a74fbdea889ccae98fc03aacac7a)
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
        '''The Amazon Resource Name of the SAP application.

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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The ID of the application.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__220b45a13373704aaeea23f5880c81f1bc987f9d6ae87a01a80fcd60f3d2c899)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="applicationType")
    def application_type(self) -> builtins.str:
        '''The type of the application.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationType"))

    @application_type.setter
    def application_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4b8f1dc3ab2cc2af53565165fea2e3a71b3636909d6590d329ac8b01f5b260e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationType", value)

    @builtins.property
    @jsii.member(jsii_name="credentials")
    def credentials(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApplication.CredentialProperty"]]]]:
        '''The credentials of the SAP application.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApplication.CredentialProperty"]]]], jsii.get(self, "credentials"))

    @credentials.setter
    def credentials(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApplication.CredentialProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d7fd4ddc7b1c5dd15b7872fe8002624e595dabcca134f126fb732c23e5149c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "credentials", value)

    @builtins.property
    @jsii.member(jsii_name="instances")
    def instances(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Amazon EC2 instances on which your SAP application is running.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "instances"))

    @instances.setter
    def instances(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48b3e39bb8fbcf7bc24ce4c336c75b3d07f5a67befd7f0db2fe31c5755ceaf51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instances", value)

    @builtins.property
    @jsii.member(jsii_name="sapInstanceNumber")
    def sap_instance_number(self) -> typing.Optional[builtins.str]:
        '''The SAP instance number of the application.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sapInstanceNumber"))

    @sap_instance_number.setter
    def sap_instance_number(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fb3deb902943f4524698d7c3e52743d2dc332c2bae4baf1ab12cd65c6c078e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sapInstanceNumber", value)

    @builtins.property
    @jsii.member(jsii_name="sid")
    def sid(self) -> typing.Optional[builtins.str]:
        '''The System ID of the application.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sid"))

    @sid.setter
    def sid(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0b28059915ab835dbf826d7b5f1ea9b83530b99eae63df75921d1cb417d53e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sid", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags on the application.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84a8afb3becf838692cd2e040ef53d955aba6f46033283c6fd2d807663f653d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_systemsmanagersap.CfnApplication.CredentialProperty",
        jsii_struct_bases=[],
        name_mapping={
            "credential_type": "credentialType",
            "database_name": "databaseName",
            "secret_id": "secretId",
        },
    )
    class CredentialProperty:
        def __init__(
            self,
            *,
            credential_type: typing.Optional[builtins.str] = None,
            database_name: typing.Optional[builtins.str] = None,
            secret_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The credentials of your SAP application.

            :param credential_type: The type of the application credentials.
            :param database_name: The name of the SAP HANA database.
            :param secret_id: The secret ID created in AWS Secrets Manager to store the credentials of the SAP application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-systemsmanagersap-application-credential.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_systemsmanagersap as systemsmanagersap
                
                credential_property = systemsmanagersap.CfnApplication.CredentialProperty(
                    credential_type="credentialType",
                    database_name="databaseName",
                    secret_id="secretId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__209aa7feaf1ed6ac2bf183538ccbb7555a21c47880975dd9f9b002d73b1e7cbb)
                check_type(argname="argument credential_type", value=credential_type, expected_type=type_hints["credential_type"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument secret_id", value=secret_id, expected_type=type_hints["secret_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if credential_type is not None:
                self._values["credential_type"] = credential_type
            if database_name is not None:
                self._values["database_name"] = database_name
            if secret_id is not None:
                self._values["secret_id"] = secret_id

        @builtins.property
        def credential_type(self) -> typing.Optional[builtins.str]:
            '''The type of the application credentials.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-systemsmanagersap-application-credential.html#cfn-systemsmanagersap-application-credential-credentialtype
            '''
            result = self._values.get("credential_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def database_name(self) -> typing.Optional[builtins.str]:
            '''The name of the SAP HANA database.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-systemsmanagersap-application-credential.html#cfn-systemsmanagersap-application-credential-databasename
            '''
            result = self._values.get("database_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secret_id(self) -> typing.Optional[builtins.str]:
            '''The secret ID created in AWS Secrets Manager to store the credentials of the SAP application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-systemsmanagersap-application-credential.html#cfn-systemsmanagersap-application-credential-secretid
            '''
            result = self._values.get("secret_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CredentialProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_systemsmanagersap.CfnApplicationProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "application_type": "applicationType",
        "credentials": "credentials",
        "instances": "instances",
        "sap_instance_number": "sapInstanceNumber",
        "sid": "sid",
        "tags": "tags",
    },
)
class CfnApplicationProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        application_type: builtins.str,
        credentials: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.CredentialProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        instances: typing.Optional[typing.Sequence[builtins.str]] = None,
        sap_instance_number: typing.Optional[builtins.str] = None,
        sid: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnApplication``.

        :param application_id: The ID of the application.
        :param application_type: The type of the application.
        :param credentials: The credentials of the SAP application.
        :param instances: The Amazon EC2 instances on which your SAP application is running.
        :param sap_instance_number: The SAP instance number of the application.
        :param sid: The System ID of the application.
        :param tags: The tags on the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-systemsmanagersap-application.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_systemsmanagersap as systemsmanagersap
            
            cfn_application_props = systemsmanagersap.CfnApplicationProps(
                application_id="applicationId",
                application_type="applicationType",
            
                # the properties below are optional
                credentials=[systemsmanagersap.CfnApplication.CredentialProperty(
                    credential_type="credentialType",
                    database_name="databaseName",
                    secret_id="secretId"
                )],
                instances=["instances"],
                sap_instance_number="sapInstanceNumber",
                sid="sid",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a3a450935d6aacabad9991c3fdce7052d4392d63c713049280ff2a2a2615a38)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument application_type", value=application_type, expected_type=type_hints["application_type"])
            check_type(argname="argument credentials", value=credentials, expected_type=type_hints["credentials"])
            check_type(argname="argument instances", value=instances, expected_type=type_hints["instances"])
            check_type(argname="argument sap_instance_number", value=sap_instance_number, expected_type=type_hints["sap_instance_number"])
            check_type(argname="argument sid", value=sid, expected_type=type_hints["sid"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
            "application_type": application_type,
        }
        if credentials is not None:
            self._values["credentials"] = credentials
        if instances is not None:
            self._values["instances"] = instances
        if sap_instance_number is not None:
            self._values["sap_instance_number"] = sap_instance_number
        if sid is not None:
            self._values["sid"] = sid
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The ID of the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-systemsmanagersap-application.html#cfn-systemsmanagersap-application-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def application_type(self) -> builtins.str:
        '''The type of the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-systemsmanagersap-application.html#cfn-systemsmanagersap-application-applicationtype
        '''
        result = self._values.get("application_type")
        assert result is not None, "Required property 'application_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def credentials(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnApplication.CredentialProperty]]]]:
        '''The credentials of the SAP application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-systemsmanagersap-application.html#cfn-systemsmanagersap-application-credentials
        '''
        result = self._values.get("credentials")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnApplication.CredentialProperty]]]], result)

    @builtins.property
    def instances(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Amazon EC2 instances on which your SAP application is running.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-systemsmanagersap-application.html#cfn-systemsmanagersap-application-instances
        '''
        result = self._values.get("instances")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def sap_instance_number(self) -> typing.Optional[builtins.str]:
        '''The SAP instance number of the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-systemsmanagersap-application.html#cfn-systemsmanagersap-application-sapinstancenumber
        '''
        result = self._values.get("sap_instance_number")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sid(self) -> typing.Optional[builtins.str]:
        '''The System ID of the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-systemsmanagersap-application.html#cfn-systemsmanagersap-application-sid
        '''
        result = self._values.get("sid")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags on the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-systemsmanagersap-application.html#cfn-systemsmanagersap-application-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApplication",
    "CfnApplicationProps",
]

publication.publish()

def _typecheckingstub__d9271c1fe4df837d944d62ed41ed4e1f7b01ee290ee0cedef450b7d3b63dd216(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_id: builtins.str,
    application_type: builtins.str,
    credentials: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.CredentialProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    instances: typing.Optional[typing.Sequence[builtins.str]] = None,
    sap_instance_number: typing.Optional[builtins.str] = None,
    sid: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15a497d637abd8065bbb16e179dbb14e650a0d40e3b2d0ff21c9e6117f62d46d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e314ab0ac8f39d15430971791f3c7cd85e16a74fbdea889ccae98fc03aacac7a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__220b45a13373704aaeea23f5880c81f1bc987f9d6ae87a01a80fcd60f3d2c899(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4b8f1dc3ab2cc2af53565165fea2e3a71b3636909d6590d329ac8b01f5b260e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d7fd4ddc7b1c5dd15b7872fe8002624e595dabcca134f126fb732c23e5149c6(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnApplication.CredentialProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48b3e39bb8fbcf7bc24ce4c336c75b3d07f5a67befd7f0db2fe31c5755ceaf51(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fb3deb902943f4524698d7c3e52743d2dc332c2bae4baf1ab12cd65c6c078e1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0b28059915ab835dbf826d7b5f1ea9b83530b99eae63df75921d1cb417d53e5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84a8afb3becf838692cd2e040ef53d955aba6f46033283c6fd2d807663f653d1(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__209aa7feaf1ed6ac2bf183538ccbb7555a21c47880975dd9f9b002d73b1e7cbb(
    *,
    credential_type: typing.Optional[builtins.str] = None,
    database_name: typing.Optional[builtins.str] = None,
    secret_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a3a450935d6aacabad9991c3fdce7052d4392d63c713049280ff2a2a2615a38(
    *,
    application_id: builtins.str,
    application_type: builtins.str,
    credentials: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.CredentialProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    instances: typing.Optional[typing.Sequence[builtins.str]] = None,
    sap_instance_number: typing.Optional[builtins.str] = None,
    sid: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
