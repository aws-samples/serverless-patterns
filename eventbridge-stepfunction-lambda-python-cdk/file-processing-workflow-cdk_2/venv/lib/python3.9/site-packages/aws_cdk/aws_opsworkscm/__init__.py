'''
# AWS OpsWorks CM Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_opsworkscm as opsworkscm
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for OpsWorksCM construct libraries](https://constructs.dev/search?q=opsworkscm)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::OpsWorksCM resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_OpsWorksCM.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::OpsWorksCM](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_OpsWorksCM.html).

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
class CfnServer(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_opsworkscm.CfnServer",
):
    '''The ``AWS::OpsWorksCM::Server`` resource creates an AWS OpsWorks for Chef Automate or OpsWorks for Puppet Enterprise configuration management server.

    For more information, see `Create a Chef Automate Server in AWS CloudFormation <https://docs.aws.amazon.com/opsworks/latest/userguide/opscm-create-server-cfn.html>`_ or `Create a Puppet Enterprise Master in AWS CloudFormation <https://docs.aws.amazon.com/opsworks/latest/userguide/opspup-create-server-cfn.html>`_ in the *AWS OpsWorks User Guide* , and `CreateServer <https://docs.aws.amazon.com/opsworks-cm/latest/APIReference/API_CreateServer.html>`_ in the *AWS OpsWorks CM API Reference* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_opsworkscm as opsworkscm
        
        cfn_server = opsworkscm.CfnServer(self, "MyCfnServer",
            instance_profile_arn="instanceProfileArn",
            instance_type="instanceType",
            service_role_arn="serviceRoleArn",
        
            # the properties below are optional
            associate_public_ip_address=False,
            backup_id="backupId",
            backup_retention_count=123,
            custom_certificate="customCertificate",
            custom_domain="customDomain",
            custom_private_key="customPrivateKey",
            disable_automated_backup=False,
            engine="engine",
            engine_attributes=[opsworkscm.CfnServer.EngineAttributeProperty(
                name="name",
                value="value"
            )],
            engine_model="engineModel",
            engine_version="engineVersion",
            key_pair="keyPair",
            preferred_backup_window="preferredBackupWindow",
            preferred_maintenance_window="preferredMaintenanceWindow",
            security_group_ids=["securityGroupIds"],
            server_name="serverName",
            subnet_ids=["subnetIds"],
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
        instance_profile_arn: builtins.str,
        instance_type: builtins.str,
        service_role_arn: builtins.str,
        associate_public_ip_address: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        backup_id: typing.Optional[builtins.str] = None,
        backup_retention_count: typing.Optional[jsii.Number] = None,
        custom_certificate: typing.Optional[builtins.str] = None,
        custom_domain: typing.Optional[builtins.str] = None,
        custom_private_key: typing.Optional[builtins.str] = None,
        disable_automated_backup: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        engine: typing.Optional[builtins.str] = None,
        engine_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnServer.EngineAttributeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        engine_model: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        key_pair: typing.Optional[builtins.str] = None,
        preferred_backup_window: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        server_name: typing.Optional[builtins.str] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param instance_profile_arn: The ARN of the instance profile that your Amazon EC2 instances use.
        :param instance_type: The Amazon EC2 instance type to use. For example, ``m5.large`` .
        :param service_role_arn: The service role that the AWS OpsWorks CM service backend uses to work with your account. Although the AWS OpsWorks management console typically creates the service role for you, if you are using the AWS CLI or API commands, run the service-role-creation.yaml AWS CloudFormation template, located at https://s3.amazonaws.com/opsworks-cm-us-east-1-prod-default-assets/misc/opsworks-cm-roles.yaml. This template creates a CloudFormation stack that includes the service role and instance profile that you need.
        :param associate_public_ip_address: Associate a public IP address with a server that you are launching. Valid values are ``true`` or ``false`` . The default value is ``true`` .
        :param backup_id: If you specify this field, AWS OpsWorks CM creates the server by using the backup represented by BackupId.
        :param backup_retention_count: The number of automated backups that you want to keep. Whenever a new backup is created, AWS OpsWorks CM deletes the oldest backups if this number is exceeded. The default value is ``1`` .
        :param custom_certificate: Supported on servers running Chef Automate 2.0 only. A PEM-formatted HTTPS certificate. The value can be be a single, self-signed certificate, or a certificate chain. If you specify a custom certificate, you must also specify values for ``CustomDomain`` and ``CustomPrivateKey`` . The following are requirements for the ``CustomCertificate`` value:. - You can provide either a self-signed, custom certificate, or the full certificate chain. - The certificate must be a valid X509 certificate, or a certificate chain in PEM format. - The certificate must be valid at the time of upload. A certificate can't be used before its validity period begins (the certificate's ``NotBefore`` date), or after it expires (the certificate's ``NotAfter`` date). - The certificate’s common name or subject alternative names (SANs), if present, must match the value of ``CustomDomain`` . - The certificate must match the value of ``CustomPrivateKey`` .
        :param custom_domain: Supported on servers running Chef Automate 2.0 only. An optional public endpoint of a server, such as ``https://aws.my-company.com`` . To access the server, create a CNAME DNS record in your preferred DNS service that points the custom domain to the endpoint that is generated when the server is created (the value of the CreateServer Endpoint attribute). You cannot access the server by using the generated ``Endpoint`` value if the server is using a custom domain. If you specify a custom domain, you must also specify values for ``CustomCertificate`` and ``CustomPrivateKey`` .
        :param custom_private_key: Supported on servers running Chef Automate 2.0 only. A private key in PEM format for connecting to the server by using HTTPS. The private key must not be encrypted; it cannot be protected by a password or passphrase. If you specify a custom private key, you must also specify values for ``CustomDomain`` and ``CustomCertificate`` .
        :param disable_automated_backup: Enable or disable scheduled backups. Valid values are ``true`` or ``false`` . The default value is ``true`` .
        :param engine: The configuration management engine to use. Valid values include ``ChefAutomate`` and ``Puppet`` .
        :param engine_attributes: Optional engine attributes on a specified server. **Attributes accepted in a Chef createServer request:** - ``CHEF_AUTOMATE_PIVOTAL_KEY`` : A base64-encoded RSA public key. The corresponding private key is required to access the Chef API. When no CHEF_AUTOMATE_PIVOTAL_KEY is set, a private key is generated and returned in the response. When you are specifying the value of CHEF_AUTOMATE_PIVOTAL_KEY as a parameter in the AWS CloudFormation console, you must add newline ( ``\\n`` ) characters at the end of each line of the pivotal key value. - ``CHEF_AUTOMATE_ADMIN_PASSWORD`` : The password for the administrative user in the Chef Automate web-based dashboard. The password length is a minimum of eight characters, and a maximum of 32. The password can contain letters, numbers, and special characters (!/@#$%^&+=_). The password must contain at least one lower case letter, one upper case letter, one number, and one special character. When no CHEF_AUTOMATE_ADMIN_PASSWORD is set, one is generated and returned in the response. **Attributes accepted in a Puppet createServer request:** - ``PUPPET_ADMIN_PASSWORD`` : To work with the Puppet Enterprise console, a password must use ASCII characters. - ``PUPPET_R10K_REMOTE`` : The r10k remote is the URL of your control repository (for example, ssh://git@your.git-repo.com:user/control-repo.git). Specifying an r10k remote opens TCP port 8170. - ``PUPPET_R10K_PRIVATE_KEY`` : If you are using a private Git repository, add PUPPET_R10K_PRIVATE_KEY to specify a PEM-encoded private SSH key.
        :param engine_model: The engine model of the server. Valid values in this release include ``Monolithic`` for Puppet and ``Single`` for Chef.
        :param engine_version: The major release version of the engine that you want to use. For a Chef server, the valid value for EngineVersion is currently ``2`` . For a Puppet server, valid values are ``2019`` or ``2017`` .
        :param key_pair: The Amazon EC2 key pair to set for the instance. This parameter is optional; if desired, you may specify this parameter to connect to your instances by using SSH.
        :param preferred_backup_window: The start time for a one-hour period during which AWS OpsWorks CM backs up application-level data on your server if automated backups are enabled. Valid values must be specified in one of the following formats: - ``HH:MM`` for daily backups - ``DDD:HH:MM`` for weekly backups ``MM`` must be specified as ``00`` . The specified time is in coordinated universal time (UTC). The default value is a random, daily start time. *Example:* ``08:00`` , which represents a daily start time of 08:00 UTC. *Example:* ``Mon:08:00`` , which represents a start time of every Monday at 08:00 UTC. (8:00 a.m.)
        :param preferred_maintenance_window: The start time for a one-hour period each week during which AWS OpsWorks CM performs maintenance on the instance. Valid values must be specified in the following format: ``DDD:HH:MM`` . ``MM`` must be specified as ``00`` . The specified time is in coordinated universal time (UTC). The default value is a random one-hour period on Tuesday, Wednesday, or Friday. See ``TimeWindowDefinition`` for more information. *Example:* ``Mon:08:00`` , which represents a start time of every Monday at 08:00 UTC. (8:00 a.m.)
        :param security_group_ids: A list of security group IDs to attach to the Amazon EC2 instance. If you add this parameter, the specified security groups must be within the VPC that is specified by ``SubnetIds`` . If you do not specify this parameter, AWS OpsWorks CM creates one new security group that uses TCP ports 22 and 443, open to 0.0.0.0/0 (everyone).
        :param server_name: 
        :param subnet_ids: The IDs of subnets in which to launch the server EC2 instance. Amazon EC2-Classic customers: This field is required. All servers must run within a VPC. The VPC must have "Auto Assign Public IP" enabled. EC2-VPC customers: This field is optional. If you do not specify subnet IDs, your EC2 instances are created in a default subnet that is selected by Amazon EC2. If you specify subnet IDs, the VPC must have "Auto Assign Public IP" enabled. For more information about supported Amazon EC2 platforms, see `Supported Platforms <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-platforms.html>`_ .
        :param tags: A map that contains tag keys and tag values to attach to an AWS OpsWorks for Chef Automate or OpsWorks for Puppet Enterprise server. - The key cannot be empty. - The key can be a maximum of 127 characters, and can contain only Unicode letters, numbers, or separators, or the following special characters: `+ - = . _ : /
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fcf3005231c62e7682797d2e25d33ceb0c0b9602a2f2ffe6a7c3dabf9da5450)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnServerProps(
            instance_profile_arn=instance_profile_arn,
            instance_type=instance_type,
            service_role_arn=service_role_arn,
            associate_public_ip_address=associate_public_ip_address,
            backup_id=backup_id,
            backup_retention_count=backup_retention_count,
            custom_certificate=custom_certificate,
            custom_domain=custom_domain,
            custom_private_key=custom_private_key,
            disable_automated_backup=disable_automated_backup,
            engine=engine,
            engine_attributes=engine_attributes,
            engine_model=engine_model,
            engine_version=engine_version,
            key_pair=key_pair,
            preferred_backup_window=preferred_backup_window,
            preferred_maintenance_window=preferred_maintenance_window,
            security_group_ids=security_group_ids,
            server_name=server_name,
            subnet_ids=subnet_ids,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19f2feeaf9088052d1e3d91318248757951a8853d230fb27b822589707fba494)
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
            type_hints = typing.get_type_hints(_typecheckingstub__04f0ea48bc08ee57eae94ea7e74cde1be9a4eb55ead4693f6becb5ba26cbdd90)
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
        '''The Amazon Resource Name (ARN) of the server, such as ``arn:aws:OpsWorksCM:us-east-1:123456789012:server/server-a1bzhi`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrEndpoint")
    def attr_endpoint(self) -> builtins.str:
        '''A DNS name that can be used to access the engine.

        Example: ``myserver-asdfghjkl.us-east-1.opsworks.io`` .

        :cloudformationAttribute: Endpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="attrServerName")
    def attr_server_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: ServerName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServerName"))

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
    @jsii.member(jsii_name="instanceProfileArn")
    def instance_profile_arn(self) -> builtins.str:
        '''The ARN of the instance profile that your Amazon EC2 instances use.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceProfileArn"))

    @instance_profile_arn.setter
    def instance_profile_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cea404186dae083539bd261d91a2f704a0ad4ec99d3abe052a149ec64595f96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceProfileArn", value)

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        '''The Amazon EC2 instance type to use.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3258bb290dc0840f3f119cff658102d64e3429e9d5268528b404ca2ecf77aae5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="serviceRoleArn")
    def service_role_arn(self) -> builtins.str:
        '''The service role that the AWS OpsWorks CM service backend uses to work with your account.'''
        return typing.cast(builtins.str, jsii.get(self, "serviceRoleArn"))

    @service_role_arn.setter
    def service_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27e33b0e01ec2af856c064c8227863649264c091a560be64ce5e0057d50e27e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="associatePublicIpAddress")
    def associate_public_ip_address(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Associate a public IP address with a server that you are launching.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "associatePublicIpAddress"))

    @associate_public_ip_address.setter
    def associate_public_ip_address(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3c45f815d3ef6098f824925685877dd7c49f4e57de602dc79fe506c8adeab8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associatePublicIpAddress", value)

    @builtins.property
    @jsii.member(jsii_name="backupId")
    def backup_id(self) -> typing.Optional[builtins.str]:
        '''If you specify this field, AWS OpsWorks CM creates the server by using the backup represented by BackupId.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backupId"))

    @backup_id.setter
    def backup_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ff36405f0c4238b4f820f697148f11af2c945cc9e1512bdbf6a26697c92bac2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupId", value)

    @builtins.property
    @jsii.member(jsii_name="backupRetentionCount")
    def backup_retention_count(self) -> typing.Optional[jsii.Number]:
        '''The number of automated backups that you want to keep.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "backupRetentionCount"))

    @backup_retention_count.setter
    def backup_retention_count(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__602a97f999cfcf118a833fda9b050dc1c19210323de39137eae7639fa35fa512)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupRetentionCount", value)

    @builtins.property
    @jsii.member(jsii_name="customCertificate")
    def custom_certificate(self) -> typing.Optional[builtins.str]:
        '''Supported on servers running Chef Automate 2.0 only. A PEM-formatted HTTPS certificate. The value can be be a single, self-signed certificate, or a certificate chain. If you specify a custom certificate, you must also specify values for ``CustomDomain`` and ``CustomPrivateKey`` . The following are requirements for the ``CustomCertificate`` value:.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customCertificate"))

    @custom_certificate.setter
    def custom_certificate(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65e65fd3bac358e350993fab131e8924caaa5509a261eb6929615ea06d6aa40f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="customDomain")
    def custom_domain(self) -> typing.Optional[builtins.str]:
        '''Supported on servers running Chef Automate 2.0 only. An optional public endpoint of a server, such as ``https://aws.my-company.com`` . To access the server, create a CNAME DNS record in your preferred DNS service that points the custom domain to the endpoint that is generated when the server is created (the value of the CreateServer Endpoint attribute). You cannot access the server by using the generated ``Endpoint`` value if the server is using a custom domain. If you specify a custom domain, you must also specify values for ``CustomCertificate`` and ``CustomPrivateKey`` .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customDomain"))

    @custom_domain.setter
    def custom_domain(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49d14cd4b4c8a5a3194a4dc123e3b901df963d3dce3180595609cc817dbcf699)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customDomain", value)

    @builtins.property
    @jsii.member(jsii_name="customPrivateKey")
    def custom_private_key(self) -> typing.Optional[builtins.str]:
        '''Supported on servers running Chef Automate 2.0 only. A private key in PEM format for connecting to the server by using HTTPS. The private key must not be encrypted; it cannot be protected by a password or passphrase. If you specify a custom private key, you must also specify values for ``CustomDomain`` and ``CustomCertificate`` .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customPrivateKey"))

    @custom_private_key.setter
    def custom_private_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39571623019f045a76d90d7f9729edd88d7d6963801142ea34b3c8153919a142)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customPrivateKey", value)

    @builtins.property
    @jsii.member(jsii_name="disableAutomatedBackup")
    def disable_automated_backup(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Enable or disable scheduled backups.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "disableAutomatedBackup"))

    @disable_automated_backup.setter
    def disable_automated_backup(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b46443fdafed279ac49545af3fa84aa00384aacb75e125ca14388f79d9cfb786)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableAutomatedBackup", value)

    @builtins.property
    @jsii.member(jsii_name="engine")
    def engine(self) -> typing.Optional[builtins.str]:
        '''The configuration management engine to use.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engine"))

    @engine.setter
    def engine(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d41af7192af6a5b257f30522feb9b821520405f3d11fdcc7845a94b8d910f44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engine", value)

    @builtins.property
    @jsii.member(jsii_name="engineAttributes")
    def engine_attributes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnServer.EngineAttributeProperty"]]]]:
        '''Optional engine attributes on a specified server.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnServer.EngineAttributeProperty"]]]], jsii.get(self, "engineAttributes"))

    @engine_attributes.setter
    def engine_attributes(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnServer.EngineAttributeProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__348bb1528287c10d8bc70ea5676023d151054ec708b5c1cba5a2b8ec906b759b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engineAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="engineModel")
    def engine_model(self) -> typing.Optional[builtins.str]:
        '''The engine model of the server.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engineModel"))

    @engine_model.setter
    def engine_model(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cb402a1e7248fab4c783a38c551c26fc366f3d61896f1dad658eddde63b52a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engineModel", value)

    @builtins.property
    @jsii.member(jsii_name="engineVersion")
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''The major release version of the engine that you want to use.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engineVersion"))

    @engine_version.setter
    def engine_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15e50201c5f7c3740fbea434ec68a86d658a7e64e35b180f30aaa5f9594f858c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engineVersion", value)

    @builtins.property
    @jsii.member(jsii_name="keyPair")
    def key_pair(self) -> typing.Optional[builtins.str]:
        '''The Amazon EC2 key pair to set for the instance.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyPair"))

    @key_pair.setter
    def key_pair(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d73128a54fec0b519b3d2b7e1aa04cb520dc6435e37c750821725b46ddcdf0d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyPair", value)

    @builtins.property
    @jsii.member(jsii_name="preferredBackupWindow")
    def preferred_backup_window(self) -> typing.Optional[builtins.str]:
        '''The start time for a one-hour period during which AWS OpsWorks CM backs up application-level data on your server if automated backups are enabled.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredBackupWindow"))

    @preferred_backup_window.setter
    def preferred_backup_window(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64463af4a3732dff3189eb07ca005e06511180ee587cbd4997c7ba95ea989072)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredBackupWindow", value)

    @builtins.property
    @jsii.member(jsii_name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''The start time for a one-hour period each week during which AWS OpsWorks CM performs maintenance on the instance.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredMaintenanceWindow"))

    @preferred_maintenance_window.setter
    def preferred_maintenance_window(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b24b9a8fe79cad6d7297372ca05dcffd87916dc46d9475f22e55bcac954c78ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredMaintenanceWindow", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of security group IDs to attach to the Amazon EC2 instance.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7663e937d0fabd66d40de7584fca886669aae87261a418b199493778688eb09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="serverName")
    def server_name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverName"))

    @server_name.setter
    def server_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fdc9b0c6ccfb79b318a5321a2bdb7586f084e301b627e9b708804bad96c9238)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverName", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The IDs of subnets in which to launch the server EC2 instance.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6d133d8dd209b40a7f4c3900293e312fe8b95abc9cfff43e88a6fd1608b595b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A map that contains tag keys and tag values to attach to an AWS OpsWorks for Chef Automate or OpsWorks for Puppet Enterprise server.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f1391da7f04a55c9f7f9adf16c4634190fb6dbb84aa6805530fa127a387881e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_opsworkscm.CfnServer.EngineAttributeProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class EngineAttributeProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``EngineAttribute`` property type specifies administrator credentials for an AWS OpsWorks for Chef Automate or OpsWorks for Puppet Enterprise server.

            ``EngineAttribute`` is a property of the ``AWS::OpsWorksCM::Server`` resource type.

            :param name: The name of the engine attribute. *Attribute name for Chef Automate servers:* - ``CHEF_AUTOMATE_ADMIN_PASSWORD`` *Attribute names for Puppet Enterprise servers:* - ``PUPPET_ADMIN_PASSWORD`` - ``PUPPET_R10K_REMOTE`` - ``PUPPET_R10K_PRIVATE_KEY``
            :param value: The value of the engine attribute. *Attribute value for Chef Automate servers:* - ``CHEF_AUTOMATE_PIVOTAL_KEY`` : A base64-encoded RSA public key. The corresponding private key is required to access the Chef API. You can generate this key by running the following `OpenSSL <https://docs.aws.amazon.com/https://www.openssl.org/>`_ command on Linux-based computers. ``openssl genrsa -out *pivotal_key_file_name* .pem 2048`` On Windows-based computers, you can use the PuTTYgen utility to generate a base64-encoded RSA private key. For more information, see `PuTTYgen - Key Generator for PuTTY on Windows <https://docs.aws.amazon.com/https://www.ssh.com/ssh/putty/windows/puttygen>`_ on SSH.com. *Attribute values for Puppet Enterprise servers:* - ``PUPPET_ADMIN_PASSWORD`` : An administrator password that you can use to sign in to the Puppet Enterprise console webpage after the server is online. The password must use between 8 and 32 ASCII characters. - ``PUPPET_R10K_REMOTE`` : The r10k remote is the URL of your control repository (for example, ssh://git@your.git-repo.com:user/control-repo.git). Specifying an r10k remote opens TCP port 8170. - ``PUPPET_R10K_PRIVATE_KEY`` : If you are using a private Git repository, add ``PUPPET_R10K_PRIVATE_KEY`` to specify a PEM-encoded private SSH key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworkscm-server-engineattribute.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_opsworkscm as opsworkscm
                
                engine_attribute_property = opsworkscm.CfnServer.EngineAttributeProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__67fded34344e0064de0c9f210bea59e7367c41094d8989087df77f333f754b2b)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the engine attribute.

            *Attribute name for Chef Automate servers:*

            - ``CHEF_AUTOMATE_ADMIN_PASSWORD``

            *Attribute names for Puppet Enterprise servers:*

            - ``PUPPET_ADMIN_PASSWORD``
            - ``PUPPET_R10K_REMOTE``
            - ``PUPPET_R10K_PRIVATE_KEY``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworkscm-server-engineattribute.html#cfn-opsworkscm-server-engineattribute-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The value of the engine attribute.

            *Attribute value for Chef Automate servers:*

            - ``CHEF_AUTOMATE_PIVOTAL_KEY`` : A base64-encoded RSA public key. The corresponding private key is required to access the Chef API. You can generate this key by running the following `OpenSSL <https://docs.aws.amazon.com/https://www.openssl.org/>`_ command on Linux-based computers.

            ``openssl genrsa -out *pivotal_key_file_name* .pem 2048``

            On Windows-based computers, you can use the PuTTYgen utility to generate a base64-encoded RSA private key. For more information, see `PuTTYgen - Key Generator for PuTTY on Windows <https://docs.aws.amazon.com/https://www.ssh.com/ssh/putty/windows/puttygen>`_ on SSH.com.

            *Attribute values for Puppet Enterprise servers:*

            - ``PUPPET_ADMIN_PASSWORD`` : An administrator password that you can use to sign in to the Puppet Enterprise console webpage after the server is online. The password must use between 8 and 32 ASCII characters.
            - ``PUPPET_R10K_REMOTE`` : The r10k remote is the URL of your control repository (for example, ssh://git@your.git-repo.com:user/control-repo.git). Specifying an r10k remote opens TCP port 8170.
            - ``PUPPET_R10K_PRIVATE_KEY`` : If you are using a private Git repository, add ``PUPPET_R10K_PRIVATE_KEY`` to specify a PEM-encoded private SSH key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworkscm-server-engineattribute.html#cfn-opsworkscm-server-engineattribute-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EngineAttributeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_opsworkscm.CfnServerProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_profile_arn": "instanceProfileArn",
        "instance_type": "instanceType",
        "service_role_arn": "serviceRoleArn",
        "associate_public_ip_address": "associatePublicIpAddress",
        "backup_id": "backupId",
        "backup_retention_count": "backupRetentionCount",
        "custom_certificate": "customCertificate",
        "custom_domain": "customDomain",
        "custom_private_key": "customPrivateKey",
        "disable_automated_backup": "disableAutomatedBackup",
        "engine": "engine",
        "engine_attributes": "engineAttributes",
        "engine_model": "engineModel",
        "engine_version": "engineVersion",
        "key_pair": "keyPair",
        "preferred_backup_window": "preferredBackupWindow",
        "preferred_maintenance_window": "preferredMaintenanceWindow",
        "security_group_ids": "securityGroupIds",
        "server_name": "serverName",
        "subnet_ids": "subnetIds",
        "tags": "tags",
    },
)
class CfnServerProps:
    def __init__(
        self,
        *,
        instance_profile_arn: builtins.str,
        instance_type: builtins.str,
        service_role_arn: builtins.str,
        associate_public_ip_address: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        backup_id: typing.Optional[builtins.str] = None,
        backup_retention_count: typing.Optional[jsii.Number] = None,
        custom_certificate: typing.Optional[builtins.str] = None,
        custom_domain: typing.Optional[builtins.str] = None,
        custom_private_key: typing.Optional[builtins.str] = None,
        disable_automated_backup: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        engine: typing.Optional[builtins.str] = None,
        engine_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServer.EngineAttributeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        engine_model: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        key_pair: typing.Optional[builtins.str] = None,
        preferred_backup_window: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        server_name: typing.Optional[builtins.str] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnServer``.

        :param instance_profile_arn: The ARN of the instance profile that your Amazon EC2 instances use.
        :param instance_type: The Amazon EC2 instance type to use. For example, ``m5.large`` .
        :param service_role_arn: The service role that the AWS OpsWorks CM service backend uses to work with your account. Although the AWS OpsWorks management console typically creates the service role for you, if you are using the AWS CLI or API commands, run the service-role-creation.yaml AWS CloudFormation template, located at https://s3.amazonaws.com/opsworks-cm-us-east-1-prod-default-assets/misc/opsworks-cm-roles.yaml. This template creates a CloudFormation stack that includes the service role and instance profile that you need.
        :param associate_public_ip_address: Associate a public IP address with a server that you are launching. Valid values are ``true`` or ``false`` . The default value is ``true`` .
        :param backup_id: If you specify this field, AWS OpsWorks CM creates the server by using the backup represented by BackupId.
        :param backup_retention_count: The number of automated backups that you want to keep. Whenever a new backup is created, AWS OpsWorks CM deletes the oldest backups if this number is exceeded. The default value is ``1`` .
        :param custom_certificate: Supported on servers running Chef Automate 2.0 only. A PEM-formatted HTTPS certificate. The value can be be a single, self-signed certificate, or a certificate chain. If you specify a custom certificate, you must also specify values for ``CustomDomain`` and ``CustomPrivateKey`` . The following are requirements for the ``CustomCertificate`` value:. - You can provide either a self-signed, custom certificate, or the full certificate chain. - The certificate must be a valid X509 certificate, or a certificate chain in PEM format. - The certificate must be valid at the time of upload. A certificate can't be used before its validity period begins (the certificate's ``NotBefore`` date), or after it expires (the certificate's ``NotAfter`` date). - The certificate’s common name or subject alternative names (SANs), if present, must match the value of ``CustomDomain`` . - The certificate must match the value of ``CustomPrivateKey`` .
        :param custom_domain: Supported on servers running Chef Automate 2.0 only. An optional public endpoint of a server, such as ``https://aws.my-company.com`` . To access the server, create a CNAME DNS record in your preferred DNS service that points the custom domain to the endpoint that is generated when the server is created (the value of the CreateServer Endpoint attribute). You cannot access the server by using the generated ``Endpoint`` value if the server is using a custom domain. If you specify a custom domain, you must also specify values for ``CustomCertificate`` and ``CustomPrivateKey`` .
        :param custom_private_key: Supported on servers running Chef Automate 2.0 only. A private key in PEM format for connecting to the server by using HTTPS. The private key must not be encrypted; it cannot be protected by a password or passphrase. If you specify a custom private key, you must also specify values for ``CustomDomain`` and ``CustomCertificate`` .
        :param disable_automated_backup: Enable or disable scheduled backups. Valid values are ``true`` or ``false`` . The default value is ``true`` .
        :param engine: The configuration management engine to use. Valid values include ``ChefAutomate`` and ``Puppet`` .
        :param engine_attributes: Optional engine attributes on a specified server. **Attributes accepted in a Chef createServer request:** - ``CHEF_AUTOMATE_PIVOTAL_KEY`` : A base64-encoded RSA public key. The corresponding private key is required to access the Chef API. When no CHEF_AUTOMATE_PIVOTAL_KEY is set, a private key is generated and returned in the response. When you are specifying the value of CHEF_AUTOMATE_PIVOTAL_KEY as a parameter in the AWS CloudFormation console, you must add newline ( ``\\n`` ) characters at the end of each line of the pivotal key value. - ``CHEF_AUTOMATE_ADMIN_PASSWORD`` : The password for the administrative user in the Chef Automate web-based dashboard. The password length is a minimum of eight characters, and a maximum of 32. The password can contain letters, numbers, and special characters (!/@#$%^&+=_). The password must contain at least one lower case letter, one upper case letter, one number, and one special character. When no CHEF_AUTOMATE_ADMIN_PASSWORD is set, one is generated and returned in the response. **Attributes accepted in a Puppet createServer request:** - ``PUPPET_ADMIN_PASSWORD`` : To work with the Puppet Enterprise console, a password must use ASCII characters. - ``PUPPET_R10K_REMOTE`` : The r10k remote is the URL of your control repository (for example, ssh://git@your.git-repo.com:user/control-repo.git). Specifying an r10k remote opens TCP port 8170. - ``PUPPET_R10K_PRIVATE_KEY`` : If you are using a private Git repository, add PUPPET_R10K_PRIVATE_KEY to specify a PEM-encoded private SSH key.
        :param engine_model: The engine model of the server. Valid values in this release include ``Monolithic`` for Puppet and ``Single`` for Chef.
        :param engine_version: The major release version of the engine that you want to use. For a Chef server, the valid value for EngineVersion is currently ``2`` . For a Puppet server, valid values are ``2019`` or ``2017`` .
        :param key_pair: The Amazon EC2 key pair to set for the instance. This parameter is optional; if desired, you may specify this parameter to connect to your instances by using SSH.
        :param preferred_backup_window: The start time for a one-hour period during which AWS OpsWorks CM backs up application-level data on your server if automated backups are enabled. Valid values must be specified in one of the following formats: - ``HH:MM`` for daily backups - ``DDD:HH:MM`` for weekly backups ``MM`` must be specified as ``00`` . The specified time is in coordinated universal time (UTC). The default value is a random, daily start time. *Example:* ``08:00`` , which represents a daily start time of 08:00 UTC. *Example:* ``Mon:08:00`` , which represents a start time of every Monday at 08:00 UTC. (8:00 a.m.)
        :param preferred_maintenance_window: The start time for a one-hour period each week during which AWS OpsWorks CM performs maintenance on the instance. Valid values must be specified in the following format: ``DDD:HH:MM`` . ``MM`` must be specified as ``00`` . The specified time is in coordinated universal time (UTC). The default value is a random one-hour period on Tuesday, Wednesday, or Friday. See ``TimeWindowDefinition`` for more information. *Example:* ``Mon:08:00`` , which represents a start time of every Monday at 08:00 UTC. (8:00 a.m.)
        :param security_group_ids: A list of security group IDs to attach to the Amazon EC2 instance. If you add this parameter, the specified security groups must be within the VPC that is specified by ``SubnetIds`` . If you do not specify this parameter, AWS OpsWorks CM creates one new security group that uses TCP ports 22 and 443, open to 0.0.0.0/0 (everyone).
        :param server_name: 
        :param subnet_ids: The IDs of subnets in which to launch the server EC2 instance. Amazon EC2-Classic customers: This field is required. All servers must run within a VPC. The VPC must have "Auto Assign Public IP" enabled. EC2-VPC customers: This field is optional. If you do not specify subnet IDs, your EC2 instances are created in a default subnet that is selected by Amazon EC2. If you specify subnet IDs, the VPC must have "Auto Assign Public IP" enabled. For more information about supported Amazon EC2 platforms, see `Supported Platforms <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-platforms.html>`_ .
        :param tags: A map that contains tag keys and tag values to attach to an AWS OpsWorks for Chef Automate or OpsWorks for Puppet Enterprise server. - The key cannot be empty. - The key can be a maximum of 127 characters, and can contain only Unicode letters, numbers, or separators, or the following special characters: `+ - = . _ : /

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_opsworkscm as opsworkscm
            
            cfn_server_props = opsworkscm.CfnServerProps(
                instance_profile_arn="instanceProfileArn",
                instance_type="instanceType",
                service_role_arn="serviceRoleArn",
            
                # the properties below are optional
                associate_public_ip_address=False,
                backup_id="backupId",
                backup_retention_count=123,
                custom_certificate="customCertificate",
                custom_domain="customDomain",
                custom_private_key="customPrivateKey",
                disable_automated_backup=False,
                engine="engine",
                engine_attributes=[opsworkscm.CfnServer.EngineAttributeProperty(
                    name="name",
                    value="value"
                )],
                engine_model="engineModel",
                engine_version="engineVersion",
                key_pair="keyPair",
                preferred_backup_window="preferredBackupWindow",
                preferred_maintenance_window="preferredMaintenanceWindow",
                security_group_ids=["securityGroupIds"],
                server_name="serverName",
                subnet_ids=["subnetIds"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f3d9a63c768f1a40206835320dfa128b267da1fa702fbb4ecd8ac94b87e6841)
            check_type(argname="argument instance_profile_arn", value=instance_profile_arn, expected_type=type_hints["instance_profile_arn"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument service_role_arn", value=service_role_arn, expected_type=type_hints["service_role_arn"])
            check_type(argname="argument associate_public_ip_address", value=associate_public_ip_address, expected_type=type_hints["associate_public_ip_address"])
            check_type(argname="argument backup_id", value=backup_id, expected_type=type_hints["backup_id"])
            check_type(argname="argument backup_retention_count", value=backup_retention_count, expected_type=type_hints["backup_retention_count"])
            check_type(argname="argument custom_certificate", value=custom_certificate, expected_type=type_hints["custom_certificate"])
            check_type(argname="argument custom_domain", value=custom_domain, expected_type=type_hints["custom_domain"])
            check_type(argname="argument custom_private_key", value=custom_private_key, expected_type=type_hints["custom_private_key"])
            check_type(argname="argument disable_automated_backup", value=disable_automated_backup, expected_type=type_hints["disable_automated_backup"])
            check_type(argname="argument engine", value=engine, expected_type=type_hints["engine"])
            check_type(argname="argument engine_attributes", value=engine_attributes, expected_type=type_hints["engine_attributes"])
            check_type(argname="argument engine_model", value=engine_model, expected_type=type_hints["engine_model"])
            check_type(argname="argument engine_version", value=engine_version, expected_type=type_hints["engine_version"])
            check_type(argname="argument key_pair", value=key_pair, expected_type=type_hints["key_pair"])
            check_type(argname="argument preferred_backup_window", value=preferred_backup_window, expected_type=type_hints["preferred_backup_window"])
            check_type(argname="argument preferred_maintenance_window", value=preferred_maintenance_window, expected_type=type_hints["preferred_maintenance_window"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument server_name", value=server_name, expected_type=type_hints["server_name"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_profile_arn": instance_profile_arn,
            "instance_type": instance_type,
            "service_role_arn": service_role_arn,
        }
        if associate_public_ip_address is not None:
            self._values["associate_public_ip_address"] = associate_public_ip_address
        if backup_id is not None:
            self._values["backup_id"] = backup_id
        if backup_retention_count is not None:
            self._values["backup_retention_count"] = backup_retention_count
        if custom_certificate is not None:
            self._values["custom_certificate"] = custom_certificate
        if custom_domain is not None:
            self._values["custom_domain"] = custom_domain
        if custom_private_key is not None:
            self._values["custom_private_key"] = custom_private_key
        if disable_automated_backup is not None:
            self._values["disable_automated_backup"] = disable_automated_backup
        if engine is not None:
            self._values["engine"] = engine
        if engine_attributes is not None:
            self._values["engine_attributes"] = engine_attributes
        if engine_model is not None:
            self._values["engine_model"] = engine_model
        if engine_version is not None:
            self._values["engine_version"] = engine_version
        if key_pair is not None:
            self._values["key_pair"] = key_pair
        if preferred_backup_window is not None:
            self._values["preferred_backup_window"] = preferred_backup_window
        if preferred_maintenance_window is not None:
            self._values["preferred_maintenance_window"] = preferred_maintenance_window
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if server_name is not None:
            self._values["server_name"] = server_name
        if subnet_ids is not None:
            self._values["subnet_ids"] = subnet_ids
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def instance_profile_arn(self) -> builtins.str:
        '''The ARN of the instance profile that your Amazon EC2 instances use.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-instanceprofilearn
        '''
        result = self._values.get("instance_profile_arn")
        assert result is not None, "Required property 'instance_profile_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_type(self) -> builtins.str:
        '''The Amazon EC2 instance type to use.

        For example, ``m5.large`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-instancetype
        '''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_role_arn(self) -> builtins.str:
        '''The service role that the AWS OpsWorks CM service backend uses to work with your account.

        Although the AWS OpsWorks management console typically creates the service role for you, if you are using the AWS CLI or API commands, run the service-role-creation.yaml AWS CloudFormation template, located at https://s3.amazonaws.com/opsworks-cm-us-east-1-prod-default-assets/misc/opsworks-cm-roles.yaml. This template creates a CloudFormation stack that includes the service role and instance profile that you need.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-servicerolearn
        '''
        result = self._values.get("service_role_arn")
        assert result is not None, "Required property 'service_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def associate_public_ip_address(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Associate a public IP address with a server that you are launching.

        Valid values are ``true`` or ``false`` . The default value is ``true`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-associatepublicipaddress
        '''
        result = self._values.get("associate_public_ip_address")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def backup_id(self) -> typing.Optional[builtins.str]:
        '''If you specify this field, AWS OpsWorks CM creates the server by using the backup represented by BackupId.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-backupid
        '''
        result = self._values.get("backup_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backup_retention_count(self) -> typing.Optional[jsii.Number]:
        '''The number of automated backups that you want to keep.

        Whenever a new backup is created, AWS OpsWorks CM deletes the oldest backups if this number is exceeded. The default value is ``1`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-backupretentioncount
        '''
        result = self._values.get("backup_retention_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def custom_certificate(self) -> typing.Optional[builtins.str]:
        '''Supported on servers running Chef Automate 2.0 only. A PEM-formatted HTTPS certificate. The value can be be a single, self-signed certificate, or a certificate chain. If you specify a custom certificate, you must also specify values for ``CustomDomain`` and ``CustomPrivateKey`` . The following are requirements for the ``CustomCertificate`` value:.

        - You can provide either a self-signed, custom certificate, or the full certificate chain.
        - The certificate must be a valid X509 certificate, or a certificate chain in PEM format.
        - The certificate must be valid at the time of upload. A certificate can't be used before its validity period begins (the certificate's ``NotBefore`` date), or after it expires (the certificate's ``NotAfter`` date).
        - The certificate’s common name or subject alternative names (SANs), if present, must match the value of ``CustomDomain`` .
        - The certificate must match the value of ``CustomPrivateKey`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-customcertificate
        '''
        result = self._values.get("custom_certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_domain(self) -> typing.Optional[builtins.str]:
        '''Supported on servers running Chef Automate 2.0 only. An optional public endpoint of a server, such as ``https://aws.my-company.com`` . To access the server, create a CNAME DNS record in your preferred DNS service that points the custom domain to the endpoint that is generated when the server is created (the value of the CreateServer Endpoint attribute). You cannot access the server by using the generated ``Endpoint`` value if the server is using a custom domain. If you specify a custom domain, you must also specify values for ``CustomCertificate`` and ``CustomPrivateKey`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-customdomain
        '''
        result = self._values.get("custom_domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_private_key(self) -> typing.Optional[builtins.str]:
        '''Supported on servers running Chef Automate 2.0 only. A private key in PEM format for connecting to the server by using HTTPS. The private key must not be encrypted; it cannot be protected by a password or passphrase. If you specify a custom private key, you must also specify values for ``CustomDomain`` and ``CustomCertificate`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-customprivatekey
        '''
        result = self._values.get("custom_private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_automated_backup(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Enable or disable scheduled backups.

        Valid values are ``true`` or ``false`` . The default value is ``true`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-disableautomatedbackup
        '''
        result = self._values.get("disable_automated_backup")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def engine(self) -> typing.Optional[builtins.str]:
        '''The configuration management engine to use.

        Valid values include ``ChefAutomate`` and ``Puppet`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-engine
        '''
        result = self._values.get("engine")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def engine_attributes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnServer.EngineAttributeProperty]]]]:
        '''Optional engine attributes on a specified server.

        **Attributes accepted in a Chef createServer request:** - ``CHEF_AUTOMATE_PIVOTAL_KEY`` : A base64-encoded RSA public key. The corresponding private key is required to access the Chef API. When no CHEF_AUTOMATE_PIVOTAL_KEY is set, a private key is generated and returned in the response. When you are specifying the value of CHEF_AUTOMATE_PIVOTAL_KEY as a parameter in the AWS CloudFormation console, you must add newline ( ``\\n`` ) characters at the end of each line of the pivotal key value.

        - ``CHEF_AUTOMATE_ADMIN_PASSWORD`` : The password for the administrative user in the Chef Automate web-based dashboard. The password length is a minimum of eight characters, and a maximum of 32. The password can contain letters, numbers, and special characters (!/@#$%^&+=_). The password must contain at least one lower case letter, one upper case letter, one number, and one special character. When no CHEF_AUTOMATE_ADMIN_PASSWORD is set, one is generated and returned in the response.

        **Attributes accepted in a Puppet createServer request:** - ``PUPPET_ADMIN_PASSWORD`` : To work with the Puppet Enterprise console, a password must use ASCII characters.

        - ``PUPPET_R10K_REMOTE`` : The r10k remote is the URL of your control repository (for example, ssh://git@your.git-repo.com:user/control-repo.git). Specifying an r10k remote opens TCP port 8170.
        - ``PUPPET_R10K_PRIVATE_KEY`` : If you are using a private Git repository, add PUPPET_R10K_PRIVATE_KEY to specify a PEM-encoded private SSH key.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-engineattributes
        '''
        result = self._values.get("engine_attributes")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnServer.EngineAttributeProperty]]]], result)

    @builtins.property
    def engine_model(self) -> typing.Optional[builtins.str]:
        '''The engine model of the server.

        Valid values in this release include ``Monolithic`` for Puppet and ``Single`` for Chef.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-enginemodel
        '''
        result = self._values.get("engine_model")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''The major release version of the engine that you want to use.

        For a Chef server, the valid value for EngineVersion is currently ``2`` . For a Puppet server, valid values are ``2019`` or ``2017`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-engineversion
        '''
        result = self._values.get("engine_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_pair(self) -> typing.Optional[builtins.str]:
        '''The Amazon EC2 key pair to set for the instance.

        This parameter is optional; if desired, you may specify this parameter to connect to your instances by using SSH.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-keypair
        '''
        result = self._values.get("key_pair")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preferred_backup_window(self) -> typing.Optional[builtins.str]:
        '''The start time for a one-hour period during which AWS OpsWorks CM backs up application-level data on your server if automated backups are enabled.

        Valid values must be specified in one of the following formats:

        - ``HH:MM`` for daily backups
        - ``DDD:HH:MM`` for weekly backups

        ``MM`` must be specified as ``00`` . The specified time is in coordinated universal time (UTC). The default value is a random, daily start time.

        *Example:* ``08:00`` , which represents a daily start time of 08:00 UTC.

        *Example:* ``Mon:08:00`` , which represents a start time of every Monday at 08:00 UTC. (8:00 a.m.)

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-preferredbackupwindow
        '''
        result = self._values.get("preferred_backup_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''The start time for a one-hour period each week during which AWS OpsWorks CM performs maintenance on the instance.

        Valid values must be specified in the following format: ``DDD:HH:MM`` . ``MM`` must be specified as ``00`` . The specified time is in coordinated universal time (UTC). The default value is a random one-hour period on Tuesday, Wednesday, or Friday. See ``TimeWindowDefinition`` for more information.

        *Example:* ``Mon:08:00`` , which represents a start time of every Monday at 08:00 UTC. (8:00 a.m.)

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-preferredmaintenancewindow
        '''
        result = self._values.get("preferred_maintenance_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of security group IDs to attach to the Amazon EC2 instance.

        If you add this parameter, the specified security groups must be within the VPC that is specified by ``SubnetIds`` .

        If you do not specify this parameter, AWS OpsWorks CM creates one new security group that uses TCP ports 22 and 443, open to 0.0.0.0/0 (everyone).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-securitygroupids
        '''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def server_name(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-servername
        '''
        result = self._values.get("server_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The IDs of subnets in which to launch the server EC2 instance.

        Amazon EC2-Classic customers: This field is required. All servers must run within a VPC. The VPC must have "Auto Assign Public IP" enabled.

        EC2-VPC customers: This field is optional. If you do not specify subnet IDs, your EC2 instances are created in a default subnet that is selected by Amazon EC2. If you specify subnet IDs, the VPC must have "Auto Assign Public IP" enabled.

        For more information about supported Amazon EC2 platforms, see `Supported Platforms <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-platforms.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-subnetids
        '''
        result = self._values.get("subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A map that contains tag keys and tag values to attach to an AWS OpsWorks for Chef Automate or OpsWorks for Puppet Enterprise server.

        - The key cannot be empty.
        - The key can be a maximum of 127 characters, and can contain only Unicode letters, numbers, or separators, or the following special characters: `+ - = . _ : /

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html#cfn-opsworkscm-server-tags
        ::

        `

        - The value can be a maximum 255 characters, and contain only Unicode letters, numbers, or separators, or the following special characters: ``+ - = . _ : / @``
        - Leading and trailing spaces are trimmed from both the key and value.
        - A maximum of 50 user-applied tags is allowed for any AWS OpsWorks CM server.
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnServer",
    "CfnServerProps",
]

publication.publish()

def _typecheckingstub__4fcf3005231c62e7682797d2e25d33ceb0c0b9602a2f2ffe6a7c3dabf9da5450(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instance_profile_arn: builtins.str,
    instance_type: builtins.str,
    service_role_arn: builtins.str,
    associate_public_ip_address: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    backup_id: typing.Optional[builtins.str] = None,
    backup_retention_count: typing.Optional[jsii.Number] = None,
    custom_certificate: typing.Optional[builtins.str] = None,
    custom_domain: typing.Optional[builtins.str] = None,
    custom_private_key: typing.Optional[builtins.str] = None,
    disable_automated_backup: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    engine: typing.Optional[builtins.str] = None,
    engine_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServer.EngineAttributeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    engine_model: typing.Optional[builtins.str] = None,
    engine_version: typing.Optional[builtins.str] = None,
    key_pair: typing.Optional[builtins.str] = None,
    preferred_backup_window: typing.Optional[builtins.str] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    server_name: typing.Optional[builtins.str] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19f2feeaf9088052d1e3d91318248757951a8853d230fb27b822589707fba494(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04f0ea48bc08ee57eae94ea7e74cde1be9a4eb55ead4693f6becb5ba26cbdd90(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cea404186dae083539bd261d91a2f704a0ad4ec99d3abe052a149ec64595f96(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3258bb290dc0840f3f119cff658102d64e3429e9d5268528b404ca2ecf77aae5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27e33b0e01ec2af856c064c8227863649264c091a560be64ce5e0057d50e27e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3c45f815d3ef6098f824925685877dd7c49f4e57de602dc79fe506c8adeab8a(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ff36405f0c4238b4f820f697148f11af2c945cc9e1512bdbf6a26697c92bac2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__602a97f999cfcf118a833fda9b050dc1c19210323de39137eae7639fa35fa512(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65e65fd3bac358e350993fab131e8924caaa5509a261eb6929615ea06d6aa40f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49d14cd4b4c8a5a3194a4dc123e3b901df963d3dce3180595609cc817dbcf699(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39571623019f045a76d90d7f9729edd88d7d6963801142ea34b3c8153919a142(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b46443fdafed279ac49545af3fa84aa00384aacb75e125ca14388f79d9cfb786(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d41af7192af6a5b257f30522feb9b821520405f3d11fdcc7845a94b8d910f44(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__348bb1528287c10d8bc70ea5676023d151054ec708b5c1cba5a2b8ec906b759b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnServer.EngineAttributeProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cb402a1e7248fab4c783a38c551c26fc366f3d61896f1dad658eddde63b52a8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15e50201c5f7c3740fbea434ec68a86d658a7e64e35b180f30aaa5f9594f858c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d73128a54fec0b519b3d2b7e1aa04cb520dc6435e37c750821725b46ddcdf0d5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64463af4a3732dff3189eb07ca005e06511180ee587cbd4997c7ba95ea989072(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b24b9a8fe79cad6d7297372ca05dcffd87916dc46d9475f22e55bcac954c78ea(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7663e937d0fabd66d40de7584fca886669aae87261a418b199493778688eb09(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fdc9b0c6ccfb79b318a5321a2bdb7586f084e301b627e9b708804bad96c9238(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6d133d8dd209b40a7f4c3900293e312fe8b95abc9cfff43e88a6fd1608b595b(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f1391da7f04a55c9f7f9adf16c4634190fb6dbb84aa6805530fa127a387881e(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67fded34344e0064de0c9f210bea59e7367c41094d8989087df77f333f754b2b(
    *,
    name: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f3d9a63c768f1a40206835320dfa128b267da1fa702fbb4ecd8ac94b87e6841(
    *,
    instance_profile_arn: builtins.str,
    instance_type: builtins.str,
    service_role_arn: builtins.str,
    associate_public_ip_address: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    backup_id: typing.Optional[builtins.str] = None,
    backup_retention_count: typing.Optional[jsii.Number] = None,
    custom_certificate: typing.Optional[builtins.str] = None,
    custom_domain: typing.Optional[builtins.str] = None,
    custom_private_key: typing.Optional[builtins.str] = None,
    disable_automated_backup: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    engine: typing.Optional[builtins.str] = None,
    engine_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServer.EngineAttributeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    engine_model: typing.Optional[builtins.str] = None,
    engine_version: typing.Optional[builtins.str] = None,
    key_pair: typing.Optional[builtins.str] = None,
    preferred_backup_window: typing.Optional[builtins.str] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    server_name: typing.Optional[builtins.str] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
