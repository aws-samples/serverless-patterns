'''
# AWS Backup Construct Library

AWS Backup is a fully managed backup service that makes it easy to centralize and automate the
backup of data across AWS services in the cloud and on premises. Using AWS Backup, you can
configure backup policies and monitor backup activity for your AWS resources in one place.

## Backup plan and selection

In AWS Backup, a *backup plan* is a policy expression that defines when and how you want to back up
your AWS resources, such as Amazon DynamoDB tables or Amazon Elastic File System (Amazon EFS) file
systems. You can assign resources to backup plans, and AWS Backup automatically backs up and retains
backups for those resources according to the backup plan. You can create multiple backup plans if you
have workloads with different backup requirements.

This module provides ready-made backup plans (similar to the console experience):

```python
# Daily, weekly and monthly with 5 year retention
plan = backup.BackupPlan.daily_weekly_monthly5_year_retention(self, "Plan")
```

Assigning resources to a plan can be done with `addSelection()`:

```python
# plan: backup.BackupPlan
# vpc: ec2.Vpc

my_table = dynamodb.Table.from_table_name(self, "Table", "myTableName")
my_database_instance = rds.DatabaseInstance(self, "DatabaseInstance",
    engine=rds.DatabaseInstanceEngine.mysql(version=rds.MysqlEngineVersion.VER_8_0_26),
    vpc=vpc
)
my_database_cluster = rds.DatabaseCluster(self, "DatabaseCluster",
    engine=rds.DatabaseClusterEngine.aurora_mysql(version=rds.AuroraMysqlEngineVersion.VER_2_08_1),
    credentials=rds.Credentials.from_generated_secret("clusteradmin"),
    instance_props=rds.InstanceProps(
        vpc=vpc
    )
)
my_serverless_cluster = rds.ServerlessCluster(self, "ServerlessCluster",
    engine=rds.DatabaseClusterEngine.AURORA_POSTGRESQL,
    parameter_group=rds.ParameterGroup.from_parameter_group_name(self, "ParameterGroup", "default.aurora-postgresql11"),
    vpc=vpc
)
my_cool_construct = Construct(self, "MyCoolConstruct")

plan.add_selection("Selection",
    resources=[
        backup.BackupResource.from_dynamo_db_table(my_table),  # A DynamoDB table
        backup.BackupResource.from_rds_database_instance(my_database_instance),  # A RDS instance
        backup.BackupResource.from_rds_database_cluster(my_database_cluster),  # A RDS database cluster
        backup.BackupResource.from_rds_serverless_cluster(my_serverless_cluster),  # An Aurora Serverless cluster
        backup.BackupResource.from_tag("stage", "prod"),  # All resources that are tagged stage=prod in the region/account
        backup.BackupResource.from_construct(my_cool_construct)
    ]
)
```

If not specified, a new IAM role with a managed policy for backup will be
created for the selection. The `BackupSelection` implements `IGrantable`.

To disable the plan from assigning the default `AWSBackupServiceRolePolicyForBackup` backup policy use the `disableDefaultBackupPolicy` property.

This is useful if you want to avoid granting unnecessary permissions to the role.

```python
# plan: backup.BackupPlan


role = iam.Role(self, "BackupRole",
    assumed_by=iam.ServicePrincipal("backup.amazonaws.com")
)
# Assign S3-specific backup policy
role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AWSBackupServiceRolePolicyForS3Backup"))

plan.add_selection("Selection",
    resources=[
        backup.BackupResource.from_tag("stage", "prod")
    ],
    role=role,
    disable_default_backup_policy=True
)
```

To add rules to a plan, use `addRule()`:

```python
# plan: backup.BackupPlan

plan.add_rule(backup.BackupPlanRule(
    completion_window=Duration.hours(2),
    start_window=Duration.hours(1),
    schedule_expression=events.Schedule.cron( # Only cron expressions are supported
        day="15",
        hour="3",
        minute="30"),
    move_to_cold_storage_after=Duration.days(30)
))
```

Continuous backup and point-in-time restores (PITR) can be configured.
Property `deleteAfter` defines the retention period for the backup. It is mandatory if PITR is enabled.
If no value is specified, the retention period is set to 35 days which is the maximum retention period supported by PITR.
Property `moveToColdStorageAfter` must not be specified because PITR does not support this option.
This example defines an AWS Backup rule with PITR and a retention period set to 14 days:

```python
# plan: backup.BackupPlan

plan.add_rule(backup.BackupPlanRule(
    enable_continuous_backup=True,
    delete_after=Duration.days(14)
))
```

Rules can also specify to copy recovery points to another Backup Vault using `copyActions`. Copied recovery points can
optionally have `moveToColdStorageAfter` and `deleteAfter` configured.

```python
# plan: backup.BackupPlan
# secondary_vault: backup.BackupVault

plan.add_rule(backup.BackupPlanRule(
    copy_actions=[backup.BackupPlanCopyActionProps(
        destination_backup_vault=secondary_vault,
        move_to_cold_storage_after=Duration.days(30),
        delete_after=Duration.days(120)
    )]
))
```

You can assign your own metadata to the resources that are associated with the rule when restored from backup using `recoveryPointTags`. Each tag is a key-value pair.

```python
# plan: backup.BackupPlan

plan.add_rule(backup.BackupPlanRule(
    recovery_point_tags={
        "key": "value"
    }
))
```

Ready-made rules are also available:

```python
# plan: backup.BackupPlan

plan.add_rule(backup.BackupPlanRule.daily())
plan.add_rule(backup.BackupPlanRule.weekly())
```

By default a new [vault](#Backup-vault) is created when creating a plan.
It is also possible to specify a vault either at the plan level or at the
rule level.

```python
my_vault = backup.BackupVault.from_backup_vault_name(self, "Vault1", "myVault")
other_vault = backup.BackupVault.from_backup_vault_name(self, "Vault2", "otherVault")

plan = backup.BackupPlan.daily35_day_retention(self, "Plan", my_vault) # Use `myVault` for all plan rules
plan.add_rule(backup.BackupPlanRule.monthly1_year(other_vault))
```

You can [backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/windows-backups.html)
VSS-enabled Windows applications running on Amazon EC2 instances by setting the `windowsVss`
parameter to `true`. If the application has VSS writer registered with Windows VSS,
then AWS Backup creates a snapshot that will be consistent for that application.

```python
plan = backup.BackupPlan(self, "Plan",
    windows_vss=True
)
```

## Backup vault

In AWS Backup, a *backup vault* is a container that you organize your backups in. You can use backup
vaults to set the AWS Key Management Service (AWS KMS) encryption key that is used to encrypt backups
in the backup vault and to control access to the backups in the backup vault. If you require different
encryption keys or access policies for different groups of backups, you can optionally create multiple
backup vaults.

```python
my_key = kms.Key.from_key_arn(self, "MyKey", "aaa")
my_topic = sns.Topic.from_topic_arn(self, "MyTopic", "bbb")

vault = backup.BackupVault(self, "Vault",
    encryption_key=my_key,  # Custom encryption key
    notification_topic=my_topic
)
```

A vault has a default `RemovalPolicy` set to `RETAIN`. Note that removing a vault
that contains recovery points will fail.

You can assign policies to backup vaults and the resources they contain. Assigning policies allows
you to do things like grant access to users to create backup plans and on-demand backups, but limit
their ability to delete recovery points after they're created.

Use the `accessPolicy` property to create a backup vault policy:

```python
vault = backup.BackupVault(self, "Vault",
    access_policy=iam.PolicyDocument(
        statements=[
            iam.PolicyStatement(
                effect=iam.Effect.DENY,
                principals=[iam.AnyPrincipal()],
                actions=["backup:DeleteRecoveryPoint"],
                resources=["*"],
                conditions={
                    "StringNotLike": {
                        "aws:userId": ["user1", "user2"
                        ]
                    }
                }
            )
        ]
    )
)
```

Alternativately statements can be added to the vault policy using `addToAccessPolicy()`.

Use the `blockRecoveryPointDeletion` property or the `blockRecoveryPointDeletion()` method to add
a statement to the vault access policy that prevents recovery point deletions in your vault:

```python
# backup_vault: backup.BackupVault
backup.BackupVault(self, "Vault",
    block_recovery_point_deletion=True
)
backup_vault.block_recovery_point_deletion()
```

By default access is not restricted.

Use the `lockConfiguration` property to enable [AWS Backup Vault Lock](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html):

```python
backup.BackupVault(self, "Vault",
    lock_configuration=backup.LockConfiguration(
        min_retention=Duration.days(30)
    )
)
```

## Importing existing backup vault

To import an existing backup vault into your CDK application, use the `BackupVault.fromBackupVaultArn` or `BackupVault.fromBackupVaultName`
static method. Here is an example of giving an IAM Role permission to start a backup job:

```python
imported_vault = backup.BackupVault.from_backup_vault_name(self, "Vault", "myVaultName")

role = iam.Role(self, "Access Role", assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"))

imported_vault.grant(role, "backup:StartBackupJob")
```
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
    Duration as _Duration_4839e8c3,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    IResource as _IResource_c80c4260,
    ITaggableV2 as _ITaggableV2_4e6798f8,
    RemovalPolicy as _RemovalPolicy_9f93c814,
    Resource as _Resource_45bc6135,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..aws_dynamodb import ITable as _ITable_504fd401
from ..aws_ec2 import IInstance as _IInstance_ab239e7c
from ..aws_efs import IFileSystem as _IFileSystem_b2d3a7cb
from ..aws_events import Schedule as _Schedule_c151d01f
from ..aws_iam import (
    Grant as _Grant_a7ae64f8,
    IGrantable as _IGrantable_71c4f5de,
    IPrincipal as _IPrincipal_539bb2fd,
    IRole as _IRole_235f5d8e,
    PolicyDocument as _PolicyDocument_3ac34393,
    PolicyStatement as _PolicyStatement_0fe33853,
)
from ..aws_kms import IKey as _IKey_5f11635f
from ..aws_rds import (
    IDatabaseCluster as _IDatabaseCluster_6554c32b,
    IDatabaseInstance as _IDatabaseInstance_e4cb03a8,
    IServerlessCluster as _IServerlessCluster_adbbb720,
)
from ..aws_sns import ITopic as _ITopic_9eca4852


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_backup.BackupPlanCopyActionProps",
    jsii_struct_bases=[],
    name_mapping={
        "destination_backup_vault": "destinationBackupVault",
        "delete_after": "deleteAfter",
        "move_to_cold_storage_after": "moveToColdStorageAfter",
    },
)
class BackupPlanCopyActionProps:
    def __init__(
        self,
        *,
        destination_backup_vault: "IBackupVault",
        delete_after: typing.Optional[_Duration_4839e8c3] = None,
        move_to_cold_storage_after: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''Properties for a BackupPlanCopyAction.

        :param destination_backup_vault: Destination Vault for recovery points to be copied into.
        :param delete_after: Specifies the duration after creation that a copied recovery point is deleted from the destination vault. Must be at least 90 days greater than ``moveToColdStorageAfter``, if specified. Default: - recovery point is never deleted
        :param move_to_cold_storage_after: Specifies the duration after creation that a copied recovery point is moved to cold storage. Default: - recovery point is never moved to cold storage

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_backup as backup
            
            # backup_vault: backup.BackupVault
            
            backup_plan_copy_action_props = backup.BackupPlanCopyActionProps(
                destination_backup_vault=backup_vault,
            
                # the properties below are optional
                delete_after=cdk.Duration.minutes(30),
                move_to_cold_storage_after=cdk.Duration.minutes(30)
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__502c247f5c1b9824033ca24f5efe3e1d20ee8980208ae5382890f6168ba12843)
            check_type(argname="argument destination_backup_vault", value=destination_backup_vault, expected_type=type_hints["destination_backup_vault"])
            check_type(argname="argument delete_after", value=delete_after, expected_type=type_hints["delete_after"])
            check_type(argname="argument move_to_cold_storage_after", value=move_to_cold_storage_after, expected_type=type_hints["move_to_cold_storage_after"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination_backup_vault": destination_backup_vault,
        }
        if delete_after is not None:
            self._values["delete_after"] = delete_after
        if move_to_cold_storage_after is not None:
            self._values["move_to_cold_storage_after"] = move_to_cold_storage_after

    @builtins.property
    def destination_backup_vault(self) -> "IBackupVault":
        '''Destination Vault for recovery points to be copied into.'''
        result = self._values.get("destination_backup_vault")
        assert result is not None, "Required property 'destination_backup_vault' is missing"
        return typing.cast("IBackupVault", result)

    @builtins.property
    def delete_after(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Specifies the duration after creation that a copied recovery point is deleted from the destination vault.

        Must be at least 90 days greater than ``moveToColdStorageAfter``, if specified.

        :default: - recovery point is never deleted
        '''
        result = self._values.get("delete_after")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def move_to_cold_storage_after(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Specifies the duration after creation that a copied recovery point is moved to cold storage.

        :default: - recovery point is never moved to cold storage
        '''
        result = self._values.get("move_to_cold_storage_after")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupPlanCopyActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_backup.BackupPlanProps",
    jsii_struct_bases=[],
    name_mapping={
        "backup_plan_name": "backupPlanName",
        "backup_plan_rules": "backupPlanRules",
        "backup_vault": "backupVault",
        "windows_vss": "windowsVss",
    },
)
class BackupPlanProps:
    def __init__(
        self,
        *,
        backup_plan_name: typing.Optional[builtins.str] = None,
        backup_plan_rules: typing.Optional[typing.Sequence["BackupPlanRule"]] = None,
        backup_vault: typing.Optional["IBackupVault"] = None,
        windows_vss: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Properties for a BackupPlan.

        :param backup_plan_name: The display name of the backup plan. Default: - A CDK generated name
        :param backup_plan_rules: Rules for the backup plan. Use ``addRule()`` to add rules after instantiation. Default: - use ``addRule()`` to add rules
        :param backup_vault: The backup vault where backups are stored. Default: - use the vault defined at the rule level. If not defined a new common vault for the plan will be created
        :param windows_vss: Enable Windows VSS backup. Default: false

        :exampleMetadata: infused

        Example::

            plan = backup.BackupPlan(self, "Plan",
                windows_vss=True
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c977b2da08bc5e51abde064245ef25c86ebdc30dd86fbb4658318249248eafb)
            check_type(argname="argument backup_plan_name", value=backup_plan_name, expected_type=type_hints["backup_plan_name"])
            check_type(argname="argument backup_plan_rules", value=backup_plan_rules, expected_type=type_hints["backup_plan_rules"])
            check_type(argname="argument backup_vault", value=backup_vault, expected_type=type_hints["backup_vault"])
            check_type(argname="argument windows_vss", value=windows_vss, expected_type=type_hints["windows_vss"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if backup_plan_name is not None:
            self._values["backup_plan_name"] = backup_plan_name
        if backup_plan_rules is not None:
            self._values["backup_plan_rules"] = backup_plan_rules
        if backup_vault is not None:
            self._values["backup_vault"] = backup_vault
        if windows_vss is not None:
            self._values["windows_vss"] = windows_vss

    @builtins.property
    def backup_plan_name(self) -> typing.Optional[builtins.str]:
        '''The display name of the backup plan.

        :default: - A CDK generated name
        '''
        result = self._values.get("backup_plan_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backup_plan_rules(self) -> typing.Optional[typing.List["BackupPlanRule"]]:
        '''Rules for the backup plan.

        Use ``addRule()`` to add rules after
        instantiation.

        :default: - use ``addRule()`` to add rules
        '''
        result = self._values.get("backup_plan_rules")
        return typing.cast(typing.Optional[typing.List["BackupPlanRule"]], result)

    @builtins.property
    def backup_vault(self) -> typing.Optional["IBackupVault"]:
        '''The backup vault where backups are stored.

        :default:

        - use the vault defined at the rule level. If not defined a new
        common vault for the plan will be created
        '''
        result = self._values.get("backup_vault")
        return typing.cast(typing.Optional["IBackupVault"], result)

    @builtins.property
    def windows_vss(self) -> typing.Optional[builtins.bool]:
        '''Enable Windows VSS backup.

        :default: false

        :see: https://docs.aws.amazon.com/aws-backup/latest/devguide/windows-backups.html
        '''
        result = self._values.get("windows_vss")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupPlanProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BackupPlanRule(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_backup.BackupPlanRule",
):
    '''A backup plan rule.

    :exampleMetadata: infused

    Example::

        # plan: backup.BackupPlan
        
        plan.add_rule(backup.BackupPlanRule(
            enable_continuous_backup=True,
            delete_after=Duration.days(14)
        ))
    '''

    def __init__(
        self,
        *,
        backup_vault: typing.Optional["IBackupVault"] = None,
        completion_window: typing.Optional[_Duration_4839e8c3] = None,
        copy_actions: typing.Optional[typing.Sequence[typing.Union[BackupPlanCopyActionProps, typing.Dict[builtins.str, typing.Any]]]] = None,
        delete_after: typing.Optional[_Duration_4839e8c3] = None,
        enable_continuous_backup: typing.Optional[builtins.bool] = None,
        move_to_cold_storage_after: typing.Optional[_Duration_4839e8c3] = None,
        recovery_point_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        rule_name: typing.Optional[builtins.str] = None,
        schedule_expression: typing.Optional[_Schedule_c151d01f] = None,
        start_window: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''
        :param backup_vault: The backup vault where backups are. Default: - use the vault defined at the plan level. If not defined a new common vault for the plan will be created
        :param completion_window: The duration after a backup job is successfully started before it must be completed or it is canceled by AWS Backup. Default: - 7 days
        :param copy_actions: Copy operations to perform on recovery points created by this rule. Default: - no copy actions
        :param delete_after: Specifies the duration after creation that a recovery point is deleted. Must be greater than ``moveToColdStorageAfter``. Default: - recovery point is never deleted
        :param enable_continuous_backup: Enables continuous backup and point-in-time restores (PITR). Property ``deleteAfter`` defines the retention period for the backup. It is mandatory if PITR is enabled. If no value is specified, the retention period is set to 35 days which is the maximum retention period supported by PITR. Property ``moveToColdStorageAfter`` must not be specified because PITR does not support this option. Default: false
        :param move_to_cold_storage_after: Specifies the duration after creation that a recovery point is moved to cold storage. Default: - recovery point is never moved to cold storage
        :param recovery_point_tags: To help organize your resources, you can assign your own metadata to the resources that you create. Each tag is a key-value pair. Default: - no recovery point tags.
        :param rule_name: A display name for the backup rule. Default: - a CDK generated name
        :param schedule_expression: A CRON expression specifying when AWS Backup initiates a backup job. Default: - no schedule
        :param start_window: The duration after a backup is scheduled before a job is canceled if it doesn't start successfully. Default: - 8 hours
        '''
        props = BackupPlanRuleProps(
            backup_vault=backup_vault,
            completion_window=completion_window,
            copy_actions=copy_actions,
            delete_after=delete_after,
            enable_continuous_backup=enable_continuous_backup,
            move_to_cold_storage_after=move_to_cold_storage_after,
            recovery_point_tags=recovery_point_tags,
            rule_name=rule_name,
            schedule_expression=schedule_expression,
            start_window=start_window,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="daily")
    @builtins.classmethod
    def daily(
        cls,
        backup_vault: typing.Optional["IBackupVault"] = None,
    ) -> "BackupPlanRule":
        '''Daily with 35 days retention.

        :param backup_vault: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f78e665a93a5f3c61a81adf713b3dce3bf2c3c24d2e314a1fbc4460dc83b538)
            check_type(argname="argument backup_vault", value=backup_vault, expected_type=type_hints["backup_vault"])
        return typing.cast("BackupPlanRule", jsii.sinvoke(cls, "daily", [backup_vault]))

    @jsii.member(jsii_name="monthly1Year")
    @builtins.classmethod
    def monthly1_year(
        cls,
        backup_vault: typing.Optional["IBackupVault"] = None,
    ) -> "BackupPlanRule":
        '''Monthly 1 year retention, move to cold storage after 1 month.

        :param backup_vault: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d00b6f39a5ae5e68dc286fee4603f5606c654c044712abfb5d45b4c538938e0a)
            check_type(argname="argument backup_vault", value=backup_vault, expected_type=type_hints["backup_vault"])
        return typing.cast("BackupPlanRule", jsii.sinvoke(cls, "monthly1Year", [backup_vault]))

    @jsii.member(jsii_name="monthly5Year")
    @builtins.classmethod
    def monthly5_year(
        cls,
        backup_vault: typing.Optional["IBackupVault"] = None,
    ) -> "BackupPlanRule":
        '''Monthly 5 year retention, move to cold storage after 3 months.

        :param backup_vault: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4124e390401942af3d104beae29adc9c33bd1305f68302b0dd47aae3e11ca132)
            check_type(argname="argument backup_vault", value=backup_vault, expected_type=type_hints["backup_vault"])
        return typing.cast("BackupPlanRule", jsii.sinvoke(cls, "monthly5Year", [backup_vault]))

    @jsii.member(jsii_name="monthly7Year")
    @builtins.classmethod
    def monthly7_year(
        cls,
        backup_vault: typing.Optional["IBackupVault"] = None,
    ) -> "BackupPlanRule":
        '''Monthly 7 year retention, move to cold storage after 3 months.

        :param backup_vault: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af7999bcc928a751830ca431012278b60250723ffee54654765a4596696d022d)
            check_type(argname="argument backup_vault", value=backup_vault, expected_type=type_hints["backup_vault"])
        return typing.cast("BackupPlanRule", jsii.sinvoke(cls, "monthly7Year", [backup_vault]))

    @jsii.member(jsii_name="weekly")
    @builtins.classmethod
    def weekly(
        cls,
        backup_vault: typing.Optional["IBackupVault"] = None,
    ) -> "BackupPlanRule":
        '''Weekly with 3 months retention.

        :param backup_vault: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__759b8b9514606abffe4399669994cb3f2c365fc9e05295dd8d754f5af6bb329f)
            check_type(argname="argument backup_vault", value=backup_vault, expected_type=type_hints["backup_vault"])
        return typing.cast("BackupPlanRule", jsii.sinvoke(cls, "weekly", [backup_vault]))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "BackupPlanRuleProps":
        '''Properties of BackupPlanRule.'''
        return typing.cast("BackupPlanRuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_backup.BackupPlanRuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "backup_vault": "backupVault",
        "completion_window": "completionWindow",
        "copy_actions": "copyActions",
        "delete_after": "deleteAfter",
        "enable_continuous_backup": "enableContinuousBackup",
        "move_to_cold_storage_after": "moveToColdStorageAfter",
        "recovery_point_tags": "recoveryPointTags",
        "rule_name": "ruleName",
        "schedule_expression": "scheduleExpression",
        "start_window": "startWindow",
    },
)
class BackupPlanRuleProps:
    def __init__(
        self,
        *,
        backup_vault: typing.Optional["IBackupVault"] = None,
        completion_window: typing.Optional[_Duration_4839e8c3] = None,
        copy_actions: typing.Optional[typing.Sequence[typing.Union[BackupPlanCopyActionProps, typing.Dict[builtins.str, typing.Any]]]] = None,
        delete_after: typing.Optional[_Duration_4839e8c3] = None,
        enable_continuous_backup: typing.Optional[builtins.bool] = None,
        move_to_cold_storage_after: typing.Optional[_Duration_4839e8c3] = None,
        recovery_point_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        rule_name: typing.Optional[builtins.str] = None,
        schedule_expression: typing.Optional[_Schedule_c151d01f] = None,
        start_window: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''Properties for a BackupPlanRule.

        :param backup_vault: The backup vault where backups are. Default: - use the vault defined at the plan level. If not defined a new common vault for the plan will be created
        :param completion_window: The duration after a backup job is successfully started before it must be completed or it is canceled by AWS Backup. Default: - 7 days
        :param copy_actions: Copy operations to perform on recovery points created by this rule. Default: - no copy actions
        :param delete_after: Specifies the duration after creation that a recovery point is deleted. Must be greater than ``moveToColdStorageAfter``. Default: - recovery point is never deleted
        :param enable_continuous_backup: Enables continuous backup and point-in-time restores (PITR). Property ``deleteAfter`` defines the retention period for the backup. It is mandatory if PITR is enabled. If no value is specified, the retention period is set to 35 days which is the maximum retention period supported by PITR. Property ``moveToColdStorageAfter`` must not be specified because PITR does not support this option. Default: false
        :param move_to_cold_storage_after: Specifies the duration after creation that a recovery point is moved to cold storage. Default: - recovery point is never moved to cold storage
        :param recovery_point_tags: To help organize your resources, you can assign your own metadata to the resources that you create. Each tag is a key-value pair. Default: - no recovery point tags.
        :param rule_name: A display name for the backup rule. Default: - a CDK generated name
        :param schedule_expression: A CRON expression specifying when AWS Backup initiates a backup job. Default: - no schedule
        :param start_window: The duration after a backup is scheduled before a job is canceled if it doesn't start successfully. Default: - 8 hours

        :exampleMetadata: infused

        Example::

            # plan: backup.BackupPlan
            # secondary_vault: backup.BackupVault
            
            plan.add_rule(backup.BackupPlanRule(
                copy_actions=[backup.BackupPlanCopyActionProps(
                    destination_backup_vault=secondary_vault,
                    move_to_cold_storage_after=Duration.days(30),
                    delete_after=Duration.days(120)
                )]
            ))
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__521e43eca71db1c8347b5dbf1e88135cbc1fd43f07248784b33b55d8353d5d90)
            check_type(argname="argument backup_vault", value=backup_vault, expected_type=type_hints["backup_vault"])
            check_type(argname="argument completion_window", value=completion_window, expected_type=type_hints["completion_window"])
            check_type(argname="argument copy_actions", value=copy_actions, expected_type=type_hints["copy_actions"])
            check_type(argname="argument delete_after", value=delete_after, expected_type=type_hints["delete_after"])
            check_type(argname="argument enable_continuous_backup", value=enable_continuous_backup, expected_type=type_hints["enable_continuous_backup"])
            check_type(argname="argument move_to_cold_storage_after", value=move_to_cold_storage_after, expected_type=type_hints["move_to_cold_storage_after"])
            check_type(argname="argument recovery_point_tags", value=recovery_point_tags, expected_type=type_hints["recovery_point_tags"])
            check_type(argname="argument rule_name", value=rule_name, expected_type=type_hints["rule_name"])
            check_type(argname="argument schedule_expression", value=schedule_expression, expected_type=type_hints["schedule_expression"])
            check_type(argname="argument start_window", value=start_window, expected_type=type_hints["start_window"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if backup_vault is not None:
            self._values["backup_vault"] = backup_vault
        if completion_window is not None:
            self._values["completion_window"] = completion_window
        if copy_actions is not None:
            self._values["copy_actions"] = copy_actions
        if delete_after is not None:
            self._values["delete_after"] = delete_after
        if enable_continuous_backup is not None:
            self._values["enable_continuous_backup"] = enable_continuous_backup
        if move_to_cold_storage_after is not None:
            self._values["move_to_cold_storage_after"] = move_to_cold_storage_after
        if recovery_point_tags is not None:
            self._values["recovery_point_tags"] = recovery_point_tags
        if rule_name is not None:
            self._values["rule_name"] = rule_name
        if schedule_expression is not None:
            self._values["schedule_expression"] = schedule_expression
        if start_window is not None:
            self._values["start_window"] = start_window

    @builtins.property
    def backup_vault(self) -> typing.Optional["IBackupVault"]:
        '''The backup vault where backups are.

        :default:

        - use the vault defined at the plan level. If not defined a new
        common vault for the plan will be created
        '''
        result = self._values.get("backup_vault")
        return typing.cast(typing.Optional["IBackupVault"], result)

    @builtins.property
    def completion_window(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The duration after a backup job is successfully started before it must be completed or it is canceled by AWS Backup.

        :default: - 7 days
        '''
        result = self._values.get("completion_window")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def copy_actions(self) -> typing.Optional[typing.List[BackupPlanCopyActionProps]]:
        '''Copy operations to perform on recovery points created by this rule.

        :default: - no copy actions
        '''
        result = self._values.get("copy_actions")
        return typing.cast(typing.Optional[typing.List[BackupPlanCopyActionProps]], result)

    @builtins.property
    def delete_after(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Specifies the duration after creation that a recovery point is deleted.

        Must be greater than ``moveToColdStorageAfter``.

        :default: - recovery point is never deleted
        '''
        result = self._values.get("delete_after")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def enable_continuous_backup(self) -> typing.Optional[builtins.bool]:
        '''Enables continuous backup and point-in-time restores (PITR).

        Property ``deleteAfter`` defines the retention period for the backup. It is mandatory if PITR is enabled.
        If no value is specified, the retention period is set to 35 days which is the maximum retention period supported by PITR.

        Property ``moveToColdStorageAfter`` must not be specified because PITR does not support this option.

        :default: false
        '''
        result = self._values.get("enable_continuous_backup")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def move_to_cold_storage_after(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Specifies the duration after creation that a recovery point is moved to cold storage.

        :default: - recovery point is never moved to cold storage
        '''
        result = self._values.get("move_to_cold_storage_after")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def recovery_point_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''To help organize your resources, you can assign your own metadata to the resources that you create.

        Each tag is a key-value pair.

        :default: - no recovery point tags.
        '''
        result = self._values.get("recovery_point_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def rule_name(self) -> typing.Optional[builtins.str]:
        '''A display name for the backup rule.

        :default: - a CDK generated name
        '''
        result = self._values.get("rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedule_expression(self) -> typing.Optional[_Schedule_c151d01f]:
        '''A CRON expression specifying when AWS Backup initiates a backup job.

        :default: - no schedule
        '''
        result = self._values.get("schedule_expression")
        return typing.cast(typing.Optional[_Schedule_c151d01f], result)

    @builtins.property
    def start_window(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The duration after a backup is scheduled before a job is canceled if it doesn't start successfully.

        :default: - 8 hours
        '''
        result = self._values.get("start_window")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupPlanRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BackupResource(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_backup.BackupResource",
):
    '''A resource to backup.

    :exampleMetadata: infused

    Example::

        # plan: backup.BackupPlan
        # vpc: ec2.Vpc
        
        my_table = dynamodb.Table.from_table_name(self, "Table", "myTableName")
        my_database_instance = rds.DatabaseInstance(self, "DatabaseInstance",
            engine=rds.DatabaseInstanceEngine.mysql(version=rds.MysqlEngineVersion.VER_8_0_26),
            vpc=vpc
        )
        my_database_cluster = rds.DatabaseCluster(self, "DatabaseCluster",
            engine=rds.DatabaseClusterEngine.aurora_mysql(version=rds.AuroraMysqlEngineVersion.VER_2_08_1),
            credentials=rds.Credentials.from_generated_secret("clusteradmin"),
            instance_props=rds.InstanceProps(
                vpc=vpc
            )
        )
        my_serverless_cluster = rds.ServerlessCluster(self, "ServerlessCluster",
            engine=rds.DatabaseClusterEngine.AURORA_POSTGRESQL,
            parameter_group=rds.ParameterGroup.from_parameter_group_name(self, "ParameterGroup", "default.aurora-postgresql11"),
            vpc=vpc
        )
        my_cool_construct = Construct(self, "MyCoolConstruct")
        
        plan.add_selection("Selection",
            resources=[
                backup.BackupResource.from_dynamo_db_table(my_table),  # A DynamoDB table
                backup.BackupResource.from_rds_database_instance(my_database_instance),  # A RDS instance
                backup.BackupResource.from_rds_database_cluster(my_database_cluster),  # A RDS database cluster
                backup.BackupResource.from_rds_serverless_cluster(my_serverless_cluster),  # An Aurora Serverless cluster
                backup.BackupResource.from_tag("stage", "prod"),  # All resources that are tagged stage=prod in the region/account
                backup.BackupResource.from_construct(my_cool_construct)
            ]
        )
    '''

    def __init__(
        self,
        resource: typing.Optional[builtins.str] = None,
        tag_condition: typing.Optional[typing.Union["TagCondition", typing.Dict[builtins.str, typing.Any]]] = None,
        construct: typing.Optional[_constructs_77d1e7e8.Construct] = None,
    ) -> None:
        '''
        :param resource: -
        :param tag_condition: -
        :param construct: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da262bae32a880066638158d96c942364504852f2d4af32d72bcd0034c7fbd32)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
            check_type(argname="argument tag_condition", value=tag_condition, expected_type=type_hints["tag_condition"])
            check_type(argname="argument construct", value=construct, expected_type=type_hints["construct"])
        jsii.create(self.__class__, self, [resource, tag_condition, construct])

    @jsii.member(jsii_name="fromArn")
    @builtins.classmethod
    def from_arn(cls, arn: builtins.str) -> "BackupResource":
        '''A list of ARNs or match patterns such as ``arn:aws:ec2:us-east-1:123456789012:volume/*``.

        :param arn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2db3e845e2974e883de9fa3efc667fda5fd092ba7fea3f5fa1f1c15a5188862a)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
        return typing.cast("BackupResource", jsii.sinvoke(cls, "fromArn", [arn]))

    @jsii.member(jsii_name="fromConstruct")
    @builtins.classmethod
    def from_construct(
        cls,
        construct: _constructs_77d1e7e8.Construct,
    ) -> "BackupResource":
        '''Adds all supported resources in a construct.

        :param construct: The construct containing resources to backup.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c8359998ff8f774202e1b0869097e19c3e167e8e7a6a5ee95936f1b09f063b8)
            check_type(argname="argument construct", value=construct, expected_type=type_hints["construct"])
        return typing.cast("BackupResource", jsii.sinvoke(cls, "fromConstruct", [construct]))

    @jsii.member(jsii_name="fromDynamoDbTable")
    @builtins.classmethod
    def from_dynamo_db_table(cls, table: _ITable_504fd401) -> "BackupResource":
        '''A DynamoDB table.

        :param table: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75ec54ba33468f397b4b954ffff5bb4a26a29e306b38c37a8a831233ca47cf40)
            check_type(argname="argument table", value=table, expected_type=type_hints["table"])
        return typing.cast("BackupResource", jsii.sinvoke(cls, "fromDynamoDbTable", [table]))

    @jsii.member(jsii_name="fromEc2Instance")
    @builtins.classmethod
    def from_ec2_instance(cls, instance: _IInstance_ab239e7c) -> "BackupResource":
        '''An EC2 instance.

        :param instance: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfac18ef33642ed976be7473c0fe4b5174e370a770ceabc690e397bcecfce6a3)
            check_type(argname="argument instance", value=instance, expected_type=type_hints["instance"])
        return typing.cast("BackupResource", jsii.sinvoke(cls, "fromEc2Instance", [instance]))

    @jsii.member(jsii_name="fromEfsFileSystem")
    @builtins.classmethod
    def from_efs_file_system(
        cls,
        file_system: _IFileSystem_b2d3a7cb,
    ) -> "BackupResource":
        '''An EFS file system.

        :param file_system: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a724b31752318e43681480d257f284af035f11db8b7b91a2712b0a19a09283b)
            check_type(argname="argument file_system", value=file_system, expected_type=type_hints["file_system"])
        return typing.cast("BackupResource", jsii.sinvoke(cls, "fromEfsFileSystem", [file_system]))

    @jsii.member(jsii_name="fromRdsDatabaseCluster")
    @builtins.classmethod
    def from_rds_database_cluster(
        cls,
        cluster: _IDatabaseCluster_6554c32b,
    ) -> "BackupResource":
        '''A RDS database cluter.

        :param cluster: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2043352654f5d7b0272be6002773b2263d7a3a58bb3ca681d050846773b6a7a4)
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
        return typing.cast("BackupResource", jsii.sinvoke(cls, "fromRdsDatabaseCluster", [cluster]))

    @jsii.member(jsii_name="fromRdsDatabaseInstance")
    @builtins.classmethod
    def from_rds_database_instance(
        cls,
        instance: _IDatabaseInstance_e4cb03a8,
    ) -> "BackupResource":
        '''A RDS database instance.

        :param instance: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3a85f96e06b0e43fed194c604af81aa14d506827b7f57b6fef4f8e0191d38d1)
            check_type(argname="argument instance", value=instance, expected_type=type_hints["instance"])
        return typing.cast("BackupResource", jsii.sinvoke(cls, "fromRdsDatabaseInstance", [instance]))

    @jsii.member(jsii_name="fromRdsServerlessCluster")
    @builtins.classmethod
    def from_rds_serverless_cluster(
        cls,
        cluster: _IServerlessCluster_adbbb720,
    ) -> "BackupResource":
        '''An Aurora database instance.

        :param cluster: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a96658ef472d54f85f9fb6dfeffb763befda835ec279615ad329c159e5acf1a6)
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
        return typing.cast("BackupResource", jsii.sinvoke(cls, "fromRdsServerlessCluster", [cluster]))

    @jsii.member(jsii_name="fromTag")
    @builtins.classmethod
    def from_tag(
        cls,
        key: builtins.str,
        value: builtins.str,
        operation: typing.Optional["TagOperation"] = None,
    ) -> "BackupResource":
        '''A tag condition.

        :param key: -
        :param value: -
        :param operation: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c47a77dd61236c04d92fba31585e4ea943b8bb7dfce2ab0dc2f09ab9bd172316)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument operation", value=operation, expected_type=type_hints["operation"])
        return typing.cast("BackupResource", jsii.sinvoke(cls, "fromTag", [key, value, operation]))

    @builtins.property
    @jsii.member(jsii_name="construct")
    def construct(self) -> typing.Optional[_constructs_77d1e7e8.Construct]:
        '''A construct.'''
        return typing.cast(typing.Optional[_constructs_77d1e7e8.Construct], jsii.get(self, "construct"))

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(self) -> typing.Optional[builtins.str]:
        '''A resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resource"))

    @builtins.property
    @jsii.member(jsii_name="tagCondition")
    def tag_condition(self) -> typing.Optional["TagCondition"]:
        '''A condition on a tag.'''
        return typing.cast(typing.Optional["TagCondition"], jsii.get(self, "tagCondition"))


@jsii.implements(_IGrantable_71c4f5de)
class BackupSelection(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_backup.BackupSelection",
):
    '''A backup selection.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_backup as backup
        from aws_cdk import aws_iam as iam
        
        # backup_plan: backup.BackupPlan
        # backup_resource: backup.BackupResource
        # role: iam.Role
        
        backup_selection = backup.BackupSelection(self, "MyBackupSelection",
            backup_plan=backup_plan,
            resources=[backup_resource],
        
            # the properties below are optional
            allow_restores=False,
            backup_selection_name="backupSelectionName",
            disable_default_backup_policy=False,
            role=role
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        backup_plan: "IBackupPlan",
        resources: typing.Sequence[BackupResource],
        allow_restores: typing.Optional[builtins.bool] = None,
        backup_selection_name: typing.Optional[builtins.str] = None,
        disable_default_backup_policy: typing.Optional[builtins.bool] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param backup_plan: The backup plan for this selection.
        :param resources: The resources to backup. Use the helper static methods defined on ``BackupResource``.
        :param allow_restores: Whether to automatically give restores permissions to the role that AWS Backup uses. If ``true``, the ``AWSBackupServiceRolePolicyForRestores`` managed policy will be attached to the role. Default: false
        :param backup_selection_name: The name for this selection. Default: - a CDK generated name
        :param disable_default_backup_policy: Whether to disable automatically assigning default backup permissions to the role that AWS Backup uses. If ``false``, the ``AWSBackupServiceRolePolicyForBackup`` managed policy will be attached to the role. Default: false
        :param role: The role that AWS Backup uses to authenticate when backuping or restoring the resources. The ``AWSBackupServiceRolePolicyForBackup`` managed policy will be attached to this role unless ``disableDefaultBackupPolicy`` is set to ``true``. Default: - a new role will be created
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb124dbc539b313053b8d36e3fbbda7c8ef513917e5cdb41a9d2a7ecaaca7643)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = BackupSelectionProps(
            backup_plan=backup_plan,
            resources=resources,
            allow_restores=allow_restores,
            backup_selection_name=backup_selection_name,
            disable_default_backup_policy=disable_default_backup_policy,
            role=role,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="backupPlanId")
    def backup_plan_id(self) -> builtins.str:
        '''The identifier of the backup plan.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "backupPlanId"))

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> _IPrincipal_539bb2fd:
        '''The principal to grant permissions to.'''
        return typing.cast(_IPrincipal_539bb2fd, jsii.get(self, "grantPrincipal"))

    @builtins.property
    @jsii.member(jsii_name="selectionId")
    def selection_id(self) -> builtins.str:
        '''The identifier of the backup selection.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "selectionId"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_backup.BackupSelectionOptions",
    jsii_struct_bases=[],
    name_mapping={
        "resources": "resources",
        "allow_restores": "allowRestores",
        "backup_selection_name": "backupSelectionName",
        "disable_default_backup_policy": "disableDefaultBackupPolicy",
        "role": "role",
    },
)
class BackupSelectionOptions:
    def __init__(
        self,
        *,
        resources: typing.Sequence[BackupResource],
        allow_restores: typing.Optional[builtins.bool] = None,
        backup_selection_name: typing.Optional[builtins.str] = None,
        disable_default_backup_policy: typing.Optional[builtins.bool] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''Options for a BackupSelection.

        :param resources: The resources to backup. Use the helper static methods defined on ``BackupResource``.
        :param allow_restores: Whether to automatically give restores permissions to the role that AWS Backup uses. If ``true``, the ``AWSBackupServiceRolePolicyForRestores`` managed policy will be attached to the role. Default: false
        :param backup_selection_name: The name for this selection. Default: - a CDK generated name
        :param disable_default_backup_policy: Whether to disable automatically assigning default backup permissions to the role that AWS Backup uses. If ``false``, the ``AWSBackupServiceRolePolicyForBackup`` managed policy will be attached to the role. Default: false
        :param role: The role that AWS Backup uses to authenticate when backuping or restoring the resources. The ``AWSBackupServiceRolePolicyForBackup`` managed policy will be attached to this role unless ``disableDefaultBackupPolicy`` is set to ``true``. Default: - a new role will be created

        :exampleMetadata: infused

        Example::

            # plan: backup.BackupPlan
            # vpc: ec2.Vpc
            
            my_table = dynamodb.Table.from_table_name(self, "Table", "myTableName")
            my_database_instance = rds.DatabaseInstance(self, "DatabaseInstance",
                engine=rds.DatabaseInstanceEngine.mysql(version=rds.MysqlEngineVersion.VER_8_0_26),
                vpc=vpc
            )
            my_database_cluster = rds.DatabaseCluster(self, "DatabaseCluster",
                engine=rds.DatabaseClusterEngine.aurora_mysql(version=rds.AuroraMysqlEngineVersion.VER_2_08_1),
                credentials=rds.Credentials.from_generated_secret("clusteradmin"),
                instance_props=rds.InstanceProps(
                    vpc=vpc
                )
            )
            my_serverless_cluster = rds.ServerlessCluster(self, "ServerlessCluster",
                engine=rds.DatabaseClusterEngine.AURORA_POSTGRESQL,
                parameter_group=rds.ParameterGroup.from_parameter_group_name(self, "ParameterGroup", "default.aurora-postgresql11"),
                vpc=vpc
            )
            my_cool_construct = Construct(self, "MyCoolConstruct")
            
            plan.add_selection("Selection",
                resources=[
                    backup.BackupResource.from_dynamo_db_table(my_table),  # A DynamoDB table
                    backup.BackupResource.from_rds_database_instance(my_database_instance),  # A RDS instance
                    backup.BackupResource.from_rds_database_cluster(my_database_cluster),  # A RDS database cluster
                    backup.BackupResource.from_rds_serverless_cluster(my_serverless_cluster),  # An Aurora Serverless cluster
                    backup.BackupResource.from_tag("stage", "prod"),  # All resources that are tagged stage=prod in the region/account
                    backup.BackupResource.from_construct(my_cool_construct)
                ]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99c0cf23958862e40e3aaa86170756388807569db1aeb820435bca2898ff496c)
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
            check_type(argname="argument allow_restores", value=allow_restores, expected_type=type_hints["allow_restores"])
            check_type(argname="argument backup_selection_name", value=backup_selection_name, expected_type=type_hints["backup_selection_name"])
            check_type(argname="argument disable_default_backup_policy", value=disable_default_backup_policy, expected_type=type_hints["disable_default_backup_policy"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resources": resources,
        }
        if allow_restores is not None:
            self._values["allow_restores"] = allow_restores
        if backup_selection_name is not None:
            self._values["backup_selection_name"] = backup_selection_name
        if disable_default_backup_policy is not None:
            self._values["disable_default_backup_policy"] = disable_default_backup_policy
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def resources(self) -> typing.List[BackupResource]:
        '''The resources to backup.

        Use the helper static methods defined on ``BackupResource``.
        '''
        result = self._values.get("resources")
        assert result is not None, "Required property 'resources' is missing"
        return typing.cast(typing.List[BackupResource], result)

    @builtins.property
    def allow_restores(self) -> typing.Optional[builtins.bool]:
        '''Whether to automatically give restores permissions to the role that AWS Backup uses.

        If ``true``, the ``AWSBackupServiceRolePolicyForRestores`` managed
        policy will be attached to the role.

        :default: false
        '''
        result = self._values.get("allow_restores")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def backup_selection_name(self) -> typing.Optional[builtins.str]:
        '''The name for this selection.

        :default: - a CDK generated name
        '''
        result = self._values.get("backup_selection_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_default_backup_policy(self) -> typing.Optional[builtins.bool]:
        '''Whether to disable automatically assigning default backup permissions to the role that AWS Backup uses.

        If ``false``, the ``AWSBackupServiceRolePolicyForBackup`` managed policy will be
        attached to the role.

        :default: false
        '''
        result = self._values.get("disable_default_backup_policy")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The role that AWS Backup uses to authenticate when backuping or restoring the resources.

        The ``AWSBackupServiceRolePolicyForBackup`` managed policy
        will be attached to this role unless ``disableDefaultBackupPolicy``
        is set to ``true``.

        :default: - a new role will be created
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupSelectionOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_backup.BackupSelectionProps",
    jsii_struct_bases=[BackupSelectionOptions],
    name_mapping={
        "resources": "resources",
        "allow_restores": "allowRestores",
        "backup_selection_name": "backupSelectionName",
        "disable_default_backup_policy": "disableDefaultBackupPolicy",
        "role": "role",
        "backup_plan": "backupPlan",
    },
)
class BackupSelectionProps(BackupSelectionOptions):
    def __init__(
        self,
        *,
        resources: typing.Sequence[BackupResource],
        allow_restores: typing.Optional[builtins.bool] = None,
        backup_selection_name: typing.Optional[builtins.str] = None,
        disable_default_backup_policy: typing.Optional[builtins.bool] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        backup_plan: "IBackupPlan",
    ) -> None:
        '''Properties for a BackupSelection.

        :param resources: The resources to backup. Use the helper static methods defined on ``BackupResource``.
        :param allow_restores: Whether to automatically give restores permissions to the role that AWS Backup uses. If ``true``, the ``AWSBackupServiceRolePolicyForRestores`` managed policy will be attached to the role. Default: false
        :param backup_selection_name: The name for this selection. Default: - a CDK generated name
        :param disable_default_backup_policy: Whether to disable automatically assigning default backup permissions to the role that AWS Backup uses. If ``false``, the ``AWSBackupServiceRolePolicyForBackup`` managed policy will be attached to the role. Default: false
        :param role: The role that AWS Backup uses to authenticate when backuping or restoring the resources. The ``AWSBackupServiceRolePolicyForBackup`` managed policy will be attached to this role unless ``disableDefaultBackupPolicy`` is set to ``true``. Default: - a new role will be created
        :param backup_plan: The backup plan for this selection.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_backup as backup
            from aws_cdk import aws_iam as iam
            
            # backup_plan: backup.BackupPlan
            # backup_resource: backup.BackupResource
            # role: iam.Role
            
            backup_selection_props = backup.BackupSelectionProps(
                backup_plan=backup_plan,
                resources=[backup_resource],
            
                # the properties below are optional
                allow_restores=False,
                backup_selection_name="backupSelectionName",
                disable_default_backup_policy=False,
                role=role
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd3a38c041da3373a6278620797d45b4058a0d5aede2c0a4bc706fdeff586bc8)
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
            check_type(argname="argument allow_restores", value=allow_restores, expected_type=type_hints["allow_restores"])
            check_type(argname="argument backup_selection_name", value=backup_selection_name, expected_type=type_hints["backup_selection_name"])
            check_type(argname="argument disable_default_backup_policy", value=disable_default_backup_policy, expected_type=type_hints["disable_default_backup_policy"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument backup_plan", value=backup_plan, expected_type=type_hints["backup_plan"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resources": resources,
            "backup_plan": backup_plan,
        }
        if allow_restores is not None:
            self._values["allow_restores"] = allow_restores
        if backup_selection_name is not None:
            self._values["backup_selection_name"] = backup_selection_name
        if disable_default_backup_policy is not None:
            self._values["disable_default_backup_policy"] = disable_default_backup_policy
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def resources(self) -> typing.List[BackupResource]:
        '''The resources to backup.

        Use the helper static methods defined on ``BackupResource``.
        '''
        result = self._values.get("resources")
        assert result is not None, "Required property 'resources' is missing"
        return typing.cast(typing.List[BackupResource], result)

    @builtins.property
    def allow_restores(self) -> typing.Optional[builtins.bool]:
        '''Whether to automatically give restores permissions to the role that AWS Backup uses.

        If ``true``, the ``AWSBackupServiceRolePolicyForRestores`` managed
        policy will be attached to the role.

        :default: false
        '''
        result = self._values.get("allow_restores")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def backup_selection_name(self) -> typing.Optional[builtins.str]:
        '''The name for this selection.

        :default: - a CDK generated name
        '''
        result = self._values.get("backup_selection_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_default_backup_policy(self) -> typing.Optional[builtins.bool]:
        '''Whether to disable automatically assigning default backup permissions to the role that AWS Backup uses.

        If ``false``, the ``AWSBackupServiceRolePolicyForBackup`` managed policy will be
        attached to the role.

        :default: false
        '''
        result = self._values.get("disable_default_backup_policy")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The role that AWS Backup uses to authenticate when backuping or restoring the resources.

        The ``AWSBackupServiceRolePolicyForBackup`` managed policy
        will be attached to this role unless ``disableDefaultBackupPolicy``
        is set to ``true``.

        :default: - a new role will be created
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def backup_plan(self) -> "IBackupPlan":
        '''The backup plan for this selection.'''
        result = self._values.get("backup_plan")
        assert result is not None, "Required property 'backup_plan' is missing"
        return typing.cast("IBackupPlan", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupSelectionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_backup.BackupVaultEvents")
class BackupVaultEvents(enum.Enum):
    '''Backup vault events.

    Some events are no longer supported and will not return
    statuses or notifications.

    :see: https://docs.aws.amazon.com/aws-backup/latest/devguide/API_PutBackupVaultNotifications.html#API_PutBackupVaultNotifications_RequestBody
    '''

    BACKUP_JOB_STARTED = "BACKUP_JOB_STARTED"
    '''BACKUP_JOB_STARTED.'''
    BACKUP_JOB_COMPLETED = "BACKUP_JOB_COMPLETED"
    '''BACKUP_JOB_COMPLETED.'''
    BACKUP_JOB_SUCCESSFUL = "BACKUP_JOB_SUCCESSFUL"
    '''BACKUP_JOB_SUCCESSFUL.'''
    BACKUP_JOB_FAILED = "BACKUP_JOB_FAILED"
    '''BACKUP_JOB_FAILED.'''
    BACKUP_JOB_EXPIRED = "BACKUP_JOB_EXPIRED"
    '''BACKUP_JOB_EXPIRED.'''
    RESTORE_JOB_STARTED = "RESTORE_JOB_STARTED"
    '''RESTORE_JOB_STARTED.'''
    RESTORE_JOB_COMPLETED = "RESTORE_JOB_COMPLETED"
    '''RESTORE_JOB_COMPLETED.'''
    RESTORE_JOB_SUCCESSFUL = "RESTORE_JOB_SUCCESSFUL"
    '''RESTORE_JOB_SUCCESSFUL.'''
    RESTORE_JOB_FAILED = "RESTORE_JOB_FAILED"
    '''RESTORE_JOB_FAILED.'''
    COPY_JOB_STARTED = "COPY_JOB_STARTED"
    '''COPY_JOB_STARTED.'''
    COPY_JOB_SUCCESSFUL = "COPY_JOB_SUCCESSFUL"
    '''COPY_JOB_SUCCESSFUL.'''
    COPY_JOB_FAILED = "COPY_JOB_FAILED"
    '''COPY_JOB_FAILED.'''
    RECOVERY_POINT_MODIFIED = "RECOVERY_POINT_MODIFIED"
    '''RECOVERY_POINT_MODIFIED.'''
    BACKUP_PLAN_CREATED = "BACKUP_PLAN_CREATED"
    '''BACKUP_PLAN_CREATED.'''
    BACKUP_PLAN_MODIFIED = "BACKUP_PLAN_MODIFIED"
    '''BACKUP_PLAN_MODIFIED.'''
    S3_BACKUP_OBJECT_FAILED = "S3_BACKUP_OBJECT_FAILED"
    '''S3_BACKUP_OBJECT_FAILED.'''
    S3_RESTORE_OBJECT_FAILED = "S3_RESTORE_OBJECT_FAILED"
    '''BACKUP_PLAN_MODIFIED.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_backup.BackupVaultProps",
    jsii_struct_bases=[],
    name_mapping={
        "access_policy": "accessPolicy",
        "backup_vault_name": "backupVaultName",
        "block_recovery_point_deletion": "blockRecoveryPointDeletion",
        "encryption_key": "encryptionKey",
        "lock_configuration": "lockConfiguration",
        "notification_events": "notificationEvents",
        "notification_topic": "notificationTopic",
        "removal_policy": "removalPolicy",
    },
)
class BackupVaultProps:
    def __init__(
        self,
        *,
        access_policy: typing.Optional[_PolicyDocument_3ac34393] = None,
        backup_vault_name: typing.Optional[builtins.str] = None,
        block_recovery_point_deletion: typing.Optional[builtins.bool] = None,
        encryption_key: typing.Optional[_IKey_5f11635f] = None,
        lock_configuration: typing.Optional[typing.Union["LockConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        notification_events: typing.Optional[typing.Sequence[BackupVaultEvents]] = None,
        notification_topic: typing.Optional[_ITopic_9eca4852] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    ) -> None:
        '''Properties for a BackupVault.

        :param access_policy: A resource-based policy that is used to manage access permissions on the backup vault. Default: - access is not restricted
        :param backup_vault_name: The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. Default: - A CDK generated name
        :param block_recovery_point_deletion: Whether to add statements to the vault access policy that prevents anyone from deleting a recovery point. Default: false
        :param encryption_key: The server-side encryption key to use to protect your backups. Default: - an Amazon managed KMS key
        :param lock_configuration: Configuration for AWS Backup Vault Lock. Default: - AWS Backup Vault Lock is disabled
        :param notification_events: The vault events to send. Default: - all vault events if ``notificationTopic`` is defined
        :param notification_topic: A SNS topic to send vault events to. Default: - no notifications
        :param removal_policy: The removal policy to apply to the vault. Note that removing a vault that contains recovery points will fail. Default: RemovalPolicy.RETAIN

        :exampleMetadata: infused

        Example::

            my_key = kms.Key.from_key_arn(self, "MyKey", "aaa")
            my_topic = sns.Topic.from_topic_arn(self, "MyTopic", "bbb")
            
            vault = backup.BackupVault(self, "Vault",
                encryption_key=my_key,  # Custom encryption key
                notification_topic=my_topic
            )
        '''
        if isinstance(lock_configuration, dict):
            lock_configuration = LockConfiguration(**lock_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a7555f4b25ca4760e3a057b8e3a9b5e07feed1f99319d6e434cc8fed4e71af6)
            check_type(argname="argument access_policy", value=access_policy, expected_type=type_hints["access_policy"])
            check_type(argname="argument backup_vault_name", value=backup_vault_name, expected_type=type_hints["backup_vault_name"])
            check_type(argname="argument block_recovery_point_deletion", value=block_recovery_point_deletion, expected_type=type_hints["block_recovery_point_deletion"])
            check_type(argname="argument encryption_key", value=encryption_key, expected_type=type_hints["encryption_key"])
            check_type(argname="argument lock_configuration", value=lock_configuration, expected_type=type_hints["lock_configuration"])
            check_type(argname="argument notification_events", value=notification_events, expected_type=type_hints["notification_events"])
            check_type(argname="argument notification_topic", value=notification_topic, expected_type=type_hints["notification_topic"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if access_policy is not None:
            self._values["access_policy"] = access_policy
        if backup_vault_name is not None:
            self._values["backup_vault_name"] = backup_vault_name
        if block_recovery_point_deletion is not None:
            self._values["block_recovery_point_deletion"] = block_recovery_point_deletion
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if lock_configuration is not None:
            self._values["lock_configuration"] = lock_configuration
        if notification_events is not None:
            self._values["notification_events"] = notification_events
        if notification_topic is not None:
            self._values["notification_topic"] = notification_topic
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy

    @builtins.property
    def access_policy(self) -> typing.Optional[_PolicyDocument_3ac34393]:
        '''A resource-based policy that is used to manage access permissions on the backup vault.

        :default: - access is not restricted
        '''
        result = self._values.get("access_policy")
        return typing.cast(typing.Optional[_PolicyDocument_3ac34393], result)

    @builtins.property
    def backup_vault_name(self) -> typing.Optional[builtins.str]:
        '''The name of a logical container where backups are stored.

        Backup vaults
        are identified by names that are unique to the account used to create
        them and the AWS Region where they are created.

        :default: - A CDK generated name
        '''
        result = self._values.get("backup_vault_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def block_recovery_point_deletion(self) -> typing.Optional[builtins.bool]:
        '''Whether to add statements to the vault access policy that prevents anyone from deleting a recovery point.

        :default: false
        '''
        result = self._values.get("block_recovery_point_deletion")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''The server-side encryption key to use to protect your backups.

        :default: - an Amazon managed KMS key
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[_IKey_5f11635f], result)

    @builtins.property
    def lock_configuration(self) -> typing.Optional["LockConfiguration"]:
        '''Configuration for AWS Backup Vault Lock.

        :default: - AWS Backup Vault Lock is disabled

        :see: https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html
        '''
        result = self._values.get("lock_configuration")
        return typing.cast(typing.Optional["LockConfiguration"], result)

    @builtins.property
    def notification_events(self) -> typing.Optional[typing.List[BackupVaultEvents]]:
        '''The vault events to send.

        :default: - all vault events if ``notificationTopic`` is defined

        :see: https://docs.aws.amazon.com/aws-backup/latest/devguide/sns-notifications.html
        '''
        result = self._values.get("notification_events")
        return typing.cast(typing.Optional[typing.List[BackupVaultEvents]], result)

    @builtins.property
    def notification_topic(self) -> typing.Optional[_ITopic_9eca4852]:
        '''A SNS topic to send vault events to.

        :default: - no notifications

        :see: https://docs.aws.amazon.com/aws-backup/latest/devguide/sns-notifications.html
        '''
        result = self._values.get("notification_topic")
        return typing.cast(typing.Optional[_ITopic_9eca4852], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[_RemovalPolicy_9f93c814]:
        '''The removal policy to apply to the vault.

        Note that removing a vault
        that contains recovery points will fail.

        :default: RemovalPolicy.RETAIN
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_RemovalPolicy_9f93c814], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupVaultProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnBackupPlan(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_backup.CfnBackupPlan",
):
    '''Contains an optional backup plan display name and an array of ``BackupRule`` objects, each of which specifies a backup rule.

    Each rule in a backup plan is a separate scheduled task and can back up a different selection of AWS resources.

    For a sample AWS CloudFormation template, see the `AWS Backup Developer Guide <https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html#assigning-resources-cfn>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupplan.html
    :cloudformationResource: AWS::Backup::BackupPlan
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_backup as backup
        
        # backup_options: Any
        
        cfn_backup_plan = backup.CfnBackupPlan(self, "MyCfnBackupPlan",
            backup_plan=backup.CfnBackupPlan.BackupPlanResourceTypeProperty(
                backup_plan_name="backupPlanName",
                backup_plan_rule=[backup.CfnBackupPlan.BackupRuleResourceTypeProperty(
                    rule_name="ruleName",
                    target_backup_vault="targetBackupVault",
        
                    # the properties below are optional
                    completion_window_minutes=123,
                    copy_actions=[backup.CfnBackupPlan.CopyActionResourceTypeProperty(
                        destination_backup_vault_arn="destinationBackupVaultArn",
        
                        # the properties below are optional
                        lifecycle=backup.CfnBackupPlan.LifecycleResourceTypeProperty(
                            delete_after_days=123,
                            move_to_cold_storage_after_days=123,
                            opt_in_to_archive_for_supported_resources=False
                        )
                    )],
                    enable_continuous_backup=False,
                    lifecycle=backup.CfnBackupPlan.LifecycleResourceTypeProperty(
                        delete_after_days=123,
                        move_to_cold_storage_after_days=123,
                        opt_in_to_archive_for_supported_resources=False
                    ),
                    recovery_point_tags={
                        "recovery_point_tags_key": "recoveryPointTags"
                    },
                    schedule_expression="scheduleExpression",
                    schedule_expression_timezone="scheduleExpressionTimezone",
                    start_window_minutes=123
                )],
        
                # the properties below are optional
                advanced_backup_settings=[backup.CfnBackupPlan.AdvancedBackupSettingResourceTypeProperty(
                    backup_options=backup_options,
                    resource_type="resourceType"
                )]
            ),
        
            # the properties below are optional
            backup_plan_tags={
                "backup_plan_tags_key": "backupPlanTags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        backup_plan: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBackupPlan.BackupPlanResourceTypeProperty", typing.Dict[builtins.str, typing.Any]]],
        backup_plan_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param backup_plan: Uniquely identifies the backup plan to be associated with the selection of resources.
        :param backup_plan_tags: The tags to assign to the backup plan.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8250888ac08b345ef300cc4ce53cc267858e31401cdc7b6a427c98f5b05a644a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBackupPlanProps(
            backup_plan=backup_plan, backup_plan_tags=backup_plan_tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff313ad9e84c3475e4286a17d3e066d3b8ff12dcdde29c7a2727bf7529fa7fbb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__629c13605c998df9d353c86512eb681d4a36a976085dd6b817284d7c538366bf)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrBackupPlanArn")
    def attr_backup_plan_arn(self) -> builtins.str:
        '''An Amazon Resource Name (ARN) that uniquely identifies a backup plan;

        for example, ``arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`` .

        :cloudformationAttribute: BackupPlanArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBackupPlanArn"))

    @builtins.property
    @jsii.member(jsii_name="attrBackupPlanId")
    def attr_backup_plan_id(self) -> builtins.str:
        '''Uniquely identifies a backup plan.

        :cloudformationAttribute: BackupPlanId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBackupPlanId"))

    @builtins.property
    @jsii.member(jsii_name="attrVersionId")
    def attr_version_id(self) -> builtins.str:
        '''Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long.

        Version Ids cannot be edited.

        :cloudformationAttribute: VersionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVersionId"))

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
    @jsii.member(jsii_name="backupPlan")
    def backup_plan(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnBackupPlan.BackupPlanResourceTypeProperty"]:
        '''Uniquely identifies the backup plan to be associated with the selection of resources.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBackupPlan.BackupPlanResourceTypeProperty"], jsii.get(self, "backupPlan"))

    @backup_plan.setter
    def backup_plan(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnBackupPlan.BackupPlanResourceTypeProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6bcd3444e7d21cd081d514b722a886bbe4d7a7b6f5d932136467b22b0e106cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupPlan", value)

    @builtins.property
    @jsii.member(jsii_name="backupPlanTags")
    def backup_plan_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags to assign to the backup plan.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "backupPlanTags"))

    @backup_plan_tags.setter
    def backup_plan_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb59689e4858e7d33cb520f2ac89e6fb2e87b5adf8cc0ba009807aac7f9f269b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupPlanTags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_backup.CfnBackupPlan.AdvancedBackupSettingResourceTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "backup_options": "backupOptions",
            "resource_type": "resourceType",
        },
    )
    class AdvancedBackupSettingResourceTypeProperty:
        def __init__(
            self,
            *,
            backup_options: typing.Any,
            resource_type: builtins.str,
        ) -> None:
            '''Specifies an object containing resource type and backup options.

            This is only supported for Windows VSS backups.

            :param backup_options: The backup option for the resource. Each option is a key-value pair. This option is only available for Windows VSS backup jobs. Valid values: Set to ``"WindowsVSS":"enabled"`` to enable the ``WindowsVSS`` backup option and create a Windows VSS backup. Set to ``"WindowsVSS":"disabled"`` to create a regular backup. The ``WindowsVSS`` option is not enabled by default. If you specify an invalid option, you get an ``InvalidParameterValueException`` exception. For more information about Windows VSS backups, see `Creating a VSS-Enabled Windows Backup <https://docs.aws.amazon.com/aws-backup/latest/devguide/windows-backups.html>`_ .
            :param resource_type: The name of a resource type. The only supported resource type is EC2.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-advancedbackupsettingresourcetype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_backup as backup
                
                # backup_options: Any
                
                advanced_backup_setting_resource_type_property = backup.CfnBackupPlan.AdvancedBackupSettingResourceTypeProperty(
                    backup_options=backup_options,
                    resource_type="resourceType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__adac2a2fa454c7ba68def940750a72e610647ccbdd2ff4bbb5b5a2aa0137684c)
                check_type(argname="argument backup_options", value=backup_options, expected_type=type_hints["backup_options"])
                check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "backup_options": backup_options,
                "resource_type": resource_type,
            }

        @builtins.property
        def backup_options(self) -> typing.Any:
            '''The backup option for the resource.

            Each option is a key-value pair. This option is only available for Windows VSS backup jobs.

            Valid values:

            Set to ``"WindowsVSS":"enabled"`` to enable the ``WindowsVSS`` backup option and create a Windows VSS backup.

            Set to ``"WindowsVSS":"disabled"`` to create a regular backup. The ``WindowsVSS`` option is not enabled by default.

            If you specify an invalid option, you get an ``InvalidParameterValueException`` exception.

            For more information about Windows VSS backups, see `Creating a VSS-Enabled Windows Backup <https://docs.aws.amazon.com/aws-backup/latest/devguide/windows-backups.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-advancedbackupsettingresourcetype.html#cfn-backup-backupplan-advancedbackupsettingresourcetype-backupoptions
            '''
            result = self._values.get("backup_options")
            assert result is not None, "Required property 'backup_options' is missing"
            return typing.cast(typing.Any, result)

        @builtins.property
        def resource_type(self) -> builtins.str:
            '''The name of a resource type.

            The only supported resource type is EC2.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-advancedbackupsettingresourcetype.html#cfn-backup-backupplan-advancedbackupsettingresourcetype-resourcetype
            '''
            result = self._values.get("resource_type")
            assert result is not None, "Required property 'resource_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AdvancedBackupSettingResourceTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_backup.CfnBackupPlan.BackupPlanResourceTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "backup_plan_name": "backupPlanName",
            "backup_plan_rule": "backupPlanRule",
            "advanced_backup_settings": "advancedBackupSettings",
        },
    )
    class BackupPlanResourceTypeProperty:
        def __init__(
            self,
            *,
            backup_plan_name: builtins.str,
            backup_plan_rule: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBackupPlan.BackupRuleResourceTypeProperty", typing.Dict[builtins.str, typing.Any]]]]],
            advanced_backup_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBackupPlan.AdvancedBackupSettingResourceTypeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Specifies an object containing properties used to create a backup plan.

            :param backup_plan_name: The display name of a backup plan.
            :param backup_plan_rule: An array of ``BackupRule`` objects, each of which specifies a scheduled task that is used to back up a selection of resources.
            :param advanced_backup_settings: A list of backup options for each resource type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupplanresourcetype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_backup as backup
                
                # backup_options: Any
                
                backup_plan_resource_type_property = backup.CfnBackupPlan.BackupPlanResourceTypeProperty(
                    backup_plan_name="backupPlanName",
                    backup_plan_rule=[backup.CfnBackupPlan.BackupRuleResourceTypeProperty(
                        rule_name="ruleName",
                        target_backup_vault="targetBackupVault",
                
                        # the properties below are optional
                        completion_window_minutes=123,
                        copy_actions=[backup.CfnBackupPlan.CopyActionResourceTypeProperty(
                            destination_backup_vault_arn="destinationBackupVaultArn",
                
                            # the properties below are optional
                            lifecycle=backup.CfnBackupPlan.LifecycleResourceTypeProperty(
                                delete_after_days=123,
                                move_to_cold_storage_after_days=123,
                                opt_in_to_archive_for_supported_resources=False
                            )
                        )],
                        enable_continuous_backup=False,
                        lifecycle=backup.CfnBackupPlan.LifecycleResourceTypeProperty(
                            delete_after_days=123,
                            move_to_cold_storage_after_days=123,
                            opt_in_to_archive_for_supported_resources=False
                        ),
                        recovery_point_tags={
                            "recovery_point_tags_key": "recoveryPointTags"
                        },
                        schedule_expression="scheduleExpression",
                        schedule_expression_timezone="scheduleExpressionTimezone",
                        start_window_minutes=123
                    )],
                
                    # the properties below are optional
                    advanced_backup_settings=[backup.CfnBackupPlan.AdvancedBackupSettingResourceTypeProperty(
                        backup_options=backup_options,
                        resource_type="resourceType"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4fa711ce952ba97854872fd98c8f8e371b8e208c6e6c6d9d96087f413097338f)
                check_type(argname="argument backup_plan_name", value=backup_plan_name, expected_type=type_hints["backup_plan_name"])
                check_type(argname="argument backup_plan_rule", value=backup_plan_rule, expected_type=type_hints["backup_plan_rule"])
                check_type(argname="argument advanced_backup_settings", value=advanced_backup_settings, expected_type=type_hints["advanced_backup_settings"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "backup_plan_name": backup_plan_name,
                "backup_plan_rule": backup_plan_rule,
            }
            if advanced_backup_settings is not None:
                self._values["advanced_backup_settings"] = advanced_backup_settings

        @builtins.property
        def backup_plan_name(self) -> builtins.str:
            '''The display name of a backup plan.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupplanresourcetype.html#cfn-backup-backupplan-backupplanresourcetype-backupplanname
            '''
            result = self._values.get("backup_plan_name")
            assert result is not None, "Required property 'backup_plan_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def backup_plan_rule(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBackupPlan.BackupRuleResourceTypeProperty"]]]:
            '''An array of ``BackupRule`` objects, each of which specifies a scheduled task that is used to back up a selection of resources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupplanresourcetype.html#cfn-backup-backupplan-backupplanresourcetype-backupplanrule
            '''
            result = self._values.get("backup_plan_rule")
            assert result is not None, "Required property 'backup_plan_rule' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBackupPlan.BackupRuleResourceTypeProperty"]]], result)

        @builtins.property
        def advanced_backup_settings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBackupPlan.AdvancedBackupSettingResourceTypeProperty"]]]]:
            '''A list of backup options for each resource type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupplanresourcetype.html#cfn-backup-backupplan-backupplanresourcetype-advancedbackupsettings
            '''
            result = self._values.get("advanced_backup_settings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBackupPlan.AdvancedBackupSettingResourceTypeProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BackupPlanResourceTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_backup.CfnBackupPlan.BackupRuleResourceTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "rule_name": "ruleName",
            "target_backup_vault": "targetBackupVault",
            "completion_window_minutes": "completionWindowMinutes",
            "copy_actions": "copyActions",
            "enable_continuous_backup": "enableContinuousBackup",
            "lifecycle": "lifecycle",
            "recovery_point_tags": "recoveryPointTags",
            "schedule_expression": "scheduleExpression",
            "schedule_expression_timezone": "scheduleExpressionTimezone",
            "start_window_minutes": "startWindowMinutes",
        },
    )
    class BackupRuleResourceTypeProperty:
        def __init__(
            self,
            *,
            rule_name: builtins.str,
            target_backup_vault: builtins.str,
            completion_window_minutes: typing.Optional[jsii.Number] = None,
            copy_actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBackupPlan.CopyActionResourceTypeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            enable_continuous_backup: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            lifecycle: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBackupPlan.LifecycleResourceTypeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            recovery_point_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
            schedule_expression: typing.Optional[builtins.str] = None,
            schedule_expression_timezone: typing.Optional[builtins.str] = None,
            start_window_minutes: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Specifies an object containing properties used to schedule a task to back up a selection of resources.

            :param rule_name: A display name for a backup rule.
            :param target_backup_vault: The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of letters, numbers, and hyphens.
            :param completion_window_minutes: A value in minutes after a backup job is successfully started before it must be completed or it is canceled by AWS Backup .
            :param copy_actions: An array of CopyAction objects, which contains the details of the copy operation.
            :param enable_continuous_backup: Enables continuous backup and point-in-time restores (PITR).
            :param lifecycle: The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. AWS Backup transitions and expires backups automatically according to the lifecycle that you define.
            :param recovery_point_tags: The tags to assign to the resources.
            :param schedule_expression: A CRON expression specifying when AWS Backup initiates a backup job.
            :param schedule_expression_timezone: This is the timezone in which the schedule expression is set. By default, ScheduleExpressions are in UTC. You can modify this to a specified timezone.
            :param start_window_minutes: An optional value that specifies a period of time in minutes after a backup is scheduled before a job is canceled if it doesn't start successfully. If this value is included, it must be at least 60 minutes to avoid errors.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_backup as backup
                
                backup_rule_resource_type_property = backup.CfnBackupPlan.BackupRuleResourceTypeProperty(
                    rule_name="ruleName",
                    target_backup_vault="targetBackupVault",
                
                    # the properties below are optional
                    completion_window_minutes=123,
                    copy_actions=[backup.CfnBackupPlan.CopyActionResourceTypeProperty(
                        destination_backup_vault_arn="destinationBackupVaultArn",
                
                        # the properties below are optional
                        lifecycle=backup.CfnBackupPlan.LifecycleResourceTypeProperty(
                            delete_after_days=123,
                            move_to_cold_storage_after_days=123,
                            opt_in_to_archive_for_supported_resources=False
                        )
                    )],
                    enable_continuous_backup=False,
                    lifecycle=backup.CfnBackupPlan.LifecycleResourceTypeProperty(
                        delete_after_days=123,
                        move_to_cold_storage_after_days=123,
                        opt_in_to_archive_for_supported_resources=False
                    ),
                    recovery_point_tags={
                        "recovery_point_tags_key": "recoveryPointTags"
                    },
                    schedule_expression="scheduleExpression",
                    schedule_expression_timezone="scheduleExpressionTimezone",
                    start_window_minutes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a15d5028e47f5757a8c2319a31ccf993bd398f0a4476991c75f1e1c3b52e84b2)
                check_type(argname="argument rule_name", value=rule_name, expected_type=type_hints["rule_name"])
                check_type(argname="argument target_backup_vault", value=target_backup_vault, expected_type=type_hints["target_backup_vault"])
                check_type(argname="argument completion_window_minutes", value=completion_window_minutes, expected_type=type_hints["completion_window_minutes"])
                check_type(argname="argument copy_actions", value=copy_actions, expected_type=type_hints["copy_actions"])
                check_type(argname="argument enable_continuous_backup", value=enable_continuous_backup, expected_type=type_hints["enable_continuous_backup"])
                check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
                check_type(argname="argument recovery_point_tags", value=recovery_point_tags, expected_type=type_hints["recovery_point_tags"])
                check_type(argname="argument schedule_expression", value=schedule_expression, expected_type=type_hints["schedule_expression"])
                check_type(argname="argument schedule_expression_timezone", value=schedule_expression_timezone, expected_type=type_hints["schedule_expression_timezone"])
                check_type(argname="argument start_window_minutes", value=start_window_minutes, expected_type=type_hints["start_window_minutes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "rule_name": rule_name,
                "target_backup_vault": target_backup_vault,
            }
            if completion_window_minutes is not None:
                self._values["completion_window_minutes"] = completion_window_minutes
            if copy_actions is not None:
                self._values["copy_actions"] = copy_actions
            if enable_continuous_backup is not None:
                self._values["enable_continuous_backup"] = enable_continuous_backup
            if lifecycle is not None:
                self._values["lifecycle"] = lifecycle
            if recovery_point_tags is not None:
                self._values["recovery_point_tags"] = recovery_point_tags
            if schedule_expression is not None:
                self._values["schedule_expression"] = schedule_expression
            if schedule_expression_timezone is not None:
                self._values["schedule_expression_timezone"] = schedule_expression_timezone
            if start_window_minutes is not None:
                self._values["start_window_minutes"] = start_window_minutes

        @builtins.property
        def rule_name(self) -> builtins.str:
            '''A display name for a backup rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-rulename
            '''
            result = self._values.get("rule_name")
            assert result is not None, "Required property 'rule_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def target_backup_vault(self) -> builtins.str:
            '''The name of a logical container where backups are stored.

            Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of letters, numbers, and hyphens.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-targetbackupvault
            '''
            result = self._values.get("target_backup_vault")
            assert result is not None, "Required property 'target_backup_vault' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def completion_window_minutes(self) -> typing.Optional[jsii.Number]:
            '''A value in minutes after a backup job is successfully started before it must be completed or it is canceled by AWS Backup .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-completionwindowminutes
            '''
            result = self._values.get("completion_window_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def copy_actions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBackupPlan.CopyActionResourceTypeProperty"]]]]:
            '''An array of CopyAction objects, which contains the details of the copy operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-copyactions
            '''
            result = self._values.get("copy_actions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBackupPlan.CopyActionResourceTypeProperty"]]]], result)

        @builtins.property
        def enable_continuous_backup(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Enables continuous backup and point-in-time restores (PITR).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-enablecontinuousbackup
            '''
            result = self._values.get("enable_continuous_backup")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def lifecycle(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBackupPlan.LifecycleResourceTypeProperty"]]:
            '''The lifecycle defines when a protected resource is transitioned to cold storage and when it expires.

            AWS Backup transitions and expires backups automatically according to the lifecycle that you define.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-lifecycle
            '''
            result = self._values.get("lifecycle")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBackupPlan.LifecycleResourceTypeProperty"]], result)

        @builtins.property
        def recovery_point_tags(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''The tags to assign to the resources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-recoverypointtags
            '''
            result = self._values.get("recovery_point_tags")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def schedule_expression(self) -> typing.Optional[builtins.str]:
            '''A CRON expression specifying when AWS Backup initiates a backup job.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-scheduleexpression
            '''
            result = self._values.get("schedule_expression")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def schedule_expression_timezone(self) -> typing.Optional[builtins.str]:
            '''This is the timezone in which the schedule expression is set.

            By default, ScheduleExpressions are in UTC. You can modify this to a specified timezone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-scheduleexpressiontimezone
            '''
            result = self._values.get("schedule_expression_timezone")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def start_window_minutes(self) -> typing.Optional[jsii.Number]:
            '''An optional value that specifies a period of time in minutes after a backup is scheduled before a job is canceled if it doesn't start successfully.

            If this value is included, it must be at least 60 minutes to avoid errors.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-startwindowminutes
            '''
            result = self._values.get("start_window_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BackupRuleResourceTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_backup.CfnBackupPlan.CopyActionResourceTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_backup_vault_arn": "destinationBackupVaultArn",
            "lifecycle": "lifecycle",
        },
    )
    class CopyActionResourceTypeProperty:
        def __init__(
            self,
            *,
            destination_backup_vault_arn: builtins.str,
            lifecycle: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBackupPlan.LifecycleResourceTypeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Copies backups created by a backup rule to another vault.

            :param destination_backup_vault_arn: An Amazon Resource Name (ARN) that uniquely identifies the destination backup vault for the copied backup. For example, ``arn:aws:backup:us-east-1:123456789012:vault:aBackupVault.``
            :param lifecycle: Defines when a protected resource is transitioned to cold storage and when it expires. AWS Backup transitions and expires backups automatically according to the lifecycle that you define. If you do not specify a lifecycle, AWS Backup applies the lifecycle policy of the source backup to the destination backup. Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-copyactionresourcetype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_backup as backup
                
                copy_action_resource_type_property = backup.CfnBackupPlan.CopyActionResourceTypeProperty(
                    destination_backup_vault_arn="destinationBackupVaultArn",
                
                    # the properties below are optional
                    lifecycle=backup.CfnBackupPlan.LifecycleResourceTypeProperty(
                        delete_after_days=123,
                        move_to_cold_storage_after_days=123,
                        opt_in_to_archive_for_supported_resources=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b0175b5c6dd7a96151259f5cc498692c56086843795ca19e3f9f696707f1d48a)
                check_type(argname="argument destination_backup_vault_arn", value=destination_backup_vault_arn, expected_type=type_hints["destination_backup_vault_arn"])
                check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination_backup_vault_arn": destination_backup_vault_arn,
            }
            if lifecycle is not None:
                self._values["lifecycle"] = lifecycle

        @builtins.property
        def destination_backup_vault_arn(self) -> builtins.str:
            '''An Amazon Resource Name (ARN) that uniquely identifies the destination backup vault for the copied backup.

            For example, ``arn:aws:backup:us-east-1:123456789012:vault:aBackupVault.``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-copyactionresourcetype.html#cfn-backup-backupplan-copyactionresourcetype-destinationbackupvaultarn
            '''
            result = self._values.get("destination_backup_vault_arn")
            assert result is not None, "Required property 'destination_backup_vault_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def lifecycle(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBackupPlan.LifecycleResourceTypeProperty"]]:
            '''Defines when a protected resource is transitioned to cold storage and when it expires.

            AWS Backup transitions and expires backups automatically according to the lifecycle that you define. If you do not specify a lifecycle, AWS Backup applies the lifecycle policy of the source backup to the destination backup.

            Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-copyactionresourcetype.html#cfn-backup-backupplan-copyactionresourcetype-lifecycle
            '''
            result = self._values.get("lifecycle")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBackupPlan.LifecycleResourceTypeProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CopyActionResourceTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_backup.CfnBackupPlan.LifecycleResourceTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delete_after_days": "deleteAfterDays",
            "move_to_cold_storage_after_days": "moveToColdStorageAfterDays",
            "opt_in_to_archive_for_supported_resources": "optInToArchiveForSupportedResources",
        },
    )
    class LifecycleResourceTypeProperty:
        def __init__(
            self,
            *,
            delete_after_days: typing.Optional[jsii.Number] = None,
            move_to_cold_storage_after_days: typing.Optional[jsii.Number] = None,
            opt_in_to_archive_for_supported_resources: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Specifies an object containing an array of ``Transition`` objects that determine how long in days before a recovery point transitions to cold storage or is deleted.

            :param delete_after_days: Specifies the number of days after creation that a recovery point is deleted. Must be greater than ``MoveToColdStorageAfterDays`` .
            :param move_to_cold_storage_after_days: Specifies the number of days after creation that a recovery point is moved to cold storage.
            :param opt_in_to_archive_for_supported_resources: If the value is true, your backup plan transitions supported resources to archive (cold) storage tier in accordance with your lifecycle settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-lifecycleresourcetype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_backup as backup
                
                lifecycle_resource_type_property = backup.CfnBackupPlan.LifecycleResourceTypeProperty(
                    delete_after_days=123,
                    move_to_cold_storage_after_days=123,
                    opt_in_to_archive_for_supported_resources=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b9cc85d565a0bdd44f5b8b5d29dce7bae38cfd50437c39a049e1b16bd8a24c1e)
                check_type(argname="argument delete_after_days", value=delete_after_days, expected_type=type_hints["delete_after_days"])
                check_type(argname="argument move_to_cold_storage_after_days", value=move_to_cold_storage_after_days, expected_type=type_hints["move_to_cold_storage_after_days"])
                check_type(argname="argument opt_in_to_archive_for_supported_resources", value=opt_in_to_archive_for_supported_resources, expected_type=type_hints["opt_in_to_archive_for_supported_resources"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if delete_after_days is not None:
                self._values["delete_after_days"] = delete_after_days
            if move_to_cold_storage_after_days is not None:
                self._values["move_to_cold_storage_after_days"] = move_to_cold_storage_after_days
            if opt_in_to_archive_for_supported_resources is not None:
                self._values["opt_in_to_archive_for_supported_resources"] = opt_in_to_archive_for_supported_resources

        @builtins.property
        def delete_after_days(self) -> typing.Optional[jsii.Number]:
            '''Specifies the number of days after creation that a recovery point is deleted.

            Must be greater than ``MoveToColdStorageAfterDays`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-lifecycleresourcetype.html#cfn-backup-backupplan-lifecycleresourcetype-deleteafterdays
            '''
            result = self._values.get("delete_after_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def move_to_cold_storage_after_days(self) -> typing.Optional[jsii.Number]:
            '''Specifies the number of days after creation that a recovery point is moved to cold storage.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-lifecycleresourcetype.html#cfn-backup-backupplan-lifecycleresourcetype-movetocoldstorageafterdays
            '''
            result = self._values.get("move_to_cold_storage_after_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def opt_in_to_archive_for_supported_resources(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If the value is true, your backup plan transitions supported resources to archive (cold) storage tier in accordance with your lifecycle settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-lifecycleresourcetype.html#cfn-backup-backupplan-lifecycleresourcetype-optintoarchiveforsupportedresources
            '''
            result = self._values.get("opt_in_to_archive_for_supported_resources")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LifecycleResourceTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_backup.CfnBackupPlanProps",
    jsii_struct_bases=[],
    name_mapping={"backup_plan": "backupPlan", "backup_plan_tags": "backupPlanTags"},
)
class CfnBackupPlanProps:
    def __init__(
        self,
        *,
        backup_plan: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBackupPlan.BackupPlanResourceTypeProperty, typing.Dict[builtins.str, typing.Any]]],
        backup_plan_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnBackupPlan``.

        :param backup_plan: Uniquely identifies the backup plan to be associated with the selection of resources.
        :param backup_plan_tags: The tags to assign to the backup plan.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupplan.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_backup as backup
            
            # backup_options: Any
            
            cfn_backup_plan_props = backup.CfnBackupPlanProps(
                backup_plan=backup.CfnBackupPlan.BackupPlanResourceTypeProperty(
                    backup_plan_name="backupPlanName",
                    backup_plan_rule=[backup.CfnBackupPlan.BackupRuleResourceTypeProperty(
                        rule_name="ruleName",
                        target_backup_vault="targetBackupVault",
            
                        # the properties below are optional
                        completion_window_minutes=123,
                        copy_actions=[backup.CfnBackupPlan.CopyActionResourceTypeProperty(
                            destination_backup_vault_arn="destinationBackupVaultArn",
            
                            # the properties below are optional
                            lifecycle=backup.CfnBackupPlan.LifecycleResourceTypeProperty(
                                delete_after_days=123,
                                move_to_cold_storage_after_days=123,
                                opt_in_to_archive_for_supported_resources=False
                            )
                        )],
                        enable_continuous_backup=False,
                        lifecycle=backup.CfnBackupPlan.LifecycleResourceTypeProperty(
                            delete_after_days=123,
                            move_to_cold_storage_after_days=123,
                            opt_in_to_archive_for_supported_resources=False
                        ),
                        recovery_point_tags={
                            "recovery_point_tags_key": "recoveryPointTags"
                        },
                        schedule_expression="scheduleExpression",
                        schedule_expression_timezone="scheduleExpressionTimezone",
                        start_window_minutes=123
                    )],
            
                    # the properties below are optional
                    advanced_backup_settings=[backup.CfnBackupPlan.AdvancedBackupSettingResourceTypeProperty(
                        backup_options=backup_options,
                        resource_type="resourceType"
                    )]
                ),
            
                # the properties below are optional
                backup_plan_tags={
                    "backup_plan_tags_key": "backupPlanTags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38320d1a2a15443c671b35047636824301e490f9e4406be550e214bb8dea25d8)
            check_type(argname="argument backup_plan", value=backup_plan, expected_type=type_hints["backup_plan"])
            check_type(argname="argument backup_plan_tags", value=backup_plan_tags, expected_type=type_hints["backup_plan_tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "backup_plan": backup_plan,
        }
        if backup_plan_tags is not None:
            self._values["backup_plan_tags"] = backup_plan_tags

    @builtins.property
    def backup_plan(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnBackupPlan.BackupPlanResourceTypeProperty]:
        '''Uniquely identifies the backup plan to be associated with the selection of resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupplan.html#cfn-backup-backupplan-backupplan
        '''
        result = self._values.get("backup_plan")
        assert result is not None, "Required property 'backup_plan' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnBackupPlan.BackupPlanResourceTypeProperty], result)

    @builtins.property
    def backup_plan_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags to assign to the backup plan.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupplan.html#cfn-backup-backupplan-backupplantags
        '''
        result = self._values.get("backup_plan_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBackupPlanProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnBackupSelection(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_backup.CfnBackupSelection",
):
    '''Specifies a set of resources to assign to a backup plan.

    For a sample AWS CloudFormation template, see the `AWS Backup Developer Guide <https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html#assigning-resources-cfn>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupselection.html
    :cloudformationResource: AWS::Backup::BackupSelection
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_backup as backup
        
        # conditions: Any
        
        cfn_backup_selection = backup.CfnBackupSelection(self, "MyCfnBackupSelection",
            backup_plan_id="backupPlanId",
            backup_selection=backup.CfnBackupSelection.BackupSelectionResourceTypeProperty(
                iam_role_arn="iamRoleArn",
                selection_name="selectionName",
        
                # the properties below are optional
                conditions=conditions,
                list_of_tags=[backup.CfnBackupSelection.ConditionResourceTypeProperty(
                    condition_key="conditionKey",
                    condition_type="conditionType",
                    condition_value="conditionValue"
                )],
                not_resources=["notResources"],
                resources=["resources"]
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        backup_plan_id: builtins.str,
        backup_selection: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBackupSelection.BackupSelectionResourceTypeProperty", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param backup_plan_id: Uniquely identifies a backup plan.
        :param backup_selection: Specifies the body of a request to assign a set of resources to a backup plan. It includes an array of resources, an optional array of patterns to exclude resources, an optional role to provide access to the AWS service the resource belongs to, and an optional array of tags used to identify a set of resources.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__436ffdeb945f1d3144a7bb788e19b389a62e6e70ce5e213a46bb8c9ea289c07f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBackupSelectionProps(
            backup_plan_id=backup_plan_id, backup_selection=backup_selection
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b980d8bc69846edd28b19d93b1e66494af7417d2c8bfcc63913b9bf28df47fa)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c986b57932b74d2da2b1f64dec5155c7fdf62e7a88a73fb7936731938fa34e00)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrBackupPlanId")
    def attr_backup_plan_id(self) -> builtins.str:
        '''Uniquely identifies a backup plan.

        :cloudformationAttribute: BackupPlanId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBackupPlanId"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Uniquely identifies the backup selection.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrSelectionId")
    def attr_selection_id(self) -> builtins.str:
        '''Uniquely identifies a request to assign a set of resources to a backup plan.

        :cloudformationAttribute: SelectionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSelectionId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="backupPlanId")
    def backup_plan_id(self) -> builtins.str:
        '''Uniquely identifies a backup plan.'''
        return typing.cast(builtins.str, jsii.get(self, "backupPlanId"))

    @backup_plan_id.setter
    def backup_plan_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb392f817509871513c4b0fafb43edac23006950a5084d282e3b5261b24f5603)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupPlanId", value)

    @builtins.property
    @jsii.member(jsii_name="backupSelection")
    def backup_selection(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnBackupSelection.BackupSelectionResourceTypeProperty"]:
        '''Specifies the body of a request to assign a set of resources to a backup plan.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBackupSelection.BackupSelectionResourceTypeProperty"], jsii.get(self, "backupSelection"))

    @backup_selection.setter
    def backup_selection(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnBackupSelection.BackupSelectionResourceTypeProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c50a31cd4319cd1c025574f4d4937c890776ab110ae28de39672caf7d2e4b86b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupSelection", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_backup.CfnBackupSelection.BackupSelectionResourceTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "iam_role_arn": "iamRoleArn",
            "selection_name": "selectionName",
            "conditions": "conditions",
            "list_of_tags": "listOfTags",
            "not_resources": "notResources",
            "resources": "resources",
        },
    )
    class BackupSelectionResourceTypeProperty:
        def __init__(
            self,
            *,
            iam_role_arn: builtins.str,
            selection_name: builtins.str,
            conditions: typing.Any = None,
            list_of_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBackupSelection.ConditionResourceTypeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            not_resources: typing.Optional[typing.Sequence[builtins.str]] = None,
            resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Specifies an object containing properties used to assign a set of resources to a backup plan.

            :param iam_role_arn: The ARN of the IAM role that AWS Backup uses to authenticate when backing up the target resource; for example, ``arn:aws:iam::123456789012:role/S3Access`` .
            :param selection_name: The display name of a resource selection document.
            :param conditions: A list of conditions that you define to assign resources to your backup plans using tags. For example, ``"StringEquals": { "ConditionKey": "aws:ResourceTag/CreatedByCryo", "ConditionValue": "true" },`` . Condition operators are case sensitive. ``Conditions`` differs from ``ListOfTags`` as follows: - When you specify more than one condition, you only assign the resources that match ALL conditions (using AND logic). - ``Conditions`` supports ``StringEquals`` , ``StringLike`` , ``StringNotEquals`` , and ``StringNotLike`` . ``ListOfTags`` only supports ``StringEquals`` .
            :param list_of_tags: A list of conditions that you define to assign resources to your backup plans using tags. For example, ``"StringEquals": { "ConditionKey": "aws:ResourceTag/CreatedByCryo", "ConditionValue": "true" },`` . Condition operators are case sensitive. ``ListOfTags`` differs from ``Conditions`` as follows: - When you specify more than one condition, you assign all resources that match AT LEAST ONE condition (using OR logic). - ``ListOfTags`` only supports ``StringEquals`` . ``Conditions`` supports ``StringEquals`` , ``StringLike`` , ``StringNotEquals`` , and ``StringNotLike`` .
            :param not_resources: A list of Amazon Resource Names (ARNs) to exclude from a backup plan. The maximum number of ARNs is 500 without wildcards, or 30 ARNs with wildcards. If you need to exclude many resources from a backup plan, consider a different resource selection strategy, such as assigning only one or a few resource types or refining your resource selection using tags.
            :param resources: An array of strings that contain Amazon Resource Names (ARNs) of resources to assign to a backup plan.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_backup as backup
                
                # conditions: Any
                
                backup_selection_resource_type_property = backup.CfnBackupSelection.BackupSelectionResourceTypeProperty(
                    iam_role_arn="iamRoleArn",
                    selection_name="selectionName",
                
                    # the properties below are optional
                    conditions=conditions,
                    list_of_tags=[backup.CfnBackupSelection.ConditionResourceTypeProperty(
                        condition_key="conditionKey",
                        condition_type="conditionType",
                        condition_value="conditionValue"
                    )],
                    not_resources=["notResources"],
                    resources=["resources"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__53f9191660f873982da4ff5df24ce6724761f33be21d9fd33f43da81cca720c0)
                check_type(argname="argument iam_role_arn", value=iam_role_arn, expected_type=type_hints["iam_role_arn"])
                check_type(argname="argument selection_name", value=selection_name, expected_type=type_hints["selection_name"])
                check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
                check_type(argname="argument list_of_tags", value=list_of_tags, expected_type=type_hints["list_of_tags"])
                check_type(argname="argument not_resources", value=not_resources, expected_type=type_hints["not_resources"])
                check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "iam_role_arn": iam_role_arn,
                "selection_name": selection_name,
            }
            if conditions is not None:
                self._values["conditions"] = conditions
            if list_of_tags is not None:
                self._values["list_of_tags"] = list_of_tags
            if not_resources is not None:
                self._values["not_resources"] = not_resources
            if resources is not None:
                self._values["resources"] = resources

        @builtins.property
        def iam_role_arn(self) -> builtins.str:
            '''The ARN of the IAM role that AWS Backup uses to authenticate when backing up the target resource;

            for example, ``arn:aws:iam::123456789012:role/S3Access`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html#cfn-backup-backupselection-backupselectionresourcetype-iamrolearn
            '''
            result = self._values.get("iam_role_arn")
            assert result is not None, "Required property 'iam_role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def selection_name(self) -> builtins.str:
            '''The display name of a resource selection document.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html#cfn-backup-backupselection-backupselectionresourcetype-selectionname
            '''
            result = self._values.get("selection_name")
            assert result is not None, "Required property 'selection_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def conditions(self) -> typing.Any:
            '''A list of conditions that you define to assign resources to your backup plans using tags.

            For example, ``"StringEquals": { "ConditionKey": "aws:ResourceTag/CreatedByCryo", "ConditionValue": "true" },`` . Condition operators are case sensitive.

            ``Conditions`` differs from ``ListOfTags`` as follows:

            - When you specify more than one condition, you only assign the resources that match ALL conditions (using AND logic).
            - ``Conditions`` supports ``StringEquals`` , ``StringLike`` , ``StringNotEquals`` , and ``StringNotLike`` . ``ListOfTags`` only supports ``StringEquals`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html#cfn-backup-backupselection-backupselectionresourcetype-conditions
            '''
            result = self._values.get("conditions")
            return typing.cast(typing.Any, result)

        @builtins.property
        def list_of_tags(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBackupSelection.ConditionResourceTypeProperty"]]]]:
            '''A list of conditions that you define to assign resources to your backup plans using tags.

            For example, ``"StringEquals": { "ConditionKey": "aws:ResourceTag/CreatedByCryo", "ConditionValue": "true" },`` . Condition operators are case sensitive.

            ``ListOfTags`` differs from ``Conditions`` as follows:

            - When you specify more than one condition, you assign all resources that match AT LEAST ONE condition (using OR logic).
            - ``ListOfTags`` only supports ``StringEquals`` . ``Conditions`` supports ``StringEquals`` , ``StringLike`` , ``StringNotEquals`` , and ``StringNotLike`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html#cfn-backup-backupselection-backupselectionresourcetype-listoftags
            '''
            result = self._values.get("list_of_tags")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBackupSelection.ConditionResourceTypeProperty"]]]], result)

        @builtins.property
        def not_resources(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of Amazon Resource Names (ARNs) to exclude from a backup plan.

            The maximum number of ARNs is 500 without wildcards, or 30 ARNs with wildcards.

            If you need to exclude many resources from a backup plan, consider a different resource selection strategy, such as assigning only one or a few resource types or refining your resource selection using tags.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html#cfn-backup-backupselection-backupselectionresourcetype-notresources
            '''
            result = self._values.get("not_resources")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def resources(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An array of strings that contain Amazon Resource Names (ARNs) of resources to assign to a backup plan.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html#cfn-backup-backupselection-backupselectionresourcetype-resources
            '''
            result = self._values.get("resources")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BackupSelectionResourceTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_backup.CfnBackupSelection.ConditionParameterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "condition_key": "conditionKey",
            "condition_value": "conditionValue",
        },
    )
    class ConditionParameterProperty:
        def __init__(
            self,
            *,
            condition_key: typing.Optional[builtins.str] = None,
            condition_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Includes information about tags you define to assign tagged resources to a backup plan.

            Include the prefix ``aws:ResourceTag`` in your tags. For example, ``"aws:ResourceTag/TagKey1": "Value1"`` .

            :param condition_key: The key in a key-value pair. For example, in the tag ``Department: Accounting`` , ``Department`` is the key.
            :param condition_value: The value in a key-value pair. For example, in the tag ``Department: Accounting`` , ``Accounting`` is the value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditionparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_backup as backup
                
                condition_parameter_property = backup.CfnBackupSelection.ConditionParameterProperty(
                    condition_key="conditionKey",
                    condition_value="conditionValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c7fe06535a46bfa87352df9bd09ca629b6962d225411249a065f4ba72647b33a)
                check_type(argname="argument condition_key", value=condition_key, expected_type=type_hints["condition_key"])
                check_type(argname="argument condition_value", value=condition_value, expected_type=type_hints["condition_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if condition_key is not None:
                self._values["condition_key"] = condition_key
            if condition_value is not None:
                self._values["condition_value"] = condition_value

        @builtins.property
        def condition_key(self) -> typing.Optional[builtins.str]:
            '''The key in a key-value pair.

            For example, in the tag ``Department: Accounting`` , ``Department`` is the key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditionparameter.html#cfn-backup-backupselection-conditionparameter-conditionkey
            '''
            result = self._values.get("condition_key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def condition_value(self) -> typing.Optional[builtins.str]:
            '''The value in a key-value pair.

            For example, in the tag ``Department: Accounting`` , ``Accounting`` is the value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditionparameter.html#cfn-backup-backupselection-conditionparameter-conditionvalue
            '''
            result = self._values.get("condition_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConditionParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_backup.CfnBackupSelection.ConditionResourceTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "condition_key": "conditionKey",
            "condition_type": "conditionType",
            "condition_value": "conditionValue",
        },
    )
    class ConditionResourceTypeProperty:
        def __init__(
            self,
            *,
            condition_key: builtins.str,
            condition_type: builtins.str,
            condition_value: builtins.str,
        ) -> None:
            '''Specifies an object that contains an array of triplets made up of a condition type (such as ``STRINGEQUALS`` ), a key, and a value.

            Conditions are used to filter resources in a selection that is assigned to a backup plan.

            :param condition_key: The key in a key-value pair. For example, in ``"Department": "accounting"`` , ``"Department"`` is the key.
            :param condition_type: An operation, such as ``STRINGEQUALS`` , that is applied to a key-value pair used to filter resources in a selection.
            :param condition_value: The value in a key-value pair. For example, in ``"Department": "accounting"`` , ``"accounting"`` is the value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditionresourcetype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_backup as backup
                
                condition_resource_type_property = backup.CfnBackupSelection.ConditionResourceTypeProperty(
                    condition_key="conditionKey",
                    condition_type="conditionType",
                    condition_value="conditionValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__346e9a31a7a4a5ad318acaee89a646b6b23822feb831da857c4c300731df22c9)
                check_type(argname="argument condition_key", value=condition_key, expected_type=type_hints["condition_key"])
                check_type(argname="argument condition_type", value=condition_type, expected_type=type_hints["condition_type"])
                check_type(argname="argument condition_value", value=condition_value, expected_type=type_hints["condition_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "condition_key": condition_key,
                "condition_type": condition_type,
                "condition_value": condition_value,
            }

        @builtins.property
        def condition_key(self) -> builtins.str:
            '''The key in a key-value pair.

            For example, in ``"Department": "accounting"`` , ``"Department"`` is the key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditionresourcetype.html#cfn-backup-backupselection-conditionresourcetype-conditionkey
            '''
            result = self._values.get("condition_key")
            assert result is not None, "Required property 'condition_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def condition_type(self) -> builtins.str:
            '''An operation, such as ``STRINGEQUALS`` , that is applied to a key-value pair used to filter resources in a selection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditionresourcetype.html#cfn-backup-backupselection-conditionresourcetype-conditiontype
            '''
            result = self._values.get("condition_type")
            assert result is not None, "Required property 'condition_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def condition_value(self) -> builtins.str:
            '''The value in a key-value pair.

            For example, in ``"Department": "accounting"`` , ``"accounting"`` is the value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditionresourcetype.html#cfn-backup-backupselection-conditionresourcetype-conditionvalue
            '''
            result = self._values.get("condition_value")
            assert result is not None, "Required property 'condition_value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConditionResourceTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_backup.CfnBackupSelection.ConditionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "string_equals": "stringEquals",
            "string_like": "stringLike",
            "string_not_equals": "stringNotEquals",
            "string_not_like": "stringNotLike",
        },
    )
    class ConditionsProperty:
        def __init__(
            self,
            *,
            string_equals: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBackupSelection.ConditionParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            string_like: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBackupSelection.ConditionParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            string_not_equals: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBackupSelection.ConditionParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            string_not_like: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBackupSelection.ConditionParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Contains information about which resources to include or exclude from a backup plan using their tags.

            Conditions are case sensitive.

            :param string_equals: Filters the values of your tagged resources for only those resources that you tagged with the same value. Also called "exact matching."
            :param string_like: Filters the values of your tagged resources for matching tag values with the use of a wildcard character (*) anywhere in the string. For example, "prod*" or "*rod*" matches the tag value "production".
            :param string_not_equals: Filters the values of your tagged resources for only those resources that you tagged that do not have the same value. Also called "negated matching."
            :param string_not_like: Filters the values of your tagged resources for non-matching tag values with the use of a wildcard character (*) anywhere in the string.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_backup as backup
                
                conditions_property = backup.CfnBackupSelection.ConditionsProperty(
                    string_equals=[backup.CfnBackupSelection.ConditionParameterProperty(
                        condition_key="conditionKey",
                        condition_value="conditionValue"
                    )],
                    string_like=[backup.CfnBackupSelection.ConditionParameterProperty(
                        condition_key="conditionKey",
                        condition_value="conditionValue"
                    )],
                    string_not_equals=[backup.CfnBackupSelection.ConditionParameterProperty(
                        condition_key="conditionKey",
                        condition_value="conditionValue"
                    )],
                    string_not_like=[backup.CfnBackupSelection.ConditionParameterProperty(
                        condition_key="conditionKey",
                        condition_value="conditionValue"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d4989780545fff72ed41947c50d0e49cf85d2cf412bc84422f8757131068aa57)
                check_type(argname="argument string_equals", value=string_equals, expected_type=type_hints["string_equals"])
                check_type(argname="argument string_like", value=string_like, expected_type=type_hints["string_like"])
                check_type(argname="argument string_not_equals", value=string_not_equals, expected_type=type_hints["string_not_equals"])
                check_type(argname="argument string_not_like", value=string_not_like, expected_type=type_hints["string_not_like"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if string_equals is not None:
                self._values["string_equals"] = string_equals
            if string_like is not None:
                self._values["string_like"] = string_like
            if string_not_equals is not None:
                self._values["string_not_equals"] = string_not_equals
            if string_not_like is not None:
                self._values["string_not_like"] = string_not_like

        @builtins.property
        def string_equals(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBackupSelection.ConditionParameterProperty"]]]]:
            '''Filters the values of your tagged resources for only those resources that you tagged with the same value.

            Also called "exact matching."

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditions.html#cfn-backup-backupselection-conditions-stringequals
            '''
            result = self._values.get("string_equals")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBackupSelection.ConditionParameterProperty"]]]], result)

        @builtins.property
        def string_like(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBackupSelection.ConditionParameterProperty"]]]]:
            '''Filters the values of your tagged resources for matching tag values with the use of a wildcard character (*) anywhere in the string.

            For example, "prod*" or "*rod*" matches the tag value "production".

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditions.html#cfn-backup-backupselection-conditions-stringlike
            '''
            result = self._values.get("string_like")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBackupSelection.ConditionParameterProperty"]]]], result)

        @builtins.property
        def string_not_equals(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBackupSelection.ConditionParameterProperty"]]]]:
            '''Filters the values of your tagged resources for only those resources that you tagged that do not have the same value.

            Also called "negated matching."

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditions.html#cfn-backup-backupselection-conditions-stringnotequals
            '''
            result = self._values.get("string_not_equals")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBackupSelection.ConditionParameterProperty"]]]], result)

        @builtins.property
        def string_not_like(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBackupSelection.ConditionParameterProperty"]]]]:
            '''Filters the values of your tagged resources for non-matching tag values with the use of a wildcard character (*) anywhere in the string.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditions.html#cfn-backup-backupselection-conditions-stringnotlike
            '''
            result = self._values.get("string_not_like")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBackupSelection.ConditionParameterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConditionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_backup.CfnBackupSelectionProps",
    jsii_struct_bases=[],
    name_mapping={
        "backup_plan_id": "backupPlanId",
        "backup_selection": "backupSelection",
    },
)
class CfnBackupSelectionProps:
    def __init__(
        self,
        *,
        backup_plan_id: builtins.str,
        backup_selection: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBackupSelection.BackupSelectionResourceTypeProperty, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Properties for defining a ``CfnBackupSelection``.

        :param backup_plan_id: Uniquely identifies a backup plan.
        :param backup_selection: Specifies the body of a request to assign a set of resources to a backup plan. It includes an array of resources, an optional array of patterns to exclude resources, an optional role to provide access to the AWS service the resource belongs to, and an optional array of tags used to identify a set of resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupselection.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_backup as backup
            
            # conditions: Any
            
            cfn_backup_selection_props = backup.CfnBackupSelectionProps(
                backup_plan_id="backupPlanId",
                backup_selection=backup.CfnBackupSelection.BackupSelectionResourceTypeProperty(
                    iam_role_arn="iamRoleArn",
                    selection_name="selectionName",
            
                    # the properties below are optional
                    conditions=conditions,
                    list_of_tags=[backup.CfnBackupSelection.ConditionResourceTypeProperty(
                        condition_key="conditionKey",
                        condition_type="conditionType",
                        condition_value="conditionValue"
                    )],
                    not_resources=["notResources"],
                    resources=["resources"]
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62d83c7c1dd04eb3d32a7eb1179b31577aa76122fb844fd17ddef00d8ef261c9)
            check_type(argname="argument backup_plan_id", value=backup_plan_id, expected_type=type_hints["backup_plan_id"])
            check_type(argname="argument backup_selection", value=backup_selection, expected_type=type_hints["backup_selection"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "backup_plan_id": backup_plan_id,
            "backup_selection": backup_selection,
        }

    @builtins.property
    def backup_plan_id(self) -> builtins.str:
        '''Uniquely identifies a backup plan.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupselection.html#cfn-backup-backupselection-backupplanid
        '''
        result = self._values.get("backup_plan_id")
        assert result is not None, "Required property 'backup_plan_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def backup_selection(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnBackupSelection.BackupSelectionResourceTypeProperty]:
        '''Specifies the body of a request to assign a set of resources to a backup plan.

        It includes an array of resources, an optional array of patterns to exclude resources, an optional role to provide access to the AWS service the resource belongs to, and an optional array of tags used to identify a set of resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupselection.html#cfn-backup-backupselection-backupselection
        '''
        result = self._values.get("backup_selection")
        assert result is not None, "Required property 'backup_selection' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnBackupSelection.BackupSelectionResourceTypeProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBackupSelectionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnBackupVault(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_backup.CfnBackupVault",
):
    '''Creates a logical container where backups are stored.

    A ``CreateBackupVault`` request includes a name, optionally one or more resource tags, an encryption key, and a request ID.

    Do not include sensitive data, such as passport numbers, in the name of a backup vault.

    For a sample AWS CloudFormation template, see the `AWS Backup Developer Guide <https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html#assigning-resources-cfn>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html
    :cloudformationResource: AWS::Backup::BackupVault
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_backup as backup
        
        # access_policy: Any
        
        cfn_backup_vault = backup.CfnBackupVault(self, "MyCfnBackupVault",
            backup_vault_name="backupVaultName",
        
            # the properties below are optional
            access_policy=access_policy,
            backup_vault_tags={
                "backup_vault_tags_key": "backupVaultTags"
            },
            encryption_key_arn="encryptionKeyArn",
            lock_configuration=backup.CfnBackupVault.LockConfigurationTypeProperty(
                min_retention_days=123,
        
                # the properties below are optional
                changeable_for_days=123,
                max_retention_days=123
            ),
            notifications=backup.CfnBackupVault.NotificationObjectTypeProperty(
                backup_vault_events=["backupVaultEvents"],
                sns_topic_arn="snsTopicArn"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        backup_vault_name: builtins.str,
        access_policy: typing.Any = None,
        backup_vault_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        encryption_key_arn: typing.Optional[builtins.str] = None,
        lock_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBackupVault.LockConfigurationTypeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        notifications: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBackupVault.NotificationObjectTypeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param backup_vault_name: The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created.
        :param access_policy: A resource-based policy that is used to manage access permissions on the target backup vault.
        :param backup_vault_tags: The tags to assign to the backup vault.
        :param encryption_key_arn: A server-side encryption key you can specify to encrypt your backups from services that support full AWS Backup management; for example, ``arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`` . If you specify a key, you must specify its ARN, not its alias. If you do not specify a key, AWS Backup creates a KMS key for you by default. To learn which AWS Backup services support full AWS Backup management and how AWS Backup handles encryption for backups from services that do not yet support full AWS Backup , see `Encryption for backups in AWS Backup <https://docs.aws.amazon.com/aws-backup/latest/devguide/encryption.html>`_
        :param lock_configuration: Configuration for `AWS Backup Vault Lock <https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html>`_ .
        :param notifications: The SNS event notifications for the specified backup vault.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91f579bea882f82608d503a3e561568131d8e8e6d825c152c63d596228cb1283)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBackupVaultProps(
            backup_vault_name=backup_vault_name,
            access_policy=access_policy,
            backup_vault_tags=backup_vault_tags,
            encryption_key_arn=encryption_key_arn,
            lock_configuration=lock_configuration,
            notifications=notifications,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5303f64257feccbaac430e6766ee8dd85d8293dcda5a0b514f9128fa193e156)
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
            type_hints = typing.get_type_hints(_typecheckingstub__29e9aaac48a3b884ecef6959c7ece545318b968f28907af6d6f9ef8a7be5eca5)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrBackupVaultArn")
    def attr_backup_vault_arn(self) -> builtins.str:
        '''An Amazon Resource Name (ARN) that uniquely identifies a backup vault;

        for example, ``arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault`` .

        :cloudformationAttribute: BackupVaultArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBackupVaultArn"))

    @builtins.property
    @jsii.member(jsii_name="attrBackupVaultName")
    def attr_backup_vault_name(self) -> builtins.str:
        '''The name of a logical container where backups are stored.

        Backup vaults are identified by names that are unique to the account used to create them and the Region where they are created. They consist of lowercase and uppercase letters, numbers, and hyphens.

        :cloudformationAttribute: BackupVaultName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBackupVaultName"))

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
    @jsii.member(jsii_name="backupVaultName")
    def backup_vault_name(self) -> builtins.str:
        '''The name of a logical container where backups are stored.'''
        return typing.cast(builtins.str, jsii.get(self, "backupVaultName"))

    @backup_vault_name.setter
    def backup_vault_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efe38ab6a95c28a99f2a827659f4327017e61fc72434108ce384f3b817de14be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupVaultName", value)

    @builtins.property
    @jsii.member(jsii_name="accessPolicy")
    def access_policy(self) -> typing.Any:
        '''A resource-based policy that is used to manage access permissions on the target backup vault.'''
        return typing.cast(typing.Any, jsii.get(self, "accessPolicy"))

    @access_policy.setter
    def access_policy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2658b3b3b3e44ef30d5a8cb2081ad397d0fcb37c7f096da80902213d302577e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="backupVaultTags")
    def backup_vault_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags to assign to the backup vault.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "backupVaultTags"))

    @backup_vault_tags.setter
    def backup_vault_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2f59a90eb93017be4632c741610e42551c72baea27b40db6f4ee7a97d80f0dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupVaultTags", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionKeyArn")
    def encryption_key_arn(self) -> typing.Optional[builtins.str]:
        '''A server-side encryption key you can specify to encrypt your backups from services that support full AWS Backup management;'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionKeyArn"))

    @encryption_key_arn.setter
    def encryption_key_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0b723f932eeee018a3da33f56242664a27dbe5da02fc1a2ca3fef2169b24096)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="lockConfiguration")
    def lock_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBackupVault.LockConfigurationTypeProperty"]]:
        '''Configuration for `AWS Backup Vault Lock <https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html>`_ .'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBackupVault.LockConfigurationTypeProperty"]], jsii.get(self, "lockConfiguration"))

    @lock_configuration.setter
    def lock_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBackupVault.LockConfigurationTypeProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c2b8e8d837c9ecececc40d52f27a016b926cd8c10c242b093a3f7cf0d24407a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lockConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="notifications")
    def notifications(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBackupVault.NotificationObjectTypeProperty"]]:
        '''The SNS event notifications for the specified backup vault.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBackupVault.NotificationObjectTypeProperty"]], jsii.get(self, "notifications"))

    @notifications.setter
    def notifications(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBackupVault.NotificationObjectTypeProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd703ee9b654a333d2dac663658fcec508ffab2fc620c932c524dcd0df84e35e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notifications", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_backup.CfnBackupVault.LockConfigurationTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "min_retention_days": "minRetentionDays",
            "changeable_for_days": "changeableForDays",
            "max_retention_days": "maxRetentionDays",
        },
    )
    class LockConfigurationTypeProperty:
        def __init__(
            self,
            *,
            min_retention_days: jsii.Number,
            changeable_for_days: typing.Optional[jsii.Number] = None,
            max_retention_days: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The ``LockConfigurationType`` property type specifies configuration for `AWS Backup Vault Lock <https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html>`_ .

            :param min_retention_days: The AWS Backup Vault Lock configuration that specifies the minimum retention period that the vault retains its recovery points. This setting can be useful if, for example, your organization's policies require you to retain certain data for at least seven years (2555 days). If this parameter is not specified, Vault Lock will not enforce a minimum retention period. If this parameter is specified, any backup or copy job to the vault must have a lifecycle policy with a retention period equal to or longer than the minimum retention period. If the job's retention period is shorter than that minimum retention period, then the vault fails that backup or copy job, and you should either modify your lifecycle settings or use a different vault. Recovery points already saved in the vault prior to Vault Lock are not affected.
            :param changeable_for_days: The AWS Backup Vault Lock configuration that specifies the number of days before the lock date. For example, setting ``ChangeableForDays`` to 30 on Jan. 1, 2022 at 8pm UTC will set the lock date to Jan. 31, 2022 at 8pm UTC. AWS Backup enforces a 72-hour cooling-off period before Vault Lock takes effect and becomes immutable. Therefore, you must set ``ChangeableForDays`` to 3 or greater. Before the lock date, you can delete Vault Lock from the vault using ``DeleteBackupVaultLockConfiguration`` or change the Vault Lock configuration using ``PutBackupVaultLockConfiguration`` . On and after the lock date, the Vault Lock becomes immutable and cannot be changed or deleted. If this parameter is not specified, you can delete Vault Lock from the vault using ``DeleteBackupVaultLockConfiguration`` or change the Vault Lock configuration using ``PutBackupVaultLockConfiguration`` at any time.
            :param max_retention_days: The AWS Backup Vault Lock configuration that specifies the maximum retention period that the vault retains its recovery points. This setting can be useful if, for example, your organization's policies require you to destroy certain data after retaining it for four years (1460 days). If this parameter is not included, Vault Lock does not enforce a maximum retention period on the recovery points in the vault. If this parameter is included without a value, Vault Lock will not enforce a maximum retention period. If this parameter is specified, any backup or copy job to the vault must have a lifecycle policy with a retention period equal to or shorter than the maximum retention period. If the job's retention period is longer than that maximum retention period, then the vault fails the backup or copy job, and you should either modify your lifecycle settings or use a different vault. Recovery points already saved in the vault prior to Vault Lock are not affected.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-lockconfigurationtype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_backup as backup
                
                lock_configuration_type_property = backup.CfnBackupVault.LockConfigurationTypeProperty(
                    min_retention_days=123,
                
                    # the properties below are optional
                    changeable_for_days=123,
                    max_retention_days=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6838c822361ad0f655e1f64f503799de6da67231ac1aa7e8b88f548f690295d8)
                check_type(argname="argument min_retention_days", value=min_retention_days, expected_type=type_hints["min_retention_days"])
                check_type(argname="argument changeable_for_days", value=changeable_for_days, expected_type=type_hints["changeable_for_days"])
                check_type(argname="argument max_retention_days", value=max_retention_days, expected_type=type_hints["max_retention_days"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "min_retention_days": min_retention_days,
            }
            if changeable_for_days is not None:
                self._values["changeable_for_days"] = changeable_for_days
            if max_retention_days is not None:
                self._values["max_retention_days"] = max_retention_days

        @builtins.property
        def min_retention_days(self) -> jsii.Number:
            '''The AWS Backup Vault Lock configuration that specifies the minimum retention period that the vault retains its recovery points.

            This setting can be useful if, for example, your organization's policies require you to retain certain data for at least seven years (2555 days).

            If this parameter is not specified, Vault Lock will not enforce a minimum retention period.

            If this parameter is specified, any backup or copy job to the vault must have a lifecycle policy with a retention period equal to or longer than the minimum retention period. If the job's retention period is shorter than that minimum retention period, then the vault fails that backup or copy job, and you should either modify your lifecycle settings or use a different vault. Recovery points already saved in the vault prior to Vault Lock are not affected.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-lockconfigurationtype.html#cfn-backup-backupvault-lockconfigurationtype-minretentiondays
            '''
            result = self._values.get("min_retention_days")
            assert result is not None, "Required property 'min_retention_days' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def changeable_for_days(self) -> typing.Optional[jsii.Number]:
            '''The AWS Backup Vault Lock configuration that specifies the number of days before the lock date.

            For example, setting ``ChangeableForDays`` to 30 on Jan. 1, 2022 at 8pm UTC will set the lock date to Jan. 31, 2022 at 8pm UTC.

            AWS Backup enforces a 72-hour cooling-off period before Vault Lock takes effect and becomes immutable. Therefore, you must set ``ChangeableForDays`` to 3 or greater.

            Before the lock date, you can delete Vault Lock from the vault using ``DeleteBackupVaultLockConfiguration`` or change the Vault Lock configuration using ``PutBackupVaultLockConfiguration`` . On and after the lock date, the Vault Lock becomes immutable and cannot be changed or deleted.

            If this parameter is not specified, you can delete Vault Lock from the vault using ``DeleteBackupVaultLockConfiguration`` or change the Vault Lock configuration using ``PutBackupVaultLockConfiguration`` at any time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-lockconfigurationtype.html#cfn-backup-backupvault-lockconfigurationtype-changeablefordays
            '''
            result = self._values.get("changeable_for_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_retention_days(self) -> typing.Optional[jsii.Number]:
            '''The AWS Backup Vault Lock configuration that specifies the maximum retention period that the vault retains its recovery points.

            This setting can be useful if, for example, your organization's policies require you to destroy certain data after retaining it for four years (1460 days).

            If this parameter is not included, Vault Lock does not enforce a maximum retention period on the recovery points in the vault. If this parameter is included without a value, Vault Lock will not enforce a maximum retention period.

            If this parameter is specified, any backup or copy job to the vault must have a lifecycle policy with a retention period equal to or shorter than the maximum retention period. If the job's retention period is longer than that maximum retention period, then the vault fails the backup or copy job, and you should either modify your lifecycle settings or use a different vault. Recovery points already saved in the vault prior to Vault Lock are not affected.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-lockconfigurationtype.html#cfn-backup-backupvault-lockconfigurationtype-maxretentiondays
            '''
            result = self._values.get("max_retention_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LockConfigurationTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_backup.CfnBackupVault.NotificationObjectTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "backup_vault_events": "backupVaultEvents",
            "sns_topic_arn": "snsTopicArn",
        },
    )
    class NotificationObjectTypeProperty:
        def __init__(
            self,
            *,
            backup_vault_events: typing.Sequence[builtins.str],
            sns_topic_arn: builtins.str,
        ) -> None:
            '''Specifies an object containing SNS event notification properties for the target backup vault.

            :param backup_vault_events: An array of events that indicate the status of jobs to back up resources to the backup vault. For valid events, see `BackupVaultEvents <https://docs.aws.amazon.com/aws-backup/latest/devguide/API_PutBackupVaultNotifications.html#API_PutBackupVaultNotifications_RequestSyntax>`_ in the *AWS Backup API Guide* .
            :param sns_topic_arn: An ARN that uniquely identifies an Amazon Simple Notification Service (Amazon SNS) topic; for example, ``arn:aws:sns:us-west-2:111122223333:MyTopic`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-notificationobjecttype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_backup as backup
                
                notification_object_type_property = backup.CfnBackupVault.NotificationObjectTypeProperty(
                    backup_vault_events=["backupVaultEvents"],
                    sns_topic_arn="snsTopicArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b1a218026ba958c0d56b8c624f104b73e68fb60c3d3ea03864a8affbd11f0090)
                check_type(argname="argument backup_vault_events", value=backup_vault_events, expected_type=type_hints["backup_vault_events"])
                check_type(argname="argument sns_topic_arn", value=sns_topic_arn, expected_type=type_hints["sns_topic_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "backup_vault_events": backup_vault_events,
                "sns_topic_arn": sns_topic_arn,
            }

        @builtins.property
        def backup_vault_events(self) -> typing.List[builtins.str]:
            '''An array of events that indicate the status of jobs to back up resources to the backup vault.

            For valid events, see `BackupVaultEvents <https://docs.aws.amazon.com/aws-backup/latest/devguide/API_PutBackupVaultNotifications.html#API_PutBackupVaultNotifications_RequestSyntax>`_ in the *AWS Backup API Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-notificationobjecttype.html#cfn-backup-backupvault-notificationobjecttype-backupvaultevents
            '''
            result = self._values.get("backup_vault_events")
            assert result is not None, "Required property 'backup_vault_events' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def sns_topic_arn(self) -> builtins.str:
            '''An ARN that uniquely identifies an Amazon Simple Notification Service (Amazon SNS) topic;

            for example, ``arn:aws:sns:us-west-2:111122223333:MyTopic`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-notificationobjecttype.html#cfn-backup-backupvault-notificationobjecttype-snstopicarn
            '''
            result = self._values.get("sns_topic_arn")
            assert result is not None, "Required property 'sns_topic_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NotificationObjectTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_backup.CfnBackupVaultProps",
    jsii_struct_bases=[],
    name_mapping={
        "backup_vault_name": "backupVaultName",
        "access_policy": "accessPolicy",
        "backup_vault_tags": "backupVaultTags",
        "encryption_key_arn": "encryptionKeyArn",
        "lock_configuration": "lockConfiguration",
        "notifications": "notifications",
    },
)
class CfnBackupVaultProps:
    def __init__(
        self,
        *,
        backup_vault_name: builtins.str,
        access_policy: typing.Any = None,
        backup_vault_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        encryption_key_arn: typing.Optional[builtins.str] = None,
        lock_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBackupVault.LockConfigurationTypeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        notifications: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBackupVault.NotificationObjectTypeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnBackupVault``.

        :param backup_vault_name: The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created.
        :param access_policy: A resource-based policy that is used to manage access permissions on the target backup vault.
        :param backup_vault_tags: The tags to assign to the backup vault.
        :param encryption_key_arn: A server-side encryption key you can specify to encrypt your backups from services that support full AWS Backup management; for example, ``arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`` . If you specify a key, you must specify its ARN, not its alias. If you do not specify a key, AWS Backup creates a KMS key for you by default. To learn which AWS Backup services support full AWS Backup management and how AWS Backup handles encryption for backups from services that do not yet support full AWS Backup , see `Encryption for backups in AWS Backup <https://docs.aws.amazon.com/aws-backup/latest/devguide/encryption.html>`_
        :param lock_configuration: Configuration for `AWS Backup Vault Lock <https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html>`_ .
        :param notifications: The SNS event notifications for the specified backup vault.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_backup as backup
            
            # access_policy: Any
            
            cfn_backup_vault_props = backup.CfnBackupVaultProps(
                backup_vault_name="backupVaultName",
            
                # the properties below are optional
                access_policy=access_policy,
                backup_vault_tags={
                    "backup_vault_tags_key": "backupVaultTags"
                },
                encryption_key_arn="encryptionKeyArn",
                lock_configuration=backup.CfnBackupVault.LockConfigurationTypeProperty(
                    min_retention_days=123,
            
                    # the properties below are optional
                    changeable_for_days=123,
                    max_retention_days=123
                ),
                notifications=backup.CfnBackupVault.NotificationObjectTypeProperty(
                    backup_vault_events=["backupVaultEvents"],
                    sns_topic_arn="snsTopicArn"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8f4cc95a208ae1aaf01a8bfd7ead0ecbd6d7559786be34f0a6087355d66ca28)
            check_type(argname="argument backup_vault_name", value=backup_vault_name, expected_type=type_hints["backup_vault_name"])
            check_type(argname="argument access_policy", value=access_policy, expected_type=type_hints["access_policy"])
            check_type(argname="argument backup_vault_tags", value=backup_vault_tags, expected_type=type_hints["backup_vault_tags"])
            check_type(argname="argument encryption_key_arn", value=encryption_key_arn, expected_type=type_hints["encryption_key_arn"])
            check_type(argname="argument lock_configuration", value=lock_configuration, expected_type=type_hints["lock_configuration"])
            check_type(argname="argument notifications", value=notifications, expected_type=type_hints["notifications"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "backup_vault_name": backup_vault_name,
        }
        if access_policy is not None:
            self._values["access_policy"] = access_policy
        if backup_vault_tags is not None:
            self._values["backup_vault_tags"] = backup_vault_tags
        if encryption_key_arn is not None:
            self._values["encryption_key_arn"] = encryption_key_arn
        if lock_configuration is not None:
            self._values["lock_configuration"] = lock_configuration
        if notifications is not None:
            self._values["notifications"] = notifications

    @builtins.property
    def backup_vault_name(self) -> builtins.str:
        '''The name of a logical container where backups are stored.

        Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-backupvaultname
        '''
        result = self._values.get("backup_vault_name")
        assert result is not None, "Required property 'backup_vault_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_policy(self) -> typing.Any:
        '''A resource-based policy that is used to manage access permissions on the target backup vault.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-accesspolicy
        '''
        result = self._values.get("access_policy")
        return typing.cast(typing.Any, result)

    @builtins.property
    def backup_vault_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags to assign to the backup vault.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-backupvaulttags
        '''
        result = self._values.get("backup_vault_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def encryption_key_arn(self) -> typing.Optional[builtins.str]:
        '''A server-side encryption key you can specify to encrypt your backups from services that support full AWS Backup management;

        for example, ``arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`` . If you specify a key, you must specify its ARN, not its alias. If you do not specify a key, AWS Backup creates a KMS key for you by default.

        To learn which AWS Backup services support full AWS Backup management and how AWS Backup handles encryption for backups from services that do not yet support full AWS Backup , see `Encryption for backups in AWS Backup <https://docs.aws.amazon.com/aws-backup/latest/devguide/encryption.html>`_

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-encryptionkeyarn
        '''
        result = self._values.get("encryption_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lock_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBackupVault.LockConfigurationTypeProperty]]:
        '''Configuration for `AWS Backup Vault Lock <https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-lockconfiguration
        '''
        result = self._values.get("lock_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBackupVault.LockConfigurationTypeProperty]], result)

    @builtins.property
    def notifications(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBackupVault.NotificationObjectTypeProperty]]:
        '''The SNS event notifications for the specified backup vault.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-notifications
        '''
        result = self._values.get("notifications")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBackupVault.NotificationObjectTypeProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBackupVaultProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnFramework(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_backup.CfnFramework",
):
    '''Creates a framework with one or more controls.

    A framework is a collection of controls that you can use to evaluate your backup practices. By using pre-built customizable controls to define your policies, you can evaluate whether your backup practices comply with your policies and which resources are not yet in compliance.

    For a sample AWS CloudFormation template, see the `AWS Backup Developer Guide <https://docs.aws.amazon.com/aws-backup/latest/devguide/bam-cfn-integration.html#bam-cfn-frameworks-template>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html
    :cloudformationResource: AWS::Backup::Framework
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_backup as backup
        
        # control_scope: Any
        
        cfn_framework = backup.CfnFramework(self, "MyCfnFramework",
            framework_controls=[backup.CfnFramework.FrameworkControlProperty(
                control_name="controlName",
        
                # the properties below are optional
                control_input_parameters=[backup.CfnFramework.ControlInputParameterProperty(
                    parameter_name="parameterName",
                    parameter_value="parameterValue"
                )],
                control_scope=control_scope
            )],
        
            # the properties below are optional
            framework_description="frameworkDescription",
            framework_name="frameworkName",
            framework_tags=[CfnTag(
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
        framework_controls: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFramework.FrameworkControlProperty", typing.Dict[builtins.str, typing.Any]]]]],
        framework_description: typing.Optional[builtins.str] = None,
        framework_name: typing.Optional[builtins.str] = None,
        framework_tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param framework_controls: Contains detailed information about all of the controls of a framework. Each framework must contain at least one control.
        :param framework_description: An optional description of the framework with a maximum 1,024 characters.
        :param framework_name: The unique name of a framework. This name is between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).
        :param framework_tags: The tags to assign to your framework.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__762b6f2cf173ed987e2f05e55b691e4e8e14552591e05b26b7f7f4e08e3c739d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFrameworkProps(
            framework_controls=framework_controls,
            framework_description=framework_description,
            framework_name=framework_name,
            framework_tags=framework_tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__772cf75dbb4416fa5340091bf8716f709bcd79a3fef3bf9744a593360d85b617)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5fec0fb3c848f86413b75960fc140604dfee8403702a31925ae61dc8c73e9879)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''The UTC time when you created your framework.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrDeploymentStatus")
    def attr_deployment_status(self) -> builtins.str:
        '''Depolyment status refers to whether your framework has completed deployment.

        This status is usually ``Completed`` , but might also be ``Create in progress`` or another status. For a list of statuses, see `Framework compliance status <https://docs.aws.amazon.com/aws-backup/latest/devguide/viewing-frameworks.html>`_ in the *Developer Guide* .

        :cloudformationAttribute: DeploymentStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDeploymentStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrFrameworkArn")
    def attr_framework_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of your framework.

        :cloudformationAttribute: FrameworkArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFrameworkArn"))

    @builtins.property
    @jsii.member(jsii_name="attrFrameworkStatus")
    def attr_framework_status(self) -> builtins.str:
        '''Framework status refers to whether you have turned on resource tracking for all of your resources.

        This status is ``Active`` when you turn on all resources the framework evaluates. For other statuses and steps to correct them, see `Framework compliance status <https://docs.aws.amazon.com/aws-backup/latest/devguide/viewing-frameworks.html>`_ in the *Developer Guide* .

        :cloudformationAttribute: FrameworkStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFrameworkStatus"))

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
    @jsii.member(jsii_name="frameworkControls")
    def framework_controls(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFramework.FrameworkControlProperty"]]]:
        '''Contains detailed information about all of the controls of a framework.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFramework.FrameworkControlProperty"]]], jsii.get(self, "frameworkControls"))

    @framework_controls.setter
    def framework_controls(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFramework.FrameworkControlProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3915617d48c3c99a3779ed995d74734c2f731d452cc340e149dd92de02e68dc6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frameworkControls", value)

    @builtins.property
    @jsii.member(jsii_name="frameworkDescription")
    def framework_description(self) -> typing.Optional[builtins.str]:
        '''An optional description of the framework with a maximum 1,024 characters.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frameworkDescription"))

    @framework_description.setter
    def framework_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9208446adcef370a60eb7a60602ec6f41c22bd0a8094a6e9276f8c9dc50ce211)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frameworkDescription", value)

    @builtins.property
    @jsii.member(jsii_name="frameworkName")
    def framework_name(self) -> typing.Optional[builtins.str]:
        '''The unique name of a framework.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frameworkName"))

    @framework_name.setter
    def framework_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5b6c11306aa239f885eed40f25fa93c3a57a2c996e35e5a03b218b580a69caf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frameworkName", value)

    @builtins.property
    @jsii.member(jsii_name="frameworkTags")
    def framework_tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to assign to your framework.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "frameworkTags"))

    @framework_tags.setter
    def framework_tags(
        self,
        value: typing.Optional[typing.List[_CfnTag_f6864754]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d4922912c7db9cfb847d446edf6701acea095c2d0fefb7def73f3da3aa1cc1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frameworkTags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_backup.CfnFramework.ControlInputParameterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "parameter_name": "parameterName",
            "parameter_value": "parameterValue",
        },
    )
    class ControlInputParameterProperty:
        def __init__(
            self,
            *,
            parameter_name: builtins.str,
            parameter_value: builtins.str,
        ) -> None:
            '''The parameters for a control.

            A control can have zero, one, or more than one parameter. An example of a control with two parameters is: "backup plan frequency is at least ``daily`` and the retention period is at least ``1 year`` ". The first parameter is ``daily`` . The second parameter is ``1 year`` .

            :param parameter_name: The name of a parameter, for example, ``BackupPlanFrequency`` .
            :param parameter_value: The value of parameter, for example, ``hourly`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-controlinputparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_backup as backup
                
                control_input_parameter_property = backup.CfnFramework.ControlInputParameterProperty(
                    parameter_name="parameterName",
                    parameter_value="parameterValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dab5ceb07bfb68ba9a8118e37c2455f99ed12c16a7af1c7b9630695eaee92261)
                check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
                check_type(argname="argument parameter_value", value=parameter_value, expected_type=type_hints["parameter_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "parameter_name": parameter_name,
                "parameter_value": parameter_value,
            }

        @builtins.property
        def parameter_name(self) -> builtins.str:
            '''The name of a parameter, for example, ``BackupPlanFrequency`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-controlinputparameter.html#cfn-backup-framework-controlinputparameter-parametername
            '''
            result = self._values.get("parameter_name")
            assert result is not None, "Required property 'parameter_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def parameter_value(self) -> builtins.str:
            '''The value of parameter, for example, ``hourly`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-controlinputparameter.html#cfn-backup-framework-controlinputparameter-parametervalue
            '''
            result = self._values.get("parameter_value")
            assert result is not None, "Required property 'parameter_value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ControlInputParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_backup.CfnFramework.ControlScopeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "compliance_resource_ids": "complianceResourceIds",
            "compliance_resource_types": "complianceResourceTypes",
            "tags": "tags",
        },
    )
    class ControlScopeProperty:
        def __init__(
            self,
            *,
            compliance_resource_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            compliance_resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
            tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A framework consists of one or more controls.

            Each control has its own control scope. The control scope can include one or more resource types, a combination of a tag key and value, or a combination of one resource type and one resource ID. If no scope is specified, evaluations for the rule are triggered when any resource in your recording group changes in configuration.
            .. epigraph::

               To set a control scope that includes all of a particular resource, leave the ``ControlScope`` empty or do not pass it when calling ``CreateFramework`` .

            :param compliance_resource_ids: The ID of the only AWS resource that you want your control scope to contain.
            :param compliance_resource_types: Describes whether the control scope includes one or more types of resources, such as ``EFS`` or ``RDS`` .
            :param tags: The tag key-value pair applied to those AWS resources that you want to trigger an evaluation for a rule. A maximum of one key-value pair can be provided. The tag value is optional, but it cannot be an empty string if you are creating or editing a framework from the console (though the value can be an empty string when included in a CloudFormation template). The structure to assign a tag is: ``[{"Key":"string","Value":"string"}]`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-controlscope.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_backup as backup
                
                control_scope_property = backup.CfnFramework.ControlScopeProperty(
                    compliance_resource_ids=["complianceResourceIds"],
                    compliance_resource_types=["complianceResourceTypes"],
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f2f11947bed37971122729e32bbef595427b4ad564167fe2e94024e5751025f0)
                check_type(argname="argument compliance_resource_ids", value=compliance_resource_ids, expected_type=type_hints["compliance_resource_ids"])
                check_type(argname="argument compliance_resource_types", value=compliance_resource_types, expected_type=type_hints["compliance_resource_types"])
                check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if compliance_resource_ids is not None:
                self._values["compliance_resource_ids"] = compliance_resource_ids
            if compliance_resource_types is not None:
                self._values["compliance_resource_types"] = compliance_resource_types
            if tags is not None:
                self._values["tags"] = tags

        @builtins.property
        def compliance_resource_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The ID of the only AWS resource that you want your control scope to contain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-controlscope.html#cfn-backup-framework-controlscope-complianceresourceids
            '''
            result = self._values.get("compliance_resource_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def compliance_resource_types(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''Describes whether the control scope includes one or more types of resources, such as ``EFS`` or ``RDS`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-controlscope.html#cfn-backup-framework-controlscope-complianceresourcetypes
            '''
            result = self._values.get("compliance_resource_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
            '''The tag key-value pair applied to those AWS resources that you want to trigger an evaluation for a rule.

            A maximum of one key-value pair can be provided. The tag value is optional, but it cannot be an empty string if you are creating or editing a framework from the console (though the value can be an empty string when included in a CloudFormation template).

            The structure to assign a tag is: ``[{"Key":"string","Value":"string"}]`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-controlscope.html#cfn-backup-framework-controlscope-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ControlScopeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_backup.CfnFramework.FrameworkControlProperty",
        jsii_struct_bases=[],
        name_mapping={
            "control_name": "controlName",
            "control_input_parameters": "controlInputParameters",
            "control_scope": "controlScope",
        },
    )
    class FrameworkControlProperty:
        def __init__(
            self,
            *,
            control_name: builtins.str,
            control_input_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFramework.ControlInputParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            control_scope: typing.Any = None,
        ) -> None:
            '''Contains detailed information about all of the controls of a framework.

            Each framework must contain at least one control.

            :param control_name: The name of a control. This name is between 1 and 256 characters.
            :param control_input_parameters: The name/value pairs.
            :param control_scope: The scope of a control. The control scope defines what the control will evaluate. Three examples of control scopes are: a specific backup plan, all backup plans with a specific tag, or all backup plans. For more information, see ```ControlScope`` . <https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ControlScope.html>`_

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-frameworkcontrol.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_backup as backup
                
                # control_scope: Any
                
                framework_control_property = backup.CfnFramework.FrameworkControlProperty(
                    control_name="controlName",
                
                    # the properties below are optional
                    control_input_parameters=[backup.CfnFramework.ControlInputParameterProperty(
                        parameter_name="parameterName",
                        parameter_value="parameterValue"
                    )],
                    control_scope=control_scope
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2629d2cfa8ee3e24a49017e656aec6745967bedbc91fb85dae3a38dfe31fbb23)
                check_type(argname="argument control_name", value=control_name, expected_type=type_hints["control_name"])
                check_type(argname="argument control_input_parameters", value=control_input_parameters, expected_type=type_hints["control_input_parameters"])
                check_type(argname="argument control_scope", value=control_scope, expected_type=type_hints["control_scope"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "control_name": control_name,
            }
            if control_input_parameters is not None:
                self._values["control_input_parameters"] = control_input_parameters
            if control_scope is not None:
                self._values["control_scope"] = control_scope

        @builtins.property
        def control_name(self) -> builtins.str:
            '''The name of a control.

            This name is between 1 and 256 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-frameworkcontrol.html#cfn-backup-framework-frameworkcontrol-controlname
            '''
            result = self._values.get("control_name")
            assert result is not None, "Required property 'control_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def control_input_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFramework.ControlInputParameterProperty"]]]]:
            '''The name/value pairs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-frameworkcontrol.html#cfn-backup-framework-frameworkcontrol-controlinputparameters
            '''
            result = self._values.get("control_input_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFramework.ControlInputParameterProperty"]]]], result)

        @builtins.property
        def control_scope(self) -> typing.Any:
            '''The scope of a control.

            The control scope defines what the control will evaluate. Three examples of control scopes are: a specific backup plan, all backup plans with a specific tag, or all backup plans.

            For more information, see ```ControlScope`` . <https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ControlScope.html>`_

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-frameworkcontrol.html#cfn-backup-framework-frameworkcontrol-controlscope
            '''
            result = self._values.get("control_scope")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FrameworkControlProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_backup.CfnFrameworkProps",
    jsii_struct_bases=[],
    name_mapping={
        "framework_controls": "frameworkControls",
        "framework_description": "frameworkDescription",
        "framework_name": "frameworkName",
        "framework_tags": "frameworkTags",
    },
)
class CfnFrameworkProps:
    def __init__(
        self,
        *,
        framework_controls: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFramework.FrameworkControlProperty, typing.Dict[builtins.str, typing.Any]]]]],
        framework_description: typing.Optional[builtins.str] = None,
        framework_name: typing.Optional[builtins.str] = None,
        framework_tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFramework``.

        :param framework_controls: Contains detailed information about all of the controls of a framework. Each framework must contain at least one control.
        :param framework_description: An optional description of the framework with a maximum 1,024 characters.
        :param framework_name: The unique name of a framework. This name is between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).
        :param framework_tags: The tags to assign to your framework.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_backup as backup
            
            # control_scope: Any
            
            cfn_framework_props = backup.CfnFrameworkProps(
                framework_controls=[backup.CfnFramework.FrameworkControlProperty(
                    control_name="controlName",
            
                    # the properties below are optional
                    control_input_parameters=[backup.CfnFramework.ControlInputParameterProperty(
                        parameter_name="parameterName",
                        parameter_value="parameterValue"
                    )],
                    control_scope=control_scope
                )],
            
                # the properties below are optional
                framework_description="frameworkDescription",
                framework_name="frameworkName",
                framework_tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a04013c0cacc7cf95b5f7954572128dbc2c4529bb364b61a38c324e4d52b5fd7)
            check_type(argname="argument framework_controls", value=framework_controls, expected_type=type_hints["framework_controls"])
            check_type(argname="argument framework_description", value=framework_description, expected_type=type_hints["framework_description"])
            check_type(argname="argument framework_name", value=framework_name, expected_type=type_hints["framework_name"])
            check_type(argname="argument framework_tags", value=framework_tags, expected_type=type_hints["framework_tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "framework_controls": framework_controls,
        }
        if framework_description is not None:
            self._values["framework_description"] = framework_description
        if framework_name is not None:
            self._values["framework_name"] = framework_name
        if framework_tags is not None:
            self._values["framework_tags"] = framework_tags

    @builtins.property
    def framework_controls(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFramework.FrameworkControlProperty]]]:
        '''Contains detailed information about all of the controls of a framework.

        Each framework must contain at least one control.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html#cfn-backup-framework-frameworkcontrols
        '''
        result = self._values.get("framework_controls")
        assert result is not None, "Required property 'framework_controls' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFramework.FrameworkControlProperty]]], result)

    @builtins.property
    def framework_description(self) -> typing.Optional[builtins.str]:
        '''An optional description of the framework with a maximum 1,024 characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html#cfn-backup-framework-frameworkdescription
        '''
        result = self._values.get("framework_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def framework_name(self) -> typing.Optional[builtins.str]:
        '''The unique name of a framework.

        This name is between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html#cfn-backup-framework-frameworkname
        '''
        result = self._values.get("framework_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def framework_tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to assign to your framework.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html#cfn-backup-framework-frameworktags
        '''
        result = self._values.get("framework_tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFrameworkProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnReportPlan(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_backup.CfnReportPlan",
):
    '''Creates a report plan.

    A report plan is a document that contains information about the contents of the report and where AWS Backup will deliver it.

    If you call ``CreateReportPlan`` with a plan that already exists, you receive an ``AlreadyExistsException`` exception.

    For a sample AWS CloudFormation template, see the `AWS Backup Developer Guide <https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html#assigning-resources-cfn>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html
    :cloudformationResource: AWS::Backup::ReportPlan
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_backup as backup
        
        # report_delivery_channel: Any
        # report_setting: Any
        
        cfn_report_plan = backup.CfnReportPlan(self, "MyCfnReportPlan",
            report_delivery_channel=report_delivery_channel,
            report_setting=report_setting,
        
            # the properties below are optional
            report_plan_description="reportPlanDescription",
            report_plan_name="reportPlanName",
            report_plan_tags=[CfnTag(
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
        report_delivery_channel: typing.Any,
        report_setting: typing.Any,
        report_plan_description: typing.Optional[builtins.str] = None,
        report_plan_name: typing.Optional[builtins.str] = None,
        report_plan_tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param report_delivery_channel: Contains information about where and how to deliver your reports, specifically your Amazon S3 bucket name, S3 key prefix, and the formats of your reports.
        :param report_setting: Identifies the report template for the report. Reports are built using a report template. The report templates are:. ``RESOURCE_COMPLIANCE_REPORT | CONTROL_COMPLIANCE_REPORT | BACKUP_JOB_REPORT | COPY_JOB_REPORT | RESTORE_JOB_REPORT`` If the report template is ``RESOURCE_COMPLIANCE_REPORT`` or ``CONTROL_COMPLIANCE_REPORT`` , this API resource also describes the report coverage by AWS Regions and frameworks.
        :param report_plan_description: An optional description of the report plan with a maximum 1,024 characters.
        :param report_plan_name: The unique name of the report plan. This name is between 1 and 256 characters starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).
        :param report_plan_tags: The tags to assign to your report plan.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c6528de906751786b24f01244334abf14ddb763be763a416a6d4f3c8b779828)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnReportPlanProps(
            report_delivery_channel=report_delivery_channel,
            report_setting=report_setting,
            report_plan_description=report_plan_description,
            report_plan_name=report_plan_name,
            report_plan_tags=report_plan_tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f16e67dc9d6ebba3468d37c10baab99ff7e531b9adb1ec5e7f3259c7c6f7f9aa)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9c7b68d11abde2aa0d9a37b0c93b72ae7b52fee9f08d4f38397745e4d72f524f)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrReportPlanArn")
    def attr_report_plan_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of your report plan.

        :cloudformationAttribute: ReportPlanArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrReportPlanArn"))

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
    @jsii.member(jsii_name="reportDeliveryChannel")
    def report_delivery_channel(self) -> typing.Any:
        '''Contains information about where and how to deliver your reports, specifically your Amazon S3 bucket name, S3 key prefix, and the formats of your reports.'''
        return typing.cast(typing.Any, jsii.get(self, "reportDeliveryChannel"))

    @report_delivery_channel.setter
    def report_delivery_channel(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f59e4877274d33fdd0b7b625f974f6963731efadb02eb1735d077c10708f32a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reportDeliveryChannel", value)

    @builtins.property
    @jsii.member(jsii_name="reportSetting")
    def report_setting(self) -> typing.Any:
        '''Identifies the report template for the report.

        Reports are built using a report template. The report templates are:.
        '''
        return typing.cast(typing.Any, jsii.get(self, "reportSetting"))

    @report_setting.setter
    def report_setting(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f16d9fa0a96dbb11b2af025cb683de73134d878e6b6aa892388da1b0ba219734)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reportSetting", value)

    @builtins.property
    @jsii.member(jsii_name="reportPlanDescription")
    def report_plan_description(self) -> typing.Optional[builtins.str]:
        '''An optional description of the report plan with a maximum 1,024 characters.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "reportPlanDescription"))

    @report_plan_description.setter
    def report_plan_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd7915156dce61fe52d1f2c30121d3b6944167aaa29a3d385bd84dc1027de25a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reportPlanDescription", value)

    @builtins.property
    @jsii.member(jsii_name="reportPlanName")
    def report_plan_name(self) -> typing.Optional[builtins.str]:
        '''The unique name of the report plan.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "reportPlanName"))

    @report_plan_name.setter
    def report_plan_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ac2566ae00a72a2736504779f108399d133fb5744a76f8690cb6e5a7a85a8bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reportPlanName", value)

    @builtins.property
    @jsii.member(jsii_name="reportPlanTags")
    def report_plan_tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to assign to your report plan.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "reportPlanTags"))

    @report_plan_tags.setter
    def report_plan_tags(
        self,
        value: typing.Optional[typing.List[_CfnTag_f6864754]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16e4bb4b012408e08ab26526c9837368cc6121e55f663b4a10170c9edb8466f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reportPlanTags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_backup.CfnReportPlan.ReportDeliveryChannelProperty",
        jsii_struct_bases=[],
        name_mapping={
            "s3_bucket_name": "s3BucketName",
            "formats": "formats",
            "s3_key_prefix": "s3KeyPrefix",
        },
    )
    class ReportDeliveryChannelProperty:
        def __init__(
            self,
            *,
            s3_bucket_name: builtins.str,
            formats: typing.Optional[typing.Sequence[builtins.str]] = None,
            s3_key_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains information from your report plan about where to deliver your reports, specifically your Amazon S3 bucket name, S3 key prefix, and the formats of your reports.

            :param s3_bucket_name: The unique name of the S3 bucket that receives your reports.
            :param formats: The format of your reports: ``CSV`` , ``JSON`` , or both. If not specified, the default format is ``CSV`` .
            :param s3_key_prefix: The prefix for where AWS Backup Audit Manager delivers your reports to Amazon S3. The prefix is this part of the following path: s3://your-bucket-name/ ``prefix`` /Backup/us-west-2/year/month/day/report-name. If not specified, there is no prefix.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-reportplan-reportdeliverychannel.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_backup as backup
                
                report_delivery_channel_property = backup.CfnReportPlan.ReportDeliveryChannelProperty(
                    s3_bucket_name="s3BucketName",
                
                    # the properties below are optional
                    formats=["formats"],
                    s3_key_prefix="s3KeyPrefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c24b871d5606676d6a9c03353da61f5c6dd25f1faa08da3b2350be2abc2960e9)
                check_type(argname="argument s3_bucket_name", value=s3_bucket_name, expected_type=type_hints["s3_bucket_name"])
                check_type(argname="argument formats", value=formats, expected_type=type_hints["formats"])
                check_type(argname="argument s3_key_prefix", value=s3_key_prefix, expected_type=type_hints["s3_key_prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "s3_bucket_name": s3_bucket_name,
            }
            if formats is not None:
                self._values["formats"] = formats
            if s3_key_prefix is not None:
                self._values["s3_key_prefix"] = s3_key_prefix

        @builtins.property
        def s3_bucket_name(self) -> builtins.str:
            '''The unique name of the S3 bucket that receives your reports.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-reportplan-reportdeliverychannel.html#cfn-backup-reportplan-reportdeliverychannel-s3bucketname
            '''
            result = self._values.get("s3_bucket_name")
            assert result is not None, "Required property 's3_bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def formats(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The format of your reports: ``CSV`` , ``JSON`` , or both.

            If not specified, the default format is ``CSV`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-reportplan-reportdeliverychannel.html#cfn-backup-reportplan-reportdeliverychannel-formats
            '''
            result = self._values.get("formats")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def s3_key_prefix(self) -> typing.Optional[builtins.str]:
            '''The prefix for where AWS Backup Audit Manager delivers your reports to Amazon S3.

            The prefix is this part of the following path: s3://your-bucket-name/ ``prefix`` /Backup/us-west-2/year/month/day/report-name. If not specified, there is no prefix.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-reportplan-reportdeliverychannel.html#cfn-backup-reportplan-reportdeliverychannel-s3keyprefix
            '''
            result = self._values.get("s3_key_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReportDeliveryChannelProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_backup.CfnReportPlan.ReportSettingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "report_template": "reportTemplate",
            "accounts": "accounts",
            "framework_arns": "frameworkArns",
            "organization_units": "organizationUnits",
            "regions": "regions",
        },
    )
    class ReportSettingProperty:
        def __init__(
            self,
            *,
            report_template: builtins.str,
            accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
            framework_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
            organization_units: typing.Optional[typing.Sequence[builtins.str]] = None,
            regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Contains detailed information about a report setting.

            :param report_template: Identifies the report template for the report. Reports are built using a report template. The report templates are:. ``RESOURCE_COMPLIANCE_REPORT | CONTROL_COMPLIANCE_REPORT | BACKUP_JOB_REPORT | COPY_JOB_REPORT | RESTORE_JOB_REPORT``
            :param accounts: These are the accounts to be included in the report. Use string value of ``ROOT`` to include all organizational units.
            :param framework_arns: The Amazon Resource Names (ARNs) of the frameworks a report covers.
            :param organization_units: These are the Organizational Units to be included in the report.
            :param regions: These are the Regions to be included in the report. Use the wildcard as the string value to include all Regions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-reportplan-reportsetting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_backup as backup
                
                report_setting_property = backup.CfnReportPlan.ReportSettingProperty(
                    report_template="reportTemplate",
                
                    # the properties below are optional
                    accounts=["accounts"],
                    framework_arns=["frameworkArns"],
                    organization_units=["organizationUnits"],
                    regions=["regions"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f82410dd1600e96bdbb1b09d2f427b262b59db1aee2a2d8a69b04a7c45213f39)
                check_type(argname="argument report_template", value=report_template, expected_type=type_hints["report_template"])
                check_type(argname="argument accounts", value=accounts, expected_type=type_hints["accounts"])
                check_type(argname="argument framework_arns", value=framework_arns, expected_type=type_hints["framework_arns"])
                check_type(argname="argument organization_units", value=organization_units, expected_type=type_hints["organization_units"])
                check_type(argname="argument regions", value=regions, expected_type=type_hints["regions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "report_template": report_template,
            }
            if accounts is not None:
                self._values["accounts"] = accounts
            if framework_arns is not None:
                self._values["framework_arns"] = framework_arns
            if organization_units is not None:
                self._values["organization_units"] = organization_units
            if regions is not None:
                self._values["regions"] = regions

        @builtins.property
        def report_template(self) -> builtins.str:
            '''Identifies the report template for the report. Reports are built using a report template. The report templates are:.

            ``RESOURCE_COMPLIANCE_REPORT | CONTROL_COMPLIANCE_REPORT | BACKUP_JOB_REPORT | COPY_JOB_REPORT | RESTORE_JOB_REPORT``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-reportplan-reportsetting.html#cfn-backup-reportplan-reportsetting-reporttemplate
            '''
            result = self._values.get("report_template")
            assert result is not None, "Required property 'report_template' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def accounts(self) -> typing.Optional[typing.List[builtins.str]]:
            '''These are the accounts to be included in the report.

            Use string value of ``ROOT`` to include all organizational units.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-reportplan-reportsetting.html#cfn-backup-reportplan-reportsetting-accounts
            '''
            result = self._values.get("accounts")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def framework_arns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The Amazon Resource Names (ARNs) of the frameworks a report covers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-reportplan-reportsetting.html#cfn-backup-reportplan-reportsetting-frameworkarns
            '''
            result = self._values.get("framework_arns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def organization_units(self) -> typing.Optional[typing.List[builtins.str]]:
            '''These are the Organizational Units to be included in the report.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-reportplan-reportsetting.html#cfn-backup-reportplan-reportsetting-organizationunits
            '''
            result = self._values.get("organization_units")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def regions(self) -> typing.Optional[typing.List[builtins.str]]:
            '''These are the Regions to be included in the report.

            Use the wildcard as the string value to include all Regions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-reportplan-reportsetting.html#cfn-backup-reportplan-reportsetting-regions
            '''
            result = self._values.get("regions")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReportSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_backup.CfnReportPlanProps",
    jsii_struct_bases=[],
    name_mapping={
        "report_delivery_channel": "reportDeliveryChannel",
        "report_setting": "reportSetting",
        "report_plan_description": "reportPlanDescription",
        "report_plan_name": "reportPlanName",
        "report_plan_tags": "reportPlanTags",
    },
)
class CfnReportPlanProps:
    def __init__(
        self,
        *,
        report_delivery_channel: typing.Any,
        report_setting: typing.Any,
        report_plan_description: typing.Optional[builtins.str] = None,
        report_plan_name: typing.Optional[builtins.str] = None,
        report_plan_tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnReportPlan``.

        :param report_delivery_channel: Contains information about where and how to deliver your reports, specifically your Amazon S3 bucket name, S3 key prefix, and the formats of your reports.
        :param report_setting: Identifies the report template for the report. Reports are built using a report template. The report templates are:. ``RESOURCE_COMPLIANCE_REPORT | CONTROL_COMPLIANCE_REPORT | BACKUP_JOB_REPORT | COPY_JOB_REPORT | RESTORE_JOB_REPORT`` If the report template is ``RESOURCE_COMPLIANCE_REPORT`` or ``CONTROL_COMPLIANCE_REPORT`` , this API resource also describes the report coverage by AWS Regions and frameworks.
        :param report_plan_description: An optional description of the report plan with a maximum 1,024 characters.
        :param report_plan_name: The unique name of the report plan. This name is between 1 and 256 characters starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).
        :param report_plan_tags: The tags to assign to your report plan.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_backup as backup
            
            # report_delivery_channel: Any
            # report_setting: Any
            
            cfn_report_plan_props = backup.CfnReportPlanProps(
                report_delivery_channel=report_delivery_channel,
                report_setting=report_setting,
            
                # the properties below are optional
                report_plan_description="reportPlanDescription",
                report_plan_name="reportPlanName",
                report_plan_tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afbe22eade35dfb4647750a128ae7ae610bb82584420423ce86400329eeb84d9)
            check_type(argname="argument report_delivery_channel", value=report_delivery_channel, expected_type=type_hints["report_delivery_channel"])
            check_type(argname="argument report_setting", value=report_setting, expected_type=type_hints["report_setting"])
            check_type(argname="argument report_plan_description", value=report_plan_description, expected_type=type_hints["report_plan_description"])
            check_type(argname="argument report_plan_name", value=report_plan_name, expected_type=type_hints["report_plan_name"])
            check_type(argname="argument report_plan_tags", value=report_plan_tags, expected_type=type_hints["report_plan_tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "report_delivery_channel": report_delivery_channel,
            "report_setting": report_setting,
        }
        if report_plan_description is not None:
            self._values["report_plan_description"] = report_plan_description
        if report_plan_name is not None:
            self._values["report_plan_name"] = report_plan_name
        if report_plan_tags is not None:
            self._values["report_plan_tags"] = report_plan_tags

    @builtins.property
    def report_delivery_channel(self) -> typing.Any:
        '''Contains information about where and how to deliver your reports, specifically your Amazon S3 bucket name, S3 key prefix, and the formats of your reports.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html#cfn-backup-reportplan-reportdeliverychannel
        '''
        result = self._values.get("report_delivery_channel")
        assert result is not None, "Required property 'report_delivery_channel' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def report_setting(self) -> typing.Any:
        '''Identifies the report template for the report. Reports are built using a report template. The report templates are:.

        ``RESOURCE_COMPLIANCE_REPORT | CONTROL_COMPLIANCE_REPORT | BACKUP_JOB_REPORT | COPY_JOB_REPORT | RESTORE_JOB_REPORT``

        If the report template is ``RESOURCE_COMPLIANCE_REPORT`` or ``CONTROL_COMPLIANCE_REPORT`` , this API resource also describes the report coverage by AWS Regions and frameworks.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html#cfn-backup-reportplan-reportsetting
        '''
        result = self._values.get("report_setting")
        assert result is not None, "Required property 'report_setting' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def report_plan_description(self) -> typing.Optional[builtins.str]:
        '''An optional description of the report plan with a maximum 1,024 characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html#cfn-backup-reportplan-reportplandescription
        '''
        result = self._values.get("report_plan_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def report_plan_name(self) -> typing.Optional[builtins.str]:
        '''The unique name of the report plan.

        This name is between 1 and 256 characters starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html#cfn-backup-reportplan-reportplanname
        '''
        result = self._values.get("report_plan_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def report_plan_tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to assign to your report plan.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html#cfn-backup-reportplan-reportplantags
        '''
        result = self._values.get("report_plan_tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnReportPlanProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnRestoreTestingPlan(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_backup.CfnRestoreTestingPlan",
):
    '''Creates a restore testing plan.

    The first of two steps to create a restore testing plan. After this request is successful, finish the procedure using CreateRestoreTestingSelection.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-restoretestingplan.html
    :cloudformationResource: AWS::Backup::RestoreTestingPlan
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_backup as backup
        
        cfn_restore_testing_plan = backup.CfnRestoreTestingPlan(self, "MyCfnRestoreTestingPlan",
            recovery_point_selection=backup.CfnRestoreTestingPlan.RestoreTestingRecoveryPointSelectionProperty(
                algorithm="algorithm",
                include_vaults=["includeVaults"],
                recovery_point_types=["recoveryPointTypes"],
        
                # the properties below are optional
                exclude_vaults=["excludeVaults"],
                selection_window_days=123
            ),
            restore_testing_plan_name="restoreTestingPlanName",
            schedule_expression="scheduleExpression",
        
            # the properties below are optional
            schedule_expression_timezone="scheduleExpressionTimezone",
            start_window_hours=123,
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
        recovery_point_selection: typing.Union[_IResolvable_da3f097b, typing.Union["CfnRestoreTestingPlan.RestoreTestingRecoveryPointSelectionProperty", typing.Dict[builtins.str, typing.Any]]],
        restore_testing_plan_name: builtins.str,
        schedule_expression: builtins.str,
        schedule_expression_timezone: typing.Optional[builtins.str] = None,
        start_window_hours: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param recovery_point_selection: The specified criteria to assign a set of resources, such as recovery point types or backup vaults.
        :param restore_testing_plan_name: The RestoreTestingPlanName is a unique string that is the name of the restore testing plan. This cannot be changed after creation, and it must consist of only alphanumeric characters and underscores.
        :param schedule_expression: A CRON expression in specified timezone when a restore testing plan is executed.
        :param schedule_expression_timezone: Optional. This is the timezone in which the schedule expression is set. By default, ScheduleExpressions are in UTC. You can modify this to a specified timezone.
        :param start_window_hours: Defaults to 24 hours. A value in hours after a restore test is scheduled before a job will be canceled if it doesn't start successfully. This value is optional. If this value is included, this parameter has a maximum value of 168 hours (one week).
        :param tags: Optional tags to include. A tag is a key-value pair you can use to manage, filter, and search for your resources. Allowed characters include UTF-8 letters,numbers, spaces, and the following characters: ``+ - = . _ : /.``
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce1d12683247bbd0bcd185e807f3b41b4b53ee7cfd847d57ecbf875d4e7c017f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRestoreTestingPlanProps(
            recovery_point_selection=recovery_point_selection,
            restore_testing_plan_name=restore_testing_plan_name,
            schedule_expression=schedule_expression,
            schedule_expression_timezone=schedule_expression_timezone,
            start_window_hours=start_window_hours,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5ba5ffd43036caff767719ec070ceb8bbd591fd4d39ca36636cd2d29d4a56ff)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6702caf44f3579436a6db3b23da78e6d5e41775573ce62e2e8078955e933edbd)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrRestoreTestingPlanArn")
    def attr_restore_testing_plan_arn(self) -> builtins.str:
        '''An Amazon Resource Name (ARN) that uniquely identifies a restore testing plan.

        :cloudformationAttribute: RestoreTestingPlanArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRestoreTestingPlanArn"))

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
    @jsii.member(jsii_name="recoveryPointSelection")
    def recovery_point_selection(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnRestoreTestingPlan.RestoreTestingRecoveryPointSelectionProperty"]:
        '''The specified criteria to assign a set of resources, such as recovery point types or backup vaults.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnRestoreTestingPlan.RestoreTestingRecoveryPointSelectionProperty"], jsii.get(self, "recoveryPointSelection"))

    @recovery_point_selection.setter
    def recovery_point_selection(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnRestoreTestingPlan.RestoreTestingRecoveryPointSelectionProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__469f816a79c521b1d05c16d66ccb2fb6a0fe1163701e6173b0840fee4d922c49)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recoveryPointSelection", value)

    @builtins.property
    @jsii.member(jsii_name="restoreTestingPlanName")
    def restore_testing_plan_name(self) -> builtins.str:
        '''The RestoreTestingPlanName is a unique string that is the name of the restore testing plan.'''
        return typing.cast(builtins.str, jsii.get(self, "restoreTestingPlanName"))

    @restore_testing_plan_name.setter
    def restore_testing_plan_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6269ad4a6dda73789ac04d7e345263bf14c4a20f6442d99fbd191aeb740ccbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restoreTestingPlanName", value)

    @builtins.property
    @jsii.member(jsii_name="scheduleExpression")
    def schedule_expression(self) -> builtins.str:
        '''A CRON expression in specified timezone when a restore testing plan is executed.'''
        return typing.cast(builtins.str, jsii.get(self, "scheduleExpression"))

    @schedule_expression.setter
    def schedule_expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__feb7dec7f23768db6fb25c010ce6d88323b9a74c117f6237056d65ed8bc1b49b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduleExpression", value)

    @builtins.property
    @jsii.member(jsii_name="scheduleExpressionTimezone")
    def schedule_expression_timezone(self) -> typing.Optional[builtins.str]:
        '''Optional.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduleExpressionTimezone"))

    @schedule_expression_timezone.setter
    def schedule_expression_timezone(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45df227f118297319531c266e28ed0c7920e380fc44ad9f041510f5e6aeef7ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduleExpressionTimezone", value)

    @builtins.property
    @jsii.member(jsii_name="startWindowHours")
    def start_window_hours(self) -> typing.Optional[jsii.Number]:
        '''Defaults to 24 hours.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startWindowHours"))

    @start_window_hours.setter
    def start_window_hours(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9df0eb1aaa95a7ca07b1c2dc88007e89e56d90a6006630d5680cdb415dd093f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startWindowHours", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Optional tags to include.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93b4eb4b15380d36fec202a3d3c50a366e86616c5516db286f16625d21096205)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_backup.CfnRestoreTestingPlan.RestoreTestingRecoveryPointSelectionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "algorithm": "algorithm",
            "include_vaults": "includeVaults",
            "recovery_point_types": "recoveryPointTypes",
            "exclude_vaults": "excludeVaults",
            "selection_window_days": "selectionWindowDays",
        },
    )
    class RestoreTestingRecoveryPointSelectionProperty:
        def __init__(
            self,
            *,
            algorithm: builtins.str,
            include_vaults: typing.Sequence[builtins.str],
            recovery_point_types: typing.Sequence[builtins.str],
            exclude_vaults: typing.Optional[typing.Sequence[builtins.str]] = None,
            selection_window_days: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''``RecoveryPointSelection`` has five parameters (three required and two optional).

            The values you specify determine which recovery point is included in the restore test. You must indicate with ``Algorithm`` if you want the latest recovery point within your ``SelectionWindowDays`` or if you want a random recovery point, and you must indicate through ``IncludeVaults`` from which vaults the recovery points can be chosen.

            ``Algorithm`` ( *required* ) Valid values: " ``LATEST_WITHIN_WINDOW`` " or " ``RANDOM_WITHIN_WINDOW`` ".

            ``Recovery point types`` ( *required* ) Valid values: " ``SNAPSHOT`` " and/or " ``CONTINUOUS`` ". Include ``SNAPSHOT`` to restore only snapshot recovery points; include ``CONTINUOUS`` to restore continuous recovery points (point in time restore / PITR); use both to restore either a snapshot or a continuous recovery point. The recovery point will be determined by the value for ``Algorithm`` .

            ``IncludeVaults`` ( *required* ). You must include one or more backup vaults. Use the wildcard ["*"] or specific ARNs.

            ``SelectionWindowDays`` ( *optional* ) Value must be an integer (in days) from 1 to 365. If not included, the value defaults to ``30`` .

            ``ExcludeVaults`` ( *optional* ). You can choose to input one or more specific backup vault ARNs to exclude those vaults' contents from restore eligibility. Or, you can include a list of selectors. If this parameter and its value are not included, it defaults to empty list.

            :param algorithm: Acceptable values include "LATEST_WITHIN_WINDOW" or "RANDOM_WITHIN_WINDOW".
            :param include_vaults: Accepted values include wildcard ["*"] or by specific ARNs or ARN wilcard replacement ["arn:aws:backup:us-west-2:123456789012:backup-vault:asdf", ...] ["arn:aws:backup:*:*:backup-vault:asdf-*", ...].
            :param recovery_point_types: These are the types of recovery points. Include ``SNAPSHOT`` to restore only snapshot recovery points; include ``CONTINUOUS`` to restore continuous recovery points (point in time restore / PITR); use both to restore either a snapshot or a continuous recovery point. The recovery point will be determined by the value for ``Algorithm`` .
            :param exclude_vaults: Accepted values include specific ARNs or list of selectors. Defaults to empty list if not listed.
            :param selection_window_days: Accepted values are integers from 1 to 365.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-restoretestingplan-restoretestingrecoverypointselection.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_backup as backup
                
                restore_testing_recovery_point_selection_property = backup.CfnRestoreTestingPlan.RestoreTestingRecoveryPointSelectionProperty(
                    algorithm="algorithm",
                    include_vaults=["includeVaults"],
                    recovery_point_types=["recoveryPointTypes"],
                
                    # the properties below are optional
                    exclude_vaults=["excludeVaults"],
                    selection_window_days=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b5c7325bf12ffdf44c2a91f87260dec7090351b3a614521cad6d903cf2ee98bf)
                check_type(argname="argument algorithm", value=algorithm, expected_type=type_hints["algorithm"])
                check_type(argname="argument include_vaults", value=include_vaults, expected_type=type_hints["include_vaults"])
                check_type(argname="argument recovery_point_types", value=recovery_point_types, expected_type=type_hints["recovery_point_types"])
                check_type(argname="argument exclude_vaults", value=exclude_vaults, expected_type=type_hints["exclude_vaults"])
                check_type(argname="argument selection_window_days", value=selection_window_days, expected_type=type_hints["selection_window_days"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "algorithm": algorithm,
                "include_vaults": include_vaults,
                "recovery_point_types": recovery_point_types,
            }
            if exclude_vaults is not None:
                self._values["exclude_vaults"] = exclude_vaults
            if selection_window_days is not None:
                self._values["selection_window_days"] = selection_window_days

        @builtins.property
        def algorithm(self) -> builtins.str:
            '''Acceptable values include "LATEST_WITHIN_WINDOW" or "RANDOM_WITHIN_WINDOW".

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-restoretestingplan-restoretestingrecoverypointselection.html#cfn-backup-restoretestingplan-restoretestingrecoverypointselection-algorithm
            '''
            result = self._values.get("algorithm")
            assert result is not None, "Required property 'algorithm' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def include_vaults(self) -> typing.List[builtins.str]:
            '''Accepted values include wildcard ["*"] or by specific ARNs or ARN wilcard replacement ["arn:aws:backup:us-west-2:123456789012:backup-vault:asdf", ...] ["arn:aws:backup:*:*:backup-vault:asdf-*", ...].

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-restoretestingplan-restoretestingrecoverypointselection.html#cfn-backup-restoretestingplan-restoretestingrecoverypointselection-includevaults
            '''
            result = self._values.get("include_vaults")
            assert result is not None, "Required property 'include_vaults' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def recovery_point_types(self) -> typing.List[builtins.str]:
            '''These are the types of recovery points.

            Include ``SNAPSHOT`` to restore only snapshot recovery points; include ``CONTINUOUS`` to restore continuous recovery points (point in time restore / PITR); use both to restore either a snapshot or a continuous recovery point. The recovery point will be determined by the value for ``Algorithm`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-restoretestingplan-restoretestingrecoverypointselection.html#cfn-backup-restoretestingplan-restoretestingrecoverypointselection-recoverypointtypes
            '''
            result = self._values.get("recovery_point_types")
            assert result is not None, "Required property 'recovery_point_types' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def exclude_vaults(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Accepted values include specific ARNs or list of selectors.

            Defaults to empty list if not listed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-restoretestingplan-restoretestingrecoverypointselection.html#cfn-backup-restoretestingplan-restoretestingrecoverypointselection-excludevaults
            '''
            result = self._values.get("exclude_vaults")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def selection_window_days(self) -> typing.Optional[jsii.Number]:
            '''Accepted values are integers from 1 to 365.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-restoretestingplan-restoretestingrecoverypointselection.html#cfn-backup-restoretestingplan-restoretestingrecoverypointselection-selectionwindowdays
            '''
            result = self._values.get("selection_window_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RestoreTestingRecoveryPointSelectionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_backup.CfnRestoreTestingPlanProps",
    jsii_struct_bases=[],
    name_mapping={
        "recovery_point_selection": "recoveryPointSelection",
        "restore_testing_plan_name": "restoreTestingPlanName",
        "schedule_expression": "scheduleExpression",
        "schedule_expression_timezone": "scheduleExpressionTimezone",
        "start_window_hours": "startWindowHours",
        "tags": "tags",
    },
)
class CfnRestoreTestingPlanProps:
    def __init__(
        self,
        *,
        recovery_point_selection: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRestoreTestingPlan.RestoreTestingRecoveryPointSelectionProperty, typing.Dict[builtins.str, typing.Any]]],
        restore_testing_plan_name: builtins.str,
        schedule_expression: builtins.str,
        schedule_expression_timezone: typing.Optional[builtins.str] = None,
        start_window_hours: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRestoreTestingPlan``.

        :param recovery_point_selection: The specified criteria to assign a set of resources, such as recovery point types or backup vaults.
        :param restore_testing_plan_name: The RestoreTestingPlanName is a unique string that is the name of the restore testing plan. This cannot be changed after creation, and it must consist of only alphanumeric characters and underscores.
        :param schedule_expression: A CRON expression in specified timezone when a restore testing plan is executed.
        :param schedule_expression_timezone: Optional. This is the timezone in which the schedule expression is set. By default, ScheduleExpressions are in UTC. You can modify this to a specified timezone.
        :param start_window_hours: Defaults to 24 hours. A value in hours after a restore test is scheduled before a job will be canceled if it doesn't start successfully. This value is optional. If this value is included, this parameter has a maximum value of 168 hours (one week).
        :param tags: Optional tags to include. A tag is a key-value pair you can use to manage, filter, and search for your resources. Allowed characters include UTF-8 letters,numbers, spaces, and the following characters: ``+ - = . _ : /.``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-restoretestingplan.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_backup as backup
            
            cfn_restore_testing_plan_props = backup.CfnRestoreTestingPlanProps(
                recovery_point_selection=backup.CfnRestoreTestingPlan.RestoreTestingRecoveryPointSelectionProperty(
                    algorithm="algorithm",
                    include_vaults=["includeVaults"],
                    recovery_point_types=["recoveryPointTypes"],
            
                    # the properties below are optional
                    exclude_vaults=["excludeVaults"],
                    selection_window_days=123
                ),
                restore_testing_plan_name="restoreTestingPlanName",
                schedule_expression="scheduleExpression",
            
                # the properties below are optional
                schedule_expression_timezone="scheduleExpressionTimezone",
                start_window_hours=123,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d65b2884e40d5939ab5441a32efe6879390155bd000dab9e921f71ac415b50f5)
            check_type(argname="argument recovery_point_selection", value=recovery_point_selection, expected_type=type_hints["recovery_point_selection"])
            check_type(argname="argument restore_testing_plan_name", value=restore_testing_plan_name, expected_type=type_hints["restore_testing_plan_name"])
            check_type(argname="argument schedule_expression", value=schedule_expression, expected_type=type_hints["schedule_expression"])
            check_type(argname="argument schedule_expression_timezone", value=schedule_expression_timezone, expected_type=type_hints["schedule_expression_timezone"])
            check_type(argname="argument start_window_hours", value=start_window_hours, expected_type=type_hints["start_window_hours"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "recovery_point_selection": recovery_point_selection,
            "restore_testing_plan_name": restore_testing_plan_name,
            "schedule_expression": schedule_expression,
        }
        if schedule_expression_timezone is not None:
            self._values["schedule_expression_timezone"] = schedule_expression_timezone
        if start_window_hours is not None:
            self._values["start_window_hours"] = start_window_hours
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def recovery_point_selection(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnRestoreTestingPlan.RestoreTestingRecoveryPointSelectionProperty]:
        '''The specified criteria to assign a set of resources, such as recovery point types or backup vaults.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-restoretestingplan.html#cfn-backup-restoretestingplan-recoverypointselection
        '''
        result = self._values.get("recovery_point_selection")
        assert result is not None, "Required property 'recovery_point_selection' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnRestoreTestingPlan.RestoreTestingRecoveryPointSelectionProperty], result)

    @builtins.property
    def restore_testing_plan_name(self) -> builtins.str:
        '''The RestoreTestingPlanName is a unique string that is the name of the restore testing plan.

        This cannot be changed after creation, and it must consist of only alphanumeric characters and underscores.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-restoretestingplan.html#cfn-backup-restoretestingplan-restoretestingplanname
        '''
        result = self._values.get("restore_testing_plan_name")
        assert result is not None, "Required property 'restore_testing_plan_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schedule_expression(self) -> builtins.str:
        '''A CRON expression in specified timezone when a restore testing plan is executed.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-restoretestingplan.html#cfn-backup-restoretestingplan-scheduleexpression
        '''
        result = self._values.get("schedule_expression")
        assert result is not None, "Required property 'schedule_expression' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schedule_expression_timezone(self) -> typing.Optional[builtins.str]:
        '''Optional.

        This is the timezone in which the schedule expression is set. By default, ScheduleExpressions are in UTC. You can modify this to a specified timezone.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-restoretestingplan.html#cfn-backup-restoretestingplan-scheduleexpressiontimezone
        '''
        result = self._values.get("schedule_expression_timezone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_window_hours(self) -> typing.Optional[jsii.Number]:
        '''Defaults to 24 hours.

        A value in hours after a restore test is scheduled before a job will be canceled if it doesn't start successfully. This value is optional. If this value is included, this parameter has a maximum value of 168 hours (one week).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-restoretestingplan.html#cfn-backup-restoretestingplan-startwindowhours
        '''
        result = self._values.get("start_window_hours")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Optional tags to include.

        A tag is a key-value pair you can use to manage, filter, and search for your resources. Allowed characters include UTF-8 letters,numbers, spaces, and the following characters: ``+ - = . _ : /.``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-restoretestingplan.html#cfn-backup-restoretestingplan-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRestoreTestingPlanProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnRestoreTestingSelection(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_backup.CfnRestoreTestingSelection",
):
    '''This request can be sent after CreateRestoreTestingPlan request returns successfully.

    This is the second part of creating a resource testing plan, and it must be completed sequentially.

    This consists of ``RestoreTestingSelectionName`` , ``ProtectedResourceType`` , and one of the following:

    - ``ProtectedResourceArns``
    - ``ProtectedResourceConditions``

    Each protected resource type can have one single value.

    A restore testing selection can include a wildcard value ("*") for ``ProtectedResourceArns`` along with ``ProtectedResourceConditions`` . Alternatively, you can include up to 30 specific protected resource ARNs in ``ProtectedResourceArns`` .

    Cannot select by both protected resource types AND specific ARNs. Request will fail if both are included.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-restoretestingselection.html
    :cloudformationResource: AWS::Backup::RestoreTestingSelection
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_backup as backup
        
        cfn_restore_testing_selection = backup.CfnRestoreTestingSelection(self, "MyCfnRestoreTestingSelection",
            iam_role_arn="iamRoleArn",
            protected_resource_type="protectedResourceType",
            restore_testing_plan_name="restoreTestingPlanName",
            restore_testing_selection_name="restoreTestingSelectionName",
        
            # the properties below are optional
            protected_resource_arns=["protectedResourceArns"],
            protected_resource_conditions=backup.CfnRestoreTestingSelection.ProtectedResourceConditionsProperty(
                string_equals=[backup.CfnRestoreTestingSelection.KeyValueProperty(
                    key="key",
                    value="value"
                )],
                string_not_equals=[backup.CfnRestoreTestingSelection.KeyValueProperty(
                    key="key",
                    value="value"
                )]
            ),
            restore_metadata_overrides={
                "restore_metadata_overrides_key": "restoreMetadataOverrides"
            },
            validation_window_hours=123
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        iam_role_arn: builtins.str,
        protected_resource_type: builtins.str,
        restore_testing_plan_name: builtins.str,
        restore_testing_selection_name: builtins.str,
        protected_resource_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        protected_resource_conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRestoreTestingSelection.ProtectedResourceConditionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        restore_metadata_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        validation_window_hours: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param iam_role_arn: The Amazon Resource Name (ARN) of the IAM role that AWS Backup uses to create the target resource; for example: ``arn:aws:iam::123456789012:role/S3Access`` .
        :param protected_resource_type: The type of AWS resource included in a resource testing selection; for example, an Amazon EBS volume or an Amazon RDS database.
        :param restore_testing_plan_name: Unique string that is the name of the restore testing plan. The name cannot be changed after creation. The name must consist of only alphanumeric characters and underscores. Maximum length is 50.
        :param restore_testing_selection_name: The unique name of the restore testing selection that belongs to the related restore testing plan.
        :param protected_resource_arns: You can include specific ARNs, such as ``ProtectedResourceArns: ["arn:aws:...", "arn:aws:..."]`` or you can include a wildcard: ``ProtectedResourceArns: ["*"]`` , but not both.
        :param protected_resource_conditions: In a resource testing selection, this parameter filters by specific conditions such as ``StringEquals`` or ``StringNotEquals`` .
        :param restore_metadata_overrides: You can override certain restore metadata keys by including the parameter ``RestoreMetadataOverrides`` in the body of ``RestoreTestingSelection`` . Key values are not case sensitive. See the complete list of `restore testing inferred metadata <https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing-inferred-metadata.html>`_ .
        :param validation_window_hours: This is amount of hours (1 to 168) available to run a validation script on the data. The data will be deleted upon the completion of the validation script or the end of the specified retention period, whichever comes first.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcf5b783f910e19031573c45aeb82865ab4fa2145dd36242b383df442b55b4cd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRestoreTestingSelectionProps(
            iam_role_arn=iam_role_arn,
            protected_resource_type=protected_resource_type,
            restore_testing_plan_name=restore_testing_plan_name,
            restore_testing_selection_name=restore_testing_selection_name,
            protected_resource_arns=protected_resource_arns,
            protected_resource_conditions=protected_resource_conditions,
            restore_metadata_overrides=restore_metadata_overrides,
            validation_window_hours=validation_window_hours,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6d08475ef8ec086062770da8c6ae1e386a46bcdff9dfb5040b7f1493611cb3e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__34de78e7710b49a3b42ef7d51f2dfc0e53d42cd2f7a806ece05933ad0dd33be4)
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
    @jsii.member(jsii_name="iamRoleArn")
    def iam_role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role that AWS Backup uses to create the target resource;'''
        return typing.cast(builtins.str, jsii.get(self, "iamRoleArn"))

    @iam_role_arn.setter
    def iam_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34257f3d99d8dd81dd7c1970745d4963406e9997794afa2eaa58e5f3091981d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="protectedResourceType")
    def protected_resource_type(self) -> builtins.str:
        '''The type of AWS resource included in a resource testing selection;'''
        return typing.cast(builtins.str, jsii.get(self, "protectedResourceType"))

    @protected_resource_type.setter
    def protected_resource_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6719783d182adbeb22a96172d51be6ee382ad7651dee643d5a90d3cb2adff232)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protectedResourceType", value)

    @builtins.property
    @jsii.member(jsii_name="restoreTestingPlanName")
    def restore_testing_plan_name(self) -> builtins.str:
        '''Unique string that is the name of the restore testing plan.'''
        return typing.cast(builtins.str, jsii.get(self, "restoreTestingPlanName"))

    @restore_testing_plan_name.setter
    def restore_testing_plan_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac3b68fe5b51b83a59b83e052ca08ca16d71cb6968805dd38de621c693f4dc59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restoreTestingPlanName", value)

    @builtins.property
    @jsii.member(jsii_name="restoreTestingSelectionName")
    def restore_testing_selection_name(self) -> builtins.str:
        '''The unique name of the restore testing selection that belongs to the related restore testing plan.'''
        return typing.cast(builtins.str, jsii.get(self, "restoreTestingSelectionName"))

    @restore_testing_selection_name.setter
    def restore_testing_selection_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c01d71d9386b9d1b2bb36875e5603d6b15b83bc54c7690640a18bdbe764a8ec9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restoreTestingSelectionName", value)

    @builtins.property
    @jsii.member(jsii_name="protectedResourceArns")
    def protected_resource_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''You can include specific ARNs, such as ``ProtectedResourceArns: ["arn:aws:...", "arn:aws:..."]`` or you can include a wildcard: ``ProtectedResourceArns: ["*"]`` , but not both.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "protectedResourceArns"))

    @protected_resource_arns.setter
    def protected_resource_arns(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e6805582b6d06e09dd1dcb088e5e9cda91f926647460866a9ee4aaf1b53c5db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protectedResourceArns", value)

    @builtins.property
    @jsii.member(jsii_name="protectedResourceConditions")
    def protected_resource_conditions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRestoreTestingSelection.ProtectedResourceConditionsProperty"]]:
        '''In a resource testing selection, this parameter filters by specific conditions such as ``StringEquals`` or ``StringNotEquals`` .'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRestoreTestingSelection.ProtectedResourceConditionsProperty"]], jsii.get(self, "protectedResourceConditions"))

    @protected_resource_conditions.setter
    def protected_resource_conditions(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRestoreTestingSelection.ProtectedResourceConditionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bca09c3c518b6d44e5cb2086f38f9235f25ef7744e3c6cfba7d01b48e73b989)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protectedResourceConditions", value)

    @builtins.property
    @jsii.member(jsii_name="restoreMetadataOverrides")
    def restore_metadata_overrides(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''You can override certain restore metadata keys by including the parameter ``RestoreMetadataOverrides`` in the body of ``RestoreTestingSelection`` .'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "restoreMetadataOverrides"))

    @restore_metadata_overrides.setter
    def restore_metadata_overrides(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9afb00368be90e46cf02ec2498547553cd056db449734f0be5d5877e388c4af5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restoreMetadataOverrides", value)

    @builtins.property
    @jsii.member(jsii_name="validationWindowHours")
    def validation_window_hours(self) -> typing.Optional[jsii.Number]:
        '''This is amount of hours (1 to 168) available to run a validation script on the data.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "validationWindowHours"))

    @validation_window_hours.setter
    def validation_window_hours(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2be1604fc1c4809e8243d2870eda79b55ab549c0f8a8368d99aded8cda271d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validationWindowHours", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_backup.CfnRestoreTestingSelection.KeyValueProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class KeyValueProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''Pair of two related strings.

            Allowed characters are letters, white space, and numbers that can be represented in UTF-8 and the following characters: ``+ - = . _ : /``

            :param key: The tag key.
            :param value: The tag value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-restoretestingselection-keyvalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_backup as backup
                
                key_value_property = backup.CfnRestoreTestingSelection.KeyValueProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ab32bbff81cfbfeb46780f1db32ce34c7ddfe0658843461e3c5e6ddccc176c3d)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The tag key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-restoretestingselection-keyvalue.html#cfn-backup-restoretestingselection-keyvalue-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The tag value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-restoretestingselection-keyvalue.html#cfn-backup-restoretestingselection-keyvalue-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KeyValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_backup.CfnRestoreTestingSelection.ProtectedResourceConditionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "string_equals": "stringEquals",
            "string_not_equals": "stringNotEquals",
        },
    )
    class ProtectedResourceConditionsProperty:
        def __init__(
            self,
            *,
            string_equals: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRestoreTestingSelection.KeyValueProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            string_not_equals: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRestoreTestingSelection.KeyValueProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The conditions that you define for resources in your restore testing plan using tags.

            For example, ``"StringEquals": { "Key": "aws:ResourceTag/CreatedByCryo", "Value": "true" },`` . Condition operators are case sensitive.

            :param string_equals: Filters the values of your tagged resources for only those resources that you tagged with the same value. Also called "exact matching."
            :param string_not_equals: Filters the values of your tagged resources for only those resources that you tagged that do not have the same value. Also called "negated matching."

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-restoretestingselection-protectedresourceconditions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_backup as backup
                
                protected_resource_conditions_property = backup.CfnRestoreTestingSelection.ProtectedResourceConditionsProperty(
                    string_equals=[backup.CfnRestoreTestingSelection.KeyValueProperty(
                        key="key",
                        value="value"
                    )],
                    string_not_equals=[backup.CfnRestoreTestingSelection.KeyValueProperty(
                        key="key",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__21f4334cd0e11f4b24684e9ff9cf575380c735e9265b95d69aa611aae88b0a78)
                check_type(argname="argument string_equals", value=string_equals, expected_type=type_hints["string_equals"])
                check_type(argname="argument string_not_equals", value=string_not_equals, expected_type=type_hints["string_not_equals"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if string_equals is not None:
                self._values["string_equals"] = string_equals
            if string_not_equals is not None:
                self._values["string_not_equals"] = string_not_equals

        @builtins.property
        def string_equals(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRestoreTestingSelection.KeyValueProperty"]]]]:
            '''Filters the values of your tagged resources for only those resources that you tagged with the same value.

            Also called "exact matching."

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-restoretestingselection-protectedresourceconditions.html#cfn-backup-restoretestingselection-protectedresourceconditions-stringequals
            '''
            result = self._values.get("string_equals")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRestoreTestingSelection.KeyValueProperty"]]]], result)

        @builtins.property
        def string_not_equals(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRestoreTestingSelection.KeyValueProperty"]]]]:
            '''Filters the values of your tagged resources for only those resources that you tagged that do not have the same value.

            Also called "negated matching."

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-restoretestingselection-protectedresourceconditions.html#cfn-backup-restoretestingselection-protectedresourceconditions-stringnotequals
            '''
            result = self._values.get("string_not_equals")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRestoreTestingSelection.KeyValueProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProtectedResourceConditionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_backup.CfnRestoreTestingSelectionProps",
    jsii_struct_bases=[],
    name_mapping={
        "iam_role_arn": "iamRoleArn",
        "protected_resource_type": "protectedResourceType",
        "restore_testing_plan_name": "restoreTestingPlanName",
        "restore_testing_selection_name": "restoreTestingSelectionName",
        "protected_resource_arns": "protectedResourceArns",
        "protected_resource_conditions": "protectedResourceConditions",
        "restore_metadata_overrides": "restoreMetadataOverrides",
        "validation_window_hours": "validationWindowHours",
    },
)
class CfnRestoreTestingSelectionProps:
    def __init__(
        self,
        *,
        iam_role_arn: builtins.str,
        protected_resource_type: builtins.str,
        restore_testing_plan_name: builtins.str,
        restore_testing_selection_name: builtins.str,
        protected_resource_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        protected_resource_conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRestoreTestingSelection.ProtectedResourceConditionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        restore_metadata_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        validation_window_hours: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``CfnRestoreTestingSelection``.

        :param iam_role_arn: The Amazon Resource Name (ARN) of the IAM role that AWS Backup uses to create the target resource; for example: ``arn:aws:iam::123456789012:role/S3Access`` .
        :param protected_resource_type: The type of AWS resource included in a resource testing selection; for example, an Amazon EBS volume or an Amazon RDS database.
        :param restore_testing_plan_name: Unique string that is the name of the restore testing plan. The name cannot be changed after creation. The name must consist of only alphanumeric characters and underscores. Maximum length is 50.
        :param restore_testing_selection_name: The unique name of the restore testing selection that belongs to the related restore testing plan.
        :param protected_resource_arns: You can include specific ARNs, such as ``ProtectedResourceArns: ["arn:aws:...", "arn:aws:..."]`` or you can include a wildcard: ``ProtectedResourceArns: ["*"]`` , but not both.
        :param protected_resource_conditions: In a resource testing selection, this parameter filters by specific conditions such as ``StringEquals`` or ``StringNotEquals`` .
        :param restore_metadata_overrides: You can override certain restore metadata keys by including the parameter ``RestoreMetadataOverrides`` in the body of ``RestoreTestingSelection`` . Key values are not case sensitive. See the complete list of `restore testing inferred metadata <https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing-inferred-metadata.html>`_ .
        :param validation_window_hours: This is amount of hours (1 to 168) available to run a validation script on the data. The data will be deleted upon the completion of the validation script or the end of the specified retention period, whichever comes first.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-restoretestingselection.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_backup as backup
            
            cfn_restore_testing_selection_props = backup.CfnRestoreTestingSelectionProps(
                iam_role_arn="iamRoleArn",
                protected_resource_type="protectedResourceType",
                restore_testing_plan_name="restoreTestingPlanName",
                restore_testing_selection_name="restoreTestingSelectionName",
            
                # the properties below are optional
                protected_resource_arns=["protectedResourceArns"],
                protected_resource_conditions=backup.CfnRestoreTestingSelection.ProtectedResourceConditionsProperty(
                    string_equals=[backup.CfnRestoreTestingSelection.KeyValueProperty(
                        key="key",
                        value="value"
                    )],
                    string_not_equals=[backup.CfnRestoreTestingSelection.KeyValueProperty(
                        key="key",
                        value="value"
                    )]
                ),
                restore_metadata_overrides={
                    "restore_metadata_overrides_key": "restoreMetadataOverrides"
                },
                validation_window_hours=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd755bb9b5c3f12e065d4bb10b1805bc3571946724f1d8f52794cc5491212cdb)
            check_type(argname="argument iam_role_arn", value=iam_role_arn, expected_type=type_hints["iam_role_arn"])
            check_type(argname="argument protected_resource_type", value=protected_resource_type, expected_type=type_hints["protected_resource_type"])
            check_type(argname="argument restore_testing_plan_name", value=restore_testing_plan_name, expected_type=type_hints["restore_testing_plan_name"])
            check_type(argname="argument restore_testing_selection_name", value=restore_testing_selection_name, expected_type=type_hints["restore_testing_selection_name"])
            check_type(argname="argument protected_resource_arns", value=protected_resource_arns, expected_type=type_hints["protected_resource_arns"])
            check_type(argname="argument protected_resource_conditions", value=protected_resource_conditions, expected_type=type_hints["protected_resource_conditions"])
            check_type(argname="argument restore_metadata_overrides", value=restore_metadata_overrides, expected_type=type_hints["restore_metadata_overrides"])
            check_type(argname="argument validation_window_hours", value=validation_window_hours, expected_type=type_hints["validation_window_hours"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "iam_role_arn": iam_role_arn,
            "protected_resource_type": protected_resource_type,
            "restore_testing_plan_name": restore_testing_plan_name,
            "restore_testing_selection_name": restore_testing_selection_name,
        }
        if protected_resource_arns is not None:
            self._values["protected_resource_arns"] = protected_resource_arns
        if protected_resource_conditions is not None:
            self._values["protected_resource_conditions"] = protected_resource_conditions
        if restore_metadata_overrides is not None:
            self._values["restore_metadata_overrides"] = restore_metadata_overrides
        if validation_window_hours is not None:
            self._values["validation_window_hours"] = validation_window_hours

    @builtins.property
    def iam_role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role that AWS Backup uses to create the target resource;

        for example: ``arn:aws:iam::123456789012:role/S3Access`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-restoretestingselection.html#cfn-backup-restoretestingselection-iamrolearn
        '''
        result = self._values.get("iam_role_arn")
        assert result is not None, "Required property 'iam_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protected_resource_type(self) -> builtins.str:
        '''The type of AWS resource included in a resource testing selection;

        for example, an Amazon EBS volume or an Amazon RDS database.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-restoretestingselection.html#cfn-backup-restoretestingselection-protectedresourcetype
        '''
        result = self._values.get("protected_resource_type")
        assert result is not None, "Required property 'protected_resource_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def restore_testing_plan_name(self) -> builtins.str:
        '''Unique string that is the name of the restore testing plan.

        The name cannot be changed after creation. The name must consist of only alphanumeric characters and underscores. Maximum length is 50.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-restoretestingselection.html#cfn-backup-restoretestingselection-restoretestingplanname
        '''
        result = self._values.get("restore_testing_plan_name")
        assert result is not None, "Required property 'restore_testing_plan_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def restore_testing_selection_name(self) -> builtins.str:
        '''The unique name of the restore testing selection that belongs to the related restore testing plan.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-restoretestingselection.html#cfn-backup-restoretestingselection-restoretestingselectionname
        '''
        result = self._values.get("restore_testing_selection_name")
        assert result is not None, "Required property 'restore_testing_selection_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protected_resource_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''You can include specific ARNs, such as ``ProtectedResourceArns: ["arn:aws:...", "arn:aws:..."]`` or you can include a wildcard: ``ProtectedResourceArns: ["*"]`` , but not both.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-restoretestingselection.html#cfn-backup-restoretestingselection-protectedresourcearns
        '''
        result = self._values.get("protected_resource_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def protected_resource_conditions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRestoreTestingSelection.ProtectedResourceConditionsProperty]]:
        '''In a resource testing selection, this parameter filters by specific conditions such as ``StringEquals`` or ``StringNotEquals`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-restoretestingselection.html#cfn-backup-restoretestingselection-protectedresourceconditions
        '''
        result = self._values.get("protected_resource_conditions")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRestoreTestingSelection.ProtectedResourceConditionsProperty]], result)

    @builtins.property
    def restore_metadata_overrides(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''You can override certain restore metadata keys by including the parameter ``RestoreMetadataOverrides`` in the body of ``RestoreTestingSelection`` .

        Key values are not case sensitive.

        See the complete list of `restore testing inferred metadata <https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing-inferred-metadata.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-restoretestingselection.html#cfn-backup-restoretestingselection-restoremetadataoverrides
        '''
        result = self._values.get("restore_metadata_overrides")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def validation_window_hours(self) -> typing.Optional[jsii.Number]:
        '''This is amount of hours (1 to 168) available to run a validation script on the data.

        The data will be deleted upon the completion of the validation script or the end of the specified retention period, whichever comes first.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-restoretestingselection.html#cfn-backup-restoretestingselection-validationwindowhours
        '''
        result = self._values.get("validation_window_hours")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRestoreTestingSelectionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.aws_backup.IBackupPlan")
class IBackupPlan(_IResource_c80c4260, typing_extensions.Protocol):
    '''A backup plan.'''

    @builtins.property
    @jsii.member(jsii_name="backupPlanId")
    def backup_plan_id(self) -> builtins.str:
        '''The identifier of the backup plan.

        :attribute: true
        '''
        ...


class _IBackupPlanProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''A backup plan.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_backup.IBackupPlan"

    @builtins.property
    @jsii.member(jsii_name="backupPlanId")
    def backup_plan_id(self) -> builtins.str:
        '''The identifier of the backup plan.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "backupPlanId"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBackupPlan).__jsii_proxy_class__ = lambda : _IBackupPlanProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_backup.IBackupVault")
class IBackupVault(_IResource_c80c4260, typing_extensions.Protocol):
    '''A backup vault.'''

    @builtins.property
    @jsii.member(jsii_name="backupVaultArn")
    def backup_vault_arn(self) -> builtins.str:
        '''The ARN of the backup vault.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="backupVaultName")
    def backup_vault_name(self) -> builtins.str:
        '''The name of a logical container where backups are stored.

        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Grant the actions defined in actions to the given grantee on this backup vault.

        :param grantee: -
        :param actions: -
        '''
        ...


class _IBackupVaultProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''A backup vault.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_backup.IBackupVault"

    @builtins.property
    @jsii.member(jsii_name="backupVaultArn")
    def backup_vault_arn(self) -> builtins.str:
        '''The ARN of the backup vault.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "backupVaultArn"))

    @builtins.property
    @jsii.member(jsii_name="backupVaultName")
    def backup_vault_name(self) -> builtins.str:
        '''The name of a logical container where backups are stored.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "backupVaultName"))

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Grant the actions defined in actions to the given grantee on this backup vault.

        :param grantee: -
        :param actions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f046e29be9f6222e2ff343629e5ca635543c7abc067c609446b86467be6c5b68)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grant", [grantee, *actions]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBackupVault).__jsii_proxy_class__ = lambda : _IBackupVaultProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_backup.LockConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "min_retention": "minRetention",
        "changeable_for": "changeableFor",
        "max_retention": "maxRetention",
    },
)
class LockConfiguration:
    def __init__(
        self,
        *,
        min_retention: _Duration_4839e8c3,
        changeable_for: typing.Optional[_Duration_4839e8c3] = None,
        max_retention: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''Configuration for AWS Backup Vault Lock.

        :param min_retention: The minimum retention period that the vault retains its recovery points. If this parameter is specified, any backup or copy job to the vault must have a lifecycle policy with a retention period equal to or longer than the minimum retention period. If the job's retention period is shorter than that minimum retention period, then the vault fails that backup or copy job, and you should either modify your lifecycle settings or use a different vault. Recovery points already saved in the vault prior to Vault Lock are not affected.
        :param changeable_for: The duration before the lock date. AWS Backup enforces a 72-hour cooling-off period before Vault Lock takes effect and becomes immutable. Before the lock date, you can delete Vault Lock from the vault or change the Vault Lock configuration. On and after the lock date, the Vault Lock becomes immutable and cannot be changed or deleted. Default: - Vault Lock can be deleted or changed at any time
        :param max_retention: The maximum retention period that the vault retains its recovery points. If this parameter is specified, any backup or copy job to the vault must have a lifecycle policy with a retention period equal to or shorter than the maximum retention period. If the job's retention period is longer than that maximum retention period, then the vault fails the backup or copy job, and you should either modify your lifecycle settings or use a different vault. Recovery points already saved in the vault prior to Vault Lock are not affected. Default: - Vault Lock does not enforce a maximum retention period

        :see: https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html
        :exampleMetadata: infused

        Example::

            backup.BackupVault(self, "Vault",
                lock_configuration=backup.LockConfiguration(
                    min_retention=Duration.days(30)
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f8085843c1a2a230e0c965fbb91f96b1b11b817ee7d9232b4d368b4767e6681)
            check_type(argname="argument min_retention", value=min_retention, expected_type=type_hints["min_retention"])
            check_type(argname="argument changeable_for", value=changeable_for, expected_type=type_hints["changeable_for"])
            check_type(argname="argument max_retention", value=max_retention, expected_type=type_hints["max_retention"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "min_retention": min_retention,
        }
        if changeable_for is not None:
            self._values["changeable_for"] = changeable_for
        if max_retention is not None:
            self._values["max_retention"] = max_retention

    @builtins.property
    def min_retention(self) -> _Duration_4839e8c3:
        '''The minimum retention period that the vault retains its recovery points.

        If this parameter is specified, any backup or copy job to the vault must
        have a lifecycle policy with a retention period equal to or longer than
        the minimum retention period. If the job's retention period is shorter than
        that minimum retention period, then the vault fails that backup or copy job,
        and you should either modify your lifecycle settings or use a different
        vault. Recovery points already saved in the vault prior to Vault Lock are
        not affected.
        '''
        result = self._values.get("min_retention")
        assert result is not None, "Required property 'min_retention' is missing"
        return typing.cast(_Duration_4839e8c3, result)

    @builtins.property
    def changeable_for(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The duration before the lock date.

        AWS Backup enforces a 72-hour cooling-off period before Vault Lock takes
        effect and becomes immutable.

        Before the lock date, you can delete Vault Lock from the vault or change
        the Vault Lock configuration. On and after the lock date, the Vault Lock
        becomes immutable and cannot be changed or deleted.

        :default: - Vault Lock can be deleted or changed at any time
        '''
        result = self._values.get("changeable_for")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def max_retention(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The maximum retention period that the vault retains its recovery points.

        If this parameter is specified, any backup or copy job to the vault must
        have a lifecycle policy with a retention period equal to or shorter than
        the maximum retention period. If the job's retention period is longer than
        that maximum retention period, then the vault fails the backup or copy job,
        and you should either modify your lifecycle settings or use a different
        vault. Recovery points already saved in the vault prior to Vault Lock are
        not affected.

        :default: - Vault Lock does not enforce a maximum retention period
        '''
        result = self._values.get("max_retention")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LockConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_backup.TagCondition",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value", "operation": "operation"},
)
class TagCondition:
    def __init__(
        self,
        *,
        key: builtins.str,
        value: builtins.str,
        operation: typing.Optional["TagOperation"] = None,
    ) -> None:
        '''A tag condition.

        :param key: The key in a key-value pair. For example, in ``"ec2:ResourceTag/Department": "accounting"``, ``ec2:ResourceTag/Department`` is the key.
        :param value: The value in a key-value pair. For example, in ``"ec2:ResourceTag/Department": "accounting"``, ``accounting`` is the value.
        :param operation: An operation that is applied to a key-value pair used to filter resources in a selection. Default: STRING_EQUALS

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_backup as backup
            
            tag_condition = backup.TagCondition(
                key="key",
                value="value",
            
                # the properties below are optional
                operation=backup.TagOperation.STRING_EQUALS
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebec77480ee4239c5e74e693ea6942bce079e6a195e1db4021330679f19a3080)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument operation", value=operation, expected_type=type_hints["operation"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "value": value,
        }
        if operation is not None:
            self._values["operation"] = operation

    @builtins.property
    def key(self) -> builtins.str:
        '''The key in a key-value pair.

        For example, in ``"ec2:ResourceTag/Department": "accounting"``,
        ``ec2:ResourceTag/Department`` is the key.
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The value in a key-value pair.

        For example, in ``"ec2:ResourceTag/Department": "accounting"``,
        ``accounting`` is the value.
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operation(self) -> typing.Optional["TagOperation"]:
        '''An operation that is applied to a key-value pair used to filter resources in a selection.

        :default: STRING_EQUALS
        '''
        result = self._values.get("operation")
        return typing.cast(typing.Optional["TagOperation"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TagCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_backup.TagOperation")
class TagOperation(enum.Enum):
    '''An operation that is applied to a key-value pair.'''

    STRING_EQUALS = "STRING_EQUALS"
    '''StringEquals.'''
    DUMMY = "DUMMY"
    '''Dummy member.'''


@jsii.implements(IBackupPlan)
class BackupPlan(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_backup.BackupPlan",
):
    '''A backup plan.

    :exampleMetadata: infused

    Example::

        # Daily, weekly and monthly with 5 year retention
        plan = backup.BackupPlan.daily_weekly_monthly5_year_retention(self, "Plan")
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        backup_plan_name: typing.Optional[builtins.str] = None,
        backup_plan_rules: typing.Optional[typing.Sequence[BackupPlanRule]] = None,
        backup_vault: typing.Optional[IBackupVault] = None,
        windows_vss: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param backup_plan_name: The display name of the backup plan. Default: - A CDK generated name
        :param backup_plan_rules: Rules for the backup plan. Use ``addRule()`` to add rules after instantiation. Default: - use ``addRule()`` to add rules
        :param backup_vault: The backup vault where backups are stored. Default: - use the vault defined at the rule level. If not defined a new common vault for the plan will be created
        :param windows_vss: Enable Windows VSS backup. Default: false
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac9eeb1158690e76fc800429198c84b42bf4dc68c223e34e743ca5c3de83102d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = BackupPlanProps(
            backup_plan_name=backup_plan_name,
            backup_plan_rules=backup_plan_rules,
            backup_vault=backup_vault,
            windows_vss=windows_vss,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="daily35DayRetention")
    @builtins.classmethod
    def daily35_day_retention(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        backup_vault: typing.Optional[IBackupVault] = None,
    ) -> "BackupPlan":
        '''Daily with 35 day retention.

        :param scope: -
        :param id: -
        :param backup_vault: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17983f2742df72bf64d28b678e89a057f2b1feed375c39a562e042faadaf8668)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument backup_vault", value=backup_vault, expected_type=type_hints["backup_vault"])
        return typing.cast("BackupPlan", jsii.sinvoke(cls, "daily35DayRetention", [scope, id, backup_vault]))

    @jsii.member(jsii_name="dailyMonthly1YearRetention")
    @builtins.classmethod
    def daily_monthly1_year_retention(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        backup_vault: typing.Optional[IBackupVault] = None,
    ) -> "BackupPlan":
        '''Daily and monthly with 1 year retention.

        :param scope: -
        :param id: -
        :param backup_vault: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bb65bf5b0ac30cf59b76bfc6b0fd6a5c44fe614f682166d81e998f4dd87179a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument backup_vault", value=backup_vault, expected_type=type_hints["backup_vault"])
        return typing.cast("BackupPlan", jsii.sinvoke(cls, "dailyMonthly1YearRetention", [scope, id, backup_vault]))

    @jsii.member(jsii_name="dailyWeeklyMonthly5YearRetention")
    @builtins.classmethod
    def daily_weekly_monthly5_year_retention(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        backup_vault: typing.Optional[IBackupVault] = None,
    ) -> "BackupPlan":
        '''Daily, weekly and monthly with 5 year retention.

        :param scope: -
        :param id: -
        :param backup_vault: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e80dbcebd876b060051ccd746c3d678b6857f64ed24fda01e09c953ebbc3199c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument backup_vault", value=backup_vault, expected_type=type_hints["backup_vault"])
        return typing.cast("BackupPlan", jsii.sinvoke(cls, "dailyWeeklyMonthly5YearRetention", [scope, id, backup_vault]))

    @jsii.member(jsii_name="dailyWeeklyMonthly7YearRetention")
    @builtins.classmethod
    def daily_weekly_monthly7_year_retention(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        backup_vault: typing.Optional[IBackupVault] = None,
    ) -> "BackupPlan":
        '''Daily, weekly and monthly with 7 year retention.

        :param scope: -
        :param id: -
        :param backup_vault: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__564733017434e9f62e49bb99610f3dd11fc4692ba00892447d2c38e0be976290)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument backup_vault", value=backup_vault, expected_type=type_hints["backup_vault"])
        return typing.cast("BackupPlan", jsii.sinvoke(cls, "dailyWeeklyMonthly7YearRetention", [scope, id, backup_vault]))

    @jsii.member(jsii_name="fromBackupPlanId")
    @builtins.classmethod
    def from_backup_plan_id(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        backup_plan_id: builtins.str,
    ) -> IBackupPlan:
        '''Import an existing backup plan.

        :param scope: -
        :param id: -
        :param backup_plan_id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9d7e2dd359a33f71d62dc691f0b94d1443cc763901092b01ca933df0c543219)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument backup_plan_id", value=backup_plan_id, expected_type=type_hints["backup_plan_id"])
        return typing.cast(IBackupPlan, jsii.sinvoke(cls, "fromBackupPlanId", [scope, id, backup_plan_id]))

    @jsii.member(jsii_name="addRule")
    def add_rule(self, rule: BackupPlanRule) -> None:
        '''Adds a rule to a plan.

        :param rule: the rule to add.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__398b9447d6dff004e80a6df5262bac01ef5f8f5af47ef115c710b218e23791df)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
        return typing.cast(None, jsii.invoke(self, "addRule", [rule]))

    @jsii.member(jsii_name="addSelection")
    def add_selection(
        self,
        id: builtins.str,
        *,
        resources: typing.Sequence[BackupResource],
        allow_restores: typing.Optional[builtins.bool] = None,
        backup_selection_name: typing.Optional[builtins.str] = None,
        disable_default_backup_policy: typing.Optional[builtins.bool] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> BackupSelection:
        '''Adds a selection to this plan.

        :param id: -
        :param resources: The resources to backup. Use the helper static methods defined on ``BackupResource``.
        :param allow_restores: Whether to automatically give restores permissions to the role that AWS Backup uses. If ``true``, the ``AWSBackupServiceRolePolicyForRestores`` managed policy will be attached to the role. Default: false
        :param backup_selection_name: The name for this selection. Default: - a CDK generated name
        :param disable_default_backup_policy: Whether to disable automatically assigning default backup permissions to the role that AWS Backup uses. If ``false``, the ``AWSBackupServiceRolePolicyForBackup`` managed policy will be attached to the role. Default: false
        :param role: The role that AWS Backup uses to authenticate when backuping or restoring the resources. The ``AWSBackupServiceRolePolicyForBackup`` managed policy will be attached to this role unless ``disableDefaultBackupPolicy`` is set to ``true``. Default: - a new role will be created
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__588f53b2d13b2b789941caeafb53933090659574015281ee228d0d35b924172b)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = BackupSelectionOptions(
            resources=resources,
            allow_restores=allow_restores,
            backup_selection_name=backup_selection_name,
            disable_default_backup_policy=disable_default_backup_policy,
            role=role,
        )

        return typing.cast(BackupSelection, jsii.invoke(self, "addSelection", [id, options]))

    @builtins.property
    @jsii.member(jsii_name="backupPlanArn")
    def backup_plan_arn(self) -> builtins.str:
        '''The ARN of the backup plan.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "backupPlanArn"))

    @builtins.property
    @jsii.member(jsii_name="backupPlanId")
    def backup_plan_id(self) -> builtins.str:
        '''The identifier of the backup plan.'''
        return typing.cast(builtins.str, jsii.get(self, "backupPlanId"))

    @builtins.property
    @jsii.member(jsii_name="backupVault")
    def backup_vault(self) -> IBackupVault:
        '''The backup vault where backups are stored if not defined at the rule level.'''
        return typing.cast(IBackupVault, jsii.get(self, "backupVault"))

    @builtins.property
    @jsii.member(jsii_name="versionId")
    def version_id(self) -> builtins.str:
        '''Version Id.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "versionId"))


@jsii.implements(IBackupVault)
class BackupVault(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_backup.BackupVault",
):
    '''A backup vault.

    :exampleMetadata: infused

    Example::

        imported_vault = backup.BackupVault.from_backup_vault_name(self, "Vault", "myVaultName")
        
        role = iam.Role(self, "Access Role", assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"))
        
        imported_vault.grant(role, "backup:StartBackupJob")
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        access_policy: typing.Optional[_PolicyDocument_3ac34393] = None,
        backup_vault_name: typing.Optional[builtins.str] = None,
        block_recovery_point_deletion: typing.Optional[builtins.bool] = None,
        encryption_key: typing.Optional[_IKey_5f11635f] = None,
        lock_configuration: typing.Optional[typing.Union[LockConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
        notification_events: typing.Optional[typing.Sequence[BackupVaultEvents]] = None,
        notification_topic: typing.Optional[_ITopic_9eca4852] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param access_policy: A resource-based policy that is used to manage access permissions on the backup vault. Default: - access is not restricted
        :param backup_vault_name: The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. Default: - A CDK generated name
        :param block_recovery_point_deletion: Whether to add statements to the vault access policy that prevents anyone from deleting a recovery point. Default: false
        :param encryption_key: The server-side encryption key to use to protect your backups. Default: - an Amazon managed KMS key
        :param lock_configuration: Configuration for AWS Backup Vault Lock. Default: - AWS Backup Vault Lock is disabled
        :param notification_events: The vault events to send. Default: - all vault events if ``notificationTopic`` is defined
        :param notification_topic: A SNS topic to send vault events to. Default: - no notifications
        :param removal_policy: The removal policy to apply to the vault. Note that removing a vault that contains recovery points will fail. Default: RemovalPolicy.RETAIN
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5938cd051d17a4aa98a61f204449a9c4416544ba91e3c4e4821b784b40ffc921)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = BackupVaultProps(
            access_policy=access_policy,
            backup_vault_name=backup_vault_name,
            block_recovery_point_deletion=block_recovery_point_deletion,
            encryption_key=encryption_key,
            lock_configuration=lock_configuration,
            notification_events=notification_events,
            notification_topic=notification_topic,
            removal_policy=removal_policy,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromBackupVaultArn")
    @builtins.classmethod
    def from_backup_vault_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        backup_vault_arn: builtins.str,
    ) -> IBackupVault:
        '''Import an existing backup vault by arn.

        :param scope: -
        :param id: -
        :param backup_vault_arn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58170569b5f8f6dd33d5d700cfb73499de3162167c227fa90c30956f0160a753)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument backup_vault_arn", value=backup_vault_arn, expected_type=type_hints["backup_vault_arn"])
        return typing.cast(IBackupVault, jsii.sinvoke(cls, "fromBackupVaultArn", [scope, id, backup_vault_arn]))

    @jsii.member(jsii_name="fromBackupVaultName")
    @builtins.classmethod
    def from_backup_vault_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        backup_vault_name: builtins.str,
    ) -> IBackupVault:
        '''Import an existing backup vault by name.

        :param scope: -
        :param id: -
        :param backup_vault_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdc42d68a7099dab372cd0e3291aa3e3a7794912bbd2c7df2a059b1c39cc0e40)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument backup_vault_name", value=backup_vault_name, expected_type=type_hints["backup_vault_name"])
        return typing.cast(IBackupVault, jsii.sinvoke(cls, "fromBackupVaultName", [scope, id, backup_vault_name]))

    @jsii.member(jsii_name="addToAccessPolicy")
    def add_to_access_policy(self, statement: _PolicyStatement_0fe33853) -> None:
        '''Adds a statement to the vault access policy.

        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e100029ccf44a7b32d3531902bcf8361f5e0f4bf872de45a759df0cb251ea175)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(None, jsii.invoke(self, "addToAccessPolicy", [statement]))

    @jsii.member(jsii_name="blockRecoveryPointDeletion")
    def block_recovery_point_deletion(self) -> None:
        '''Adds a statement to the vault access policy that prevents anyone from deleting a recovery point.'''
        return typing.cast(None, jsii.invoke(self, "blockRecoveryPointDeletion", []))

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Grant the actions defined in actions to the given grantee on this Backup Vault resource.

        :param grantee: Principal to grant right to.
        :param actions: The actions to grant.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6f51b6b852524375032f5dd45b5c00d5d86423092d20d599599a38ce40675a8)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grant", [grantee, *actions]))

    @builtins.property
    @jsii.member(jsii_name="backupVaultArn")
    def backup_vault_arn(self) -> builtins.str:
        '''The ARN of the backup vault.'''
        return typing.cast(builtins.str, jsii.get(self, "backupVaultArn"))

    @builtins.property
    @jsii.member(jsii_name="backupVaultName")
    def backup_vault_name(self) -> builtins.str:
        '''The name of a logical container where backups are stored.'''
        return typing.cast(builtins.str, jsii.get(self, "backupVaultName"))


__all__ = [
    "BackupPlan",
    "BackupPlanCopyActionProps",
    "BackupPlanProps",
    "BackupPlanRule",
    "BackupPlanRuleProps",
    "BackupResource",
    "BackupSelection",
    "BackupSelectionOptions",
    "BackupSelectionProps",
    "BackupVault",
    "BackupVaultEvents",
    "BackupVaultProps",
    "CfnBackupPlan",
    "CfnBackupPlanProps",
    "CfnBackupSelection",
    "CfnBackupSelectionProps",
    "CfnBackupVault",
    "CfnBackupVaultProps",
    "CfnFramework",
    "CfnFrameworkProps",
    "CfnReportPlan",
    "CfnReportPlanProps",
    "CfnRestoreTestingPlan",
    "CfnRestoreTestingPlanProps",
    "CfnRestoreTestingSelection",
    "CfnRestoreTestingSelectionProps",
    "IBackupPlan",
    "IBackupVault",
    "LockConfiguration",
    "TagCondition",
    "TagOperation",
]

publication.publish()

def _typecheckingstub__502c247f5c1b9824033ca24f5efe3e1d20ee8980208ae5382890f6168ba12843(
    *,
    destination_backup_vault: IBackupVault,
    delete_after: typing.Optional[_Duration_4839e8c3] = None,
    move_to_cold_storage_after: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c977b2da08bc5e51abde064245ef25c86ebdc30dd86fbb4658318249248eafb(
    *,
    backup_plan_name: typing.Optional[builtins.str] = None,
    backup_plan_rules: typing.Optional[typing.Sequence[BackupPlanRule]] = None,
    backup_vault: typing.Optional[IBackupVault] = None,
    windows_vss: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f78e665a93a5f3c61a81adf713b3dce3bf2c3c24d2e314a1fbc4460dc83b538(
    backup_vault: typing.Optional[IBackupVault] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d00b6f39a5ae5e68dc286fee4603f5606c654c044712abfb5d45b4c538938e0a(
    backup_vault: typing.Optional[IBackupVault] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4124e390401942af3d104beae29adc9c33bd1305f68302b0dd47aae3e11ca132(
    backup_vault: typing.Optional[IBackupVault] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af7999bcc928a751830ca431012278b60250723ffee54654765a4596696d022d(
    backup_vault: typing.Optional[IBackupVault] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__759b8b9514606abffe4399669994cb3f2c365fc9e05295dd8d754f5af6bb329f(
    backup_vault: typing.Optional[IBackupVault] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__521e43eca71db1c8347b5dbf1e88135cbc1fd43f07248784b33b55d8353d5d90(
    *,
    backup_vault: typing.Optional[IBackupVault] = None,
    completion_window: typing.Optional[_Duration_4839e8c3] = None,
    copy_actions: typing.Optional[typing.Sequence[typing.Union[BackupPlanCopyActionProps, typing.Dict[builtins.str, typing.Any]]]] = None,
    delete_after: typing.Optional[_Duration_4839e8c3] = None,
    enable_continuous_backup: typing.Optional[builtins.bool] = None,
    move_to_cold_storage_after: typing.Optional[_Duration_4839e8c3] = None,
    recovery_point_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    rule_name: typing.Optional[builtins.str] = None,
    schedule_expression: typing.Optional[_Schedule_c151d01f] = None,
    start_window: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da262bae32a880066638158d96c942364504852f2d4af32d72bcd0034c7fbd32(
    resource: typing.Optional[builtins.str] = None,
    tag_condition: typing.Optional[typing.Union[TagCondition, typing.Dict[builtins.str, typing.Any]]] = None,
    construct: typing.Optional[_constructs_77d1e7e8.Construct] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2db3e845e2974e883de9fa3efc667fda5fd092ba7fea3f5fa1f1c15a5188862a(
    arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c8359998ff8f774202e1b0869097e19c3e167e8e7a6a5ee95936f1b09f063b8(
    construct: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75ec54ba33468f397b4b954ffff5bb4a26a29e306b38c37a8a831233ca47cf40(
    table: _ITable_504fd401,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfac18ef33642ed976be7473c0fe4b5174e370a770ceabc690e397bcecfce6a3(
    instance: _IInstance_ab239e7c,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a724b31752318e43681480d257f284af035f11db8b7b91a2712b0a19a09283b(
    file_system: _IFileSystem_b2d3a7cb,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2043352654f5d7b0272be6002773b2263d7a3a58bb3ca681d050846773b6a7a4(
    cluster: _IDatabaseCluster_6554c32b,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3a85f96e06b0e43fed194c604af81aa14d506827b7f57b6fef4f8e0191d38d1(
    instance: _IDatabaseInstance_e4cb03a8,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a96658ef472d54f85f9fb6dfeffb763befda835ec279615ad329c159e5acf1a6(
    cluster: _IServerlessCluster_adbbb720,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c47a77dd61236c04d92fba31585e4ea943b8bb7dfce2ab0dc2f09ab9bd172316(
    key: builtins.str,
    value: builtins.str,
    operation: typing.Optional[TagOperation] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb124dbc539b313053b8d36e3fbbda7c8ef513917e5cdb41a9d2a7ecaaca7643(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    backup_plan: IBackupPlan,
    resources: typing.Sequence[BackupResource],
    allow_restores: typing.Optional[builtins.bool] = None,
    backup_selection_name: typing.Optional[builtins.str] = None,
    disable_default_backup_policy: typing.Optional[builtins.bool] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99c0cf23958862e40e3aaa86170756388807569db1aeb820435bca2898ff496c(
    *,
    resources: typing.Sequence[BackupResource],
    allow_restores: typing.Optional[builtins.bool] = None,
    backup_selection_name: typing.Optional[builtins.str] = None,
    disable_default_backup_policy: typing.Optional[builtins.bool] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd3a38c041da3373a6278620797d45b4058a0d5aede2c0a4bc706fdeff586bc8(
    *,
    resources: typing.Sequence[BackupResource],
    allow_restores: typing.Optional[builtins.bool] = None,
    backup_selection_name: typing.Optional[builtins.str] = None,
    disable_default_backup_policy: typing.Optional[builtins.bool] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    backup_plan: IBackupPlan,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a7555f4b25ca4760e3a057b8e3a9b5e07feed1f99319d6e434cc8fed4e71af6(
    *,
    access_policy: typing.Optional[_PolicyDocument_3ac34393] = None,
    backup_vault_name: typing.Optional[builtins.str] = None,
    block_recovery_point_deletion: typing.Optional[builtins.bool] = None,
    encryption_key: typing.Optional[_IKey_5f11635f] = None,
    lock_configuration: typing.Optional[typing.Union[LockConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    notification_events: typing.Optional[typing.Sequence[BackupVaultEvents]] = None,
    notification_topic: typing.Optional[_ITopic_9eca4852] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8250888ac08b345ef300cc4ce53cc267858e31401cdc7b6a427c98f5b05a644a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    backup_plan: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBackupPlan.BackupPlanResourceTypeProperty, typing.Dict[builtins.str, typing.Any]]],
    backup_plan_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff313ad9e84c3475e4286a17d3e066d3b8ff12dcdde29c7a2727bf7529fa7fbb(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__629c13605c998df9d353c86512eb681d4a36a976085dd6b817284d7c538366bf(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6bcd3444e7d21cd081d514b722a886bbe4d7a7b6f5d932136467b22b0e106cb(
    value: typing.Union[_IResolvable_da3f097b, CfnBackupPlan.BackupPlanResourceTypeProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb59689e4858e7d33cb520f2ac89e6fb2e87b5adf8cc0ba009807aac7f9f269b(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adac2a2fa454c7ba68def940750a72e610647ccbdd2ff4bbb5b5a2aa0137684c(
    *,
    backup_options: typing.Any,
    resource_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fa711ce952ba97854872fd98c8f8e371b8e208c6e6c6d9d96087f413097338f(
    *,
    backup_plan_name: builtins.str,
    backup_plan_rule: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBackupPlan.BackupRuleResourceTypeProperty, typing.Dict[builtins.str, typing.Any]]]]],
    advanced_backup_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBackupPlan.AdvancedBackupSettingResourceTypeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a15d5028e47f5757a8c2319a31ccf993bd398f0a4476991c75f1e1c3b52e84b2(
    *,
    rule_name: builtins.str,
    target_backup_vault: builtins.str,
    completion_window_minutes: typing.Optional[jsii.Number] = None,
    copy_actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBackupPlan.CopyActionResourceTypeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    enable_continuous_backup: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    lifecycle: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBackupPlan.LifecycleResourceTypeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    recovery_point_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    schedule_expression: typing.Optional[builtins.str] = None,
    schedule_expression_timezone: typing.Optional[builtins.str] = None,
    start_window_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0175b5c6dd7a96151259f5cc498692c56086843795ca19e3f9f696707f1d48a(
    *,
    destination_backup_vault_arn: builtins.str,
    lifecycle: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBackupPlan.LifecycleResourceTypeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9cc85d565a0bdd44f5b8b5d29dce7bae38cfd50437c39a049e1b16bd8a24c1e(
    *,
    delete_after_days: typing.Optional[jsii.Number] = None,
    move_to_cold_storage_after_days: typing.Optional[jsii.Number] = None,
    opt_in_to_archive_for_supported_resources: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38320d1a2a15443c671b35047636824301e490f9e4406be550e214bb8dea25d8(
    *,
    backup_plan: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBackupPlan.BackupPlanResourceTypeProperty, typing.Dict[builtins.str, typing.Any]]],
    backup_plan_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__436ffdeb945f1d3144a7bb788e19b389a62e6e70ce5e213a46bb8c9ea289c07f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    backup_plan_id: builtins.str,
    backup_selection: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBackupSelection.BackupSelectionResourceTypeProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b980d8bc69846edd28b19d93b1e66494af7417d2c8bfcc63913b9bf28df47fa(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c986b57932b74d2da2b1f64dec5155c7fdf62e7a88a73fb7936731938fa34e00(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb392f817509871513c4b0fafb43edac23006950a5084d282e3b5261b24f5603(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c50a31cd4319cd1c025574f4d4937c890776ab110ae28de39672caf7d2e4b86b(
    value: typing.Union[_IResolvable_da3f097b, CfnBackupSelection.BackupSelectionResourceTypeProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53f9191660f873982da4ff5df24ce6724761f33be21d9fd33f43da81cca720c0(
    *,
    iam_role_arn: builtins.str,
    selection_name: builtins.str,
    conditions: typing.Any = None,
    list_of_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBackupSelection.ConditionResourceTypeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    not_resources: typing.Optional[typing.Sequence[builtins.str]] = None,
    resources: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7fe06535a46bfa87352df9bd09ca629b6962d225411249a065f4ba72647b33a(
    *,
    condition_key: typing.Optional[builtins.str] = None,
    condition_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__346e9a31a7a4a5ad318acaee89a646b6b23822feb831da857c4c300731df22c9(
    *,
    condition_key: builtins.str,
    condition_type: builtins.str,
    condition_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4989780545fff72ed41947c50d0e49cf85d2cf412bc84422f8757131068aa57(
    *,
    string_equals: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBackupSelection.ConditionParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    string_like: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBackupSelection.ConditionParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    string_not_equals: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBackupSelection.ConditionParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    string_not_like: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBackupSelection.ConditionParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62d83c7c1dd04eb3d32a7eb1179b31577aa76122fb844fd17ddef00d8ef261c9(
    *,
    backup_plan_id: builtins.str,
    backup_selection: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBackupSelection.BackupSelectionResourceTypeProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91f579bea882f82608d503a3e561568131d8e8e6d825c152c63d596228cb1283(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    backup_vault_name: builtins.str,
    access_policy: typing.Any = None,
    backup_vault_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    encryption_key_arn: typing.Optional[builtins.str] = None,
    lock_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBackupVault.LockConfigurationTypeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    notifications: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBackupVault.NotificationObjectTypeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5303f64257feccbaac430e6766ee8dd85d8293dcda5a0b514f9128fa193e156(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29e9aaac48a3b884ecef6959c7ece545318b968f28907af6d6f9ef8a7be5eca5(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efe38ab6a95c28a99f2a827659f4327017e61fc72434108ce384f3b817de14be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2658b3b3b3e44ef30d5a8cb2081ad397d0fcb37c7f096da80902213d302577e6(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2f59a90eb93017be4632c741610e42551c72baea27b40db6f4ee7a97d80f0dc(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0b723f932eeee018a3da33f56242664a27dbe5da02fc1a2ca3fef2169b24096(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c2b8e8d837c9ecececc40d52f27a016b926cd8c10c242b093a3f7cf0d24407a(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBackupVault.LockConfigurationTypeProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd703ee9b654a333d2dac663658fcec508ffab2fc620c932c524dcd0df84e35e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBackupVault.NotificationObjectTypeProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6838c822361ad0f655e1f64f503799de6da67231ac1aa7e8b88f548f690295d8(
    *,
    min_retention_days: jsii.Number,
    changeable_for_days: typing.Optional[jsii.Number] = None,
    max_retention_days: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1a218026ba958c0d56b8c624f104b73e68fb60c3d3ea03864a8affbd11f0090(
    *,
    backup_vault_events: typing.Sequence[builtins.str],
    sns_topic_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8f4cc95a208ae1aaf01a8bfd7ead0ecbd6d7559786be34f0a6087355d66ca28(
    *,
    backup_vault_name: builtins.str,
    access_policy: typing.Any = None,
    backup_vault_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    encryption_key_arn: typing.Optional[builtins.str] = None,
    lock_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBackupVault.LockConfigurationTypeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    notifications: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBackupVault.NotificationObjectTypeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__762b6f2cf173ed987e2f05e55b691e4e8e14552591e05b26b7f7f4e08e3c739d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    framework_controls: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFramework.FrameworkControlProperty, typing.Dict[builtins.str, typing.Any]]]]],
    framework_description: typing.Optional[builtins.str] = None,
    framework_name: typing.Optional[builtins.str] = None,
    framework_tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__772cf75dbb4416fa5340091bf8716f709bcd79a3fef3bf9744a593360d85b617(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fec0fb3c848f86413b75960fc140604dfee8403702a31925ae61dc8c73e9879(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3915617d48c3c99a3779ed995d74734c2f731d452cc340e149dd92de02e68dc6(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFramework.FrameworkControlProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9208446adcef370a60eb7a60602ec6f41c22bd0a8094a6e9276f8c9dc50ce211(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5b6c11306aa239f885eed40f25fa93c3a57a2c996e35e5a03b218b580a69caf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d4922912c7db9cfb847d446edf6701acea095c2d0fefb7def73f3da3aa1cc1d(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dab5ceb07bfb68ba9a8118e37c2455f99ed12c16a7af1c7b9630695eaee92261(
    *,
    parameter_name: builtins.str,
    parameter_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2f11947bed37971122729e32bbef595427b4ad564167fe2e94024e5751025f0(
    *,
    compliance_resource_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    compliance_resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2629d2cfa8ee3e24a49017e656aec6745967bedbc91fb85dae3a38dfe31fbb23(
    *,
    control_name: builtins.str,
    control_input_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFramework.ControlInputParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    control_scope: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a04013c0cacc7cf95b5f7954572128dbc2c4529bb364b61a38c324e4d52b5fd7(
    *,
    framework_controls: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFramework.FrameworkControlProperty, typing.Dict[builtins.str, typing.Any]]]]],
    framework_description: typing.Optional[builtins.str] = None,
    framework_name: typing.Optional[builtins.str] = None,
    framework_tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c6528de906751786b24f01244334abf14ddb763be763a416a6d4f3c8b779828(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    report_delivery_channel: typing.Any,
    report_setting: typing.Any,
    report_plan_description: typing.Optional[builtins.str] = None,
    report_plan_name: typing.Optional[builtins.str] = None,
    report_plan_tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f16e67dc9d6ebba3468d37c10baab99ff7e531b9adb1ec5e7f3259c7c6f7f9aa(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c7b68d11abde2aa0d9a37b0c93b72ae7b52fee9f08d4f38397745e4d72f524f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f59e4877274d33fdd0b7b625f974f6963731efadb02eb1735d077c10708f32a(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f16d9fa0a96dbb11b2af025cb683de73134d878e6b6aa892388da1b0ba219734(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd7915156dce61fe52d1f2c30121d3b6944167aaa29a3d385bd84dc1027de25a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ac2566ae00a72a2736504779f108399d133fb5744a76f8690cb6e5a7a85a8bc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16e4bb4b012408e08ab26526c9837368cc6121e55f663b4a10170c9edb8466f8(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c24b871d5606676d6a9c03353da61f5c6dd25f1faa08da3b2350be2abc2960e9(
    *,
    s3_bucket_name: builtins.str,
    formats: typing.Optional[typing.Sequence[builtins.str]] = None,
    s3_key_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f82410dd1600e96bdbb1b09d2f427b262b59db1aee2a2d8a69b04a7c45213f39(
    *,
    report_template: builtins.str,
    accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
    framework_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    organization_units: typing.Optional[typing.Sequence[builtins.str]] = None,
    regions: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afbe22eade35dfb4647750a128ae7ae610bb82584420423ce86400329eeb84d9(
    *,
    report_delivery_channel: typing.Any,
    report_setting: typing.Any,
    report_plan_description: typing.Optional[builtins.str] = None,
    report_plan_name: typing.Optional[builtins.str] = None,
    report_plan_tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce1d12683247bbd0bcd185e807f3b41b4b53ee7cfd847d57ecbf875d4e7c017f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    recovery_point_selection: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRestoreTestingPlan.RestoreTestingRecoveryPointSelectionProperty, typing.Dict[builtins.str, typing.Any]]],
    restore_testing_plan_name: builtins.str,
    schedule_expression: builtins.str,
    schedule_expression_timezone: typing.Optional[builtins.str] = None,
    start_window_hours: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5ba5ffd43036caff767719ec070ceb8bbd591fd4d39ca36636cd2d29d4a56ff(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6702caf44f3579436a6db3b23da78e6d5e41775573ce62e2e8078955e933edbd(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__469f816a79c521b1d05c16d66ccb2fb6a0fe1163701e6173b0840fee4d922c49(
    value: typing.Union[_IResolvable_da3f097b, CfnRestoreTestingPlan.RestoreTestingRecoveryPointSelectionProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6269ad4a6dda73789ac04d7e345263bf14c4a20f6442d99fbd191aeb740ccbe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__feb7dec7f23768db6fb25c010ce6d88323b9a74c117f6237056d65ed8bc1b49b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45df227f118297319531c266e28ed0c7920e380fc44ad9f041510f5e6aeef7ef(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9df0eb1aaa95a7ca07b1c2dc88007e89e56d90a6006630d5680cdb415dd093f9(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93b4eb4b15380d36fec202a3d3c50a366e86616c5516db286f16625d21096205(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5c7325bf12ffdf44c2a91f87260dec7090351b3a614521cad6d903cf2ee98bf(
    *,
    algorithm: builtins.str,
    include_vaults: typing.Sequence[builtins.str],
    recovery_point_types: typing.Sequence[builtins.str],
    exclude_vaults: typing.Optional[typing.Sequence[builtins.str]] = None,
    selection_window_days: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d65b2884e40d5939ab5441a32efe6879390155bd000dab9e921f71ac415b50f5(
    *,
    recovery_point_selection: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRestoreTestingPlan.RestoreTestingRecoveryPointSelectionProperty, typing.Dict[builtins.str, typing.Any]]],
    restore_testing_plan_name: builtins.str,
    schedule_expression: builtins.str,
    schedule_expression_timezone: typing.Optional[builtins.str] = None,
    start_window_hours: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcf5b783f910e19031573c45aeb82865ab4fa2145dd36242b383df442b55b4cd(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    iam_role_arn: builtins.str,
    protected_resource_type: builtins.str,
    restore_testing_plan_name: builtins.str,
    restore_testing_selection_name: builtins.str,
    protected_resource_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    protected_resource_conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRestoreTestingSelection.ProtectedResourceConditionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    restore_metadata_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    validation_window_hours: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6d08475ef8ec086062770da8c6ae1e386a46bcdff9dfb5040b7f1493611cb3e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34de78e7710b49a3b42ef7d51f2dfc0e53d42cd2f7a806ece05933ad0dd33be4(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34257f3d99d8dd81dd7c1970745d4963406e9997794afa2eaa58e5f3091981d1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6719783d182adbeb22a96172d51be6ee382ad7651dee643d5a90d3cb2adff232(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac3b68fe5b51b83a59b83e052ca08ca16d71cb6968805dd38de621c693f4dc59(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c01d71d9386b9d1b2bb36875e5603d6b15b83bc54c7690640a18bdbe764a8ec9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e6805582b6d06e09dd1dcb088e5e9cda91f926647460866a9ee4aaf1b53c5db(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bca09c3c518b6d44e5cb2086f38f9235f25ef7744e3c6cfba7d01b48e73b989(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRestoreTestingSelection.ProtectedResourceConditionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9afb00368be90e46cf02ec2498547553cd056db449734f0be5d5877e388c4af5(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2be1604fc1c4809e8243d2870eda79b55ab549c0f8a8368d99aded8cda271d1(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab32bbff81cfbfeb46780f1db32ce34c7ddfe0658843461e3c5e6ddccc176c3d(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21f4334cd0e11f4b24684e9ff9cf575380c735e9265b95d69aa611aae88b0a78(
    *,
    string_equals: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRestoreTestingSelection.KeyValueProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    string_not_equals: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRestoreTestingSelection.KeyValueProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd755bb9b5c3f12e065d4bb10b1805bc3571946724f1d8f52794cc5491212cdb(
    *,
    iam_role_arn: builtins.str,
    protected_resource_type: builtins.str,
    restore_testing_plan_name: builtins.str,
    restore_testing_selection_name: builtins.str,
    protected_resource_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    protected_resource_conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRestoreTestingSelection.ProtectedResourceConditionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    restore_metadata_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    validation_window_hours: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f046e29be9f6222e2ff343629e5ca635543c7abc067c609446b86467be6c5b68(
    grantee: _IGrantable_71c4f5de,
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f8085843c1a2a230e0c965fbb91f96b1b11b817ee7d9232b4d368b4767e6681(
    *,
    min_retention: _Duration_4839e8c3,
    changeable_for: typing.Optional[_Duration_4839e8c3] = None,
    max_retention: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebec77480ee4239c5e74e693ea6942bce079e6a195e1db4021330679f19a3080(
    *,
    key: builtins.str,
    value: builtins.str,
    operation: typing.Optional[TagOperation] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac9eeb1158690e76fc800429198c84b42bf4dc68c223e34e743ca5c3de83102d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    backup_plan_name: typing.Optional[builtins.str] = None,
    backup_plan_rules: typing.Optional[typing.Sequence[BackupPlanRule]] = None,
    backup_vault: typing.Optional[IBackupVault] = None,
    windows_vss: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17983f2742df72bf64d28b678e89a057f2b1feed375c39a562e042faadaf8668(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    backup_vault: typing.Optional[IBackupVault] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bb65bf5b0ac30cf59b76bfc6b0fd6a5c44fe614f682166d81e998f4dd87179a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    backup_vault: typing.Optional[IBackupVault] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e80dbcebd876b060051ccd746c3d678b6857f64ed24fda01e09c953ebbc3199c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    backup_vault: typing.Optional[IBackupVault] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__564733017434e9f62e49bb99610f3dd11fc4692ba00892447d2c38e0be976290(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    backup_vault: typing.Optional[IBackupVault] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9d7e2dd359a33f71d62dc691f0b94d1443cc763901092b01ca933df0c543219(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    backup_plan_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__398b9447d6dff004e80a6df5262bac01ef5f8f5af47ef115c710b218e23791df(
    rule: BackupPlanRule,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__588f53b2d13b2b789941caeafb53933090659574015281ee228d0d35b924172b(
    id: builtins.str,
    *,
    resources: typing.Sequence[BackupResource],
    allow_restores: typing.Optional[builtins.bool] = None,
    backup_selection_name: typing.Optional[builtins.str] = None,
    disable_default_backup_policy: typing.Optional[builtins.bool] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5938cd051d17a4aa98a61f204449a9c4416544ba91e3c4e4821b784b40ffc921(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    access_policy: typing.Optional[_PolicyDocument_3ac34393] = None,
    backup_vault_name: typing.Optional[builtins.str] = None,
    block_recovery_point_deletion: typing.Optional[builtins.bool] = None,
    encryption_key: typing.Optional[_IKey_5f11635f] = None,
    lock_configuration: typing.Optional[typing.Union[LockConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    notification_events: typing.Optional[typing.Sequence[BackupVaultEvents]] = None,
    notification_topic: typing.Optional[_ITopic_9eca4852] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58170569b5f8f6dd33d5d700cfb73499de3162167c227fa90c30956f0160a753(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    backup_vault_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdc42d68a7099dab372cd0e3291aa3e3a7794912bbd2c7df2a059b1c39cc0e40(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    backup_vault_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e100029ccf44a7b32d3531902bcf8361f5e0f4bf872de45a759df0cb251ea175(
    statement: _PolicyStatement_0fe33853,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6f51b6b852524375032f5dd45b5c00d5d86423092d20d599599a38ce40675a8(
    grantee: _IGrantable_71c4f5de,
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
