'''
# AWS::RedshiftServerless Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_redshiftserverless as redshiftserverless
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for RedshiftServerless construct libraries](https://constructs.dev/search?q=redshiftserverless)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::RedshiftServerless resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_RedshiftServerless.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::RedshiftServerless](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_RedshiftServerless.html).

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
class CfnNamespace(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_redshiftserverless.CfnNamespace",
):
    '''A collection of database objects and users.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_redshiftserverless as redshiftserverless
        
        cfn_namespace = redshiftserverless.CfnNamespace(self, "MyCfnNamespace",
            namespace_name="namespaceName",
        
            # the properties below are optional
            admin_username="adminUsername",
            admin_user_password="adminUserPassword",
            db_name="dbName",
            default_iam_role_arn="defaultIamRoleArn",
            final_snapshot_name="finalSnapshotName",
            final_snapshot_retention_period=123,
            iam_roles=["iamRoles"],
            kms_key_id="kmsKeyId",
            log_exports=["logExports"],
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
        namespace_name: builtins.str,
        admin_username: typing.Optional[builtins.str] = None,
        admin_user_password: typing.Optional[builtins.str] = None,
        db_name: typing.Optional[builtins.str] = None,
        default_iam_role_arn: typing.Optional[builtins.str] = None,
        final_snapshot_name: typing.Optional[builtins.str] = None,
        final_snapshot_retention_period: typing.Optional[jsii.Number] = None,
        iam_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        log_exports: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param namespace_name: The name of the namespace. Must be between 3-64 alphanumeric characters in lowercase, and it cannot be a reserved word. A list of reserved words can be found in `Reserved Words <https://docs.aws.amazon.com//redshift/latest/dg/r_pg_keywords.html>`_ in the Amazon Redshift Database Developer Guide.
        :param admin_username: The username of the administrator for the primary database created in the namespace.
        :param admin_user_password: The password of the administrator for the primary database created in the namespace.
        :param db_name: The name of the primary database created in the namespace.
        :param default_iam_role_arn: The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace.
        :param final_snapshot_name: The name of the snapshot to be created before the namespace is deleted.
        :param final_snapshot_retention_period: How long to retain the final snapshot.
        :param iam_roles: A list of IAM roles to associate with the namespace.
        :param kms_key_id: The ID of the AWS Key Management Service key used to encrypt your data.
        :param log_exports: The types of logs the namespace can export. Available export types are ``userlog`` , ``connectionlog`` , and ``useractivitylog`` .
        :param tags: The map of the key-value pairs used to tag the namespace.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e517382d9f55a518348d7299a7ce6c5be66bae2202f4223bf3c891a7dd669682)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnNamespaceProps(
            namespace_name=namespace_name,
            admin_username=admin_username,
            admin_user_password=admin_user_password,
            db_name=db_name,
            default_iam_role_arn=default_iam_role_arn,
            final_snapshot_name=final_snapshot_name,
            final_snapshot_retention_period=final_snapshot_retention_period,
            iam_roles=iam_roles,
            kms_key_id=kms_key_id,
            log_exports=log_exports,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2df0038e9ec3a1b73ddb07c3b803a742204804b2ccd2aab0d7df9fbb8521f86)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d877d23369c8f10ea1630884d7e7c879ab22a49fc05986834857785664c640ca)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrNamespace")
    def attr_namespace(self) -> _IResolvable_da3f097b:
        '''The collection of computing resources from which an endpoint is created.

        :cloudformationAttribute: Namespace
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrNamespace"))

    @builtins.property
    @jsii.member(jsii_name="attrNamespaceAdminUsername")
    def attr_namespace_admin_username(self) -> builtins.str:
        '''The username of the administrator for the first database created in the namespace.

        :cloudformationAttribute: Namespace.AdminUsername
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNamespaceAdminUsername"))

    @builtins.property
    @jsii.member(jsii_name="attrNamespaceCreationDate")
    def attr_namespace_creation_date(self) -> builtins.str:
        '''The date of when the namespace was created.

        :cloudformationAttribute: Namespace.CreationDate
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNamespaceCreationDate"))

    @builtins.property
    @jsii.member(jsii_name="attrNamespaceDbName")
    def attr_namespace_db_name(self) -> builtins.str:
        '''The name of the first database created in the namespace.

        :cloudformationAttribute: Namespace.DbName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNamespaceDbName"))

    @builtins.property
    @jsii.member(jsii_name="attrNamespaceDefaultIamRoleArn")
    def attr_namespace_default_iam_role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace.

        :cloudformationAttribute: Namespace.DefaultIamRoleArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNamespaceDefaultIamRoleArn"))

    @builtins.property
    @jsii.member(jsii_name="attrNamespaceIamRoles")
    def attr_namespace_iam_roles(self) -> typing.List[builtins.str]:
        '''A list of IAM roles to associate with the namespace.

        :cloudformationAttribute: Namespace.IamRoles
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrNamespaceIamRoles"))

    @builtins.property
    @jsii.member(jsii_name="attrNamespaceKmsKeyId")
    def attr_namespace_kms_key_id(self) -> builtins.str:
        '''The ID of the AWS Key Management Service key used to encrypt your data.

        :cloudformationAttribute: Namespace.KmsKeyId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNamespaceKmsKeyId"))

    @builtins.property
    @jsii.member(jsii_name="attrNamespaceLogExports")
    def attr_namespace_log_exports(self) -> typing.List[builtins.str]:
        '''The types of logs the namespace can export.

        Available export types are ``User log`` , ``Connection log`` , and ``User activity log`` .

        :cloudformationAttribute: Namespace.LogExports
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrNamespaceLogExports"))

    @builtins.property
    @jsii.member(jsii_name="attrNamespaceNamespaceArn")
    def attr_namespace_namespace_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) associated with a namespace.

        :cloudformationAttribute: Namespace.NamespaceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNamespaceNamespaceArn"))

    @builtins.property
    @jsii.member(jsii_name="attrNamespaceNamespaceId")
    def attr_namespace_namespace_id(self) -> builtins.str:
        '''The unique identifier of a namespace.

        :cloudformationAttribute: Namespace.NamespaceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNamespaceNamespaceId"))

    @builtins.property
    @jsii.member(jsii_name="attrNamespaceNamespaceName")
    def attr_namespace_namespace_name(self) -> builtins.str:
        '''The name of the namespace.

        Must be between 3-64 alphanumeric characters in lowercase, and it cannot be a reserved word. A list of reserved words can be found in `Reserved Words <https://docs.aws.amazon.com//redshift/latest/dg/r_pg_keywords.html>`_ in the Amazon Redshift Database Developer Guide.

        :cloudformationAttribute: Namespace.NamespaceName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNamespaceNamespaceName"))

    @builtins.property
    @jsii.member(jsii_name="attrNamespaceStatus")
    def attr_namespace_status(self) -> builtins.str:
        '''The status of the namespace.

        :cloudformationAttribute: Namespace.Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNamespaceStatus"))

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
    @jsii.member(jsii_name="namespaceName")
    def namespace_name(self) -> builtins.str:
        '''The name of the namespace.'''
        return typing.cast(builtins.str, jsii.get(self, "namespaceName"))

    @namespace_name.setter
    def namespace_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fe15d8ff16345a3e36d8c090d48eea89c8cd559ac4218facdfd95b67e49140c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespaceName", value)

    @builtins.property
    @jsii.member(jsii_name="adminUsername")
    def admin_username(self) -> typing.Optional[builtins.str]:
        '''The username of the administrator for the primary database created in the namespace.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminUsername"))

    @admin_username.setter
    def admin_username(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e95b6bb908e50903825c7cbfdb447ab3aceb27b3a93be8aa57fe8923f432493)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminUsername", value)

    @builtins.property
    @jsii.member(jsii_name="adminUserPassword")
    def admin_user_password(self) -> typing.Optional[builtins.str]:
        '''The password of the administrator for the primary database created in the namespace.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminUserPassword"))

    @admin_user_password.setter
    def admin_user_password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b50aae57ce0c503e5aed7528570d1ab32511eacbfe2dcac51d410dd4bb1991ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminUserPassword", value)

    @builtins.property
    @jsii.member(jsii_name="dbName")
    def db_name(self) -> typing.Optional[builtins.str]:
        '''The name of the primary database created in the namespace.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbName"))

    @db_name.setter
    def db_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8947213c316180fbcdb1956ca9a54febcb6a874110724c51c1db8705f8186d0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbName", value)

    @builtins.property
    @jsii.member(jsii_name="defaultIamRoleArn")
    def default_iam_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultIamRoleArn"))

    @default_iam_role_arn.setter
    def default_iam_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a992711b01695733a564873ba440d2806a3692e807afc16701507c986201edd9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultIamRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="finalSnapshotName")
    def final_snapshot_name(self) -> typing.Optional[builtins.str]:
        '''The name of the snapshot to be created before the namespace is deleted.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "finalSnapshotName"))

    @final_snapshot_name.setter
    def final_snapshot_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de06e0fc02a451c4e9e47c3f839f6289f8f8e9d4dbc0867eb263e09672990c7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "finalSnapshotName", value)

    @builtins.property
    @jsii.member(jsii_name="finalSnapshotRetentionPeriod")
    def final_snapshot_retention_period(self) -> typing.Optional[jsii.Number]:
        '''How long to retain the final snapshot.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "finalSnapshotRetentionPeriod"))

    @final_snapshot_retention_period.setter
    def final_snapshot_retention_period(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ae56ba94c395d18dd103368c4ca09a505763b47324b4820065925d61c84adaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "finalSnapshotRetentionPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="iamRoles")
    def iam_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of IAM roles to associate with the namespace.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "iamRoles"))

    @iam_roles.setter
    def iam_roles(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9111ebc5ef107cd5d00c7617518664163ccd1b1d99fb0ec53548dd04073b0e77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamRoles", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the AWS Key Management Service key used to encrypt your data.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bc1c937667ef895444beeaaacfd8af398b90be0a42f50184325fdb96072b5ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="logExports")
    def log_exports(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The types of logs the namespace can export.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "logExports"))

    @log_exports.setter
    def log_exports(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1526e0cedff0515a6bb96570f366670e82fb4d0cc597e2d7a8b0a091f0420dea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logExports", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The map of the key-value pairs used to tag the namespace.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e2da7bae4bc39426d05dc2f307e08d5246472ad626b032ef4c2ea7b7d1bd33f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_redshiftserverless.CfnNamespace.NamespaceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "admin_username": "adminUsername",
            "creation_date": "creationDate",
            "db_name": "dbName",
            "default_iam_role_arn": "defaultIamRoleArn",
            "iam_roles": "iamRoles",
            "kms_key_id": "kmsKeyId",
            "log_exports": "logExports",
            "namespace_arn": "namespaceArn",
            "namespace_id": "namespaceId",
            "namespace_name": "namespaceName",
            "status": "status",
        },
    )
    class NamespaceProperty:
        def __init__(
            self,
            *,
            admin_username: typing.Optional[builtins.str] = None,
            creation_date: typing.Optional[builtins.str] = None,
            db_name: typing.Optional[builtins.str] = None,
            default_iam_role_arn: typing.Optional[builtins.str] = None,
            iam_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
            kms_key_id: typing.Optional[builtins.str] = None,
            log_exports: typing.Optional[typing.Sequence[builtins.str]] = None,
            namespace_arn: typing.Optional[builtins.str] = None,
            namespace_id: typing.Optional[builtins.str] = None,
            namespace_name: typing.Optional[builtins.str] = None,
            status: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A collection of database objects and users.

            :param admin_username: The username of the administrator for the first database created in the namespace.
            :param creation_date: The date of when the namespace was created.
            :param db_name: The name of the first database created in the namespace.
            :param default_iam_role_arn: The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace.
            :param iam_roles: A list of IAM roles to associate with the namespace.
            :param kms_key_id: The ID of the AWS Key Management Service key used to encrypt your data.
            :param log_exports: The types of logs the namespace can export. Available export types are User log, Connection log, and User activity log.
            :param namespace_arn: The Amazon Resource Name (ARN) associated with a namespace.
            :param namespace_id: The unique identifier of a namespace.
            :param namespace_name: The name of the namespace. Must be between 3-64 alphanumeric characters in lowercase, and it cannot be a reserved word. A list of reserved words can be found in `Reserved Words <https://docs.aws.amazon.com//redshift/latest/dg/r_pg_keywords.html>`_ in the Amazon Redshift Database Developer Guide.
            :param status: The status of the namespace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_redshiftserverless as redshiftserverless
                
                namespace_property = redshiftserverless.CfnNamespace.NamespaceProperty(
                    admin_username="adminUsername",
                    creation_date="creationDate",
                    db_name="dbName",
                    default_iam_role_arn="defaultIamRoleArn",
                    iam_roles=["iamRoles"],
                    kms_key_id="kmsKeyId",
                    log_exports=["logExports"],
                    namespace_arn="namespaceArn",
                    namespace_id="namespaceId",
                    namespace_name="namespaceName",
                    status="status"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6bcbea65acb7d2a3cef7455cfbb52c832d3da01cd5e02df21a06cdb2b4822e35)
                check_type(argname="argument admin_username", value=admin_username, expected_type=type_hints["admin_username"])
                check_type(argname="argument creation_date", value=creation_date, expected_type=type_hints["creation_date"])
                check_type(argname="argument db_name", value=db_name, expected_type=type_hints["db_name"])
                check_type(argname="argument default_iam_role_arn", value=default_iam_role_arn, expected_type=type_hints["default_iam_role_arn"])
                check_type(argname="argument iam_roles", value=iam_roles, expected_type=type_hints["iam_roles"])
                check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
                check_type(argname="argument log_exports", value=log_exports, expected_type=type_hints["log_exports"])
                check_type(argname="argument namespace_arn", value=namespace_arn, expected_type=type_hints["namespace_arn"])
                check_type(argname="argument namespace_id", value=namespace_id, expected_type=type_hints["namespace_id"])
                check_type(argname="argument namespace_name", value=namespace_name, expected_type=type_hints["namespace_name"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if admin_username is not None:
                self._values["admin_username"] = admin_username
            if creation_date is not None:
                self._values["creation_date"] = creation_date
            if db_name is not None:
                self._values["db_name"] = db_name
            if default_iam_role_arn is not None:
                self._values["default_iam_role_arn"] = default_iam_role_arn
            if iam_roles is not None:
                self._values["iam_roles"] = iam_roles
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id
            if log_exports is not None:
                self._values["log_exports"] = log_exports
            if namespace_arn is not None:
                self._values["namespace_arn"] = namespace_arn
            if namespace_id is not None:
                self._values["namespace_id"] = namespace_id
            if namespace_name is not None:
                self._values["namespace_name"] = namespace_name
            if status is not None:
                self._values["status"] = status

        @builtins.property
        def admin_username(self) -> typing.Optional[builtins.str]:
            '''The username of the administrator for the first database created in the namespace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-adminusername
            '''
            result = self._values.get("admin_username")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def creation_date(self) -> typing.Optional[builtins.str]:
            '''The date of when the namespace was created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-creationdate
            '''
            result = self._values.get("creation_date")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def db_name(self) -> typing.Optional[builtins.str]:
            '''The name of the first database created in the namespace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-dbname
            '''
            result = self._values.get("db_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def default_iam_role_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-defaultiamrolearn
            '''
            result = self._values.get("default_iam_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def iam_roles(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of IAM roles to associate with the namespace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-iamroles
            '''
            result = self._values.get("iam_roles")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the AWS Key Management Service key used to encrypt your data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def log_exports(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The types of logs the namespace can export.

            Available export types are User log, Connection log, and User activity log.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-logexports
            '''
            result = self._values.get("log_exports")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def namespace_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) associated with a namespace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-namespacearn
            '''
            result = self._values.get("namespace_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def namespace_id(self) -> typing.Optional[builtins.str]:
            '''The unique identifier of a namespace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-namespaceid
            '''
            result = self._values.get("namespace_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def namespace_name(self) -> typing.Optional[builtins.str]:
            '''The name of the namespace.

            Must be between 3-64 alphanumeric characters in lowercase, and it cannot be a reserved word. A list of reserved words can be found in `Reserved Words <https://docs.aws.amazon.com//redshift/latest/dg/r_pg_keywords.html>`_ in the Amazon Redshift Database Developer Guide.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-namespacename
            '''
            result = self._values.get("namespace_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''The status of the namespace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NamespaceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_redshiftserverless.CfnNamespaceProps",
    jsii_struct_bases=[],
    name_mapping={
        "namespace_name": "namespaceName",
        "admin_username": "adminUsername",
        "admin_user_password": "adminUserPassword",
        "db_name": "dbName",
        "default_iam_role_arn": "defaultIamRoleArn",
        "final_snapshot_name": "finalSnapshotName",
        "final_snapshot_retention_period": "finalSnapshotRetentionPeriod",
        "iam_roles": "iamRoles",
        "kms_key_id": "kmsKeyId",
        "log_exports": "logExports",
        "tags": "tags",
    },
)
class CfnNamespaceProps:
    def __init__(
        self,
        *,
        namespace_name: builtins.str,
        admin_username: typing.Optional[builtins.str] = None,
        admin_user_password: typing.Optional[builtins.str] = None,
        db_name: typing.Optional[builtins.str] = None,
        default_iam_role_arn: typing.Optional[builtins.str] = None,
        final_snapshot_name: typing.Optional[builtins.str] = None,
        final_snapshot_retention_period: typing.Optional[jsii.Number] = None,
        iam_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        log_exports: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnNamespace``.

        :param namespace_name: The name of the namespace. Must be between 3-64 alphanumeric characters in lowercase, and it cannot be a reserved word. A list of reserved words can be found in `Reserved Words <https://docs.aws.amazon.com//redshift/latest/dg/r_pg_keywords.html>`_ in the Amazon Redshift Database Developer Guide.
        :param admin_username: The username of the administrator for the primary database created in the namespace.
        :param admin_user_password: The password of the administrator for the primary database created in the namespace.
        :param db_name: The name of the primary database created in the namespace.
        :param default_iam_role_arn: The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace.
        :param final_snapshot_name: The name of the snapshot to be created before the namespace is deleted.
        :param final_snapshot_retention_period: How long to retain the final snapshot.
        :param iam_roles: A list of IAM roles to associate with the namespace.
        :param kms_key_id: The ID of the AWS Key Management Service key used to encrypt your data.
        :param log_exports: The types of logs the namespace can export. Available export types are ``userlog`` , ``connectionlog`` , and ``useractivitylog`` .
        :param tags: The map of the key-value pairs used to tag the namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_redshiftserverless as redshiftserverless
            
            cfn_namespace_props = redshiftserverless.CfnNamespaceProps(
                namespace_name="namespaceName",
            
                # the properties below are optional
                admin_username="adminUsername",
                admin_user_password="adminUserPassword",
                db_name="dbName",
                default_iam_role_arn="defaultIamRoleArn",
                final_snapshot_name="finalSnapshotName",
                final_snapshot_retention_period=123,
                iam_roles=["iamRoles"],
                kms_key_id="kmsKeyId",
                log_exports=["logExports"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5964a5da555f62a5d9615a6e07cd0d1128cdf904fd5aa3c5be9fd5e53dc30bd9)
            check_type(argname="argument namespace_name", value=namespace_name, expected_type=type_hints["namespace_name"])
            check_type(argname="argument admin_username", value=admin_username, expected_type=type_hints["admin_username"])
            check_type(argname="argument admin_user_password", value=admin_user_password, expected_type=type_hints["admin_user_password"])
            check_type(argname="argument db_name", value=db_name, expected_type=type_hints["db_name"])
            check_type(argname="argument default_iam_role_arn", value=default_iam_role_arn, expected_type=type_hints["default_iam_role_arn"])
            check_type(argname="argument final_snapshot_name", value=final_snapshot_name, expected_type=type_hints["final_snapshot_name"])
            check_type(argname="argument final_snapshot_retention_period", value=final_snapshot_retention_period, expected_type=type_hints["final_snapshot_retention_period"])
            check_type(argname="argument iam_roles", value=iam_roles, expected_type=type_hints["iam_roles"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument log_exports", value=log_exports, expected_type=type_hints["log_exports"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "namespace_name": namespace_name,
        }
        if admin_username is not None:
            self._values["admin_username"] = admin_username
        if admin_user_password is not None:
            self._values["admin_user_password"] = admin_user_password
        if db_name is not None:
            self._values["db_name"] = db_name
        if default_iam_role_arn is not None:
            self._values["default_iam_role_arn"] = default_iam_role_arn
        if final_snapshot_name is not None:
            self._values["final_snapshot_name"] = final_snapshot_name
        if final_snapshot_retention_period is not None:
            self._values["final_snapshot_retention_period"] = final_snapshot_retention_period
        if iam_roles is not None:
            self._values["iam_roles"] = iam_roles
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if log_exports is not None:
            self._values["log_exports"] = log_exports
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def namespace_name(self) -> builtins.str:
        '''The name of the namespace.

        Must be between 3-64 alphanumeric characters in lowercase, and it cannot be a reserved word. A list of reserved words can be found in `Reserved Words <https://docs.aws.amazon.com//redshift/latest/dg/r_pg_keywords.html>`_ in the Amazon Redshift Database Developer Guide.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-namespacename
        '''
        result = self._values.get("namespace_name")
        assert result is not None, "Required property 'namespace_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def admin_username(self) -> typing.Optional[builtins.str]:
        '''The username of the administrator for the primary database created in the namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-adminusername
        '''
        result = self._values.get("admin_username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def admin_user_password(self) -> typing.Optional[builtins.str]:
        '''The password of the administrator for the primary database created in the namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-adminuserpassword
        '''
        result = self._values.get("admin_user_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def db_name(self) -> typing.Optional[builtins.str]:
        '''The name of the primary database created in the namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-dbname
        '''
        result = self._values.get("db_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_iam_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-defaultiamrolearn
        '''
        result = self._values.get("default_iam_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def final_snapshot_name(self) -> typing.Optional[builtins.str]:
        '''The name of the snapshot to be created before the namespace is deleted.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-finalsnapshotname
        '''
        result = self._values.get("final_snapshot_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def final_snapshot_retention_period(self) -> typing.Optional[jsii.Number]:
        '''How long to retain the final snapshot.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-finalsnapshotretentionperiod
        '''
        result = self._values.get("final_snapshot_retention_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def iam_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of IAM roles to associate with the namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-iamroles
        '''
        result = self._values.get("iam_roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the AWS Key Management Service key used to encrypt your data.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_exports(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The types of logs the namespace can export.

        Available export types are ``userlog`` , ``connectionlog`` , and ``useractivitylog`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-logexports
        '''
        result = self._values.get("log_exports")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The map of the key-value pairs used to tag the namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNamespaceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnWorkgroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_redshiftserverless.CfnWorkgroup",
):
    '''The collection of compute resources in Amazon Redshift Serverless.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_redshiftserverless as redshiftserverless
        
        cfn_workgroup = redshiftserverless.CfnWorkgroup(self, "MyCfnWorkgroup",
            workgroup_name="workgroupName",
        
            # the properties below are optional
            base_capacity=123,
            config_parameters=[redshiftserverless.CfnWorkgroup.ConfigParameterProperty(
                parameter_key="parameterKey",
                parameter_value="parameterValue"
            )],
            enhanced_vpc_routing=False,
            namespace_name="namespaceName",
            port=123,
            publicly_accessible=False,
            security_group_ids=["securityGroupIds"],
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
        workgroup_name: builtins.str,
        base_capacity: typing.Optional[jsii.Number] = None,
        config_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkgroup.ConfigParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        enhanced_vpc_routing: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        namespace_name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param workgroup_name: The name of the workgroup.
        :param base_capacity: The base compute capacity of the workgroup in Redshift Processing Units (RPUs).
        :param config_parameters: A list of parameters to set for finer control over a database. Available options are ``datestyle`` , ``enable_user_activity_logging`` , ``query_group`` , ``search_path`` , and ``max_query_execution_time`` .
        :param enhanced_vpc_routing: The value that specifies whether to enable enhanced virtual private cloud (VPC) routing, which forces Amazon Redshift Serverless to route traffic through your VPC. Default: - false
        :param namespace_name: The namespace the workgroup is associated with.
        :param port: The custom port to use when connecting to a workgroup. Valid port ranges are 5431-5455 and 8191-8215. The default is 5439.
        :param publicly_accessible: A value that specifies whether the workgroup can be accessible from a public network. Default: - false
        :param security_group_ids: A list of security group IDs to associate with the workgroup.
        :param subnet_ids: A list of subnet IDs the workgroup is associated with.
        :param tags: The map of the key-value pairs used to tag the workgroup.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61a1b6ebbdacc577619f4e17ddabdaa553ffe5fe072b72e14ddf7d9c3f7e1a04)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnWorkgroupProps(
            workgroup_name=workgroup_name,
            base_capacity=base_capacity,
            config_parameters=config_parameters,
            enhanced_vpc_routing=enhanced_vpc_routing,
            namespace_name=namespace_name,
            port=port,
            publicly_accessible=publicly_accessible,
            security_group_ids=security_group_ids,
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
            type_hints = typing.get_type_hints(_typecheckingstub__986feaaa3c97c38d5a5c4414a977741007338bd588a8ebc981d89e63b28c9c38)
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
            type_hints = typing.get_type_hints(_typecheckingstub__575b09c3449f3d47af302b94ec8c88b82387f8f428024e134c076d5600122345)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroup")
    def attr_workgroup(self) -> _IResolvable_da3f097b:
        '''Returns the ``Workgroup`` value.

        :cloudformationAttribute: Workgroup
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrWorkgroup"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroupBaseCapacity")
    def attr_workgroup_base_capacity(self) -> jsii.Number:
        '''The base data warehouse capacity of the workgroup in Redshift Processing Units (RPUs).

        :cloudformationAttribute: Workgroup.BaseCapacity
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrWorkgroupBaseCapacity"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroupConfigParameters")
    def attr_workgroup_config_parameters(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: Workgroup.ConfigParameters
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrWorkgroupConfigParameters"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroupCreationDate")
    def attr_workgroup_creation_date(self) -> builtins.str:
        '''The creation date of the workgroup.

        :cloudformationAttribute: Workgroup.CreationDate
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWorkgroupCreationDate"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroupEndpoint")
    def attr_workgroup_endpoint(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: Workgroup.Endpoint
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrWorkgroupEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroupEndpointAddress")
    def attr_workgroup_endpoint_address(self) -> builtins.str:
        '''The DNS address of the VPC endpoint.

        :cloudformationAttribute: Workgroup.Endpoint.Address
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWorkgroupEndpointAddress"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroupEndpointPort")
    def attr_workgroup_endpoint_port(self) -> jsii.Number:
        '''The custom port to use when connecting to a workgroup.

        Valid port ranges are 5431-5455 and 8191-8215. The default is 5439.

        :cloudformationAttribute: Workgroup.Endpoint.Port
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrWorkgroupEndpointPort"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroupEndpointVpcEndpoints")
    def attr_workgroup_endpoint_vpc_endpoints(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: Workgroup.Endpoint.VpcEndpoints
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrWorkgroupEndpointVpcEndpoints"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroupEnhancedVpcRouting")
    def attr_workgroup_enhanced_vpc_routing(self) -> _IResolvable_da3f097b:
        '''The value that specifies whether to enable enhanced virtual private cloud (VPC) routing, which forces Amazon Redshift Serverless to route traffic through your VPC.

        :cloudformationAttribute: Workgroup.EnhancedVpcRouting
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrWorkgroupEnhancedVpcRouting"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroupNamespaceName")
    def attr_workgroup_namespace_name(self) -> builtins.str:
        '''The namespace the workgroup is associated with.

        :cloudformationAttribute: Workgroup.NamespaceName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWorkgroupNamespaceName"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroupPubliclyAccessible")
    def attr_workgroup_publicly_accessible(self) -> _IResolvable_da3f097b:
        '''A value that specifies whether the workgroup can be accessible from a public network.

        :cloudformationAttribute: Workgroup.PubliclyAccessible
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrWorkgroupPubliclyAccessible"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroupSecurityGroupIds")
    def attr_workgroup_security_group_ids(self) -> typing.List[builtins.str]:
        '''An array of security group IDs to associate with the workgroup.

        :cloudformationAttribute: Workgroup.SecurityGroupIds
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrWorkgroupSecurityGroupIds"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroupStatus")
    def attr_workgroup_status(self) -> builtins.str:
        '''The status of the workgroup.

        :cloudformationAttribute: Workgroup.Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWorkgroupStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroupSubnetIds")
    def attr_workgroup_subnet_ids(self) -> typing.List[builtins.str]:
        '''An array of subnet IDs the workgroup is associated with.

        :cloudformationAttribute: Workgroup.SubnetIds
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrWorkgroupSubnetIds"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroupWorkgroupArn")
    def attr_workgroup_workgroup_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) that links to the workgroup.

        :cloudformationAttribute: Workgroup.WorkgroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWorkgroupWorkgroupArn"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroupWorkgroupId")
    def attr_workgroup_workgroup_id(self) -> builtins.str:
        '''The unique identifier of the workgroup.

        :cloudformationAttribute: Workgroup.WorkgroupId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWorkgroupWorkgroupId"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroupWorkgroupName")
    def attr_workgroup_workgroup_name(self) -> builtins.str:
        '''The name of the workgroup.

        :cloudformationAttribute: Workgroup.WorkgroupName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWorkgroupWorkgroupName"))

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
    @jsii.member(jsii_name="workgroupName")
    def workgroup_name(self) -> builtins.str:
        '''The name of the workgroup.'''
        return typing.cast(builtins.str, jsii.get(self, "workgroupName"))

    @workgroup_name.setter
    def workgroup_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44b001bba04c1f96a7169e528d056ccd8d9035fee30af63b1f339873bf7e3ea7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workgroupName", value)

    @builtins.property
    @jsii.member(jsii_name="baseCapacity")
    def base_capacity(self) -> typing.Optional[jsii.Number]:
        '''The base compute capacity of the workgroup in Redshift Processing Units (RPUs).'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "baseCapacity"))

    @base_capacity.setter
    def base_capacity(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d35b55423f49c0c42ee449a11852238ff7a68ae5e2e78f2da58bcb94c221a85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "baseCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="configParameters")
    def config_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkgroup.ConfigParameterProperty"]]]]:
        '''A list of parameters to set for finer control over a database.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkgroup.ConfigParameterProperty"]]]], jsii.get(self, "configParameters"))

    @config_parameters.setter
    def config_parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkgroup.ConfigParameterProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00339df2c3d04a43ab10d867748f8678b0423745badc0e14afa8bb128d473607)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configParameters", value)

    @builtins.property
    @jsii.member(jsii_name="enhancedVpcRouting")
    def enhanced_vpc_routing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''The value that specifies whether to enable enhanced virtual private cloud (VPC) routing, which forces Amazon Redshift Serverless to route traffic through your VPC.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enhancedVpcRouting"))

    @enhanced_vpc_routing.setter
    def enhanced_vpc_routing(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b06db2b227debd7cc917f51bf7c4c0bb700bca075b329af61a43f37521feba71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enhancedVpcRouting", value)

    @builtins.property
    @jsii.member(jsii_name="namespaceName")
    def namespace_name(self) -> typing.Optional[builtins.str]:
        '''The namespace the workgroup is associated with.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceName"))

    @namespace_name.setter
    def namespace_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a009fb86999f55de110193d15ea127b35ea379a1d840ddd42a0406b02f3a997a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespaceName", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> typing.Optional[jsii.Number]:
        '''The custom port to use when connecting to a workgroup.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "port"))

    @port.setter
    def port(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e3a61acfcbbe3b107c15ebd1c1248f3bd150ad58cf876908da7870de9fd6fde)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="publiclyAccessible")
    def publicly_accessible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A value that specifies whether the workgroup can be accessible from a public network.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "publiclyAccessible"))

    @publicly_accessible.setter
    def publicly_accessible(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__974542b0d8aa6c1847dd536dcf795ef2c4719aed798ea365b0767f6ad3234ca0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publiclyAccessible", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of security group IDs to associate with the workgroup.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2864d0fac41ac305963b5532a731665cbc0d93a810a41ea2d2fe98a5285e8aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of subnet IDs the workgroup is associated with.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67e139cef151f144f2bb04082850da469be0ab0515cff591edf9fc1e44df78a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The map of the key-value pairs used to tag the workgroup.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3104c5d5a81618ce7738aabf06bbd67fea6c82cd5abea01e1b03c71c5065efc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_redshiftserverless.CfnWorkgroup.ConfigParameterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "parameter_key": "parameterKey",
            "parameter_value": "parameterValue",
        },
    )
    class ConfigParameterProperty:
        def __init__(
            self,
            *,
            parameter_key: typing.Optional[builtins.str] = None,
            parameter_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A array of parameters to set for more control over a serverless database.

            :param parameter_key: The key of the parameter. The options are ``datestyle`` , ``enable_user_activity_logging`` , ``query_group`` , ``search_path`` , and ``max_query_execution_time`` .
            :param parameter_value: The value of the parameter to set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-configparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_redshiftserverless as redshiftserverless
                
                config_parameter_property = redshiftserverless.CfnWorkgroup.ConfigParameterProperty(
                    parameter_key="parameterKey",
                    parameter_value="parameterValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__322e3a40a90a7ebca9e3ef09024360dddede638badc33eeda64eccd556f3dc5f)
                check_type(argname="argument parameter_key", value=parameter_key, expected_type=type_hints["parameter_key"])
                check_type(argname="argument parameter_value", value=parameter_value, expected_type=type_hints["parameter_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if parameter_key is not None:
                self._values["parameter_key"] = parameter_key
            if parameter_value is not None:
                self._values["parameter_value"] = parameter_value

        @builtins.property
        def parameter_key(self) -> typing.Optional[builtins.str]:
            '''The key of the parameter.

            The options are ``datestyle`` , ``enable_user_activity_logging`` , ``query_group`` , ``search_path`` , and ``max_query_execution_time`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-configparameter.html#cfn-redshiftserverless-workgroup-configparameter-parameterkey
            '''
            result = self._values.get("parameter_key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parameter_value(self) -> typing.Optional[builtins.str]:
            '''The value of the parameter to set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-configparameter.html#cfn-redshiftserverless-workgroup-configparameter-parametervalue
            '''
            result = self._values.get("parameter_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_redshiftserverless.CfnWorkgroup.EndpointProperty",
        jsii_struct_bases=[],
        name_mapping={
            "address": "address",
            "port": "port",
            "vpc_endpoints": "vpcEndpoints",
        },
    )
    class EndpointProperty:
        def __init__(
            self,
            *,
            address: typing.Optional[builtins.str] = None,
            port: typing.Optional[jsii.Number] = None,
            vpc_endpoints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkgroup.VpcEndpointProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The VPC endpoint object.

            :param address: The DNS address of the VPC endpoint.
            :param port: The port that Amazon Redshift Serverless listens on.
            :param vpc_endpoints: An array of ``VpcEndpoint`` objects.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-endpoint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_redshiftserverless as redshiftserverless
                
                endpoint_property = redshiftserverless.CfnWorkgroup.EndpointProperty(
                    address="address",
                    port=123,
                    vpc_endpoints=[redshiftserverless.CfnWorkgroup.VpcEndpointProperty(
                        network_interfaces=[redshiftserverless.CfnWorkgroup.NetworkInterfaceProperty(
                            availability_zone="availabilityZone",
                            network_interface_id="networkInterfaceId",
                            private_ip_address="privateIpAddress",
                            subnet_id="subnetId"
                        )],
                        vpc_endpoint_id="vpcEndpointId",
                        vpc_id="vpcId"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1064dbbc6e1afc7fbd36b9ac721b89fc24382d0930f8f41542644b48bc6c07bf)
                check_type(argname="argument address", value=address, expected_type=type_hints["address"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
                check_type(argname="argument vpc_endpoints", value=vpc_endpoints, expected_type=type_hints["vpc_endpoints"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if address is not None:
                self._values["address"] = address
            if port is not None:
                self._values["port"] = port
            if vpc_endpoints is not None:
                self._values["vpc_endpoints"] = vpc_endpoints

        @builtins.property
        def address(self) -> typing.Optional[builtins.str]:
            '''The DNS address of the VPC endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-endpoint.html#cfn-redshiftserverless-workgroup-endpoint-address
            '''
            result = self._values.get("address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def port(self) -> typing.Optional[jsii.Number]:
            '''The port that Amazon Redshift Serverless listens on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-endpoint.html#cfn-redshiftserverless-workgroup-endpoint-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def vpc_endpoints(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkgroup.VpcEndpointProperty"]]]]:
            '''An array of ``VpcEndpoint`` objects.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-endpoint.html#cfn-redshiftserverless-workgroup-endpoint-vpcendpoints
            '''
            result = self._values.get("vpc_endpoints")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkgroup.VpcEndpointProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EndpointProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_redshiftserverless.CfnWorkgroup.NetworkInterfaceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "availability_zone": "availabilityZone",
            "network_interface_id": "networkInterfaceId",
            "private_ip_address": "privateIpAddress",
            "subnet_id": "subnetId",
        },
    )
    class NetworkInterfaceProperty:
        def __init__(
            self,
            *,
            availability_zone: typing.Optional[builtins.str] = None,
            network_interface_id: typing.Optional[builtins.str] = None,
            private_ip_address: typing.Optional[builtins.str] = None,
            subnet_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains information about a network interface in an Amazon Redshift Serverless managed VPC endpoint.

            :param availability_zone: The availability Zone.
            :param network_interface_id: The unique identifier of the network interface.
            :param private_ip_address: The IPv4 address of the network interface within the subnet.
            :param subnet_id: The unique identifier of the subnet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-networkinterface.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_redshiftserverless as redshiftserverless
                
                network_interface_property = redshiftserverless.CfnWorkgroup.NetworkInterfaceProperty(
                    availability_zone="availabilityZone",
                    network_interface_id="networkInterfaceId",
                    private_ip_address="privateIpAddress",
                    subnet_id="subnetId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c27a8032aaa250691e1e68b2e75ce65c47142ac6b83ad22f01b09ec293f841b8)
                check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
                check_type(argname="argument network_interface_id", value=network_interface_id, expected_type=type_hints["network_interface_id"])
                check_type(argname="argument private_ip_address", value=private_ip_address, expected_type=type_hints["private_ip_address"])
                check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if availability_zone is not None:
                self._values["availability_zone"] = availability_zone
            if network_interface_id is not None:
                self._values["network_interface_id"] = network_interface_id
            if private_ip_address is not None:
                self._values["private_ip_address"] = private_ip_address
            if subnet_id is not None:
                self._values["subnet_id"] = subnet_id

        @builtins.property
        def availability_zone(self) -> typing.Optional[builtins.str]:
            '''The availability Zone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-networkinterface.html#cfn-redshiftserverless-workgroup-networkinterface-availabilityzone
            '''
            result = self._values.get("availability_zone")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def network_interface_id(self) -> typing.Optional[builtins.str]:
            '''The unique identifier of the network interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-networkinterface.html#cfn-redshiftserverless-workgroup-networkinterface-networkinterfaceid
            '''
            result = self._values.get("network_interface_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def private_ip_address(self) -> typing.Optional[builtins.str]:
            '''The IPv4 address of the network interface within the subnet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-networkinterface.html#cfn-redshiftserverless-workgroup-networkinterface-privateipaddress
            '''
            result = self._values.get("private_ip_address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def subnet_id(self) -> typing.Optional[builtins.str]:
            '''The unique identifier of the subnet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-networkinterface.html#cfn-redshiftserverless-workgroup-networkinterface-subnetid
            '''
            result = self._values.get("subnet_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkInterfaceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_redshiftserverless.CfnWorkgroup.VpcEndpointProperty",
        jsii_struct_bases=[],
        name_mapping={
            "network_interfaces": "networkInterfaces",
            "vpc_endpoint_id": "vpcEndpointId",
            "vpc_id": "vpcId",
        },
    )
    class VpcEndpointProperty:
        def __init__(
            self,
            *,
            network_interfaces: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkgroup.NetworkInterfaceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            vpc_endpoint_id: typing.Optional[builtins.str] = None,
            vpc_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The connection endpoint for connecting to Amazon Redshift Serverless through the proxy.

            :param network_interfaces: One or more network interfaces of the endpoint. Also known as an interface endpoint.
            :param vpc_endpoint_id: The connection endpoint ID for connecting to Amazon Redshift Serverless.
            :param vpc_id: The VPC identifier that the endpoint is associated with.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-vpcendpoint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_redshiftserverless as redshiftserverless
                
                vpc_endpoint_property = redshiftserverless.CfnWorkgroup.VpcEndpointProperty(
                    network_interfaces=[redshiftserverless.CfnWorkgroup.NetworkInterfaceProperty(
                        availability_zone="availabilityZone",
                        network_interface_id="networkInterfaceId",
                        private_ip_address="privateIpAddress",
                        subnet_id="subnetId"
                    )],
                    vpc_endpoint_id="vpcEndpointId",
                    vpc_id="vpcId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__200b427a09281b666ef25deaac2b6bf3abeeda64d77ffa3f7903dbe300b6606d)
                check_type(argname="argument network_interfaces", value=network_interfaces, expected_type=type_hints["network_interfaces"])
                check_type(argname="argument vpc_endpoint_id", value=vpc_endpoint_id, expected_type=type_hints["vpc_endpoint_id"])
                check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if network_interfaces is not None:
                self._values["network_interfaces"] = network_interfaces
            if vpc_endpoint_id is not None:
                self._values["vpc_endpoint_id"] = vpc_endpoint_id
            if vpc_id is not None:
                self._values["vpc_id"] = vpc_id

        @builtins.property
        def network_interfaces(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkgroup.NetworkInterfaceProperty"]]]]:
            '''One or more network interfaces of the endpoint.

            Also known as an interface endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-vpcendpoint.html#cfn-redshiftserverless-workgroup-vpcendpoint-networkinterfaces
            '''
            result = self._values.get("network_interfaces")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkgroup.NetworkInterfaceProperty"]]]], result)

        @builtins.property
        def vpc_endpoint_id(self) -> typing.Optional[builtins.str]:
            '''The connection endpoint ID for connecting to Amazon Redshift Serverless.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-vpcendpoint.html#cfn-redshiftserverless-workgroup-vpcendpoint-vpcendpointid
            '''
            result = self._values.get("vpc_endpoint_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vpc_id(self) -> typing.Optional[builtins.str]:
            '''The VPC identifier that the endpoint is associated with.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-vpcendpoint.html#cfn-redshiftserverless-workgroup-vpcendpoint-vpcid
            '''
            result = self._values.get("vpc_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcEndpointProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_redshiftserverless.CfnWorkgroup.WorkgroupProperty",
        jsii_struct_bases=[],
        name_mapping={
            "base_capacity": "baseCapacity",
            "config_parameters": "configParameters",
            "creation_date": "creationDate",
            "endpoint": "endpoint",
            "enhanced_vpc_routing": "enhancedVpcRouting",
            "namespace_name": "namespaceName",
            "publicly_accessible": "publiclyAccessible",
            "security_group_ids": "securityGroupIds",
            "status": "status",
            "subnet_ids": "subnetIds",
            "workgroup_arn": "workgroupArn",
            "workgroup_id": "workgroupId",
            "workgroup_name": "workgroupName",
        },
    )
    class WorkgroupProperty:
        def __init__(
            self,
            *,
            base_capacity: typing.Optional[jsii.Number] = None,
            config_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkgroup.ConfigParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            creation_date: typing.Optional[builtins.str] = None,
            endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkgroup.EndpointProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            enhanced_vpc_routing: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            namespace_name: typing.Optional[builtins.str] = None,
            publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            status: typing.Optional[builtins.str] = None,
            subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            workgroup_arn: typing.Optional[builtins.str] = None,
            workgroup_id: typing.Optional[builtins.str] = None,
            workgroup_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The collection of computing resources from which an endpoint is created.

            :param base_capacity: The base data warehouse capacity of the workgroup in Redshift Processing Units (RPUs).
            :param config_parameters: An array of parameters to set for advanced control over a database. The options are ``auto_mv`` , ``datestyle`` , ``enable_case_sensitivity_identifier`` , ``enable_user_activity_logging`` , ``query_group`` , , ``search_path`` , and query monitoring metrics that let you define performance boundaries. For more information about query monitoring rules and available metrics, see `Query monitoring metrics for Amazon Redshift Serverless <https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html#cm-c-wlm-query-monitoring-metrics-serverless>`_ .
            :param creation_date: The creation date of the workgroup.
            :param endpoint: The endpoint that is created from the workgroup.
            :param enhanced_vpc_routing: The value that specifies whether to enable enhanced virtual private cloud (VPC) routing, which forces Amazon Redshift Serverless to route traffic through your VPC.
            :param namespace_name: The namespace the workgroup is associated with.
            :param publicly_accessible: A value that specifies whether the workgroup can be accessible from a public network.
            :param security_group_ids: An array of security group IDs to associate with the workgroup.
            :param status: The status of the workgroup.
            :param subnet_ids: An array of subnet IDs the workgroup is associated with.
            :param workgroup_arn: The Amazon Resource Name (ARN) that links to the workgroup.
            :param workgroup_id: The unique identifier of the workgroup.
            :param workgroup_name: The name of the workgroup.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_redshiftserverless as redshiftserverless
                
                workgroup_property = redshiftserverless.CfnWorkgroup.WorkgroupProperty(
                    base_capacity=123,
                    config_parameters=[redshiftserverless.CfnWorkgroup.ConfigParameterProperty(
                        parameter_key="parameterKey",
                        parameter_value="parameterValue"
                    )],
                    creation_date="creationDate",
                    endpoint=redshiftserverless.CfnWorkgroup.EndpointProperty(
                        address="address",
                        port=123,
                        vpc_endpoints=[redshiftserverless.CfnWorkgroup.VpcEndpointProperty(
                            network_interfaces=[redshiftserverless.CfnWorkgroup.NetworkInterfaceProperty(
                                availability_zone="availabilityZone",
                                network_interface_id="networkInterfaceId",
                                private_ip_address="privateIpAddress",
                                subnet_id="subnetId"
                            )],
                            vpc_endpoint_id="vpcEndpointId",
                            vpc_id="vpcId"
                        )]
                    ),
                    enhanced_vpc_routing=False,
                    namespace_name="namespaceName",
                    publicly_accessible=False,
                    security_group_ids=["securityGroupIds"],
                    status="status",
                    subnet_ids=["subnetIds"],
                    workgroup_arn="workgroupArn",
                    workgroup_id="workgroupId",
                    workgroup_name="workgroupName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b7cad236eecd67272da075e88f17a1dbdae4ee5083553d6443dcc19b3a333780)
                check_type(argname="argument base_capacity", value=base_capacity, expected_type=type_hints["base_capacity"])
                check_type(argname="argument config_parameters", value=config_parameters, expected_type=type_hints["config_parameters"])
                check_type(argname="argument creation_date", value=creation_date, expected_type=type_hints["creation_date"])
                check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
                check_type(argname="argument enhanced_vpc_routing", value=enhanced_vpc_routing, expected_type=type_hints["enhanced_vpc_routing"])
                check_type(argname="argument namespace_name", value=namespace_name, expected_type=type_hints["namespace_name"])
                check_type(argname="argument publicly_accessible", value=publicly_accessible, expected_type=type_hints["publicly_accessible"])
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
                check_type(argname="argument workgroup_arn", value=workgroup_arn, expected_type=type_hints["workgroup_arn"])
                check_type(argname="argument workgroup_id", value=workgroup_id, expected_type=type_hints["workgroup_id"])
                check_type(argname="argument workgroup_name", value=workgroup_name, expected_type=type_hints["workgroup_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if base_capacity is not None:
                self._values["base_capacity"] = base_capacity
            if config_parameters is not None:
                self._values["config_parameters"] = config_parameters
            if creation_date is not None:
                self._values["creation_date"] = creation_date
            if endpoint is not None:
                self._values["endpoint"] = endpoint
            if enhanced_vpc_routing is not None:
                self._values["enhanced_vpc_routing"] = enhanced_vpc_routing
            if namespace_name is not None:
                self._values["namespace_name"] = namespace_name
            if publicly_accessible is not None:
                self._values["publicly_accessible"] = publicly_accessible
            if security_group_ids is not None:
                self._values["security_group_ids"] = security_group_ids
            if status is not None:
                self._values["status"] = status
            if subnet_ids is not None:
                self._values["subnet_ids"] = subnet_ids
            if workgroup_arn is not None:
                self._values["workgroup_arn"] = workgroup_arn
            if workgroup_id is not None:
                self._values["workgroup_id"] = workgroup_id
            if workgroup_name is not None:
                self._values["workgroup_name"] = workgroup_name

        @builtins.property
        def base_capacity(self) -> typing.Optional[jsii.Number]:
            '''The base data warehouse capacity of the workgroup in Redshift Processing Units (RPUs).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-basecapacity
            '''
            result = self._values.get("base_capacity")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def config_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkgroup.ConfigParameterProperty"]]]]:
            '''An array of parameters to set for advanced control over a database.

            The options are ``auto_mv`` , ``datestyle`` , ``enable_case_sensitivity_identifier`` , ``enable_user_activity_logging`` , ``query_group`` , , ``search_path`` , and query monitoring metrics that let you define performance boundaries. For more information about query monitoring rules and available metrics, see `Query monitoring metrics for Amazon Redshift Serverless <https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html#cm-c-wlm-query-monitoring-metrics-serverless>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-configparameters
            '''
            result = self._values.get("config_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkgroup.ConfigParameterProperty"]]]], result)

        @builtins.property
        def creation_date(self) -> typing.Optional[builtins.str]:
            '''The creation date of the workgroup.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-creationdate
            '''
            result = self._values.get("creation_date")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def endpoint(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkgroup.EndpointProperty"]]:
            '''The endpoint that is created from the workgroup.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-endpoint
            '''
            result = self._values.get("endpoint")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkgroup.EndpointProperty"]], result)

        @builtins.property
        def enhanced_vpc_routing(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The value that specifies whether to enable enhanced virtual private cloud (VPC) routing, which forces Amazon Redshift Serverless to route traffic through your VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-enhancedvpcrouting
            '''
            result = self._values.get("enhanced_vpc_routing")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def namespace_name(self) -> typing.Optional[builtins.str]:
            '''The namespace the workgroup is associated with.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-namespacename
            '''
            result = self._values.get("namespace_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def publicly_accessible(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A value that specifies whether the workgroup can be accessible from a public network.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-publiclyaccessible
            '''
            result = self._values.get("publicly_accessible")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An array of security group IDs to associate with the workgroup.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''The status of the workgroup.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An array of subnet IDs the workgroup is associated with.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-subnetids
            '''
            result = self._values.get("subnet_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def workgroup_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) that links to the workgroup.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-workgrouparn
            '''
            result = self._values.get("workgroup_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def workgroup_id(self) -> typing.Optional[builtins.str]:
            '''The unique identifier of the workgroup.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-workgroupid
            '''
            result = self._values.get("workgroup_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def workgroup_name(self) -> typing.Optional[builtins.str]:
            '''The name of the workgroup.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-workgroupname
            '''
            result = self._values.get("workgroup_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkgroupProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_redshiftserverless.CfnWorkgroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "workgroup_name": "workgroupName",
        "base_capacity": "baseCapacity",
        "config_parameters": "configParameters",
        "enhanced_vpc_routing": "enhancedVpcRouting",
        "namespace_name": "namespaceName",
        "port": "port",
        "publicly_accessible": "publiclyAccessible",
        "security_group_ids": "securityGroupIds",
        "subnet_ids": "subnetIds",
        "tags": "tags",
    },
)
class CfnWorkgroupProps:
    def __init__(
        self,
        *,
        workgroup_name: builtins.str,
        base_capacity: typing.Optional[jsii.Number] = None,
        config_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkgroup.ConfigParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        enhanced_vpc_routing: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        namespace_name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnWorkgroup``.

        :param workgroup_name: The name of the workgroup.
        :param base_capacity: The base compute capacity of the workgroup in Redshift Processing Units (RPUs).
        :param config_parameters: A list of parameters to set for finer control over a database. Available options are ``datestyle`` , ``enable_user_activity_logging`` , ``query_group`` , ``search_path`` , and ``max_query_execution_time`` .
        :param enhanced_vpc_routing: The value that specifies whether to enable enhanced virtual private cloud (VPC) routing, which forces Amazon Redshift Serverless to route traffic through your VPC. Default: - false
        :param namespace_name: The namespace the workgroup is associated with.
        :param port: The custom port to use when connecting to a workgroup. Valid port ranges are 5431-5455 and 8191-8215. The default is 5439.
        :param publicly_accessible: A value that specifies whether the workgroup can be accessible from a public network. Default: - false
        :param security_group_ids: A list of security group IDs to associate with the workgroup.
        :param subnet_ids: A list of subnet IDs the workgroup is associated with.
        :param tags: The map of the key-value pairs used to tag the workgroup.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_redshiftserverless as redshiftserverless
            
            cfn_workgroup_props = redshiftserverless.CfnWorkgroupProps(
                workgroup_name="workgroupName",
            
                # the properties below are optional
                base_capacity=123,
                config_parameters=[redshiftserverless.CfnWorkgroup.ConfigParameterProperty(
                    parameter_key="parameterKey",
                    parameter_value="parameterValue"
                )],
                enhanced_vpc_routing=False,
                namespace_name="namespaceName",
                port=123,
                publicly_accessible=False,
                security_group_ids=["securityGroupIds"],
                subnet_ids=["subnetIds"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ee3941005026bdab05d38183c12cc7cf5ff218e6db3877161b60d823e21a136)
            check_type(argname="argument workgroup_name", value=workgroup_name, expected_type=type_hints["workgroup_name"])
            check_type(argname="argument base_capacity", value=base_capacity, expected_type=type_hints["base_capacity"])
            check_type(argname="argument config_parameters", value=config_parameters, expected_type=type_hints["config_parameters"])
            check_type(argname="argument enhanced_vpc_routing", value=enhanced_vpc_routing, expected_type=type_hints["enhanced_vpc_routing"])
            check_type(argname="argument namespace_name", value=namespace_name, expected_type=type_hints["namespace_name"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument publicly_accessible", value=publicly_accessible, expected_type=type_hints["publicly_accessible"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "workgroup_name": workgroup_name,
        }
        if base_capacity is not None:
            self._values["base_capacity"] = base_capacity
        if config_parameters is not None:
            self._values["config_parameters"] = config_parameters
        if enhanced_vpc_routing is not None:
            self._values["enhanced_vpc_routing"] = enhanced_vpc_routing
        if namespace_name is not None:
            self._values["namespace_name"] = namespace_name
        if port is not None:
            self._values["port"] = port
        if publicly_accessible is not None:
            self._values["publicly_accessible"] = publicly_accessible
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if subnet_ids is not None:
            self._values["subnet_ids"] = subnet_ids
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def workgroup_name(self) -> builtins.str:
        '''The name of the workgroup.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-workgroupname
        '''
        result = self._values.get("workgroup_name")
        assert result is not None, "Required property 'workgroup_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def base_capacity(self) -> typing.Optional[jsii.Number]:
        '''The base compute capacity of the workgroup in Redshift Processing Units (RPUs).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-basecapacity
        '''
        result = self._values.get("base_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def config_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnWorkgroup.ConfigParameterProperty]]]]:
        '''A list of parameters to set for finer control over a database.

        Available options are ``datestyle`` , ``enable_user_activity_logging`` , ``query_group`` , ``search_path`` , and ``max_query_execution_time`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-configparameters
        '''
        result = self._values.get("config_parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnWorkgroup.ConfigParameterProperty]]]], result)

    @builtins.property
    def enhanced_vpc_routing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''The value that specifies whether to enable enhanced virtual private cloud (VPC) routing, which forces Amazon Redshift Serverless to route traffic through your VPC.

        :default: - false

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-enhancedvpcrouting
        '''
        result = self._values.get("enhanced_vpc_routing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def namespace_name(self) -> typing.Optional[builtins.str]:
        '''The namespace the workgroup is associated with.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-namespacename
        '''
        result = self._values.get("namespace_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The custom port to use when connecting to a workgroup.

        Valid port ranges are 5431-5455 and 8191-8215. The default is 5439.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def publicly_accessible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A value that specifies whether the workgroup can be accessible from a public network.

        :default: - false

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-publiclyaccessible
        '''
        result = self._values.get("publicly_accessible")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of security group IDs to associate with the workgroup.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-securitygroupids
        '''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of subnet IDs the workgroup is associated with.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-subnetids
        '''
        result = self._values.get("subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The map of the key-value pairs used to tag the workgroup.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWorkgroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnNamespace",
    "CfnNamespaceProps",
    "CfnWorkgroup",
    "CfnWorkgroupProps",
]

publication.publish()

def _typecheckingstub__e517382d9f55a518348d7299a7ce6c5be66bae2202f4223bf3c891a7dd669682(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    namespace_name: builtins.str,
    admin_username: typing.Optional[builtins.str] = None,
    admin_user_password: typing.Optional[builtins.str] = None,
    db_name: typing.Optional[builtins.str] = None,
    default_iam_role_arn: typing.Optional[builtins.str] = None,
    final_snapshot_name: typing.Optional[builtins.str] = None,
    final_snapshot_retention_period: typing.Optional[jsii.Number] = None,
    iam_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    log_exports: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2df0038e9ec3a1b73ddb07c3b803a742204804b2ccd2aab0d7df9fbb8521f86(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d877d23369c8f10ea1630884d7e7c879ab22a49fc05986834857785664c640ca(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fe15d8ff16345a3e36d8c090d48eea89c8cd559ac4218facdfd95b67e49140c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e95b6bb908e50903825c7cbfdb447ab3aceb27b3a93be8aa57fe8923f432493(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b50aae57ce0c503e5aed7528570d1ab32511eacbfe2dcac51d410dd4bb1991ec(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8947213c316180fbcdb1956ca9a54febcb6a874110724c51c1db8705f8186d0a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a992711b01695733a564873ba440d2806a3692e807afc16701507c986201edd9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de06e0fc02a451c4e9e47c3f839f6289f8f8e9d4dbc0867eb263e09672990c7e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ae56ba94c395d18dd103368c4ca09a505763b47324b4820065925d61c84adaf(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9111ebc5ef107cd5d00c7617518664163ccd1b1d99fb0ec53548dd04073b0e77(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bc1c937667ef895444beeaaacfd8af398b90be0a42f50184325fdb96072b5ba(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1526e0cedff0515a6bb96570f366670e82fb4d0cc597e2d7a8b0a091f0420dea(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e2da7bae4bc39426d05dc2f307e08d5246472ad626b032ef4c2ea7b7d1bd33f(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bcbea65acb7d2a3cef7455cfbb52c832d3da01cd5e02df21a06cdb2b4822e35(
    *,
    admin_username: typing.Optional[builtins.str] = None,
    creation_date: typing.Optional[builtins.str] = None,
    db_name: typing.Optional[builtins.str] = None,
    default_iam_role_arn: typing.Optional[builtins.str] = None,
    iam_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    log_exports: typing.Optional[typing.Sequence[builtins.str]] = None,
    namespace_arn: typing.Optional[builtins.str] = None,
    namespace_id: typing.Optional[builtins.str] = None,
    namespace_name: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5964a5da555f62a5d9615a6e07cd0d1128cdf904fd5aa3c5be9fd5e53dc30bd9(
    *,
    namespace_name: builtins.str,
    admin_username: typing.Optional[builtins.str] = None,
    admin_user_password: typing.Optional[builtins.str] = None,
    db_name: typing.Optional[builtins.str] = None,
    default_iam_role_arn: typing.Optional[builtins.str] = None,
    final_snapshot_name: typing.Optional[builtins.str] = None,
    final_snapshot_retention_period: typing.Optional[jsii.Number] = None,
    iam_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    log_exports: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61a1b6ebbdacc577619f4e17ddabdaa553ffe5fe072b72e14ddf7d9c3f7e1a04(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    workgroup_name: builtins.str,
    base_capacity: typing.Optional[jsii.Number] = None,
    config_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkgroup.ConfigParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    enhanced_vpc_routing: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    namespace_name: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__986feaaa3c97c38d5a5c4414a977741007338bd588a8ebc981d89e63b28c9c38(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__575b09c3449f3d47af302b94ec8c88b82387f8f428024e134c076d5600122345(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44b001bba04c1f96a7169e528d056ccd8d9035fee30af63b1f339873bf7e3ea7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d35b55423f49c0c42ee449a11852238ff7a68ae5e2e78f2da58bcb94c221a85(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00339df2c3d04a43ab10d867748f8678b0423745badc0e14afa8bb128d473607(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnWorkgroup.ConfigParameterProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b06db2b227debd7cc917f51bf7c4c0bb700bca075b329af61a43f37521feba71(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a009fb86999f55de110193d15ea127b35ea379a1d840ddd42a0406b02f3a997a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e3a61acfcbbe3b107c15ebd1c1248f3bd150ad58cf876908da7870de9fd6fde(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__974542b0d8aa6c1847dd536dcf795ef2c4719aed798ea365b0767f6ad3234ca0(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2864d0fac41ac305963b5532a731665cbc0d93a810a41ea2d2fe98a5285e8aa(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67e139cef151f144f2bb04082850da469be0ab0515cff591edf9fc1e44df78a9(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3104c5d5a81618ce7738aabf06bbd67fea6c82cd5abea01e1b03c71c5065efc(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__322e3a40a90a7ebca9e3ef09024360dddede638badc33eeda64eccd556f3dc5f(
    *,
    parameter_key: typing.Optional[builtins.str] = None,
    parameter_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1064dbbc6e1afc7fbd36b9ac721b89fc24382d0930f8f41542644b48bc6c07bf(
    *,
    address: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    vpc_endpoints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkgroup.VpcEndpointProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c27a8032aaa250691e1e68b2e75ce65c47142ac6b83ad22f01b09ec293f841b8(
    *,
    availability_zone: typing.Optional[builtins.str] = None,
    network_interface_id: typing.Optional[builtins.str] = None,
    private_ip_address: typing.Optional[builtins.str] = None,
    subnet_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__200b427a09281b666ef25deaac2b6bf3abeeda64d77ffa3f7903dbe300b6606d(
    *,
    network_interfaces: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkgroup.NetworkInterfaceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    vpc_endpoint_id: typing.Optional[builtins.str] = None,
    vpc_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7cad236eecd67272da075e88f17a1dbdae4ee5083553d6443dcc19b3a333780(
    *,
    base_capacity: typing.Optional[jsii.Number] = None,
    config_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkgroup.ConfigParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    creation_date: typing.Optional[builtins.str] = None,
    endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkgroup.EndpointProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    enhanced_vpc_routing: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    namespace_name: typing.Optional[builtins.str] = None,
    publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    status: typing.Optional[builtins.str] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    workgroup_arn: typing.Optional[builtins.str] = None,
    workgroup_id: typing.Optional[builtins.str] = None,
    workgroup_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ee3941005026bdab05d38183c12cc7cf5ff218e6db3877161b60d823e21a136(
    *,
    workgroup_name: builtins.str,
    base_capacity: typing.Optional[jsii.Number] = None,
    config_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkgroup.ConfigParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    enhanced_vpc_routing: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    namespace_name: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
