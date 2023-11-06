'''
# Amazon Elastic File System Construct Library

[Amazon Elastic File System](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html) (Amazon EFS) provides a simple, scalable,
fully managed elastic NFS file system for use with AWS Cloud services and on-premises resources.
Amazon EFS provides file storage in the AWS Cloud. With Amazon EFS, you can create a file system,
mount the file system on an Amazon EC2 instance, and then read and write data to and from your file system.

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

## File Systems

Amazon EFS provides elastic, shared file storage that is POSIX-compliant. The file system you create
supports concurrent read and write access from multiple Amazon EC2 instances and is accessible from
all of the Availability Zones in the AWS Region where it is created. Learn more about [EFS file systems](https://docs.aws.amazon.com/efs/latest/ug/creating-using.html)

### Create an Amazon EFS file system

A Virtual Private Cloud (VPC) is required to create an Amazon EFS file system.
The following example creates a file system that is encrypted at rest, running in `General Purpose`
performance mode, and `Bursting` throughput mode and does not transition files to the Infrequent
Access (IA) storage class.

```python
file_system = efs.FileSystem(self, "MyEfsFileSystem",
    vpc=ec2.Vpc(self, "VPC"),
    lifecycle_policy=efs.LifecyclePolicy.AFTER_14_DAYS,  # files are not transitioned to infrequent access (IA) storage by default
    performance_mode=efs.PerformanceMode.GENERAL_PURPOSE,  # default
    out_of_infrequent_access_policy=efs.OutOfInfrequentAccessPolicy.AFTER_1_ACCESS
)
```

⚠️ An Amazon EFS file system's performance mode can't be MAX_IO when its throughputMode is ELASTIC.

⚠️ An Amazon EFS file system's performance mode can't be changed after the file system has been created.
Updating this property will replace the file system.

Any file system that has been created outside the stack can be imported into your CDK app.

Use the `fromFileSystemAttributes()` API to import an existing file system.
Here is an example of giving a role write permissions on a file system.

```python
import aws_cdk.aws_iam as iam


imported_file_system = efs.FileSystem.from_file_system_attributes(self, "existingFS",
    file_system_id="fs-12345678",  # You can also use fileSystemArn instead of fileSystemId.
    security_group=ec2.SecurityGroup.from_security_group_id(self, "SG", "sg-123456789",
        allow_all_outbound=False
    )
)
```

### IAM to control file system data access

You can use both IAM identity policies and resource policies to control client access to Amazon EFS resources in a way that is scalable and optimized for cloud environments. Using IAM, you can permit clients to perform specific actions on a file system, including read-only, write, and root access.

```python
import aws_cdk.aws_iam as iam


my_file_system_policy = iam.PolicyDocument(
    statements=[iam.PolicyStatement(
        actions=["elasticfilesystem:ClientWrite", "elasticfilesystem:ClientMount"
        ],
        principals=[iam.AccountRootPrincipal()],
        resources=["*"],
        conditions={
            "Bool": {
                "elasticfilesystem:AccessedViaMountTarget": "true"
            }
        }
    )]
)

file_system = efs.FileSystem(self, "MyEfsFileSystem",
    vpc=ec2.Vpc(self, "VPC"),
    file_system_policy=my_file_system_policy
)
```

Alternatively, a resource policy can be added later using `addToResourcePolicy(statement)`. Note that this will not work with imported FileSystem.

```python
import aws_cdk.aws_iam as iam

# statement: iam.PolicyStatement

file_system = efs.FileSystem(self, "MyEfsFileSystem",
    vpc=ec2.Vpc(self, "VPC")
)

file_system.add_to_resource_policy(statement)
```

### Permissions

If you need to grant file system permissions to another resource, you can use the `.grant()` API.
As an example, the following code gives `elasticfilesystem:ClientWrite` permissions to an IAM role.

```python
role = iam.Role(self, "Role",
    assumed_by=iam.AnyPrincipal()
)

file_system.grant(role, "elasticfilesystem:ClientWrite")
```

### Access Point

An access point is an application-specific view into an EFS file system that applies an operating
system user and group, and a file system path, to any file system request made through the access
point. The operating system user and group override any identity information provided by the NFS
client. The file system path is exposed as the access point's root directory. Applications using
the access point can only access data in its own directory and below. To learn more, see [Mounting a File System Using EFS Access Points](https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html).

Use the `addAccessPoint` API to create an access point from a fileSystem.

```python
file_system.add_access_point("AccessPoint")
```

By default, when you create an access point, the root(`/`) directory is exposed to the client
connecting to the access point. You can specify a custom path with the `path` property.

If `path` does not exist, it will be created with the settings defined in the `creationInfo`.
See [Creating Access Points](https://docs.aws.amazon.com/efs/latest/ug/create-access-point.html) for more details.

Any access point that has been created outside the stack can be imported into your CDK app.

Use the `fromAccessPointAttributes()` API to import an existing access point.

```python
efs.AccessPoint.from_access_point_attributes(self, "ap",
    access_point_id="fsap-1293c4d9832fo0912",
    file_system=efs.FileSystem.from_file_system_attributes(self, "efs",
        file_system_id="fs-099d3e2f",
        security_group=ec2.SecurityGroup.from_security_group_id(self, "sg", "sg-51530134")
    )
)
```

⚠️ Notice: When importing an Access Point using `fromAccessPointAttributes()`, you must make sure
the mount targets are deployed and their lifecycle state is `available`. Otherwise, you may encounter
the following error when deploying:

> EFS file system <ARN of efs> referenced by access point <ARN of access point of EFS> has
> mount targets created in all availability zones the function will execute in, but not all
> are in the available life cycle state yet. Please wait for them to become available and
> try the request again.

### Connecting

To control who can access the EFS, use the `.connections` attribute. EFS has
a fixed default port, so you don't need to specify the port:

```python
file_system.connections.allow_default_port_from(instance)
```

Learn more about [managing file system network accessibility](https://docs.aws.amazon.com/efs/latest/ug/manage-fs-access.html)

### Mounting the file system using User Data

After you create a file system, you can create mount targets. Then you can mount the file system on
EC2 instances, containers, and Lambda functions in your virtual private cloud (VPC).

The following example automatically mounts a file system during instance launch.

```python
file_system.connections.allow_default_port_from(instance)

instance.user_data.add_commands("yum check-update -y", "yum upgrade -y", "yum install -y amazon-efs-utils", "yum install -y nfs-utils", "file_system_id_1=" + file_system.file_system_id, "efs_mount_point_1=/mnt/efs/fs1", "mkdir -p \"${efs_mount_point_1}\"", "test -f \"/sbin/mount.efs\" && echo \"${file_system_id_1}:/ ${efs_mount_point_1} efs defaults,_netdev\" >> /etc/fstab || " + "echo \"${file_system_id_1}.efs." + Stack.of(self).region + ".amazonaws.com:/ ${efs_mount_point_1} nfs4 nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport,_netdev 0 0\" >> /etc/fstab", "mount -a -t efs,nfs4 defaults")
```

Learn more about [mounting EFS file systems](https://docs.aws.amazon.com/efs/latest/ug/mounting-fs.html)

### Deleting

Since file systems are stateful resources, by default the file system will not be deleted when your
stack is deleted.

You can configure the file system to be destroyed on stack deletion by setting a `removalPolicy`

```python
file_system = efs.FileSystem(self, "EfsFileSystem",
    vpc=ec2.Vpc(self, "VPC"),
    removal_policy=RemovalPolicy.DESTROY
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
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    IResource as _IResource_c80c4260,
    ITaggable as _ITaggable_36806126,
    RemovalPolicy as _RemovalPolicy_9f93c814,
    Resource as _Resource_45bc6135,
    Size as _Size_7b441c34,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..aws_ec2 import (
    Connections as _Connections_0f31fce8,
    IConnectable as _IConnectable_10015a05,
    ISecurityGroup as _ISecurityGroup_acf8a799,
    IVpc as _IVpc_f30d5663,
    SubnetSelection as _SubnetSelection_e57d76df,
)
from ..aws_iam import (
    AddToResourcePolicyResult as _AddToResourcePolicyResult_1d0a53ad,
    Grant as _Grant_a7ae64f8,
    IGrantable as _IGrantable_71c4f5de,
    IResourceWithPolicy as _IResourceWithPolicy_720d64fc,
    PolicyDocument as _PolicyDocument_3ac34393,
    PolicyStatement as _PolicyStatement_0fe33853,
)
from ..aws_kms import IKey as _IKey_5f11635f


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_efs.AccessPointAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "access_point_arn": "accessPointArn",
        "access_point_id": "accessPointId",
        "file_system": "fileSystem",
    },
)
class AccessPointAttributes:
    def __init__(
        self,
        *,
        access_point_arn: typing.Optional[builtins.str] = None,
        access_point_id: typing.Optional[builtins.str] = None,
        file_system: typing.Optional["IFileSystem"] = None,
    ) -> None:
        '''Attributes that can be specified when importing an AccessPoint.

        :param access_point_arn: The ARN of the AccessPoint One of this, or ``accessPointId`` is required. Default: - determined based on accessPointId
        :param access_point_id: The ID of the AccessPoint One of this, or ``accessPointArn`` is required. Default: - determined based on accessPointArn
        :param file_system: The EFS file system. Default: - no EFS file system

        :exampleMetadata: infused

        Example::

            efs.AccessPoint.from_access_point_attributes(self, "ap",
                access_point_id="fsap-1293c4d9832fo0912",
                file_system=efs.FileSystem.from_file_system_attributes(self, "efs",
                    file_system_id="fs-099d3e2f",
                    security_group=ec2.SecurityGroup.from_security_group_id(self, "sg", "sg-51530134")
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7d29db03188d21de563fa9ac94c4de056afa5ee45616d3e16e4b53de731bedd)
            check_type(argname="argument access_point_arn", value=access_point_arn, expected_type=type_hints["access_point_arn"])
            check_type(argname="argument access_point_id", value=access_point_id, expected_type=type_hints["access_point_id"])
            check_type(argname="argument file_system", value=file_system, expected_type=type_hints["file_system"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if access_point_arn is not None:
            self._values["access_point_arn"] = access_point_arn
        if access_point_id is not None:
            self._values["access_point_id"] = access_point_id
        if file_system is not None:
            self._values["file_system"] = file_system

    @builtins.property
    def access_point_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the AccessPoint One of this, or ``accessPointId`` is required.

        :default: - determined based on accessPointId
        '''
        result = self._values.get("access_point_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def access_point_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the AccessPoint One of this, or ``accessPointArn`` is required.

        :default: - determined based on accessPointArn
        '''
        result = self._values.get("access_point_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_system(self) -> typing.Optional["IFileSystem"]:
        '''The EFS file system.

        :default: - no EFS file system
        '''
        result = self._values.get("file_system")
        return typing.cast(typing.Optional["IFileSystem"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPointAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_efs.AccessPointOptions",
    jsii_struct_bases=[],
    name_mapping={
        "create_acl": "createAcl",
        "path": "path",
        "posix_user": "posixUser",
    },
)
class AccessPointOptions:
    def __init__(
        self,
        *,
        create_acl: typing.Optional[typing.Union["Acl", typing.Dict[builtins.str, typing.Any]]] = None,
        path: typing.Optional[builtins.str] = None,
        posix_user: typing.Optional[typing.Union["PosixUser", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Options to create an AccessPoint.

        :param create_acl: Specifies the POSIX IDs and permissions to apply when creating the access point's root directory. If the root directory specified by ``path`` does not exist, EFS creates the root directory and applies the permissions specified here. If the specified ``path`` does not exist, you must specify ``createAcl``. Default: - None. The directory specified by ``path`` must exist.
        :param path: Specifies the path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system. Default: '/'
        :param posix_user: The full POSIX identity, including the user ID, group ID, and any secondary group IDs, on the access point that is used for all file system operations performed by NFS clients using the access point. Specify this to enforce a user identity using an access point. Default: - user identity not enforced

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_ec2 as ec2
            import aws_cdk.aws_efs as efs
            
            
            # create a new VPC
            vpc = ec2.Vpc(self, "VPC")
            
            # create a new Amazon EFS filesystem
            file_system = efs.FileSystem(self, "Efs", vpc=vpc)
            
            # create a new access point from the filesystem
            access_point = file_system.add_access_point("AccessPoint",
                # set /export/lambda as the root of the access point
                path="/export/lambda",
                # as /export/lambda does not exist in a new efs filesystem, the efs will create the directory with the following createAcl
                create_acl=efs.Acl(
                    owner_uid="1001",
                    owner_gid="1001",
                    permissions="750"
                ),
                # enforce the POSIX identity so lambda function will access with this identity
                posix_user=efs.PosixUser(
                    uid="1001",
                    gid="1001"
                )
            )
            
            fn = lambda_.Function(self, "MyLambda",
                # mount the access point to /mnt/msg in the lambda runtime environment
                filesystem=lambda_.FileSystem.from_efs_access_point(access_point, "/mnt/msg"),
                runtime=lambda_.Runtime.NODEJS_18_X,
                handler="index.handler",
                code=lambda_.Code.from_asset(path.join(__dirname, "lambda-handler")),
                vpc=vpc
            )
        '''
        if isinstance(create_acl, dict):
            create_acl = Acl(**create_acl)
        if isinstance(posix_user, dict):
            posix_user = PosixUser(**posix_user)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__913ac22cf5c450fc4c0b0a7b6d77a1e412a1276f6c512fbacf766f6ab3a7d900)
            check_type(argname="argument create_acl", value=create_acl, expected_type=type_hints["create_acl"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument posix_user", value=posix_user, expected_type=type_hints["posix_user"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create_acl is not None:
            self._values["create_acl"] = create_acl
        if path is not None:
            self._values["path"] = path
        if posix_user is not None:
            self._values["posix_user"] = posix_user

    @builtins.property
    def create_acl(self) -> typing.Optional["Acl"]:
        '''Specifies the POSIX IDs and permissions to apply when creating the access point's root directory.

        If the
        root directory specified by ``path`` does not exist, EFS creates the root directory and applies the
        permissions specified here. If the specified ``path`` does not exist, you must specify ``createAcl``.

        :default: - None. The directory specified by ``path`` must exist.
        '''
        result = self._values.get("create_acl")
        return typing.cast(typing.Optional["Acl"], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Specifies the path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system.

        :default: '/'
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def posix_user(self) -> typing.Optional["PosixUser"]:
        '''The full POSIX identity, including the user ID, group ID, and any secondary group IDs, on the access point that is used for all file system operations performed by NFS clients using the access point.

        Specify this to enforce a user identity using an access point.

        :default: - user identity not enforced

        :see: - `Enforcing a User Identity Using an Access Point <https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html>`_
        '''
        result = self._values.get("posix_user")
        return typing.cast(typing.Optional["PosixUser"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPointOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_efs.AccessPointProps",
    jsii_struct_bases=[AccessPointOptions],
    name_mapping={
        "create_acl": "createAcl",
        "path": "path",
        "posix_user": "posixUser",
        "file_system": "fileSystem",
    },
)
class AccessPointProps(AccessPointOptions):
    def __init__(
        self,
        *,
        create_acl: typing.Optional[typing.Union["Acl", typing.Dict[builtins.str, typing.Any]]] = None,
        path: typing.Optional[builtins.str] = None,
        posix_user: typing.Optional[typing.Union["PosixUser", typing.Dict[builtins.str, typing.Any]]] = None,
        file_system: "IFileSystem",
    ) -> None:
        '''Properties for the AccessPoint.

        :param create_acl: Specifies the POSIX IDs and permissions to apply when creating the access point's root directory. If the root directory specified by ``path`` does not exist, EFS creates the root directory and applies the permissions specified here. If the specified ``path`` does not exist, you must specify ``createAcl``. Default: - None. The directory specified by ``path`` must exist.
        :param path: Specifies the path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system. Default: '/'
        :param posix_user: The full POSIX identity, including the user ID, group ID, and any secondary group IDs, on the access point that is used for all file system operations performed by NFS clients using the access point. Specify this to enforce a user identity using an access point. Default: - user identity not enforced
        :param file_system: The efs filesystem.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_efs as efs
            
            # file_system: efs.FileSystem
            
            access_point_props = efs.AccessPointProps(
                file_system=file_system,
            
                # the properties below are optional
                create_acl=efs.Acl(
                    owner_gid="ownerGid",
                    owner_uid="ownerUid",
                    permissions="permissions"
                ),
                path="path",
                posix_user=efs.PosixUser(
                    gid="gid",
                    uid="uid",
            
                    # the properties below are optional
                    secondary_gids=["secondaryGids"]
                )
            )
        '''
        if isinstance(create_acl, dict):
            create_acl = Acl(**create_acl)
        if isinstance(posix_user, dict):
            posix_user = PosixUser(**posix_user)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32b9cfe4790278ebfef38060a79ab8e87662b5508943b46c7da6a219e5bc224e)
            check_type(argname="argument create_acl", value=create_acl, expected_type=type_hints["create_acl"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument posix_user", value=posix_user, expected_type=type_hints["posix_user"])
            check_type(argname="argument file_system", value=file_system, expected_type=type_hints["file_system"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "file_system": file_system,
        }
        if create_acl is not None:
            self._values["create_acl"] = create_acl
        if path is not None:
            self._values["path"] = path
        if posix_user is not None:
            self._values["posix_user"] = posix_user

    @builtins.property
    def create_acl(self) -> typing.Optional["Acl"]:
        '''Specifies the POSIX IDs and permissions to apply when creating the access point's root directory.

        If the
        root directory specified by ``path`` does not exist, EFS creates the root directory and applies the
        permissions specified here. If the specified ``path`` does not exist, you must specify ``createAcl``.

        :default: - None. The directory specified by ``path`` must exist.
        '''
        result = self._values.get("create_acl")
        return typing.cast(typing.Optional["Acl"], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Specifies the path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system.

        :default: '/'
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def posix_user(self) -> typing.Optional["PosixUser"]:
        '''The full POSIX identity, including the user ID, group ID, and any secondary group IDs, on the access point that is used for all file system operations performed by NFS clients using the access point.

        Specify this to enforce a user identity using an access point.

        :default: - user identity not enforced

        :see: - `Enforcing a User Identity Using an Access Point <https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html>`_
        '''
        result = self._values.get("posix_user")
        return typing.cast(typing.Optional["PosixUser"], result)

    @builtins.property
    def file_system(self) -> "IFileSystem":
        '''The efs filesystem.'''
        result = self._values.get("file_system")
        assert result is not None, "Required property 'file_system' is missing"
        return typing.cast("IFileSystem", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_efs.Acl",
    jsii_struct_bases=[],
    name_mapping={
        "owner_gid": "ownerGid",
        "owner_uid": "ownerUid",
        "permissions": "permissions",
    },
)
class Acl:
    def __init__(
        self,
        *,
        owner_gid: builtins.str,
        owner_uid: builtins.str,
        permissions: builtins.str,
    ) -> None:
        '''Permissions as POSIX ACL.

        :param owner_gid: Specifies the POSIX group ID to apply to the RootDirectory. Accepts values from 0 to 2^32 (4294967295).
        :param owner_uid: Specifies the POSIX user ID to apply to the RootDirectory. Accepts values from 0 to 2^32 (4294967295).
        :param permissions: Specifies the POSIX permissions to apply to the RootDirectory, in the format of an octal number representing the file's mode bits.

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_ec2 as ec2
            import aws_cdk.aws_efs as efs
            
            
            # create a new VPC
            vpc = ec2.Vpc(self, "VPC")
            
            # create a new Amazon EFS filesystem
            file_system = efs.FileSystem(self, "Efs", vpc=vpc)
            
            # create a new access point from the filesystem
            access_point = file_system.add_access_point("AccessPoint",
                # set /export/lambda as the root of the access point
                path="/export/lambda",
                # as /export/lambda does not exist in a new efs filesystem, the efs will create the directory with the following createAcl
                create_acl=efs.Acl(
                    owner_uid="1001",
                    owner_gid="1001",
                    permissions="750"
                ),
                # enforce the POSIX identity so lambda function will access with this identity
                posix_user=efs.PosixUser(
                    uid="1001",
                    gid="1001"
                )
            )
            
            fn = lambda_.Function(self, "MyLambda",
                # mount the access point to /mnt/msg in the lambda runtime environment
                filesystem=lambda_.FileSystem.from_efs_access_point(access_point, "/mnt/msg"),
                runtime=lambda_.Runtime.NODEJS_18_X,
                handler="index.handler",
                code=lambda_.Code.from_asset(path.join(__dirname, "lambda-handler")),
                vpc=vpc
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f439deeada51bd0f31384ee4b4e958560a0a30822d3f26655f3a4b6a2568825)
            check_type(argname="argument owner_gid", value=owner_gid, expected_type=type_hints["owner_gid"])
            check_type(argname="argument owner_uid", value=owner_uid, expected_type=type_hints["owner_uid"])
            check_type(argname="argument permissions", value=permissions, expected_type=type_hints["permissions"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "owner_gid": owner_gid,
            "owner_uid": owner_uid,
            "permissions": permissions,
        }

    @builtins.property
    def owner_gid(self) -> builtins.str:
        '''Specifies the POSIX group ID to apply to the RootDirectory.

        Accepts values from 0 to 2^32 (4294967295).
        '''
        result = self._values.get("owner_gid")
        assert result is not None, "Required property 'owner_gid' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def owner_uid(self) -> builtins.str:
        '''Specifies the POSIX user ID to apply to the RootDirectory.

        Accepts values from 0 to 2^32 (4294967295).
        '''
        result = self._values.get("owner_uid")
        assert result is not None, "Required property 'owner_uid' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def permissions(self) -> builtins.str:
        '''Specifies the POSIX permissions to apply to the RootDirectory, in the format of an octal number representing the file's mode bits.'''
        result = self._values.get("permissions")
        assert result is not None, "Required property 'permissions' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Acl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnAccessPoint(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_efs.CfnAccessPoint",
):
    '''The ``AWS::EFS::AccessPoint`` resource creates an EFS access point.

    An access point is an application-specific view into an EFS file system that applies an operating system user and group, and a file system path, to any file system request made through the access point. The operating system user and group override any identity information provided by the NFS client. The file system path is exposed as the access point's root directory. Applications using the access point can only access data in its own directory and below. To learn more, see `Mounting a file system using EFS access points <https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html>`_ .

    This operation requires permissions for the ``elasticfilesystem:CreateAccessPoint`` action.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-accesspoint.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_efs as efs
        
        cfn_access_point = efs.CfnAccessPoint(self, "MyCfnAccessPoint",
            file_system_id="fileSystemId",
        
            # the properties below are optional
            access_point_tags=[efs.CfnAccessPoint.AccessPointTagProperty(
                key="key",
                value="value"
            )],
            client_token="clientToken",
            posix_user=efs.CfnAccessPoint.PosixUserProperty(
                gid="gid",
                uid="uid",
        
                # the properties below are optional
                secondary_gids=["secondaryGids"]
            ),
            root_directory=efs.CfnAccessPoint.RootDirectoryProperty(
                creation_info=efs.CfnAccessPoint.CreationInfoProperty(
                    owner_gid="ownerGid",
                    owner_uid="ownerUid",
                    permissions="permissions"
                ),
                path="path"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        file_system_id: builtins.str,
        access_point_tags: typing.Optional[typing.Sequence[typing.Union["CfnAccessPoint.AccessPointTagProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        client_token: typing.Optional[builtins.str] = None,
        posix_user: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAccessPoint.PosixUserProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        root_directory: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAccessPoint.RootDirectoryProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param file_system_id: The ID of the EFS file system that the access point applies to. Accepts only the ID format for input when specifying a file system, for example ``fs-0123456789abcedf2`` .
        :param access_point_tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param client_token: The opaque string specified in the request to ensure idempotent creation.
        :param posix_user: The full POSIX identity, including the user ID, group ID, and secondary group IDs on the access point that is used for all file operations by NFS clients using the access point.
        :param root_directory: The directory on the Amazon EFS file system that the access point exposes as the root directory to NFS clients using the access point.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee6cf8e32e236f5b64c41d34d8956a146a19df0d9467273bec84f3053dc68070)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAccessPointProps(
            file_system_id=file_system_id,
            access_point_tags=access_point_tags,
            client_token=client_token,
            posix_user=posix_user,
            root_directory=root_directory,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca8bc4bd98606c2925e8e3beaf6899315a3a8aa05fe42a495c106412587debb7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__17e606a40f63a3efd1580567556b9224350cfb37bd36418259a5a97278069b76)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAccessPointId")
    def attr_access_point_id(self) -> builtins.str:
        '''The ID of the EFS access point.

        :cloudformationAttribute: AccessPointId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAccessPointId"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the access point.

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
    @jsii.member(jsii_name="fileSystemId")
    def file_system_id(self) -> builtins.str:
        '''The ID of the EFS file system that the access point applies to.'''
        return typing.cast(builtins.str, jsii.get(self, "fileSystemId"))

    @file_system_id.setter
    def file_system_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9aea834bdfbaebbad27efcd560e0cd5498ef3d5969d70369e72304aed575791)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileSystemId", value)

    @builtins.property
    @jsii.member(jsii_name="accessPointTagsRaw")
    def access_point_tags_raw(
        self,
    ) -> typing.Optional[typing.List["CfnAccessPoint.AccessPointTagProperty"]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List["CfnAccessPoint.AccessPointTagProperty"]], jsii.get(self, "accessPointTagsRaw"))

    @access_point_tags_raw.setter
    def access_point_tags_raw(
        self,
        value: typing.Optional[typing.List["CfnAccessPoint.AccessPointTagProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aeb74855ac1106765931a5c783dbbf7f4179c6aa7d804023e0d75ac4601576b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessPointTagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="clientToken")
    def client_token(self) -> typing.Optional[builtins.str]:
        '''The opaque string specified in the request to ensure idempotent creation.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientToken"))

    @client_token.setter
    def client_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__052a7200703646606a8831b74c4f5511cf71ee496fd407ed4059efc71782703e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientToken", value)

    @builtins.property
    @jsii.member(jsii_name="posixUser")
    def posix_user(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAccessPoint.PosixUserProperty"]]:
        '''The full POSIX identity, including the user ID, group ID, and secondary group IDs on the access point that is used for all file operations by NFS clients using the access point.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAccessPoint.PosixUserProperty"]], jsii.get(self, "posixUser"))

    @posix_user.setter
    def posix_user(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAccessPoint.PosixUserProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cc245c2e53318bdc7d3164c462d6e8a52bf82fb7fe49247d2231ef329a53d87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "posixUser", value)

    @builtins.property
    @jsii.member(jsii_name="rootDirectory")
    def root_directory(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAccessPoint.RootDirectoryProperty"]]:
        '''The directory on the Amazon EFS file system that the access point exposes as the root directory to NFS clients using the access point.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAccessPoint.RootDirectoryProperty"]], jsii.get(self, "rootDirectory"))

    @root_directory.setter
    def root_directory(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAccessPoint.RootDirectoryProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9667e2e350935a923b952abf9558fa66f4e1917b4233a4c26c0b65c8fd475e03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootDirectory", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_efs.CfnAccessPoint.AccessPointTagProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class AccessPointTagProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A tag is a key-value pair attached to a file system.

            Allowed characters in the ``Key`` and ``Value`` properties are letters, white space, and numbers that can be represented in UTF-8, and the following characters: ``+ - = . _ : /``

            :param key: The tag key (String). The key can't start with ``aws:`` .
            :param value: The value of the tag key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-accesspointtag.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_efs as efs
                
                access_point_tag_property = efs.CfnAccessPoint.AccessPointTagProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__18158f047ae4eb17326b1111683835556cf447939c66247854d140d2e078ab7b)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''The tag key (String).

            The key can't start with ``aws:`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-accesspointtag.html#cfn-efs-accesspoint-accesspointtag-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The value of the tag key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-accesspointtag.html#cfn-efs-accesspoint-accesspointtag-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccessPointTagProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_efs.CfnAccessPoint.CreationInfoProperty",
        jsii_struct_bases=[],
        name_mapping={
            "owner_gid": "ownerGid",
            "owner_uid": "ownerUid",
            "permissions": "permissions",
        },
    )
    class CreationInfoProperty:
        def __init__(
            self,
            *,
            owner_gid: builtins.str,
            owner_uid: builtins.str,
            permissions: builtins.str,
        ) -> None:
            '''Required if the ``RootDirectory`` > ``Path`` specified does not exist.

            Specifies the POSIX IDs and permissions to apply to the access point's ``RootDirectory`` > ``Path`` . If the access point root directory does not exist, EFS creates it with these settings when a client connects to the access point. When specifying ``CreationInfo`` , you must include values for all properties.

            Amazon EFS creates a root directory only if you have provided the CreationInfo: OwnUid, OwnGID, and permissions for the directory. If you do not provide this information, Amazon EFS does not create the root directory. If the root directory does not exist, attempts to mount using the access point will fail.
            .. epigraph::

               If you do not provide ``CreationInfo`` and the specified ``RootDirectory`` does not exist, attempts to mount the file system using the access point will fail.

            :param owner_gid: Specifies the POSIX group ID to apply to the ``RootDirectory`` . Accepts values from 0 to 2^32 (4294967295).
            :param owner_uid: Specifies the POSIX user ID to apply to the ``RootDirectory`` . Accepts values from 0 to 2^32 (4294967295).
            :param permissions: Specifies the POSIX permissions to apply to the ``RootDirectory`` , in the format of an octal number representing the file's mode bits.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-creationinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_efs as efs
                
                creation_info_property = efs.CfnAccessPoint.CreationInfoProperty(
                    owner_gid="ownerGid",
                    owner_uid="ownerUid",
                    permissions="permissions"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d74896f895974aeb78b39425593b263e2cca8c26b3d717b7ab981d784a7b9593)
                check_type(argname="argument owner_gid", value=owner_gid, expected_type=type_hints["owner_gid"])
                check_type(argname="argument owner_uid", value=owner_uid, expected_type=type_hints["owner_uid"])
                check_type(argname="argument permissions", value=permissions, expected_type=type_hints["permissions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "owner_gid": owner_gid,
                "owner_uid": owner_uid,
                "permissions": permissions,
            }

        @builtins.property
        def owner_gid(self) -> builtins.str:
            '''Specifies the POSIX group ID to apply to the ``RootDirectory`` .

            Accepts values from 0 to 2^32 (4294967295).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-creationinfo.html#cfn-efs-accesspoint-creationinfo-ownergid
            '''
            result = self._values.get("owner_gid")
            assert result is not None, "Required property 'owner_gid' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def owner_uid(self) -> builtins.str:
            '''Specifies the POSIX user ID to apply to the ``RootDirectory`` .

            Accepts values from 0 to 2^32 (4294967295).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-creationinfo.html#cfn-efs-accesspoint-creationinfo-owneruid
            '''
            result = self._values.get("owner_uid")
            assert result is not None, "Required property 'owner_uid' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def permissions(self) -> builtins.str:
            '''Specifies the POSIX permissions to apply to the ``RootDirectory`` , in the format of an octal number representing the file's mode bits.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-creationinfo.html#cfn-efs-accesspoint-creationinfo-permissions
            '''
            result = self._values.get("permissions")
            assert result is not None, "Required property 'permissions' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CreationInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_efs.CfnAccessPoint.PosixUserProperty",
        jsii_struct_bases=[],
        name_mapping={"gid": "gid", "uid": "uid", "secondary_gids": "secondaryGids"},
    )
    class PosixUserProperty:
        def __init__(
            self,
            *,
            gid: builtins.str,
            uid: builtins.str,
            secondary_gids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The full POSIX identity, including the user ID, group ID, and any secondary group IDs, on the access point that is used for all file system operations performed by NFS clients using the access point.

            :param gid: The POSIX group ID used for all file system operations using this access point.
            :param uid: The POSIX user ID used for all file system operations using this access point.
            :param secondary_gids: Secondary POSIX group IDs used for all file system operations using this access point.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-posixuser.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_efs as efs
                
                posix_user_property = efs.CfnAccessPoint.PosixUserProperty(
                    gid="gid",
                    uid="uid",
                
                    # the properties below are optional
                    secondary_gids=["secondaryGids"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__501010539c7a611efa4b96840cdd89ac2086e0864afcb2855144c64fa71ab81c)
                check_type(argname="argument gid", value=gid, expected_type=type_hints["gid"])
                check_type(argname="argument uid", value=uid, expected_type=type_hints["uid"])
                check_type(argname="argument secondary_gids", value=secondary_gids, expected_type=type_hints["secondary_gids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "gid": gid,
                "uid": uid,
            }
            if secondary_gids is not None:
                self._values["secondary_gids"] = secondary_gids

        @builtins.property
        def gid(self) -> builtins.str:
            '''The POSIX group ID used for all file system operations using this access point.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-posixuser.html#cfn-efs-accesspoint-posixuser-gid
            '''
            result = self._values.get("gid")
            assert result is not None, "Required property 'gid' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def uid(self) -> builtins.str:
            '''The POSIX user ID used for all file system operations using this access point.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-posixuser.html#cfn-efs-accesspoint-posixuser-uid
            '''
            result = self._values.get("uid")
            assert result is not None, "Required property 'uid' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def secondary_gids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Secondary POSIX group IDs used for all file system operations using this access point.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-posixuser.html#cfn-efs-accesspoint-posixuser-secondarygids
            '''
            result = self._values.get("secondary_gids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PosixUserProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_efs.CfnAccessPoint.RootDirectoryProperty",
        jsii_struct_bases=[],
        name_mapping={"creation_info": "creationInfo", "path": "path"},
    )
    class RootDirectoryProperty:
        def __init__(
            self,
            *,
            creation_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAccessPoint.CreationInfoProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the directory on the Amazon EFS file system that the access point provides access to.

            The access point exposes the specified file system path as the root directory of your file system to applications using the access point. NFS clients using the access point can only access data in the access point's ``RootDirectory`` and it's subdirectories.

            :param creation_info: (Optional) Specifies the POSIX IDs and permissions to apply to the access point's ``RootDirectory`` . If the ``RootDirectory`` > ``Path`` specified does not exist, EFS creates the root directory using the ``CreationInfo`` settings when a client connects to an access point. When specifying the ``CreationInfo`` , you must provide values for all properties. .. epigraph:: If you do not provide ``CreationInfo`` and the specified ``RootDirectory`` > ``Path`` does not exist, attempts to mount the file system using the access point will fail.
            :param path: Specifies the path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system. A path can have up to four subdirectories. If the specified path does not exist, you are required to provide the ``CreationInfo`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-rootdirectory.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_efs as efs
                
                root_directory_property = efs.CfnAccessPoint.RootDirectoryProperty(
                    creation_info=efs.CfnAccessPoint.CreationInfoProperty(
                        owner_gid="ownerGid",
                        owner_uid="ownerUid",
                        permissions="permissions"
                    ),
                    path="path"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__89b051df2a59c0884b5df1f891e75e8c5eecc226e4e3c37de3b47e49fc555dde)
                check_type(argname="argument creation_info", value=creation_info, expected_type=type_hints["creation_info"])
                check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if creation_info is not None:
                self._values["creation_info"] = creation_info
            if path is not None:
                self._values["path"] = path

        @builtins.property
        def creation_info(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAccessPoint.CreationInfoProperty"]]:
            '''(Optional) Specifies the POSIX IDs and permissions to apply to the access point's ``RootDirectory`` .

            If the ``RootDirectory`` > ``Path`` specified does not exist, EFS creates the root directory using the ``CreationInfo`` settings when a client connects to an access point. When specifying the ``CreationInfo`` , you must provide values for all properties.
            .. epigraph::

               If you do not provide ``CreationInfo`` and the specified ``RootDirectory`` > ``Path`` does not exist, attempts to mount the file system using the access point will fail.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-rootdirectory.html#cfn-efs-accesspoint-rootdirectory-creationinfo
            '''
            result = self._values.get("creation_info")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAccessPoint.CreationInfoProperty"]], result)

        @builtins.property
        def path(self) -> typing.Optional[builtins.str]:
            '''Specifies the path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system.

            A path can have up to four subdirectories. If the specified path does not exist, you are required to provide the ``CreationInfo`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-rootdirectory.html#cfn-efs-accesspoint-rootdirectory-path
            '''
            result = self._values.get("path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RootDirectoryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_efs.CfnAccessPointProps",
    jsii_struct_bases=[],
    name_mapping={
        "file_system_id": "fileSystemId",
        "access_point_tags": "accessPointTags",
        "client_token": "clientToken",
        "posix_user": "posixUser",
        "root_directory": "rootDirectory",
    },
)
class CfnAccessPointProps:
    def __init__(
        self,
        *,
        file_system_id: builtins.str,
        access_point_tags: typing.Optional[typing.Sequence[typing.Union[CfnAccessPoint.AccessPointTagProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        client_token: typing.Optional[builtins.str] = None,
        posix_user: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAccessPoint.PosixUserProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        root_directory: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAccessPoint.RootDirectoryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAccessPoint``.

        :param file_system_id: The ID of the EFS file system that the access point applies to. Accepts only the ID format for input when specifying a file system, for example ``fs-0123456789abcedf2`` .
        :param access_point_tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param client_token: The opaque string specified in the request to ensure idempotent creation.
        :param posix_user: The full POSIX identity, including the user ID, group ID, and secondary group IDs on the access point that is used for all file operations by NFS clients using the access point.
        :param root_directory: The directory on the Amazon EFS file system that the access point exposes as the root directory to NFS clients using the access point.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-accesspoint.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_efs as efs
            
            cfn_access_point_props = efs.CfnAccessPointProps(
                file_system_id="fileSystemId",
            
                # the properties below are optional
                access_point_tags=[efs.CfnAccessPoint.AccessPointTagProperty(
                    key="key",
                    value="value"
                )],
                client_token="clientToken",
                posix_user=efs.CfnAccessPoint.PosixUserProperty(
                    gid="gid",
                    uid="uid",
            
                    # the properties below are optional
                    secondary_gids=["secondaryGids"]
                ),
                root_directory=efs.CfnAccessPoint.RootDirectoryProperty(
                    creation_info=efs.CfnAccessPoint.CreationInfoProperty(
                        owner_gid="ownerGid",
                        owner_uid="ownerUid",
                        permissions="permissions"
                    ),
                    path="path"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d9e6a6ec2a31d2d52416a71ce47e5ce1ad556ab26693686a787d2d7d21231d6)
            check_type(argname="argument file_system_id", value=file_system_id, expected_type=type_hints["file_system_id"])
            check_type(argname="argument access_point_tags", value=access_point_tags, expected_type=type_hints["access_point_tags"])
            check_type(argname="argument client_token", value=client_token, expected_type=type_hints["client_token"])
            check_type(argname="argument posix_user", value=posix_user, expected_type=type_hints["posix_user"])
            check_type(argname="argument root_directory", value=root_directory, expected_type=type_hints["root_directory"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "file_system_id": file_system_id,
        }
        if access_point_tags is not None:
            self._values["access_point_tags"] = access_point_tags
        if client_token is not None:
            self._values["client_token"] = client_token
        if posix_user is not None:
            self._values["posix_user"] = posix_user
        if root_directory is not None:
            self._values["root_directory"] = root_directory

    @builtins.property
    def file_system_id(self) -> builtins.str:
        '''The ID of the EFS file system that the access point applies to.

        Accepts only the ID format for input when specifying a file system, for example ``fs-0123456789abcedf2`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-accesspoint.html#cfn-efs-accesspoint-filesystemid
        '''
        result = self._values.get("file_system_id")
        assert result is not None, "Required property 'file_system_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_point_tags(
        self,
    ) -> typing.Optional[typing.List[CfnAccessPoint.AccessPointTagProperty]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-accesspoint.html#cfn-efs-accesspoint-accesspointtags
        '''
        result = self._values.get("access_point_tags")
        return typing.cast(typing.Optional[typing.List[CfnAccessPoint.AccessPointTagProperty]], result)

    @builtins.property
    def client_token(self) -> typing.Optional[builtins.str]:
        '''The opaque string specified in the request to ensure idempotent creation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-accesspoint.html#cfn-efs-accesspoint-clienttoken
        '''
        result = self._values.get("client_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def posix_user(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAccessPoint.PosixUserProperty]]:
        '''The full POSIX identity, including the user ID, group ID, and secondary group IDs on the access point that is used for all file operations by NFS clients using the access point.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-accesspoint.html#cfn-efs-accesspoint-posixuser
        '''
        result = self._values.get("posix_user")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAccessPoint.PosixUserProperty]], result)

    @builtins.property
    def root_directory(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAccessPoint.RootDirectoryProperty]]:
        '''The directory on the Amazon EFS file system that the access point exposes as the root directory to NFS clients using the access point.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-accesspoint.html#cfn-efs-accesspoint-rootdirectory
        '''
        result = self._values.get("root_directory")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAccessPoint.RootDirectoryProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAccessPointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnFileSystem(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_efs.CfnFileSystem",
):
    '''The ``AWS::EFS::FileSystem`` resource creates a new, empty file system in Amazon Elastic File System ( Amazon EFS ).

    You must create a mount target ( `AWS::EFS::MountTarget <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-mounttarget.html>`_ ) to mount your EFS file system on an Amazon EC2 or other AWS cloud compute resource.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_efs as efs
        
        # file_system_policy: Any
        
        cfn_file_system = efs.CfnFileSystem(self, "MyCfnFileSystem",
            availability_zone_name="availabilityZoneName",
            backup_policy=efs.CfnFileSystem.BackupPolicyProperty(
                status="status"
            ),
            bypass_policy_lockout_safety_check=False,
            encrypted=False,
            file_system_policy=file_system_policy,
            file_system_tags=[efs.CfnFileSystem.ElasticFileSystemTagProperty(
                key="key",
                value="value"
            )],
            kms_key_id="kmsKeyId",
            lifecycle_policies=[efs.CfnFileSystem.LifecyclePolicyProperty(
                transition_to_ia="transitionToIa",
                transition_to_primary_storage_class="transitionToPrimaryStorageClass"
            )],
            performance_mode="performanceMode",
            provisioned_throughput_in_mibps=123,
            throughput_mode="throughputMode"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        availability_zone_name: typing.Optional[builtins.str] = None,
        backup_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFileSystem.BackupPolicyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        bypass_policy_lockout_safety_check: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        encrypted: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        file_system_policy: typing.Any = None,
        file_system_tags: typing.Optional[typing.Sequence[typing.Union["CfnFileSystem.ElasticFileSystemTagProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        lifecycle_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFileSystem.LifecyclePolicyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        performance_mode: typing.Optional[builtins.str] = None,
        provisioned_throughput_in_mibps: typing.Optional[jsii.Number] = None,
        throughput_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param availability_zone_name: Used to create a file system that uses One Zone storage classes. It specifies the AWS Availability Zone in which to create the file system. Use the format ``us-east-1a`` to specify the Availability Zone. For more information about One Zone storage classes, see `Using EFS storage classes <https://docs.aws.amazon.com/efs/latest/ug/storage-classes.html>`_ in the *Amazon EFS User Guide* . .. epigraph:: One Zone storage classes are not available in all Availability Zones in AWS Regions where Amazon EFS is available.
        :param backup_policy: Use the ``BackupPolicy`` to turn automatic backups on or off for the file system.
        :param bypass_policy_lockout_safety_check: (Optional) A boolean that specifies whether or not to bypass the ``FileSystemPolicy`` lockout safety check. The lockout safety check determines whether the policy in the request will lock out, or prevent, the IAM principal that is making the request from making future ``PutFileSystemPolicy`` requests on this file system. Set ``BypassPolicyLockoutSafetyCheck`` to ``True`` only when you intend to prevent the IAM principal that is making the request from making subsequent ``PutFileSystemPolicy`` requests on this file system. The default value is ``False`` .
        :param encrypted: A Boolean value that, if true, creates an encrypted file system. When creating an encrypted file system, you have the option of specifying a KmsKeyId for an existing AWS KMS key . If you don't specify a KMS key , then the default KMS key for Amazon EFS , ``/aws/elasticfilesystem`` , is used to protect the encrypted file system.
        :param file_system_policy: The ``FileSystemPolicy`` for the EFS file system. A file system policy is an IAM resource policy used to control NFS access to an EFS file system. For more information, see `Using IAM to control NFS access to Amazon EFS <https://docs.aws.amazon.com/efs/latest/ug/iam-access-control-nfs-efs.html>`_ in the *Amazon EFS User Guide* .
        :param file_system_tags: Use to create one or more tags associated with the file system. Each tag is a user-defined key-value pair. Name your file system on creation by including a ``"Key":"Name","Value":"{value}"`` key-value pair. Each key must be unique. For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference Guide* .
        :param kms_key_id: The ID of the AWS KMS key to be used to protect the encrypted file system. This parameter is only required if you want to use a nondefault KMS key . If this parameter is not specified, the default KMS key for Amazon EFS is used. This ID can be in one of the following formats: - Key ID - A unique identifier of the key, for example ``1234abcd-12ab-34cd-56ef-1234567890ab`` . - ARN - An Amazon Resource Name (ARN) for the key, for example ``arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`` . - Key alias - A previously created display name for a key, for example ``alias/projectKey1`` . - Key alias ARN - An ARN for a key alias, for example ``arn:aws:kms:us-west-2:444455556666:alias/projectKey1`` . If ``KmsKeyId`` is specified, the ``Encrypted`` parameter must be set to true.
        :param lifecycle_policies: An array of ``LifecyclePolicy`` objects that define the file system's ``LifecycleConfiguration`` object. A ``LifecycleConfiguration`` object informs EFS lifecycle management and intelligent tiering of the following: - When to move files in the file system from primary storage to the IA storage class. - When to move files that are in IA storage to primary storage. .. epigraph:: Amazon EFS requires that each ``LifecyclePolicy`` object have only a single transition. This means that in a request body, ``LifecyclePolicies`` needs to be structured as an array of ``LifecyclePolicy`` objects, one object for each transition, ``TransitionToIA`` , ``TransitionToPrimaryStorageClass`` . See the example requests in the following section for more information.
        :param performance_mode: The performance mode of the file system. We recommend ``generalPurpose`` performance mode for most file systems. File systems using the ``maxIO`` performance mode can scale to higher levels of aggregate throughput and operations per second with a tradeoff of slightly higher latencies for most file operations. The performance mode can't be changed after the file system has been created. .. epigraph:: The ``maxIO`` mode is not supported on file systems using One Zone storage classes. Default is ``generalPurpose`` .
        :param provisioned_throughput_in_mibps: The throughput, measured in mebibytes per second (MiBps), that you want to provision for a file system that you're creating. Required if ``ThroughputMode`` is set to ``provisioned`` . Valid values are 1-3414 MiBps, with the upper limit depending on Region. To increase this limit, contact AWS Support . For more information, see `Amazon EFS quotas that you can increase <https://docs.aws.amazon.com/efs/latest/ug/limits.html#soft-limits>`_ in the *Amazon EFS User Guide* .
        :param throughput_mode: Specifies the throughput mode for the file system. The mode can be ``bursting`` , ``provisioned`` , or ``elastic`` . If you set ``ThroughputMode`` to ``provisioned`` , you must also set a value for ``ProvisionedThroughputInMibps`` . After you create the file system, you can decrease your file system's throughput in Provisioned Throughput mode or change between the throughput modes, with certain time restrictions. For more information, see `Specifying throughput with provisioned mode <https://docs.aws.amazon.com/efs/latest/ug/performance.html#provisioned-throughput>`_ in the *Amazon EFS User Guide* . Default is ``elastic`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc457ee31ba660f40c549433977317b66ec9b461edc7a3afd3a157dcf7b8d48f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFileSystemProps(
            availability_zone_name=availability_zone_name,
            backup_policy=backup_policy,
            bypass_policy_lockout_safety_check=bypass_policy_lockout_safety_check,
            encrypted=encrypted,
            file_system_policy=file_system_policy,
            file_system_tags=file_system_tags,
            kms_key_id=kms_key_id,
            lifecycle_policies=lifecycle_policies,
            performance_mode=performance_mode,
            provisioned_throughput_in_mibps=provisioned_throughput_in_mibps,
            throughput_mode=throughput_mode,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4de45f38231d265020ffa3517bb2f41c6c7f64bc0414e943cf094f6436b824df)
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
            type_hints = typing.get_type_hints(_typecheckingstub__64147597fb4c53ed2d67a6b0ef31707f2352f072a9c53f4fe39bc738512a4681)
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
        '''The Amazon Resource Name (ARN) of the EFS file system.

        Example: ``arn:aws:elasticfilesystem:us-west-2:1111333322228888:file-system/fs-0123456789abcdef8``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrFileSystemId")
    def attr_file_system_id(self) -> builtins.str:
        '''The ID of the EFS file system.

        For example: ``fs-abcdef0123456789a``

        :cloudformationAttribute: FileSystemId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFileSystemId"))

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
    @jsii.member(jsii_name="availabilityZoneName")
    def availability_zone_name(self) -> typing.Optional[builtins.str]:
        '''Used to create a file system that uses One Zone storage classes.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZoneName"))

    @availability_zone_name.setter
    def availability_zone_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bcd28f23c44d69b6a8f6fd61de5866f3fdb618cec9e47e4a49ed73986bdd849)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZoneName", value)

    @builtins.property
    @jsii.member(jsii_name="backupPolicy")
    def backup_policy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFileSystem.BackupPolicyProperty"]]:
        '''Use the ``BackupPolicy`` to turn automatic backups on or off for the file system.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFileSystem.BackupPolicyProperty"]], jsii.get(self, "backupPolicy"))

    @backup_policy.setter
    def backup_policy(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFileSystem.BackupPolicyProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53fc5b9ed624a6fc84a03901041ea70dcde091bbcc6330be8fa5cf3fdf8c38b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="bypassPolicyLockoutSafetyCheck")
    def bypass_policy_lockout_safety_check(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''(Optional) A boolean that specifies whether or not to bypass the ``FileSystemPolicy`` lockout safety check.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "bypassPolicyLockoutSafetyCheck"))

    @bypass_policy_lockout_safety_check.setter
    def bypass_policy_lockout_safety_check(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbd68d0f7f29b58d297e40085872ecac516d0817c15d9490f68a92f7aa0b8ea5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bypassPolicyLockoutSafetyCheck", value)

    @builtins.property
    @jsii.member(jsii_name="encrypted")
    def encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A Boolean value that, if true, creates an encrypted file system.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "encrypted"))

    @encrypted.setter
    def encrypted(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9501af5a47c0d34d9710df284e85c94248a9579987a05605e729328fa911ff46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encrypted", value)

    @builtins.property
    @jsii.member(jsii_name="fileSystemPolicy")
    def file_system_policy(self) -> typing.Any:
        '''The ``FileSystemPolicy`` for the EFS file system.'''
        return typing.cast(typing.Any, jsii.get(self, "fileSystemPolicy"))

    @file_system_policy.setter
    def file_system_policy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__666e3c63493f31759a99ed7071553b2e9c97fd2b8a0c9b681208a654ad356c9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileSystemPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="fileSystemTagsRaw")
    def file_system_tags_raw(
        self,
    ) -> typing.Optional[typing.List["CfnFileSystem.ElasticFileSystemTagProperty"]]:
        '''Use to create one or more tags associated with the file system.'''
        return typing.cast(typing.Optional[typing.List["CfnFileSystem.ElasticFileSystemTagProperty"]], jsii.get(self, "fileSystemTagsRaw"))

    @file_system_tags_raw.setter
    def file_system_tags_raw(
        self,
        value: typing.Optional[typing.List["CfnFileSystem.ElasticFileSystemTagProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d84f46b1475d1cae884e8108f8439bdc99a546d9a8b21f2a8f1f4417cadc3585)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileSystemTagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the AWS KMS key to be used to protect the encrypted file system.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a55210d3081fdfc59eb5c327bf8219f72804cd3b9d3e4b881f3edb7c67b5f3eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="lifecyclePolicies")
    def lifecycle_policies(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFileSystem.LifecyclePolicyProperty"]]]]:
        '''An array of ``LifecyclePolicy`` objects that define the file system's ``LifecycleConfiguration`` object.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFileSystem.LifecyclePolicyProperty"]]]], jsii.get(self, "lifecyclePolicies"))

    @lifecycle_policies.setter
    def lifecycle_policies(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFileSystem.LifecyclePolicyProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd864e190d9a9b64a7046d9259a257368e4b66a44f4da384a9b88751c2a5271d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecyclePolicies", value)

    @builtins.property
    @jsii.member(jsii_name="performanceMode")
    def performance_mode(self) -> typing.Optional[builtins.str]:
        '''The performance mode of the file system.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "performanceMode"))

    @performance_mode.setter
    def performance_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__840c02c07752d49064a9e001bb6d5e27747e9a3c922771a75a094ace12f9fcc4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "performanceMode", value)

    @builtins.property
    @jsii.member(jsii_name="provisionedThroughputInMibps")
    def provisioned_throughput_in_mibps(self) -> typing.Optional[jsii.Number]:
        '''The throughput, measured in mebibytes per second (MiBps), that you want to provision for a file system that you're creating.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "provisionedThroughputInMibps"))

    @provisioned_throughput_in_mibps.setter
    def provisioned_throughput_in_mibps(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc4b244b6d015f638041856e6a5998aa7289240b34d904419c12431ce5f68b4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisionedThroughputInMibps", value)

    @builtins.property
    @jsii.member(jsii_name="throughputMode")
    def throughput_mode(self) -> typing.Optional[builtins.str]:
        '''Specifies the throughput mode for the file system.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "throughputMode"))

    @throughput_mode.setter
    def throughput_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c5e0603f09328aca127a79f4af8caf4140cb862bf23ebe0cbe2e1e4c05dc8b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "throughputMode", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_efs.CfnFileSystem.BackupPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"status": "status"},
    )
    class BackupPolicyProperty:
        def __init__(self, *, status: builtins.str) -> None:
            '''The backup policy turns automatic backups for the file system on or off.

            :param status: Set the backup policy status for the file system. - *``ENABLED``* - Turns automatic backups on for the file system. - *``DISABLED``* - Turns automatic backups off for the file system.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-backuppolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_efs as efs
                
                backup_policy_property = efs.CfnFileSystem.BackupPolicyProperty(
                    status="status"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9c002a7547dd1af97cb52ea97bde78ee445e9676e5214ccc0edc9f10622d992a)
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "status": status,
            }

        @builtins.property
        def status(self) -> builtins.str:
            '''Set the backup policy status for the file system.

            - *``ENABLED``* - Turns automatic backups on for the file system.
            - *``DISABLED``* - Turns automatic backups off for the file system.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-backuppolicy.html#cfn-efs-filesystem-backuppolicy-status
            '''
            result = self._values.get("status")
            assert result is not None, "Required property 'status' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BackupPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_efs.CfnFileSystem.ElasticFileSystemTagProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class ElasticFileSystemTagProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''A tag is a key-value pair attached to a file system.

            Allowed characters in the ``Key`` and ``Value`` properties are letters, white space, and numbers that can be represented in UTF-8, and the following characters: ``+ - = . _ : /``

            :param key: The tag key (String). The key can't start with ``aws:`` .
            :param value: The value of the tag key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-elasticfilesystemtag.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_efs as efs
                
                elastic_file_system_tag_property = efs.CfnFileSystem.ElasticFileSystemTagProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__786d6bbf33204cdfd92e62176c97bd5739bc95bda3441156be931c7335e637b7)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The tag key (String).

            The key can't start with ``aws:`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-elasticfilesystemtag.html#cfn-efs-filesystem-elasticfilesystemtag-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value of the tag key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-elasticfilesystemtag.html#cfn-efs-filesystem-elasticfilesystemtag-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ElasticFileSystemTagProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_efs.CfnFileSystem.LifecyclePolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "transition_to_ia": "transitionToIa",
            "transition_to_primary_storage_class": "transitionToPrimaryStorageClass",
        },
    )
    class LifecyclePolicyProperty:
        def __init__(
            self,
            *,
            transition_to_ia: typing.Optional[builtins.str] = None,
            transition_to_primary_storage_class: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes a policy used by EFS lifecycle management and EFS Intelligent-Tiering that specifies when to transition files into and out of the file system's Infrequent Access (IA) storage class.

            For more information, see `EFS Intelligent‐Tiering and EFS Lifecycle Management <https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html>`_ .
            .. epigraph::

               - Each ``LifecyclePolicy`` object can have only a single transition. This means that in a request body, ``LifecyclePolicies`` must be structured as an array of ``LifecyclePolicy`` objects, one object for each transition, ``TransitionToIA`` , ``TransitionToPrimaryStorageClass`` .
               - See the AWS::EFS::FileSystem examples for the correct ``LifecyclePolicy`` structure. Do not use the syntax shown on this page.

            :param transition_to_ia: Describes the period of time that a file is not accessed, after which it transitions to IA storage. Metadata operations such as listing the contents of a directory don't count as file access events.
            :param transition_to_primary_storage_class: Describes when to transition a file from IA storage to primary storage. Metadata operations such as listing the contents of a directory don't count as file access events.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-lifecyclepolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_efs as efs
                
                lifecycle_policy_property = efs.CfnFileSystem.LifecyclePolicyProperty(
                    transition_to_ia="transitionToIa",
                    transition_to_primary_storage_class="transitionToPrimaryStorageClass"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a5fbc3e227009fdec1c9845be8c439793816fbd90d94dd67c54610c9832a0e99)
                check_type(argname="argument transition_to_ia", value=transition_to_ia, expected_type=type_hints["transition_to_ia"])
                check_type(argname="argument transition_to_primary_storage_class", value=transition_to_primary_storage_class, expected_type=type_hints["transition_to_primary_storage_class"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if transition_to_ia is not None:
                self._values["transition_to_ia"] = transition_to_ia
            if transition_to_primary_storage_class is not None:
                self._values["transition_to_primary_storage_class"] = transition_to_primary_storage_class

        @builtins.property
        def transition_to_ia(self) -> typing.Optional[builtins.str]:
            '''Describes the period of time that a file is not accessed, after which it transitions to IA storage.

            Metadata operations such as listing the contents of a directory don't count as file access events.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-lifecyclepolicy.html#cfn-efs-filesystem-lifecyclepolicy-transitiontoia
            '''
            result = self._values.get("transition_to_ia")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def transition_to_primary_storage_class(self) -> typing.Optional[builtins.str]:
            '''Describes when to transition a file from IA storage to primary storage.

            Metadata operations such as listing the contents of a directory don't count as file access events.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-lifecyclepolicy.html#cfn-efs-filesystem-lifecyclepolicy-transitiontoprimarystorageclass
            '''
            result = self._values.get("transition_to_primary_storage_class")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LifecyclePolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_efs.CfnFileSystemProps",
    jsii_struct_bases=[],
    name_mapping={
        "availability_zone_name": "availabilityZoneName",
        "backup_policy": "backupPolicy",
        "bypass_policy_lockout_safety_check": "bypassPolicyLockoutSafetyCheck",
        "encrypted": "encrypted",
        "file_system_policy": "fileSystemPolicy",
        "file_system_tags": "fileSystemTags",
        "kms_key_id": "kmsKeyId",
        "lifecycle_policies": "lifecyclePolicies",
        "performance_mode": "performanceMode",
        "provisioned_throughput_in_mibps": "provisionedThroughputInMibps",
        "throughput_mode": "throughputMode",
    },
)
class CfnFileSystemProps:
    def __init__(
        self,
        *,
        availability_zone_name: typing.Optional[builtins.str] = None,
        backup_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFileSystem.BackupPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        bypass_policy_lockout_safety_check: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        encrypted: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        file_system_policy: typing.Any = None,
        file_system_tags: typing.Optional[typing.Sequence[typing.Union[CfnFileSystem.ElasticFileSystemTagProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        lifecycle_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFileSystem.LifecyclePolicyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        performance_mode: typing.Optional[builtins.str] = None,
        provisioned_throughput_in_mibps: typing.Optional[jsii.Number] = None,
        throughput_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnFileSystem``.

        :param availability_zone_name: Used to create a file system that uses One Zone storage classes. It specifies the AWS Availability Zone in which to create the file system. Use the format ``us-east-1a`` to specify the Availability Zone. For more information about One Zone storage classes, see `Using EFS storage classes <https://docs.aws.amazon.com/efs/latest/ug/storage-classes.html>`_ in the *Amazon EFS User Guide* . .. epigraph:: One Zone storage classes are not available in all Availability Zones in AWS Regions where Amazon EFS is available.
        :param backup_policy: Use the ``BackupPolicy`` to turn automatic backups on or off for the file system.
        :param bypass_policy_lockout_safety_check: (Optional) A boolean that specifies whether or not to bypass the ``FileSystemPolicy`` lockout safety check. The lockout safety check determines whether the policy in the request will lock out, or prevent, the IAM principal that is making the request from making future ``PutFileSystemPolicy`` requests on this file system. Set ``BypassPolicyLockoutSafetyCheck`` to ``True`` only when you intend to prevent the IAM principal that is making the request from making subsequent ``PutFileSystemPolicy`` requests on this file system. The default value is ``False`` .
        :param encrypted: A Boolean value that, if true, creates an encrypted file system. When creating an encrypted file system, you have the option of specifying a KmsKeyId for an existing AWS KMS key . If you don't specify a KMS key , then the default KMS key for Amazon EFS , ``/aws/elasticfilesystem`` , is used to protect the encrypted file system.
        :param file_system_policy: The ``FileSystemPolicy`` for the EFS file system. A file system policy is an IAM resource policy used to control NFS access to an EFS file system. For more information, see `Using IAM to control NFS access to Amazon EFS <https://docs.aws.amazon.com/efs/latest/ug/iam-access-control-nfs-efs.html>`_ in the *Amazon EFS User Guide* .
        :param file_system_tags: Use to create one or more tags associated with the file system. Each tag is a user-defined key-value pair. Name your file system on creation by including a ``"Key":"Name","Value":"{value}"`` key-value pair. Each key must be unique. For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference Guide* .
        :param kms_key_id: The ID of the AWS KMS key to be used to protect the encrypted file system. This parameter is only required if you want to use a nondefault KMS key . If this parameter is not specified, the default KMS key for Amazon EFS is used. This ID can be in one of the following formats: - Key ID - A unique identifier of the key, for example ``1234abcd-12ab-34cd-56ef-1234567890ab`` . - ARN - An Amazon Resource Name (ARN) for the key, for example ``arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`` . - Key alias - A previously created display name for a key, for example ``alias/projectKey1`` . - Key alias ARN - An ARN for a key alias, for example ``arn:aws:kms:us-west-2:444455556666:alias/projectKey1`` . If ``KmsKeyId`` is specified, the ``Encrypted`` parameter must be set to true.
        :param lifecycle_policies: An array of ``LifecyclePolicy`` objects that define the file system's ``LifecycleConfiguration`` object. A ``LifecycleConfiguration`` object informs EFS lifecycle management and intelligent tiering of the following: - When to move files in the file system from primary storage to the IA storage class. - When to move files that are in IA storage to primary storage. .. epigraph:: Amazon EFS requires that each ``LifecyclePolicy`` object have only a single transition. This means that in a request body, ``LifecyclePolicies`` needs to be structured as an array of ``LifecyclePolicy`` objects, one object for each transition, ``TransitionToIA`` , ``TransitionToPrimaryStorageClass`` . See the example requests in the following section for more information.
        :param performance_mode: The performance mode of the file system. We recommend ``generalPurpose`` performance mode for most file systems. File systems using the ``maxIO`` performance mode can scale to higher levels of aggregate throughput and operations per second with a tradeoff of slightly higher latencies for most file operations. The performance mode can't be changed after the file system has been created. .. epigraph:: The ``maxIO`` mode is not supported on file systems using One Zone storage classes. Default is ``generalPurpose`` .
        :param provisioned_throughput_in_mibps: The throughput, measured in mebibytes per second (MiBps), that you want to provision for a file system that you're creating. Required if ``ThroughputMode`` is set to ``provisioned`` . Valid values are 1-3414 MiBps, with the upper limit depending on Region. To increase this limit, contact AWS Support . For more information, see `Amazon EFS quotas that you can increase <https://docs.aws.amazon.com/efs/latest/ug/limits.html#soft-limits>`_ in the *Amazon EFS User Guide* .
        :param throughput_mode: Specifies the throughput mode for the file system. The mode can be ``bursting`` , ``provisioned`` , or ``elastic`` . If you set ``ThroughputMode`` to ``provisioned`` , you must also set a value for ``ProvisionedThroughputInMibps`` . After you create the file system, you can decrease your file system's throughput in Provisioned Throughput mode or change between the throughput modes, with certain time restrictions. For more information, see `Specifying throughput with provisioned mode <https://docs.aws.amazon.com/efs/latest/ug/performance.html#provisioned-throughput>`_ in the *Amazon EFS User Guide* . Default is ``elastic`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_efs as efs
            
            # file_system_policy: Any
            
            cfn_file_system_props = efs.CfnFileSystemProps(
                availability_zone_name="availabilityZoneName",
                backup_policy=efs.CfnFileSystem.BackupPolicyProperty(
                    status="status"
                ),
                bypass_policy_lockout_safety_check=False,
                encrypted=False,
                file_system_policy=file_system_policy,
                file_system_tags=[efs.CfnFileSystem.ElasticFileSystemTagProperty(
                    key="key",
                    value="value"
                )],
                kms_key_id="kmsKeyId",
                lifecycle_policies=[efs.CfnFileSystem.LifecyclePolicyProperty(
                    transition_to_ia="transitionToIa",
                    transition_to_primary_storage_class="transitionToPrimaryStorageClass"
                )],
                performance_mode="performanceMode",
                provisioned_throughput_in_mibps=123,
                throughput_mode="throughputMode"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__925156e2041b66f4aaa35cff9ceb098b90fd9cbb2027eb0431f56b2aa0c4aa89)
            check_type(argname="argument availability_zone_name", value=availability_zone_name, expected_type=type_hints["availability_zone_name"])
            check_type(argname="argument backup_policy", value=backup_policy, expected_type=type_hints["backup_policy"])
            check_type(argname="argument bypass_policy_lockout_safety_check", value=bypass_policy_lockout_safety_check, expected_type=type_hints["bypass_policy_lockout_safety_check"])
            check_type(argname="argument encrypted", value=encrypted, expected_type=type_hints["encrypted"])
            check_type(argname="argument file_system_policy", value=file_system_policy, expected_type=type_hints["file_system_policy"])
            check_type(argname="argument file_system_tags", value=file_system_tags, expected_type=type_hints["file_system_tags"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument lifecycle_policies", value=lifecycle_policies, expected_type=type_hints["lifecycle_policies"])
            check_type(argname="argument performance_mode", value=performance_mode, expected_type=type_hints["performance_mode"])
            check_type(argname="argument provisioned_throughput_in_mibps", value=provisioned_throughput_in_mibps, expected_type=type_hints["provisioned_throughput_in_mibps"])
            check_type(argname="argument throughput_mode", value=throughput_mode, expected_type=type_hints["throughput_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if availability_zone_name is not None:
            self._values["availability_zone_name"] = availability_zone_name
        if backup_policy is not None:
            self._values["backup_policy"] = backup_policy
        if bypass_policy_lockout_safety_check is not None:
            self._values["bypass_policy_lockout_safety_check"] = bypass_policy_lockout_safety_check
        if encrypted is not None:
            self._values["encrypted"] = encrypted
        if file_system_policy is not None:
            self._values["file_system_policy"] = file_system_policy
        if file_system_tags is not None:
            self._values["file_system_tags"] = file_system_tags
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if lifecycle_policies is not None:
            self._values["lifecycle_policies"] = lifecycle_policies
        if performance_mode is not None:
            self._values["performance_mode"] = performance_mode
        if provisioned_throughput_in_mibps is not None:
            self._values["provisioned_throughput_in_mibps"] = provisioned_throughput_in_mibps
        if throughput_mode is not None:
            self._values["throughput_mode"] = throughput_mode

    @builtins.property
    def availability_zone_name(self) -> typing.Optional[builtins.str]:
        '''Used to create a file system that uses One Zone storage classes.

        It specifies the AWS Availability Zone in which to create the file system. Use the format ``us-east-1a`` to specify the Availability Zone. For more information about One Zone storage classes, see `Using EFS storage classes <https://docs.aws.amazon.com/efs/latest/ug/storage-classes.html>`_ in the *Amazon EFS User Guide* .
        .. epigraph::

           One Zone storage classes are not available in all Availability Zones in AWS Regions where Amazon EFS is available.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-availabilityzonename
        '''
        result = self._values.get("availability_zone_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backup_policy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFileSystem.BackupPolicyProperty]]:
        '''Use the ``BackupPolicy`` to turn automatic backups on or off for the file system.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-backuppolicy
        '''
        result = self._values.get("backup_policy")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFileSystem.BackupPolicyProperty]], result)

    @builtins.property
    def bypass_policy_lockout_safety_check(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''(Optional) A boolean that specifies whether or not to bypass the ``FileSystemPolicy`` lockout safety check.

        The lockout safety check determines whether the policy in the request will lock out, or prevent, the IAM principal that is making the request from making future ``PutFileSystemPolicy`` requests on this file system. Set ``BypassPolicyLockoutSafetyCheck`` to ``True`` only when you intend to prevent the IAM principal that is making the request from making subsequent ``PutFileSystemPolicy`` requests on this file system. The default value is ``False`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-bypasspolicylockoutsafetycheck
        '''
        result = self._values.get("bypass_policy_lockout_safety_check")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A Boolean value that, if true, creates an encrypted file system.

        When creating an encrypted file system, you have the option of specifying a KmsKeyId for an existing AWS KMS key . If you don't specify a KMS key , then the default KMS key for Amazon EFS , ``/aws/elasticfilesystem`` , is used to protect the encrypted file system.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-encrypted
        '''
        result = self._values.get("encrypted")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def file_system_policy(self) -> typing.Any:
        '''The ``FileSystemPolicy`` for the EFS file system.

        A file system policy is an IAM resource policy used to control NFS access to an EFS file system. For more information, see `Using IAM to control NFS access to Amazon EFS <https://docs.aws.amazon.com/efs/latest/ug/iam-access-control-nfs-efs.html>`_ in the *Amazon EFS User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-filesystempolicy
        '''
        result = self._values.get("file_system_policy")
        return typing.cast(typing.Any, result)

    @builtins.property
    def file_system_tags(
        self,
    ) -> typing.Optional[typing.List[CfnFileSystem.ElasticFileSystemTagProperty]]:
        '''Use to create one or more tags associated with the file system.

        Each tag is a user-defined key-value pair. Name your file system on creation by including a ``"Key":"Name","Value":"{value}"`` key-value pair. Each key must be unique. For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-filesystemtags
        '''
        result = self._values.get("file_system_tags")
        return typing.cast(typing.Optional[typing.List[CfnFileSystem.ElasticFileSystemTagProperty]], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the AWS KMS key to be used to protect the encrypted file system.

        This parameter is only required if you want to use a nondefault KMS key . If this parameter is not specified, the default KMS key for Amazon EFS is used. This ID can be in one of the following formats:

        - Key ID - A unique identifier of the key, for example ``1234abcd-12ab-34cd-56ef-1234567890ab`` .
        - ARN - An Amazon Resource Name (ARN) for the key, for example ``arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`` .
        - Key alias - A previously created display name for a key, for example ``alias/projectKey1`` .
        - Key alias ARN - An ARN for a key alias, for example ``arn:aws:kms:us-west-2:444455556666:alias/projectKey1`` .

        If ``KmsKeyId`` is specified, the ``Encrypted`` parameter must be set to true.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lifecycle_policies(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFileSystem.LifecyclePolicyProperty]]]]:
        '''An array of ``LifecyclePolicy`` objects that define the file system's ``LifecycleConfiguration`` object.

        A ``LifecycleConfiguration`` object informs EFS lifecycle management and intelligent tiering of the following:

        - When to move files in the file system from primary storage to the IA storage class.
        - When to move files that are in IA storage to primary storage.

        .. epigraph::

           Amazon EFS requires that each ``LifecyclePolicy`` object have only a single transition. This means that in a request body, ``LifecyclePolicies`` needs to be structured as an array of ``LifecyclePolicy`` objects, one object for each transition, ``TransitionToIA`` , ``TransitionToPrimaryStorageClass`` . See the example requests in the following section for more information.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-lifecyclepolicies
        '''
        result = self._values.get("lifecycle_policies")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFileSystem.LifecyclePolicyProperty]]]], result)

    @builtins.property
    def performance_mode(self) -> typing.Optional[builtins.str]:
        '''The performance mode of the file system.

        We recommend ``generalPurpose`` performance mode for most file systems. File systems using the ``maxIO`` performance mode can scale to higher levels of aggregate throughput and operations per second with a tradeoff of slightly higher latencies for most file operations. The performance mode can't be changed after the file system has been created.
        .. epigraph::

           The ``maxIO`` mode is not supported on file systems using One Zone storage classes.

        Default is ``generalPurpose`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-performancemode
        '''
        result = self._values.get("performance_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provisioned_throughput_in_mibps(self) -> typing.Optional[jsii.Number]:
        '''The throughput, measured in mebibytes per second (MiBps), that you want to provision for a file system that you're creating.

        Required if ``ThroughputMode`` is set to ``provisioned`` . Valid values are 1-3414 MiBps, with the upper limit depending on Region. To increase this limit, contact AWS Support . For more information, see `Amazon EFS quotas that you can increase <https://docs.aws.amazon.com/efs/latest/ug/limits.html#soft-limits>`_ in the *Amazon EFS User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-provisionedthroughputinmibps
        '''
        result = self._values.get("provisioned_throughput_in_mibps")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def throughput_mode(self) -> typing.Optional[builtins.str]:
        '''Specifies the throughput mode for the file system.

        The mode can be ``bursting`` , ``provisioned`` , or ``elastic`` . If you set ``ThroughputMode`` to ``provisioned`` , you must also set a value for ``ProvisionedThroughputInMibps`` . After you create the file system, you can decrease your file system's throughput in Provisioned Throughput mode or change between the throughput modes, with certain time restrictions. For more information, see `Specifying throughput with provisioned mode <https://docs.aws.amazon.com/efs/latest/ug/performance.html#provisioned-throughput>`_ in the *Amazon EFS User Guide* .

        Default is ``elastic`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-efs-filesystem-throughputmode
        '''
        result = self._values.get("throughput_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFileSystemProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnMountTarget(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_efs.CfnMountTarget",
):
    '''The ``AWS::EFS::MountTarget`` resource is an Amazon EFS resource that creates a mount target for an EFS file system.

    You can then mount the file system on Amazon EC2 instances or other resources by using the mount target.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-mounttarget.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_efs as efs
        
        cfn_mount_target = efs.CfnMountTarget(self, "MyCfnMountTarget",
            file_system_id="fileSystemId",
            security_groups=["securityGroups"],
            subnet_id="subnetId",
        
            # the properties below are optional
            ip_address="ipAddress"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        file_system_id: builtins.str,
        security_groups: typing.Sequence[builtins.str],
        subnet_id: builtins.str,
        ip_address: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param file_system_id: The ID of the file system for which to create the mount target.
        :param security_groups: Up to five VPC security group IDs, of the form ``sg-xxxxxxxx`` . These must be for the same VPC as subnet specified.
        :param subnet_id: The ID of the subnet to add the mount target in. For file systems that use One Zone storage classes, use the subnet that is associated with the file system's Availability Zone.
        :param ip_address: Valid IPv4 address within the address range of the specified subnet.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53e47daec02e70bf8a73cac8e0366ac0f8a6af5ccf7598cf37952afe954d30bd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMountTargetProps(
            file_system_id=file_system_id,
            security_groups=security_groups,
            subnet_id=subnet_id,
            ip_address=ip_address,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb6e3b45bc9899160915641ff41c877062b796ef4defc0cec595a2913b545b0e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9a6f002228f19658915474a99c7342ed28bb87dd419575b819f330121028b1d4)
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
        '''The ID of the Amazon EFS file system that the mount target provides access to.

        Example: ``fs-0123456789111222a``

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrIpAddress")
    def attr_ip_address(self) -> builtins.str:
        '''The IPv4 address of the mount target.

        Example: 192.0.2.0

        :cloudformationAttribute: IpAddress
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIpAddress"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemId")
    def file_system_id(self) -> builtins.str:
        '''The ID of the file system for which to create the mount target.'''
        return typing.cast(builtins.str, jsii.get(self, "fileSystemId"))

    @file_system_id.setter
    def file_system_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c545a16b175530231985303ae48e8a4172cb3481a6b860def4e97a508f1c9e96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileSystemId", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.List[builtins.str]:
        '''Up to five VPC security group IDs, of the form ``sg-xxxxxxxx`` .'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroups"))

    @security_groups.setter
    def security_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__066c884c347c67446131a6b113dd92657eeddbf024cb39e3a188a1b06305d1c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroups", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        '''The ID of the subnet to add the mount target in.'''
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25e2f5c1fe6c4bf78d2c5698cccb1fc3bb199eff31e3534fa6957dabf3467bcc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="ipAddress")
    def ip_address(self) -> typing.Optional[builtins.str]:
        '''Valid IPv4 address within the address range of the specified subnet.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipAddress"))

    @ip_address.setter
    def ip_address(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__804f6c8cadefc6e3bd989db6da64591d147d67de340d096244f68a21842bb5ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddress", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_efs.CfnMountTargetProps",
    jsii_struct_bases=[],
    name_mapping={
        "file_system_id": "fileSystemId",
        "security_groups": "securityGroups",
        "subnet_id": "subnetId",
        "ip_address": "ipAddress",
    },
)
class CfnMountTargetProps:
    def __init__(
        self,
        *,
        file_system_id: builtins.str,
        security_groups: typing.Sequence[builtins.str],
        subnet_id: builtins.str,
        ip_address: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnMountTarget``.

        :param file_system_id: The ID of the file system for which to create the mount target.
        :param security_groups: Up to five VPC security group IDs, of the form ``sg-xxxxxxxx`` . These must be for the same VPC as subnet specified.
        :param subnet_id: The ID of the subnet to add the mount target in. For file systems that use One Zone storage classes, use the subnet that is associated with the file system's Availability Zone.
        :param ip_address: Valid IPv4 address within the address range of the specified subnet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-mounttarget.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_efs as efs
            
            cfn_mount_target_props = efs.CfnMountTargetProps(
                file_system_id="fileSystemId",
                security_groups=["securityGroups"],
                subnet_id="subnetId",
            
                # the properties below are optional
                ip_address="ipAddress"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2ad126af1a9797276c238562f8185eb06a56da00a9b12a35504f9d72fbdc711)
            check_type(argname="argument file_system_id", value=file_system_id, expected_type=type_hints["file_system_id"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            check_type(argname="argument ip_address", value=ip_address, expected_type=type_hints["ip_address"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "file_system_id": file_system_id,
            "security_groups": security_groups,
            "subnet_id": subnet_id,
        }
        if ip_address is not None:
            self._values["ip_address"] = ip_address

    @builtins.property
    def file_system_id(self) -> builtins.str:
        '''The ID of the file system for which to create the mount target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-mounttarget.html#cfn-efs-mounttarget-filesystemid
        '''
        result = self._values.get("file_system_id")
        assert result is not None, "Required property 'file_system_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_groups(self) -> typing.List[builtins.str]:
        '''Up to five VPC security group IDs, of the form ``sg-xxxxxxxx`` .

        These must be for the same VPC as subnet specified.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-mounttarget.html#cfn-efs-mounttarget-securitygroups
        '''
        result = self._values.get("security_groups")
        assert result is not None, "Required property 'security_groups' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def subnet_id(self) -> builtins.str:
        '''The ID of the subnet to add the mount target in.

        For file systems that use One Zone storage classes, use the subnet that is associated with the file system's Availability Zone.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-mounttarget.html#cfn-efs-mounttarget-subnetid
        '''
        result = self._values.get("subnet_id")
        assert result is not None, "Required property 'subnet_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ip_address(self) -> typing.Optional[builtins.str]:
        '''Valid IPv4 address within the address range of the specified subnet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-mounttarget.html#cfn-efs-mounttarget-ipaddress
        '''
        result = self._values.get("ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMountTargetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_efs.FileSystemAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "security_group": "securityGroup",
        "file_system_arn": "fileSystemArn",
        "file_system_id": "fileSystemId",
    },
)
class FileSystemAttributes:
    def __init__(
        self,
        *,
        security_group: _ISecurityGroup_acf8a799,
        file_system_arn: typing.Optional[builtins.str] = None,
        file_system_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties that describe an existing EFS file system.

        :param security_group: The security group of the file system.
        :param file_system_arn: The File System's Arn. Default: - determined based on fileSystemId
        :param file_system_id: The File System's ID. Default: - determined based on fileSystemArn

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_iam as iam
            
            
            imported_file_system = efs.FileSystem.from_file_system_attributes(self, "existingFS",
                file_system_id="fs-12345678",  # You can also use fileSystemArn instead of fileSystemId.
                security_group=ec2.SecurityGroup.from_security_group_id(self, "SG", "sg-123456789",
                    allow_all_outbound=False
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7f9028e19d4f85ea9a53bb13e46bb5ac917443add6e7ec5e117fdc6136100b7)
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
            check_type(argname="argument file_system_arn", value=file_system_arn, expected_type=type_hints["file_system_arn"])
            check_type(argname="argument file_system_id", value=file_system_id, expected_type=type_hints["file_system_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "security_group": security_group,
        }
        if file_system_arn is not None:
            self._values["file_system_arn"] = file_system_arn
        if file_system_id is not None:
            self._values["file_system_id"] = file_system_id

    @builtins.property
    def security_group(self) -> _ISecurityGroup_acf8a799:
        '''The security group of the file system.'''
        result = self._values.get("security_group")
        assert result is not None, "Required property 'security_group' is missing"
        return typing.cast(_ISecurityGroup_acf8a799, result)

    @builtins.property
    def file_system_arn(self) -> typing.Optional[builtins.str]:
        '''The File System's Arn.

        :default: - determined based on fileSystemId
        '''
        result = self._values.get("file_system_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_system_id(self) -> typing.Optional[builtins.str]:
        '''The File System's ID.

        :default: - determined based on fileSystemArn
        '''
        result = self._values.get("file_system_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FileSystemAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_efs.FileSystemProps",
    jsii_struct_bases=[],
    name_mapping={
        "vpc": "vpc",
        "enable_automatic_backups": "enableAutomaticBackups",
        "encrypted": "encrypted",
        "file_system_name": "fileSystemName",
        "file_system_policy": "fileSystemPolicy",
        "kms_key": "kmsKey",
        "lifecycle_policy": "lifecyclePolicy",
        "out_of_infrequent_access_policy": "outOfInfrequentAccessPolicy",
        "performance_mode": "performanceMode",
        "provisioned_throughput_per_second": "provisionedThroughputPerSecond",
        "removal_policy": "removalPolicy",
        "security_group": "securityGroup",
        "throughput_mode": "throughputMode",
        "vpc_subnets": "vpcSubnets",
    },
)
class FileSystemProps:
    def __init__(
        self,
        *,
        vpc: _IVpc_f30d5663,
        enable_automatic_backups: typing.Optional[builtins.bool] = None,
        encrypted: typing.Optional[builtins.bool] = None,
        file_system_name: typing.Optional[builtins.str] = None,
        file_system_policy: typing.Optional[_PolicyDocument_3ac34393] = None,
        kms_key: typing.Optional[_IKey_5f11635f] = None,
        lifecycle_policy: typing.Optional["LifecyclePolicy"] = None,
        out_of_infrequent_access_policy: typing.Optional["OutOfInfrequentAccessPolicy"] = None,
        performance_mode: typing.Optional["PerformanceMode"] = None,
        provisioned_throughput_per_second: typing.Optional[_Size_7b441c34] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
        security_group: typing.Optional[_ISecurityGroup_acf8a799] = None,
        throughput_mode: typing.Optional["ThroughputMode"] = None,
        vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Properties of EFS FileSystem.

        :param vpc: VPC to launch the file system in.
        :param enable_automatic_backups: Whether to enable automatic backups for the file system. Default: false
        :param encrypted: Defines if the data at rest in the file system is encrypted or not. Default: - If your application has the '@aws-cdk/aws-efs:defaultEncryptionAtRest' feature flag set, the default is true, otherwise, the default is false.
        :param file_system_name: The file system's name. Default: - CDK generated name
        :param file_system_policy: File system policy is an IAM resource policy used to control NFS access to an EFS file system. Default: none
        :param kms_key: The KMS key used for encryption. This is required to encrypt the data at rest if Default: - if 'encrypted' is true, the default key for EFS (/aws/elasticfilesystem) is used
        :param lifecycle_policy: A policy used by EFS lifecycle management to transition files to the Infrequent Access (IA) storage class. Default: - None. EFS will not transition files to the IA storage class.
        :param out_of_infrequent_access_policy: A policy used by EFS lifecycle management to transition files from Infrequent Access (IA) storage class to primary storage class. Default: - None. EFS will not transition files from IA storage to primary storage.
        :param performance_mode: The performance mode that the file system will operate under. An Amazon EFS file system's performance mode can't be changed after the file system has been created. Updating this property will replace the file system. Default: PerformanceMode.GENERAL_PURPOSE
        :param provisioned_throughput_per_second: Provisioned throughput for the file system. This is a required property if the throughput mode is set to PROVISIONED. Must be at least 1MiB/s. Default: - none, errors out
        :param removal_policy: The removal policy to apply to the file system. Default: RemovalPolicy.RETAIN
        :param security_group: Security Group to assign to this file system. Default: - creates new security group which allows all outbound traffic
        :param throughput_mode: Enum to mention the throughput mode of the file system. Default: ThroughputMode.BURSTING
        :param vpc_subnets: Which subnets to place the mount target in the VPC. Default: - the Vpc default strategy if not specified

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_iam as iam
            
            
            my_file_system_policy = iam.PolicyDocument(
                statements=[iam.PolicyStatement(
                    actions=["elasticfilesystem:ClientWrite", "elasticfilesystem:ClientMount"
                    ],
                    principals=[iam.AccountRootPrincipal()],
                    resources=["*"],
                    conditions={
                        "Bool": {
                            "elasticfilesystem:AccessedViaMountTarget": "true"
                        }
                    }
                )]
            )
            
            file_system = efs.FileSystem(self, "MyEfsFileSystem",
                vpc=ec2.Vpc(self, "VPC"),
                file_system_policy=my_file_system_policy
            )
        '''
        if isinstance(vpc_subnets, dict):
            vpc_subnets = _SubnetSelection_e57d76df(**vpc_subnets)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a11d59607a7c01a190b2b0587733658cfcb8eddfb252f3c48abdc988b9f09cff)
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument enable_automatic_backups", value=enable_automatic_backups, expected_type=type_hints["enable_automatic_backups"])
            check_type(argname="argument encrypted", value=encrypted, expected_type=type_hints["encrypted"])
            check_type(argname="argument file_system_name", value=file_system_name, expected_type=type_hints["file_system_name"])
            check_type(argname="argument file_system_policy", value=file_system_policy, expected_type=type_hints["file_system_policy"])
            check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
            check_type(argname="argument lifecycle_policy", value=lifecycle_policy, expected_type=type_hints["lifecycle_policy"])
            check_type(argname="argument out_of_infrequent_access_policy", value=out_of_infrequent_access_policy, expected_type=type_hints["out_of_infrequent_access_policy"])
            check_type(argname="argument performance_mode", value=performance_mode, expected_type=type_hints["performance_mode"])
            check_type(argname="argument provisioned_throughput_per_second", value=provisioned_throughput_per_second, expected_type=type_hints["provisioned_throughput_per_second"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
            check_type(argname="argument throughput_mode", value=throughput_mode, expected_type=type_hints["throughput_mode"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vpc": vpc,
        }
        if enable_automatic_backups is not None:
            self._values["enable_automatic_backups"] = enable_automatic_backups
        if encrypted is not None:
            self._values["encrypted"] = encrypted
        if file_system_name is not None:
            self._values["file_system_name"] = file_system_name
        if file_system_policy is not None:
            self._values["file_system_policy"] = file_system_policy
        if kms_key is not None:
            self._values["kms_key"] = kms_key
        if lifecycle_policy is not None:
            self._values["lifecycle_policy"] = lifecycle_policy
        if out_of_infrequent_access_policy is not None:
            self._values["out_of_infrequent_access_policy"] = out_of_infrequent_access_policy
        if performance_mode is not None:
            self._values["performance_mode"] = performance_mode
        if provisioned_throughput_per_second is not None:
            self._values["provisioned_throughput_per_second"] = provisioned_throughput_per_second
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if security_group is not None:
            self._values["security_group"] = security_group
        if throughput_mode is not None:
            self._values["throughput_mode"] = throughput_mode
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets

    @builtins.property
    def vpc(self) -> _IVpc_f30d5663:
        '''VPC to launch the file system in.'''
        result = self._values.get("vpc")
        assert result is not None, "Required property 'vpc' is missing"
        return typing.cast(_IVpc_f30d5663, result)

    @builtins.property
    def enable_automatic_backups(self) -> typing.Optional[builtins.bool]:
        '''Whether to enable automatic backups for the file system.

        :default: false
        '''
        result = self._values.get("enable_automatic_backups")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def encrypted(self) -> typing.Optional[builtins.bool]:
        '''Defines if the data at rest in the file system is encrypted or not.

        :default: - If your application has the '@aws-cdk/aws-efs:defaultEncryptionAtRest' feature flag set, the default is true, otherwise, the default is false.

        :link: https://docs.aws.amazon.com/cdk/latest/guide/featureflags.html
        '''
        result = self._values.get("encrypted")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def file_system_name(self) -> typing.Optional[builtins.str]:
        '''The file system's name.

        :default: - CDK generated name
        '''
        result = self._values.get("file_system_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_system_policy(self) -> typing.Optional[_PolicyDocument_3ac34393]:
        '''File system policy is an IAM resource policy used to control NFS access to an EFS file system.

        :default: none
        '''
        result = self._values.get("file_system_policy")
        return typing.cast(typing.Optional[_PolicyDocument_3ac34393], result)

    @builtins.property
    def kms_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''The KMS key used for encryption.

        This is required to encrypt the data at rest if

        :default: - if 'encrypted' is true, the default key for EFS (/aws/elasticfilesystem) is used

        :encrypted: is set to true.
        '''
        result = self._values.get("kms_key")
        return typing.cast(typing.Optional[_IKey_5f11635f], result)

    @builtins.property
    def lifecycle_policy(self) -> typing.Optional["LifecyclePolicy"]:
        '''A policy used by EFS lifecycle management to transition files to the Infrequent Access (IA) storage class.

        :default: - None. EFS will not transition files to the IA storage class.
        '''
        result = self._values.get("lifecycle_policy")
        return typing.cast(typing.Optional["LifecyclePolicy"], result)

    @builtins.property
    def out_of_infrequent_access_policy(
        self,
    ) -> typing.Optional["OutOfInfrequentAccessPolicy"]:
        '''A policy used by EFS lifecycle management to transition files from Infrequent Access (IA) storage class to primary storage class.

        :default: - None. EFS will not transition files from IA storage to primary storage.
        '''
        result = self._values.get("out_of_infrequent_access_policy")
        return typing.cast(typing.Optional["OutOfInfrequentAccessPolicy"], result)

    @builtins.property
    def performance_mode(self) -> typing.Optional["PerformanceMode"]:
        '''The performance mode that the file system will operate under.

        An Amazon EFS file system's performance mode can't be changed after the file system has been created.
        Updating this property will replace the file system.

        :default: PerformanceMode.GENERAL_PURPOSE
        '''
        result = self._values.get("performance_mode")
        return typing.cast(typing.Optional["PerformanceMode"], result)

    @builtins.property
    def provisioned_throughput_per_second(self) -> typing.Optional[_Size_7b441c34]:
        '''Provisioned throughput for the file system.

        This is a required property if the throughput mode is set to PROVISIONED.
        Must be at least 1MiB/s.

        :default: - none, errors out
        '''
        result = self._values.get("provisioned_throughput_per_second")
        return typing.cast(typing.Optional[_Size_7b441c34], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[_RemovalPolicy_9f93c814]:
        '''The removal policy to apply to the file system.

        :default: RemovalPolicy.RETAIN
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_RemovalPolicy_9f93c814], result)

    @builtins.property
    def security_group(self) -> typing.Optional[_ISecurityGroup_acf8a799]:
        '''Security Group to assign to this file system.

        :default: - creates new security group which allows all outbound traffic
        '''
        result = self._values.get("security_group")
        return typing.cast(typing.Optional[_ISecurityGroup_acf8a799], result)

    @builtins.property
    def throughput_mode(self) -> typing.Optional["ThroughputMode"]:
        '''Enum to mention the throughput mode of the file system.

        :default: ThroughputMode.BURSTING
        '''
        result = self._values.get("throughput_mode")
        return typing.cast(typing.Optional["ThroughputMode"], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[_SubnetSelection_e57d76df]:
        '''Which subnets to place the mount target in the VPC.

        :default: - the Vpc default strategy if not specified
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[_SubnetSelection_e57d76df], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FileSystemProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.aws_efs.IAccessPoint")
class IAccessPoint(_IResource_c80c4260, typing_extensions.Protocol):
    '''Represents an EFS AccessPoint.'''

    @builtins.property
    @jsii.member(jsii_name="accessPointArn")
    def access_point_arn(self) -> builtins.str:
        '''The ARN of the AccessPoint.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="accessPointId")
    def access_point_id(self) -> builtins.str:
        '''The ID of the AccessPoint.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="fileSystem")
    def file_system(self) -> "IFileSystem":
        '''The EFS file system.'''
        ...


class _IAccessPointProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''Represents an EFS AccessPoint.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_efs.IAccessPoint"

    @builtins.property
    @jsii.member(jsii_name="accessPointArn")
    def access_point_arn(self) -> builtins.str:
        '''The ARN of the AccessPoint.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "accessPointArn"))

    @builtins.property
    @jsii.member(jsii_name="accessPointId")
    def access_point_id(self) -> builtins.str:
        '''The ID of the AccessPoint.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "accessPointId"))

    @builtins.property
    @jsii.member(jsii_name="fileSystem")
    def file_system(self) -> "IFileSystem":
        '''The EFS file system.'''
        return typing.cast("IFileSystem", jsii.get(self, "fileSystem"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAccessPoint).__jsii_proxy_class__ = lambda : _IAccessPointProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_efs.IFileSystem")
class IFileSystem(
    _IConnectable_10015a05,
    _IResourceWithPolicy_720d64fc,
    typing_extensions.Protocol,
):
    '''Represents an Amazon EFS file system.'''

    @builtins.property
    @jsii.member(jsii_name="fileSystemArn")
    def file_system_arn(self) -> builtins.str:
        '''The ARN of the file system.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="fileSystemId")
    def file_system_id(self) -> builtins.str:
        '''The ID of the file system, assigned by Amazon EFS.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="mountTargetsAvailable")
    def mount_targets_available(self) -> _constructs_77d1e7e8.IDependable:
        '''Dependable that can be depended upon to ensure the mount targets of the filesystem are ready.'''
        ...

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Grant the actions defined in actions to the given grantee on this File System resource.

        :param grantee: -
        :param actions: -
        '''
        ...


class _IFileSystemProxy(
    jsii.proxy_for(_IConnectable_10015a05), # type: ignore[misc]
    jsii.proxy_for(_IResourceWithPolicy_720d64fc), # type: ignore[misc]
):
    '''Represents an Amazon EFS file system.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_efs.IFileSystem"

    @builtins.property
    @jsii.member(jsii_name="fileSystemArn")
    def file_system_arn(self) -> builtins.str:
        '''The ARN of the file system.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "fileSystemArn"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemId")
    def file_system_id(self) -> builtins.str:
        '''The ID of the file system, assigned by Amazon EFS.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "fileSystemId"))

    @builtins.property
    @jsii.member(jsii_name="mountTargetsAvailable")
    def mount_targets_available(self) -> _constructs_77d1e7e8.IDependable:
        '''Dependable that can be depended upon to ensure the mount targets of the filesystem are ready.'''
        return typing.cast(_constructs_77d1e7e8.IDependable, jsii.get(self, "mountTargetsAvailable"))

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Grant the actions defined in actions to the given grantee on this File System resource.

        :param grantee: -
        :param actions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d30690bfc35cb7c7060f6f609a976e22081bcba7be3b93da3b5b3a122eae8ece)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grant", [grantee, *actions]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFileSystem).__jsii_proxy_class__ = lambda : _IFileSystemProxy


@jsii.enum(jsii_type="aws-cdk-lib.aws_efs.LifecyclePolicy")
class LifecyclePolicy(enum.Enum):
    '''EFS Lifecycle Policy, if a file is not accessed for given days, it will move to EFS Infrequent Access.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html#cfn-elasticfilesystem-filesystem-lifecyclepolicies
    :exampleMetadata: infused

    Example::

        file_system = efs.FileSystem(self, "MyEfsFileSystem",
            vpc=ec2.Vpc(self, "VPC"),
            lifecycle_policy=efs.LifecyclePolicy.AFTER_14_DAYS,  # files are not transitioned to infrequent access (IA) storage by default
            performance_mode=efs.PerformanceMode.GENERAL_PURPOSE,  # default
            out_of_infrequent_access_policy=efs.OutOfInfrequentAccessPolicy.AFTER_1_ACCESS
        )
    '''

    AFTER_1_DAY = "AFTER_1_DAY"
    '''After 1 day of not being accessed.'''
    AFTER_7_DAYS = "AFTER_7_DAYS"
    '''After 7 days of not being accessed.'''
    AFTER_14_DAYS = "AFTER_14_DAYS"
    '''After 14 days of not being accessed.'''
    AFTER_30_DAYS = "AFTER_30_DAYS"
    '''After 30 days of not being accessed.'''
    AFTER_60_DAYS = "AFTER_60_DAYS"
    '''After 60 days of not being accessed.'''
    AFTER_90_DAYS = "AFTER_90_DAYS"
    '''After 90 days of not being accessed.'''


@jsii.enum(jsii_type="aws-cdk-lib.aws_efs.OutOfInfrequentAccessPolicy")
class OutOfInfrequentAccessPolicy(enum.Enum):
    '''EFS Out Of Infrequent Access Policy, if a file is accessed given times, it will move back to primary storage class.

    :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-lifecyclepolicy.html#cfn-efs-filesystem-lifecyclepolicy-transitiontoprimarystorageclass
    :exampleMetadata: infused

    Example::

        file_system = efs.FileSystem(self, "MyEfsFileSystem",
            vpc=ec2.Vpc(self, "VPC"),
            lifecycle_policy=efs.LifecyclePolicy.AFTER_14_DAYS,  # files are not transitioned to infrequent access (IA) storage by default
            performance_mode=efs.PerformanceMode.GENERAL_PURPOSE,  # default
            out_of_infrequent_access_policy=efs.OutOfInfrequentAccessPolicy.AFTER_1_ACCESS
        )
    '''

    AFTER_1_ACCESS = "AFTER_1_ACCESS"
    '''After 1 access.'''


@jsii.enum(jsii_type="aws-cdk-lib.aws_efs.PerformanceMode")
class PerformanceMode(enum.Enum):
    '''EFS Performance mode.

    :see: https://docs.aws.amazon.com/efs/latest/ug/performance.html#performancemodes
    :exampleMetadata: infused

    Example::

        file_system = efs.FileSystem(self, "MyEfsFileSystem",
            vpc=ec2.Vpc(self, "VPC"),
            lifecycle_policy=efs.LifecyclePolicy.AFTER_14_DAYS,  # files are not transitioned to infrequent access (IA) storage by default
            performance_mode=efs.PerformanceMode.GENERAL_PURPOSE,  # default
            out_of_infrequent_access_policy=efs.OutOfInfrequentAccessPolicy.AFTER_1_ACCESS
        )
    '''

    GENERAL_PURPOSE = "GENERAL_PURPOSE"
    '''General Purpose is ideal for latency-sensitive use cases, like web serving environments, content management systems, home directories, and general file serving.

    Recommended for the majority of Amazon EFS file systems.
    '''
    MAX_IO = "MAX_IO"
    '''File systems in the Max I/O mode can scale to higher levels of aggregate throughput and operations per second.

    This scaling is done with a tradeoff
    of slightly higher latencies for file metadata operations.
    Highly parallelized applications and workloads, such as big data analysis,
    media processing, and genomics analysis, can benefit from this mode.
    '''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_efs.PosixUser",
    jsii_struct_bases=[],
    name_mapping={"gid": "gid", "uid": "uid", "secondary_gids": "secondaryGids"},
)
class PosixUser:
    def __init__(
        self,
        *,
        gid: builtins.str,
        uid: builtins.str,
        secondary_gids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Represents the PosixUser.

        :param gid: The POSIX group ID used for all file system operations using this access point.
        :param uid: The POSIX user ID used for all file system operations using this access point.
        :param secondary_gids: Secondary POSIX group IDs used for all file system operations using this access point. Default: - None

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_ec2 as ec2
            import aws_cdk.aws_efs as efs
            
            
            # create a new VPC
            vpc = ec2.Vpc(self, "VPC")
            
            # create a new Amazon EFS filesystem
            file_system = efs.FileSystem(self, "Efs", vpc=vpc)
            
            # create a new access point from the filesystem
            access_point = file_system.add_access_point("AccessPoint",
                # set /export/lambda as the root of the access point
                path="/export/lambda",
                # as /export/lambda does not exist in a new efs filesystem, the efs will create the directory with the following createAcl
                create_acl=efs.Acl(
                    owner_uid="1001",
                    owner_gid="1001",
                    permissions="750"
                ),
                # enforce the POSIX identity so lambda function will access with this identity
                posix_user=efs.PosixUser(
                    uid="1001",
                    gid="1001"
                )
            )
            
            fn = lambda_.Function(self, "MyLambda",
                # mount the access point to /mnt/msg in the lambda runtime environment
                filesystem=lambda_.FileSystem.from_efs_access_point(access_point, "/mnt/msg"),
                runtime=lambda_.Runtime.NODEJS_18_X,
                handler="index.handler",
                code=lambda_.Code.from_asset(path.join(__dirname, "lambda-handler")),
                vpc=vpc
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c952f8c1704201f25c4d7df8b8a5c994569b8513be332681526a695abb83999b)
            check_type(argname="argument gid", value=gid, expected_type=type_hints["gid"])
            check_type(argname="argument uid", value=uid, expected_type=type_hints["uid"])
            check_type(argname="argument secondary_gids", value=secondary_gids, expected_type=type_hints["secondary_gids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "gid": gid,
            "uid": uid,
        }
        if secondary_gids is not None:
            self._values["secondary_gids"] = secondary_gids

    @builtins.property
    def gid(self) -> builtins.str:
        '''The POSIX group ID used for all file system operations using this access point.'''
        result = self._values.get("gid")
        assert result is not None, "Required property 'gid' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def uid(self) -> builtins.str:
        '''The POSIX user ID used for all file system operations using this access point.'''
        result = self._values.get("uid")
        assert result is not None, "Required property 'uid' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def secondary_gids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Secondary POSIX group IDs used for all file system operations using this access point.

        :default: - None
        '''
        result = self._values.get("secondary_gids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PosixUser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_efs.ThroughputMode")
class ThroughputMode(enum.Enum):
    '''EFS Throughput mode.

    :see: https://docs.aws.amazon.com/efs/latest/ug/performance.html#throughput-modes
    '''

    BURSTING = "BURSTING"
    '''This mode scales as the size of the file system in the standard storage class grows.'''
    PROVISIONED = "PROVISIONED"
    '''This mode can instantly provision the throughput of the file system (in MiB/s) independent of the amount of data stored.'''
    ELASTIC = "ELASTIC"
    '''This mode scales the throughput automatically regardless of file system size.'''


@jsii.implements(IAccessPoint)
class AccessPoint(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_efs.AccessPoint",
):
    '''Represents the AccessPoint.

    :exampleMetadata: infused

    Example::

        efs.AccessPoint.from_access_point_attributes(self, "ap",
            access_point_id="fsap-1293c4d9832fo0912",
            file_system=efs.FileSystem.from_file_system_attributes(self, "efs",
                file_system_id="fs-099d3e2f",
                security_group=ec2.SecurityGroup.from_security_group_id(self, "sg", "sg-51530134")
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        file_system: IFileSystem,
        create_acl: typing.Optional[typing.Union[Acl, typing.Dict[builtins.str, typing.Any]]] = None,
        path: typing.Optional[builtins.str] = None,
        posix_user: typing.Optional[typing.Union[PosixUser, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param file_system: The efs filesystem.
        :param create_acl: Specifies the POSIX IDs and permissions to apply when creating the access point's root directory. If the root directory specified by ``path`` does not exist, EFS creates the root directory and applies the permissions specified here. If the specified ``path`` does not exist, you must specify ``createAcl``. Default: - None. The directory specified by ``path`` must exist.
        :param path: Specifies the path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system. Default: '/'
        :param posix_user: The full POSIX identity, including the user ID, group ID, and any secondary group IDs, on the access point that is used for all file system operations performed by NFS clients using the access point. Specify this to enforce a user identity using an access point. Default: - user identity not enforced
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4cd5acd3aac2348517085a4188b85a5e2329da4dc443644482b9153e1014bfa)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = AccessPointProps(
            file_system=file_system,
            create_acl=create_acl,
            path=path,
            posix_user=posix_user,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromAccessPointAttributes")
    @builtins.classmethod
    def from_access_point_attributes(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        access_point_arn: typing.Optional[builtins.str] = None,
        access_point_id: typing.Optional[builtins.str] = None,
        file_system: typing.Optional[IFileSystem] = None,
    ) -> IAccessPoint:
        '''Import an existing Access Point by attributes.

        :param scope: -
        :param id: -
        :param access_point_arn: The ARN of the AccessPoint One of this, or ``accessPointId`` is required. Default: - determined based on accessPointId
        :param access_point_id: The ID of the AccessPoint One of this, or ``accessPointArn`` is required. Default: - determined based on accessPointArn
        :param file_system: The EFS file system. Default: - no EFS file system
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0959a679ec1620c39a9d0f9763692323c37cf7d3425d339a42722079da77067)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = AccessPointAttributes(
            access_point_arn=access_point_arn,
            access_point_id=access_point_id,
            file_system=file_system,
        )

        return typing.cast(IAccessPoint, jsii.sinvoke(cls, "fromAccessPointAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="fromAccessPointId")
    @builtins.classmethod
    def from_access_point_id(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        access_point_id: builtins.str,
    ) -> IAccessPoint:
        '''Import an existing Access Point by id.

        :param scope: -
        :param id: -
        :param access_point_id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d38e8f8212fb31c6248399b59a7a6bc5264d8d91253af77c2da7346b497f98a4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument access_point_id", value=access_point_id, expected_type=type_hints["access_point_id"])
        return typing.cast(IAccessPoint, jsii.sinvoke(cls, "fromAccessPointId", [scope, id, access_point_id]))

    @builtins.property
    @jsii.member(jsii_name="accessPointArn")
    def access_point_arn(self) -> builtins.str:
        '''The ARN of the Access Point.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "accessPointArn"))

    @builtins.property
    @jsii.member(jsii_name="accessPointId")
    def access_point_id(self) -> builtins.str:
        '''The ID of the Access Point.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "accessPointId"))

    @builtins.property
    @jsii.member(jsii_name="fileSystem")
    def file_system(self) -> IFileSystem:
        '''The file system of the access point.'''
        return typing.cast(IFileSystem, jsii.get(self, "fileSystem"))


@jsii.implements(IFileSystem)
class FileSystem(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_efs.FileSystem",
):
    '''The Elastic File System implementation of IFileSystem.

    It creates a new, empty file system in Amazon Elastic File System (Amazon EFS).
    It also creates mount target (AWS::EFS::MountTarget) implicitly to mount the
    EFS file system on an Amazon Elastic Compute Cloud (Amazon EC2) instance or another resource.

    :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html
    :resource: AWS::EFS::FileSystem
    :exampleMetadata: infused

    Example::

        file_system = efs.FileSystem(self, "MyEfsFileSystem",
            vpc=ec2.Vpc(self, "VPC"),
            lifecycle_policy=efs.LifecyclePolicy.AFTER_14_DAYS,  # files are not transitioned to infrequent access (IA) storage by default
            performance_mode=efs.PerformanceMode.GENERAL_PURPOSE,  # default
            out_of_infrequent_access_policy=efs.OutOfInfrequentAccessPolicy.AFTER_1_ACCESS
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        vpc: _IVpc_f30d5663,
        enable_automatic_backups: typing.Optional[builtins.bool] = None,
        encrypted: typing.Optional[builtins.bool] = None,
        file_system_name: typing.Optional[builtins.str] = None,
        file_system_policy: typing.Optional[_PolicyDocument_3ac34393] = None,
        kms_key: typing.Optional[_IKey_5f11635f] = None,
        lifecycle_policy: typing.Optional[LifecyclePolicy] = None,
        out_of_infrequent_access_policy: typing.Optional[OutOfInfrequentAccessPolicy] = None,
        performance_mode: typing.Optional[PerformanceMode] = None,
        provisioned_throughput_per_second: typing.Optional[_Size_7b441c34] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
        security_group: typing.Optional[_ISecurityGroup_acf8a799] = None,
        throughput_mode: typing.Optional[ThroughputMode] = None,
        vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Constructor for creating a new EFS FileSystem.

        :param scope: -
        :param id: -
        :param vpc: VPC to launch the file system in.
        :param enable_automatic_backups: Whether to enable automatic backups for the file system. Default: false
        :param encrypted: Defines if the data at rest in the file system is encrypted or not. Default: - If your application has the '@aws-cdk/aws-efs:defaultEncryptionAtRest' feature flag set, the default is true, otherwise, the default is false.
        :param file_system_name: The file system's name. Default: - CDK generated name
        :param file_system_policy: File system policy is an IAM resource policy used to control NFS access to an EFS file system. Default: none
        :param kms_key: The KMS key used for encryption. This is required to encrypt the data at rest if Default: - if 'encrypted' is true, the default key for EFS (/aws/elasticfilesystem) is used
        :param lifecycle_policy: A policy used by EFS lifecycle management to transition files to the Infrequent Access (IA) storage class. Default: - None. EFS will not transition files to the IA storage class.
        :param out_of_infrequent_access_policy: A policy used by EFS lifecycle management to transition files from Infrequent Access (IA) storage class to primary storage class. Default: - None. EFS will not transition files from IA storage to primary storage.
        :param performance_mode: The performance mode that the file system will operate under. An Amazon EFS file system's performance mode can't be changed after the file system has been created. Updating this property will replace the file system. Default: PerformanceMode.GENERAL_PURPOSE
        :param provisioned_throughput_per_second: Provisioned throughput for the file system. This is a required property if the throughput mode is set to PROVISIONED. Must be at least 1MiB/s. Default: - none, errors out
        :param removal_policy: The removal policy to apply to the file system. Default: RemovalPolicy.RETAIN
        :param security_group: Security Group to assign to this file system. Default: - creates new security group which allows all outbound traffic
        :param throughput_mode: Enum to mention the throughput mode of the file system. Default: ThroughputMode.BURSTING
        :param vpc_subnets: Which subnets to place the mount target in the VPC. Default: - the Vpc default strategy if not specified
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe7547e76a3f3502ef6c67d1cc851b25d13fe1b4b980d3bccee8eae2ff469690)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = FileSystemProps(
            vpc=vpc,
            enable_automatic_backups=enable_automatic_backups,
            encrypted=encrypted,
            file_system_name=file_system_name,
            file_system_policy=file_system_policy,
            kms_key=kms_key,
            lifecycle_policy=lifecycle_policy,
            out_of_infrequent_access_policy=out_of_infrequent_access_policy,
            performance_mode=performance_mode,
            provisioned_throughput_per_second=provisioned_throughput_per_second,
            removal_policy=removal_policy,
            security_group=security_group,
            throughput_mode=throughput_mode,
            vpc_subnets=vpc_subnets,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromFileSystemAttributes")
    @builtins.classmethod
    def from_file_system_attributes(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        security_group: _ISecurityGroup_acf8a799,
        file_system_arn: typing.Optional[builtins.str] = None,
        file_system_id: typing.Optional[builtins.str] = None,
    ) -> IFileSystem:
        '''Import an existing File System from the given properties.

        :param scope: -
        :param id: -
        :param security_group: The security group of the file system.
        :param file_system_arn: The File System's Arn. Default: - determined based on fileSystemId
        :param file_system_id: The File System's ID. Default: - determined based on fileSystemArn
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dece37ce89e2cfb5f78f1232aff0c1114df92cbaea2ee4e9ea83cdad9812a448)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = FileSystemAttributes(
            security_group=security_group,
            file_system_arn=file_system_arn,
            file_system_id=file_system_id,
        )

        return typing.cast(IFileSystem, jsii.sinvoke(cls, "fromFileSystemAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="addAccessPoint")
    def add_access_point(
        self,
        id: builtins.str,
        *,
        create_acl: typing.Optional[typing.Union[Acl, typing.Dict[builtins.str, typing.Any]]] = None,
        path: typing.Optional[builtins.str] = None,
        posix_user: typing.Optional[typing.Union[PosixUser, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> AccessPoint:
        '''create access point from this filesystem.

        :param id: -
        :param create_acl: Specifies the POSIX IDs and permissions to apply when creating the access point's root directory. If the root directory specified by ``path`` does not exist, EFS creates the root directory and applies the permissions specified here. If the specified ``path`` does not exist, you must specify ``createAcl``. Default: - None. The directory specified by ``path`` must exist.
        :param path: Specifies the path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system. Default: '/'
        :param posix_user: The full POSIX identity, including the user ID, group ID, and any secondary group IDs, on the access point that is used for all file system operations performed by NFS clients using the access point. Specify this to enforce a user identity using an access point. Default: - user identity not enforced
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ae17f92be1f854e9add049e3ad7507b46fbd97b0ceecc5921b74cffabc0fd7f)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        access_point_options = AccessPointOptions(
            create_acl=create_acl, path=path, posix_user=posix_user
        )

        return typing.cast(AccessPoint, jsii.invoke(self, "addAccessPoint", [id, access_point_options]))

    @jsii.member(jsii_name="addToResourcePolicy")
    def add_to_resource_policy(
        self,
        statement: _PolicyStatement_0fe33853,
    ) -> _AddToResourcePolicyResult_1d0a53ad:
        '''Adds a statement to the resource policy associated with this file system.

        A resource policy will be automatically created upon the first call to ``addToResourcePolicy``.

        Note that this does not work with imported file systems.

        :param statement: The policy statement to add.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1eff11f92ecb28f1cedf7f1f5bd707e2f23777bb0f90efb50e5454827f766dd7)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(_AddToResourcePolicyResult_1d0a53ad, jsii.invoke(self, "addToResourcePolicy", [statement]))

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Grant the actions defined in actions to the given grantee on this File System resource.

        :param grantee: Principal to grant right to.
        :param actions: The actions to grant.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d469ca5d09698c2cd0c0b2ce1f4112950cbc13abe1c176ec39092c058940a48)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grant", [grantee, *actions]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DEFAULT_PORT")
    def DEFAULT_PORT(cls) -> jsii.Number:
        '''The default port File System listens on.'''
        return typing.cast(jsii.Number, jsii.sget(cls, "DEFAULT_PORT"))

    @builtins.property
    @jsii.member(jsii_name="connections")
    def connections(self) -> _Connections_0f31fce8:
        '''The security groups/rules used to allow network connections to the file system.'''
        return typing.cast(_Connections_0f31fce8, jsii.get(self, "connections"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemArn")
    def file_system_arn(self) -> builtins.str:
        '''The ARN of the file system.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "fileSystemArn"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemId")
    def file_system_id(self) -> builtins.str:
        '''The ID of the file system, assigned by Amazon EFS.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "fileSystemId"))

    @builtins.property
    @jsii.member(jsii_name="mountTargetsAvailable")
    def mount_targets_available(self) -> _constructs_77d1e7e8.IDependable:
        '''Dependable that can be depended upon to ensure the mount targets of the filesystem are ready.'''
        return typing.cast(_constructs_77d1e7e8.IDependable, jsii.get(self, "mountTargetsAvailable"))


__all__ = [
    "AccessPoint",
    "AccessPointAttributes",
    "AccessPointOptions",
    "AccessPointProps",
    "Acl",
    "CfnAccessPoint",
    "CfnAccessPointProps",
    "CfnFileSystem",
    "CfnFileSystemProps",
    "CfnMountTarget",
    "CfnMountTargetProps",
    "FileSystem",
    "FileSystemAttributes",
    "FileSystemProps",
    "IAccessPoint",
    "IFileSystem",
    "LifecyclePolicy",
    "OutOfInfrequentAccessPolicy",
    "PerformanceMode",
    "PosixUser",
    "ThroughputMode",
]

publication.publish()

def _typecheckingstub__a7d29db03188d21de563fa9ac94c4de056afa5ee45616d3e16e4b53de731bedd(
    *,
    access_point_arn: typing.Optional[builtins.str] = None,
    access_point_id: typing.Optional[builtins.str] = None,
    file_system: typing.Optional[IFileSystem] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__913ac22cf5c450fc4c0b0a7b6d77a1e412a1276f6c512fbacf766f6ab3a7d900(
    *,
    create_acl: typing.Optional[typing.Union[Acl, typing.Dict[builtins.str, typing.Any]]] = None,
    path: typing.Optional[builtins.str] = None,
    posix_user: typing.Optional[typing.Union[PosixUser, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32b9cfe4790278ebfef38060a79ab8e87662b5508943b46c7da6a219e5bc224e(
    *,
    create_acl: typing.Optional[typing.Union[Acl, typing.Dict[builtins.str, typing.Any]]] = None,
    path: typing.Optional[builtins.str] = None,
    posix_user: typing.Optional[typing.Union[PosixUser, typing.Dict[builtins.str, typing.Any]]] = None,
    file_system: IFileSystem,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f439deeada51bd0f31384ee4b4e958560a0a30822d3f26655f3a4b6a2568825(
    *,
    owner_gid: builtins.str,
    owner_uid: builtins.str,
    permissions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee6cf8e32e236f5b64c41d34d8956a146a19df0d9467273bec84f3053dc68070(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    file_system_id: builtins.str,
    access_point_tags: typing.Optional[typing.Sequence[typing.Union[CfnAccessPoint.AccessPointTagProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    client_token: typing.Optional[builtins.str] = None,
    posix_user: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAccessPoint.PosixUserProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    root_directory: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAccessPoint.RootDirectoryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca8bc4bd98606c2925e8e3beaf6899315a3a8aa05fe42a495c106412587debb7(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17e606a40f63a3efd1580567556b9224350cfb37bd36418259a5a97278069b76(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9aea834bdfbaebbad27efcd560e0cd5498ef3d5969d70369e72304aed575791(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aeb74855ac1106765931a5c783dbbf7f4179c6aa7d804023e0d75ac4601576b8(
    value: typing.Optional[typing.List[CfnAccessPoint.AccessPointTagProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__052a7200703646606a8831b74c4f5511cf71ee496fd407ed4059efc71782703e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cc245c2e53318bdc7d3164c462d6e8a52bf82fb7fe49247d2231ef329a53d87(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAccessPoint.PosixUserProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9667e2e350935a923b952abf9558fa66f4e1917b4233a4c26c0b65c8fd475e03(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAccessPoint.RootDirectoryProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18158f047ae4eb17326b1111683835556cf447939c66247854d140d2e078ab7b(
    *,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d74896f895974aeb78b39425593b263e2cca8c26b3d717b7ab981d784a7b9593(
    *,
    owner_gid: builtins.str,
    owner_uid: builtins.str,
    permissions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__501010539c7a611efa4b96840cdd89ac2086e0864afcb2855144c64fa71ab81c(
    *,
    gid: builtins.str,
    uid: builtins.str,
    secondary_gids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89b051df2a59c0884b5df1f891e75e8c5eecc226e4e3c37de3b47e49fc555dde(
    *,
    creation_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAccessPoint.CreationInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d9e6a6ec2a31d2d52416a71ce47e5ce1ad556ab26693686a787d2d7d21231d6(
    *,
    file_system_id: builtins.str,
    access_point_tags: typing.Optional[typing.Sequence[typing.Union[CfnAccessPoint.AccessPointTagProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    client_token: typing.Optional[builtins.str] = None,
    posix_user: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAccessPoint.PosixUserProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    root_directory: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAccessPoint.RootDirectoryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc457ee31ba660f40c549433977317b66ec9b461edc7a3afd3a157dcf7b8d48f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    availability_zone_name: typing.Optional[builtins.str] = None,
    backup_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFileSystem.BackupPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    bypass_policy_lockout_safety_check: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    encrypted: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    file_system_policy: typing.Any = None,
    file_system_tags: typing.Optional[typing.Sequence[typing.Union[CfnFileSystem.ElasticFileSystemTagProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    lifecycle_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFileSystem.LifecyclePolicyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    performance_mode: typing.Optional[builtins.str] = None,
    provisioned_throughput_in_mibps: typing.Optional[jsii.Number] = None,
    throughput_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4de45f38231d265020ffa3517bb2f41c6c7f64bc0414e943cf094f6436b824df(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64147597fb4c53ed2d67a6b0ef31707f2352f072a9c53f4fe39bc738512a4681(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bcd28f23c44d69b6a8f6fd61de5866f3fdb618cec9e47e4a49ed73986bdd849(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53fc5b9ed624a6fc84a03901041ea70dcde091bbcc6330be8fa5cf3fdf8c38b9(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFileSystem.BackupPolicyProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbd68d0f7f29b58d297e40085872ecac516d0817c15d9490f68a92f7aa0b8ea5(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9501af5a47c0d34d9710df284e85c94248a9579987a05605e729328fa911ff46(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__666e3c63493f31759a99ed7071553b2e9c97fd2b8a0c9b681208a654ad356c9a(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d84f46b1475d1cae884e8108f8439bdc99a546d9a8b21f2a8f1f4417cadc3585(
    value: typing.Optional[typing.List[CfnFileSystem.ElasticFileSystemTagProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a55210d3081fdfc59eb5c327bf8219f72804cd3b9d3e4b881f3edb7c67b5f3eb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd864e190d9a9b64a7046d9259a257368e4b66a44f4da384a9b88751c2a5271d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFileSystem.LifecyclePolicyProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__840c02c07752d49064a9e001bb6d5e27747e9a3c922771a75a094ace12f9fcc4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc4b244b6d015f638041856e6a5998aa7289240b34d904419c12431ce5f68b4e(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c5e0603f09328aca127a79f4af8caf4140cb862bf23ebe0cbe2e1e4c05dc8b8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c002a7547dd1af97cb52ea97bde78ee445e9676e5214ccc0edc9f10622d992a(
    *,
    status: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__786d6bbf33204cdfd92e62176c97bd5739bc95bda3441156be931c7335e637b7(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5fbc3e227009fdec1c9845be8c439793816fbd90d94dd67c54610c9832a0e99(
    *,
    transition_to_ia: typing.Optional[builtins.str] = None,
    transition_to_primary_storage_class: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__925156e2041b66f4aaa35cff9ceb098b90fd9cbb2027eb0431f56b2aa0c4aa89(
    *,
    availability_zone_name: typing.Optional[builtins.str] = None,
    backup_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFileSystem.BackupPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    bypass_policy_lockout_safety_check: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    encrypted: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    file_system_policy: typing.Any = None,
    file_system_tags: typing.Optional[typing.Sequence[typing.Union[CfnFileSystem.ElasticFileSystemTagProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    lifecycle_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFileSystem.LifecyclePolicyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    performance_mode: typing.Optional[builtins.str] = None,
    provisioned_throughput_in_mibps: typing.Optional[jsii.Number] = None,
    throughput_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53e47daec02e70bf8a73cac8e0366ac0f8a6af5ccf7598cf37952afe954d30bd(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    file_system_id: builtins.str,
    security_groups: typing.Sequence[builtins.str],
    subnet_id: builtins.str,
    ip_address: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb6e3b45bc9899160915641ff41c877062b796ef4defc0cec595a2913b545b0e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a6f002228f19658915474a99c7342ed28bb87dd419575b819f330121028b1d4(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c545a16b175530231985303ae48e8a4172cb3481a6b860def4e97a508f1c9e96(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__066c884c347c67446131a6b113dd92657eeddbf024cb39e3a188a1b06305d1c1(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25e2f5c1fe6c4bf78d2c5698cccb1fc3bb199eff31e3534fa6957dabf3467bcc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__804f6c8cadefc6e3bd989db6da64591d147d67de340d096244f68a21842bb5ab(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2ad126af1a9797276c238562f8185eb06a56da00a9b12a35504f9d72fbdc711(
    *,
    file_system_id: builtins.str,
    security_groups: typing.Sequence[builtins.str],
    subnet_id: builtins.str,
    ip_address: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7f9028e19d4f85ea9a53bb13e46bb5ac917443add6e7ec5e117fdc6136100b7(
    *,
    security_group: _ISecurityGroup_acf8a799,
    file_system_arn: typing.Optional[builtins.str] = None,
    file_system_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a11d59607a7c01a190b2b0587733658cfcb8eddfb252f3c48abdc988b9f09cff(
    *,
    vpc: _IVpc_f30d5663,
    enable_automatic_backups: typing.Optional[builtins.bool] = None,
    encrypted: typing.Optional[builtins.bool] = None,
    file_system_name: typing.Optional[builtins.str] = None,
    file_system_policy: typing.Optional[_PolicyDocument_3ac34393] = None,
    kms_key: typing.Optional[_IKey_5f11635f] = None,
    lifecycle_policy: typing.Optional[LifecyclePolicy] = None,
    out_of_infrequent_access_policy: typing.Optional[OutOfInfrequentAccessPolicy] = None,
    performance_mode: typing.Optional[PerformanceMode] = None,
    provisioned_throughput_per_second: typing.Optional[_Size_7b441c34] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    security_group: typing.Optional[_ISecurityGroup_acf8a799] = None,
    throughput_mode: typing.Optional[ThroughputMode] = None,
    vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d30690bfc35cb7c7060f6f609a976e22081bcba7be3b93da3b5b3a122eae8ece(
    grantee: _IGrantable_71c4f5de,
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c952f8c1704201f25c4d7df8b8a5c994569b8513be332681526a695abb83999b(
    *,
    gid: builtins.str,
    uid: builtins.str,
    secondary_gids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4cd5acd3aac2348517085a4188b85a5e2329da4dc443644482b9153e1014bfa(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    file_system: IFileSystem,
    create_acl: typing.Optional[typing.Union[Acl, typing.Dict[builtins.str, typing.Any]]] = None,
    path: typing.Optional[builtins.str] = None,
    posix_user: typing.Optional[typing.Union[PosixUser, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0959a679ec1620c39a9d0f9763692323c37cf7d3425d339a42722079da77067(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    access_point_arn: typing.Optional[builtins.str] = None,
    access_point_id: typing.Optional[builtins.str] = None,
    file_system: typing.Optional[IFileSystem] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d38e8f8212fb31c6248399b59a7a6bc5264d8d91253af77c2da7346b497f98a4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    access_point_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe7547e76a3f3502ef6c67d1cc851b25d13fe1b4b980d3bccee8eae2ff469690(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    vpc: _IVpc_f30d5663,
    enable_automatic_backups: typing.Optional[builtins.bool] = None,
    encrypted: typing.Optional[builtins.bool] = None,
    file_system_name: typing.Optional[builtins.str] = None,
    file_system_policy: typing.Optional[_PolicyDocument_3ac34393] = None,
    kms_key: typing.Optional[_IKey_5f11635f] = None,
    lifecycle_policy: typing.Optional[LifecyclePolicy] = None,
    out_of_infrequent_access_policy: typing.Optional[OutOfInfrequentAccessPolicy] = None,
    performance_mode: typing.Optional[PerformanceMode] = None,
    provisioned_throughput_per_second: typing.Optional[_Size_7b441c34] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    security_group: typing.Optional[_ISecurityGroup_acf8a799] = None,
    throughput_mode: typing.Optional[ThroughputMode] = None,
    vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dece37ce89e2cfb5f78f1232aff0c1114df92cbaea2ee4e9ea83cdad9812a448(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    security_group: _ISecurityGroup_acf8a799,
    file_system_arn: typing.Optional[builtins.str] = None,
    file_system_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ae17f92be1f854e9add049e3ad7507b46fbd97b0ceecc5921b74cffabc0fd7f(
    id: builtins.str,
    *,
    create_acl: typing.Optional[typing.Union[Acl, typing.Dict[builtins.str, typing.Any]]] = None,
    path: typing.Optional[builtins.str] = None,
    posix_user: typing.Optional[typing.Union[PosixUser, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1eff11f92ecb28f1cedf7f1f5bd707e2f23777bb0f90efb50e5454827f766dd7(
    statement: _PolicyStatement_0fe33853,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d469ca5d09698c2cd0c0b2ce1f4112950cbc13abe1c176ec39092c058940a48(
    grantee: _IGrantable_71c4f5de,
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
