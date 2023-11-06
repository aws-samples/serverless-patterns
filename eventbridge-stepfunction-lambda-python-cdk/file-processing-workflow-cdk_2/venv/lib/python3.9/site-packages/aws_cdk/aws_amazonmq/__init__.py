'''
# Amazon MQ Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_amazonmq as amazonmq
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for AmazonMQ construct libraries](https://constructs.dev/search?q=amazonmq)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::AmazonMQ resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AmazonMQ.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::AmazonMQ](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AmazonMQ.html).

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
    ITaggable as _ITaggable_36806126,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnBroker(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_amazonmq.CfnBroker",
):
    '''A *broker* is a message broker environment running on Amazon MQ .

    It is the basic building block of Amazon MQ .

    The ``AWS::AmazonMQ::Broker`` resource lets you create Amazon MQ for ActiveMQ and Amazon MQ for RabbitMQ brokers, add configuration changes or modify users for a speified ActiveMQ broker, return information about the specified broker, and delete the broker. For more information, see `How Amazon MQ works <https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/amazon-mq-how-it-works.html>`_ in the *Amazon MQ Developer Guide* .

    - ``ec2:CreateNetworkInterface``

    This permission is required to allow Amazon MQ to create an elastic network interface (ENI) on behalf of your account.

    - ``ec2:CreateNetworkInterfacePermission``

    This permission is required to attach the ENI to the broker instance.

    - ``ec2:DeleteNetworkInterface``
    - ``ec2:DeleteNetworkInterfacePermission``
    - ``ec2:DetachNetworkInterface``
    - ``ec2:DescribeInternetGateways``
    - ``ec2:DescribeNetworkInterfaces``
    - ``ec2:DescribeNetworkInterfacePermissions``
    - ``ec2:DescribeRouteTables``
    - ``ec2:DescribeSecurityGroups``
    - ``ec2:DescribeSubnets``
    - ``ec2:DescribeVpcs``

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_amazonmq as amazonmq
        
        cfn_broker = amazonmq.CfnBroker(self, "MyCfnBroker",
            auto_minor_version_upgrade=False,
            broker_name="brokerName",
            deployment_mode="deploymentMode",
            engine_type="engineType",
            engine_version="engineVersion",
            host_instance_type="hostInstanceType",
            publicly_accessible=False,
            users=[amazonmq.CfnBroker.UserProperty(
                password="password",
                username="username",
        
                # the properties below are optional
                console_access=False,
                groups=["groups"]
            )],
        
            # the properties below are optional
            authentication_strategy="authenticationStrategy",
            configuration=amazonmq.CfnBroker.ConfigurationIdProperty(
                id="id",
                revision=123
            ),
            data_replication_mode="dataReplicationMode",
            data_replication_primary_broker_arn="dataReplicationPrimaryBrokerArn",
            encryption_options=amazonmq.CfnBroker.EncryptionOptionsProperty(
                use_aws_owned_key=False,
        
                # the properties below are optional
                kms_key_id="kmsKeyId"
            ),
            ldap_server_metadata=amazonmq.CfnBroker.LdapServerMetadataProperty(
                hosts=["hosts"],
                role_base="roleBase",
                role_search_matching="roleSearchMatching",
                service_account_password="serviceAccountPassword",
                service_account_username="serviceAccountUsername",
                user_base="userBase",
                user_search_matching="userSearchMatching",
        
                # the properties below are optional
                role_name="roleName",
                role_search_subtree=False,
                user_role_name="userRoleName",
                user_search_subtree=False
            ),
            logs=amazonmq.CfnBroker.LogListProperty(
                audit=False,
                general=False
            ),
            maintenance_window_start_time=amazonmq.CfnBroker.MaintenanceWindowProperty(
                day_of_week="dayOfWeek",
                time_of_day="timeOfDay",
                time_zone="timeZone"
            ),
            security_groups=["securityGroups"],
            storage_type="storageType",
            subnet_ids=["subnetIds"],
            tags=[amazonmq.CfnBroker.TagsEntryProperty(
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
        auto_minor_version_upgrade: typing.Union[builtins.bool, _IResolvable_da3f097b],
        broker_name: builtins.str,
        deployment_mode: builtins.str,
        engine_type: builtins.str,
        engine_version: builtins.str,
        host_instance_type: builtins.str,
        publicly_accessible: typing.Union[builtins.bool, _IResolvable_da3f097b],
        users: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBroker.UserProperty", typing.Dict[builtins.str, typing.Any]]]]],
        authentication_strategy: typing.Optional[builtins.str] = None,
        configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBroker.ConfigurationIdProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        data_replication_mode: typing.Optional[builtins.str] = None,
        data_replication_primary_broker_arn: typing.Optional[builtins.str] = None,
        encryption_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBroker.EncryptionOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ldap_server_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBroker.LdapServerMetadataProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBroker.LogListProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        maintenance_window_start_time: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBroker.MaintenanceWindowProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        storage_type: typing.Optional[builtins.str] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["CfnBroker.TagsEntryProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param auto_minor_version_upgrade: Enables automatic upgrades to new minor versions for brokers, as new broker engine versions are released and supported by Amazon MQ. Automatic upgrades occur during the scheduled maintenance window of the broker or after a manual broker reboot.
        :param broker_name: The name of the broker. This value must be unique in your AWS account , 1-50 characters long, must contain only letters, numbers, dashes, and underscores, and must not contain white spaces, brackets, wildcard characters, or special characters. .. epigraph:: Do not add personally identifiable information (PII) or other confidential or sensitive information in broker names. Broker names are accessible to other AWS services, including C CloudWatch Logs . Broker names are not intended to be used for private or sensitive data.
        :param deployment_mode: The deployment mode of the broker. Available values:. - ``SINGLE_INSTANCE`` - ``ACTIVE_STANDBY_MULTI_AZ`` - ``CLUSTER_MULTI_AZ``
        :param engine_type: The type of broker engine. Currently, Amazon MQ supports ``ACTIVEMQ`` and ``RABBITMQ`` .
        :param engine_version: The version of the broker engine. For a list of supported engine versions, see `Engine <https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html>`_ in the *Amazon MQ Developer Guide* .
        :param host_instance_type: The broker's instance type.
        :param publicly_accessible: Enables connections from applications outside of the VPC that hosts the broker's subnets.
        :param users: The list of broker users (persons or applications) who can access queues and topics. For Amazon MQ for RabbitMQ brokers, one and only one administrative user is accepted and created when a broker is first provisioned. All subsequent RabbitMQ users are created by via the RabbitMQ web console or by using the RabbitMQ management API.
        :param authentication_strategy: Optional. The authentication strategy used to secure the broker. The default is ``SIMPLE`` .
        :param configuration: A list of information about the configuration. Does not apply to RabbitMQ brokers.
        :param data_replication_mode: 
        :param data_replication_primary_broker_arn: 
        :param encryption_options: Encryption options for the broker. Does not apply to RabbitMQ brokers.
        :param ldap_server_metadata: Optional. The metadata of the LDAP server used to authenticate and authorize connections to the broker. Does not apply to RabbitMQ brokers.
        :param logs: Enables Amazon CloudWatch logging for brokers.
        :param maintenance_window_start_time: The scheduled time period relative to UTC during which Amazon MQ begins to apply pending updates or patches to the broker.
        :param security_groups: The list of rules (1 minimum, 125 maximum) that authorize connections to brokers.
        :param storage_type: The broker's storage type.
        :param subnet_ids: The list of groups that define which subnets and IP ranges the broker can use from different Availability Zones. If you specify more than one subnet, the subnets must be in different Availability Zones. Amazon MQ will not be able to create VPC endpoints for your broker with multiple subnets in the same Availability Zone. A SINGLE_INSTANCE deployment requires one subnet (for example, the default subnet). An ACTIVE_STANDBY_MULTI_AZ deployment (ACTIVEMQ) requires two subnets. A CLUSTER_MULTI_AZ deployment (RABBITMQ) has no subnet requirements when deployed with public accessibility, deployment without public accessibility requires at least one subnet. .. epigraph:: If you specify subnets in a shared VPC for a RabbitMQ broker, the associated VPC to which the specified subnets belong must be owned by your AWS account . Amazon MQ will not be able to create VPC enpoints in VPCs that are not owned by your AWS account .
        :param tags: An array of key-value pairs. For more information, see `Using Cost Allocation Tags <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`_ in the *Billing and Cost Management User Guide* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d16f84aeefdd69c636acf0c8b4d958b93ded39c1da5d5eecb39ce87535c69cb7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBrokerProps(
            auto_minor_version_upgrade=auto_minor_version_upgrade,
            broker_name=broker_name,
            deployment_mode=deployment_mode,
            engine_type=engine_type,
            engine_version=engine_version,
            host_instance_type=host_instance_type,
            publicly_accessible=publicly_accessible,
            users=users,
            authentication_strategy=authentication_strategy,
            configuration=configuration,
            data_replication_mode=data_replication_mode,
            data_replication_primary_broker_arn=data_replication_primary_broker_arn,
            encryption_options=encryption_options,
            ldap_server_metadata=ldap_server_metadata,
            logs=logs,
            maintenance_window_start_time=maintenance_window_start_time,
            security_groups=security_groups,
            storage_type=storage_type,
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
            type_hints = typing.get_type_hints(_typecheckingstub__2d7a61b5b47c0d5f9d4072378260a383a676994ae22eab1593156375aeda79a7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5b2faabcb2fd601665f655b0a42ddecd67459d337d8e81f23d1a39ee8cbb4bb0)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAmqpEndpoints")
    def attr_amqp_endpoints(self) -> typing.List[builtins.str]:
        '''The AMQP endpoints of each broker instance as a list of strings.

        ``amqp+ssl://b-4aada85d-a80c-4be0-9d30-e344a01b921e-1.mq.eu-central-amazonaws.com:5671``

        :cloudformationAttribute: AmqpEndpoints
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrAmqpEndpoints"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Amazon MQ broker.

        ``arn:aws:mq:us-east-2:123456789012:broker:MyBroker:b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrConfigurationId")
    def attr_configuration_id(self) -> builtins.str:
        '''The unique ID that Amazon MQ generates for the configuration.

        ``c-1234a5b6-78cd-901e-2fgh-3i45j6k178l9``

        :cloudformationAttribute: ConfigurationId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConfigurationId"))

    @builtins.property
    @jsii.member(jsii_name="attrConfigurationRevision")
    def attr_configuration_revision(self) -> jsii.Number:
        '''The revision number of the configuration.

        ``1``

        :cloudformationAttribute: ConfigurationRevision
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrConfigurationRevision"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrIpAddresses")
    def attr_ip_addresses(self) -> typing.List[builtins.str]:
        '''The IP addresses of each broker instance as a list of strings. Does not apply to RabbitMQ brokers.

        ``['198.51.100.2', '203.0.113.9']``

        :cloudformationAttribute: IpAddresses
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrIpAddresses"))

    @builtins.property
    @jsii.member(jsii_name="attrMqttEndpoints")
    def attr_mqtt_endpoints(self) -> typing.List[builtins.str]:
        '''The MQTT endpoints of each broker instance as a list of strings.

        ``mqtt+ssl://b-4aada85d-a80c-4be0-9d30-e344a01b921e-1.mq.eu-central-amazonaws.com:8883``

        :cloudformationAttribute: MqttEndpoints
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrMqttEndpoints"))

    @builtins.property
    @jsii.member(jsii_name="attrOpenWireEndpoints")
    def attr_open_wire_endpoints(self) -> typing.List[builtins.str]:
        '''The OpenWire endpoints of each broker instance as a list of strings.

        ``ssl://b-4aada85d-a80c-4be0-9d30-e344a01b921e-1.mq.eu-central-amazonaws.com:61617``

        :cloudformationAttribute: OpenWireEndpoints
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrOpenWireEndpoints"))

    @builtins.property
    @jsii.member(jsii_name="attrStompEndpoints")
    def attr_stomp_endpoints(self) -> typing.List[builtins.str]:
        '''The STOMP endpoints of each broker instance as a list of strings.

        ``stomp+ssl://b-4aada85d-a80c-4be0-9d30-e344a01b921e-1.mq.eu-central-amazonaws.com:61614``

        :cloudformationAttribute: StompEndpoints
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrStompEndpoints"))

    @builtins.property
    @jsii.member(jsii_name="attrWssEndpoints")
    def attr_wss_endpoints(self) -> typing.List[builtins.str]:
        '''The WSS endpoints of each broker instance as a list of strings.

        ``wss://b-4aada85d-a80c-4be0-9d30-e344a01b921e-1.mq.eu-central-amazonaws.com:61619``

        :cloudformationAttribute: WssEndpoints
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrWssEndpoints"))

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
    @jsii.member(jsii_name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(
        self,
    ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Enables automatic upgrades to new minor versions for brokers, as new broker engine versions are released and supported by Amazon MQ.'''
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], jsii.get(self, "autoMinorVersionUpgrade"))

    @auto_minor_version_upgrade.setter
    def auto_minor_version_upgrade(
        self,
        value: typing.Union[builtins.bool, _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1becedc098602474059b0aaa465b25ea1b7124443411ed6a42b02d6a5344cdda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoMinorVersionUpgrade", value)

    @builtins.property
    @jsii.member(jsii_name="brokerName")
    def broker_name(self) -> builtins.str:
        '''The name of the broker.'''
        return typing.cast(builtins.str, jsii.get(self, "brokerName"))

    @broker_name.setter
    def broker_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0511cf4804dad2e6e03dc33f21bf9d654b3598349ced7ea110e5591745f76bdc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "brokerName", value)

    @builtins.property
    @jsii.member(jsii_name="deploymentMode")
    def deployment_mode(self) -> builtins.str:
        '''The deployment mode of the broker.

        Available values:.
        '''
        return typing.cast(builtins.str, jsii.get(self, "deploymentMode"))

    @deployment_mode.setter
    def deployment_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35ac0143ff0fe5df5b06639c734e8dce854395762102045c72ecfdd080395609)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentMode", value)

    @builtins.property
    @jsii.member(jsii_name="engineType")
    def engine_type(self) -> builtins.str:
        '''The type of broker engine.'''
        return typing.cast(builtins.str, jsii.get(self, "engineType"))

    @engine_type.setter
    def engine_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edb02169dcf378d5d01cba6368876329b4e7f4e34fde8d2f0f58da09a46b65bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engineType", value)

    @builtins.property
    @jsii.member(jsii_name="engineVersion")
    def engine_version(self) -> builtins.str:
        '''The version of the broker engine.'''
        return typing.cast(builtins.str, jsii.get(self, "engineVersion"))

    @engine_version.setter
    def engine_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__631fd780aebb5b339c2238752e33306ea6591245c7231c4db165256d69094ceb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engineVersion", value)

    @builtins.property
    @jsii.member(jsii_name="hostInstanceType")
    def host_instance_type(self) -> builtins.str:
        '''The broker's instance type.'''
        return typing.cast(builtins.str, jsii.get(self, "hostInstanceType"))

    @host_instance_type.setter
    def host_instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8a51a01838222e13c8eba50f7d568dc975a2e3c5c2d18f21339bc702ffc284b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostInstanceType", value)

    @builtins.property
    @jsii.member(jsii_name="publiclyAccessible")
    def publicly_accessible(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Enables connections from applications outside of the VPC that hosts the broker's subnets.'''
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], jsii.get(self, "publiclyAccessible"))

    @publicly_accessible.setter
    def publicly_accessible(
        self,
        value: typing.Union[builtins.bool, _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a82a112ececec828f3c746f7c18e6b6ce32a5aa08550a05a69d7babd8852a7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publiclyAccessible", value)

    @builtins.property
    @jsii.member(jsii_name="users")
    def users(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBroker.UserProperty"]]]:
        '''The list of broker users (persons or applications) who can access queues and topics.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBroker.UserProperty"]]], jsii.get(self, "users"))

    @users.setter
    def users(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBroker.UserProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85b9c0c3c3aa438279362aeaae2a3de844ec906edf5b12b7601c78bc63fbfd6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "users", value)

    @builtins.property
    @jsii.member(jsii_name="authenticationStrategy")
    def authentication_strategy(self) -> typing.Optional[builtins.str]:
        '''Optional.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authenticationStrategy"))

    @authentication_strategy.setter
    def authentication_strategy(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3eab9258c47a74b1aabb4a39e66512dbb010a0f1c8838ec359338808e1f64681)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="configuration")
    def configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBroker.ConfigurationIdProperty"]]:
        '''A list of information about the configuration.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBroker.ConfigurationIdProperty"]], jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBroker.ConfigurationIdProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0eabdb321f6595584d9f056a97a3a7481faa1ad417f76f3ea42484e5ef0b195f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuration", value)

    @builtins.property
    @jsii.member(jsii_name="dataReplicationMode")
    def data_replication_mode(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataReplicationMode"))

    @data_replication_mode.setter
    def data_replication_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fb3d9abae1cb6570b9ccf260c74e4f47d43eda2d732d8b3bcfa03b254143b3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataReplicationMode", value)

    @builtins.property
    @jsii.member(jsii_name="dataReplicationPrimaryBrokerArn")
    def data_replication_primary_broker_arn(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataReplicationPrimaryBrokerArn"))

    @data_replication_primary_broker_arn.setter
    def data_replication_primary_broker_arn(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8ffdb4011b4637fc96f4f2d0dcab95738383a77b9240b6d0f3cdf96f87e7725)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataReplicationPrimaryBrokerArn", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionOptions")
    def encryption_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBroker.EncryptionOptionsProperty"]]:
        '''Encryption options for the broker.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBroker.EncryptionOptionsProperty"]], jsii.get(self, "encryptionOptions"))

    @encryption_options.setter
    def encryption_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBroker.EncryptionOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3846e06a73702f6e76ab386acc1ad9128b00ec2357b3396abf86d893cdbae15d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionOptions", value)

    @builtins.property
    @jsii.member(jsii_name="ldapServerMetadata")
    def ldap_server_metadata(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBroker.LdapServerMetadataProperty"]]:
        '''Optional.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBroker.LdapServerMetadataProperty"]], jsii.get(self, "ldapServerMetadata"))

    @ldap_server_metadata.setter
    def ldap_server_metadata(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBroker.LdapServerMetadataProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8de6a532c388b2fc838b3141f942b6cbbc5d1a796bb76e3fc3fe5a446d932f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ldapServerMetadata", value)

    @builtins.property
    @jsii.member(jsii_name="logs")
    def logs(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBroker.LogListProperty"]]:
        '''Enables Amazon CloudWatch logging for brokers.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBroker.LogListProperty"]], jsii.get(self, "logs"))

    @logs.setter
    def logs(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBroker.LogListProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36b6d40f90e93b4b35c3ffbb3065567a24c0bd9312758826697afa2118901335)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logs", value)

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowStartTime")
    def maintenance_window_start_time(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBroker.MaintenanceWindowProperty"]]:
        '''The scheduled time period relative to UTC during which Amazon MQ begins to apply pending updates or patches to the broker.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBroker.MaintenanceWindowProperty"]], jsii.get(self, "maintenanceWindowStartTime"))

    @maintenance_window_start_time.setter
    def maintenance_window_start_time(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBroker.MaintenanceWindowProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e2d1a75b2e491fa226b7065a64e24f522ac7be048073da54600cfd720b1240f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maintenanceWindowStartTime", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of rules (1 minimum, 125 maximum) that authorize connections to brokers.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroups"))

    @security_groups.setter
    def security_groups(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e87ea78ee8e3d556f9e322090479023fa17920888ca10cd4413f4e00c942ffec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroups", value)

    @builtins.property
    @jsii.member(jsii_name="storageType")
    def storage_type(self) -> typing.Optional[builtins.str]:
        '''The broker's storage type.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageType"))

    @storage_type.setter
    def storage_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc1a4f009fd81070f5c68b6193804c7fd4733299a2c55d2e81fd5c11f62da6ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageType", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of groups that define which subnets and IP ranges the broker can use from different Availability Zones.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa1ab62865033946dc6d8cee45676096e4e10411bffb97c3db615e4d2aa1652f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List["CfnBroker.TagsEntryProperty"]]:
        '''An array of key-value pairs.'''
        return typing.cast(typing.Optional[typing.List["CfnBroker.TagsEntryProperty"]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.List["CfnBroker.TagsEntryProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__739d50e75e2a93ab9671710563ad1ed5176802aef44a2986de718c86a94e7e8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amazonmq.CfnBroker.ConfigurationIdProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id", "revision": "revision"},
    )
    class ConfigurationIdProperty:
        def __init__(self, *, id: builtins.str, revision: jsii.Number) -> None:
            '''A list of information about the configuration.

            .. epigraph::

               Does not apply to RabbitMQ brokers.

            :param id: The unique ID that Amazon MQ generates for the configuration.
            :param revision: The revision number of the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-configurationid.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amazonmq as amazonmq
                
                configuration_id_property = amazonmq.CfnBroker.ConfigurationIdProperty(
                    id="id",
                    revision=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f9d5131bf29ed360bf06fb2fc10b8d6ac62da622a4f41bd0e435a4436ba5511c)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument revision", value=revision, expected_type=type_hints["revision"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "id": id,
                "revision": revision,
            }

        @builtins.property
        def id(self) -> builtins.str:
            '''The unique ID that Amazon MQ generates for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-configurationid.html#cfn-amazonmq-broker-configurationid-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def revision(self) -> jsii.Number:
            '''The revision number of the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-configurationid.html#cfn-amazonmq-broker-configurationid-revision
            '''
            result = self._values.get("revision")
            assert result is not None, "Required property 'revision' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigurationIdProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amazonmq.CfnBroker.EncryptionOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"use_aws_owned_key": "useAwsOwnedKey", "kms_key_id": "kmsKeyId"},
    )
    class EncryptionOptionsProperty:
        def __init__(
            self,
            *,
            use_aws_owned_key: typing.Union[builtins.bool, _IResolvable_da3f097b],
            kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Encryption options for the broker.

            .. epigraph::

               Does not apply to RabbitMQ brokers.

            :param use_aws_owned_key: Enables the use of an AWS owned CMK using AWS KMS (KMS). Set to ``true`` by default, if no value is provided, for example, for RabbitMQ brokers.
            :param kms_key_id: The customer master key (CMK) to use for the A AWS KMS (KMS). This key is used to encrypt your data at rest. If not provided, Amazon MQ will use a default CMK to encrypt your data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-encryptionoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amazonmq as amazonmq
                
                encryption_options_property = amazonmq.CfnBroker.EncryptionOptionsProperty(
                    use_aws_owned_key=False,
                
                    # the properties below are optional
                    kms_key_id="kmsKeyId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__95df5a3839d7c2d80c93cb1b9948b6d4ef43f2e19eb9097abb3cbae048c164aa)
                check_type(argname="argument use_aws_owned_key", value=use_aws_owned_key, expected_type=type_hints["use_aws_owned_key"])
                check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "use_aws_owned_key": use_aws_owned_key,
            }
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def use_aws_owned_key(
            self,
        ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Enables the use of an AWS owned CMK using AWS KMS (KMS).

            Set to ``true`` by default, if no value is provided, for example, for RabbitMQ brokers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-encryptionoptions.html#cfn-amazonmq-broker-encryptionoptions-useawsownedkey
            '''
            result = self._values.get("use_aws_owned_key")
            assert result is not None, "Required property 'use_aws_owned_key' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''The customer master key (CMK) to use for the A AWS KMS (KMS).

            This key is used to encrypt your data at rest. If not provided, Amazon MQ will use a default CMK to encrypt your data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-encryptionoptions.html#cfn-amazonmq-broker-encryptionoptions-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amazonmq.CfnBroker.LdapServerMetadataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "hosts": "hosts",
            "role_base": "roleBase",
            "role_search_matching": "roleSearchMatching",
            "service_account_password": "serviceAccountPassword",
            "service_account_username": "serviceAccountUsername",
            "user_base": "userBase",
            "user_search_matching": "userSearchMatching",
            "role_name": "roleName",
            "role_search_subtree": "roleSearchSubtree",
            "user_role_name": "userRoleName",
            "user_search_subtree": "userSearchSubtree",
        },
    )
    class LdapServerMetadataProperty:
        def __init__(
            self,
            *,
            hosts: typing.Sequence[builtins.str],
            role_base: builtins.str,
            role_search_matching: builtins.str,
            service_account_password: builtins.str,
            service_account_username: builtins.str,
            user_base: builtins.str,
            user_search_matching: builtins.str,
            role_name: typing.Optional[builtins.str] = None,
            role_search_subtree: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            user_role_name: typing.Optional[builtins.str] = None,
            user_search_subtree: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Optional. The metadata of the LDAP server used to authenticate and authorize connections to the broker.

            .. epigraph::

               Does not apply to RabbitMQ brokers.

            :param hosts: Specifies the location of the LDAP server such as AWS Directory Service for Microsoft Active Directory . Optional failover server.
            :param role_base: The distinguished name of the node in the directory information tree (DIT) to search for roles or groups. For example, ``ou=group`` , ``ou=corp`` , ``dc=corp`` , ``dc=example`` , ``dc=com`` .
            :param role_search_matching: The LDAP search filter used to find roles within the roleBase. The distinguished name of the user matched by userSearchMatching is substituted into the ``{0}`` placeholder in the search filter. The client's username is substituted into the ``{1}`` placeholder. For example, if you set this option to ``(member=uid={1})`` for the user janedoe, the search filter becomes ``(member=uid=janedoe)`` after string substitution. It matches all role entries that have a member attribute equal to ``uid=janedoe`` under the subtree selected by the ``RoleBases`` .
            :param service_account_password: Service account password. A service account is an account in your LDAP server that has access to initiate a connection. For example, ``cn=admin`` , ``dc=corp`` , ``dc=example`` , ``dc=com`` .
            :param service_account_username: Service account username. A service account is an account in your LDAP server that has access to initiate a connection. For example, ``cn=admin`` , ``ou=corp`` , ``dc=corp`` , ``dc=example`` , ``dc=com`` .
            :param user_base: Select a particular subtree of the directory information tree (DIT) to search for user entries. The subtree is specified by a DN, which specifies the base node of the subtree. For example, by setting this option to ``ou=Users`` , ``ou=corp`` , ``dc=corp`` , ``dc=example`` , ``dc=com`` , the search for user entries is restricted to the subtree beneath ``ou=Users`` , ``ou=corp`` , ``dc=corp`` , ``dc=example`` , ``dc=com`` .
            :param user_search_matching: The LDAP search filter used to find users within the ``userBase`` . The client's username is substituted into the ``{0}`` placeholder in the search filter. For example, if this option is set to ``(uid={0})`` and the received username is ``janedoe`` , the search filter becomes ``(uid=janedoe)`` after string substitution. It will result in matching an entry like ``uid=janedoe`` , ``ou=Users`` , ``ou=corp`` , ``dc=corp`` , ``dc=example`` , ``dc=com`` .
            :param role_name: The group name attribute in a role entry whose value is the name of that role. For example, you can specify ``cn`` for a group entry's common name. If authentication succeeds, then the user is assigned the the value of the ``cn`` attribute for each role entry that they are a member of.
            :param role_search_subtree: The directory search scope for the role. If set to true, scope is to search the entire subtree.
            :param user_role_name: The name of the LDAP attribute in the user's directory entry for the user's group membership. In some cases, user roles may be identified by the value of an attribute in the user's directory entry. The ``UserRoleName`` option allows you to provide the name of this attribute.
            :param user_search_subtree: The directory search scope for the user. If set to true, scope is to search the entire subtree.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-ldapservermetadata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amazonmq as amazonmq
                
                ldap_server_metadata_property = amazonmq.CfnBroker.LdapServerMetadataProperty(
                    hosts=["hosts"],
                    role_base="roleBase",
                    role_search_matching="roleSearchMatching",
                    service_account_password="serviceAccountPassword",
                    service_account_username="serviceAccountUsername",
                    user_base="userBase",
                    user_search_matching="userSearchMatching",
                
                    # the properties below are optional
                    role_name="roleName",
                    role_search_subtree=False,
                    user_role_name="userRoleName",
                    user_search_subtree=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__282093319da5ca5716ae9202b23fde6f2380a3a720f7bac369f166119c58cfa8)
                check_type(argname="argument hosts", value=hosts, expected_type=type_hints["hosts"])
                check_type(argname="argument role_base", value=role_base, expected_type=type_hints["role_base"])
                check_type(argname="argument role_search_matching", value=role_search_matching, expected_type=type_hints["role_search_matching"])
                check_type(argname="argument service_account_password", value=service_account_password, expected_type=type_hints["service_account_password"])
                check_type(argname="argument service_account_username", value=service_account_username, expected_type=type_hints["service_account_username"])
                check_type(argname="argument user_base", value=user_base, expected_type=type_hints["user_base"])
                check_type(argname="argument user_search_matching", value=user_search_matching, expected_type=type_hints["user_search_matching"])
                check_type(argname="argument role_name", value=role_name, expected_type=type_hints["role_name"])
                check_type(argname="argument role_search_subtree", value=role_search_subtree, expected_type=type_hints["role_search_subtree"])
                check_type(argname="argument user_role_name", value=user_role_name, expected_type=type_hints["user_role_name"])
                check_type(argname="argument user_search_subtree", value=user_search_subtree, expected_type=type_hints["user_search_subtree"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "hosts": hosts,
                "role_base": role_base,
                "role_search_matching": role_search_matching,
                "service_account_password": service_account_password,
                "service_account_username": service_account_username,
                "user_base": user_base,
                "user_search_matching": user_search_matching,
            }
            if role_name is not None:
                self._values["role_name"] = role_name
            if role_search_subtree is not None:
                self._values["role_search_subtree"] = role_search_subtree
            if user_role_name is not None:
                self._values["user_role_name"] = user_role_name
            if user_search_subtree is not None:
                self._values["user_search_subtree"] = user_search_subtree

        @builtins.property
        def hosts(self) -> typing.List[builtins.str]:
            '''Specifies the location of the LDAP server such as AWS Directory Service for Microsoft Active Directory .

            Optional failover server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-ldapservermetadata.html#cfn-amazonmq-broker-ldapservermetadata-hosts
            '''
            result = self._values.get("hosts")
            assert result is not None, "Required property 'hosts' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def role_base(self) -> builtins.str:
            '''The distinguished name of the node in the directory information tree (DIT) to search for roles or groups.

            For example, ``ou=group`` , ``ou=corp`` , ``dc=corp`` , ``dc=example`` , ``dc=com`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-ldapservermetadata.html#cfn-amazonmq-broker-ldapservermetadata-rolebase
            '''
            result = self._values.get("role_base")
            assert result is not None, "Required property 'role_base' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_search_matching(self) -> builtins.str:
            '''The LDAP search filter used to find roles within the roleBase.

            The distinguished name of the user matched by userSearchMatching is substituted into the ``{0}`` placeholder in the search filter. The client's username is substituted into the ``{1}`` placeholder. For example, if you set this option to ``(member=uid={1})`` for the user janedoe, the search filter becomes ``(member=uid=janedoe)`` after string substitution. It matches all role entries that have a member attribute equal to ``uid=janedoe`` under the subtree selected by the ``RoleBases`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-ldapservermetadata.html#cfn-amazonmq-broker-ldapservermetadata-rolesearchmatching
            '''
            result = self._values.get("role_search_matching")
            assert result is not None, "Required property 'role_search_matching' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def service_account_password(self) -> builtins.str:
            '''Service account password.

            A service account is an account in your LDAP server that has access to initiate a connection. For example, ``cn=admin`` , ``dc=corp`` , ``dc=example`` , ``dc=com`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-ldapservermetadata.html#cfn-amazonmq-broker-ldapservermetadata-serviceaccountpassword
            '''
            result = self._values.get("service_account_password")
            assert result is not None, "Required property 'service_account_password' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def service_account_username(self) -> builtins.str:
            '''Service account username.

            A service account is an account in your LDAP server that has access to initiate a connection. For example, ``cn=admin`` , ``ou=corp`` , ``dc=corp`` , ``dc=example`` , ``dc=com`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-ldapservermetadata.html#cfn-amazonmq-broker-ldapservermetadata-serviceaccountusername
            '''
            result = self._values.get("service_account_username")
            assert result is not None, "Required property 'service_account_username' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def user_base(self) -> builtins.str:
            '''Select a particular subtree of the directory information tree (DIT) to search for user entries.

            The subtree is specified by a DN, which specifies the base node of the subtree. For example, by setting this option to ``ou=Users`` , ``ou=corp`` , ``dc=corp`` , ``dc=example`` , ``dc=com`` , the search for user entries is restricted to the subtree beneath ``ou=Users`` , ``ou=corp`` , ``dc=corp`` , ``dc=example`` , ``dc=com`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-ldapservermetadata.html#cfn-amazonmq-broker-ldapservermetadata-userbase
            '''
            result = self._values.get("user_base")
            assert result is not None, "Required property 'user_base' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def user_search_matching(self) -> builtins.str:
            '''The LDAP search filter used to find users within the ``userBase`` .

            The client's username is substituted into the ``{0}`` placeholder in the search filter. For example, if this option is set to ``(uid={0})`` and the received username is ``janedoe`` , the search filter becomes ``(uid=janedoe)`` after string substitution. It will result in matching an entry like ``uid=janedoe`` , ``ou=Users`` , ``ou=corp`` , ``dc=corp`` , ``dc=example`` , ``dc=com`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-ldapservermetadata.html#cfn-amazonmq-broker-ldapservermetadata-usersearchmatching
            '''
            result = self._values.get("user_search_matching")
            assert result is not None, "Required property 'user_search_matching' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_name(self) -> typing.Optional[builtins.str]:
            '''The group name attribute in a role entry whose value is the name of that role.

            For example, you can specify ``cn`` for a group entry's common name. If authentication succeeds, then the user is assigned the the value of the ``cn`` attribute for each role entry that they are a member of.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-ldapservermetadata.html#cfn-amazonmq-broker-ldapservermetadata-rolename
            '''
            result = self._values.get("role_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def role_search_subtree(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The directory search scope for the role.

            If set to true, scope is to search the entire subtree.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-ldapservermetadata.html#cfn-amazonmq-broker-ldapservermetadata-rolesearchsubtree
            '''
            result = self._values.get("role_search_subtree")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def user_role_name(self) -> typing.Optional[builtins.str]:
            '''The name of the LDAP attribute in the user's directory entry for the user's group membership.

            In some cases, user roles may be identified by the value of an attribute in the user's directory entry. The ``UserRoleName`` option allows you to provide the name of this attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-ldapservermetadata.html#cfn-amazonmq-broker-ldapservermetadata-userrolename
            '''
            result = self._values.get("user_role_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def user_search_subtree(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The directory search scope for the user.

            If set to true, scope is to search the entire subtree.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-ldapservermetadata.html#cfn-amazonmq-broker-ldapservermetadata-usersearchsubtree
            '''
            result = self._values.get("user_search_subtree")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LdapServerMetadataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amazonmq.CfnBroker.LogListProperty",
        jsii_struct_bases=[],
        name_mapping={"audit": "audit", "general": "general"},
    )
    class LogListProperty:
        def __init__(
            self,
            *,
            audit: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            general: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The list of information about logs to be enabled for the specified broker.

            :param audit: Enables audit logging. Every user management action made using JMX or the ActiveMQ Web Console is logged. Does not apply to RabbitMQ brokers.
            :param general: Enables general logging.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-loglist.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amazonmq as amazonmq
                
                log_list_property = amazonmq.CfnBroker.LogListProperty(
                    audit=False,
                    general=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cc6518d5765d0a7bdb0ead05cff3d08ab216b44006da8bba35424620fea26077)
                check_type(argname="argument audit", value=audit, expected_type=type_hints["audit"])
                check_type(argname="argument general", value=general, expected_type=type_hints["general"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if audit is not None:
                self._values["audit"] = audit
            if general is not None:
                self._values["general"] = general

        @builtins.property
        def audit(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Enables audit logging.

            Every user management action made using JMX or the ActiveMQ Web Console is logged. Does not apply to RabbitMQ brokers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-loglist.html#cfn-amazonmq-broker-loglist-audit
            '''
            result = self._values.get("audit")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def general(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Enables general logging.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-loglist.html#cfn-amazonmq-broker-loglist-general
            '''
            result = self._values.get("general")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogListProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amazonmq.CfnBroker.MaintenanceWindowProperty",
        jsii_struct_bases=[],
        name_mapping={
            "day_of_week": "dayOfWeek",
            "time_of_day": "timeOfDay",
            "time_zone": "timeZone",
        },
    )
    class MaintenanceWindowProperty:
        def __init__(
            self,
            *,
            day_of_week: builtins.str,
            time_of_day: builtins.str,
            time_zone: builtins.str,
        ) -> None:
            '''The parameters that determine the ``WeeklyStartTime`` to apply pending updates or patches to the broker.

            :param day_of_week: The day of the week.
            :param time_of_day: The time, in 24-hour format.
            :param time_zone: The time zone, UTC by default, in either the Country/City format, or the UTC offset format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-maintenancewindow.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amazonmq as amazonmq
                
                maintenance_window_property = amazonmq.CfnBroker.MaintenanceWindowProperty(
                    day_of_week="dayOfWeek",
                    time_of_day="timeOfDay",
                    time_zone="timeZone"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cd0060c95e384a30563d722724745751c5579e5b53fa378c0b36e301bb067795)
                check_type(argname="argument day_of_week", value=day_of_week, expected_type=type_hints["day_of_week"])
                check_type(argname="argument time_of_day", value=time_of_day, expected_type=type_hints["time_of_day"])
                check_type(argname="argument time_zone", value=time_zone, expected_type=type_hints["time_zone"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "day_of_week": day_of_week,
                "time_of_day": time_of_day,
                "time_zone": time_zone,
            }

        @builtins.property
        def day_of_week(self) -> builtins.str:
            '''The day of the week.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-maintenancewindow.html#cfn-amazonmq-broker-maintenancewindow-dayofweek
            '''
            result = self._values.get("day_of_week")
            assert result is not None, "Required property 'day_of_week' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def time_of_day(self) -> builtins.str:
            '''The time, in 24-hour format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-maintenancewindow.html#cfn-amazonmq-broker-maintenancewindow-timeofday
            '''
            result = self._values.get("time_of_day")
            assert result is not None, "Required property 'time_of_day' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def time_zone(self) -> builtins.str:
            '''The time zone, UTC by default, in either the Country/City format, or the UTC offset format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-maintenancewindow.html#cfn-amazonmq-broker-maintenancewindow-timezone
            '''
            result = self._values.get("time_zone")
            assert result is not None, "Required property 'time_zone' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MaintenanceWindowProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amazonmq.CfnBroker.TagsEntryProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class TagsEntryProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''A key-value pair to associate with the broker.

            :param key: The key in a key-value pair.
            :param value: The value in a key-value pair.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-tagsentry.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amazonmq as amazonmq
                
                tags_entry_property = amazonmq.CfnBroker.TagsEntryProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7825e3fdf121f81e27fcd00d00f2c5d2d105311b09671d687ee257d56a749171)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The key in a key-value pair.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-tagsentry.html#cfn-amazonmq-broker-tagsentry-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value in a key-value pair.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-tagsentry.html#cfn-amazonmq-broker-tagsentry-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagsEntryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amazonmq.CfnBroker.UserProperty",
        jsii_struct_bases=[],
        name_mapping={
            "password": "password",
            "username": "username",
            "console_access": "consoleAccess",
            "groups": "groups",
        },
    )
    class UserProperty:
        def __init__(
            self,
            *,
            password: builtins.str,
            username: builtins.str,
            console_access: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The list of broker users (persons or applications) who can access queues and topics.

            For Amazon MQ for RabbitMQ brokers, one and only one administrative user is accepted and created when a broker is first provisioned. All subsequent broker users are created via the RabbitMQ web console or by using the RabbitMQ management API.

            :param password: The password of the user. This value must be at least 12 characters long, must contain at least 4 unique characters, and must not contain commas, colons, or equal signs (,:=).
            :param username: The username of the broker user. For Amazon MQ for ActiveMQ brokers, this value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). For Amazon MQ for RabbitMQ brokers, this value can contain only alphanumeric characters, dashes, periods, underscores (- . _). This value must not contain a tilde (~) character. Amazon MQ prohibts using guest as a valid usename. This value must be 2-100 characters long. .. epigraph:: Do not add personally identifiable information (PII) or other confidential or sensitive information in broker usernames. Broker usernames are accessible to other AWS services, including CloudWatch Logs . Broker usernames are not intended to be used for private or sensitive data.
            :param console_access: Enables access to the ActiveMQ web console for the ActiveMQ user. Does not apply to RabbitMQ brokers.
            :param groups: The list of groups (20 maximum) to which the ActiveMQ user belongs. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long. Does not apply to RabbitMQ brokers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-user.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amazonmq as amazonmq
                
                user_property = amazonmq.CfnBroker.UserProperty(
                    password="password",
                    username="username",
                
                    # the properties below are optional
                    console_access=False,
                    groups=["groups"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8a458786a0cd0d4269adef0bf3c85862386851ab69649004d5d3dcba4c238445)
                check_type(argname="argument password", value=password, expected_type=type_hints["password"])
                check_type(argname="argument username", value=username, expected_type=type_hints["username"])
                check_type(argname="argument console_access", value=console_access, expected_type=type_hints["console_access"])
                check_type(argname="argument groups", value=groups, expected_type=type_hints["groups"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "password": password,
                "username": username,
            }
            if console_access is not None:
                self._values["console_access"] = console_access
            if groups is not None:
                self._values["groups"] = groups

        @builtins.property
        def password(self) -> builtins.str:
            '''The password of the user.

            This value must be at least 12 characters long, must contain at least 4 unique characters, and must not contain commas, colons, or equal signs (,:=).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-user.html#cfn-amazonmq-broker-user-password
            '''
            result = self._values.get("password")
            assert result is not None, "Required property 'password' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def username(self) -> builtins.str:
            '''The username of the broker user.

            For Amazon MQ for ActiveMQ brokers, this value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). For Amazon MQ for RabbitMQ brokers, this value can contain only alphanumeric characters, dashes, periods, underscores (- . _). This value must not contain a tilde (~) character. Amazon MQ prohibts using guest as a valid usename. This value must be 2-100 characters long.
            .. epigraph::

               Do not add personally identifiable information (PII) or other confidential or sensitive information in broker usernames. Broker usernames are accessible to other AWS services, including CloudWatch Logs . Broker usernames are not intended to be used for private or sensitive data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-user.html#cfn-amazonmq-broker-user-username
            '''
            result = self._values.get("username")
            assert result is not None, "Required property 'username' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def console_access(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Enables access to the ActiveMQ web console for the ActiveMQ user.

            Does not apply to RabbitMQ brokers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-user.html#cfn-amazonmq-broker-user-consoleaccess
            '''
            result = self._values.get("console_access")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def groups(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The list of groups (20 maximum) to which the ActiveMQ user belongs.

            This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long. Does not apply to RabbitMQ brokers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-user.html#cfn-amazonmq-broker-user-groups
            '''
            result = self._values.get("groups")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_amazonmq.CfnBrokerProps",
    jsii_struct_bases=[],
    name_mapping={
        "auto_minor_version_upgrade": "autoMinorVersionUpgrade",
        "broker_name": "brokerName",
        "deployment_mode": "deploymentMode",
        "engine_type": "engineType",
        "engine_version": "engineVersion",
        "host_instance_type": "hostInstanceType",
        "publicly_accessible": "publiclyAccessible",
        "users": "users",
        "authentication_strategy": "authenticationStrategy",
        "configuration": "configuration",
        "data_replication_mode": "dataReplicationMode",
        "data_replication_primary_broker_arn": "dataReplicationPrimaryBrokerArn",
        "encryption_options": "encryptionOptions",
        "ldap_server_metadata": "ldapServerMetadata",
        "logs": "logs",
        "maintenance_window_start_time": "maintenanceWindowStartTime",
        "security_groups": "securityGroups",
        "storage_type": "storageType",
        "subnet_ids": "subnetIds",
        "tags": "tags",
    },
)
class CfnBrokerProps:
    def __init__(
        self,
        *,
        auto_minor_version_upgrade: typing.Union[builtins.bool, _IResolvable_da3f097b],
        broker_name: builtins.str,
        deployment_mode: builtins.str,
        engine_type: builtins.str,
        engine_version: builtins.str,
        host_instance_type: builtins.str,
        publicly_accessible: typing.Union[builtins.bool, _IResolvable_da3f097b],
        users: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBroker.UserProperty, typing.Dict[builtins.str, typing.Any]]]]],
        authentication_strategy: typing.Optional[builtins.str] = None,
        configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBroker.ConfigurationIdProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        data_replication_mode: typing.Optional[builtins.str] = None,
        data_replication_primary_broker_arn: typing.Optional[builtins.str] = None,
        encryption_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBroker.EncryptionOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        ldap_server_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBroker.LdapServerMetadataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBroker.LogListProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        maintenance_window_start_time: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBroker.MaintenanceWindowProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        storage_type: typing.Optional[builtins.str] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[CfnBroker.TagsEntryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnBroker``.

        :param auto_minor_version_upgrade: Enables automatic upgrades to new minor versions for brokers, as new broker engine versions are released and supported by Amazon MQ. Automatic upgrades occur during the scheduled maintenance window of the broker or after a manual broker reboot.
        :param broker_name: The name of the broker. This value must be unique in your AWS account , 1-50 characters long, must contain only letters, numbers, dashes, and underscores, and must not contain white spaces, brackets, wildcard characters, or special characters. .. epigraph:: Do not add personally identifiable information (PII) or other confidential or sensitive information in broker names. Broker names are accessible to other AWS services, including C CloudWatch Logs . Broker names are not intended to be used for private or sensitive data.
        :param deployment_mode: The deployment mode of the broker. Available values:. - ``SINGLE_INSTANCE`` - ``ACTIVE_STANDBY_MULTI_AZ`` - ``CLUSTER_MULTI_AZ``
        :param engine_type: The type of broker engine. Currently, Amazon MQ supports ``ACTIVEMQ`` and ``RABBITMQ`` .
        :param engine_version: The version of the broker engine. For a list of supported engine versions, see `Engine <https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html>`_ in the *Amazon MQ Developer Guide* .
        :param host_instance_type: The broker's instance type.
        :param publicly_accessible: Enables connections from applications outside of the VPC that hosts the broker's subnets.
        :param users: The list of broker users (persons or applications) who can access queues and topics. For Amazon MQ for RabbitMQ brokers, one and only one administrative user is accepted and created when a broker is first provisioned. All subsequent RabbitMQ users are created by via the RabbitMQ web console or by using the RabbitMQ management API.
        :param authentication_strategy: Optional. The authentication strategy used to secure the broker. The default is ``SIMPLE`` .
        :param configuration: A list of information about the configuration. Does not apply to RabbitMQ brokers.
        :param data_replication_mode: 
        :param data_replication_primary_broker_arn: 
        :param encryption_options: Encryption options for the broker. Does not apply to RabbitMQ brokers.
        :param ldap_server_metadata: Optional. The metadata of the LDAP server used to authenticate and authorize connections to the broker. Does not apply to RabbitMQ brokers.
        :param logs: Enables Amazon CloudWatch logging for brokers.
        :param maintenance_window_start_time: The scheduled time period relative to UTC during which Amazon MQ begins to apply pending updates or patches to the broker.
        :param security_groups: The list of rules (1 minimum, 125 maximum) that authorize connections to brokers.
        :param storage_type: The broker's storage type.
        :param subnet_ids: The list of groups that define which subnets and IP ranges the broker can use from different Availability Zones. If you specify more than one subnet, the subnets must be in different Availability Zones. Amazon MQ will not be able to create VPC endpoints for your broker with multiple subnets in the same Availability Zone. A SINGLE_INSTANCE deployment requires one subnet (for example, the default subnet). An ACTIVE_STANDBY_MULTI_AZ deployment (ACTIVEMQ) requires two subnets. A CLUSTER_MULTI_AZ deployment (RABBITMQ) has no subnet requirements when deployed with public accessibility, deployment without public accessibility requires at least one subnet. .. epigraph:: If you specify subnets in a shared VPC for a RabbitMQ broker, the associated VPC to which the specified subnets belong must be owned by your AWS account . Amazon MQ will not be able to create VPC enpoints in VPCs that are not owned by your AWS account .
        :param tags: An array of key-value pairs. For more information, see `Using Cost Allocation Tags <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`_ in the *Billing and Cost Management User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_amazonmq as amazonmq
            
            cfn_broker_props = amazonmq.CfnBrokerProps(
                auto_minor_version_upgrade=False,
                broker_name="brokerName",
                deployment_mode="deploymentMode",
                engine_type="engineType",
                engine_version="engineVersion",
                host_instance_type="hostInstanceType",
                publicly_accessible=False,
                users=[amazonmq.CfnBroker.UserProperty(
                    password="password",
                    username="username",
            
                    # the properties below are optional
                    console_access=False,
                    groups=["groups"]
                )],
            
                # the properties below are optional
                authentication_strategy="authenticationStrategy",
                configuration=amazonmq.CfnBroker.ConfigurationIdProperty(
                    id="id",
                    revision=123
                ),
                data_replication_mode="dataReplicationMode",
                data_replication_primary_broker_arn="dataReplicationPrimaryBrokerArn",
                encryption_options=amazonmq.CfnBroker.EncryptionOptionsProperty(
                    use_aws_owned_key=False,
            
                    # the properties below are optional
                    kms_key_id="kmsKeyId"
                ),
                ldap_server_metadata=amazonmq.CfnBroker.LdapServerMetadataProperty(
                    hosts=["hosts"],
                    role_base="roleBase",
                    role_search_matching="roleSearchMatching",
                    service_account_password="serviceAccountPassword",
                    service_account_username="serviceAccountUsername",
                    user_base="userBase",
                    user_search_matching="userSearchMatching",
            
                    # the properties below are optional
                    role_name="roleName",
                    role_search_subtree=False,
                    user_role_name="userRoleName",
                    user_search_subtree=False
                ),
                logs=amazonmq.CfnBroker.LogListProperty(
                    audit=False,
                    general=False
                ),
                maintenance_window_start_time=amazonmq.CfnBroker.MaintenanceWindowProperty(
                    day_of_week="dayOfWeek",
                    time_of_day="timeOfDay",
                    time_zone="timeZone"
                ),
                security_groups=["securityGroups"],
                storage_type="storageType",
                subnet_ids=["subnetIds"],
                tags=[amazonmq.CfnBroker.TagsEntryProperty(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d255f8718bac4d1453cb7e2ae3f8fb5a5ac0ed5b3551f73d52e4123fad831a1c)
            check_type(argname="argument auto_minor_version_upgrade", value=auto_minor_version_upgrade, expected_type=type_hints["auto_minor_version_upgrade"])
            check_type(argname="argument broker_name", value=broker_name, expected_type=type_hints["broker_name"])
            check_type(argname="argument deployment_mode", value=deployment_mode, expected_type=type_hints["deployment_mode"])
            check_type(argname="argument engine_type", value=engine_type, expected_type=type_hints["engine_type"])
            check_type(argname="argument engine_version", value=engine_version, expected_type=type_hints["engine_version"])
            check_type(argname="argument host_instance_type", value=host_instance_type, expected_type=type_hints["host_instance_type"])
            check_type(argname="argument publicly_accessible", value=publicly_accessible, expected_type=type_hints["publicly_accessible"])
            check_type(argname="argument users", value=users, expected_type=type_hints["users"])
            check_type(argname="argument authentication_strategy", value=authentication_strategy, expected_type=type_hints["authentication_strategy"])
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument data_replication_mode", value=data_replication_mode, expected_type=type_hints["data_replication_mode"])
            check_type(argname="argument data_replication_primary_broker_arn", value=data_replication_primary_broker_arn, expected_type=type_hints["data_replication_primary_broker_arn"])
            check_type(argname="argument encryption_options", value=encryption_options, expected_type=type_hints["encryption_options"])
            check_type(argname="argument ldap_server_metadata", value=ldap_server_metadata, expected_type=type_hints["ldap_server_metadata"])
            check_type(argname="argument logs", value=logs, expected_type=type_hints["logs"])
            check_type(argname="argument maintenance_window_start_time", value=maintenance_window_start_time, expected_type=type_hints["maintenance_window_start_time"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument storage_type", value=storage_type, expected_type=type_hints["storage_type"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "auto_minor_version_upgrade": auto_minor_version_upgrade,
            "broker_name": broker_name,
            "deployment_mode": deployment_mode,
            "engine_type": engine_type,
            "engine_version": engine_version,
            "host_instance_type": host_instance_type,
            "publicly_accessible": publicly_accessible,
            "users": users,
        }
        if authentication_strategy is not None:
            self._values["authentication_strategy"] = authentication_strategy
        if configuration is not None:
            self._values["configuration"] = configuration
        if data_replication_mode is not None:
            self._values["data_replication_mode"] = data_replication_mode
        if data_replication_primary_broker_arn is not None:
            self._values["data_replication_primary_broker_arn"] = data_replication_primary_broker_arn
        if encryption_options is not None:
            self._values["encryption_options"] = encryption_options
        if ldap_server_metadata is not None:
            self._values["ldap_server_metadata"] = ldap_server_metadata
        if logs is not None:
            self._values["logs"] = logs
        if maintenance_window_start_time is not None:
            self._values["maintenance_window_start_time"] = maintenance_window_start_time
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if storage_type is not None:
            self._values["storage_type"] = storage_type
        if subnet_ids is not None:
            self._values["subnet_ids"] = subnet_ids
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def auto_minor_version_upgrade(
        self,
    ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Enables automatic upgrades to new minor versions for brokers, as new broker engine versions are released and supported by Amazon MQ.

        Automatic upgrades occur during the scheduled maintenance window of the broker or after a manual broker reboot.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-autominorversionupgrade
        '''
        result = self._values.get("auto_minor_version_upgrade")
        assert result is not None, "Required property 'auto_minor_version_upgrade' is missing"
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

    @builtins.property
    def broker_name(self) -> builtins.str:
        '''The name of the broker.

        This value must be unique in your AWS account , 1-50 characters long, must contain only letters, numbers, dashes, and underscores, and must not contain white spaces, brackets, wildcard characters, or special characters.
        .. epigraph::

           Do not add personally identifiable information (PII) or other confidential or sensitive information in broker names. Broker names are accessible to other AWS services, including C CloudWatch Logs . Broker names are not intended to be used for private or sensitive data.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-brokername
        '''
        result = self._values.get("broker_name")
        assert result is not None, "Required property 'broker_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def deployment_mode(self) -> builtins.str:
        '''The deployment mode of the broker. Available values:.

        - ``SINGLE_INSTANCE``
        - ``ACTIVE_STANDBY_MULTI_AZ``
        - ``CLUSTER_MULTI_AZ``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-deploymentmode
        '''
        result = self._values.get("deployment_mode")
        assert result is not None, "Required property 'deployment_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def engine_type(self) -> builtins.str:
        '''The type of broker engine.

        Currently, Amazon MQ supports ``ACTIVEMQ`` and ``RABBITMQ`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-enginetype
        '''
        result = self._values.get("engine_type")
        assert result is not None, "Required property 'engine_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def engine_version(self) -> builtins.str:
        '''The version of the broker engine.

        For a list of supported engine versions, see `Engine <https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html>`_ in the *Amazon MQ Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-engineversion
        '''
        result = self._values.get("engine_version")
        assert result is not None, "Required property 'engine_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host_instance_type(self) -> builtins.str:
        '''The broker's instance type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-hostinstancetype
        '''
        result = self._values.get("host_instance_type")
        assert result is not None, "Required property 'host_instance_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def publicly_accessible(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Enables connections from applications outside of the VPC that hosts the broker's subnets.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-publiclyaccessible
        '''
        result = self._values.get("publicly_accessible")
        assert result is not None, "Required property 'publicly_accessible' is missing"
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

    @builtins.property
    def users(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnBroker.UserProperty]]]:
        '''The list of broker users (persons or applications) who can access queues and topics.

        For Amazon MQ for RabbitMQ brokers, one and only one administrative user is accepted and created when a broker is first provisioned. All subsequent RabbitMQ users are created by via the RabbitMQ web console or by using the RabbitMQ management API.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-users
        '''
        result = self._values.get("users")
        assert result is not None, "Required property 'users' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnBroker.UserProperty]]], result)

    @builtins.property
    def authentication_strategy(self) -> typing.Optional[builtins.str]:
        '''Optional.

        The authentication strategy used to secure the broker. The default is ``SIMPLE`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-authenticationstrategy
        '''
        result = self._values.get("authentication_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBroker.ConfigurationIdProperty]]:
        '''A list of information about the configuration.

        Does not apply to RabbitMQ brokers.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-configuration
        '''
        result = self._values.get("configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBroker.ConfigurationIdProperty]], result)

    @builtins.property
    def data_replication_mode(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-datareplicationmode
        '''
        result = self._values.get("data_replication_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_replication_primary_broker_arn(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-datareplicationprimarybrokerarn
        '''
        result = self._values.get("data_replication_primary_broker_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBroker.EncryptionOptionsProperty]]:
        '''Encryption options for the broker.

        Does not apply to RabbitMQ brokers.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-encryptionoptions
        '''
        result = self._values.get("encryption_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBroker.EncryptionOptionsProperty]], result)

    @builtins.property
    def ldap_server_metadata(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBroker.LdapServerMetadataProperty]]:
        '''Optional.

        The metadata of the LDAP server used to authenticate and authorize connections to the broker. Does not apply to RabbitMQ brokers.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-ldapservermetadata
        '''
        result = self._values.get("ldap_server_metadata")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBroker.LdapServerMetadataProperty]], result)

    @builtins.property
    def logs(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBroker.LogListProperty]]:
        '''Enables Amazon CloudWatch logging for brokers.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-logs
        '''
        result = self._values.get("logs")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBroker.LogListProperty]], result)

    @builtins.property
    def maintenance_window_start_time(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBroker.MaintenanceWindowProperty]]:
        '''The scheduled time period relative to UTC during which Amazon MQ begins to apply pending updates or patches to the broker.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-maintenancewindowstarttime
        '''
        result = self._values.get("maintenance_window_start_time")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBroker.MaintenanceWindowProperty]], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of rules (1 minimum, 125 maximum) that authorize connections to brokers.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-securitygroups
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def storage_type(self) -> typing.Optional[builtins.str]:
        '''The broker's storage type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-storagetype
        '''
        result = self._values.get("storage_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of groups that define which subnets and IP ranges the broker can use from different Availability Zones.

        If you specify more than one subnet, the subnets must be in different Availability Zones. Amazon MQ will not be able to create VPC endpoints for your broker with multiple subnets in the same Availability Zone. A SINGLE_INSTANCE deployment requires one subnet (for example, the default subnet). An ACTIVE_STANDBY_MULTI_AZ deployment (ACTIVEMQ) requires two subnets. A CLUSTER_MULTI_AZ deployment (RABBITMQ) has no subnet requirements when deployed with public accessibility, deployment without public accessibility requires at least one subnet.
        .. epigraph::

           If you specify subnets in a shared VPC for a RabbitMQ broker, the associated VPC to which the specified subnets belong must be owned by your AWS account . Amazon MQ will not be able to create VPC enpoints in VPCs that are not owned by your AWS account .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-subnetids
        '''
        result = self._values.get("subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[CfnBroker.TagsEntryProperty]]:
        '''An array of key-value pairs.

        For more information, see `Using Cost Allocation Tags <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`_ in the *Billing and Cost Management User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[CfnBroker.TagsEntryProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBrokerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_amazonmq.CfnConfiguration",
):
    '''Creates a new configuration for the specified configuration name.

    Amazon MQ uses the default configuration (the engine type and version).
    .. epigraph::

       Does not apply to RabbitMQ brokers.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_amazonmq as amazonmq
        
        cfn_configuration = amazonmq.CfnConfiguration(self, "MyCfnConfiguration",
            data="data",
            engine_type="engineType",
            engine_version="engineVersion",
            name="name",
        
            # the properties below are optional
            authentication_strategy="authenticationStrategy",
            description="description",
            tags=[amazonmq.CfnConfiguration.TagsEntryProperty(
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
        data: builtins.str,
        engine_type: builtins.str,
        engine_version: builtins.str,
        name: builtins.str,
        authentication_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["CfnConfiguration.TagsEntryProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param data: The base64-encoded XML configuration.
        :param engine_type: The type of broker engine. Note: Currently, Amazon MQ only supports ACTIVEMQ for creating and editing broker configurations.
        :param engine_version: The version of the broker engine. For a list of supported engine versions, see ` <https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html>`_
        :param name: The name of the configuration. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 1-150 characters long.
        :param authentication_strategy: Optional. The authentication strategy associated with the configuration. The default is ``SIMPLE`` .
        :param description: The description of the configuration.
        :param tags: Create tags when creating the configuration.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5d8c71c30a8f2bd8b3e455320ae87cc2204a9546d3ee226605a9575372df4fc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConfigurationProps(
            data=data,
            engine_type=engine_type,
            engine_version=engine_version,
            name=name,
            authentication_strategy=authentication_strategy,
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
            type_hints = typing.get_type_hints(_typecheckingstub__df4e9311d1aa33bca48575d715d3a7e801184dc0b0d7ccbd91d39c5dd0ca05ce)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3d26068de9c2c4b31dd208267b790265051c2f549c0e83ce735c10dbb4dd1fb3)
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
        '''The Amazon Resource Name (ARN) of the Amazon MQ configuration.

        ``arn:aws:mq:us-east-2:123456789012:configuration:MyConfigurationDevelopment:c-1234a5b6-78cd-901e-2fgh-3i45j6k178l9``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the Amazon MQ configuration.

        ``c-1234a5b6-78cd-901e-2fgh-3i45j6k178l9``

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrRevision")
    def attr_revision(self) -> jsii.Number:
        '''The revision number of the configuration.

        ``1``

        :cloudformationAttribute: Revision
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrRevision"))

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
    @jsii.member(jsii_name="data")
    def data(self) -> builtins.str:
        '''The base64-encoded XML configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "data"))

    @data.setter
    def data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93df7b636c49e24d098eef8a55838ad32b99b6986e3499b80882163f47bcceff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "data", value)

    @builtins.property
    @jsii.member(jsii_name="engineType")
    def engine_type(self) -> builtins.str:
        '''The type of broker engine.'''
        return typing.cast(builtins.str, jsii.get(self, "engineType"))

    @engine_type.setter
    def engine_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c128a8f454f5f3c6aa7f53673b3a6ff18a16f9a57d23f00a8ae771a0e07fd47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engineType", value)

    @builtins.property
    @jsii.member(jsii_name="engineVersion")
    def engine_version(self) -> builtins.str:
        '''The version of the broker engine.'''
        return typing.cast(builtins.str, jsii.get(self, "engineVersion"))

    @engine_version.setter
    def engine_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2a28dc59c3dc2c56f801f6ba425c8d15fa5408a1e6494c0c27387fdd42210c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engineVersion", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__289eb9b7603fb0304d15adaf4ff07e313a569aa2af4bf93d7cb2c2f30ad39faf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="authenticationStrategy")
    def authentication_strategy(self) -> typing.Optional[builtins.str]:
        '''Optional.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authenticationStrategy"))

    @authentication_strategy.setter
    def authentication_strategy(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff746c5afeef7636cc2943e0307f0c73fc2e55dc7ec0a26556d504a9fcb0fc00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__480fb06649e1285f95654ba53b3a408febbb52196799763e9131443825beeeaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(
        self,
    ) -> typing.Optional[typing.List["CfnConfiguration.TagsEntryProperty"]]:
        '''Create tags when creating the configuration.'''
        return typing.cast(typing.Optional[typing.List["CfnConfiguration.TagsEntryProperty"]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.List["CfnConfiguration.TagsEntryProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a054ae8c8be290faa22413b18b520f85d06186364109595d98e6fe5dab6126e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amazonmq.CfnConfiguration.TagsEntryProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class TagsEntryProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''A key-value pair to associate with the configuration.

            :param key: The key in a key-value pair.
            :param value: The value in a key-value pair.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-configuration-tagsentry.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amazonmq as amazonmq
                
                tags_entry_property = amazonmq.CfnConfiguration.TagsEntryProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4fe3f9e966befae25ac877bbbdd63895c649331fa5425c359414dd8f24ccc11b)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The key in a key-value pair.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-configuration-tagsentry.html#cfn-amazonmq-configuration-tagsentry-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value in a key-value pair.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-configuration-tagsentry.html#cfn-amazonmq-configuration-tagsentry-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagsEntryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnConfigurationAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_amazonmq.CfnConfigurationAssociation",
):
    '''Use the AWS CloudFormation ``AWS::AmazonMQ::ConfigurationAssociation`` resource to associate a configuration with a broker, or return information about the specified ConfigurationAssociation.

    Only use one per broker, and don't use a configuration on the broker resource if you have associated a configuration with that broker.
    .. epigraph::

       Does not apply to RabbitMQ brokers.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configurationassociation.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_amazonmq as amazonmq
        
        cfn_configuration_association = amazonmq.CfnConfigurationAssociation(self, "MyCfnConfigurationAssociation",
            broker="broker",
            configuration=amazonmq.CfnConfigurationAssociation.ConfigurationIdProperty(
                id="id",
                revision=123
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        broker: builtins.str,
        configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationAssociation.ConfigurationIdProperty", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param broker: The broker to associate with a configuration.
        :param configuration: The configuration to associate with a broker.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bc27c46ef5e7e06d6d69ca58cb1eeb529e57c3a1b1af3771750fe74a0e5a436)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConfigurationAssociationProps(
            broker=broker, configuration=configuration
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79c1d4520032b7f7c0b21bb027542ad67eed75cc3f2420a71560985cd7a5d95b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c2bf2d4a5d6c557ed603a44c98984b27963d1c37cb39e57f78967d32993bebfe)
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
    @jsii.member(jsii_name="broker")
    def broker(self) -> builtins.str:
        '''The broker to associate with a configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "broker"))

    @broker.setter
    def broker(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdbfb700e696e0a2f32b9de9d84566a84719a73bda01942e115e55df84e2750b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "broker", value)

    @builtins.property
    @jsii.member(jsii_name="configuration")
    def configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnConfigurationAssociation.ConfigurationIdProperty"]:
        '''The configuration to associate with a broker.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnConfigurationAssociation.ConfigurationIdProperty"], jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnConfigurationAssociation.ConfigurationIdProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4880b79512d307d86febbd936290d7f133d94115f216f3f043c71ceab0b3e4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuration", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amazonmq.CfnConfigurationAssociation.ConfigurationIdProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id", "revision": "revision"},
    )
    class ConfigurationIdProperty:
        def __init__(self, *, id: builtins.str, revision: jsii.Number) -> None:
            '''The ``ConfigurationId`` property type specifies a configuration Id and the revision of a configuration.

            :param id: The unique ID that Amazon MQ generates for the configuration.
            :param revision: The revision number of the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-configurationassociation-configurationid.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amazonmq as amazonmq
                
                configuration_id_property = amazonmq.CfnConfigurationAssociation.ConfigurationIdProperty(
                    id="id",
                    revision=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__08e92a82af3e279f734ea3e7cb4083780249c19e2dd02ec38e2bacb5b5a4b39b)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument revision", value=revision, expected_type=type_hints["revision"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "id": id,
                "revision": revision,
            }

        @builtins.property
        def id(self) -> builtins.str:
            '''The unique ID that Amazon MQ generates for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-configurationassociation-configurationid.html#cfn-amazonmq-configurationassociation-configurationid-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def revision(self) -> jsii.Number:
            '''The revision number of the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-configurationassociation-configurationid.html#cfn-amazonmq-configurationassociation-configurationid-revision
            '''
            result = self._values.get("revision")
            assert result is not None, "Required property 'revision' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigurationIdProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_amazonmq.CfnConfigurationAssociationProps",
    jsii_struct_bases=[],
    name_mapping={"broker": "broker", "configuration": "configuration"},
)
class CfnConfigurationAssociationProps:
    def __init__(
        self,
        *,
        broker: builtins.str,
        configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationAssociation.ConfigurationIdProperty, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Properties for defining a ``CfnConfigurationAssociation``.

        :param broker: The broker to associate with a configuration.
        :param configuration: The configuration to associate with a broker.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configurationassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_amazonmq as amazonmq
            
            cfn_configuration_association_props = amazonmq.CfnConfigurationAssociationProps(
                broker="broker",
                configuration=amazonmq.CfnConfigurationAssociation.ConfigurationIdProperty(
                    id="id",
                    revision=123
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75f4d3d98205a43f8d3d0c512582ddb9b38aec2162a51f98f40a83656ca93ec8)
            check_type(argname="argument broker", value=broker, expected_type=type_hints["broker"])
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "broker": broker,
            "configuration": configuration,
        }

    @builtins.property
    def broker(self) -> builtins.str:
        '''The broker to associate with a configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configurationassociation.html#cfn-amazonmq-configurationassociation-broker
        '''
        result = self._values.get("broker")
        assert result is not None, "Required property 'broker' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnConfigurationAssociation.ConfigurationIdProperty]:
        '''The configuration to associate with a broker.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configurationassociation.html#cfn-amazonmq-configurationassociation-configuration
        '''
        result = self._values.get("configuration")
        assert result is not None, "Required property 'configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnConfigurationAssociation.ConfigurationIdProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfigurationAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_amazonmq.CfnConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "data": "data",
        "engine_type": "engineType",
        "engine_version": "engineVersion",
        "name": "name",
        "authentication_strategy": "authenticationStrategy",
        "description": "description",
        "tags": "tags",
    },
)
class CfnConfigurationProps:
    def __init__(
        self,
        *,
        data: builtins.str,
        engine_type: builtins.str,
        engine_version: builtins.str,
        name: builtins.str,
        authentication_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[CfnConfiguration.TagsEntryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConfiguration``.

        :param data: The base64-encoded XML configuration.
        :param engine_type: The type of broker engine. Note: Currently, Amazon MQ only supports ACTIVEMQ for creating and editing broker configurations.
        :param engine_version: The version of the broker engine. For a list of supported engine versions, see ` <https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html>`_
        :param name: The name of the configuration. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 1-150 characters long.
        :param authentication_strategy: Optional. The authentication strategy associated with the configuration. The default is ``SIMPLE`` .
        :param description: The description of the configuration.
        :param tags: Create tags when creating the configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_amazonmq as amazonmq
            
            cfn_configuration_props = amazonmq.CfnConfigurationProps(
                data="data",
                engine_type="engineType",
                engine_version="engineVersion",
                name="name",
            
                # the properties below are optional
                authentication_strategy="authenticationStrategy",
                description="description",
                tags=[amazonmq.CfnConfiguration.TagsEntryProperty(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de9d7705a9b711c2e53aeb7eaf29e3a459350a0552e89619099efdb9d14d28cc)
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument engine_type", value=engine_type, expected_type=type_hints["engine_type"])
            check_type(argname="argument engine_version", value=engine_version, expected_type=type_hints["engine_version"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument authentication_strategy", value=authentication_strategy, expected_type=type_hints["authentication_strategy"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data": data,
            "engine_type": engine_type,
            "engine_version": engine_version,
            "name": name,
        }
        if authentication_strategy is not None:
            self._values["authentication_strategy"] = authentication_strategy
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def data(self) -> builtins.str:
        '''The base64-encoded XML configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html#cfn-amazonmq-configuration-data
        '''
        result = self._values.get("data")
        assert result is not None, "Required property 'data' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def engine_type(self) -> builtins.str:
        '''The type of broker engine.

        Note: Currently, Amazon MQ only supports ACTIVEMQ for creating and editing broker configurations.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html#cfn-amazonmq-configuration-enginetype
        '''
        result = self._values.get("engine_type")
        assert result is not None, "Required property 'engine_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def engine_version(self) -> builtins.str:
        '''The version of the broker engine.

        For a list of supported engine versions, see ` <https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html>`_

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html#cfn-amazonmq-configuration-engineversion
        '''
        result = self._values.get("engine_version")
        assert result is not None, "Required property 'engine_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the configuration.

        This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 1-150 characters long.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html#cfn-amazonmq-configuration-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authentication_strategy(self) -> typing.Optional[builtins.str]:
        '''Optional.

        The authentication strategy associated with the configuration. The default is ``SIMPLE`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html#cfn-amazonmq-configuration-authenticationstrategy
        '''
        result = self._values.get("authentication_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html#cfn-amazonmq-configuration-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[CfnConfiguration.TagsEntryProperty]]:
        '''Create tags when creating the configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html#cfn-amazonmq-configuration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[CfnConfiguration.TagsEntryProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnBroker",
    "CfnBrokerProps",
    "CfnConfiguration",
    "CfnConfigurationAssociation",
    "CfnConfigurationAssociationProps",
    "CfnConfigurationProps",
]

publication.publish()

def _typecheckingstub__d16f84aeefdd69c636acf0c8b4d958b93ded39c1da5d5eecb39ce87535c69cb7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    auto_minor_version_upgrade: typing.Union[builtins.bool, _IResolvable_da3f097b],
    broker_name: builtins.str,
    deployment_mode: builtins.str,
    engine_type: builtins.str,
    engine_version: builtins.str,
    host_instance_type: builtins.str,
    publicly_accessible: typing.Union[builtins.bool, _IResolvable_da3f097b],
    users: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBroker.UserProperty, typing.Dict[builtins.str, typing.Any]]]]],
    authentication_strategy: typing.Optional[builtins.str] = None,
    configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBroker.ConfigurationIdProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    data_replication_mode: typing.Optional[builtins.str] = None,
    data_replication_primary_broker_arn: typing.Optional[builtins.str] = None,
    encryption_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBroker.EncryptionOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ldap_server_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBroker.LdapServerMetadataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBroker.LogListProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    maintenance_window_start_time: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBroker.MaintenanceWindowProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    storage_type: typing.Optional[builtins.str] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnBroker.TagsEntryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d7a61b5b47c0d5f9d4072378260a383a676994ae22eab1593156375aeda79a7(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b2faabcb2fd601665f655b0a42ddecd67459d337d8e81f23d1a39ee8cbb4bb0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1becedc098602474059b0aaa465b25ea1b7124443411ed6a42b02d6a5344cdda(
    value: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0511cf4804dad2e6e03dc33f21bf9d654b3598349ced7ea110e5591745f76bdc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35ac0143ff0fe5df5b06639c734e8dce854395762102045c72ecfdd080395609(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edb02169dcf378d5d01cba6368876329b4e7f4e34fde8d2f0f58da09a46b65bd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__631fd780aebb5b339c2238752e33306ea6591245c7231c4db165256d69094ceb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8a51a01838222e13c8eba50f7d568dc975a2e3c5c2d18f21339bc702ffc284b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a82a112ececec828f3c746f7c18e6b6ce32a5aa08550a05a69d7babd8852a7e(
    value: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85b9c0c3c3aa438279362aeaae2a3de844ec906edf5b12b7601c78bc63fbfd6b(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnBroker.UserProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3eab9258c47a74b1aabb4a39e66512dbb010a0f1c8838ec359338808e1f64681(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0eabdb321f6595584d9f056a97a3a7481faa1ad417f76f3ea42484e5ef0b195f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBroker.ConfigurationIdProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fb3d9abae1cb6570b9ccf260c74e4f47d43eda2d732d8b3bcfa03b254143b3e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8ffdb4011b4637fc96f4f2d0dcab95738383a77b9240b6d0f3cdf96f87e7725(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3846e06a73702f6e76ab386acc1ad9128b00ec2357b3396abf86d893cdbae15d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBroker.EncryptionOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8de6a532c388b2fc838b3141f942b6cbbc5d1a796bb76e3fc3fe5a446d932f8(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBroker.LdapServerMetadataProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36b6d40f90e93b4b35c3ffbb3065567a24c0bd9312758826697afa2118901335(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBroker.LogListProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e2d1a75b2e491fa226b7065a64e24f522ac7be048073da54600cfd720b1240f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBroker.MaintenanceWindowProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e87ea78ee8e3d556f9e322090479023fa17920888ca10cd4413f4e00c942ffec(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc1a4f009fd81070f5c68b6193804c7fd4733299a2c55d2e81fd5c11f62da6ec(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa1ab62865033946dc6d8cee45676096e4e10411bffb97c3db615e4d2aa1652f(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__739d50e75e2a93ab9671710563ad1ed5176802aef44a2986de718c86a94e7e8e(
    value: typing.Optional[typing.List[CfnBroker.TagsEntryProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9d5131bf29ed360bf06fb2fc10b8d6ac62da622a4f41bd0e435a4436ba5511c(
    *,
    id: builtins.str,
    revision: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95df5a3839d7c2d80c93cb1b9948b6d4ef43f2e19eb9097abb3cbae048c164aa(
    *,
    use_aws_owned_key: typing.Union[builtins.bool, _IResolvable_da3f097b],
    kms_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__282093319da5ca5716ae9202b23fde6f2380a3a720f7bac369f166119c58cfa8(
    *,
    hosts: typing.Sequence[builtins.str],
    role_base: builtins.str,
    role_search_matching: builtins.str,
    service_account_password: builtins.str,
    service_account_username: builtins.str,
    user_base: builtins.str,
    user_search_matching: builtins.str,
    role_name: typing.Optional[builtins.str] = None,
    role_search_subtree: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    user_role_name: typing.Optional[builtins.str] = None,
    user_search_subtree: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc6518d5765d0a7bdb0ead05cff3d08ab216b44006da8bba35424620fea26077(
    *,
    audit: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    general: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd0060c95e384a30563d722724745751c5579e5b53fa378c0b36e301bb067795(
    *,
    day_of_week: builtins.str,
    time_of_day: builtins.str,
    time_zone: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7825e3fdf121f81e27fcd00d00f2c5d2d105311b09671d687ee257d56a749171(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a458786a0cd0d4269adef0bf3c85862386851ab69649004d5d3dcba4c238445(
    *,
    password: builtins.str,
    username: builtins.str,
    console_access: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    groups: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d255f8718bac4d1453cb7e2ae3f8fb5a5ac0ed5b3551f73d52e4123fad831a1c(
    *,
    auto_minor_version_upgrade: typing.Union[builtins.bool, _IResolvable_da3f097b],
    broker_name: builtins.str,
    deployment_mode: builtins.str,
    engine_type: builtins.str,
    engine_version: builtins.str,
    host_instance_type: builtins.str,
    publicly_accessible: typing.Union[builtins.bool, _IResolvable_da3f097b],
    users: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBroker.UserProperty, typing.Dict[builtins.str, typing.Any]]]]],
    authentication_strategy: typing.Optional[builtins.str] = None,
    configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBroker.ConfigurationIdProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    data_replication_mode: typing.Optional[builtins.str] = None,
    data_replication_primary_broker_arn: typing.Optional[builtins.str] = None,
    encryption_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBroker.EncryptionOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ldap_server_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBroker.LdapServerMetadataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBroker.LogListProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    maintenance_window_start_time: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBroker.MaintenanceWindowProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    storage_type: typing.Optional[builtins.str] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnBroker.TagsEntryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5d8c71c30a8f2bd8b3e455320ae87cc2204a9546d3ee226605a9575372df4fc(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    data: builtins.str,
    engine_type: builtins.str,
    engine_version: builtins.str,
    name: builtins.str,
    authentication_strategy: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnConfiguration.TagsEntryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df4e9311d1aa33bca48575d715d3a7e801184dc0b0d7ccbd91d39c5dd0ca05ce(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d26068de9c2c4b31dd208267b790265051c2f549c0e83ce735c10dbb4dd1fb3(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93df7b636c49e24d098eef8a55838ad32b99b6986e3499b80882163f47bcceff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c128a8f454f5f3c6aa7f53673b3a6ff18a16f9a57d23f00a8ae771a0e07fd47(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2a28dc59c3dc2c56f801f6ba425c8d15fa5408a1e6494c0c27387fdd42210c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__289eb9b7603fb0304d15adaf4ff07e313a569aa2af4bf93d7cb2c2f30ad39faf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff746c5afeef7636cc2943e0307f0c73fc2e55dc7ec0a26556d504a9fcb0fc00(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__480fb06649e1285f95654ba53b3a408febbb52196799763e9131443825beeeaf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a054ae8c8be290faa22413b18b520f85d06186364109595d98e6fe5dab6126e6(
    value: typing.Optional[typing.List[CfnConfiguration.TagsEntryProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fe3f9e966befae25ac877bbbdd63895c649331fa5425c359414dd8f24ccc11b(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bc27c46ef5e7e06d6d69ca58cb1eeb529e57c3a1b1af3771750fe74a0e5a436(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    broker: builtins.str,
    configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationAssociation.ConfigurationIdProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79c1d4520032b7f7c0b21bb027542ad67eed75cc3f2420a71560985cd7a5d95b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2bf2d4a5d6c557ed603a44c98984b27963d1c37cb39e57f78967d32993bebfe(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdbfb700e696e0a2f32b9de9d84566a84719a73bda01942e115e55df84e2750b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4880b79512d307d86febbd936290d7f133d94115f216f3f043c71ceab0b3e4c(
    value: typing.Union[_IResolvable_da3f097b, CfnConfigurationAssociation.ConfigurationIdProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08e92a82af3e279f734ea3e7cb4083780249c19e2dd02ec38e2bacb5b5a4b39b(
    *,
    id: builtins.str,
    revision: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75f4d3d98205a43f8d3d0c512582ddb9b38aec2162a51f98f40a83656ca93ec8(
    *,
    broker: builtins.str,
    configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationAssociation.ConfigurationIdProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de9d7705a9b711c2e53aeb7eaf29e3a459350a0552e89619099efdb9d14d28cc(
    *,
    data: builtins.str,
    engine_type: builtins.str,
    engine_version: builtins.str,
    name: builtins.str,
    authentication_strategy: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnConfiguration.TagsEntryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
