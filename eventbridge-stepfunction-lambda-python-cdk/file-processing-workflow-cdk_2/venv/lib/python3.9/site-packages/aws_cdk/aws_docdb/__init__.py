'''
# Amazon DocumentDB Construct Library

## Starting a Clustered Database

To set up a clustered DocumentDB database, define a `DatabaseCluster`. You must
always launch a database in a VPC. Use the `vpcSubnets` attribute to control whether
your instances will be launched privately or publicly:

```python
# vpc: ec2.Vpc

cluster = docdb.DatabaseCluster(self, "Database",
    master_user=docdb.Login(
        username="myuser",  # NOTE: 'admin' is reserved by DocumentDB
        exclude_characters="\"@/:",  # optional, defaults to the set "\"@/" and is also used for eventually created rotations
        secret_name="/myapp/mydocdb/masteruser"
    ),
    instance_type=ec2.InstanceType.of(ec2.InstanceClass.MEMORY5, ec2.InstanceSize.LARGE),
    vpc_subnets=ec2.SubnetSelection(
        subnet_type=ec2.SubnetType.PUBLIC
    ),
    vpc=vpc
)
```

By default, the master password will be generated and stored in AWS Secrets Manager with auto-generated description.

Your cluster will be empty by default.

## Connecting

To control who can access the cluster, use the `.connections` attribute. DocumentDB databases have a default port, so
you don't need to specify the port:

```python
# cluster: docdb.DatabaseCluster

cluster.connections.allow_default_port_from_any_ipv4("Open to the world")
```

The endpoints to access your database cluster will be available as the `.clusterEndpoint` and `.clusterReadEndpoint`
attributes:

```python
# cluster: docdb.DatabaseCluster

write_address = cluster.cluster_endpoint.socket_address
```

If you have existing security groups you would like to add to the cluster, use the `addSecurityGroups` method. Security
groups added in this way will not be managed by the `Connections` object of the cluster.

```python
# vpc: ec2.Vpc
# cluster: docdb.DatabaseCluster


security_group = ec2.SecurityGroup(self, "SecurityGroup",
    vpc=vpc
)
cluster.add_security_groups(security_group)
```

## Deletion protection

Deletion protection can be enabled on an Amazon DocumentDB cluster to prevent accidental deletion of the cluster:

```python
# vpc: ec2.Vpc

cluster = docdb.DatabaseCluster(self, "Database",
    master_user=docdb.Login(
        username="myuser"
    ),
    instance_type=ec2.InstanceType.of(ec2.InstanceClass.MEMORY5, ec2.InstanceSize.LARGE),
    vpc_subnets=ec2.SubnetSelection(
        subnet_type=ec2.SubnetType.PUBLIC
    ),
    vpc=vpc,
    deletion_protection=True
)
```

## Rotating credentials

When the master password is generated and stored in AWS Secrets Manager, it can be rotated automatically:

```python
# cluster: docdb.DatabaseCluster

cluster.add_rotation_single_user()
```

```python
cluster = docdb.DatabaseCluster(stack, "Database",
    master_user=cdk.aws_docdb.Login(
        username="docdb"
    ),
    instance_type=ec2.InstanceType.of(ec2.InstanceClass.R5, ec2.InstanceSize.LARGE),
    vpc=vpc,
    removal_policy=cdk.RemovalPolicy.DESTROY
)

cluster.add_rotation_single_user()
```

The multi user rotation scheme is also available:

```python
import aws_cdk.aws_secretsmanager as secretsmanager

# my_imported_secret: secretsmanager.Secret
# cluster: docdb.DatabaseCluster


cluster.add_rotation_multi_user("MyUser",
    secret=my_imported_secret
)
```

It's also possible to create user credentials together with the cluster and add rotation:

```python
# cluster: docdb.DatabaseCluster

my_user_secret = docdb.DatabaseSecret(self, "MyUserSecret",
    username="myuser",
    master_secret=cluster.secret
)
my_user_secret_attached = my_user_secret.attach(cluster) # Adds DB connections information in the secret

cluster.add_rotation_multi_user("MyUser",  # Add rotation using the multi user scheme
    secret=my_user_secret_attached)
```

**Note**: This user must be created manually in the database using the master credentials.
The rotation will start as soon as this user exists.

See also [aws-cdk-lib/aws-secretsmanager](https://github.com/aws/aws-cdk/blob/main/packages/aws-cdk-lib/aws-secretsmanager/README.md) for credentials rotation of existing clusters.

## Audit and profiler Logs

Sending audit or profiler needs to be configured in two places:

1. Check / create the needed options in your ParameterGroup for [audit](https://docs.aws.amazon.com/documentdb/latest/developerguide/event-auditing.html#event-auditing-enabling-auditing) and
   [profiler](https://docs.aws.amazon.com/documentdb/latest/developerguide/profiling.html#profiling.enable-profiling) logs.
2. Enable the corresponding option(s) when creating the `DatabaseCluster`:

```python
import aws_cdk.aws_iam as iam
import aws_cdk.aws_logs as logs

# my_logs_publishing_role: iam.Role
# vpc: ec2.Vpc


cluster = docdb.DatabaseCluster(self, "Database",
    master_user=docdb.Login(
        username="myuser"
    ),
    instance_type=ec2.InstanceType.of(ec2.InstanceClass.MEMORY5, ec2.InstanceSize.LARGE),
    vpc_subnets=ec2.SubnetSelection(
        subnet_type=ec2.SubnetType.PUBLIC
    ),
    vpc=vpc,
    export_profiler_logs_to_cloud_watch=True,  # Enable sending profiler logs
    export_audit_logs_to_cloud_watch=True,  # Enable sending audit logs
    cloud_watch_logs_retention=logs.RetentionDays.THREE_MONTHS,  # Optional - default is to never expire logs
    cloud_watch_logs_retention_role=my_logs_publishing_role
)
```

## Enable Performance Insights

By enabling this feature it will be cascaded and enabled in all instances inside the cluster:

```python
# vpc: ec2.Vpc


cluster = docdb.DatabaseCluster(self, "Database",
    master_user=docdb.Login(
        username="myuser"
    ),
    instance_type=ec2.InstanceType.of(ec2.InstanceClass.MEMORY5, ec2.InstanceSize.LARGE),
    vpc_subnets=ec2.SubnetSelection(
        subnet_type=ec2.SubnetType.PUBLIC
    ),
    vpc=vpc,
    enable_performance_insights=True
)
```
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
    Duration as _Duration_4839e8c3,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    IResource as _IResource_c80c4260,
    ITaggable as _ITaggable_36806126,
    RemovalPolicy as _RemovalPolicy_9f93c814,
    Resource as _Resource_45bc6135,
    SecretValue as _SecretValue_3dd0ddae,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..aws_ec2 import (
    Connections as _Connections_0f31fce8,
    IConnectable as _IConnectable_10015a05,
    ISecurityGroup as _ISecurityGroup_acf8a799,
    IVpc as _IVpc_f30d5663,
    InstanceType as _InstanceType_f64915b9,
    SubnetSelection as _SubnetSelection_e57d76df,
)
from ..aws_iam import IRole as _IRole_235f5d8e
from ..aws_kms import IKey as _IKey_5f11635f
from ..aws_logs import RetentionDays as _RetentionDays_070f99f0
from ..aws_secretsmanager import (
    ISecret as _ISecret_6e020e6a,
    ISecretAttachmentTarget as _ISecretAttachmentTarget_123e2df9,
    Secret as _Secret_50778576,
    SecretAttachmentTargetProps as _SecretAttachmentTargetProps_9ec7949d,
    SecretRotation as _SecretRotation_38c354d9,
)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_docdb.BackupProps",
    jsii_struct_bases=[],
    name_mapping={"retention": "retention", "preferred_window": "preferredWindow"},
)
class BackupProps:
    def __init__(
        self,
        *,
        retention: _Duration_4839e8c3,
        preferred_window: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Backup configuration for DocumentDB databases.

        :param retention: How many days to retain the backup.
        :param preferred_window: A daily time range in 24-hours UTC format in which backups preferably execute. Must be at least 30 minutes long. Example: '01:00-02:00' Default: - a 30-minute window selected at random from an 8-hour block of time for each AWS Region. To see the time blocks available, see https://docs.aws.amazon.com/documentdb/latest/developerguide/backup-restore.db-cluster-snapshots.html#backup-restore.backup-window

        :default:

        - The retention period for automated backups is 1 day.
        The preferred backup window will be a 30-minute window selected at random
        from an 8-hour block of time for each AWS Region.

        :see: https://docs.aws.amazon.com/documentdb/latest/developerguide/backup-restore.db-cluster-snapshots.html#backup-restore.backup-window
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_docdb as docdb
            
            backup_props = docdb.BackupProps(
                retention=cdk.Duration.minutes(30),
            
                # the properties below are optional
                preferred_window="preferredWindow"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee6fe0fa77944f4ac01bc65293ff8588d9093a5a1b3fa48a6bab1d3e79b40b09)
            check_type(argname="argument retention", value=retention, expected_type=type_hints["retention"])
            check_type(argname="argument preferred_window", value=preferred_window, expected_type=type_hints["preferred_window"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "retention": retention,
        }
        if preferred_window is not None:
            self._values["preferred_window"] = preferred_window

    @builtins.property
    def retention(self) -> _Duration_4839e8c3:
        '''How many days to retain the backup.'''
        result = self._values.get("retention")
        assert result is not None, "Required property 'retention' is missing"
        return typing.cast(_Duration_4839e8c3, result)

    @builtins.property
    def preferred_window(self) -> typing.Optional[builtins.str]:
        '''A daily time range in 24-hours UTC format in which backups preferably execute.

        Must be at least 30 minutes long.

        Example: '01:00-02:00'

        :default:

        - a 30-minute window selected at random from an 8-hour block of
        time for each AWS Region. To see the time blocks available, see
        https://docs.aws.amazon.com/documentdb/latest/developerguide/backup-restore.db-cluster-snapshots.html#backup-restore.backup-window
        '''
        result = self._values.get("preferred_window")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnDBCluster(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_docdb.CfnDBCluster",
):
    '''The ``AWS::DocDB::DBCluster`` Amazon DocumentDB (with MongoDB compatibility) resource describes a DBCluster.

    Amazon DocumentDB is a fully managed, MongoDB-compatible document database engine. For more information, see `DBCluster <https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DBCluster.html>`_ in the *Amazon DocumentDB Developer Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_docdb as docdb
        
        cfn_dBCluster = docdb.CfnDBCluster(self, "MyCfnDBCluster",
            availability_zones=["availabilityZones"],
            backup_retention_period=123,
            copy_tags_to_snapshot=False,
            db_cluster_identifier="dbClusterIdentifier",
            db_cluster_parameter_group_name="dbClusterParameterGroupName",
            db_subnet_group_name="dbSubnetGroupName",
            deletion_protection=False,
            enable_cloudwatch_logs_exports=["enableCloudwatchLogsExports"],
            engine_version="engineVersion",
            kms_key_id="kmsKeyId",
            master_username="masterUsername",
            master_user_password="masterUserPassword",
            port=123,
            preferred_backup_window="preferredBackupWindow",
            preferred_maintenance_window="preferredMaintenanceWindow",
            restore_to_time="restoreToTime",
            restore_type="restoreType",
            snapshot_identifier="snapshotIdentifier",
            source_db_cluster_identifier="sourceDbClusterIdentifier",
            storage_encrypted=False,
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            use_latest_restorable_time=False,
            vpc_security_group_ids=["vpcSecurityGroupIds"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        backup_retention_period: typing.Optional[jsii.Number] = None,
        copy_tags_to_snapshot: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        db_cluster_identifier: typing.Optional[builtins.str] = None,
        db_cluster_parameter_group_name: typing.Optional[builtins.str] = None,
        db_subnet_group_name: typing.Optional[builtins.str] = None,
        deletion_protection: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        enable_cloudwatch_logs_exports: typing.Optional[typing.Sequence[builtins.str]] = None,
        engine_version: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        master_username: typing.Optional[builtins.str] = None,
        master_user_password: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        preferred_backup_window: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        restore_to_time: typing.Optional[builtins.str] = None,
        restore_type: typing.Optional[builtins.str] = None,
        snapshot_identifier: typing.Optional[builtins.str] = None,
        source_db_cluster_identifier: typing.Optional[builtins.str] = None,
        storage_encrypted: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        use_latest_restorable_time: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param availability_zones: A list of Amazon EC2 Availability Zones that instances in the cluster can be created in.
        :param backup_retention_period: The number of days for which automated backups are retained. You must specify a minimum value of 1. Default: 1 Constraints: - Must be a value from 1 to 35.
        :param copy_tags_to_snapshot: 
        :param db_cluster_identifier: The cluster identifier. This parameter is stored as a lowercase string. Constraints: - Must contain from 1 to 63 letters, numbers, or hyphens. - The first character must be a letter. - Cannot end with a hyphen or contain two consecutive hyphens. Example: ``my-cluster``
        :param db_cluster_parameter_group_name: The name of the cluster parameter group to associate with this cluster.
        :param db_subnet_group_name: A subnet group to associate with this cluster. Constraints: Must match the name of an existing ``DBSubnetGroup`` . Must not be default. Example: ``mySubnetgroup``
        :param deletion_protection: Protects clusters from being accidentally deleted. If enabled, the cluster cannot be deleted unless it is modified and ``DeletionProtection`` is disabled.
        :param enable_cloudwatch_logs_exports: The list of log types that need to be enabled for exporting to Amazon CloudWatch Logs. You can enable audit logs or profiler logs. For more information, see `Auditing Amazon DocumentDB Events <https://docs.aws.amazon.com/documentdb/latest/developerguide/event-auditing.html>`_ and `Profiling Amazon DocumentDB Operations <https://docs.aws.amazon.com/documentdb/latest/developerguide/profiling.html>`_ .
        :param engine_version: The version number of the database engine to use. The ``--engine-version`` will default to the latest major engine version. For production workloads, we recommend explicitly declaring this parameter with the intended major engine version.
        :param kms_key_id: The AWS KMS key identifier for an encrypted cluster. The AWS KMS key identifier is the Amazon Resource Name (ARN) for the AWS KMS encryption key. If you are creating a cluster using the same AWS account that owns the AWS KMS encryption key that is used to encrypt the new cluster, you can use the AWS KMS key alias instead of the ARN for the AWS KMS encryption key. If an encryption key is not specified in ``KmsKeyId`` : - If the ``StorageEncrypted`` parameter is ``true`` , Amazon DocumentDB uses your default encryption key. AWS KMS creates the default encryption key for your AWS account . Your AWS account has a different default encryption key for each AWS Regions .
        :param master_username: The name of the master user for the cluster. Constraints: - Must be from 1 to 63 letters or numbers. - The first character must be a letter. - Cannot be a reserved word for the chosen database engine.
        :param master_user_password: The password for the master database user. This password can contain any printable ASCII character except forward slash (/), double quote ("), or the "at" symbol (@). Constraints: Must contain from 8 to 100 characters.
        :param port: Specifies the port that the database engine is listening on.
        :param preferred_backup_window: The daily time range during which automated backups are created if automated backups are enabled using the ``BackupRetentionPeriod`` parameter. The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region . Constraints: - Must be in the format ``hh24:mi-hh24:mi`` . - Must be in Universal Coordinated Time (UTC). - Must not conflict with the preferred maintenance window. - Must be at least 30 minutes.
        :param preferred_maintenance_window: The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC). Format: ``ddd:hh24:mi-ddd:hh24:mi`` The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region , occurring on a random day of the week. Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun Constraints: Minimum 30-minute window.
        :param restore_to_time: 
        :param restore_type: 
        :param snapshot_identifier: The identifier for the snapshot or cluster snapshot to restore from. You can use either the name or the Amazon Resource Name (ARN) to specify a cluster snapshot. However, you can use only the ARN to specify a snapshot. Constraints: - Must match the identifier of an existing snapshot.
        :param source_db_cluster_identifier: 
        :param storage_encrypted: Specifies whether the cluster is encrypted.
        :param tags: The tags to be assigned to the cluster.
        :param use_latest_restorable_time: 
        :param vpc_security_group_ids: A list of EC2 VPC security groups to associate with this cluster.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7db61dc80f26049d79a38255d8a0b3abaf4b5019d7cbed64c937ec0f3e40056c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDBClusterProps(
            availability_zones=availability_zones,
            backup_retention_period=backup_retention_period,
            copy_tags_to_snapshot=copy_tags_to_snapshot,
            db_cluster_identifier=db_cluster_identifier,
            db_cluster_parameter_group_name=db_cluster_parameter_group_name,
            db_subnet_group_name=db_subnet_group_name,
            deletion_protection=deletion_protection,
            enable_cloudwatch_logs_exports=enable_cloudwatch_logs_exports,
            engine_version=engine_version,
            kms_key_id=kms_key_id,
            master_username=master_username,
            master_user_password=master_user_password,
            port=port,
            preferred_backup_window=preferred_backup_window,
            preferred_maintenance_window=preferred_maintenance_window,
            restore_to_time=restore_to_time,
            restore_type=restore_type,
            snapshot_identifier=snapshot_identifier,
            source_db_cluster_identifier=source_db_cluster_identifier,
            storage_encrypted=storage_encrypted,
            tags=tags,
            use_latest_restorable_time=use_latest_restorable_time,
            vpc_security_group_ids=vpc_security_group_ids,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f49adaa49bdc08b786dfe6f113030ff5dd0db0af1cab13c2ea50ea5487f4b802)
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
            type_hints = typing.get_type_hints(_typecheckingstub__49d68682da6d2b0ce5ca0609607e472a09f9f77f27ba4214de01d037f2eca6c6)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrClusterResourceId")
    def attr_cluster_resource_id(self) -> builtins.str:
        '''The resource id for the cluster;

        for example: ``cluster-ABCD1234EFGH5678IJKL90MNOP`` . The cluster ID uniquely identifies the cluster and is used in things like IAM authentication policies.

        :cloudformationAttribute: ClusterResourceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrClusterResourceId"))

    @builtins.property
    @jsii.member(jsii_name="attrEndpoint")
    def attr_endpoint(self) -> builtins.str:
        '''The connection endpoint for the cluster, such as ``sample-cluster.cluster-cozrlsfrcjoc.us-east-1.docdb.amazonaws.com`` .

        :cloudformationAttribute: Endpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrPort")
    def attr_port(self) -> builtins.str:
        '''The port number on which the cluster accepts connections.

        For example: ``27017`` .

        :cloudformationAttribute: Port
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPort"))

    @builtins.property
    @jsii.member(jsii_name="attrReadEndpoint")
    def attr_read_endpoint(self) -> builtins.str:
        '''The reader endpoint for the cluster.

        For example: ``sample-cluster.cluster-ro-cozrlsfrcjoc.us-east-1.docdb.amazonaws.com`` .

        :cloudformationAttribute: ReadEndpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrReadEndpoint"))

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
    @jsii.member(jsii_name="availabilityZones")
    def availability_zones(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of Amazon EC2 Availability Zones that instances in the cluster can be created in.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "availabilityZones"))

    @availability_zones.setter
    def availability_zones(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4bdaf0bc7cad58ade1a34b4b85daf3a0c9caf4e9c4aa423d8c08839742b0d4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZones", value)

    @builtins.property
    @jsii.member(jsii_name="backupRetentionPeriod")
    def backup_retention_period(self) -> typing.Optional[jsii.Number]:
        '''The number of days for which automated backups are retained.

        You must specify a minimum value of 1.
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "backupRetentionPeriod"))

    @backup_retention_period.setter
    def backup_retention_period(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c664a6034ddc5d1a75cd1bae48398fc11875b13ff09951c293559b0708786b47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupRetentionPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="copyTagsToSnapshot")
    def copy_tags_to_snapshot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "copyTagsToSnapshot"))

    @copy_tags_to_snapshot.setter
    def copy_tags_to_snapshot(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9579155c60f37e7baaefd2add0496a87f54293584ec94a2a7785dc3264ebe4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "copyTagsToSnapshot", value)

    @builtins.property
    @jsii.member(jsii_name="dbClusterIdentifier")
    def db_cluster_identifier(self) -> typing.Optional[builtins.str]:
        '''The cluster identifier.

        This parameter is stored as a lowercase string.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbClusterIdentifier"))

    @db_cluster_identifier.setter
    def db_cluster_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22fbd7b0bf1256197f71b3b43f4d11d7eb59e118a93d9b0c59335aea8e7b586f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbClusterIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="dbClusterParameterGroupName")
    def db_cluster_parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the cluster parameter group to associate with this cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbClusterParameterGroupName"))

    @db_cluster_parameter_group_name.setter
    def db_cluster_parameter_group_name(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1a2f5fa89f057ba4759b48019d5a08e9de7fcb5cc68ed5ace17b6303dec5d87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbClusterParameterGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="dbSubnetGroupName")
    def db_subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''A subnet group to associate with this cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbSubnetGroupName"))

    @db_subnet_group_name.setter
    def db_subnet_group_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43f1e52bdd69041102d5550de099fe30eb54180c8559f2760b4c5a4cb3af9e07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbSubnetGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="deletionProtection")
    def deletion_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Protects clusters from being accidentally deleted.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "deletionProtection"))

    @deletion_protection.setter
    def deletion_protection(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc9a3746b34c3c8e0f788ea45970b8e53d09b5b282a722fbed39cfe0b59b8f97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deletionProtection", value)

    @builtins.property
    @jsii.member(jsii_name="enableCloudwatchLogsExports")
    def enable_cloudwatch_logs_exports(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of log types that need to be enabled for exporting to Amazon CloudWatch Logs.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "enableCloudwatchLogsExports"))

    @enable_cloudwatch_logs_exports.setter
    def enable_cloudwatch_logs_exports(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b98a157c72eff100321309f96926d75d4cfd89d474c71de6df075763daff6e71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableCloudwatchLogsExports", value)

    @builtins.property
    @jsii.member(jsii_name="engineVersion")
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''The version number of the database engine to use.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engineVersion"))

    @engine_version.setter
    def engine_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6c3f347d46adbb72bedc7428b15c6469cfe26cf4f30488e8abd2f8f22ca84d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engineVersion", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The AWS KMS key identifier for an encrypted cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03e9375b32d036932973e964a270516d21d155bd0db4369d824ccb7e7f0bdc62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="masterUsername")
    def master_username(self) -> typing.Optional[builtins.str]:
        '''The name of the master user for the cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "masterUsername"))

    @master_username.setter
    def master_username(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c07cdadbef8a45e2db19e8559d89c8cec47c9d2d698c3fc441a996847907dfc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterUsername", value)

    @builtins.property
    @jsii.member(jsii_name="masterUserPassword")
    def master_user_password(self) -> typing.Optional[builtins.str]:
        '''The password for the master database user.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "masterUserPassword"))

    @master_user_password.setter
    def master_user_password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2998c76e0321a3f0bc1fe35b15ded5ba4f630cb6e5e7519736bf7455e2abe14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterUserPassword", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> typing.Optional[jsii.Number]:
        '''Specifies the port that the database engine is listening on.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "port"))

    @port.setter
    def port(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a09b878a6d8b852d7eb17f26dcd8f718779776e12f67987303b1e944b3a40516)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="preferredBackupWindow")
    def preferred_backup_window(self) -> typing.Optional[builtins.str]:
        '''The daily time range during which automated backups are created if automated backups are enabled using the ``BackupRetentionPeriod`` parameter.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredBackupWindow"))

    @preferred_backup_window.setter
    def preferred_backup_window(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__903ec8bf5c75ee86965cb4a2c278ea1e1e98dd095e22060664e8fa764f66256e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredBackupWindow", value)

    @builtins.property
    @jsii.member(jsii_name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredMaintenanceWindow"))

    @preferred_maintenance_window.setter
    def preferred_maintenance_window(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4322d6fabf4d2d1ef485d3e448e48faf3b9968a20e9c0b97b5a07213032c1c30)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredMaintenanceWindow", value)

    @builtins.property
    @jsii.member(jsii_name="restoreToTime")
    def restore_to_time(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "restoreToTime"))

    @restore_to_time.setter
    def restore_to_time(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0ee86da53d4a8f5b7ebf251632e7ba9588ee4112a830c775ece3433f227e29c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restoreToTime", value)

    @builtins.property
    @jsii.member(jsii_name="restoreType")
    def restore_type(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "restoreType"))

    @restore_type.setter
    def restore_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43c278d2c39f8d3f098ad2320789939b448b2958965646678cb8dd9f218f8736)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restoreType", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotIdentifier")
    def snapshot_identifier(self) -> typing.Optional[builtins.str]:
        '''The identifier for the snapshot or cluster snapshot to restore from.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotIdentifier"))

    @snapshot_identifier.setter
    def snapshot_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9827e5902a31fbb3009632e22e0590a6a453b8ad1f433893f790e68c5abe9b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="sourceDbClusterIdentifier")
    def source_db_cluster_identifier(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceDbClusterIdentifier"))

    @source_db_cluster_identifier.setter
    def source_db_cluster_identifier(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38eacfeb3f4a2ffe2d0fb22ed93a5652cb018e7fed96bb166e4d29176228a8d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceDbClusterIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="storageEncrypted")
    def storage_encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the cluster is encrypted.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "storageEncrypted"))

    @storage_encrypted.setter
    def storage_encrypted(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efd881b325008feb4534c0ce6da0a09c3cfeabe00ff36a389bdfadd597bcf73f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageEncrypted", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to be assigned to the cluster.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__467cb576faa79b69ba7e6b18a96e5bbf103b0f9e2e68b9ca5c5b6baa2c3116c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="useLatestRestorableTime")
    def use_latest_restorable_time(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "useLatestRestorableTime"))

    @use_latest_restorable_time.setter
    def use_latest_restorable_time(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__313b92cc69cbcbc01b1b3c76867167207277927cc984c7fd4f92ea48c138bbda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useLatestRestorableTime", value)

    @builtins.property
    @jsii.member(jsii_name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of EC2 VPC security groups to associate with this cluster.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vpcSecurityGroupIds"))

    @vpc_security_group_ids.setter
    def vpc_security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__461b181007a5279b076f42e5ac0a26f146fd3b28454ba100be1045b0614f2f9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcSecurityGroupIds", value)


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnDBClusterParameterGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_docdb.CfnDBClusterParameterGroup",
):
    '''The ``AWS::DocDB::DBClusterParameterGroup`` Amazon DocumentDB (with MongoDB compatibility) resource describes a DBClusterParameterGroup.

    For more information, see `DBClusterParameterGroup <https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DBClusterParameterGroup.html>`_ in the *Amazon DocumentDB Developer Guide* .

    Parameters in a cluster parameter group apply to all of the instances in a cluster.

    A cluster parameter group is initially created with the default parameters for the database engine used by instances in the cluster. To provide custom values for any of the parameters, you must modify the group after you create it. After you create a DB cluster parameter group, you must associate it with your cluster. For the new cluster parameter group and associated settings to take effect, you must then reboot the DB instances in the cluster without failover.
    .. epigraph::

       After you create a cluster parameter group, you should wait at least 5 minutes before creating your first cluster that uses that cluster parameter group as the default parameter group. This allows Amazon DocumentDB to fully complete the create action before the cluster parameter group is used as the default for a new cluster. This step is especially important for parameters that are critical when creating the default database for a cluster, such as the character set for the default database defined by the ``character_set_database`` parameter.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_docdb as docdb
        
        # parameters: Any
        
        cfn_dBCluster_parameter_group = docdb.CfnDBClusterParameterGroup(self, "MyCfnDBClusterParameterGroup",
            description="description",
            family="family",
            parameters=parameters,
        
            # the properties below are optional
            name="name",
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
        description: builtins.str,
        family: builtins.str,
        parameters: typing.Any,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param description: The description for the cluster parameter group.
        :param family: The cluster parameter group family name.
        :param parameters: Provides a list of parameters for the cluster parameter group.
        :param name: The name of the DB cluster parameter group. Constraints: - Must not match the name of an existing ``DBClusterParameterGroup`` . .. epigraph:: This value is stored as a lowercase string.
        :param tags: The tags to be assigned to the cluster parameter group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf702887107dc3b6d0e1c2cf7a2f922b9fa66ae4817c7d3122ceaf8e3b958132)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDBClusterParameterGroupProps(
            description=description,
            family=family,
            parameters=parameters,
            name=name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6a8171791541b174749473c2f0235ec8f6d2df6bcf47a0de97a3e0d0f5f4ba1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0c1f45d655c3578d1faf53be5531c206b7adce79fc6ed731b32498a9f03d92eb)
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
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''The description for the cluster parameter group.'''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e27b4f0b3d2455b83e7b94d42a23c0c8ff2300e3ab6fba5c69d15cd9464adb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="family")
    def family(self) -> builtins.str:
        '''The cluster parameter group family name.'''
        return typing.cast(builtins.str, jsii.get(self, "family"))

    @family.setter
    def family(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bdc5b6562ba3c1478a5fee7c979b6215b64e8bb2b58e86475cfde6421ae1272)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "family", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Any:
        '''Provides a list of parameters for the cluster parameter group.'''
        return typing.cast(typing.Any, jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__332a0d384ecea2c65bb972833483a0e813f12d76d753ec68ce55267e1a229804)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the DB cluster parameter group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__702d9cc13fd6cd2a95ea6c1b6615540be0c5afe0086986a3555d3d957840d35b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to be assigned to the cluster parameter group.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e8ee52ae08b545bed27f58e883eee6b47f43f216f34098f0850a8bd9e024e08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_docdb.CfnDBClusterParameterGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "family": "family",
        "parameters": "parameters",
        "name": "name",
        "tags": "tags",
    },
)
class CfnDBClusterParameterGroupProps:
    def __init__(
        self,
        *,
        description: builtins.str,
        family: builtins.str,
        parameters: typing.Any,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDBClusterParameterGroup``.

        :param description: The description for the cluster parameter group.
        :param family: The cluster parameter group family name.
        :param parameters: Provides a list of parameters for the cluster parameter group.
        :param name: The name of the DB cluster parameter group. Constraints: - Must not match the name of an existing ``DBClusterParameterGroup`` . .. epigraph:: This value is stored as a lowercase string.
        :param tags: The tags to be assigned to the cluster parameter group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_docdb as docdb
            
            # parameters: Any
            
            cfn_dBCluster_parameter_group_props = docdb.CfnDBClusterParameterGroupProps(
                description="description",
                family="family",
                parameters=parameters,
            
                # the properties below are optional
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ece7bd2ef5aeaa71e7436ee669c393da120bf9e46815bde86b3caa96d817ca2)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument family", value=family, expected_type=type_hints["family"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "family": family,
            "parameters": parameters,
        }
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> builtins.str:
        '''The description for the cluster parameter group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html#cfn-docdb-dbclusterparametergroup-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def family(self) -> builtins.str:
        '''The cluster parameter group family name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html#cfn-docdb-dbclusterparametergroup-family
        '''
        result = self._values.get("family")
        assert result is not None, "Required property 'family' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(self) -> typing.Any:
        '''Provides a list of parameters for the cluster parameter group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html#cfn-docdb-dbclusterparametergroup-parameters
        '''
        result = self._values.get("parameters")
        assert result is not None, "Required property 'parameters' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the DB cluster parameter group.

        Constraints:

        - Must not match the name of an existing ``DBClusterParameterGroup`` .

        .. epigraph::

           This value is stored as a lowercase string.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html#cfn-docdb-dbclusterparametergroup-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to be assigned to the cluster parameter group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html#cfn-docdb-dbclusterparametergroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDBClusterParameterGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_docdb.CfnDBClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "availability_zones": "availabilityZones",
        "backup_retention_period": "backupRetentionPeriod",
        "copy_tags_to_snapshot": "copyTagsToSnapshot",
        "db_cluster_identifier": "dbClusterIdentifier",
        "db_cluster_parameter_group_name": "dbClusterParameterGroupName",
        "db_subnet_group_name": "dbSubnetGroupName",
        "deletion_protection": "deletionProtection",
        "enable_cloudwatch_logs_exports": "enableCloudwatchLogsExports",
        "engine_version": "engineVersion",
        "kms_key_id": "kmsKeyId",
        "master_username": "masterUsername",
        "master_user_password": "masterUserPassword",
        "port": "port",
        "preferred_backup_window": "preferredBackupWindow",
        "preferred_maintenance_window": "preferredMaintenanceWindow",
        "restore_to_time": "restoreToTime",
        "restore_type": "restoreType",
        "snapshot_identifier": "snapshotIdentifier",
        "source_db_cluster_identifier": "sourceDbClusterIdentifier",
        "storage_encrypted": "storageEncrypted",
        "tags": "tags",
        "use_latest_restorable_time": "useLatestRestorableTime",
        "vpc_security_group_ids": "vpcSecurityGroupIds",
    },
)
class CfnDBClusterProps:
    def __init__(
        self,
        *,
        availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        backup_retention_period: typing.Optional[jsii.Number] = None,
        copy_tags_to_snapshot: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        db_cluster_identifier: typing.Optional[builtins.str] = None,
        db_cluster_parameter_group_name: typing.Optional[builtins.str] = None,
        db_subnet_group_name: typing.Optional[builtins.str] = None,
        deletion_protection: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        enable_cloudwatch_logs_exports: typing.Optional[typing.Sequence[builtins.str]] = None,
        engine_version: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        master_username: typing.Optional[builtins.str] = None,
        master_user_password: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        preferred_backup_window: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        restore_to_time: typing.Optional[builtins.str] = None,
        restore_type: typing.Optional[builtins.str] = None,
        snapshot_identifier: typing.Optional[builtins.str] = None,
        source_db_cluster_identifier: typing.Optional[builtins.str] = None,
        storage_encrypted: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        use_latest_restorable_time: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDBCluster``.

        :param availability_zones: A list of Amazon EC2 Availability Zones that instances in the cluster can be created in.
        :param backup_retention_period: The number of days for which automated backups are retained. You must specify a minimum value of 1. Default: 1 Constraints: - Must be a value from 1 to 35.
        :param copy_tags_to_snapshot: 
        :param db_cluster_identifier: The cluster identifier. This parameter is stored as a lowercase string. Constraints: - Must contain from 1 to 63 letters, numbers, or hyphens. - The first character must be a letter. - Cannot end with a hyphen or contain two consecutive hyphens. Example: ``my-cluster``
        :param db_cluster_parameter_group_name: The name of the cluster parameter group to associate with this cluster.
        :param db_subnet_group_name: A subnet group to associate with this cluster. Constraints: Must match the name of an existing ``DBSubnetGroup`` . Must not be default. Example: ``mySubnetgroup``
        :param deletion_protection: Protects clusters from being accidentally deleted. If enabled, the cluster cannot be deleted unless it is modified and ``DeletionProtection`` is disabled.
        :param enable_cloudwatch_logs_exports: The list of log types that need to be enabled for exporting to Amazon CloudWatch Logs. You can enable audit logs or profiler logs. For more information, see `Auditing Amazon DocumentDB Events <https://docs.aws.amazon.com/documentdb/latest/developerguide/event-auditing.html>`_ and `Profiling Amazon DocumentDB Operations <https://docs.aws.amazon.com/documentdb/latest/developerguide/profiling.html>`_ .
        :param engine_version: The version number of the database engine to use. The ``--engine-version`` will default to the latest major engine version. For production workloads, we recommend explicitly declaring this parameter with the intended major engine version.
        :param kms_key_id: The AWS KMS key identifier for an encrypted cluster. The AWS KMS key identifier is the Amazon Resource Name (ARN) for the AWS KMS encryption key. If you are creating a cluster using the same AWS account that owns the AWS KMS encryption key that is used to encrypt the new cluster, you can use the AWS KMS key alias instead of the ARN for the AWS KMS encryption key. If an encryption key is not specified in ``KmsKeyId`` : - If the ``StorageEncrypted`` parameter is ``true`` , Amazon DocumentDB uses your default encryption key. AWS KMS creates the default encryption key for your AWS account . Your AWS account has a different default encryption key for each AWS Regions .
        :param master_username: The name of the master user for the cluster. Constraints: - Must be from 1 to 63 letters or numbers. - The first character must be a letter. - Cannot be a reserved word for the chosen database engine.
        :param master_user_password: The password for the master database user. This password can contain any printable ASCII character except forward slash (/), double quote ("), or the "at" symbol (@). Constraints: Must contain from 8 to 100 characters.
        :param port: Specifies the port that the database engine is listening on.
        :param preferred_backup_window: The daily time range during which automated backups are created if automated backups are enabled using the ``BackupRetentionPeriod`` parameter. The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region . Constraints: - Must be in the format ``hh24:mi-hh24:mi`` . - Must be in Universal Coordinated Time (UTC). - Must not conflict with the preferred maintenance window. - Must be at least 30 minutes.
        :param preferred_maintenance_window: The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC). Format: ``ddd:hh24:mi-ddd:hh24:mi`` The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region , occurring on a random day of the week. Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun Constraints: Minimum 30-minute window.
        :param restore_to_time: 
        :param restore_type: 
        :param snapshot_identifier: The identifier for the snapshot or cluster snapshot to restore from. You can use either the name or the Amazon Resource Name (ARN) to specify a cluster snapshot. However, you can use only the ARN to specify a snapshot. Constraints: - Must match the identifier of an existing snapshot.
        :param source_db_cluster_identifier: 
        :param storage_encrypted: Specifies whether the cluster is encrypted.
        :param tags: The tags to be assigned to the cluster.
        :param use_latest_restorable_time: 
        :param vpc_security_group_ids: A list of EC2 VPC security groups to associate with this cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_docdb as docdb
            
            cfn_dBCluster_props = docdb.CfnDBClusterProps(
                availability_zones=["availabilityZones"],
                backup_retention_period=123,
                copy_tags_to_snapshot=False,
                db_cluster_identifier="dbClusterIdentifier",
                db_cluster_parameter_group_name="dbClusterParameterGroupName",
                db_subnet_group_name="dbSubnetGroupName",
                deletion_protection=False,
                enable_cloudwatch_logs_exports=["enableCloudwatchLogsExports"],
                engine_version="engineVersion",
                kms_key_id="kmsKeyId",
                master_username="masterUsername",
                master_user_password="masterUserPassword",
                port=123,
                preferred_backup_window="preferredBackupWindow",
                preferred_maintenance_window="preferredMaintenanceWindow",
                restore_to_time="restoreToTime",
                restore_type="restoreType",
                snapshot_identifier="snapshotIdentifier",
                source_db_cluster_identifier="sourceDbClusterIdentifier",
                storage_encrypted=False,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                use_latest_restorable_time=False,
                vpc_security_group_ids=["vpcSecurityGroupIds"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e1a4213f95bc5df31b056bdc5858ecdc49954b349d7a647b8775edf506b3937)
            check_type(argname="argument availability_zones", value=availability_zones, expected_type=type_hints["availability_zones"])
            check_type(argname="argument backup_retention_period", value=backup_retention_period, expected_type=type_hints["backup_retention_period"])
            check_type(argname="argument copy_tags_to_snapshot", value=copy_tags_to_snapshot, expected_type=type_hints["copy_tags_to_snapshot"])
            check_type(argname="argument db_cluster_identifier", value=db_cluster_identifier, expected_type=type_hints["db_cluster_identifier"])
            check_type(argname="argument db_cluster_parameter_group_name", value=db_cluster_parameter_group_name, expected_type=type_hints["db_cluster_parameter_group_name"])
            check_type(argname="argument db_subnet_group_name", value=db_subnet_group_name, expected_type=type_hints["db_subnet_group_name"])
            check_type(argname="argument deletion_protection", value=deletion_protection, expected_type=type_hints["deletion_protection"])
            check_type(argname="argument enable_cloudwatch_logs_exports", value=enable_cloudwatch_logs_exports, expected_type=type_hints["enable_cloudwatch_logs_exports"])
            check_type(argname="argument engine_version", value=engine_version, expected_type=type_hints["engine_version"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument master_username", value=master_username, expected_type=type_hints["master_username"])
            check_type(argname="argument master_user_password", value=master_user_password, expected_type=type_hints["master_user_password"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument preferred_backup_window", value=preferred_backup_window, expected_type=type_hints["preferred_backup_window"])
            check_type(argname="argument preferred_maintenance_window", value=preferred_maintenance_window, expected_type=type_hints["preferred_maintenance_window"])
            check_type(argname="argument restore_to_time", value=restore_to_time, expected_type=type_hints["restore_to_time"])
            check_type(argname="argument restore_type", value=restore_type, expected_type=type_hints["restore_type"])
            check_type(argname="argument snapshot_identifier", value=snapshot_identifier, expected_type=type_hints["snapshot_identifier"])
            check_type(argname="argument source_db_cluster_identifier", value=source_db_cluster_identifier, expected_type=type_hints["source_db_cluster_identifier"])
            check_type(argname="argument storage_encrypted", value=storage_encrypted, expected_type=type_hints["storage_encrypted"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument use_latest_restorable_time", value=use_latest_restorable_time, expected_type=type_hints["use_latest_restorable_time"])
            check_type(argname="argument vpc_security_group_ids", value=vpc_security_group_ids, expected_type=type_hints["vpc_security_group_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if availability_zones is not None:
            self._values["availability_zones"] = availability_zones
        if backup_retention_period is not None:
            self._values["backup_retention_period"] = backup_retention_period
        if copy_tags_to_snapshot is not None:
            self._values["copy_tags_to_snapshot"] = copy_tags_to_snapshot
        if db_cluster_identifier is not None:
            self._values["db_cluster_identifier"] = db_cluster_identifier
        if db_cluster_parameter_group_name is not None:
            self._values["db_cluster_parameter_group_name"] = db_cluster_parameter_group_name
        if db_subnet_group_name is not None:
            self._values["db_subnet_group_name"] = db_subnet_group_name
        if deletion_protection is not None:
            self._values["deletion_protection"] = deletion_protection
        if enable_cloudwatch_logs_exports is not None:
            self._values["enable_cloudwatch_logs_exports"] = enable_cloudwatch_logs_exports
        if engine_version is not None:
            self._values["engine_version"] = engine_version
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if master_username is not None:
            self._values["master_username"] = master_username
        if master_user_password is not None:
            self._values["master_user_password"] = master_user_password
        if port is not None:
            self._values["port"] = port
        if preferred_backup_window is not None:
            self._values["preferred_backup_window"] = preferred_backup_window
        if preferred_maintenance_window is not None:
            self._values["preferred_maintenance_window"] = preferred_maintenance_window
        if restore_to_time is not None:
            self._values["restore_to_time"] = restore_to_time
        if restore_type is not None:
            self._values["restore_type"] = restore_type
        if snapshot_identifier is not None:
            self._values["snapshot_identifier"] = snapshot_identifier
        if source_db_cluster_identifier is not None:
            self._values["source_db_cluster_identifier"] = source_db_cluster_identifier
        if storage_encrypted is not None:
            self._values["storage_encrypted"] = storage_encrypted
        if tags is not None:
            self._values["tags"] = tags
        if use_latest_restorable_time is not None:
            self._values["use_latest_restorable_time"] = use_latest_restorable_time
        if vpc_security_group_ids is not None:
            self._values["vpc_security_group_ids"] = vpc_security_group_ids

    @builtins.property
    def availability_zones(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of Amazon EC2 Availability Zones that instances in the cluster can be created in.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-availabilityzones
        '''
        result = self._values.get("availability_zones")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def backup_retention_period(self) -> typing.Optional[jsii.Number]:
        '''The number of days for which automated backups are retained. You must specify a minimum value of 1.

        Default: 1

        Constraints:

        - Must be a value from 1 to 35.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-backupretentionperiod
        '''
        result = self._values.get("backup_retention_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def copy_tags_to_snapshot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-copytagstosnapshot
        '''
        result = self._values.get("copy_tags_to_snapshot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def db_cluster_identifier(self) -> typing.Optional[builtins.str]:
        '''The cluster identifier. This parameter is stored as a lowercase string.

        Constraints:

        - Must contain from 1 to 63 letters, numbers, or hyphens.
        - The first character must be a letter.
        - Cannot end with a hyphen or contain two consecutive hyphens.

        Example: ``my-cluster``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-dbclusteridentifier
        '''
        result = self._values.get("db_cluster_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def db_cluster_parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the cluster parameter group to associate with this cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-dbclusterparametergroupname
        '''
        result = self._values.get("db_cluster_parameter_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def db_subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''A subnet group to associate with this cluster.

        Constraints: Must match the name of an existing ``DBSubnetGroup`` . Must not be default.

        Example: ``mySubnetgroup``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-dbsubnetgroupname
        '''
        result = self._values.get("db_subnet_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deletion_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Protects clusters from being accidentally deleted.

        If enabled, the cluster cannot be deleted unless it is modified and ``DeletionProtection`` is disabled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-deletionprotection
        '''
        result = self._values.get("deletion_protection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def enable_cloudwatch_logs_exports(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of log types that need to be enabled for exporting to Amazon CloudWatch Logs.

        You can enable audit logs or profiler logs. For more information, see `Auditing Amazon DocumentDB Events <https://docs.aws.amazon.com/documentdb/latest/developerguide/event-auditing.html>`_ and `Profiling Amazon DocumentDB Operations <https://docs.aws.amazon.com/documentdb/latest/developerguide/profiling.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-enablecloudwatchlogsexports
        '''
        result = self._values.get("enable_cloudwatch_logs_exports")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''The version number of the database engine to use.

        The ``--engine-version`` will default to the latest major engine version. For production workloads, we recommend explicitly declaring this parameter with the intended major engine version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-engineversion
        '''
        result = self._values.get("engine_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The AWS KMS key identifier for an encrypted cluster.

        The AWS KMS key identifier is the Amazon Resource Name (ARN) for the AWS KMS encryption key. If you are creating a cluster using the same AWS account that owns the AWS KMS encryption key that is used to encrypt the new cluster, you can use the AWS KMS key alias instead of the ARN for the AWS KMS encryption key.

        If an encryption key is not specified in ``KmsKeyId`` :

        - If the ``StorageEncrypted`` parameter is ``true`` , Amazon DocumentDB uses your default encryption key.

        AWS KMS creates the default encryption key for your AWS account . Your AWS account has a different default encryption key for each AWS Regions .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def master_username(self) -> typing.Optional[builtins.str]:
        '''The name of the master user for the cluster.

        Constraints:

        - Must be from 1 to 63 letters or numbers.
        - The first character must be a letter.
        - Cannot be a reserved word for the chosen database engine.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-masterusername
        '''
        result = self._values.get("master_username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def master_user_password(self) -> typing.Optional[builtins.str]:
        '''The password for the master database user.

        This password can contain any printable ASCII character except forward slash (/), double quote ("), or the "at" symbol (@).

        Constraints: Must contain from 8 to 100 characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-masteruserpassword
        '''
        result = self._values.get("master_user_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Specifies the port that the database engine is listening on.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def preferred_backup_window(self) -> typing.Optional[builtins.str]:
        '''The daily time range during which automated backups are created if automated backups are enabled using the ``BackupRetentionPeriod`` parameter.

        The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region .

        Constraints:

        - Must be in the format ``hh24:mi-hh24:mi`` .
        - Must be in Universal Coordinated Time (UTC).
        - Must not conflict with the preferred maintenance window.
        - Must be at least 30 minutes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-preferredbackupwindow
        '''
        result = self._values.get("preferred_backup_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

        Format: ``ddd:hh24:mi-ddd:hh24:mi``

        The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region , occurring on a random day of the week.

        Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun

        Constraints: Minimum 30-minute window.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-preferredmaintenancewindow
        '''
        result = self._values.get("preferred_maintenance_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def restore_to_time(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-restoretotime
        '''
        result = self._values.get("restore_to_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def restore_type(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-restoretype
        '''
        result = self._values.get("restore_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snapshot_identifier(self) -> typing.Optional[builtins.str]:
        '''The identifier for the snapshot or cluster snapshot to restore from.

        You can use either the name or the Amazon Resource Name (ARN) to specify a cluster snapshot. However, you can use only the ARN to specify a snapshot.

        Constraints:

        - Must match the identifier of an existing snapshot.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-snapshotidentifier
        '''
        result = self._values.get("snapshot_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_db_cluster_identifier(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-sourcedbclusteridentifier
        '''
        result = self._values.get("source_db_cluster_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the cluster is encrypted.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-storageencrypted
        '''
        result = self._values.get("storage_encrypted")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to be assigned to the cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def use_latest_restorable_time(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-uselatestrestorabletime
        '''
        result = self._values.get("use_latest_restorable_time")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def vpc_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of EC2 VPC security groups to associate with this cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html#cfn-docdb-dbcluster-vpcsecuritygroupids
        '''
        result = self._values.get("vpc_security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDBClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnDBInstance(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_docdb.CfnDBInstance",
):
    '''The ``AWS::DocDB::DBInstance`` Amazon DocumentDB (with MongoDB compatibility) resource describes a DBInstance.

    For more information, see `DBInstance <https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DBInstance.html>`_ in the *Amazon DocumentDB Developer Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_docdb as docdb
        
        cfn_dBInstance = docdb.CfnDBInstance(self, "MyCfnDBInstance",
            db_cluster_identifier="dbClusterIdentifier",
            db_instance_class="dbInstanceClass",
        
            # the properties below are optional
            auto_minor_version_upgrade=False,
            availability_zone="availabilityZone",
            db_instance_identifier="dbInstanceIdentifier",
            enable_performance_insights=False,
            preferred_maintenance_window="preferredMaintenanceWindow",
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
        db_cluster_identifier: builtins.str,
        db_instance_class: builtins.str,
        auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        db_instance_identifier: typing.Optional[builtins.str] = None,
        enable_performance_insights: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param db_cluster_identifier: The identifier of the cluster that the instance will belong to.
        :param db_instance_class: The compute and memory capacity of the instance; for example, ``db.m4.large`` . If you change the class of an instance there can be some interruption in the cluster's service.
        :param auto_minor_version_upgrade: This parameter does not apply to Amazon DocumentDB. Amazon DocumentDB does not perform minor version upgrades regardless of the value set. Default: ``false``
        :param availability_zone: The Amazon EC2 Availability Zone that the instance is created in. Default: A random, system-chosen Availability Zone in the endpoint's AWS Region . Example: ``us-east-1d``
        :param db_instance_identifier: The instance identifier. This parameter is stored as a lowercase string. Constraints: - Must contain from 1 to 63 letters, numbers, or hyphens. - The first character must be a letter. - Cannot end with a hyphen or contain two consecutive hyphens. Example: ``mydbinstance``
        :param enable_performance_insights: 
        :param preferred_maintenance_window: The time range each week during which system maintenance can occur, in Universal Coordinated Time (UTC). Format: ``ddd:hh24:mi-ddd:hh24:mi`` The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region , occurring on a random day of the week. Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun Constraints: Minimum 30-minute window.
        :param tags: The tags to be assigned to the instance. You can assign up to 10 tags to an instance.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04a2ef738116d21f3bef48c2f9d0cccb18afe06fe39e0db6ce75d1bdded1b035)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDBInstanceProps(
            db_cluster_identifier=db_cluster_identifier,
            db_instance_class=db_instance_class,
            auto_minor_version_upgrade=auto_minor_version_upgrade,
            availability_zone=availability_zone,
            db_instance_identifier=db_instance_identifier,
            enable_performance_insights=enable_performance_insights,
            preferred_maintenance_window=preferred_maintenance_window,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8aa4ecf8be7edba47bf14689b009e670ad96cd741eff0a8cc1e1339f0d0c5e9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d07607ec8a7fcfd27494096e32588c2dca376fc583b6928247cc741a848498c0)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrEndpoint")
    def attr_endpoint(self) -> builtins.str:
        '''The connection endpoint for the instance.

        For example: ``sample-cluster.cluster-abcdefghijkl.us-east-1.docdb.amazonaws.com`` .

        :cloudformationAttribute: Endpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrPort")
    def attr_port(self) -> builtins.str:
        '''The port number on which the database accepts connections, such as ``27017`` .

        :cloudformationAttribute: Port
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPort"))

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
    @jsii.member(jsii_name="dbClusterIdentifier")
    def db_cluster_identifier(self) -> builtins.str:
        '''The identifier of the cluster that the instance will belong to.'''
        return typing.cast(builtins.str, jsii.get(self, "dbClusterIdentifier"))

    @db_cluster_identifier.setter
    def db_cluster_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80b91c5185212df44fcdfd50a3fc8af7618b82ddf9b010801f03aa6406893084)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbClusterIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="dbInstanceClass")
    def db_instance_class(self) -> builtins.str:
        '''The compute and memory capacity of the instance;'''
        return typing.cast(builtins.str, jsii.get(self, "dbInstanceClass"))

    @db_instance_class.setter
    def db_instance_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__029c9f8b16eafbef2fc69d8acedeac66b64c5f54d4181c222b8ccdac9c799cf4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbInstanceClass", value)

    @builtins.property
    @jsii.member(jsii_name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''This parameter does not apply to Amazon DocumentDB.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "autoMinorVersionUpgrade"))

    @auto_minor_version_upgrade.setter
    def auto_minor_version_upgrade(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3cdf0adea06b9d8f482fb95fb33660d1499428dfa0cb77f3f07f118054cbc3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoMinorVersionUpgrade", value)

    @builtins.property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The Amazon EC2 Availability Zone that the instance is created in.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c97a8d0db9d5aeae5aae1b2716ddc77dc210b628e704c9fb560f2e5f9f354e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZone", value)

    @builtins.property
    @jsii.member(jsii_name="dbInstanceIdentifier")
    def db_instance_identifier(self) -> typing.Optional[builtins.str]:
        '''The instance identifier.

        This parameter is stored as a lowercase string.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbInstanceIdentifier"))

    @db_instance_identifier.setter
    def db_instance_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b45ff85dbf36b2c15a8a4b5e7ad1f0c9f9eb5577435cebd788a2606cbec6255)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbInstanceIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="enablePerformanceInsights")
    def enable_performance_insights(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enablePerformanceInsights"))

    @enable_performance_insights.setter
    def enable_performance_insights(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9998ef6aa09a50a2905d1d918bc4bb893f66e90b164daccd2292eab9af3d6f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enablePerformanceInsights", value)

    @builtins.property
    @jsii.member(jsii_name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''The time range each week during which system maintenance can occur, in Universal Coordinated Time (UTC).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredMaintenanceWindow"))

    @preferred_maintenance_window.setter
    def preferred_maintenance_window(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1261d32bc82ad0c231ccfd241bb82acfe898707f947c36ba29797ffe6917fbd9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredMaintenanceWindow", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to be assigned to the instance.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__112d9161916b1c4ecabe22178d1e136ce15dc818a63e39711e0c01b8a28b6e7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_docdb.CfnDBInstanceProps",
    jsii_struct_bases=[],
    name_mapping={
        "db_cluster_identifier": "dbClusterIdentifier",
        "db_instance_class": "dbInstanceClass",
        "auto_minor_version_upgrade": "autoMinorVersionUpgrade",
        "availability_zone": "availabilityZone",
        "db_instance_identifier": "dbInstanceIdentifier",
        "enable_performance_insights": "enablePerformanceInsights",
        "preferred_maintenance_window": "preferredMaintenanceWindow",
        "tags": "tags",
    },
)
class CfnDBInstanceProps:
    def __init__(
        self,
        *,
        db_cluster_identifier: builtins.str,
        db_instance_class: builtins.str,
        auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        db_instance_identifier: typing.Optional[builtins.str] = None,
        enable_performance_insights: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDBInstance``.

        :param db_cluster_identifier: The identifier of the cluster that the instance will belong to.
        :param db_instance_class: The compute and memory capacity of the instance; for example, ``db.m4.large`` . If you change the class of an instance there can be some interruption in the cluster's service.
        :param auto_minor_version_upgrade: This parameter does not apply to Amazon DocumentDB. Amazon DocumentDB does not perform minor version upgrades regardless of the value set. Default: ``false``
        :param availability_zone: The Amazon EC2 Availability Zone that the instance is created in. Default: A random, system-chosen Availability Zone in the endpoint's AWS Region . Example: ``us-east-1d``
        :param db_instance_identifier: The instance identifier. This parameter is stored as a lowercase string. Constraints: - Must contain from 1 to 63 letters, numbers, or hyphens. - The first character must be a letter. - Cannot end with a hyphen or contain two consecutive hyphens. Example: ``mydbinstance``
        :param enable_performance_insights: 
        :param preferred_maintenance_window: The time range each week during which system maintenance can occur, in Universal Coordinated Time (UTC). Format: ``ddd:hh24:mi-ddd:hh24:mi`` The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region , occurring on a random day of the week. Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun Constraints: Minimum 30-minute window.
        :param tags: The tags to be assigned to the instance. You can assign up to 10 tags to an instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_docdb as docdb
            
            cfn_dBInstance_props = docdb.CfnDBInstanceProps(
                db_cluster_identifier="dbClusterIdentifier",
                db_instance_class="dbInstanceClass",
            
                # the properties below are optional
                auto_minor_version_upgrade=False,
                availability_zone="availabilityZone",
                db_instance_identifier="dbInstanceIdentifier",
                enable_performance_insights=False,
                preferred_maintenance_window="preferredMaintenanceWindow",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6b430cf173b240abd94bd08d8d0a6aca474ffd0faaf1592b8a71dbba504f407)
            check_type(argname="argument db_cluster_identifier", value=db_cluster_identifier, expected_type=type_hints["db_cluster_identifier"])
            check_type(argname="argument db_instance_class", value=db_instance_class, expected_type=type_hints["db_instance_class"])
            check_type(argname="argument auto_minor_version_upgrade", value=auto_minor_version_upgrade, expected_type=type_hints["auto_minor_version_upgrade"])
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument db_instance_identifier", value=db_instance_identifier, expected_type=type_hints["db_instance_identifier"])
            check_type(argname="argument enable_performance_insights", value=enable_performance_insights, expected_type=type_hints["enable_performance_insights"])
            check_type(argname="argument preferred_maintenance_window", value=preferred_maintenance_window, expected_type=type_hints["preferred_maintenance_window"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "db_cluster_identifier": db_cluster_identifier,
            "db_instance_class": db_instance_class,
        }
        if auto_minor_version_upgrade is not None:
            self._values["auto_minor_version_upgrade"] = auto_minor_version_upgrade
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if db_instance_identifier is not None:
            self._values["db_instance_identifier"] = db_instance_identifier
        if enable_performance_insights is not None:
            self._values["enable_performance_insights"] = enable_performance_insights
        if preferred_maintenance_window is not None:
            self._values["preferred_maintenance_window"] = preferred_maintenance_window
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def db_cluster_identifier(self) -> builtins.str:
        '''The identifier of the cluster that the instance will belong to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-dbclusteridentifier
        '''
        result = self._values.get("db_cluster_identifier")
        assert result is not None, "Required property 'db_cluster_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def db_instance_class(self) -> builtins.str:
        '''The compute and memory capacity of the instance;

        for example, ``db.m4.large`` . If you change the class of an instance there can be some interruption in the cluster's service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-dbinstanceclass
        '''
        result = self._values.get("db_instance_class")
        assert result is not None, "Required property 'db_instance_class' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_minor_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''This parameter does not apply to Amazon DocumentDB.

        Amazon DocumentDB does not perform minor version upgrades regardless of the value set.

        Default: ``false``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-autominorversionupgrade
        '''
        result = self._values.get("auto_minor_version_upgrade")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The Amazon EC2 Availability Zone that the instance is created in.

        Default: A random, system-chosen Availability Zone in the endpoint's AWS Region .

        Example: ``us-east-1d``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-availabilityzone
        '''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def db_instance_identifier(self) -> typing.Optional[builtins.str]:
        '''The instance identifier. This parameter is stored as a lowercase string.

        Constraints:

        - Must contain from 1 to 63 letters, numbers, or hyphens.
        - The first character must be a letter.
        - Cannot end with a hyphen or contain two consecutive hyphens.

        Example: ``mydbinstance``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-dbinstanceidentifier
        '''
        result = self._values.get("db_instance_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_performance_insights(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-enableperformanceinsights
        '''
        result = self._values.get("enable_performance_insights")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''The time range each week during which system maintenance can occur, in Universal Coordinated Time (UTC).

        Format: ``ddd:hh24:mi-ddd:hh24:mi``

        The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region , occurring on a random day of the week.

        Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun

        Constraints: Minimum 30-minute window.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-preferredmaintenancewindow
        '''
        result = self._values.get("preferred_maintenance_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to be assigned to the instance.

        You can assign up to 10 tags to an instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html#cfn-docdb-dbinstance-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDBInstanceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnDBSubnetGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_docdb.CfnDBSubnetGroup",
):
    '''The ``AWS::DocDB::DBSubnetGroup`` Amazon DocumentDB (with MongoDB compatibility) resource describes a DBSubnetGroup.

    subnet groups must contain at least one subnet in at least two Availability Zones in the AWS Region . For more information, see `DBSubnetGroup <https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DBSubnetGroup.html>`_ in the *Amazon DocumentDB Developer Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_docdb as docdb
        
        cfn_dBSubnet_group = docdb.CfnDBSubnetGroup(self, "MyCfnDBSubnetGroup",
            db_subnet_group_description="dbSubnetGroupDescription",
            subnet_ids=["subnetIds"],
        
            # the properties below are optional
            db_subnet_group_name="dbSubnetGroupName",
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
        db_subnet_group_description: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        db_subnet_group_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param db_subnet_group_description: The description for the subnet group.
        :param subnet_ids: The Amazon EC2 subnet IDs for the subnet group.
        :param db_subnet_group_name: The name for the subnet group. This value is stored as a lowercase string. Constraints: Must contain no more than 255 letters, numbers, periods, underscores, spaces, or hyphens. Must not be default. Example: ``mySubnetgroup``
        :param tags: The tags to be assigned to the subnet group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a66d84abf60ab10e544c9e2e5ed2d4cacef5cda174f0ec0ff1ac838ea0658570)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDBSubnetGroupProps(
            db_subnet_group_description=db_subnet_group_description,
            subnet_ids=subnet_ids,
            db_subnet_group_name=db_subnet_group_name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__beed62a49f888c354df00668e95461321a595ecfb5f76ff1aaad757929b53ab8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a609b5a19927a1afc763cd7ea9c1e7c02e8337dedde50cdeb7a70895fd163d02)
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
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="dbSubnetGroupDescription")
    def db_subnet_group_description(self) -> builtins.str:
        '''The description for the subnet group.'''
        return typing.cast(builtins.str, jsii.get(self, "dbSubnetGroupDescription"))

    @db_subnet_group_description.setter
    def db_subnet_group_description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__850c5dced7314d3602ee9d080b8694a65dc2f4ffef020d657e4fa4fc2bf55025)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbSubnetGroupDescription", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''The Amazon EC2 subnet IDs for the subnet group.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75553da48e99dee7463a4e6973f58dfe6c143be1e0a737b8d27cab2738646257)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="dbSubnetGroupName")
    def db_subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''The name for the subnet group.

        This value is stored as a lowercase string.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbSubnetGroupName"))

    @db_subnet_group_name.setter
    def db_subnet_group_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a461937c4bb0e819298839e96415d65e9462c00459cccb23d6147d4118f1cb74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbSubnetGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to be assigned to the subnet group.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2aa03e7aefbfc736e2e8595ebfa58a0fc955af7dd797db1d97f4d1a21cd9b635)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_docdb.CfnDBSubnetGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "db_subnet_group_description": "dbSubnetGroupDescription",
        "subnet_ids": "subnetIds",
        "db_subnet_group_name": "dbSubnetGroupName",
        "tags": "tags",
    },
)
class CfnDBSubnetGroupProps:
    def __init__(
        self,
        *,
        db_subnet_group_description: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        db_subnet_group_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDBSubnetGroup``.

        :param db_subnet_group_description: The description for the subnet group.
        :param subnet_ids: The Amazon EC2 subnet IDs for the subnet group.
        :param db_subnet_group_name: The name for the subnet group. This value is stored as a lowercase string. Constraints: Must contain no more than 255 letters, numbers, periods, underscores, spaces, or hyphens. Must not be default. Example: ``mySubnetgroup``
        :param tags: The tags to be assigned to the subnet group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_docdb as docdb
            
            cfn_dBSubnet_group_props = docdb.CfnDBSubnetGroupProps(
                db_subnet_group_description="dbSubnetGroupDescription",
                subnet_ids=["subnetIds"],
            
                # the properties below are optional
                db_subnet_group_name="dbSubnetGroupName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a557322d49da14bfd89b62840e1cf819fbe27ee6b0c3d31a486b4494d8caa118)
            check_type(argname="argument db_subnet_group_description", value=db_subnet_group_description, expected_type=type_hints["db_subnet_group_description"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument db_subnet_group_name", value=db_subnet_group_name, expected_type=type_hints["db_subnet_group_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "db_subnet_group_description": db_subnet_group_description,
            "subnet_ids": subnet_ids,
        }
        if db_subnet_group_name is not None:
            self._values["db_subnet_group_name"] = db_subnet_group_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def db_subnet_group_description(self) -> builtins.str:
        '''The description for the subnet group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html#cfn-docdb-dbsubnetgroup-dbsubnetgroupdescription
        '''
        result = self._values.get("db_subnet_group_description")
        assert result is not None, "Required property 'db_subnet_group_description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''The Amazon EC2 subnet IDs for the subnet group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html#cfn-docdb-dbsubnetgroup-subnetids
        '''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def db_subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''The name for the subnet group. This value is stored as a lowercase string.

        Constraints: Must contain no more than 255 letters, numbers, periods, underscores, spaces, or hyphens. Must not be default.

        Example: ``mySubnetgroup``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html#cfn-docdb-dbsubnetgroup-dbsubnetgroupname
        '''
        result = self._values.get("db_subnet_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to be assigned to the subnet group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html#cfn-docdb-dbsubnetgroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDBSubnetGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_docdb.ClusterParameterGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "family": "family",
        "parameters": "parameters",
        "db_cluster_parameter_group_name": "dbClusterParameterGroupName",
        "description": "description",
    },
)
class ClusterParameterGroupProps:
    def __init__(
        self,
        *,
        family: builtins.str,
        parameters: typing.Mapping[builtins.str, builtins.str],
        db_cluster_parameter_group_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for a cluster parameter group.

        :param family: Database family of this parameter group.
        :param parameters: The parameters in this parameter group.
        :param db_cluster_parameter_group_name: The name of the cluster parameter group. Default: A CDK generated name for the cluster parameter group
        :param description: Description for this parameter group. Default: a CDK generated description

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_docdb as docdb
            
            cluster_parameter_group_props = docdb.ClusterParameterGroupProps(
                family="family",
                parameters={
                    "parameters_key": "parameters"
                },
            
                # the properties below are optional
                db_cluster_parameter_group_name="dbClusterParameterGroupName",
                description="description"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__491f89cfa8a5f727c317b5eded8174371b0bb8ddb08980d3f8ad7e3c0bf535e0)
            check_type(argname="argument family", value=family, expected_type=type_hints["family"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument db_cluster_parameter_group_name", value=db_cluster_parameter_group_name, expected_type=type_hints["db_cluster_parameter_group_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "family": family,
            "parameters": parameters,
        }
        if db_cluster_parameter_group_name is not None:
            self._values["db_cluster_parameter_group_name"] = db_cluster_parameter_group_name
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def family(self) -> builtins.str:
        '''Database family of this parameter group.'''
        result = self._values.get("family")
        assert result is not None, "Required property 'family' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''The parameters in this parameter group.'''
        result = self._values.get("parameters")
        assert result is not None, "Required property 'parameters' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    @builtins.property
    def db_cluster_parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the cluster parameter group.

        :default: A CDK generated name for the cluster parameter group
        '''
        result = self._values.get("db_cluster_parameter_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description for this parameter group.

        :default: a CDK generated description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterParameterGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_docdb.DatabaseClusterAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_identifier": "clusterIdentifier",
        "cluster_endpoint_address": "clusterEndpointAddress",
        "instance_endpoint_addresses": "instanceEndpointAddresses",
        "instance_identifiers": "instanceIdentifiers",
        "port": "port",
        "reader_endpoint_address": "readerEndpointAddress",
        "security_group": "securityGroup",
    },
)
class DatabaseClusterAttributes:
    def __init__(
        self,
        *,
        cluster_identifier: builtins.str,
        cluster_endpoint_address: typing.Optional[builtins.str] = None,
        instance_endpoint_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        instance_identifiers: typing.Optional[typing.Sequence[builtins.str]] = None,
        port: typing.Optional[jsii.Number] = None,
        reader_endpoint_address: typing.Optional[builtins.str] = None,
        security_group: typing.Optional[_ISecurityGroup_acf8a799] = None,
    ) -> None:
        '''Properties that describe an existing cluster instance.

        :param cluster_identifier: Identifier for the cluster.
        :param cluster_endpoint_address: Cluster endpoint address. Default: - no cluster endpoint address
        :param instance_endpoint_addresses: Endpoint addresses of individual instances. Default: - no instance endpoint addresses
        :param instance_identifiers: Identifier for the instances. Default: - no instance identifiers
        :param port: The database port. Default: - none
        :param reader_endpoint_address: Reader endpoint address. Default: - no reader endpoint address
        :param security_group: The security group of the database cluster. Default: - no security groups

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_docdb as docdb
            from aws_cdk import aws_ec2 as ec2
            
            # security_group: ec2.SecurityGroup
            
            database_cluster_attributes = docdb.DatabaseClusterAttributes(
                cluster_identifier="clusterIdentifier",
            
                # the properties below are optional
                cluster_endpoint_address="clusterEndpointAddress",
                instance_endpoint_addresses=["instanceEndpointAddresses"],
                instance_identifiers=["instanceIdentifiers"],
                port=123,
                reader_endpoint_address="readerEndpointAddress",
                security_group=security_group
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7aaa09fc3d83b3aef333d99a0eb22e9b6c412979a1f20e5f22628ebd96268af)
            check_type(argname="argument cluster_identifier", value=cluster_identifier, expected_type=type_hints["cluster_identifier"])
            check_type(argname="argument cluster_endpoint_address", value=cluster_endpoint_address, expected_type=type_hints["cluster_endpoint_address"])
            check_type(argname="argument instance_endpoint_addresses", value=instance_endpoint_addresses, expected_type=type_hints["instance_endpoint_addresses"])
            check_type(argname="argument instance_identifiers", value=instance_identifiers, expected_type=type_hints["instance_identifiers"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument reader_endpoint_address", value=reader_endpoint_address, expected_type=type_hints["reader_endpoint_address"])
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_identifier": cluster_identifier,
        }
        if cluster_endpoint_address is not None:
            self._values["cluster_endpoint_address"] = cluster_endpoint_address
        if instance_endpoint_addresses is not None:
            self._values["instance_endpoint_addresses"] = instance_endpoint_addresses
        if instance_identifiers is not None:
            self._values["instance_identifiers"] = instance_identifiers
        if port is not None:
            self._values["port"] = port
        if reader_endpoint_address is not None:
            self._values["reader_endpoint_address"] = reader_endpoint_address
        if security_group is not None:
            self._values["security_group"] = security_group

    @builtins.property
    def cluster_identifier(self) -> builtins.str:
        '''Identifier for the cluster.'''
        result = self._values.get("cluster_identifier")
        assert result is not None, "Required property 'cluster_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_endpoint_address(self) -> typing.Optional[builtins.str]:
        '''Cluster endpoint address.

        :default: - no cluster endpoint address
        '''
        result = self._values.get("cluster_endpoint_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_endpoint_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Endpoint addresses of individual instances.

        :default: - no instance endpoint addresses
        '''
        result = self._values.get("instance_endpoint_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def instance_identifiers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Identifier for the instances.

        :default: - no instance identifiers
        '''
        result = self._values.get("instance_identifiers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The database port.

        :default: - none
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def reader_endpoint_address(self) -> typing.Optional[builtins.str]:
        '''Reader endpoint address.

        :default: - no reader endpoint address
        '''
        result = self._values.get("reader_endpoint_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_group(self) -> typing.Optional[_ISecurityGroup_acf8a799]:
        '''The security group of the database cluster.

        :default: - no security groups
        '''
        result = self._values.get("security_group")
        return typing.cast(typing.Optional[_ISecurityGroup_acf8a799], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseClusterAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_docdb.DatabaseClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "master_user": "masterUser",
        "vpc": "vpc",
        "backup": "backup",
        "cloud_watch_logs_retention": "cloudWatchLogsRetention",
        "cloud_watch_logs_retention_role": "cloudWatchLogsRetentionRole",
        "db_cluster_name": "dbClusterName",
        "deletion_protection": "deletionProtection",
        "enable_performance_insights": "enablePerformanceInsights",
        "engine_version": "engineVersion",
        "export_audit_logs_to_cloud_watch": "exportAuditLogsToCloudWatch",
        "export_profiler_logs_to_cloud_watch": "exportProfilerLogsToCloudWatch",
        "instance_identifier_base": "instanceIdentifierBase",
        "instances": "instances",
        "kms_key": "kmsKey",
        "parameter_group": "parameterGroup",
        "port": "port",
        "preferred_maintenance_window": "preferredMaintenanceWindow",
        "removal_policy": "removalPolicy",
        "security_group": "securityGroup",
        "storage_encrypted": "storageEncrypted",
        "vpc_subnets": "vpcSubnets",
    },
)
class DatabaseClusterProps:
    def __init__(
        self,
        *,
        instance_type: _InstanceType_f64915b9,
        master_user: typing.Union["Login", typing.Dict[builtins.str, typing.Any]],
        vpc: _IVpc_f30d5663,
        backup: typing.Optional[typing.Union[BackupProps, typing.Dict[builtins.str, typing.Any]]] = None,
        cloud_watch_logs_retention: typing.Optional[_RetentionDays_070f99f0] = None,
        cloud_watch_logs_retention_role: typing.Optional[_IRole_235f5d8e] = None,
        db_cluster_name: typing.Optional[builtins.str] = None,
        deletion_protection: typing.Optional[builtins.bool] = None,
        enable_performance_insights: typing.Optional[builtins.bool] = None,
        engine_version: typing.Optional[builtins.str] = None,
        export_audit_logs_to_cloud_watch: typing.Optional[builtins.bool] = None,
        export_profiler_logs_to_cloud_watch: typing.Optional[builtins.bool] = None,
        instance_identifier_base: typing.Optional[builtins.str] = None,
        instances: typing.Optional[jsii.Number] = None,
        kms_key: typing.Optional[_IKey_5f11635f] = None,
        parameter_group: typing.Optional["IClusterParameterGroup"] = None,
        port: typing.Optional[jsii.Number] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
        security_group: typing.Optional[_ISecurityGroup_acf8a799] = None,
        storage_encrypted: typing.Optional[builtins.bool] = None,
        vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Properties for a new database cluster.

        :param instance_type: What type of instance to start for the replicas.
        :param master_user: Username and password for the administrative user.
        :param vpc: What subnets to run the DocumentDB instances in. Must be at least 2 subnets in two different AZs.
        :param backup: Backup settings. Default: - Backup retention period for automated backups is 1 day. Backup preferred window is set to a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.
        :param cloud_watch_logs_retention: The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``Infinity``. Default: - logs never expire
        :param cloud_watch_logs_retention_role: The IAM role for the Lambda function associated with the custom resource that sets the retention policy. Default: - a new role is created.
        :param db_cluster_name: An optional identifier for the cluster. Default: - A name is automatically generated.
        :param deletion_protection: Specifies whether this cluster can be deleted. If deletionProtection is enabled, the cluster cannot be deleted unless it is modified and deletionProtection is disabled. deletionProtection protects clusters from being accidentally deleted. Default: - false
        :param enable_performance_insights: A value that indicates whether to enable Performance Insights for the instances in the DB Cluster. Default: - false
        :param engine_version: What version of the database to start. Default: - The default engine version.
        :param export_audit_logs_to_cloud_watch: Whether the audit logs should be exported to CloudWatch. Note that you also have to configure the audit log export in the Cluster's Parameter Group. Default: false
        :param export_profiler_logs_to_cloud_watch: Whether the profiler logs should be exported to CloudWatch. Note that you also have to configure the profiler log export in the Cluster's Parameter Group. Default: false
        :param instance_identifier_base: Base identifier for instances. Every replica is named by appending the replica number to this string, 1-based. Default: - ``dbClusterName`` is used with the word "Instance" appended. If ``dbClusterName`` is not provided, the identifier is automatically generated.
        :param instances: Number of DocDB compute instances. Default: 1
        :param kms_key: The KMS key for storage encryption. Default: - default master key.
        :param parameter_group: The DB parameter group to associate with the instance. Default: no parameter group
        :param port: The port the DocumentDB cluster will listen on. Default: DatabaseCluster.DEFAULT_PORT
        :param preferred_maintenance_window: A weekly time range in which maintenance should preferably execute. Must be at least 30 minutes long. Example: 'tue:04:17-tue:04:47' Default: - 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.
        :param removal_policy: The removal policy to apply when the cluster and its instances are removed or replaced during a stack update, or when the stack is deleted. This removal policy also applies to the implicit security group created for the cluster if one is not supplied as a parameter. Default: - Retain cluster.
        :param security_group: Security group. Default: a new security group is created.
        :param storage_encrypted: Whether to enable storage encryption. Default: true
        :param vpc_subnets: Where to place the instances within the VPC. Default: private subnets

        :exampleMetadata: infused

        Example::

            # vpc: ec2.Vpc
            
            cluster = docdb.DatabaseCluster(self, "Database",
                master_user=docdb.Login(
                    username="myuser"
                ),
                instance_type=ec2.InstanceType.of(ec2.InstanceClass.MEMORY5, ec2.InstanceSize.LARGE),
                vpc_subnets=ec2.SubnetSelection(
                    subnet_type=ec2.SubnetType.PUBLIC
                ),
                vpc=vpc,
                deletion_protection=True
            )
        '''
        if isinstance(master_user, dict):
            master_user = Login(**master_user)
        if isinstance(backup, dict):
            backup = BackupProps(**backup)
        if isinstance(vpc_subnets, dict):
            vpc_subnets = _SubnetSelection_e57d76df(**vpc_subnets)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb24ec128a97ca07df15f55d4e96dda851d4300951806a7a3d7f391cc4e83218)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument master_user", value=master_user, expected_type=type_hints["master_user"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument backup", value=backup, expected_type=type_hints["backup"])
            check_type(argname="argument cloud_watch_logs_retention", value=cloud_watch_logs_retention, expected_type=type_hints["cloud_watch_logs_retention"])
            check_type(argname="argument cloud_watch_logs_retention_role", value=cloud_watch_logs_retention_role, expected_type=type_hints["cloud_watch_logs_retention_role"])
            check_type(argname="argument db_cluster_name", value=db_cluster_name, expected_type=type_hints["db_cluster_name"])
            check_type(argname="argument deletion_protection", value=deletion_protection, expected_type=type_hints["deletion_protection"])
            check_type(argname="argument enable_performance_insights", value=enable_performance_insights, expected_type=type_hints["enable_performance_insights"])
            check_type(argname="argument engine_version", value=engine_version, expected_type=type_hints["engine_version"])
            check_type(argname="argument export_audit_logs_to_cloud_watch", value=export_audit_logs_to_cloud_watch, expected_type=type_hints["export_audit_logs_to_cloud_watch"])
            check_type(argname="argument export_profiler_logs_to_cloud_watch", value=export_profiler_logs_to_cloud_watch, expected_type=type_hints["export_profiler_logs_to_cloud_watch"])
            check_type(argname="argument instance_identifier_base", value=instance_identifier_base, expected_type=type_hints["instance_identifier_base"])
            check_type(argname="argument instances", value=instances, expected_type=type_hints["instances"])
            check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
            check_type(argname="argument parameter_group", value=parameter_group, expected_type=type_hints["parameter_group"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument preferred_maintenance_window", value=preferred_maintenance_window, expected_type=type_hints["preferred_maintenance_window"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
            check_type(argname="argument storage_encrypted", value=storage_encrypted, expected_type=type_hints["storage_encrypted"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_type": instance_type,
            "master_user": master_user,
            "vpc": vpc,
        }
        if backup is not None:
            self._values["backup"] = backup
        if cloud_watch_logs_retention is not None:
            self._values["cloud_watch_logs_retention"] = cloud_watch_logs_retention
        if cloud_watch_logs_retention_role is not None:
            self._values["cloud_watch_logs_retention_role"] = cloud_watch_logs_retention_role
        if db_cluster_name is not None:
            self._values["db_cluster_name"] = db_cluster_name
        if deletion_protection is not None:
            self._values["deletion_protection"] = deletion_protection
        if enable_performance_insights is not None:
            self._values["enable_performance_insights"] = enable_performance_insights
        if engine_version is not None:
            self._values["engine_version"] = engine_version
        if export_audit_logs_to_cloud_watch is not None:
            self._values["export_audit_logs_to_cloud_watch"] = export_audit_logs_to_cloud_watch
        if export_profiler_logs_to_cloud_watch is not None:
            self._values["export_profiler_logs_to_cloud_watch"] = export_profiler_logs_to_cloud_watch
        if instance_identifier_base is not None:
            self._values["instance_identifier_base"] = instance_identifier_base
        if instances is not None:
            self._values["instances"] = instances
        if kms_key is not None:
            self._values["kms_key"] = kms_key
        if parameter_group is not None:
            self._values["parameter_group"] = parameter_group
        if port is not None:
            self._values["port"] = port
        if preferred_maintenance_window is not None:
            self._values["preferred_maintenance_window"] = preferred_maintenance_window
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if security_group is not None:
            self._values["security_group"] = security_group
        if storage_encrypted is not None:
            self._values["storage_encrypted"] = storage_encrypted
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets

    @builtins.property
    def instance_type(self) -> _InstanceType_f64915b9:
        '''What type of instance to start for the replicas.'''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast(_InstanceType_f64915b9, result)

    @builtins.property
    def master_user(self) -> "Login":
        '''Username and password for the administrative user.'''
        result = self._values.get("master_user")
        assert result is not None, "Required property 'master_user' is missing"
        return typing.cast("Login", result)

    @builtins.property
    def vpc(self) -> _IVpc_f30d5663:
        '''What subnets to run the DocumentDB instances in.

        Must be at least 2 subnets in two different AZs.
        '''
        result = self._values.get("vpc")
        assert result is not None, "Required property 'vpc' is missing"
        return typing.cast(_IVpc_f30d5663, result)

    @builtins.property
    def backup(self) -> typing.Optional[BackupProps]:
        '''Backup settings.

        :default:

        - Backup retention period for automated backups is 1 day.
        Backup preferred window is set to a 30-minute window selected at random from an
        8-hour block of time for each AWS Region, occurring on a random day of the week.

        :see: https://docs.aws.amazon.com/documentdb/latest/developerguide/backup-restore.db-cluster-snapshots.html#backup-restore.backup-window
        '''
        result = self._values.get("backup")
        return typing.cast(typing.Optional[BackupProps], result)

    @builtins.property
    def cloud_watch_logs_retention(self) -> typing.Optional[_RetentionDays_070f99f0]:
        '''The number of days log events are kept in CloudWatch Logs.

        When updating
        this property, unsetting it doesn't remove the log retention policy. To
        remove the retention policy, set the value to ``Infinity``.

        :default: - logs never expire
        '''
        result = self._values.get("cloud_watch_logs_retention")
        return typing.cast(typing.Optional[_RetentionDays_070f99f0], result)

    @builtins.property
    def cloud_watch_logs_retention_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The IAM role for the Lambda function associated with the custom resource that sets the retention policy.

        :default: - a new role is created.
        '''
        result = self._values.get("cloud_watch_logs_retention_role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def db_cluster_name(self) -> typing.Optional[builtins.str]:
        '''An optional identifier for the cluster.

        :default: - A name is automatically generated.
        '''
        result = self._values.get("db_cluster_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deletion_protection(self) -> typing.Optional[builtins.bool]:
        '''Specifies whether this cluster can be deleted.

        If deletionProtection is
        enabled, the cluster cannot be deleted unless it is modified and
        deletionProtection is disabled. deletionProtection protects clusters from
        being accidentally deleted.

        :default: - false
        '''
        result = self._values.get("deletion_protection")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_performance_insights(self) -> typing.Optional[builtins.bool]:
        '''A value that indicates whether to enable Performance Insights for the instances in the DB Cluster.

        :default: - false
        '''
        result = self._values.get("enable_performance_insights")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''What version of the database to start.

        :default: - The default engine version.
        '''
        result = self._values.get("engine_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def export_audit_logs_to_cloud_watch(self) -> typing.Optional[builtins.bool]:
        '''Whether the audit logs should be exported to CloudWatch.

        Note that you also have to configure the audit log export in the Cluster's Parameter Group.

        :default: false

        :see: https://docs.aws.amazon.com/documentdb/latest/developerguide/event-auditing.html#event-auditing-enabling-auditing
        '''
        result = self._values.get("export_audit_logs_to_cloud_watch")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def export_profiler_logs_to_cloud_watch(self) -> typing.Optional[builtins.bool]:
        '''Whether the profiler logs should be exported to CloudWatch.

        Note that you also have to configure the profiler log export in the Cluster's Parameter Group.

        :default: false

        :see: https://docs.aws.amazon.com/documentdb/latest/developerguide/profiling.html#profiling.enable-profiling
        '''
        result = self._values.get("export_profiler_logs_to_cloud_watch")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def instance_identifier_base(self) -> typing.Optional[builtins.str]:
        '''Base identifier for instances.

        Every replica is named by appending the replica number to this string, 1-based.

        :default:

        - ``dbClusterName`` is used with the word "Instance" appended. If ``dbClusterName`` is not provided, the
        identifier is automatically generated.
        '''
        result = self._values.get("instance_identifier_base")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instances(self) -> typing.Optional[jsii.Number]:
        '''Number of DocDB compute instances.

        :default: 1
        '''
        result = self._values.get("instances")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def kms_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''The KMS key for storage encryption.

        :default: - default master key.
        '''
        result = self._values.get("kms_key")
        return typing.cast(typing.Optional[_IKey_5f11635f], result)

    @builtins.property
    def parameter_group(self) -> typing.Optional["IClusterParameterGroup"]:
        '''The DB parameter group to associate with the instance.

        :default: no parameter group
        '''
        result = self._values.get("parameter_group")
        return typing.cast(typing.Optional["IClusterParameterGroup"], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The port the DocumentDB cluster will listen on.

        :default: DatabaseCluster.DEFAULT_PORT
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''A weekly time range in which maintenance should preferably execute.

        Must be at least 30 minutes long.

        Example: 'tue:04:17-tue:04:47'

        :default:

        - 30-minute window selected at random from an 8-hour block of time for
        each AWS Region, occurring on a random day of the week.

        :see: https://docs.aws.amazon.com/documentdb/latest/developerguide/db-instance-maintain.html#maintenance-window
        '''
        result = self._values.get("preferred_maintenance_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[_RemovalPolicy_9f93c814]:
        '''The removal policy to apply when the cluster and its instances are removed or replaced during a stack update, or when the stack is deleted.

        This
        removal policy also applies to the implicit security group created for the
        cluster if one is not supplied as a parameter.

        :default: - Retain cluster.
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_RemovalPolicy_9f93c814], result)

    @builtins.property
    def security_group(self) -> typing.Optional[_ISecurityGroup_acf8a799]:
        '''Security group.

        :default: a new security group is created.
        '''
        result = self._values.get("security_group")
        return typing.cast(typing.Optional[_ISecurityGroup_acf8a799], result)

    @builtins.property
    def storage_encrypted(self) -> typing.Optional[builtins.bool]:
        '''Whether to enable storage encryption.

        :default: true
        '''
        result = self._values.get("storage_encrypted")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[_SubnetSelection_e57d76df]:
        '''Where to place the instances within the VPC.

        :default: private subnets
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[_SubnetSelection_e57d76df], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_docdb.DatabaseInstanceAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "instance_endpoint_address": "instanceEndpointAddress",
        "instance_identifier": "instanceIdentifier",
        "port": "port",
    },
)
class DatabaseInstanceAttributes:
    def __init__(
        self,
        *,
        instance_endpoint_address: builtins.str,
        instance_identifier: builtins.str,
        port: jsii.Number,
    ) -> None:
        '''Properties that describe an existing instance.

        :param instance_endpoint_address: The endpoint address.
        :param instance_identifier: The instance identifier.
        :param port: The database port.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_docdb as docdb
            
            database_instance_attributes = docdb.DatabaseInstanceAttributes(
                instance_endpoint_address="instanceEndpointAddress",
                instance_identifier="instanceIdentifier",
                port=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36cfeaaeef4180fd2afc1ee16f95e19c74c9cfb8467158fc246cb7a17eb3928d)
            check_type(argname="argument instance_endpoint_address", value=instance_endpoint_address, expected_type=type_hints["instance_endpoint_address"])
            check_type(argname="argument instance_identifier", value=instance_identifier, expected_type=type_hints["instance_identifier"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_endpoint_address": instance_endpoint_address,
            "instance_identifier": instance_identifier,
            "port": port,
        }

    @builtins.property
    def instance_endpoint_address(self) -> builtins.str:
        '''The endpoint address.'''
        result = self._values.get("instance_endpoint_address")
        assert result is not None, "Required property 'instance_endpoint_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_identifier(self) -> builtins.str:
        '''The instance identifier.'''
        result = self._values.get("instance_identifier")
        assert result is not None, "Required property 'instance_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''The database port.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseInstanceAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_docdb.DatabaseInstanceProps",
    jsii_struct_bases=[],
    name_mapping={
        "cluster": "cluster",
        "instance_type": "instanceType",
        "auto_minor_version_upgrade": "autoMinorVersionUpgrade",
        "availability_zone": "availabilityZone",
        "db_instance_name": "dbInstanceName",
        "enable_performance_insights": "enablePerformanceInsights",
        "preferred_maintenance_window": "preferredMaintenanceWindow",
        "removal_policy": "removalPolicy",
    },
)
class DatabaseInstanceProps:
    def __init__(
        self,
        *,
        cluster: "IDatabaseCluster",
        instance_type: _InstanceType_f64915b9,
        auto_minor_version_upgrade: typing.Optional[builtins.bool] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        db_instance_name: typing.Optional[builtins.str] = None,
        enable_performance_insights: typing.Optional[builtins.bool] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    ) -> None:
        '''Construction properties for a DatabaseInstanceNew.

        :param cluster: The DocumentDB database cluster the instance should launch into.
        :param instance_type: The name of the compute and memory capacity classes.
        :param auto_minor_version_upgrade: Indicates that minor engine upgrades are applied automatically to the DB instance during the maintenance window. Default: true
        :param availability_zone: The name of the Availability Zone where the DB instance will be located. Default: - no preference
        :param db_instance_name: A name for the DB instance. If you specify a name, AWS CloudFormation converts it to lowercase. Default: - a CloudFormation generated name
        :param enable_performance_insights: A value that indicates whether to enable Performance Insights for the DB Instance. Default: - false
        :param preferred_maintenance_window: The weekly time range (in UTC) during which system maintenance can occur. Format: ``ddd:hh24:mi-ddd:hh24:mi`` Constraint: Minimum 30-minute window Default: - a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week. To see the time blocks available, see https://docs.aws.amazon.com/documentdb/latest/developerguide/db-instance-maintain.html#maintenance-window
        :param removal_policy: The CloudFormation policy to apply when the instance is removed from the stack or replaced during an update. Default: RemovalPolicy.Retain

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_docdb as docdb
            from aws_cdk import aws_ec2 as ec2
            
            # database_cluster: docdb.DatabaseCluster
            # instance_type: ec2.InstanceType
            
            database_instance_props = docdb.DatabaseInstanceProps(
                cluster=database_cluster,
                instance_type=instance_type,
            
                # the properties below are optional
                auto_minor_version_upgrade=False,
                availability_zone="availabilityZone",
                db_instance_name="dbInstanceName",
                enable_performance_insights=False,
                preferred_maintenance_window="preferredMaintenanceWindow",
                removal_policy=cdk.RemovalPolicy.DESTROY
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__676d69b0db2a30b5f20b867ed1d439431b0f7d419a335b2a51aaaf2086c68ada)
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument auto_minor_version_upgrade", value=auto_minor_version_upgrade, expected_type=type_hints["auto_minor_version_upgrade"])
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument db_instance_name", value=db_instance_name, expected_type=type_hints["db_instance_name"])
            check_type(argname="argument enable_performance_insights", value=enable_performance_insights, expected_type=type_hints["enable_performance_insights"])
            check_type(argname="argument preferred_maintenance_window", value=preferred_maintenance_window, expected_type=type_hints["preferred_maintenance_window"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster": cluster,
            "instance_type": instance_type,
        }
        if auto_minor_version_upgrade is not None:
            self._values["auto_minor_version_upgrade"] = auto_minor_version_upgrade
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if db_instance_name is not None:
            self._values["db_instance_name"] = db_instance_name
        if enable_performance_insights is not None:
            self._values["enable_performance_insights"] = enable_performance_insights
        if preferred_maintenance_window is not None:
            self._values["preferred_maintenance_window"] = preferred_maintenance_window
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy

    @builtins.property
    def cluster(self) -> "IDatabaseCluster":
        '''The DocumentDB database cluster the instance should launch into.'''
        result = self._values.get("cluster")
        assert result is not None, "Required property 'cluster' is missing"
        return typing.cast("IDatabaseCluster", result)

    @builtins.property
    def instance_type(self) -> _InstanceType_f64915b9:
        '''The name of the compute and memory capacity classes.'''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast(_InstanceType_f64915b9, result)

    @builtins.property
    def auto_minor_version_upgrade(self) -> typing.Optional[builtins.bool]:
        '''Indicates that minor engine upgrades are applied automatically to the DB instance during the maintenance window.

        :default: true
        '''
        result = self._values.get("auto_minor_version_upgrade")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The name of the Availability Zone where the DB instance will be located.

        :default: - no preference
        '''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def db_instance_name(self) -> typing.Optional[builtins.str]:
        '''A name for the DB instance.

        If you specify a name, AWS CloudFormation
        converts it to lowercase.

        :default: - a CloudFormation generated name
        '''
        result = self._values.get("db_instance_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_performance_insights(self) -> typing.Optional[builtins.bool]:
        '''A value that indicates whether to enable Performance Insights for the DB Instance.

        :default: - false
        '''
        result = self._values.get("enable_performance_insights")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''The weekly time range (in UTC) during which system maintenance can occur.

        Format: ``ddd:hh24:mi-ddd:hh24:mi``
        Constraint: Minimum 30-minute window

        :default:

        - a 30-minute window selected at random from an 8-hour block of
        time for each AWS Region, occurring on a random day of the week. To see
        the time blocks available, see https://docs.aws.amazon.com/documentdb/latest/developerguide/db-instance-maintain.html#maintenance-window
        '''
        result = self._values.get("preferred_maintenance_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[_RemovalPolicy_9f93c814]:
        '''The CloudFormation policy to apply when the instance is removed from the stack or replaced during an update.

        :default: RemovalPolicy.Retain
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_RemovalPolicy_9f93c814], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseInstanceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseSecret(
    _Secret_50778576,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_docdb.DatabaseSecret",
):
    '''A database secret.

    :resource: AWS::SecretsManager::Secret
    :exampleMetadata: infused

    Example::

        # cluster: docdb.DatabaseCluster
        
        my_user_secret = docdb.DatabaseSecret(self, "MyUserSecret",
            username="myuser",
            master_secret=cluster.secret
        )
        my_user_secret_attached = my_user_secret.attach(cluster) # Adds DB connections information in the secret
        
        cluster.add_rotation_multi_user("MyUser",  # Add rotation using the multi user scheme
            secret=my_user_secret_attached)
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        username: builtins.str,
        encryption_key: typing.Optional[_IKey_5f11635f] = None,
        exclude_characters: typing.Optional[builtins.str] = None,
        master_secret: typing.Optional[_ISecret_6e020e6a] = None,
        secret_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param username: The username.
        :param encryption_key: The KMS key to use to encrypt the secret. Default: default master key
        :param exclude_characters: Characters to not include in the generated password. Default: ""@/"
        :param master_secret: The master secret which will be used to rotate this secret. Default: - no master secret information will be included
        :param secret_name: The physical name of the secret. Default: Secretsmanager will generate a physical name for the secret
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__301107b66199648127d17d20860dbe803a3d87431e52d4f9d2abc79de870219d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DatabaseSecretProps(
            username=username,
            encryption_key=encryption_key,
            exclude_characters=exclude_characters,
            master_secret=master_secret,
            secret_name=secret_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_docdb.DatabaseSecretProps",
    jsii_struct_bases=[],
    name_mapping={
        "username": "username",
        "encryption_key": "encryptionKey",
        "exclude_characters": "excludeCharacters",
        "master_secret": "masterSecret",
        "secret_name": "secretName",
    },
)
class DatabaseSecretProps:
    def __init__(
        self,
        *,
        username: builtins.str,
        encryption_key: typing.Optional[_IKey_5f11635f] = None,
        exclude_characters: typing.Optional[builtins.str] = None,
        master_secret: typing.Optional[_ISecret_6e020e6a] = None,
        secret_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Construction properties for a DatabaseSecret.

        :param username: The username.
        :param encryption_key: The KMS key to use to encrypt the secret. Default: default master key
        :param exclude_characters: Characters to not include in the generated password. Default: ""@/"
        :param master_secret: The master secret which will be used to rotate this secret. Default: - no master secret information will be included
        :param secret_name: The physical name of the secret. Default: Secretsmanager will generate a physical name for the secret

        :exampleMetadata: infused

        Example::

            # cluster: docdb.DatabaseCluster
            
            my_user_secret = docdb.DatabaseSecret(self, "MyUserSecret",
                username="myuser",
                master_secret=cluster.secret
            )
            my_user_secret_attached = my_user_secret.attach(cluster) # Adds DB connections information in the secret
            
            cluster.add_rotation_multi_user("MyUser",  # Add rotation using the multi user scheme
                secret=my_user_secret_attached)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__343a21f1e686a5045ca07e1bbabf751aca7546abb7d6b4c6e772a1cb90dac5ee)
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument encryption_key", value=encryption_key, expected_type=type_hints["encryption_key"])
            check_type(argname="argument exclude_characters", value=exclude_characters, expected_type=type_hints["exclude_characters"])
            check_type(argname="argument master_secret", value=master_secret, expected_type=type_hints["master_secret"])
            check_type(argname="argument secret_name", value=secret_name, expected_type=type_hints["secret_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "username": username,
        }
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if exclude_characters is not None:
            self._values["exclude_characters"] = exclude_characters
        if master_secret is not None:
            self._values["master_secret"] = master_secret
        if secret_name is not None:
            self._values["secret_name"] = secret_name

    @builtins.property
    def username(self) -> builtins.str:
        '''The username.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''The KMS key to use to encrypt the secret.

        :default: default master key
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[_IKey_5f11635f], result)

    @builtins.property
    def exclude_characters(self) -> typing.Optional[builtins.str]:
        '''Characters to not include in the generated password.

        :default: ""@/"
        '''
        result = self._values.get("exclude_characters")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def master_secret(self) -> typing.Optional[_ISecret_6e020e6a]:
        '''The master secret which will be used to rotate this secret.

        :default: - no master secret information will be included
        '''
        result = self._values.get("master_secret")
        return typing.cast(typing.Optional[_ISecret_6e020e6a], result)

    @builtins.property
    def secret_name(self) -> typing.Optional[builtins.str]:
        '''The physical name of the secret.

        :default: Secretsmanager will generate a physical name for the secret
        '''
        result = self._values.get("secret_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSecretProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Endpoint(metaclass=jsii.JSIIMeta, jsii_type="aws-cdk-lib.aws_docdb.Endpoint"):
    '''Connection endpoint of a database cluster or instance.

    Consists of a combination of hostname and port.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_docdb as docdb
        
        endpoint = docdb.Endpoint("address", 123)
    '''

    def __init__(self, address: builtins.str, port: jsii.Number) -> None:
        '''Constructs an Endpoint instance.

        :param address: - The hostname or address of the endpoint.
        :param port: - The port number of the endpoint.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86090f1fcbb1fc65cf7280e237e3b30c007e6df106c58878ed05e8214070d42a)
            check_type(argname="argument address", value=address, expected_type=type_hints["address"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        jsii.create(self.__class__, self, [address, port])

    @jsii.member(jsii_name="portAsString")
    def port_as_string(self) -> builtins.str:
        '''Returns the port number as a string representation that can be used for embedding within other strings.

        This is intended to deal with CDK's token system. Numeric CDK tokens are not expanded when their string
        representation is embedded in a string. This function returns the port either as an unresolved string token or
        as a resolved string representation of the port value.

        :return: An (un)resolved string representation of the endpoint's port number
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "portAsString", []))

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        '''The hostname of the endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        '''The port number of the endpoint.

        This can potentially be a CDK token. If you need to embed the port in a string (e.g. instance user data script),
        use ``Endpoint.portAsString``.
        '''
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @builtins.property
    @jsii.member(jsii_name="socketAddress")
    def socket_address(self) -> builtins.str:
        '''The combination of ``HOSTNAME:PORT`` for this endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "socketAddress"))


@jsii.interface(jsii_type="aws-cdk-lib.aws_docdb.IClusterParameterGroup")
class IClusterParameterGroup(_IResource_c80c4260, typing_extensions.Protocol):
    '''A parameter group.'''

    @builtins.property
    @jsii.member(jsii_name="parameterGroupName")
    def parameter_group_name(self) -> builtins.str:
        '''The name of this parameter group.'''
        ...


class _IClusterParameterGroupProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''A parameter group.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_docdb.IClusterParameterGroup"

    @builtins.property
    @jsii.member(jsii_name="parameterGroupName")
    def parameter_group_name(self) -> builtins.str:
        '''The name of this parameter group.'''
        return typing.cast(builtins.str, jsii.get(self, "parameterGroupName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IClusterParameterGroup).__jsii_proxy_class__ = lambda : _IClusterParameterGroupProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_docdb.IDatabaseCluster")
class IDatabaseCluster(
    _IResource_c80c4260,
    _IConnectable_10015a05,
    _ISecretAttachmentTarget_123e2df9,
    typing_extensions.Protocol,
):
    '''Create a clustered database with a given number of instances.'''

    @builtins.property
    @jsii.member(jsii_name="clusterEndpoint")
    def cluster_endpoint(self) -> Endpoint:
        '''The endpoint to use for read/write operations.

        :attribute: Endpoint,Port
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="clusterIdentifier")
    def cluster_identifier(self) -> builtins.str:
        '''Identifier of the cluster.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="clusterReadEndpoint")
    def cluster_read_endpoint(self) -> Endpoint:
        '''Endpoint to use for load-balanced read-only operations.

        :attribute: ReadEndpoint
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="instanceEndpoints")
    def instance_endpoints(self) -> typing.List[Endpoint]:
        '''Endpoints which address each individual replica.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="instanceIdentifiers")
    def instance_identifiers(self) -> typing.List[builtins.str]:
        '''Identifiers of the replicas.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="securityGroupId")
    def security_group_id(self) -> builtins.str:
        '''The security group for this database cluster.'''
        ...


class _IDatabaseClusterProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
    jsii.proxy_for(_IConnectable_10015a05), # type: ignore[misc]
    jsii.proxy_for(_ISecretAttachmentTarget_123e2df9), # type: ignore[misc]
):
    '''Create a clustered database with a given number of instances.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_docdb.IDatabaseCluster"

    @builtins.property
    @jsii.member(jsii_name="clusterEndpoint")
    def cluster_endpoint(self) -> Endpoint:
        '''The endpoint to use for read/write operations.

        :attribute: Endpoint,Port
        '''
        return typing.cast(Endpoint, jsii.get(self, "clusterEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdentifier")
    def cluster_identifier(self) -> builtins.str:
        '''Identifier of the cluster.'''
        return typing.cast(builtins.str, jsii.get(self, "clusterIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="clusterReadEndpoint")
    def cluster_read_endpoint(self) -> Endpoint:
        '''Endpoint to use for load-balanced read-only operations.

        :attribute: ReadEndpoint
        '''
        return typing.cast(Endpoint, jsii.get(self, "clusterReadEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="instanceEndpoints")
    def instance_endpoints(self) -> typing.List[Endpoint]:
        '''Endpoints which address each individual replica.'''
        return typing.cast(typing.List[Endpoint], jsii.get(self, "instanceEndpoints"))

    @builtins.property
    @jsii.member(jsii_name="instanceIdentifiers")
    def instance_identifiers(self) -> typing.List[builtins.str]:
        '''Identifiers of the replicas.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "instanceIdentifiers"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupId")
    def security_group_id(self) -> builtins.str:
        '''The security group for this database cluster.'''
        return typing.cast(builtins.str, jsii.get(self, "securityGroupId"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDatabaseCluster).__jsii_proxy_class__ = lambda : _IDatabaseClusterProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_docdb.IDatabaseInstance")
class IDatabaseInstance(_IResource_c80c4260, typing_extensions.Protocol):
    '''A database instance.'''

    @builtins.property
    @jsii.member(jsii_name="dbInstanceEndpointAddress")
    def db_instance_endpoint_address(self) -> builtins.str:
        '''The instance endpoint address.

        :attribute: Endpoint
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="dbInstanceEndpointPort")
    def db_instance_endpoint_port(self) -> builtins.str:
        '''The instance endpoint port.

        :attribute: Port
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''The instance arn.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="instanceEndpoint")
    def instance_endpoint(self) -> Endpoint:
        '''The instance endpoint.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="instanceIdentifier")
    def instance_identifier(self) -> builtins.str:
        '''The instance identifier.'''
        ...


class _IDatabaseInstanceProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''A database instance.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_docdb.IDatabaseInstance"

    @builtins.property
    @jsii.member(jsii_name="dbInstanceEndpointAddress")
    def db_instance_endpoint_address(self) -> builtins.str:
        '''The instance endpoint address.

        :attribute: Endpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "dbInstanceEndpointAddress"))

    @builtins.property
    @jsii.member(jsii_name="dbInstanceEndpointPort")
    def db_instance_endpoint_port(self) -> builtins.str:
        '''The instance endpoint port.

        :attribute: Port
        '''
        return typing.cast(builtins.str, jsii.get(self, "dbInstanceEndpointPort"))

    @builtins.property
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''The instance arn.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @builtins.property
    @jsii.member(jsii_name="instanceEndpoint")
    def instance_endpoint(self) -> Endpoint:
        '''The instance endpoint.'''
        return typing.cast(Endpoint, jsii.get(self, "instanceEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="instanceIdentifier")
    def instance_identifier(self) -> builtins.str:
        '''The instance identifier.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceIdentifier"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDatabaseInstance).__jsii_proxy_class__ = lambda : _IDatabaseInstanceProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_docdb.Login",
    jsii_struct_bases=[],
    name_mapping={
        "username": "username",
        "exclude_characters": "excludeCharacters",
        "kms_key": "kmsKey",
        "password": "password",
        "secret_name": "secretName",
    },
)
class Login:
    def __init__(
        self,
        *,
        username: builtins.str,
        exclude_characters: typing.Optional[builtins.str] = None,
        kms_key: typing.Optional[_IKey_5f11635f] = None,
        password: typing.Optional[_SecretValue_3dd0ddae] = None,
        secret_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Login credentials for a database cluster.

        :param username: Username.
        :param exclude_characters: Specifies characters to not include in generated passwords. Default: ""@/"
        :param kms_key: KMS encryption key to encrypt the generated secret. Default: default master key
        :param password: Password. Do not put passwords in your CDK code directly. Default: a Secrets Manager generated password
        :param secret_name: The physical name of the secret, that will be generated. Default: Secretsmanager will generate a physical name for the secret

        :exampleMetadata: infused

        Example::

            # vpc: ec2.Vpc
            
            cluster = docdb.DatabaseCluster(self, "Database",
                master_user=docdb.Login(
                    username="myuser"
                ),
                instance_type=ec2.InstanceType.of(ec2.InstanceClass.MEMORY5, ec2.InstanceSize.LARGE),
                vpc_subnets=ec2.SubnetSelection(
                    subnet_type=ec2.SubnetType.PUBLIC
                ),
                vpc=vpc,
                deletion_protection=True
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dad38367cfec515cace70ff9a772ed28e36ab2501b59860e254c77fa2f51a005)
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument exclude_characters", value=exclude_characters, expected_type=type_hints["exclude_characters"])
            check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument secret_name", value=secret_name, expected_type=type_hints["secret_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "username": username,
        }
        if exclude_characters is not None:
            self._values["exclude_characters"] = exclude_characters
        if kms_key is not None:
            self._values["kms_key"] = kms_key
        if password is not None:
            self._values["password"] = password
        if secret_name is not None:
            self._values["secret_name"] = secret_name

    @builtins.property
    def username(self) -> builtins.str:
        '''Username.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def exclude_characters(self) -> typing.Optional[builtins.str]:
        '''Specifies characters to not include in generated passwords.

        :default: ""@/"
        '''
        result = self._values.get("exclude_characters")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''KMS encryption key to encrypt the generated secret.

        :default: default master key
        '''
        result = self._values.get("kms_key")
        return typing.cast(typing.Optional[_IKey_5f11635f], result)

    @builtins.property
    def password(self) -> typing.Optional[_SecretValue_3dd0ddae]:
        '''Password.

        Do not put passwords in your CDK code directly.

        :default: a Secrets Manager generated password
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[_SecretValue_3dd0ddae], result)

    @builtins.property
    def secret_name(self) -> typing.Optional[builtins.str]:
        '''The physical name of the secret, that will be generated.

        :default: Secretsmanager will generate a physical name for the secret
        '''
        result = self._values.get("secret_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Login(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_docdb.RotationMultiUserOptions",
    jsii_struct_bases=[],
    name_mapping={"secret": "secret", "automatically_after": "automaticallyAfter"},
)
class RotationMultiUserOptions:
    def __init__(
        self,
        *,
        secret: _ISecret_6e020e6a,
        automatically_after: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''Options to add the multi user rotation.

        :param secret: The secret to rotate. It must be a JSON string with the following format:: { "engine": <required: must be set to 'mongo'>, "host": <required: instance host name>, "username": <required: username>, "password": <required: password>, "dbname": <optional: database name>, "port": <optional: if not specified, default port 27017 will be used>, "masterarn": <required: the arn of the master secret which will be used to create users/change passwords> "ssl": <optional: if not specified, defaults to false. This must be true if being used for DocumentDB rotations where the cluster has TLS enabled> }
        :param automatically_after: Specifies the number of days after the previous rotation before Secrets Manager triggers the next automatic rotation. Default: Duration.days(30)

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_secretsmanager as secretsmanager
            
            # my_imported_secret: secretsmanager.Secret
            # cluster: docdb.DatabaseCluster
            
            
            cluster.add_rotation_multi_user("MyUser",
                secret=my_imported_secret
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__222dd3344c65bc26a3a94843e3f6ff30239e319d6a229dd3bdf41ceb343c10f8)
            check_type(argname="argument secret", value=secret, expected_type=type_hints["secret"])
            check_type(argname="argument automatically_after", value=automatically_after, expected_type=type_hints["automatically_after"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "secret": secret,
        }
        if automatically_after is not None:
            self._values["automatically_after"] = automatically_after

    @builtins.property
    def secret(self) -> _ISecret_6e020e6a:
        '''The secret to rotate.

        It must be a JSON string with the following format::

           {
             "engine": <required: must be set to 'mongo'>,
             "host": <required: instance host name>,
             "username": <required: username>,
             "password": <required: password>,
             "dbname": <optional: database name>,
             "port": <optional: if not specified, default port 27017 will be used>,
             "masterarn": <required: the arn of the master secret which will be used to create users/change passwords>
             "ssl": <optional: if not specified, defaults to false. This must be true if being used for DocumentDB rotations
                    where the cluster has TLS enabled>
           }
        '''
        result = self._values.get("secret")
        assert result is not None, "Required property 'secret' is missing"
        return typing.cast(_ISecret_6e020e6a, result)

    @builtins.property
    def automatically_after(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Specifies the number of days after the previous rotation before Secrets Manager triggers the next automatic rotation.

        :default: Duration.days(30)
        '''
        result = self._values.get("automatically_after")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RotationMultiUserOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IClusterParameterGroup)
class ClusterParameterGroup(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_docdb.ClusterParameterGroup",
):
    '''A cluster parameter group.

    :resource: AWS::DocDB::DBClusterParameterGroup
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_docdb as docdb
        
        cluster_parameter_group = docdb.ClusterParameterGroup(self, "MyClusterParameterGroup",
            family="family",
            parameters={
                "parameters_key": "parameters"
            },
        
            # the properties below are optional
            db_cluster_parameter_group_name="dbClusterParameterGroupName",
            description="description"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        family: builtins.str,
        parameters: typing.Mapping[builtins.str, builtins.str],
        db_cluster_parameter_group_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param family: Database family of this parameter group.
        :param parameters: The parameters in this parameter group.
        :param db_cluster_parameter_group_name: The name of the cluster parameter group. Default: A CDK generated name for the cluster parameter group
        :param description: Description for this parameter group. Default: a CDK generated description
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5db9713ff81354905234a3c3ad455aeb345d40d5b2e301511a38a2fed7b672b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ClusterParameterGroupProps(
            family=family,
            parameters=parameters,
            db_cluster_parameter_group_name=db_cluster_parameter_group_name,
            description=description,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromParameterGroupName")
    @builtins.classmethod
    def from_parameter_group_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        parameter_group_name: builtins.str,
    ) -> IClusterParameterGroup:
        '''Imports a parameter group.

        :param scope: -
        :param id: -
        :param parameter_group_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50a6e2f2a11bdcb60e8bb7e1afe3b0c044e984785dbe4dfdd6af3fb701d27893)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument parameter_group_name", value=parameter_group_name, expected_type=type_hints["parameter_group_name"])
        return typing.cast(IClusterParameterGroup, jsii.sinvoke(cls, "fromParameterGroupName", [scope, id, parameter_group_name]))

    @builtins.property
    @jsii.member(jsii_name="parameterGroupName")
    def parameter_group_name(self) -> builtins.str:
        '''The name of the parameter group.'''
        return typing.cast(builtins.str, jsii.get(self, "parameterGroupName"))


@jsii.implements(IDatabaseCluster)
class DatabaseCluster(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_docdb.DatabaseCluster",
):
    '''Create a clustered database with a given number of instances.

    :resource: AWS::DocDB::DBCluster
    :exampleMetadata: infused

    Example::

        # vpc: ec2.Vpc
        
        cluster = docdb.DatabaseCluster(self, "Database",
            master_user=docdb.Login(
                username="myuser"
            ),
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.MEMORY5, ec2.InstanceSize.LARGE),
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            ),
            vpc=vpc,
            deletion_protection=True
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        instance_type: _InstanceType_f64915b9,
        master_user: typing.Union[Login, typing.Dict[builtins.str, typing.Any]],
        vpc: _IVpc_f30d5663,
        backup: typing.Optional[typing.Union[BackupProps, typing.Dict[builtins.str, typing.Any]]] = None,
        cloud_watch_logs_retention: typing.Optional[_RetentionDays_070f99f0] = None,
        cloud_watch_logs_retention_role: typing.Optional[_IRole_235f5d8e] = None,
        db_cluster_name: typing.Optional[builtins.str] = None,
        deletion_protection: typing.Optional[builtins.bool] = None,
        enable_performance_insights: typing.Optional[builtins.bool] = None,
        engine_version: typing.Optional[builtins.str] = None,
        export_audit_logs_to_cloud_watch: typing.Optional[builtins.bool] = None,
        export_profiler_logs_to_cloud_watch: typing.Optional[builtins.bool] = None,
        instance_identifier_base: typing.Optional[builtins.str] = None,
        instances: typing.Optional[jsii.Number] = None,
        kms_key: typing.Optional[_IKey_5f11635f] = None,
        parameter_group: typing.Optional[IClusterParameterGroup] = None,
        port: typing.Optional[jsii.Number] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
        security_group: typing.Optional[_ISecurityGroup_acf8a799] = None,
        storage_encrypted: typing.Optional[builtins.bool] = None,
        vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param instance_type: What type of instance to start for the replicas.
        :param master_user: Username and password for the administrative user.
        :param vpc: What subnets to run the DocumentDB instances in. Must be at least 2 subnets in two different AZs.
        :param backup: Backup settings. Default: - Backup retention period for automated backups is 1 day. Backup preferred window is set to a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.
        :param cloud_watch_logs_retention: The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``Infinity``. Default: - logs never expire
        :param cloud_watch_logs_retention_role: The IAM role for the Lambda function associated with the custom resource that sets the retention policy. Default: - a new role is created.
        :param db_cluster_name: An optional identifier for the cluster. Default: - A name is automatically generated.
        :param deletion_protection: Specifies whether this cluster can be deleted. If deletionProtection is enabled, the cluster cannot be deleted unless it is modified and deletionProtection is disabled. deletionProtection protects clusters from being accidentally deleted. Default: - false
        :param enable_performance_insights: A value that indicates whether to enable Performance Insights for the instances in the DB Cluster. Default: - false
        :param engine_version: What version of the database to start. Default: - The default engine version.
        :param export_audit_logs_to_cloud_watch: Whether the audit logs should be exported to CloudWatch. Note that you also have to configure the audit log export in the Cluster's Parameter Group. Default: false
        :param export_profiler_logs_to_cloud_watch: Whether the profiler logs should be exported to CloudWatch. Note that you also have to configure the profiler log export in the Cluster's Parameter Group. Default: false
        :param instance_identifier_base: Base identifier for instances. Every replica is named by appending the replica number to this string, 1-based. Default: - ``dbClusterName`` is used with the word "Instance" appended. If ``dbClusterName`` is not provided, the identifier is automatically generated.
        :param instances: Number of DocDB compute instances. Default: 1
        :param kms_key: The KMS key for storage encryption. Default: - default master key.
        :param parameter_group: The DB parameter group to associate with the instance. Default: no parameter group
        :param port: The port the DocumentDB cluster will listen on. Default: DatabaseCluster.DEFAULT_PORT
        :param preferred_maintenance_window: A weekly time range in which maintenance should preferably execute. Must be at least 30 minutes long. Example: 'tue:04:17-tue:04:47' Default: - 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.
        :param removal_policy: The removal policy to apply when the cluster and its instances are removed or replaced during a stack update, or when the stack is deleted. This removal policy also applies to the implicit security group created for the cluster if one is not supplied as a parameter. Default: - Retain cluster.
        :param security_group: Security group. Default: a new security group is created.
        :param storage_encrypted: Whether to enable storage encryption. Default: true
        :param vpc_subnets: Where to place the instances within the VPC. Default: private subnets
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fef762ebf4d69195051e79f76d91c6d9e93e2a84a6c1e71f7b4a0b8ca6572a2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DatabaseClusterProps(
            instance_type=instance_type,
            master_user=master_user,
            vpc=vpc,
            backup=backup,
            cloud_watch_logs_retention=cloud_watch_logs_retention,
            cloud_watch_logs_retention_role=cloud_watch_logs_retention_role,
            db_cluster_name=db_cluster_name,
            deletion_protection=deletion_protection,
            enable_performance_insights=enable_performance_insights,
            engine_version=engine_version,
            export_audit_logs_to_cloud_watch=export_audit_logs_to_cloud_watch,
            export_profiler_logs_to_cloud_watch=export_profiler_logs_to_cloud_watch,
            instance_identifier_base=instance_identifier_base,
            instances=instances,
            kms_key=kms_key,
            parameter_group=parameter_group,
            port=port,
            preferred_maintenance_window=preferred_maintenance_window,
            removal_policy=removal_policy,
            security_group=security_group,
            storage_encrypted=storage_encrypted,
            vpc_subnets=vpc_subnets,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromDatabaseClusterAttributes")
    @builtins.classmethod
    def from_database_cluster_attributes(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        cluster_identifier: builtins.str,
        cluster_endpoint_address: typing.Optional[builtins.str] = None,
        instance_endpoint_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        instance_identifiers: typing.Optional[typing.Sequence[builtins.str]] = None,
        port: typing.Optional[jsii.Number] = None,
        reader_endpoint_address: typing.Optional[builtins.str] = None,
        security_group: typing.Optional[_ISecurityGroup_acf8a799] = None,
    ) -> IDatabaseCluster:
        '''Import an existing DatabaseCluster from properties.

        :param scope: -
        :param id: -
        :param cluster_identifier: Identifier for the cluster.
        :param cluster_endpoint_address: Cluster endpoint address. Default: - no cluster endpoint address
        :param instance_endpoint_addresses: Endpoint addresses of individual instances. Default: - no instance endpoint addresses
        :param instance_identifiers: Identifier for the instances. Default: - no instance identifiers
        :param port: The database port. Default: - none
        :param reader_endpoint_address: Reader endpoint address. Default: - no reader endpoint address
        :param security_group: The security group of the database cluster. Default: - no security groups
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__836902d40695afe321150a992d96ccb936e8d308be6d9a9b3da7436a3d6166af)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = DatabaseClusterAttributes(
            cluster_identifier=cluster_identifier,
            cluster_endpoint_address=cluster_endpoint_address,
            instance_endpoint_addresses=instance_endpoint_addresses,
            instance_identifiers=instance_identifiers,
            port=port,
            reader_endpoint_address=reader_endpoint_address,
            security_group=security_group,
        )

        return typing.cast(IDatabaseCluster, jsii.sinvoke(cls, "fromDatabaseClusterAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="addRotationMultiUser")
    def add_rotation_multi_user(
        self,
        id: builtins.str,
        *,
        secret: _ISecret_6e020e6a,
        automatically_after: typing.Optional[_Duration_4839e8c3] = None,
    ) -> _SecretRotation_38c354d9:
        '''Adds the multi user rotation to this cluster.

        :param id: -
        :param secret: The secret to rotate. It must be a JSON string with the following format:: { "engine": <required: must be set to 'mongo'>, "host": <required: instance host name>, "username": <required: username>, "password": <required: password>, "dbname": <optional: database name>, "port": <optional: if not specified, default port 27017 will be used>, "masterarn": <required: the arn of the master secret which will be used to create users/change passwords> "ssl": <optional: if not specified, defaults to false. This must be true if being used for DocumentDB rotations where the cluster has TLS enabled> }
        :param automatically_after: Specifies the number of days after the previous rotation before Secrets Manager triggers the next automatic rotation. Default: Duration.days(30)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8104f52075e730a66a0d312a39899ef480a9a73482a6304ac3adef88ccec5438)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = RotationMultiUserOptions(
            secret=secret, automatically_after=automatically_after
        )

        return typing.cast(_SecretRotation_38c354d9, jsii.invoke(self, "addRotationMultiUser", [id, options]))

    @jsii.member(jsii_name="addRotationSingleUser")
    def add_rotation_single_user(
        self,
        automatically_after: typing.Optional[_Duration_4839e8c3] = None,
    ) -> _SecretRotation_38c354d9:
        '''Adds the single user rotation of the master password to this cluster.

        :param automatically_after: Specifies the number of days after the previous rotation before Secrets Manager triggers the next automatic rotation.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61403f83c42064e0a8ac69316b59bc9bc7e5794511d93a60726b8afbb0c70383)
            check_type(argname="argument automatically_after", value=automatically_after, expected_type=type_hints["automatically_after"])
        return typing.cast(_SecretRotation_38c354d9, jsii.invoke(self, "addRotationSingleUser", [automatically_after]))

    @jsii.member(jsii_name="addSecurityGroups")
    def add_security_groups(self, *security_groups: _ISecurityGroup_acf8a799) -> None:
        '''Adds security groups to this cluster.

        :param security_groups: The security groups to add.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad91accb5a6911246c757ed258c9b875cb1e72172f9a4324bf015514d9e43fac)
            check_type(argname="argument security_groups", value=security_groups, expected_type=typing.Tuple[type_hints["security_groups"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addSecurityGroups", [*security_groups]))

    @jsii.member(jsii_name="asSecretAttachmentTarget")
    def as_secret_attachment_target(self) -> _SecretAttachmentTargetProps_9ec7949d:
        '''Renders the secret attachment target specifications.'''
        return typing.cast(_SecretAttachmentTargetProps_9ec7949d, jsii.invoke(self, "asSecretAttachmentTarget", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DEFAULT_NUM_INSTANCES")
    def DEFAULT_NUM_INSTANCES(cls) -> jsii.Number:
        '''The default number of instances in the DocDB cluster if none are specified.'''
        return typing.cast(jsii.Number, jsii.sget(cls, "DEFAULT_NUM_INSTANCES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DEFAULT_PORT")
    def DEFAULT_PORT(cls) -> jsii.Number:
        '''The default port Document DB listens on.'''
        return typing.cast(jsii.Number, jsii.sget(cls, "DEFAULT_PORT"))

    @builtins.property
    @jsii.member(jsii_name="clusterEndpoint")
    def cluster_endpoint(self) -> Endpoint:
        '''The endpoint to use for read/write operations.'''
        return typing.cast(Endpoint, jsii.get(self, "clusterEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdentifier")
    def cluster_identifier(self) -> builtins.str:
        '''Identifier of the cluster.'''
        return typing.cast(builtins.str, jsii.get(self, "clusterIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="clusterReadEndpoint")
    def cluster_read_endpoint(self) -> Endpoint:
        '''Endpoint to use for load-balanced read-only operations.'''
        return typing.cast(Endpoint, jsii.get(self, "clusterReadEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="clusterResourceIdentifier")
    def cluster_resource_identifier(self) -> builtins.str:
        '''The resource id for the cluster;

        for example: cluster-ABCD1234EFGH5678IJKL90MNOP. The cluster ID uniquely
        identifies the cluster and is used in things like IAM authentication policies.

        :attribute: ClusterResourceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterResourceIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="connections")
    def connections(self) -> _Connections_0f31fce8:
        '''The connections object to implement IConnectable.'''
        return typing.cast(_Connections_0f31fce8, jsii.get(self, "connections"))

    @builtins.property
    @jsii.member(jsii_name="instanceEndpoints")
    def instance_endpoints(self) -> typing.List[Endpoint]:
        '''Endpoints which address each individual replica.'''
        return typing.cast(typing.List[Endpoint], jsii.get(self, "instanceEndpoints"))

    @builtins.property
    @jsii.member(jsii_name="instanceIdentifiers")
    def instance_identifiers(self) -> typing.List[builtins.str]:
        '''Identifiers of the replicas.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "instanceIdentifiers"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupId")
    def security_group_id(self) -> builtins.str:
        '''Security group identifier of this database.'''
        return typing.cast(builtins.str, jsii.get(self, "securityGroupId"))

    @builtins.property
    @jsii.member(jsii_name="secret")
    def secret(self) -> typing.Optional[_ISecret_6e020e6a]:
        '''The secret attached to this cluster.'''
        return typing.cast(typing.Optional[_ISecret_6e020e6a], jsii.get(self, "secret"))


@jsii.implements(IDatabaseInstance)
class DatabaseInstance(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_docdb.DatabaseInstance",
):
    '''A database instance.

    :resource: AWS::DocDB::DBInstance
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk as cdk
        from aws_cdk import aws_docdb as docdb
        from aws_cdk import aws_ec2 as ec2
        
        # database_cluster: docdb.DatabaseCluster
        # instance_type: ec2.InstanceType
        
        database_instance = docdb.DatabaseInstance(self, "MyDatabaseInstance",
            cluster=database_cluster,
            instance_type=instance_type,
        
            # the properties below are optional
            auto_minor_version_upgrade=False,
            availability_zone="availabilityZone",
            db_instance_name="dbInstanceName",
            enable_performance_insights=False,
            preferred_maintenance_window="preferredMaintenanceWindow",
            removal_policy=cdk.RemovalPolicy.DESTROY
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        cluster: IDatabaseCluster,
        instance_type: _InstanceType_f64915b9,
        auto_minor_version_upgrade: typing.Optional[builtins.bool] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        db_instance_name: typing.Optional[builtins.str] = None,
        enable_performance_insights: typing.Optional[builtins.bool] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param cluster: The DocumentDB database cluster the instance should launch into.
        :param instance_type: The name of the compute and memory capacity classes.
        :param auto_minor_version_upgrade: Indicates that minor engine upgrades are applied automatically to the DB instance during the maintenance window. Default: true
        :param availability_zone: The name of the Availability Zone where the DB instance will be located. Default: - no preference
        :param db_instance_name: A name for the DB instance. If you specify a name, AWS CloudFormation converts it to lowercase. Default: - a CloudFormation generated name
        :param enable_performance_insights: A value that indicates whether to enable Performance Insights for the DB Instance. Default: - false
        :param preferred_maintenance_window: The weekly time range (in UTC) during which system maintenance can occur. Format: ``ddd:hh24:mi-ddd:hh24:mi`` Constraint: Minimum 30-minute window Default: - a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week. To see the time blocks available, see https://docs.aws.amazon.com/documentdb/latest/developerguide/db-instance-maintain.html#maintenance-window
        :param removal_policy: The CloudFormation policy to apply when the instance is removed from the stack or replaced during an update. Default: RemovalPolicy.Retain
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5817f4b16546e48d296754293847a6856ad12a571f11de701f04c21523ef2195)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DatabaseInstanceProps(
            cluster=cluster,
            instance_type=instance_type,
            auto_minor_version_upgrade=auto_minor_version_upgrade,
            availability_zone=availability_zone,
            db_instance_name=db_instance_name,
            enable_performance_insights=enable_performance_insights,
            preferred_maintenance_window=preferred_maintenance_window,
            removal_policy=removal_policy,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromDatabaseInstanceAttributes")
    @builtins.classmethod
    def from_database_instance_attributes(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        instance_endpoint_address: builtins.str,
        instance_identifier: builtins.str,
        port: jsii.Number,
    ) -> IDatabaseInstance:
        '''Import an existing database instance.

        :param scope: -
        :param id: -
        :param instance_endpoint_address: The endpoint address.
        :param instance_identifier: The instance identifier.
        :param port: The database port.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5af197dfd9513994e6eb32cf7bee6ff17fef900a5adb40b20b62ef89770a338a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = DatabaseInstanceAttributes(
            instance_endpoint_address=instance_endpoint_address,
            instance_identifier=instance_identifier,
            port=port,
        )

        return typing.cast(IDatabaseInstance, jsii.sinvoke(cls, "fromDatabaseInstanceAttributes", [scope, id, attrs]))

    @builtins.property
    @jsii.member(jsii_name="cluster")
    def cluster(self) -> IDatabaseCluster:
        '''The instance's database cluster.'''
        return typing.cast(IDatabaseCluster, jsii.get(self, "cluster"))

    @builtins.property
    @jsii.member(jsii_name="dbInstanceEndpointAddress")
    def db_instance_endpoint_address(self) -> builtins.str:
        '''The instance endpoint address.

        :inheritdoc: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "dbInstanceEndpointAddress"))

    @builtins.property
    @jsii.member(jsii_name="dbInstanceEndpointPort")
    def db_instance_endpoint_port(self) -> builtins.str:
        '''The instance endpoint port.

        :inheritdoc: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "dbInstanceEndpointPort"))

    @builtins.property
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''The instance arn.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @builtins.property
    @jsii.member(jsii_name="instanceEndpoint")
    def instance_endpoint(self) -> Endpoint:
        '''The instance endpoint.

        :inheritdoc: true
        '''
        return typing.cast(Endpoint, jsii.get(self, "instanceEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="instanceIdentifier")
    def instance_identifier(self) -> builtins.str:
        '''The instance identifier.

        :inheritdoc: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceIdentifier"))


__all__ = [
    "BackupProps",
    "CfnDBCluster",
    "CfnDBClusterParameterGroup",
    "CfnDBClusterParameterGroupProps",
    "CfnDBClusterProps",
    "CfnDBInstance",
    "CfnDBInstanceProps",
    "CfnDBSubnetGroup",
    "CfnDBSubnetGroupProps",
    "ClusterParameterGroup",
    "ClusterParameterGroupProps",
    "DatabaseCluster",
    "DatabaseClusterAttributes",
    "DatabaseClusterProps",
    "DatabaseInstance",
    "DatabaseInstanceAttributes",
    "DatabaseInstanceProps",
    "DatabaseSecret",
    "DatabaseSecretProps",
    "Endpoint",
    "IClusterParameterGroup",
    "IDatabaseCluster",
    "IDatabaseInstance",
    "Login",
    "RotationMultiUserOptions",
]

publication.publish()

def _typecheckingstub__ee6fe0fa77944f4ac01bc65293ff8588d9093a5a1b3fa48a6bab1d3e79b40b09(
    *,
    retention: _Duration_4839e8c3,
    preferred_window: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7db61dc80f26049d79a38255d8a0b3abaf4b5019d7cbed64c937ec0f3e40056c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    backup_retention_period: typing.Optional[jsii.Number] = None,
    copy_tags_to_snapshot: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    db_cluster_identifier: typing.Optional[builtins.str] = None,
    db_cluster_parameter_group_name: typing.Optional[builtins.str] = None,
    db_subnet_group_name: typing.Optional[builtins.str] = None,
    deletion_protection: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    enable_cloudwatch_logs_exports: typing.Optional[typing.Sequence[builtins.str]] = None,
    engine_version: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    master_username: typing.Optional[builtins.str] = None,
    master_user_password: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    preferred_backup_window: typing.Optional[builtins.str] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    restore_to_time: typing.Optional[builtins.str] = None,
    restore_type: typing.Optional[builtins.str] = None,
    snapshot_identifier: typing.Optional[builtins.str] = None,
    source_db_cluster_identifier: typing.Optional[builtins.str] = None,
    storage_encrypted: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    use_latest_restorable_time: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f49adaa49bdc08b786dfe6f113030ff5dd0db0af1cab13c2ea50ea5487f4b802(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49d68682da6d2b0ce5ca0609607e472a09f9f77f27ba4214de01d037f2eca6c6(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4bdaf0bc7cad58ade1a34b4b85daf3a0c9caf4e9c4aa423d8c08839742b0d4d(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c664a6034ddc5d1a75cd1bae48398fc11875b13ff09951c293559b0708786b47(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9579155c60f37e7baaefd2add0496a87f54293584ec94a2a7785dc3264ebe4e(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22fbd7b0bf1256197f71b3b43f4d11d7eb59e118a93d9b0c59335aea8e7b586f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1a2f5fa89f057ba4759b48019d5a08e9de7fcb5cc68ed5ace17b6303dec5d87(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43f1e52bdd69041102d5550de099fe30eb54180c8559f2760b4c5a4cb3af9e07(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc9a3746b34c3c8e0f788ea45970b8e53d09b5b282a722fbed39cfe0b59b8f97(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b98a157c72eff100321309f96926d75d4cfd89d474c71de6df075763daff6e71(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6c3f347d46adbb72bedc7428b15c6469cfe26cf4f30488e8abd2f8f22ca84d2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03e9375b32d036932973e964a270516d21d155bd0db4369d824ccb7e7f0bdc62(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c07cdadbef8a45e2db19e8559d89c8cec47c9d2d698c3fc441a996847907dfc0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2998c76e0321a3f0bc1fe35b15ded5ba4f630cb6e5e7519736bf7455e2abe14(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a09b878a6d8b852d7eb17f26dcd8f718779776e12f67987303b1e944b3a40516(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__903ec8bf5c75ee86965cb4a2c278ea1e1e98dd095e22060664e8fa764f66256e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4322d6fabf4d2d1ef485d3e448e48faf3b9968a20e9c0b97b5a07213032c1c30(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0ee86da53d4a8f5b7ebf251632e7ba9588ee4112a830c775ece3433f227e29c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43c278d2c39f8d3f098ad2320789939b448b2958965646678cb8dd9f218f8736(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9827e5902a31fbb3009632e22e0590a6a453b8ad1f433893f790e68c5abe9b8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38eacfeb3f4a2ffe2d0fb22ed93a5652cb018e7fed96bb166e4d29176228a8d6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efd881b325008feb4534c0ce6da0a09c3cfeabe00ff36a389bdfadd597bcf73f(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__467cb576faa79b69ba7e6b18a96e5bbf103b0f9e2e68b9ca5c5b6baa2c3116c1(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__313b92cc69cbcbc01b1b3c76867167207277927cc984c7fd4f92ea48c138bbda(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__461b181007a5279b076f42e5ac0a26f146fd3b28454ba100be1045b0614f2f9b(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf702887107dc3b6d0e1c2cf7a2f922b9fa66ae4817c7d3122ceaf8e3b958132(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    description: builtins.str,
    family: builtins.str,
    parameters: typing.Any,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6a8171791541b174749473c2f0235ec8f6d2df6bcf47a0de97a3e0d0f5f4ba1(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c1f45d655c3578d1faf53be5531c206b7adce79fc6ed731b32498a9f03d92eb(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e27b4f0b3d2455b83e7b94d42a23c0c8ff2300e3ab6fba5c69d15cd9464adb7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bdc5b6562ba3c1478a5fee7c979b6215b64e8bb2b58e86475cfde6421ae1272(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__332a0d384ecea2c65bb972833483a0e813f12d76d753ec68ce55267e1a229804(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__702d9cc13fd6cd2a95ea6c1b6615540be0c5afe0086986a3555d3d957840d35b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e8ee52ae08b545bed27f58e883eee6b47f43f216f34098f0850a8bd9e024e08(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ece7bd2ef5aeaa71e7436ee669c393da120bf9e46815bde86b3caa96d817ca2(
    *,
    description: builtins.str,
    family: builtins.str,
    parameters: typing.Any,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e1a4213f95bc5df31b056bdc5858ecdc49954b349d7a647b8775edf506b3937(
    *,
    availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    backup_retention_period: typing.Optional[jsii.Number] = None,
    copy_tags_to_snapshot: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    db_cluster_identifier: typing.Optional[builtins.str] = None,
    db_cluster_parameter_group_name: typing.Optional[builtins.str] = None,
    db_subnet_group_name: typing.Optional[builtins.str] = None,
    deletion_protection: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    enable_cloudwatch_logs_exports: typing.Optional[typing.Sequence[builtins.str]] = None,
    engine_version: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    master_username: typing.Optional[builtins.str] = None,
    master_user_password: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    preferred_backup_window: typing.Optional[builtins.str] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    restore_to_time: typing.Optional[builtins.str] = None,
    restore_type: typing.Optional[builtins.str] = None,
    snapshot_identifier: typing.Optional[builtins.str] = None,
    source_db_cluster_identifier: typing.Optional[builtins.str] = None,
    storage_encrypted: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    use_latest_restorable_time: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04a2ef738116d21f3bef48c2f9d0cccb18afe06fe39e0db6ce75d1bdded1b035(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    db_cluster_identifier: builtins.str,
    db_instance_class: builtins.str,
    auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    availability_zone: typing.Optional[builtins.str] = None,
    db_instance_identifier: typing.Optional[builtins.str] = None,
    enable_performance_insights: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8aa4ecf8be7edba47bf14689b009e670ad96cd741eff0a8cc1e1339f0d0c5e9(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d07607ec8a7fcfd27494096e32588c2dca376fc583b6928247cc741a848498c0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80b91c5185212df44fcdfd50a3fc8af7618b82ddf9b010801f03aa6406893084(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__029c9f8b16eafbef2fc69d8acedeac66b64c5f54d4181c222b8ccdac9c799cf4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3cdf0adea06b9d8f482fb95fb33660d1499428dfa0cb77f3f07f118054cbc3a(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c97a8d0db9d5aeae5aae1b2716ddc77dc210b628e704c9fb560f2e5f9f354e1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b45ff85dbf36b2c15a8a4b5e7ad1f0c9f9eb5577435cebd788a2606cbec6255(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9998ef6aa09a50a2905d1d918bc4bb893f66e90b164daccd2292eab9af3d6f8(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1261d32bc82ad0c231ccfd241bb82acfe898707f947c36ba29797ffe6917fbd9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__112d9161916b1c4ecabe22178d1e136ce15dc818a63e39711e0c01b8a28b6e7a(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6b430cf173b240abd94bd08d8d0a6aca474ffd0faaf1592b8a71dbba504f407(
    *,
    db_cluster_identifier: builtins.str,
    db_instance_class: builtins.str,
    auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    availability_zone: typing.Optional[builtins.str] = None,
    db_instance_identifier: typing.Optional[builtins.str] = None,
    enable_performance_insights: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a66d84abf60ab10e544c9e2e5ed2d4cacef5cda174f0ec0ff1ac838ea0658570(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    db_subnet_group_description: builtins.str,
    subnet_ids: typing.Sequence[builtins.str],
    db_subnet_group_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__beed62a49f888c354df00668e95461321a595ecfb5f76ff1aaad757929b53ab8(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a609b5a19927a1afc763cd7ea9c1e7c02e8337dedde50cdeb7a70895fd163d02(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__850c5dced7314d3602ee9d080b8694a65dc2f4ffef020d657e4fa4fc2bf55025(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75553da48e99dee7463a4e6973f58dfe6c143be1e0a737b8d27cab2738646257(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a461937c4bb0e819298839e96415d65e9462c00459cccb23d6147d4118f1cb74(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2aa03e7aefbfc736e2e8595ebfa58a0fc955af7dd797db1d97f4d1a21cd9b635(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a557322d49da14bfd89b62840e1cf819fbe27ee6b0c3d31a486b4494d8caa118(
    *,
    db_subnet_group_description: builtins.str,
    subnet_ids: typing.Sequence[builtins.str],
    db_subnet_group_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__491f89cfa8a5f727c317b5eded8174371b0bb8ddb08980d3f8ad7e3c0bf535e0(
    *,
    family: builtins.str,
    parameters: typing.Mapping[builtins.str, builtins.str],
    db_cluster_parameter_group_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7aaa09fc3d83b3aef333d99a0eb22e9b6c412979a1f20e5f22628ebd96268af(
    *,
    cluster_identifier: builtins.str,
    cluster_endpoint_address: typing.Optional[builtins.str] = None,
    instance_endpoint_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
    instance_identifiers: typing.Optional[typing.Sequence[builtins.str]] = None,
    port: typing.Optional[jsii.Number] = None,
    reader_endpoint_address: typing.Optional[builtins.str] = None,
    security_group: typing.Optional[_ISecurityGroup_acf8a799] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb24ec128a97ca07df15f55d4e96dda851d4300951806a7a3d7f391cc4e83218(
    *,
    instance_type: _InstanceType_f64915b9,
    master_user: typing.Union[Login, typing.Dict[builtins.str, typing.Any]],
    vpc: _IVpc_f30d5663,
    backup: typing.Optional[typing.Union[BackupProps, typing.Dict[builtins.str, typing.Any]]] = None,
    cloud_watch_logs_retention: typing.Optional[_RetentionDays_070f99f0] = None,
    cloud_watch_logs_retention_role: typing.Optional[_IRole_235f5d8e] = None,
    db_cluster_name: typing.Optional[builtins.str] = None,
    deletion_protection: typing.Optional[builtins.bool] = None,
    enable_performance_insights: typing.Optional[builtins.bool] = None,
    engine_version: typing.Optional[builtins.str] = None,
    export_audit_logs_to_cloud_watch: typing.Optional[builtins.bool] = None,
    export_profiler_logs_to_cloud_watch: typing.Optional[builtins.bool] = None,
    instance_identifier_base: typing.Optional[builtins.str] = None,
    instances: typing.Optional[jsii.Number] = None,
    kms_key: typing.Optional[_IKey_5f11635f] = None,
    parameter_group: typing.Optional[IClusterParameterGroup] = None,
    port: typing.Optional[jsii.Number] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    security_group: typing.Optional[_ISecurityGroup_acf8a799] = None,
    storage_encrypted: typing.Optional[builtins.bool] = None,
    vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36cfeaaeef4180fd2afc1ee16f95e19c74c9cfb8467158fc246cb7a17eb3928d(
    *,
    instance_endpoint_address: builtins.str,
    instance_identifier: builtins.str,
    port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__676d69b0db2a30b5f20b867ed1d439431b0f7d419a335b2a51aaaf2086c68ada(
    *,
    cluster: IDatabaseCluster,
    instance_type: _InstanceType_f64915b9,
    auto_minor_version_upgrade: typing.Optional[builtins.bool] = None,
    availability_zone: typing.Optional[builtins.str] = None,
    db_instance_name: typing.Optional[builtins.str] = None,
    enable_performance_insights: typing.Optional[builtins.bool] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__301107b66199648127d17d20860dbe803a3d87431e52d4f9d2abc79de870219d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    username: builtins.str,
    encryption_key: typing.Optional[_IKey_5f11635f] = None,
    exclude_characters: typing.Optional[builtins.str] = None,
    master_secret: typing.Optional[_ISecret_6e020e6a] = None,
    secret_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__343a21f1e686a5045ca07e1bbabf751aca7546abb7d6b4c6e772a1cb90dac5ee(
    *,
    username: builtins.str,
    encryption_key: typing.Optional[_IKey_5f11635f] = None,
    exclude_characters: typing.Optional[builtins.str] = None,
    master_secret: typing.Optional[_ISecret_6e020e6a] = None,
    secret_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86090f1fcbb1fc65cf7280e237e3b30c007e6df106c58878ed05e8214070d42a(
    address: builtins.str,
    port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dad38367cfec515cace70ff9a772ed28e36ab2501b59860e254c77fa2f51a005(
    *,
    username: builtins.str,
    exclude_characters: typing.Optional[builtins.str] = None,
    kms_key: typing.Optional[_IKey_5f11635f] = None,
    password: typing.Optional[_SecretValue_3dd0ddae] = None,
    secret_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__222dd3344c65bc26a3a94843e3f6ff30239e319d6a229dd3bdf41ceb343c10f8(
    *,
    secret: _ISecret_6e020e6a,
    automatically_after: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5db9713ff81354905234a3c3ad455aeb345d40d5b2e301511a38a2fed7b672b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    family: builtins.str,
    parameters: typing.Mapping[builtins.str, builtins.str],
    db_cluster_parameter_group_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50a6e2f2a11bdcb60e8bb7e1afe3b0c044e984785dbe4dfdd6af3fb701d27893(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    parameter_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fef762ebf4d69195051e79f76d91c6d9e93e2a84a6c1e71f7b4a0b8ca6572a2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instance_type: _InstanceType_f64915b9,
    master_user: typing.Union[Login, typing.Dict[builtins.str, typing.Any]],
    vpc: _IVpc_f30d5663,
    backup: typing.Optional[typing.Union[BackupProps, typing.Dict[builtins.str, typing.Any]]] = None,
    cloud_watch_logs_retention: typing.Optional[_RetentionDays_070f99f0] = None,
    cloud_watch_logs_retention_role: typing.Optional[_IRole_235f5d8e] = None,
    db_cluster_name: typing.Optional[builtins.str] = None,
    deletion_protection: typing.Optional[builtins.bool] = None,
    enable_performance_insights: typing.Optional[builtins.bool] = None,
    engine_version: typing.Optional[builtins.str] = None,
    export_audit_logs_to_cloud_watch: typing.Optional[builtins.bool] = None,
    export_profiler_logs_to_cloud_watch: typing.Optional[builtins.bool] = None,
    instance_identifier_base: typing.Optional[builtins.str] = None,
    instances: typing.Optional[jsii.Number] = None,
    kms_key: typing.Optional[_IKey_5f11635f] = None,
    parameter_group: typing.Optional[IClusterParameterGroup] = None,
    port: typing.Optional[jsii.Number] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    security_group: typing.Optional[_ISecurityGroup_acf8a799] = None,
    storage_encrypted: typing.Optional[builtins.bool] = None,
    vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__836902d40695afe321150a992d96ccb936e8d308be6d9a9b3da7436a3d6166af(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cluster_identifier: builtins.str,
    cluster_endpoint_address: typing.Optional[builtins.str] = None,
    instance_endpoint_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
    instance_identifiers: typing.Optional[typing.Sequence[builtins.str]] = None,
    port: typing.Optional[jsii.Number] = None,
    reader_endpoint_address: typing.Optional[builtins.str] = None,
    security_group: typing.Optional[_ISecurityGroup_acf8a799] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8104f52075e730a66a0d312a39899ef480a9a73482a6304ac3adef88ccec5438(
    id: builtins.str,
    *,
    secret: _ISecret_6e020e6a,
    automatically_after: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61403f83c42064e0a8ac69316b59bc9bc7e5794511d93a60726b8afbb0c70383(
    automatically_after: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad91accb5a6911246c757ed258c9b875cb1e72172f9a4324bf015514d9e43fac(
    *security_groups: _ISecurityGroup_acf8a799,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5817f4b16546e48d296754293847a6856ad12a571f11de701f04c21523ef2195(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cluster: IDatabaseCluster,
    instance_type: _InstanceType_f64915b9,
    auto_minor_version_upgrade: typing.Optional[builtins.bool] = None,
    availability_zone: typing.Optional[builtins.str] = None,
    db_instance_name: typing.Optional[builtins.str] = None,
    enable_performance_insights: typing.Optional[builtins.bool] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5af197dfd9513994e6eb32cf7bee6ff17fef900a5adb40b20b62ef89770a338a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instance_endpoint_address: builtins.str,
    instance_identifier: builtins.str,
    port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass
