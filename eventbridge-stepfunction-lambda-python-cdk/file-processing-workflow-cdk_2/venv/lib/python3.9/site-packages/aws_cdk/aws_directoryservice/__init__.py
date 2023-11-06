'''
# AWS Directory Service Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_directoryservice as directoryservice
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for DirectoryService construct libraries](https://constructs.dev/search?q=directoryservice)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::DirectoryService resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DirectoryService.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::DirectoryService](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DirectoryService.html).

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
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnMicrosoftAD(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_directoryservice.CfnMicrosoftAD",
):
    '''The ``AWS::DirectoryService::MicrosoftAD`` resource specifies a Microsoft Active Directory in AWS so that your directory users and groups can access the AWS Management Console and AWS applications using their existing credentials.

    For more information, see `AWS Managed Microsoft AD <https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html>`_ in the *AWS Directory Service Admin Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_directoryservice as directoryservice
        
        cfn_microsoft_aD = directoryservice.CfnMicrosoftAD(self, "MyCfnMicrosoftAD",
            name="name",
            password="password",
            vpc_settings=directoryservice.CfnMicrosoftAD.VpcSettingsProperty(
                subnet_ids=["subnetIds"],
                vpc_id="vpcId"
            ),
        
            # the properties below are optional
            create_alias=False,
            edition="edition",
            enable_sso=False,
            short_name="shortName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        password: builtins.str,
        vpc_settings: typing.Union[_IResolvable_da3f097b, typing.Union["CfnMicrosoftAD.VpcSettingsProperty", typing.Dict[builtins.str, typing.Any]]],
        create_alias: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        edition: typing.Optional[builtins.str] = None,
        enable_sso: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        short_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The fully qualified domain name for the AWS Managed Microsoft AD directory, such as ``corp.example.com`` . This name will resolve inside your VPC only. It does not need to be publicly resolvable.
        :param password: The password for the default administrative user named ``Admin`` . If you need to change the password for the administrator account, see the `ResetUserPassword <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ResetUserPassword.html>`_ API call in the *AWS Directory Service API Reference* .
        :param vpc_settings: Specifies the VPC settings of the Microsoft AD directory server in AWS .
        :param create_alias: Specifies an alias for a directory and assigns the alias to the directory. The alias is used to construct the access URL for the directory, such as ``http://<alias>.awsapps.com`` . By default, AWS CloudFormation does not create an alias. .. epigraph:: After an alias has been created, it cannot be deleted or reused, so this operation should only be used when absolutely necessary.
        :param edition: AWS Managed Microsoft AD is available in two editions: ``Standard`` and ``Enterprise`` . ``Enterprise`` is the default.
        :param enable_sso: Whether to enable single sign-on for a Microsoft Active Directory in AWS . Single sign-on allows users in your directory to access certain AWS services from a computer joined to the directory without having to enter their credentials separately. If you don't specify a value, AWS CloudFormation disables single sign-on by default.
        :param short_name: The NetBIOS name for your domain, such as ``CORP`` . If you don't specify a NetBIOS name, it will default to the first part of your directory DNS. For example, ``CORP`` for the directory DNS ``corp.example.com`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd6139d8d11b9a68029fab0f5bc46297bfd5088edc6674f022f826f902974540)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMicrosoftADProps(
            name=name,
            password=password,
            vpc_settings=vpc_settings,
            create_alias=create_alias,
            edition=edition,
            enable_sso=enable_sso,
            short_name=short_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a9ef33ce2b22ad5e906e2065f5fb2a109d663bb39d8625ac1c9c5f9290535ae)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d1e2b70ea0a0fba7b268162287b083bdf946a088db50926682f3b81a48e403c4)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAlias")
    def attr_alias(self) -> builtins.str:
        '''The alias for a directory.

        For example: ``d-12373a053a`` or ``alias4-mydirectory-12345abcgmzsk`` (if you have the ``CreateAlias`` property set to true).

        :cloudformationAttribute: Alias
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAlias"))

    @builtins.property
    @jsii.member(jsii_name="attrDnsIpAddresses")
    def attr_dns_ip_addresses(self) -> typing.List[builtins.str]:
        '''The IP addresses of the DNS servers for the directory, such as ``[ "192.0.2.1", "192.0.2.2" ]`` .

        :cloudformationAttribute: DnsIpAddresses
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrDnsIpAddresses"))

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The fully qualified domain name for the AWS Managed Microsoft AD directory, such as ``corp.example.com`` . This name will resolve inside your VPC only. It does not need to be publicly resolvable.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__112fb8405e10bbc906f83d73e5b0af5f5a8ae854c04751ac6709698a11f478bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        '''The password for the default administrative user named ``Admin`` .'''
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cc760b5f2c2b02fc7c50f03f5673177e683887f7f392b34832edb453966e992)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="vpcSettings")
    def vpc_settings(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnMicrosoftAD.VpcSettingsProperty"]:
        '''Specifies the VPC settings of the Microsoft AD directory server in AWS .'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnMicrosoftAD.VpcSettingsProperty"], jsii.get(self, "vpcSettings"))

    @vpc_settings.setter
    def vpc_settings(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnMicrosoftAD.VpcSettingsProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75297793aadbe4453a84753658d85991f077c5f42c9305cc2731693d29a5901f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcSettings", value)

    @builtins.property
    @jsii.member(jsii_name="createAlias")
    def create_alias(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies an alias for a directory and assigns the alias to the directory.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "createAlias"))

    @create_alias.setter
    def create_alias(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62ec978df7e1a1e2437893c2704eb4532e0b65321074386cfb030c8e8a99864c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createAlias", value)

    @builtins.property
    @jsii.member(jsii_name="edition")
    def edition(self) -> typing.Optional[builtins.str]:
        '''AWS Managed Microsoft AD is available in two editions: ``Standard`` and ``Enterprise`` .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "edition"))

    @edition.setter
    def edition(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ced9c598d5743f53d4678f9dfb00a06806c9e1e7c95be7ac578beb7f417c6536)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "edition", value)

    @builtins.property
    @jsii.member(jsii_name="enableSso")
    def enable_sso(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to enable single sign-on for a Microsoft Active Directory in AWS .'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enableSso"))

    @enable_sso.setter
    def enable_sso(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ce84c71d0f4e6c8581052317cb887db3b1dcb81863f7e39f3f520193f6c5287)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableSso", value)

    @builtins.property
    @jsii.member(jsii_name="shortName")
    def short_name(self) -> typing.Optional[builtins.str]:
        '''The NetBIOS name for your domain, such as ``CORP`` .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shortName"))

    @short_name.setter
    def short_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d26767a53bfb3a106209fbda0be0dc95b0dc1f47eccfcf621e2a92ff21477680)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shortName", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_directoryservice.CfnMicrosoftAD.VpcSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"subnet_ids": "subnetIds", "vpc_id": "vpcId"},
    )
    class VpcSettingsProperty:
        def __init__(
            self,
            *,
            subnet_ids: typing.Sequence[builtins.str],
            vpc_id: builtins.str,
        ) -> None:
            '''Contains VPC information for the `CreateDirectory <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateDirectory.html>`_ or `CreateMicrosoftAD <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateMicrosoftAD.html>`_ operation.

            :param subnet_ids: The identifiers of the subnets for the directory servers. The two subnets must be in different Availability Zones. AWS Directory Service specifies a directory server and a DNS server in each of these subnets.
            :param vpc_id: The identifier of the VPC in which to create the directory.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-microsoftad-vpcsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_directoryservice as directoryservice
                
                vpc_settings_property = directoryservice.CfnMicrosoftAD.VpcSettingsProperty(
                    subnet_ids=["subnetIds"],
                    vpc_id="vpcId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__87466c9ba298d42dc628a07b7127a241f6cb9e589e939fff261e0dd1c007545e)
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
                check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "subnet_ids": subnet_ids,
                "vpc_id": vpc_id,
            }

        @builtins.property
        def subnet_ids(self) -> typing.List[builtins.str]:
            '''The identifiers of the subnets for the directory servers.

            The two subnets must be in different Availability Zones. AWS Directory Service specifies a directory server and a DNS server in each of these subnets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-microsoftad-vpcsettings.html#cfn-directoryservice-microsoftad-vpcsettings-subnetids
            '''
            result = self._values.get("subnet_ids")
            assert result is not None, "Required property 'subnet_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def vpc_id(self) -> builtins.str:
            '''The identifier of the VPC in which to create the directory.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-microsoftad-vpcsettings.html#cfn-directoryservice-microsoftad-vpcsettings-vpcid
            '''
            result = self._values.get("vpc_id")
            assert result is not None, "Required property 'vpc_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_directoryservice.CfnMicrosoftADProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "password": "password",
        "vpc_settings": "vpcSettings",
        "create_alias": "createAlias",
        "edition": "edition",
        "enable_sso": "enableSso",
        "short_name": "shortName",
    },
)
class CfnMicrosoftADProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        password: builtins.str,
        vpc_settings: typing.Union[_IResolvable_da3f097b, typing.Union[CfnMicrosoftAD.VpcSettingsProperty, typing.Dict[builtins.str, typing.Any]]],
        create_alias: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        edition: typing.Optional[builtins.str] = None,
        enable_sso: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        short_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnMicrosoftAD``.

        :param name: The fully qualified domain name for the AWS Managed Microsoft AD directory, such as ``corp.example.com`` . This name will resolve inside your VPC only. It does not need to be publicly resolvable.
        :param password: The password for the default administrative user named ``Admin`` . If you need to change the password for the administrator account, see the `ResetUserPassword <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ResetUserPassword.html>`_ API call in the *AWS Directory Service API Reference* .
        :param vpc_settings: Specifies the VPC settings of the Microsoft AD directory server in AWS .
        :param create_alias: Specifies an alias for a directory and assigns the alias to the directory. The alias is used to construct the access URL for the directory, such as ``http://<alias>.awsapps.com`` . By default, AWS CloudFormation does not create an alias. .. epigraph:: After an alias has been created, it cannot be deleted or reused, so this operation should only be used when absolutely necessary.
        :param edition: AWS Managed Microsoft AD is available in two editions: ``Standard`` and ``Enterprise`` . ``Enterprise`` is the default.
        :param enable_sso: Whether to enable single sign-on for a Microsoft Active Directory in AWS . Single sign-on allows users in your directory to access certain AWS services from a computer joined to the directory without having to enter their credentials separately. If you don't specify a value, AWS CloudFormation disables single sign-on by default.
        :param short_name: The NetBIOS name for your domain, such as ``CORP`` . If you don't specify a NetBIOS name, it will default to the first part of your directory DNS. For example, ``CORP`` for the directory DNS ``corp.example.com`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_directoryservice as directoryservice
            
            cfn_microsoft_aDProps = directoryservice.CfnMicrosoftADProps(
                name="name",
                password="password",
                vpc_settings=directoryservice.CfnMicrosoftAD.VpcSettingsProperty(
                    subnet_ids=["subnetIds"],
                    vpc_id="vpcId"
                ),
            
                # the properties below are optional
                create_alias=False,
                edition="edition",
                enable_sso=False,
                short_name="shortName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c02b262207b4026ffecfe6e07c2c9ad2212defb3dd9694e86dde27643f524b4f)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument vpc_settings", value=vpc_settings, expected_type=type_hints["vpc_settings"])
            check_type(argname="argument create_alias", value=create_alias, expected_type=type_hints["create_alias"])
            check_type(argname="argument edition", value=edition, expected_type=type_hints["edition"])
            check_type(argname="argument enable_sso", value=enable_sso, expected_type=type_hints["enable_sso"])
            check_type(argname="argument short_name", value=short_name, expected_type=type_hints["short_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "password": password,
            "vpc_settings": vpc_settings,
        }
        if create_alias is not None:
            self._values["create_alias"] = create_alias
        if edition is not None:
            self._values["edition"] = edition
        if enable_sso is not None:
            self._values["enable_sso"] = enable_sso
        if short_name is not None:
            self._values["short_name"] = short_name

    @builtins.property
    def name(self) -> builtins.str:
        '''The fully qualified domain name for the AWS Managed Microsoft AD directory, such as ``corp.example.com`` . This name will resolve inside your VPC only. It does not need to be publicly resolvable.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> builtins.str:
        '''The password for the default administrative user named ``Admin`` .

        If you need to change the password for the administrator account, see the `ResetUserPassword <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ResetUserPassword.html>`_ API call in the *AWS Directory Service API Reference* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-password
        '''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_settings(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnMicrosoftAD.VpcSettingsProperty]:
        '''Specifies the VPC settings of the Microsoft AD directory server in AWS .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-vpcsettings
        '''
        result = self._values.get("vpc_settings")
        assert result is not None, "Required property 'vpc_settings' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnMicrosoftAD.VpcSettingsProperty], result)

    @builtins.property
    def create_alias(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies an alias for a directory and assigns the alias to the directory.

        The alias is used to construct the access URL for the directory, such as ``http://<alias>.awsapps.com`` . By default, AWS CloudFormation does not create an alias.
        .. epigraph::

           After an alias has been created, it cannot be deleted or reused, so this operation should only be used when absolutely necessary.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-createalias
        '''
        result = self._values.get("create_alias")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def edition(self) -> typing.Optional[builtins.str]:
        '''AWS Managed Microsoft AD is available in two editions: ``Standard`` and ``Enterprise`` .

        ``Enterprise`` is the default.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-edition
        '''
        result = self._values.get("edition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_sso(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to enable single sign-on for a Microsoft Active Directory in AWS .

        Single sign-on allows users in your directory to access certain AWS services from a computer joined to the directory without having to enter their credentials separately. If you don't specify a value, AWS CloudFormation disables single sign-on by default.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-enablesso
        '''
        result = self._values.get("enable_sso")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def short_name(self) -> typing.Optional[builtins.str]:
        '''The NetBIOS name for your domain, such as ``CORP`` .

        If you don't specify a NetBIOS name, it will default to the first part of your directory DNS. For example, ``CORP`` for the directory DNS ``corp.example.com`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-shortname
        '''
        result = self._values.get("short_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMicrosoftADProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSimpleAD(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_directoryservice.CfnSimpleAD",
):
    '''The ``AWS::DirectoryService::SimpleAD`` resource specifies an AWS Directory Service Simple Active Directory ( Simple AD ) in AWS so that your directory users and groups can access the AWS Management Console and AWS applications using their existing credentials.

    Simple AD is a Microsoft Active Directory–compatible directory. For more information, see `Simple Active Directory <https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_simple_ad.html>`_ in the *AWS Directory Service Admin Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_directoryservice as directoryservice
        
        cfn_simple_aD = directoryservice.CfnSimpleAD(self, "MyCfnSimpleAD",
            name="name",
            size="size",
            vpc_settings=directoryservice.CfnSimpleAD.VpcSettingsProperty(
                subnet_ids=["subnetIds"],
                vpc_id="vpcId"
            ),
        
            # the properties below are optional
            create_alias=False,
            description="description",
            enable_sso=False,
            password="password",
            short_name="shortName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        size: builtins.str,
        vpc_settings: typing.Union[_IResolvable_da3f097b, typing.Union["CfnSimpleAD.VpcSettingsProperty", typing.Dict[builtins.str, typing.Any]]],
        create_alias: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        description: typing.Optional[builtins.str] = None,
        enable_sso: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        password: typing.Optional[builtins.str] = None,
        short_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The fully qualified name for the directory, such as ``corp.example.com`` .
        :param size: The size of the directory. For valid values, see `CreateDirectory <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateDirectory.html>`_ in the *AWS Directory Service API Reference* .
        :param vpc_settings: A `DirectoryVpcSettings <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DirectoryVpcSettings.html>`_ object that contains additional information for the operation.
        :param create_alias: If set to ``true`` , specifies an alias for a directory and assigns the alias to the directory. The alias is used to construct the access URL for the directory, such as ``http://<alias>.awsapps.com`` . By default, this property is set to ``false`` . .. epigraph:: After an alias has been created, it cannot be deleted or reused, so this operation should only be used when absolutely necessary.
        :param description: A description for the directory.
        :param enable_sso: Whether to enable single sign-on for a directory. If you don't specify a value, AWS CloudFormation disables single sign-on by default.
        :param password: The password for the directory administrator. The directory creation process creates a directory administrator account with the user name ``Administrator`` and this password. If you need to change the password for the administrator account, see the `ResetUserPassword <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ResetUserPassword.html>`_ API call in the *AWS Directory Service API Reference* .
        :param short_name: The NetBIOS name of the directory, such as ``CORP`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40820ee1ed03f2cd4befa65e6404c1024999677e0624ca5450f4b1f9220b604a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSimpleADProps(
            name=name,
            size=size,
            vpc_settings=vpc_settings,
            create_alias=create_alias,
            description=description,
            enable_sso=enable_sso,
            password=password,
            short_name=short_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adbd82c9a36437463cde56b3a4ad4d5c5c16f2073416fd9e1873351e5eb928b2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5a7e8b311879500ab8eb669b71e4c719b95dd8d686723498b45ea89664345e41)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAlias")
    def attr_alias(self) -> builtins.str:
        '''The alias for a directory.

        For example: ``d-12373a053a`` or ``alias4-mydirectory-12345abcgmzsk`` (if you have the ``CreateAlias`` property set to true).

        :cloudformationAttribute: Alias
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAlias"))

    @builtins.property
    @jsii.member(jsii_name="attrDirectoryId")
    def attr_directory_id(self) -> builtins.str:
        '''The unique identifier for a directory.

        :cloudformationAttribute: DirectoryId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDirectoryId"))

    @builtins.property
    @jsii.member(jsii_name="attrDnsIpAddresses")
    def attr_dns_ip_addresses(self) -> typing.List[builtins.str]:
        '''The IP addresses of the DNS servers for the directory, such as ``[ "172.31.3.154", "172.31.63.203" ]`` .

        :cloudformationAttribute: DnsIpAddresses
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrDnsIpAddresses"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The fully qualified name for the directory, such as ``corp.example.com`` .'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3a78121d492cd58fc500f705f47004309952863836f8d6363c085425d61b5e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> builtins.str:
        '''The size of the directory.'''
        return typing.cast(builtins.str, jsii.get(self, "size"))

    @size.setter
    def size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c947223df100c39d3ba17f1ff698114d9a307629c47fd70256f83e548f4784ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="vpcSettings")
    def vpc_settings(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnSimpleAD.VpcSettingsProperty"]:
        '''A `DirectoryVpcSettings <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DirectoryVpcSettings.html>`_ object that contains additional information for the operation.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnSimpleAD.VpcSettingsProperty"], jsii.get(self, "vpcSettings"))

    @vpc_settings.setter
    def vpc_settings(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnSimpleAD.VpcSettingsProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6428aafed6f7ca93dde6ec0c6f047a3df0f1e0611e08f0e547ace9ba88f2405f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcSettings", value)

    @builtins.property
    @jsii.member(jsii_name="createAlias")
    def create_alias(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''If set to ``true`` , specifies an alias for a directory and assigns the alias to the directory.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "createAlias"))

    @create_alias.setter
    def create_alias(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fd6c1eca9f65d5acc1c1fa49fb9c2d7595239e452ab418012abd1a20597b5f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createAlias", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the directory.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f523334b45fcfb70dccb3363e6ec46cc38283b1a77028b92e89f62fd48ac31d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="enableSso")
    def enable_sso(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to enable single sign-on for a directory.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enableSso"))

    @enable_sso.setter
    def enable_sso(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c87bb88b5d4bdf801ed5bb1eff487991cd1104ca7311fda40c4c7666e682d3f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableSso", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> typing.Optional[builtins.str]:
        '''The password for the directory administrator.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "password"))

    @password.setter
    def password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71aba9c326c0546afb2bfadc98225001babe64951c885082746f7d7f8553bf37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="shortName")
    def short_name(self) -> typing.Optional[builtins.str]:
        '''The NetBIOS name of the directory, such as ``CORP`` .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shortName"))

    @short_name.setter
    def short_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c28a5ea3ad534ce7feaf34230d92ea3e87c2179d359d490a286a8b1936fcf350)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shortName", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_directoryservice.CfnSimpleAD.VpcSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"subnet_ids": "subnetIds", "vpc_id": "vpcId"},
    )
    class VpcSettingsProperty:
        def __init__(
            self,
            *,
            subnet_ids: typing.Sequence[builtins.str],
            vpc_id: builtins.str,
        ) -> None:
            '''Contains VPC information for the `CreateDirectory <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateDirectory.html>`_ or `CreateMicrosoftAD <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateMicrosoftAD.html>`_ operation.

            :param subnet_ids: The identifiers of the subnets for the directory servers. The two subnets must be in different Availability Zones. AWS Directory Service specifies a directory server and a DNS server in each of these subnets.
            :param vpc_id: The identifier of the VPC in which to create the directory.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-simplead-vpcsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_directoryservice as directoryservice
                
                vpc_settings_property = directoryservice.CfnSimpleAD.VpcSettingsProperty(
                    subnet_ids=["subnetIds"],
                    vpc_id="vpcId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c8735fadd5f261261242f08594a8935a9e3119659f4d14301a33cd4a4858ea92)
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
                check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "subnet_ids": subnet_ids,
                "vpc_id": vpc_id,
            }

        @builtins.property
        def subnet_ids(self) -> typing.List[builtins.str]:
            '''The identifiers of the subnets for the directory servers.

            The two subnets must be in different Availability Zones. AWS Directory Service specifies a directory server and a DNS server in each of these subnets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-simplead-vpcsettings.html#cfn-directoryservice-simplead-vpcsettings-subnetids
            '''
            result = self._values.get("subnet_ids")
            assert result is not None, "Required property 'subnet_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def vpc_id(self) -> builtins.str:
            '''The identifier of the VPC in which to create the directory.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-simplead-vpcsettings.html#cfn-directoryservice-simplead-vpcsettings-vpcid
            '''
            result = self._values.get("vpc_id")
            assert result is not None, "Required property 'vpc_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_directoryservice.CfnSimpleADProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "size": "size",
        "vpc_settings": "vpcSettings",
        "create_alias": "createAlias",
        "description": "description",
        "enable_sso": "enableSso",
        "password": "password",
        "short_name": "shortName",
    },
)
class CfnSimpleADProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        size: builtins.str,
        vpc_settings: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSimpleAD.VpcSettingsProperty, typing.Dict[builtins.str, typing.Any]]],
        create_alias: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        description: typing.Optional[builtins.str] = None,
        enable_sso: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        password: typing.Optional[builtins.str] = None,
        short_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnSimpleAD``.

        :param name: The fully qualified name for the directory, such as ``corp.example.com`` .
        :param size: The size of the directory. For valid values, see `CreateDirectory <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateDirectory.html>`_ in the *AWS Directory Service API Reference* .
        :param vpc_settings: A `DirectoryVpcSettings <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DirectoryVpcSettings.html>`_ object that contains additional information for the operation.
        :param create_alias: If set to ``true`` , specifies an alias for a directory and assigns the alias to the directory. The alias is used to construct the access URL for the directory, such as ``http://<alias>.awsapps.com`` . By default, this property is set to ``false`` . .. epigraph:: After an alias has been created, it cannot be deleted or reused, so this operation should only be used when absolutely necessary.
        :param description: A description for the directory.
        :param enable_sso: Whether to enable single sign-on for a directory. If you don't specify a value, AWS CloudFormation disables single sign-on by default.
        :param password: The password for the directory administrator. The directory creation process creates a directory administrator account with the user name ``Administrator`` and this password. If you need to change the password for the administrator account, see the `ResetUserPassword <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ResetUserPassword.html>`_ API call in the *AWS Directory Service API Reference* .
        :param short_name: The NetBIOS name of the directory, such as ``CORP`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_directoryservice as directoryservice
            
            cfn_simple_aDProps = directoryservice.CfnSimpleADProps(
                name="name",
                size="size",
                vpc_settings=directoryservice.CfnSimpleAD.VpcSettingsProperty(
                    subnet_ids=["subnetIds"],
                    vpc_id="vpcId"
                ),
            
                # the properties below are optional
                create_alias=False,
                description="description",
                enable_sso=False,
                password="password",
                short_name="shortName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d5efbbc1a7e54cd5f61f8ab3a76dddee5c6468a07c2da3178587e1a05f5f11b)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument vpc_settings", value=vpc_settings, expected_type=type_hints["vpc_settings"])
            check_type(argname="argument create_alias", value=create_alias, expected_type=type_hints["create_alias"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enable_sso", value=enable_sso, expected_type=type_hints["enable_sso"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument short_name", value=short_name, expected_type=type_hints["short_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "size": size,
            "vpc_settings": vpc_settings,
        }
        if create_alias is not None:
            self._values["create_alias"] = create_alias
        if description is not None:
            self._values["description"] = description
        if enable_sso is not None:
            self._values["enable_sso"] = enable_sso
        if password is not None:
            self._values["password"] = password
        if short_name is not None:
            self._values["short_name"] = short_name

    @builtins.property
    def name(self) -> builtins.str:
        '''The fully qualified name for the directory, such as ``corp.example.com`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def size(self) -> builtins.str:
        '''The size of the directory.

        For valid values, see `CreateDirectory <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateDirectory.html>`_ in the *AWS Directory Service API Reference* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-size
        '''
        result = self._values.get("size")
        assert result is not None, "Required property 'size' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_settings(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnSimpleAD.VpcSettingsProperty]:
        '''A `DirectoryVpcSettings <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DirectoryVpcSettings.html>`_ object that contains additional information for the operation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-vpcsettings
        '''
        result = self._values.get("vpc_settings")
        assert result is not None, "Required property 'vpc_settings' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnSimpleAD.VpcSettingsProperty], result)

    @builtins.property
    def create_alias(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''If set to ``true`` , specifies an alias for a directory and assigns the alias to the directory.

        The alias is used to construct the access URL for the directory, such as ``http://<alias>.awsapps.com`` . By default, this property is set to ``false`` .
        .. epigraph::

           After an alias has been created, it cannot be deleted or reused, so this operation should only be used when absolutely necessary.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-createalias
        '''
        result = self._values.get("create_alias")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the directory.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_sso(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to enable single sign-on for a directory.

        If you don't specify a value, AWS CloudFormation disables single sign-on by default.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-enablesso
        '''
        result = self._values.get("enable_sso")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The password for the directory administrator.

        The directory creation process creates a directory administrator account with the user name ``Administrator`` and this password.

        If you need to change the password for the administrator account, see the `ResetUserPassword <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ResetUserPassword.html>`_ API call in the *AWS Directory Service API Reference* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-password
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def short_name(self) -> typing.Optional[builtins.str]:
        '''The NetBIOS name of the directory, such as ``CORP`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-shortname
        '''
        result = self._values.get("short_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSimpleADProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnMicrosoftAD",
    "CfnMicrosoftADProps",
    "CfnSimpleAD",
    "CfnSimpleADProps",
]

publication.publish()

def _typecheckingstub__bd6139d8d11b9a68029fab0f5bc46297bfd5088edc6674f022f826f902974540(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    password: builtins.str,
    vpc_settings: typing.Union[_IResolvable_da3f097b, typing.Union[CfnMicrosoftAD.VpcSettingsProperty, typing.Dict[builtins.str, typing.Any]]],
    create_alias: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    edition: typing.Optional[builtins.str] = None,
    enable_sso: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    short_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a9ef33ce2b22ad5e906e2065f5fb2a109d663bb39d8625ac1c9c5f9290535ae(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1e2b70ea0a0fba7b268162287b083bdf946a088db50926682f3b81a48e403c4(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__112fb8405e10bbc906f83d73e5b0af5f5a8ae854c04751ac6709698a11f478bb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cc760b5f2c2b02fc7c50f03f5673177e683887f7f392b34832edb453966e992(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75297793aadbe4453a84753658d85991f077c5f42c9305cc2731693d29a5901f(
    value: typing.Union[_IResolvable_da3f097b, CfnMicrosoftAD.VpcSettingsProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62ec978df7e1a1e2437893c2704eb4532e0b65321074386cfb030c8e8a99864c(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ced9c598d5743f53d4678f9dfb00a06806c9e1e7c95be7ac578beb7f417c6536(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ce84c71d0f4e6c8581052317cb887db3b1dcb81863f7e39f3f520193f6c5287(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d26767a53bfb3a106209fbda0be0dc95b0dc1f47eccfcf621e2a92ff21477680(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87466c9ba298d42dc628a07b7127a241f6cb9e589e939fff261e0dd1c007545e(
    *,
    subnet_ids: typing.Sequence[builtins.str],
    vpc_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c02b262207b4026ffecfe6e07c2c9ad2212defb3dd9694e86dde27643f524b4f(
    *,
    name: builtins.str,
    password: builtins.str,
    vpc_settings: typing.Union[_IResolvable_da3f097b, typing.Union[CfnMicrosoftAD.VpcSettingsProperty, typing.Dict[builtins.str, typing.Any]]],
    create_alias: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    edition: typing.Optional[builtins.str] = None,
    enable_sso: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    short_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40820ee1ed03f2cd4befa65e6404c1024999677e0624ca5450f4b1f9220b604a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    size: builtins.str,
    vpc_settings: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSimpleAD.VpcSettingsProperty, typing.Dict[builtins.str, typing.Any]]],
    create_alias: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    description: typing.Optional[builtins.str] = None,
    enable_sso: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    password: typing.Optional[builtins.str] = None,
    short_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adbd82c9a36437463cde56b3a4ad4d5c5c16f2073416fd9e1873351e5eb928b2(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a7e8b311879500ab8eb669b71e4c719b95dd8d686723498b45ea89664345e41(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3a78121d492cd58fc500f705f47004309952863836f8d6363c085425d61b5e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c947223df100c39d3ba17f1ff698114d9a307629c47fd70256f83e548f4784ab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6428aafed6f7ca93dde6ec0c6f047a3df0f1e0611e08f0e547ace9ba88f2405f(
    value: typing.Union[_IResolvable_da3f097b, CfnSimpleAD.VpcSettingsProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fd6c1eca9f65d5acc1c1fa49fb9c2d7595239e452ab418012abd1a20597b5f3(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f523334b45fcfb70dccb3363e6ec46cc38283b1a77028b92e89f62fd48ac31d6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c87bb88b5d4bdf801ed5bb1eff487991cd1104ca7311fda40c4c7666e682d3f6(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71aba9c326c0546afb2bfadc98225001babe64951c885082746f7d7f8553bf37(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c28a5ea3ad534ce7feaf34230d92ea3e87c2179d359d490a286a8b1936fcf350(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8735fadd5f261261242f08594a8935a9e3119659f4d14301a33cd4a4858ea92(
    *,
    subnet_ids: typing.Sequence[builtins.str],
    vpc_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d5efbbc1a7e54cd5f61f8ab3a76dddee5c6468a07c2da3178587e1a05f5f11b(
    *,
    name: builtins.str,
    size: builtins.str,
    vpc_settings: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSimpleAD.VpcSettingsProperty, typing.Dict[builtins.str, typing.Any]]],
    create_alias: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    description: typing.Optional[builtins.str] = None,
    enable_sso: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    password: typing.Optional[builtins.str] = None,
    short_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
