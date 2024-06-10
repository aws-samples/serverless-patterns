'''
# AWS Key Management Service Construct Library

Define a KMS key:

```python
kms.Key(self, "MyKey",
    enable_key_rotation=True,
    rotation_period=Duration.days(180)
)
```

Define a KMS key with waiting period:

Specifies the number of days in the waiting period before AWS KMS deletes a CMK that has been removed from a CloudFormation stack.

```python
key = kms.Key(self, "MyKey",
    pending_window=Duration.days(10)
)
```

Add a couple of aliases:

```python
key = kms.Key(self, "MyKey")
key.add_alias("alias/foo")
key.add_alias("alias/bar")
```

Define a key with specific key spec and key usage:

Valid `keySpec` values depends on `keyUsage` value.

```python
key = kms.Key(self, "MyKey",
    key_spec=kms.KeySpec.ECC_SECG_P256K1,  # Default to SYMMETRIC_DEFAULT
    key_usage=kms.KeyUsage.SIGN_VERIFY
)
```

## Sharing keys between stacks

To use a KMS key in a different stack in the same CDK application,
pass the construct to the other stack:

```python
#
# Stack that defines the key
#
class KeyStack(cdk.Stack):

    def __init__(self, scope, id, *, description=None, env=None, stackName=None, tags=None, synthesizer=None, terminationProtection=None, analyticsReporting=None, crossRegionReferences=None, permissionsBoundary=None, suppressTemplateIndentation=None):
        super().__init__(scope, id, description=description, env=env, stackName=stackName, tags=tags, synthesizer=synthesizer, terminationProtection=terminationProtection, analyticsReporting=analyticsReporting, crossRegionReferences=crossRegionReferences, permissionsBoundary=permissionsBoundary, suppressTemplateIndentation=suppressTemplateIndentation)
        self.key = kms.Key(self, "MyKey", removal_policy=cdk.RemovalPolicy.DESTROY)

#
# Stack that uses the key
#
class UseStack(cdk.Stack):
    def __init__(self, scope, id, *, key, description=None, env=None, stackName=None, tags=None, synthesizer=None, terminationProtection=None, analyticsReporting=None, crossRegionReferences=None, permissionsBoundary=None, suppressTemplateIndentation=None):
        super().__init__(scope, id, key=key, description=description, env=env, stackName=stackName, tags=tags, synthesizer=synthesizer, terminationProtection=terminationProtection, analyticsReporting=analyticsReporting, crossRegionReferences=crossRegionReferences, permissionsBoundary=permissionsBoundary, suppressTemplateIndentation=suppressTemplateIndentation)

        # Use the IKey object here.
        kms.Alias(self, "Alias",
            alias_name="alias/foo",
            target_key=key
        )

key_stack = KeyStack(app, "KeyStack")
UseStack(app, "UseStack", key=key_stack.key)
```

## Importing existing keys

### Import key by ARN

To use a KMS key that is not defined in this CDK app, but is created through other means, use
`Key.fromKeyArn(parent, name, ref)`:

```python
my_key_imported = kms.Key.from_key_arn(self, "MyImportedKey", "arn:aws:...")

# you can do stuff with this imported key.
my_key_imported.add_alias("alias/foo")
```

Note that a call to `.addToResourcePolicy(statement)` on `myKeyImported` will not have
an affect on the key's policy because it is not owned by your stack. The call
will be a no-op.

### Import key by alias

If a Key has an associated Alias, the Alias can be imported by name and used in place
of the Key as a reference. A common scenario for this is in referencing AWS managed keys.

```python
import aws_cdk.aws_cloudtrail as cloudtrail


my_key_alias = kms.Alias.from_alias_name(self, "myKey", "alias/aws/s3")
trail = cloudtrail.Trail(self, "myCloudTrail",
    send_to_cloud_watch_logs=True,
    encryption_key=my_key_alias
)
```

Note that calls to `addToResourcePolicy` and `grant*` methods on `myKeyAlias` will be
no-ops, and `addAlias` and `aliasTargetKey` will fail, as the imported alias does not
have a reference to the underlying KMS Key.

### Lookup key by alias

If you can't use a KMS key imported by alias (e.g. because you need access to the key id), you can lookup the key with `Key.fromLookup()`.

In general, the preferred method would be to use `Alias.fromAliasName()` which returns an `IAlias` object which extends `IKey`. However, some services need to have access to the underlying key id. In this case, `Key.fromLookup()` allows to lookup the key id.

The result of the `Key.fromLookup()` operation will be written to a file
called `cdk.context.json`. You must commit this file to source control so
that the lookup values are available in non-privileged environments such
as CI build steps, and to ensure your template builds are repeatable.

Here's how `Key.fromLookup()` can be used:

```python
my_key_lookup = kms.Key.from_lookup(self, "MyKeyLookup",
    alias_name="alias/KeyAlias"
)

role = iam.Role(self, "MyRole",
    assumed_by=iam.ServicePrincipal("lambda.amazonaws.com")
)
my_key_lookup.grant_encrypt_decrypt(role)
```

Note that a call to `.addToResourcePolicy(statement)` on `myKeyLookup` will not have
an affect on the key's policy because it is not owned by your stack. The call
will be a no-op.

## Key Policies

Controlling access and usage of KMS Keys requires the use of key policies (resource-based policies attached to the key);
this is in contrast to most other AWS resources where access can be entirely controlled with IAM policies,
and optionally complemented with resource policies. For more in-depth understanding of KMS key access and policies, see

* https://docs.aws.amazon.com/kms/latest/developerguide/control-access-overview.html
* https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html

KMS keys can be created to trust IAM policies. This is the default behavior for both the KMS APIs and in
the console. This behavior is enabled by the '@aws-cdk/aws-kms:defaultKeyPolicies' feature flag,
which is set for all new projects; for existing projects, this same behavior can be enabled by
passing the `trustAccountIdentities` property as `true` when creating the key:

```python
kms.Key(self, "MyKey", trust_account_identities=True)
```

With either the `@aws-cdk/aws-kms:defaultKeyPolicies` feature flag set,
or the `trustAccountIdentities` prop set, the Key will be given the following default key policy:

```json
{
  "Effect": "Allow",
  "Principal": {"AWS": "arn:aws:iam::111122223333:root"},
  "Action": "kms:*",
  "Resource": "*"
}
```

This policy grants full access to the key to the root account user.
This enables the root account user -- via IAM policies -- to grant access to other IAM principals.
With the above default policy, future permissions can be added to either the key policy or IAM principal policy.

```python
key = kms.Key(self, "MyKey")
user = iam.User(self, "MyUser")
key.grant_encrypt(user)
```

Adopting the default KMS key policy (and so trusting account identities)
solves many issues around cyclic dependencies between stacks.
Without this default key policy, future permissions must be added to both the key policy and IAM principal policy,
which can cause cyclic dependencies if the permissions cross stack boundaries.
(For example, an encrypted bucket in one stack, and Lambda function that accesses it in another.)

### Appending to or replacing the default key policy

The default key policy can be amended or replaced entirely, depending on your use case and requirements.
A common addition to the key policy would be to add other key admins that are allowed to administer the key
(e.g., change permissions, revoke, delete). Additional key admins can be specified at key creation or after
via the `grantAdmin` method.

```python
my_trusted_admin_role = iam.Role.from_role_arn(self, "TrustedRole", "arn:aws:iam:....")
key = kms.Key(self, "MyKey",
    admins=[my_trusted_admin_role]
)

second_key = kms.Key(self, "MyKey2")
second_key.grant_admin(my_trusted_admin_role)
```

Alternatively, a custom key policy can be specified, which will replace the default key policy.

> **Note**: In applications without the '@aws-cdk/aws-kms:defaultKeyPolicies' feature flag set
> and with `trustedAccountIdentities` set to false (the default), specifying a policy at key creation *appends* the
> provided policy to the default key policy, rather than *replacing* the default policy.

```python
my_trusted_admin_role = iam.Role.from_role_arn(self, "TrustedRole", "arn:aws:iam:....")
# Creates a limited admin policy and assigns to the account root.
my_custom_policy = iam.PolicyDocument(
    statements=[iam.PolicyStatement(
        actions=["kms:Create*", "kms:Describe*", "kms:Enable*", "kms:List*", "kms:Put*"
        ],
        principals=[iam.AccountRootPrincipal()],
        resources=["*"]
    )]
)
key = kms.Key(self, "MyKey",
    policy=my_custom_policy
)
```

> **Warning:** Replacing the default key policy with one that only grants access to a specific user or role
> runs the risk of the key becoming unmanageable if that user or role is deleted.
> It is highly recommended that the key policy grants access to the account root, rather than specific principals.
> See https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html for more information.

### HMAC specific key policies

HMAC keys have a different key policy than other KMS keys. They have a policy for generating and for verifying a MAC.
The respective policies can be attached to a principal via the `grantGenerateMac` and `grantVerifyMac` methods.

```python
key = kms.Key(self, "MyKey")
user = iam.User(self, "MyUser")
key.grant_generate_mac(user) # Adds 'kms:GenerateMac' to the principal's policy
key.grant_verify_mac(user)
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
    ITaggable as _ITaggable_36806126,
    RemovalPolicy as _RemovalPolicy_9f93c814,
    Resource as _Resource_45bc6135,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..aws_iam import (
    AddToResourcePolicyResult as _AddToResourcePolicyResult_1d0a53ad,
    Grant as _Grant_a7ae64f8,
    IGrantable as _IGrantable_71c4f5de,
    IPrincipal as _IPrincipal_539bb2fd,
    PolicyDocument as _PolicyDocument_3ac34393,
    PolicyStatement as _PolicyStatement_0fe33853,
    PrincipalBase as _PrincipalBase_b5077813,
    PrincipalPolicyFragment as _PrincipalPolicyFragment_6a855d11,
)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_kms.AliasAttributes",
    jsii_struct_bases=[],
    name_mapping={"alias_name": "aliasName", "alias_target_key": "aliasTargetKey"},
)
class AliasAttributes:
    def __init__(self, *, alias_name: builtins.str, alias_target_key: "IKey") -> None:
        '''Properties of a reference to an existing KMS Alias.

        :param alias_name: Specifies the alias name. This value must begin with alias/ followed by a name (i.e. alias/ExampleAlias)
        :param alias_target_key: The customer master key (CMK) to which the Alias refers.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_kms as kms
            
            # key: kms.Key
            
            alias_attributes = kms.AliasAttributes(
                alias_name="aliasName",
                alias_target_key=key
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4044a422b77633efb024676d8b64edc24f9f3e6dda3050cda6f5bb78c388993)
            check_type(argname="argument alias_name", value=alias_name, expected_type=type_hints["alias_name"])
            check_type(argname="argument alias_target_key", value=alias_target_key, expected_type=type_hints["alias_target_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alias_name": alias_name,
            "alias_target_key": alias_target_key,
        }

    @builtins.property
    def alias_name(self) -> builtins.str:
        '''Specifies the alias name.

        This value must begin with alias/ followed by a name (i.e. alias/ExampleAlias)
        '''
        result = self._values.get("alias_name")
        assert result is not None, "Required property 'alias_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alias_target_key(self) -> "IKey":
        '''The customer master key (CMK) to which the Alias refers.'''
        result = self._values.get("alias_target_key")
        assert result is not None, "Required property 'alias_target_key' is missing"
        return typing.cast("IKey", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AliasAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_kms.AliasProps",
    jsii_struct_bases=[],
    name_mapping={
        "alias_name": "aliasName",
        "target_key": "targetKey",
        "removal_policy": "removalPolicy",
    },
)
class AliasProps:
    def __init__(
        self,
        *,
        alias_name: builtins.str,
        target_key: "IKey",
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    ) -> None:
        '''Construction properties for a KMS Key Alias object.

        :param alias_name: The name of the alias. The name must start with alias followed by a forward slash, such as alias/. You can't specify aliases that begin with alias/AWS. These aliases are reserved.
        :param target_key: The ID of the key for which you are creating the alias. Specify the key's globally unique identifier or Amazon Resource Name (ARN). You can't specify another alias.
        :param removal_policy: Policy to apply when the alias is removed from this stack. Default: - The alias will be deleted

        :exampleMetadata: infused

        Example::

            # Passing an encrypted replication bucket created in a different stack.
            app = App()
            replication_stack = Stack(app, "ReplicationStack",
                env=Environment(
                    region="us-west-1"
                )
            )
            key = kms.Key(replication_stack, "ReplicationKey")
            alias = kms.Alias(replication_stack, "ReplicationAlias",
                # aliasName is required
                alias_name=PhysicalName.GENERATE_IF_NEEDED,
                target_key=key
            )
            replication_bucket = s3.Bucket(replication_stack, "ReplicationBucket",
                bucket_name=PhysicalName.GENERATE_IF_NEEDED,
                encryption_key=alias
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e903bf066a426ef7752d4c25658bc63605bb655d804e5468ef9fa75e0fe87f57)
            check_type(argname="argument alias_name", value=alias_name, expected_type=type_hints["alias_name"])
            check_type(argname="argument target_key", value=target_key, expected_type=type_hints["target_key"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alias_name": alias_name,
            "target_key": target_key,
        }
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy

    @builtins.property
    def alias_name(self) -> builtins.str:
        '''The name of the alias.

        The name must start with alias followed by a
        forward slash, such as alias/. You can't specify aliases that begin with
        alias/AWS. These aliases are reserved.
        '''
        result = self._values.get("alias_name")
        assert result is not None, "Required property 'alias_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_key(self) -> "IKey":
        '''The ID of the key for which you are creating the alias.

        Specify the key's
        globally unique identifier or Amazon Resource Name (ARN). You can't
        specify another alias.
        '''
        result = self._values.get("target_key")
        assert result is not None, "Required property 'target_key' is missing"
        return typing.cast("IKey", result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[_RemovalPolicy_9f93c814]:
        '''Policy to apply when the alias is removed from this stack.

        :default: - The alias will be deleted
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_RemovalPolicy_9f93c814], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AliasProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnAlias(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_kms.CfnAlias",
):
    '''The ``AWS::KMS::Alias`` resource specifies a display name for a `KMS key <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#kms_keys>`_ . You can use an alias to identify a KMS key in the AWS KMS console, in the `DescribeKey <https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html>`_ operation, and in `cryptographic operations <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#cryptographic-operations>`_ , such as `Decrypt <https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html>`_ and `GenerateDataKey <https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html>`_ .

    .. epigraph::

       Adding, deleting, or updating an alias can allow or deny permission to the KMS key. For details, see `ABAC for AWS KMS <https://docs.aws.amazon.com/kms/latest/developerguide/abac.html>`_ in the *AWS Key Management Service Developer Guide* .

    Using an alias to refer to a KMS key can help you simplify key management. For example, an alias in your code can be associated with different KMS keys in different AWS Regions . For more information, see `Using aliases <https://docs.aws.amazon.com/kms/latest/developerguide/kms-alias.html>`_ in the *AWS Key Management Service Developer Guide* .

    When specifying an alias, observe the following rules.

    - Each alias is associated with one KMS key, but multiple aliases can be associated with the same KMS key.
    - The alias and its associated KMS key must be in the same AWS account and Region.
    - The alias name must be unique in the AWS account and Region. However, you can create aliases with the same name in different AWS Regions . For example, you can have an ``alias/projectKey`` in multiple Regions, each of which is associated with a KMS key in its Region.
    - Each alias name must begin with ``alias/`` followed by a name, such as ``alias/exampleKey`` . The alias name can contain only alphanumeric characters, forward slashes (/), underscores (_), and dashes (-). Alias names cannot begin with ``alias/aws/`` . That alias name prefix is reserved for `AWS managed keys <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk>`_ .

    *Regions*

    AWS KMS CloudFormation resources are available in all AWS Regions in which AWS KMS and AWS CloudFormation are supported.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-alias.html
    :cloudformationResource: AWS::KMS::Alias
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_kms as kms
        
        cfn_alias = kms.CfnAlias(self, "MyCfnAlias",
            alias_name="aliasName",
            target_key_id="targetKeyId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        alias_name: builtins.str,
        target_key_id: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param alias_name: Specifies the alias name. This value must begin with ``alias/`` followed by a name, such as ``alias/ExampleAlias`` . .. epigraph:: If you change the value of the ``AliasName`` property, the existing alias is deleted and a new alias is created for the specified KMS key. This change can disrupt applications that use the alias. It can also allow or deny access to a KMS key affected by attribute-based access control (ABAC). The alias must be string of 1-256 characters. It can contain only alphanumeric characters, forward slashes (/), underscores (_), and dashes (-). The alias name cannot begin with ``alias/aws/`` . The ``alias/aws/`` prefix is reserved for `AWS managed keys <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk>`_ .
        :param target_key_id: Associates the alias with the specified `customer managed key <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk>`_ . The KMS key must be in the same AWS account and Region. A valid key ID is required. If you supply a null or empty string value, this operation returns an error. For help finding the key ID and ARN, see `Finding the key ID and ARN <https://docs.aws.amazon.com/kms/latest/developerguide/viewing-keys.html#find-cmk-id-arn>`_ in the *AWS Key Management Service Developer Guide* . Specify the key ID or the key ARN of the KMS key. For example: - Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab`` - Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`` To get the key ID and key ARN for a KMS key, use `ListKeys <https://docs.aws.amazon.com/kms/latest/APIReference/API_ListKeys.html>`_ or `DescribeKey <https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ed5a3924f89c3ad638de218f71940a644d4f9331e3a66f708de865cc3551205)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAliasProps(alias_name=alias_name, target_key_id=target_key_id)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91d92bc86df739cdbb4a623f1bec0006f2c4e912b1d6817e7e5fc8fc28d6d61d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__be1861ad699c79ab6c6405435694534bc0b254bb6fe02fa309564e05b8ab5a6f)
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
    @jsii.member(jsii_name="aliasName")
    def alias_name(self) -> builtins.str:
        '''Specifies the alias name.

        This value must begin with ``alias/`` followed by a name, such as ``alias/ExampleAlias`` .
        '''
        return typing.cast(builtins.str, jsii.get(self, "aliasName"))

    @alias_name.setter
    def alias_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__293c0aafbebd8a831d41848f3d7035971f2665e6401dfe8705989d1abae2c2c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aliasName", value)

    @builtins.property
    @jsii.member(jsii_name="targetKeyId")
    def target_key_id(self) -> builtins.str:
        '''Associates the alias with the specified `customer managed key <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk>`_ . The KMS key must be in the same AWS account and Region.'''
        return typing.cast(builtins.str, jsii.get(self, "targetKeyId"))

    @target_key_id.setter
    def target_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e12c32dedd31d49587e236bb886a73e1a0ef34730815c73039721efa393b6fb2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetKeyId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_kms.CfnAliasProps",
    jsii_struct_bases=[],
    name_mapping={"alias_name": "aliasName", "target_key_id": "targetKeyId"},
)
class CfnAliasProps:
    def __init__(
        self,
        *,
        alias_name: builtins.str,
        target_key_id: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnAlias``.

        :param alias_name: Specifies the alias name. This value must begin with ``alias/`` followed by a name, such as ``alias/ExampleAlias`` . .. epigraph:: If you change the value of the ``AliasName`` property, the existing alias is deleted and a new alias is created for the specified KMS key. This change can disrupt applications that use the alias. It can also allow or deny access to a KMS key affected by attribute-based access control (ABAC). The alias must be string of 1-256 characters. It can contain only alphanumeric characters, forward slashes (/), underscores (_), and dashes (-). The alias name cannot begin with ``alias/aws/`` . The ``alias/aws/`` prefix is reserved for `AWS managed keys <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk>`_ .
        :param target_key_id: Associates the alias with the specified `customer managed key <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk>`_ . The KMS key must be in the same AWS account and Region. A valid key ID is required. If you supply a null or empty string value, this operation returns an error. For help finding the key ID and ARN, see `Finding the key ID and ARN <https://docs.aws.amazon.com/kms/latest/developerguide/viewing-keys.html#find-cmk-id-arn>`_ in the *AWS Key Management Service Developer Guide* . Specify the key ID or the key ARN of the KMS key. For example: - Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab`` - Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`` To get the key ID and key ARN for a KMS key, use `ListKeys <https://docs.aws.amazon.com/kms/latest/APIReference/API_ListKeys.html>`_ or `DescribeKey <https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-alias.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_kms as kms
            
            cfn_alias_props = kms.CfnAliasProps(
                alias_name="aliasName",
                target_key_id="targetKeyId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbfd3a4fafdacbfbfd8d6fce574bc924973ce57499da64b6659e12ea905b460f)
            check_type(argname="argument alias_name", value=alias_name, expected_type=type_hints["alias_name"])
            check_type(argname="argument target_key_id", value=target_key_id, expected_type=type_hints["target_key_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alias_name": alias_name,
            "target_key_id": target_key_id,
        }

    @builtins.property
    def alias_name(self) -> builtins.str:
        '''Specifies the alias name. This value must begin with ``alias/`` followed by a name, such as ``alias/ExampleAlias`` .

        .. epigraph::

           If you change the value of the ``AliasName`` property, the existing alias is deleted and a new alias is created for the specified KMS key. This change can disrupt applications that use the alias. It can also allow or deny access to a KMS key affected by attribute-based access control (ABAC).

        The alias must be string of 1-256 characters. It can contain only alphanumeric characters, forward slashes (/), underscores (_), and dashes (-). The alias name cannot begin with ``alias/aws/`` . The ``alias/aws/`` prefix is reserved for `AWS managed keys <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-alias.html#cfn-kms-alias-aliasname
        '''
        result = self._values.get("alias_name")
        assert result is not None, "Required property 'alias_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_key_id(self) -> builtins.str:
        '''Associates the alias with the specified `customer managed key <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk>`_ . The KMS key must be in the same AWS account and Region.

        A valid key ID is required. If you supply a null or empty string value, this operation returns an error.

        For help finding the key ID and ARN, see `Finding the key ID and ARN <https://docs.aws.amazon.com/kms/latest/developerguide/viewing-keys.html#find-cmk-id-arn>`_ in the *AWS Key Management Service Developer Guide* .

        Specify the key ID or the key ARN of the KMS key.

        For example:

        - Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``
        - Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

        To get the key ID and key ARN for a KMS key, use `ListKeys <https://docs.aws.amazon.com/kms/latest/APIReference/API_ListKeys.html>`_ or `DescribeKey <https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-alias.html#cfn-kms-alias-targetkeyid
        '''
        result = self._values.get("target_key_id")
        assert result is not None, "Required property 'target_key_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAliasProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnKey(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_kms.CfnKey",
):
    '''The ``AWS::KMS::Key`` resource specifies an `KMS key <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#kms_keys>`_ in AWS Key Management Service . You can use this resource to create symmetric encryption KMS keys, asymmetric KMS keys for encryption or signing, and symmetric HMAC KMS keys. You can use ``AWS::KMS::Key`` to create `multi-Region primary keys <https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html#mrk-primary-key>`_ of all supported types. To replicate a multi-Region key, use the ``AWS::KMS::ReplicaKey`` resource.

    .. epigraph::

       If you change the value of the ``KeySpec`` , ``KeyUsage`` , ``Origin`` , or ``MultiRegion`` properties of an existing KMS key, the update request fails, regardless of the value of the ```UpdateReplacePolicy`` attribute <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.html>`_ . This prevents you from accidentally deleting a KMS key by changing any of its immutable property values. > AWS KMS replaced the term *customer master key (CMK)* with *AWS KMS key* and *KMS key* . The concept has not changed. To prevent breaking changes, AWS KMS is keeping some variations of this term.

    You can use symmetric encryption KMS keys to encrypt and decrypt small amounts of data, but they are more commonly used to generate data keys and data key pairs. You can also use a symmetric encryption KMS key to encrypt data stored in AWS services that are `integrated with AWS KMS <https://docs.aws.amazon.com//kms/features/#AWS_Service_Integration>`_ . For more information, see `Symmetric encryption KMS keys <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#symmetric-cmks>`_ in the *AWS Key Management Service Developer Guide* .

    You can use asymmetric KMS keys to encrypt and decrypt data or sign messages and verify signatures. To create an asymmetric key, you must specify an asymmetric ``KeySpec`` value and a ``KeyUsage`` value. For details, see `Asymmetric keys in AWS KMS <https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html>`_ in the *AWS Key Management Service Developer Guide* .

    You can use HMAC KMS keys (which are also symmetric keys) to generate and verify hash-based message authentication codes. To create an HMAC key, you must specify an HMAC ``KeySpec`` value and a ``KeyUsage`` value of ``GENERATE_VERIFY_MAC`` . For details, see `HMAC keys in AWS KMS <https://docs.aws.amazon.com/kms/latest/developerguide/hmac.html>`_ in the *AWS Key Management Service Developer Guide* .

    You can also create symmetric encryption, asymmetric, and HMAC multi-Region primary keys. To create a multi-Region primary key, set the ``MultiRegion`` property to ``true`` . For information about multi-Region keys, see `Multi-Region keys in AWS KMS <https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html>`_ in the *AWS Key Management Service Developer Guide* .

    You cannot use the ``AWS::KMS::Key`` resource to specify a KMS key with `imported key material <https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html>`_ or a KMS key in a `custom key store <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`_ .

    *Regions*

    AWS KMS CloudFormation resources are available in all Regions in which AWS KMS and AWS CloudFormation are supported. You can use the ``AWS::KMS::Key`` resource to create and manage all KMS key types that are supported in a Region.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html
    :cloudformationResource: AWS::KMS::Key
    :exampleMetadata: infused

    Example::

        # cfn_template: cfn_inc.CfnInclude
        
        cfn_key = cfn_template.get_resource("Key")
        key = kms.Key.from_cfn_key(cfn_key)
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        bypass_policy_lockout_safety_check: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        enable_key_rotation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        key_policy: typing.Any = None,
        key_spec: typing.Optional[builtins.str] = None,
        key_usage: typing.Optional[builtins.str] = None,
        multi_region: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        origin: typing.Optional[builtins.str] = None,
        pending_window_in_days: typing.Optional[jsii.Number] = None,
        rotation_period_in_days: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param bypass_policy_lockout_safety_check: Skips ("bypasses") the key policy lockout safety check. The default value is false. .. epigraph:: Setting this value to true increases the risk that the KMS key becomes unmanageable. Do not set this value to true indiscriminately. For more information, see `Default key policy <https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-default.html#prevent-unmanageable-key>`_ in the *AWS Key Management Service Developer Guide* . Use this parameter only when you intend to prevent the principal that is making the request from making a subsequent `PutKeyPolicy <https://docs.aws.amazon.com/kms/latest/APIReference/API_PutKeyPolicy.html>`_ request on the KMS key. Default: - false
        :param description: A description of the KMS key. Use a description that helps you to distinguish this KMS key from others in the account, such as its intended use.
        :param enabled: Specifies whether the KMS key is enabled. Disabled KMS keys cannot be used in cryptographic operations. When ``Enabled`` is ``true`` , the *key state* of the KMS key is ``Enabled`` . When ``Enabled`` is ``false`` , the key state of the KMS key is ``Disabled`` . The default value is ``true`` . The actual key state of the KMS key might be affected by actions taken outside of CloudFormation, such as running the `EnableKey <https://docs.aws.amazon.com/kms/latest/APIReference/API_EnableKey.html>`_ , `DisableKey <https://docs.aws.amazon.com/kms/latest/APIReference/API_DisableKey.html>`_ , or `ScheduleKeyDeletion <https://docs.aws.amazon.com/kms/latest/APIReference/API_ScheduleKeyDeletion.html>`_ operations. For information about the key states of a KMS key, see `Key state: Effect on your KMS key <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`_ in the *AWS Key Management Service Developer Guide* .
        :param enable_key_rotation: Enables automatic rotation of the key material for the specified KMS key. By default, automatic key rotation is not enabled. AWS KMS supports automatic rotation only for symmetric encryption KMS keys ( ``KeySpec`` = ``SYMMETRIC_DEFAULT`` ). For asymmetric KMS keys, HMAC KMS keys, and KMS keys with Origin ``EXTERNAL`` , omit the ``EnableKeyRotation`` property or set it to ``false`` . To enable automatic key rotation of the key material for a multi-Region KMS key, set ``EnableKeyRotation`` to ``true`` on the primary key (created by using ``AWS::KMS::Key`` ). AWS KMS copies the rotation status to all replica keys. For details, see `Rotating multi-Region keys <https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-manage.html#multi-region-rotate>`_ in the *AWS Key Management Service Developer Guide* . When you enable automatic rotation, AWS KMS automatically creates new key material for the KMS key one year after the enable date and every year thereafter. AWS KMS retains all key material until you delete the KMS key. For detailed information about automatic key rotation, see `Rotating KMS keys <https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html>`_ in the *AWS Key Management Service Developer Guide* .
        :param key_policy: The key policy to attach to the KMS key. If you provide a key policy, it must meet the following criteria: - The key policy must allow the caller to make a subsequent `PutKeyPolicy <https://docs.aws.amazon.com/kms/latest/APIReference/API_PutKeyPolicy.html>`_ request on the KMS key. This reduces the risk that the KMS key becomes unmanageable. For more information, see `Default key policy <https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default-allow-root-enable-iam>`_ in the *AWS Key Management Service Developer Guide* . (To omit this condition, set ``BypassPolicyLockoutSafetyCheck`` to true.) - Each statement in the key policy must contain one or more principals. The principals in the key policy must exist and be visible to AWS KMS . When you create a new AWS principal (for example, an IAM user or role), you might need to enforce a delay before including the new principal in a key policy because the new principal might not be immediately visible to AWS KMS . For more information, see `Changes that I make are not always immediately visible <https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_general.html#troubleshoot_general_eventual-consistency>`_ in the *AWS Identity and Access Management User Guide* . If you do not provide a key policy, AWS KMS attaches a default key policy to the KMS key. For more information, see `Default key policy <https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default>`_ in the *AWS Key Management Service Developer Guide* . A key policy document can include only the following characters: - Printable ASCII characters - Printable characters in the Basic Latin and Latin-1 Supplement character set - The tab ( ``\\u0009`` ), line feed ( ``\\u000A`` ), and carriage return ( ``\\u000D`` ) special characters *Minimum* : ``1`` *Maximum* : ``32768``
        :param key_spec: Specifies the type of KMS key to create. The default value, ``SYMMETRIC_DEFAULT`` , creates a KMS key with a 256-bit symmetric key for encryption and decryption. In China Regions, ``SYMMETRIC_DEFAULT`` creates a 128-bit symmetric key that uses SM4 encryption. You can't change the ``KeySpec`` value after the KMS key is created. For help choosing a key spec for your KMS key, see `Choosing a KMS key type <https://docs.aws.amazon.com/kms/latest/developerguide/symm-asymm-choose.html>`_ in the *AWS Key Management Service Developer Guide* . The ``KeySpec`` property determines the type of key material in the KMS key and the algorithms that the KMS key supports. To further restrict the algorithms that can be used with the KMS key, use a condition key in its key policy or IAM policy. For more information, see `AWS KMS condition keys <https://docs.aws.amazon.com/kms/latest/developerguide/policy-conditions.html#conditions-kms>`_ in the *AWS Key Management Service Developer Guide* . .. epigraph:: If you change the value of the ``KeySpec`` property on an existing KMS key, the update request fails, regardless of the value of the ```UpdateReplacePolicy`` attribute <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.html>`_ . This prevents you from accidentally deleting a KMS key by changing an immutable property value. > `AWS services that are integrated with AWS KMS <https://docs.aws.amazon.com/kms/features/#AWS_Service_Integration>`_ use symmetric encryption KMS keys to protect your data. These services do not support encryption with asymmetric KMS keys. For help determining whether a KMS key is asymmetric, see `Identifying asymmetric KMS keys <https://docs.aws.amazon.com/kms/latest/developerguide/find-symm-asymm.html>`_ in the *AWS Key Management Service Developer Guide* . AWS KMS supports the following key specs for KMS keys: - Symmetric encryption key (default) - ``SYMMETRIC_DEFAULT`` (AES-256-GCM) - HMAC keys (symmetric) - ``HMAC_224`` - ``HMAC_256`` - ``HMAC_384`` - ``HMAC_512`` - Asymmetric RSA key pairs - ``RSA_2048`` - ``RSA_3072`` - ``RSA_4096`` - Asymmetric NIST-recommended elliptic curve key pairs - ``ECC_NIST_P256`` (secp256r1) - ``ECC_NIST_P384`` (secp384r1) - ``ECC_NIST_P521`` (secp521r1) - Other asymmetric elliptic curve key pairs - ``ECC_SECG_P256K1`` (secp256k1), commonly used for cryptocurrencies. - SM2 key pairs (China Regions only) - ``SM2`` Default: - "SYMMETRIC_DEFAULT"
        :param key_usage: Determines the `cryptographic operations <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#cryptographic-operations>`_ for which you can use the KMS key. The default value is ``ENCRYPT_DECRYPT`` . This property is required for asymmetric KMS keys and HMAC KMS keys. You can't change the ``KeyUsage`` value after the KMS key is created. .. epigraph:: If you change the value of the ``KeyUsage`` property on an existing KMS key, the update request fails, regardless of the value of the ```UpdateReplacePolicy`` attribute <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.html>`_ . This prevents you from accidentally deleting a KMS key by changing an immutable property value. Select only one valid value. - For symmetric encryption KMS keys, omit the property or specify ``ENCRYPT_DECRYPT`` . - For asymmetric KMS keys with RSA key material, specify ``ENCRYPT_DECRYPT`` or ``SIGN_VERIFY`` . - For asymmetric KMS keys with ECC key material, specify ``SIGN_VERIFY`` . - For asymmetric KMS keys with SM2 (China Regions only) key material, specify ``ENCRYPT_DECRYPT`` or ``SIGN_VERIFY`` . - For HMAC KMS keys, specify ``GENERATE_VERIFY_MAC`` . Default: - "ENCRYPT_DECRYPT"
        :param multi_region: Creates a multi-Region primary key that you can replicate in other AWS Regions . You can't change the ``MultiRegion`` value after the KMS key is created. For a list of AWS Regions in which multi-Region keys are supported, see `Multi-Region keys in AWS KMS <https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html>`_ in the ** . .. epigraph:: If you change the value of the ``MultiRegion`` property on an existing KMS key, the update request fails, regardless of the value of the ```UpdateReplacePolicy`` attribute <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.html>`_ . This prevents you from accidentally deleting a KMS key by changing an immutable property value. For a multi-Region key, set to this property to ``true`` . For a single-Region key, omit this property or set it to ``false`` . The default value is ``false`` . *Multi-Region keys* are an AWS KMS feature that lets you create multiple interoperable KMS keys in different AWS Regions . Because these KMS keys have the same key ID, key material, and other metadata, you can use them to encrypt data in one AWS Region and decrypt it in a different AWS Region without making a cross-Region call or exposing the plaintext data. For more information, see `Multi-Region keys <https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html>`_ in the *AWS Key Management Service Developer Guide* . You can create a symmetric encryption, HMAC, or asymmetric multi-Region KMS key, and you can create a multi-Region key with imported key material. However, you cannot create a multi-Region key in a custom key store. To create a replica of this primary key in a different AWS Region , create an `AWS::KMS::ReplicaKey <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-replicakey.html>`_ resource in a CloudFormation stack in the replica Region. Specify the key ARN of this primary key. Default: - false
        :param origin: The source of the key material for the KMS key. You cannot change the origin after you create the KMS key. The default is ``AWS_KMS`` , which means that AWS KMS creates the key material. To `create a KMS key with no key material <https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys-create-cmk.html>`_ (for imported key material), set this value to ``EXTERNAL`` . For more information about importing key material into AWS KMS , see `Importing Key Material <https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html>`_ in the *AWS Key Management Service Developer Guide* . You can ignore ``ENABLED`` when Origin is ``EXTERNAL`` . When a KMS key with Origin ``EXTERNAL`` is created, the key state is ``PENDING_IMPORT`` and ``ENABLED`` is ``false`` . After you import the key material, ``ENABLED`` updated to ``true`` . The KMS key can then be used for Cryptographic Operations. .. epigraph:: AWS CloudFormation doesn't support creating an ``Origin`` parameter of the ``AWS_CLOUDHSM`` or ``EXTERNAL_KEY_STORE`` values. Default: - "AWS_KMS"
        :param pending_window_in_days: Specifies the number of days in the waiting period before AWS KMS deletes a KMS key that has been removed from a CloudFormation stack. Enter a value between 7 and 30 days. The default value is 30 days. When you remove a KMS key from a CloudFormation stack, AWS KMS schedules the KMS key for deletion and starts the mandatory waiting period. The ``PendingWindowInDays`` property determines the length of waiting period. During the waiting period, the key state of KMS key is ``Pending Deletion`` or ``Pending Replica Deletion`` , which prevents the KMS key from being used in cryptographic operations. When the waiting period expires, AWS KMS permanently deletes the KMS key. AWS KMS will not delete a `multi-Region primary key <https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html>`_ that has replica keys. If you remove a multi-Region primary key from a CloudFormation stack, its key state changes to ``PendingReplicaDeletion`` so it cannot be replicated or used in cryptographic operations. This state can persist indefinitely. When the last of its replica keys is deleted, the key state of the primary key changes to ``PendingDeletion`` and the waiting period specified by ``PendingWindowInDays`` begins. When this waiting period expires, AWS KMS deletes the primary key. For details, see `Deleting multi-Region keys <https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-delete.html>`_ in the *AWS Key Management Service Developer Guide* . You cannot use a CloudFormation template to cancel deletion of the KMS key after you remove it from the stack, regardless of the waiting period. If you specify a KMS key in your template, even one with the same name, CloudFormation creates a new KMS key. To cancel deletion of a KMS key, use the AWS KMS console or the `CancelKeyDeletion <https://docs.aws.amazon.com/kms/latest/APIReference/API_CancelKeyDeletion.html>`_ operation. For information about the ``Pending Deletion`` and ``Pending Replica Deletion`` key states, see `Key state: Effect on your KMS key <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`_ in the *AWS Key Management Service Developer Guide* . For more information about deleting KMS keys, see the `ScheduleKeyDeletion <https://docs.aws.amazon.com/kms/latest/APIReference/API_ScheduleKeyDeletion.html>`_ operation in the *AWS Key Management Service API Reference* and `Deleting KMS keys <https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html>`_ in the *AWS Key Management Service Developer Guide* .
        :param rotation_period_in_days: Specifies a custom period of time between each rotation date. If no value is specified, the default value is 365 days. The rotation period defines the number of days after you enable automatic key rotation that AWS KMS will rotate your key material, and the number of days between each automatic rotation thereafter. You can use the ```kms:RotationPeriodInDays`` <https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-rotation-period-in-days>`_ condition key to further constrain the values that principals can specify in the ``RotationPeriodInDays`` parameter. For more information about rotating KMS keys and automatic rotation, see `Rotating keys <https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html>`_ in the *AWS Key Management Service Developer Guide* . Default: - 365
        :param tags: Assigns one or more tags to the replica key. .. epigraph:: Tagging or untagging a KMS key can allow or deny permission to the KMS key. For details, see `ABAC for AWS KMS <https://docs.aws.amazon.com/kms/latest/developerguide/abac.html>`_ in the *AWS Key Management Service Developer Guide* . For information about tags in AWS KMS , see `Tagging keys <https://docs.aws.amazon.com/kms/latest/developerguide/tagging-keys.html>`_ in the *AWS Key Management Service Developer Guide* . For information about tags in CloudFormation, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ea678e9e5a947601d16e5bb11fec3683fbb15bba768bee0b88be7e196d8783c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnKeyProps(
            bypass_policy_lockout_safety_check=bypass_policy_lockout_safety_check,
            description=description,
            enabled=enabled,
            enable_key_rotation=enable_key_rotation,
            key_policy=key_policy,
            key_spec=key_spec,
            key_usage=key_usage,
            multi_region=multi_region,
            origin=origin,
            pending_window_in_days=pending_window_in_days,
            rotation_period_in_days=rotation_period_in_days,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6311cde99d8265c1aa77cad19077d4dc11fa11a16a0a5d601158013e78b4de6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7468635e1eaf46c92748f2c14a3230215aa887e54ed03c370eee59b7ed05117b)
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
        '''The Amazon Resource Name (ARN) of the KMS key, such as ``arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`` .

        For information about the key ARN of a KMS key, see `Key ARN <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN>`_ in the *AWS Key Management Service Developer Guide* .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrKeyId")
    def attr_key_id(self) -> builtins.str:
        '''The key ID of the KMS key, such as ``1234abcd-12ab-34cd-56ef-1234567890ab`` .

        For information about the key ID of a KMS key, see `Key ID <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-id>`_ in the *AWS Key Management Service Developer Guide* .

        :cloudformationAttribute: KeyId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrKeyId"))

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
    @jsii.member(jsii_name="bypassPolicyLockoutSafetyCheck")
    def bypass_policy_lockout_safety_check(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Skips ("bypasses") the key policy lockout safety check.

        The default value is false.
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "bypassPolicyLockoutSafetyCheck"))

    @bypass_policy_lockout_safety_check.setter
    def bypass_policy_lockout_safety_check(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba782ca88c8b210d0c18f73ecee5e7266ed06b7428c903676aca9b26b6490443)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bypassPolicyLockoutSafetyCheck", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the KMS key.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01ec2bc212e875693eedcd62e8c0a2303fbbcbb0c0520e369d7b6372f89ba8ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the KMS key is enabled.

        Disabled KMS keys cannot be used in cryptographic operations.
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d16a27f134df94f3471ae307ddaf158320e92fc426e0a715a044c762a591e56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="enableKeyRotation")
    def enable_key_rotation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Enables automatic rotation of the key material for the specified KMS key.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enableKeyRotation"))

    @enable_key_rotation.setter
    def enable_key_rotation(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1949abfe35e26dd5174b35137bea94a550270331496fd2f865d63e22360c88de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableKeyRotation", value)

    @builtins.property
    @jsii.member(jsii_name="keyPolicy")
    def key_policy(self) -> typing.Any:
        '''The key policy to attach to the KMS key.'''
        return typing.cast(typing.Any, jsii.get(self, "keyPolicy"))

    @key_policy.setter
    def key_policy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd3f4724ca140c9b1dca16904dd53ab0905d0688de411b0f60d4f538cb2ac4a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="keySpec")
    def key_spec(self) -> typing.Optional[builtins.str]:
        '''Specifies the type of KMS key to create.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keySpec"))

    @key_spec.setter
    def key_spec(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00b8e7e0c6c26ba4d81ad2ec83a06ba02111a601de28c48a34e711a20bdb960d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keySpec", value)

    @builtins.property
    @jsii.member(jsii_name="keyUsage")
    def key_usage(self) -> typing.Optional[builtins.str]:
        '''Determines the `cryptographic operations <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#cryptographic-operations>`_ for which you can use the KMS key. The default value is ``ENCRYPT_DECRYPT`` . This property is required for asymmetric KMS keys and HMAC KMS keys. You can't change the ``KeyUsage`` value after the KMS key is created.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyUsage"))

    @key_usage.setter
    def key_usage(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3644201e513b7c747f1fac050f42c4761013ce447fd095d4670a875776c68562)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyUsage", value)

    @builtins.property
    @jsii.member(jsii_name="multiRegion")
    def multi_region(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Creates a multi-Region primary key that you can replicate in other AWS Regions .'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "multiRegion"))

    @multi_region.setter
    def multi_region(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a81f5a9d29ef2c8fdbd0a5b47659d6f998118db687737549f32e443f43446da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "multiRegion", value)

    @builtins.property
    @jsii.member(jsii_name="origin")
    def origin(self) -> typing.Optional[builtins.str]:
        '''The source of the key material for the KMS key.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "origin"))

    @origin.setter
    def origin(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e82f572625e8bbed987a6ede9a751d501f7398289c234e243ea2f716f23608b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "origin", value)

    @builtins.property
    @jsii.member(jsii_name="pendingWindowInDays")
    def pending_window_in_days(self) -> typing.Optional[jsii.Number]:
        '''Specifies the number of days in the waiting period before AWS KMS deletes a KMS key that has been removed from a CloudFormation stack.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "pendingWindowInDays"))

    @pending_window_in_days.setter
    def pending_window_in_days(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d3e524eda3827ec1d53e329afc207f3ef954caf7cf407b25faef721f3a2016d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pendingWindowInDays", value)

    @builtins.property
    @jsii.member(jsii_name="rotationPeriodInDays")
    def rotation_period_in_days(self) -> typing.Optional[jsii.Number]:
        '''Specifies a custom period of time between each rotation date.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rotationPeriodInDays"))

    @rotation_period_in_days.setter
    def rotation_period_in_days(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b766cb0a8ed53bed340510bfb429fb6a5f36d2f63f9c7718fb1f0c92f2fbc59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rotationPeriodInDays", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Assigns one or more tags to the replica key.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b85648b8166c62900697e128ab3a35c1360fdab37323145ed7b7c76dd91c4576)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_kms.CfnKeyProps",
    jsii_struct_bases=[],
    name_mapping={
        "bypass_policy_lockout_safety_check": "bypassPolicyLockoutSafetyCheck",
        "description": "description",
        "enabled": "enabled",
        "enable_key_rotation": "enableKeyRotation",
        "key_policy": "keyPolicy",
        "key_spec": "keySpec",
        "key_usage": "keyUsage",
        "multi_region": "multiRegion",
        "origin": "origin",
        "pending_window_in_days": "pendingWindowInDays",
        "rotation_period_in_days": "rotationPeriodInDays",
        "tags": "tags",
    },
)
class CfnKeyProps:
    def __init__(
        self,
        *,
        bypass_policy_lockout_safety_check: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        enable_key_rotation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        key_policy: typing.Any = None,
        key_spec: typing.Optional[builtins.str] = None,
        key_usage: typing.Optional[builtins.str] = None,
        multi_region: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        origin: typing.Optional[builtins.str] = None,
        pending_window_in_days: typing.Optional[jsii.Number] = None,
        rotation_period_in_days: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnKey``.

        :param bypass_policy_lockout_safety_check: Skips ("bypasses") the key policy lockout safety check. The default value is false. .. epigraph:: Setting this value to true increases the risk that the KMS key becomes unmanageable. Do not set this value to true indiscriminately. For more information, see `Default key policy <https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-default.html#prevent-unmanageable-key>`_ in the *AWS Key Management Service Developer Guide* . Use this parameter only when you intend to prevent the principal that is making the request from making a subsequent `PutKeyPolicy <https://docs.aws.amazon.com/kms/latest/APIReference/API_PutKeyPolicy.html>`_ request on the KMS key. Default: - false
        :param description: A description of the KMS key. Use a description that helps you to distinguish this KMS key from others in the account, such as its intended use.
        :param enabled: Specifies whether the KMS key is enabled. Disabled KMS keys cannot be used in cryptographic operations. When ``Enabled`` is ``true`` , the *key state* of the KMS key is ``Enabled`` . When ``Enabled`` is ``false`` , the key state of the KMS key is ``Disabled`` . The default value is ``true`` . The actual key state of the KMS key might be affected by actions taken outside of CloudFormation, such as running the `EnableKey <https://docs.aws.amazon.com/kms/latest/APIReference/API_EnableKey.html>`_ , `DisableKey <https://docs.aws.amazon.com/kms/latest/APIReference/API_DisableKey.html>`_ , or `ScheduleKeyDeletion <https://docs.aws.amazon.com/kms/latest/APIReference/API_ScheduleKeyDeletion.html>`_ operations. For information about the key states of a KMS key, see `Key state: Effect on your KMS key <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`_ in the *AWS Key Management Service Developer Guide* .
        :param enable_key_rotation: Enables automatic rotation of the key material for the specified KMS key. By default, automatic key rotation is not enabled. AWS KMS supports automatic rotation only for symmetric encryption KMS keys ( ``KeySpec`` = ``SYMMETRIC_DEFAULT`` ). For asymmetric KMS keys, HMAC KMS keys, and KMS keys with Origin ``EXTERNAL`` , omit the ``EnableKeyRotation`` property or set it to ``false`` . To enable automatic key rotation of the key material for a multi-Region KMS key, set ``EnableKeyRotation`` to ``true`` on the primary key (created by using ``AWS::KMS::Key`` ). AWS KMS copies the rotation status to all replica keys. For details, see `Rotating multi-Region keys <https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-manage.html#multi-region-rotate>`_ in the *AWS Key Management Service Developer Guide* . When you enable automatic rotation, AWS KMS automatically creates new key material for the KMS key one year after the enable date and every year thereafter. AWS KMS retains all key material until you delete the KMS key. For detailed information about automatic key rotation, see `Rotating KMS keys <https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html>`_ in the *AWS Key Management Service Developer Guide* .
        :param key_policy: The key policy to attach to the KMS key. If you provide a key policy, it must meet the following criteria: - The key policy must allow the caller to make a subsequent `PutKeyPolicy <https://docs.aws.amazon.com/kms/latest/APIReference/API_PutKeyPolicy.html>`_ request on the KMS key. This reduces the risk that the KMS key becomes unmanageable. For more information, see `Default key policy <https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default-allow-root-enable-iam>`_ in the *AWS Key Management Service Developer Guide* . (To omit this condition, set ``BypassPolicyLockoutSafetyCheck`` to true.) - Each statement in the key policy must contain one or more principals. The principals in the key policy must exist and be visible to AWS KMS . When you create a new AWS principal (for example, an IAM user or role), you might need to enforce a delay before including the new principal in a key policy because the new principal might not be immediately visible to AWS KMS . For more information, see `Changes that I make are not always immediately visible <https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_general.html#troubleshoot_general_eventual-consistency>`_ in the *AWS Identity and Access Management User Guide* . If you do not provide a key policy, AWS KMS attaches a default key policy to the KMS key. For more information, see `Default key policy <https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default>`_ in the *AWS Key Management Service Developer Guide* . A key policy document can include only the following characters: - Printable ASCII characters - Printable characters in the Basic Latin and Latin-1 Supplement character set - The tab ( ``\\u0009`` ), line feed ( ``\\u000A`` ), and carriage return ( ``\\u000D`` ) special characters *Minimum* : ``1`` *Maximum* : ``32768``
        :param key_spec: Specifies the type of KMS key to create. The default value, ``SYMMETRIC_DEFAULT`` , creates a KMS key with a 256-bit symmetric key for encryption and decryption. In China Regions, ``SYMMETRIC_DEFAULT`` creates a 128-bit symmetric key that uses SM4 encryption. You can't change the ``KeySpec`` value after the KMS key is created. For help choosing a key spec for your KMS key, see `Choosing a KMS key type <https://docs.aws.amazon.com/kms/latest/developerguide/symm-asymm-choose.html>`_ in the *AWS Key Management Service Developer Guide* . The ``KeySpec`` property determines the type of key material in the KMS key and the algorithms that the KMS key supports. To further restrict the algorithms that can be used with the KMS key, use a condition key in its key policy or IAM policy. For more information, see `AWS KMS condition keys <https://docs.aws.amazon.com/kms/latest/developerguide/policy-conditions.html#conditions-kms>`_ in the *AWS Key Management Service Developer Guide* . .. epigraph:: If you change the value of the ``KeySpec`` property on an existing KMS key, the update request fails, regardless of the value of the ```UpdateReplacePolicy`` attribute <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.html>`_ . This prevents you from accidentally deleting a KMS key by changing an immutable property value. > `AWS services that are integrated with AWS KMS <https://docs.aws.amazon.com/kms/features/#AWS_Service_Integration>`_ use symmetric encryption KMS keys to protect your data. These services do not support encryption with asymmetric KMS keys. For help determining whether a KMS key is asymmetric, see `Identifying asymmetric KMS keys <https://docs.aws.amazon.com/kms/latest/developerguide/find-symm-asymm.html>`_ in the *AWS Key Management Service Developer Guide* . AWS KMS supports the following key specs for KMS keys: - Symmetric encryption key (default) - ``SYMMETRIC_DEFAULT`` (AES-256-GCM) - HMAC keys (symmetric) - ``HMAC_224`` - ``HMAC_256`` - ``HMAC_384`` - ``HMAC_512`` - Asymmetric RSA key pairs - ``RSA_2048`` - ``RSA_3072`` - ``RSA_4096`` - Asymmetric NIST-recommended elliptic curve key pairs - ``ECC_NIST_P256`` (secp256r1) - ``ECC_NIST_P384`` (secp384r1) - ``ECC_NIST_P521`` (secp521r1) - Other asymmetric elliptic curve key pairs - ``ECC_SECG_P256K1`` (secp256k1), commonly used for cryptocurrencies. - SM2 key pairs (China Regions only) - ``SM2`` Default: - "SYMMETRIC_DEFAULT"
        :param key_usage: Determines the `cryptographic operations <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#cryptographic-operations>`_ for which you can use the KMS key. The default value is ``ENCRYPT_DECRYPT`` . This property is required for asymmetric KMS keys and HMAC KMS keys. You can't change the ``KeyUsage`` value after the KMS key is created. .. epigraph:: If you change the value of the ``KeyUsage`` property on an existing KMS key, the update request fails, regardless of the value of the ```UpdateReplacePolicy`` attribute <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.html>`_ . This prevents you from accidentally deleting a KMS key by changing an immutable property value. Select only one valid value. - For symmetric encryption KMS keys, omit the property or specify ``ENCRYPT_DECRYPT`` . - For asymmetric KMS keys with RSA key material, specify ``ENCRYPT_DECRYPT`` or ``SIGN_VERIFY`` . - For asymmetric KMS keys with ECC key material, specify ``SIGN_VERIFY`` . - For asymmetric KMS keys with SM2 (China Regions only) key material, specify ``ENCRYPT_DECRYPT`` or ``SIGN_VERIFY`` . - For HMAC KMS keys, specify ``GENERATE_VERIFY_MAC`` . Default: - "ENCRYPT_DECRYPT"
        :param multi_region: Creates a multi-Region primary key that you can replicate in other AWS Regions . You can't change the ``MultiRegion`` value after the KMS key is created. For a list of AWS Regions in which multi-Region keys are supported, see `Multi-Region keys in AWS KMS <https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html>`_ in the ** . .. epigraph:: If you change the value of the ``MultiRegion`` property on an existing KMS key, the update request fails, regardless of the value of the ```UpdateReplacePolicy`` attribute <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.html>`_ . This prevents you from accidentally deleting a KMS key by changing an immutable property value. For a multi-Region key, set to this property to ``true`` . For a single-Region key, omit this property or set it to ``false`` . The default value is ``false`` . *Multi-Region keys* are an AWS KMS feature that lets you create multiple interoperable KMS keys in different AWS Regions . Because these KMS keys have the same key ID, key material, and other metadata, you can use them to encrypt data in one AWS Region and decrypt it in a different AWS Region without making a cross-Region call or exposing the plaintext data. For more information, see `Multi-Region keys <https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html>`_ in the *AWS Key Management Service Developer Guide* . You can create a symmetric encryption, HMAC, or asymmetric multi-Region KMS key, and you can create a multi-Region key with imported key material. However, you cannot create a multi-Region key in a custom key store. To create a replica of this primary key in a different AWS Region , create an `AWS::KMS::ReplicaKey <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-replicakey.html>`_ resource in a CloudFormation stack in the replica Region. Specify the key ARN of this primary key. Default: - false
        :param origin: The source of the key material for the KMS key. You cannot change the origin after you create the KMS key. The default is ``AWS_KMS`` , which means that AWS KMS creates the key material. To `create a KMS key with no key material <https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys-create-cmk.html>`_ (for imported key material), set this value to ``EXTERNAL`` . For more information about importing key material into AWS KMS , see `Importing Key Material <https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html>`_ in the *AWS Key Management Service Developer Guide* . You can ignore ``ENABLED`` when Origin is ``EXTERNAL`` . When a KMS key with Origin ``EXTERNAL`` is created, the key state is ``PENDING_IMPORT`` and ``ENABLED`` is ``false`` . After you import the key material, ``ENABLED`` updated to ``true`` . The KMS key can then be used for Cryptographic Operations. .. epigraph:: AWS CloudFormation doesn't support creating an ``Origin`` parameter of the ``AWS_CLOUDHSM`` or ``EXTERNAL_KEY_STORE`` values. Default: - "AWS_KMS"
        :param pending_window_in_days: Specifies the number of days in the waiting period before AWS KMS deletes a KMS key that has been removed from a CloudFormation stack. Enter a value between 7 and 30 days. The default value is 30 days. When you remove a KMS key from a CloudFormation stack, AWS KMS schedules the KMS key for deletion and starts the mandatory waiting period. The ``PendingWindowInDays`` property determines the length of waiting period. During the waiting period, the key state of KMS key is ``Pending Deletion`` or ``Pending Replica Deletion`` , which prevents the KMS key from being used in cryptographic operations. When the waiting period expires, AWS KMS permanently deletes the KMS key. AWS KMS will not delete a `multi-Region primary key <https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html>`_ that has replica keys. If you remove a multi-Region primary key from a CloudFormation stack, its key state changes to ``PendingReplicaDeletion`` so it cannot be replicated or used in cryptographic operations. This state can persist indefinitely. When the last of its replica keys is deleted, the key state of the primary key changes to ``PendingDeletion`` and the waiting period specified by ``PendingWindowInDays`` begins. When this waiting period expires, AWS KMS deletes the primary key. For details, see `Deleting multi-Region keys <https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-delete.html>`_ in the *AWS Key Management Service Developer Guide* . You cannot use a CloudFormation template to cancel deletion of the KMS key after you remove it from the stack, regardless of the waiting period. If you specify a KMS key in your template, even one with the same name, CloudFormation creates a new KMS key. To cancel deletion of a KMS key, use the AWS KMS console or the `CancelKeyDeletion <https://docs.aws.amazon.com/kms/latest/APIReference/API_CancelKeyDeletion.html>`_ operation. For information about the ``Pending Deletion`` and ``Pending Replica Deletion`` key states, see `Key state: Effect on your KMS key <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`_ in the *AWS Key Management Service Developer Guide* . For more information about deleting KMS keys, see the `ScheduleKeyDeletion <https://docs.aws.amazon.com/kms/latest/APIReference/API_ScheduleKeyDeletion.html>`_ operation in the *AWS Key Management Service API Reference* and `Deleting KMS keys <https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html>`_ in the *AWS Key Management Service Developer Guide* .
        :param rotation_period_in_days: Specifies a custom period of time between each rotation date. If no value is specified, the default value is 365 days. The rotation period defines the number of days after you enable automatic key rotation that AWS KMS will rotate your key material, and the number of days between each automatic rotation thereafter. You can use the ```kms:RotationPeriodInDays`` <https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-rotation-period-in-days>`_ condition key to further constrain the values that principals can specify in the ``RotationPeriodInDays`` parameter. For more information about rotating KMS keys and automatic rotation, see `Rotating keys <https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html>`_ in the *AWS Key Management Service Developer Guide* . Default: - 365
        :param tags: Assigns one or more tags to the replica key. .. epigraph:: Tagging or untagging a KMS key can allow or deny permission to the KMS key. For details, see `ABAC for AWS KMS <https://docs.aws.amazon.com/kms/latest/developerguide/abac.html>`_ in the *AWS Key Management Service Developer Guide* . For information about tags in AWS KMS , see `Tagging keys <https://docs.aws.amazon.com/kms/latest/developerguide/tagging-keys.html>`_ in the *AWS Key Management Service Developer Guide* . For information about tags in CloudFormation, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_kms as kms
            
            # key_policy: Any
            
            cfn_key_props = kms.CfnKeyProps(
                bypass_policy_lockout_safety_check=False,
                description="description",
                enabled=False,
                enable_key_rotation=False,
                key_policy=key_policy,
                key_spec="keySpec",
                key_usage="keyUsage",
                multi_region=False,
                origin="origin",
                pending_window_in_days=123,
                rotation_period_in_days=123,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52751771c8b3e52917eaf0c78bad67c065fa3f95795e92f5eab3e92ce5051178)
            check_type(argname="argument bypass_policy_lockout_safety_check", value=bypass_policy_lockout_safety_check, expected_type=type_hints["bypass_policy_lockout_safety_check"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument enable_key_rotation", value=enable_key_rotation, expected_type=type_hints["enable_key_rotation"])
            check_type(argname="argument key_policy", value=key_policy, expected_type=type_hints["key_policy"])
            check_type(argname="argument key_spec", value=key_spec, expected_type=type_hints["key_spec"])
            check_type(argname="argument key_usage", value=key_usage, expected_type=type_hints["key_usage"])
            check_type(argname="argument multi_region", value=multi_region, expected_type=type_hints["multi_region"])
            check_type(argname="argument origin", value=origin, expected_type=type_hints["origin"])
            check_type(argname="argument pending_window_in_days", value=pending_window_in_days, expected_type=type_hints["pending_window_in_days"])
            check_type(argname="argument rotation_period_in_days", value=rotation_period_in_days, expected_type=type_hints["rotation_period_in_days"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bypass_policy_lockout_safety_check is not None:
            self._values["bypass_policy_lockout_safety_check"] = bypass_policy_lockout_safety_check
        if description is not None:
            self._values["description"] = description
        if enabled is not None:
            self._values["enabled"] = enabled
        if enable_key_rotation is not None:
            self._values["enable_key_rotation"] = enable_key_rotation
        if key_policy is not None:
            self._values["key_policy"] = key_policy
        if key_spec is not None:
            self._values["key_spec"] = key_spec
        if key_usage is not None:
            self._values["key_usage"] = key_usage
        if multi_region is not None:
            self._values["multi_region"] = multi_region
        if origin is not None:
            self._values["origin"] = origin
        if pending_window_in_days is not None:
            self._values["pending_window_in_days"] = pending_window_in_days
        if rotation_period_in_days is not None:
            self._values["rotation_period_in_days"] = rotation_period_in_days
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def bypass_policy_lockout_safety_check(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Skips ("bypasses") the key policy lockout safety check. The default value is false.

        .. epigraph::

           Setting this value to true increases the risk that the KMS key becomes unmanageable. Do not set this value to true indiscriminately.

           For more information, see `Default key policy <https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-default.html#prevent-unmanageable-key>`_ in the *AWS Key Management Service Developer Guide* .

        Use this parameter only when you intend to prevent the principal that is making the request from making a subsequent `PutKeyPolicy <https://docs.aws.amazon.com/kms/latest/APIReference/API_PutKeyPolicy.html>`_ request on the KMS key.

        :default: - false

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-bypasspolicylockoutsafetycheck
        '''
        result = self._values.get("bypass_policy_lockout_safety_check")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the KMS key.

        Use a description that helps you to distinguish this KMS key from others in the account, such as its intended use.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the KMS key is enabled. Disabled KMS keys cannot be used in cryptographic operations.

        When ``Enabled`` is ``true`` , the *key state* of the KMS key is ``Enabled`` . When ``Enabled`` is ``false`` , the key state of the KMS key is ``Disabled`` . The default value is ``true`` .

        The actual key state of the KMS key might be affected by actions taken outside of CloudFormation, such as running the `EnableKey <https://docs.aws.amazon.com/kms/latest/APIReference/API_EnableKey.html>`_ , `DisableKey <https://docs.aws.amazon.com/kms/latest/APIReference/API_DisableKey.html>`_ , or `ScheduleKeyDeletion <https://docs.aws.amazon.com/kms/latest/APIReference/API_ScheduleKeyDeletion.html>`_ operations.

        For information about the key states of a KMS key, see `Key state: Effect on your KMS key <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`_ in the *AWS Key Management Service Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def enable_key_rotation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Enables automatic rotation of the key material for the specified KMS key.

        By default, automatic key rotation is not enabled.

        AWS KMS supports automatic rotation only for symmetric encryption KMS keys ( ``KeySpec`` = ``SYMMETRIC_DEFAULT`` ). For asymmetric KMS keys, HMAC KMS keys, and KMS keys with Origin ``EXTERNAL`` , omit the ``EnableKeyRotation`` property or set it to ``false`` .

        To enable automatic key rotation of the key material for a multi-Region KMS key, set ``EnableKeyRotation`` to ``true`` on the primary key (created by using ``AWS::KMS::Key`` ). AWS KMS copies the rotation status to all replica keys. For details, see `Rotating multi-Region keys <https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-manage.html#multi-region-rotate>`_ in the *AWS Key Management Service Developer Guide* .

        When you enable automatic rotation, AWS KMS automatically creates new key material for the KMS key one year after the enable date and every year thereafter. AWS KMS retains all key material until you delete the KMS key. For detailed information about automatic key rotation, see `Rotating KMS keys <https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html>`_ in the *AWS Key Management Service Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-enablekeyrotation
        '''
        result = self._values.get("enable_key_rotation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def key_policy(self) -> typing.Any:
        '''The key policy to attach to the KMS key.

        If you provide a key policy, it must meet the following criteria:

        - The key policy must allow the caller to make a subsequent `PutKeyPolicy <https://docs.aws.amazon.com/kms/latest/APIReference/API_PutKeyPolicy.html>`_ request on the KMS key. This reduces the risk that the KMS key becomes unmanageable. For more information, see `Default key policy <https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default-allow-root-enable-iam>`_ in the *AWS Key Management Service Developer Guide* . (To omit this condition, set ``BypassPolicyLockoutSafetyCheck`` to true.)
        - Each statement in the key policy must contain one or more principals. The principals in the key policy must exist and be visible to AWS KMS . When you create a new AWS principal (for example, an IAM user or role), you might need to enforce a delay before including the new principal in a key policy because the new principal might not be immediately visible to AWS KMS . For more information, see `Changes that I make are not always immediately visible <https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_general.html#troubleshoot_general_eventual-consistency>`_ in the *AWS Identity and Access Management User Guide* .

        If you do not provide a key policy, AWS KMS attaches a default key policy to the KMS key. For more information, see `Default key policy <https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default>`_ in the *AWS Key Management Service Developer Guide* .

        A key policy document can include only the following characters:

        - Printable ASCII characters
        - Printable characters in the Basic Latin and Latin-1 Supplement character set
        - The tab ( ``\\u0009`` ), line feed ( ``\\u000A`` ), and carriage return ( ``\\u000D`` ) special characters

        *Minimum* : ``1``

        *Maximum* : ``32768``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-keypolicy
        '''
        result = self._values.get("key_policy")
        return typing.cast(typing.Any, result)

    @builtins.property
    def key_spec(self) -> typing.Optional[builtins.str]:
        '''Specifies the type of KMS key to create.

        The default value, ``SYMMETRIC_DEFAULT`` , creates a KMS key with a 256-bit symmetric key for encryption and decryption. In China Regions, ``SYMMETRIC_DEFAULT`` creates a 128-bit symmetric key that uses SM4 encryption. You can't change the ``KeySpec`` value after the KMS key is created. For help choosing a key spec for your KMS key, see `Choosing a KMS key type <https://docs.aws.amazon.com/kms/latest/developerguide/symm-asymm-choose.html>`_ in the *AWS Key Management Service Developer Guide* .

        The ``KeySpec`` property determines the type of key material in the KMS key and the algorithms that the KMS key supports. To further restrict the algorithms that can be used with the KMS key, use a condition key in its key policy or IAM policy. For more information, see `AWS KMS condition keys <https://docs.aws.amazon.com/kms/latest/developerguide/policy-conditions.html#conditions-kms>`_ in the *AWS Key Management Service Developer Guide* .
        .. epigraph::

           If you change the value of the ``KeySpec`` property on an existing KMS key, the update request fails, regardless of the value of the ```UpdateReplacePolicy`` attribute <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.html>`_ . This prevents you from accidentally deleting a KMS key by changing an immutable property value. > `AWS services that are integrated with AWS KMS <https://docs.aws.amazon.com/kms/features/#AWS_Service_Integration>`_ use symmetric encryption KMS keys to protect your data. These services do not support encryption with asymmetric KMS keys. For help determining whether a KMS key is asymmetric, see `Identifying asymmetric KMS keys <https://docs.aws.amazon.com/kms/latest/developerguide/find-symm-asymm.html>`_ in the *AWS Key Management Service Developer Guide* .

        AWS KMS supports the following key specs for KMS keys:

        - Symmetric encryption key (default)
        - ``SYMMETRIC_DEFAULT`` (AES-256-GCM)
        - HMAC keys (symmetric)
        - ``HMAC_224``
        - ``HMAC_256``
        - ``HMAC_384``
        - ``HMAC_512``
        - Asymmetric RSA key pairs
        - ``RSA_2048``
        - ``RSA_3072``
        - ``RSA_4096``
        - Asymmetric NIST-recommended elliptic curve key pairs
        - ``ECC_NIST_P256`` (secp256r1)
        - ``ECC_NIST_P384`` (secp384r1)
        - ``ECC_NIST_P521`` (secp521r1)
        - Other asymmetric elliptic curve key pairs
        - ``ECC_SECG_P256K1`` (secp256k1), commonly used for cryptocurrencies.
        - SM2 key pairs (China Regions only)
        - ``SM2``

        :default: - "SYMMETRIC_DEFAULT"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-keyspec
        '''
        result = self._values.get("key_spec")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_usage(self) -> typing.Optional[builtins.str]:
        '''Determines the `cryptographic operations <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#cryptographic-operations>`_ for which you can use the KMS key. The default value is ``ENCRYPT_DECRYPT`` . This property is required for asymmetric KMS keys and HMAC KMS keys. You can't change the ``KeyUsage`` value after the KMS key is created.

        .. epigraph::

           If you change the value of the ``KeyUsage`` property on an existing KMS key, the update request fails, regardless of the value of the ```UpdateReplacePolicy`` attribute <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.html>`_ . This prevents you from accidentally deleting a KMS key by changing an immutable property value.

        Select only one valid value.

        - For symmetric encryption KMS keys, omit the property or specify ``ENCRYPT_DECRYPT`` .
        - For asymmetric KMS keys with RSA key material, specify ``ENCRYPT_DECRYPT`` or ``SIGN_VERIFY`` .
        - For asymmetric KMS keys with ECC key material, specify ``SIGN_VERIFY`` .
        - For asymmetric KMS keys with SM2 (China Regions only) key material, specify ``ENCRYPT_DECRYPT`` or ``SIGN_VERIFY`` .
        - For HMAC KMS keys, specify ``GENERATE_VERIFY_MAC`` .

        :default: - "ENCRYPT_DECRYPT"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-keyusage
        '''
        result = self._values.get("key_usage")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def multi_region(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Creates a multi-Region primary key that you can replicate in other AWS Regions .

        You can't change the ``MultiRegion`` value after the KMS key is created.

        For a list of AWS Regions in which multi-Region keys are supported, see `Multi-Region keys in AWS KMS <https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html>`_ in the ** .
        .. epigraph::

           If you change the value of the ``MultiRegion`` property on an existing KMS key, the update request fails, regardless of the value of the ```UpdateReplacePolicy`` attribute <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.html>`_ . This prevents you from accidentally deleting a KMS key by changing an immutable property value.

        For a multi-Region key, set to this property to ``true`` . For a single-Region key, omit this property or set it to ``false`` . The default value is ``false`` .

        *Multi-Region keys* are an AWS KMS feature that lets you create multiple interoperable KMS keys in different AWS Regions . Because these KMS keys have the same key ID, key material, and other metadata, you can use them to encrypt data in one AWS Region and decrypt it in a different AWS Region without making a cross-Region call or exposing the plaintext data. For more information, see `Multi-Region keys <https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html>`_ in the *AWS Key Management Service Developer Guide* .

        You can create a symmetric encryption, HMAC, or asymmetric multi-Region KMS key, and you can create a multi-Region key with imported key material. However, you cannot create a multi-Region key in a custom key store.

        To create a replica of this primary key in a different AWS Region , create an `AWS::KMS::ReplicaKey <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-replicakey.html>`_ resource in a CloudFormation stack in the replica Region. Specify the key ARN of this primary key.

        :default: - false

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-multiregion
        '''
        result = self._values.get("multi_region")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def origin(self) -> typing.Optional[builtins.str]:
        '''The source of the key material for the KMS key.

        You cannot change the origin after you create the KMS key. The default is ``AWS_KMS`` , which means that AWS KMS creates the key material.

        To `create a KMS key with no key material <https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys-create-cmk.html>`_ (for imported key material), set this value to ``EXTERNAL`` . For more information about importing key material into AWS KMS , see `Importing Key Material <https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html>`_ in the *AWS Key Management Service Developer Guide* .

        You can ignore ``ENABLED`` when Origin is ``EXTERNAL`` . When a KMS key with Origin ``EXTERNAL`` is created, the key state is ``PENDING_IMPORT`` and ``ENABLED`` is ``false`` . After you import the key material, ``ENABLED`` updated to ``true`` . The KMS key can then be used for Cryptographic Operations.
        .. epigraph::

           AWS CloudFormation doesn't support creating an ``Origin`` parameter of the ``AWS_CLOUDHSM`` or ``EXTERNAL_KEY_STORE`` values.

        :default: - "AWS_KMS"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-origin
        '''
        result = self._values.get("origin")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pending_window_in_days(self) -> typing.Optional[jsii.Number]:
        '''Specifies the number of days in the waiting period before AWS KMS deletes a KMS key that has been removed from a CloudFormation stack.

        Enter a value between 7 and 30 days. The default value is 30 days.

        When you remove a KMS key from a CloudFormation stack, AWS KMS schedules the KMS key for deletion and starts the mandatory waiting period. The ``PendingWindowInDays`` property determines the length of waiting period. During the waiting period, the key state of KMS key is ``Pending Deletion`` or ``Pending Replica Deletion`` , which prevents the KMS key from being used in cryptographic operations. When the waiting period expires, AWS KMS permanently deletes the KMS key.

        AWS KMS will not delete a `multi-Region primary key <https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html>`_ that has replica keys. If you remove a multi-Region primary key from a CloudFormation stack, its key state changes to ``PendingReplicaDeletion`` so it cannot be replicated or used in cryptographic operations. This state can persist indefinitely. When the last of its replica keys is deleted, the key state of the primary key changes to ``PendingDeletion`` and the waiting period specified by ``PendingWindowInDays`` begins. When this waiting period expires, AWS KMS deletes the primary key. For details, see `Deleting multi-Region keys <https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-delete.html>`_ in the *AWS Key Management Service Developer Guide* .

        You cannot use a CloudFormation template to cancel deletion of the KMS key after you remove it from the stack, regardless of the waiting period. If you specify a KMS key in your template, even one with the same name, CloudFormation creates a new KMS key. To cancel deletion of a KMS key, use the AWS KMS console or the `CancelKeyDeletion <https://docs.aws.amazon.com/kms/latest/APIReference/API_CancelKeyDeletion.html>`_ operation.

        For information about the ``Pending Deletion`` and ``Pending Replica Deletion`` key states, see `Key state: Effect on your KMS key <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`_ in the *AWS Key Management Service Developer Guide* . For more information about deleting KMS keys, see the `ScheduleKeyDeletion <https://docs.aws.amazon.com/kms/latest/APIReference/API_ScheduleKeyDeletion.html>`_ operation in the *AWS Key Management Service API Reference* and `Deleting KMS keys <https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html>`_ in the *AWS Key Management Service Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-pendingwindowindays
        '''
        result = self._values.get("pending_window_in_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def rotation_period_in_days(self) -> typing.Optional[jsii.Number]:
        '''Specifies a custom period of time between each rotation date.

        If no value is specified, the default value is 365 days.

        The rotation period defines the number of days after you enable automatic key rotation that AWS KMS will rotate your key material, and the number of days between each automatic rotation thereafter.

        You can use the ```kms:RotationPeriodInDays`` <https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-rotation-period-in-days>`_ condition key to further constrain the values that principals can specify in the ``RotationPeriodInDays`` parameter.

        For more information about rotating KMS keys and automatic rotation, see `Rotating keys <https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html>`_ in the *AWS Key Management Service Developer Guide* .

        :default: - 365

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-rotationperiodindays
        '''
        result = self._values.get("rotation_period_in_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Assigns one or more tags to the replica key.

        .. epigraph::

           Tagging or untagging a KMS key can allow or deny permission to the KMS key. For details, see `ABAC for AWS KMS <https://docs.aws.amazon.com/kms/latest/developerguide/abac.html>`_ in the *AWS Key Management Service Developer Guide* .

        For information about tags in AWS KMS , see `Tagging keys <https://docs.aws.amazon.com/kms/latest/developerguide/tagging-keys.html>`_ in the *AWS Key Management Service Developer Guide* . For information about tags in CloudFormation, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKeyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnReplicaKey(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_kms.CfnReplicaKey",
):
    '''The ``AWS::KMS::ReplicaKey`` resource specifies a multi-Region replica key that is based on a multi-Region primary key.

    *Multi-Region keys* are an AWS KMS feature that lets you create multiple interoperable KMS keys in different AWS Regions . Because these KMS keys have the same key ID, key material, and other metadata, you can use them to encrypt data in one AWS Region and decrypt it in a different AWS Region without making a cross-Region call or exposing the plaintext data. For more information, see `Multi-Region keys <https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html>`_ in the *AWS Key Management Service Developer Guide* .

    A multi-Region *primary key* is a fully functional symmetric encryption KMS key, HMAC KMS key, or asymmetric KMS key that is also the model for replica keys in other AWS Regions . To create a multi-Region primary key, add an `AWS::KMS::Key <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html>`_ resource to your CloudFormation stack. Set its ``MultiRegion`` property to true.

    A multi-Region *replica key* is a fully functional KMS key that has the same key ID and key material as a multi-Region primary key, but is located in a different AWS Region of the same AWS partition. There can be multiple replicas of a primary key, but each must be in a different AWS Region .

    When you create a replica key in AWS CloudFormation , the replica key is created in the AWS Region represented by the endpoint you use for the request. If you try to replicate a multi-Region key into a Region in which the key type is not supported, the request will fail.

    A primary key and its replicas have the same key ID and key material. They also have the same key spec, key usage, key material origin, and automatic key rotation status. These properties are known as *shared properties* . If they change, AWS KMS synchronizes the change to all related multi-Region keys. All other properties of a replica key can differ, including its key policy, tags, aliases, and key state. AWS KMS does not synchronize these properties.

    *Regions*

    AWS KMS CloudFormation resources are available in all AWS Regions in which AWS KMS and AWS CloudFormation are supported. You can use the ``AWS::KMS::ReplicaKey`` resource to create replica keys in all Regions that support multi-Region KMS keys. For details, see `Multi-Region keys in AWS KMS <https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html>`_ in the ** .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-replicakey.html
    :cloudformationResource: AWS::KMS::ReplicaKey
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_kms as kms
        
        # key_policy: Any
        
        cfn_replica_key = kms.CfnReplicaKey(self, "MyCfnReplicaKey",
            key_policy=key_policy,
            primary_key_arn="primaryKeyArn",
        
            # the properties below are optional
            description="description",
            enabled=False,
            pending_window_in_days=123,
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
        key_policy: typing.Any,
        primary_key_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        pending_window_in_days: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param key_policy: The key policy that authorizes use of the replica key. The key policy is not a shared property of multi-Region keys. You can specify the same key policy or a different key policy for each key in a set of related multi-Region keys. AWS KMS does not synchronize this property. The key policy must conform to the following rules. - The key policy must give the caller `PutKeyPolicy <https://docs.aws.amazon.com/kms/latest/APIReference/API_PutKeyPolicy.html>`_ permission on the KMS key. This reduces the risk that the KMS key becomes unmanageable. For more information, refer to the scenario in the `Default key policy <https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default-allow-root-enable-iam>`_ section of the **AWS Key Management Service Developer Guide** . - Each statement in the key policy must contain one or more principals. The principals in the key policy must exist and be visible to AWS KMS . When you create a new AWS principal (for example, an IAM user or role), you might need to enforce a delay before including the new principal in a key policy because the new principal might not be immediately visible to AWS KMS . For more information, see `Changes that I make are not always immediately visible <https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_general.html#troubleshoot_general_eventual-consistency>`_ in the *AWS Identity and Access Management User Guide* . A key policy document can include only the following characters: - Printable ASCII characters from the space character ( ``\\u0020`` ) through the end of the ASCII character range. - Printable characters in the Basic Latin and Latin-1 Supplement character set (through ``\\u00FF`` ). - The tab ( ``\\u0009`` ), line feed ( ``\\u000A`` ), and carriage return ( ``\\u000D`` ) special characters *Minimum* : ``1`` *Maximum* : ``32768``
        :param primary_key_arn: Specifies the multi-Region primary key to replicate. The primary key must be in a different AWS Region of the same AWS partition. You can create only one replica of a given primary key in each AWS Region . .. epigraph:: If you change the ``PrimaryKeyArn`` value of a replica key, the existing replica key is scheduled for deletion and a new replica key is created based on the specified primary key. While it is scheduled for deletion, the existing replica key becomes unusable. You can cancel the scheduled deletion of the key outside of CloudFormation. However, if you inadvertently delete a replica key, you can decrypt ciphertext encrypted by that replica key by using any related multi-Region key. If necessary, you can recreate the replica in the same Region after the previous one is completely deleted. For details, see `Deleting multi-Region keys <https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-delete.html>`_ in the *AWS Key Management Service Developer Guide* Specify the key ARN of an existing multi-Region primary key. For example, ``arn:aws:kms:us-east-2:111122223333:key/mrk-1234abcd12ab34cd56ef1234567890ab`` .
        :param description: A description of the KMS key. The default value is an empty string (no description). The description is not a shared property of multi-Region keys. You can specify the same description or a different description for each key in a set of related multi-Region keys. AWS Key Management Service does not synchronize this property.
        :param enabled: Specifies whether the replica key is enabled. Disabled KMS keys cannot be used in cryptographic operations. When ``Enabled`` is ``true`` , the *key state* of the KMS key is ``Enabled`` . When ``Enabled`` is ``false`` , the key state of the KMS key is ``Disabled`` . The default value is ``true`` . The actual key state of the replica might be affected by actions taken outside of CloudFormation, such as running the `EnableKey <https://docs.aws.amazon.com/kms/latest/APIReference/API_EnableKey.html>`_ , `DisableKey <https://docs.aws.amazon.com/kms/latest/APIReference/API_DisableKey.html>`_ , or `ScheduleKeyDeletion <https://docs.aws.amazon.com/kms/latest/APIReference/API_ScheduleKeyDeletion.html>`_ operations. Also, while the replica key is being created, its key state is ``Creating`` . When the process is complete, the key state of the replica key changes to ``Enabled`` . For information about the key states of a KMS key, see `Key state: Effect on your KMS key <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`_ in the *AWS Key Management Service Developer Guide* .
        :param pending_window_in_days: Specifies the number of days in the waiting period before AWS KMS deletes a replica key that has been removed from a CloudFormation stack. Enter a value between 7 and 30 days. The default value is 30 days. When you remove a replica key from a CloudFormation stack, AWS KMS schedules the replica key for deletion and starts the mandatory waiting period. The ``PendingWindowInDays`` property determines the length of waiting period. During the waiting period, the key state of replica key is ``Pending Deletion`` , which prevents it from being used in cryptographic operations. When the waiting period expires, AWS KMS permanently deletes the replica key. If the KMS key is a multi-Region primary key with replica keys, the waiting period begins when the last of its replica keys is deleted. Otherwise, the waiting period begins immediately. You cannot use a CloudFormation template to cancel deletion of the replica after you remove it from the stack, regardless of the waiting period. However, if you specify a replica key in your template that is based on the same primary key as the original replica key, CloudFormation creates a new replica key with the same key ID, key material, and other shared properties of the original replica key. This new replica key can decrypt ciphertext that was encrypted under the original replica key, or any related multi-Region key. For detailed information about deleting multi-Region keys, see `Deleting multi-Region keys <https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-delete.html>`_ in the *AWS Key Management Service Developer Guide* . For information about the ``PendingDeletion`` key state, see `Key state: Effect on your KMS key <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`_ in the *AWS Key Management Service Developer Guide* . For more information about deleting KMS keys, see the `ScheduleKeyDeletion <https://docs.aws.amazon.com/kms/latest/APIReference/API_ScheduleKeyDeletion.html>`_ operation in the *AWS Key Management Service API Reference* and `Deleting KMS keys <https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html>`_ in the *AWS Key Management Service Developer Guide* .
        :param tags: Assigns one or more tags to the replica key. .. epigraph:: Tagging or untagging a KMS key can allow or deny permission to the KMS key. For details, see `ABAC for AWS KMS <https://docs.aws.amazon.com/kms/latest/developerguide/abac.html>`_ in the *AWS Key Management Service Developer Guide* . Tags are not a shared property of multi-Region keys. You can specify the same tags or different tags for each key in a set of related multi-Region keys. AWS KMS does not synchronize this property. Each tag consists of a tag key and a tag value. Both the tag key and the tag value are required, but the tag value can be an empty (null) string. You cannot have more than one tag on a KMS key with the same tag key. If you specify an existing tag key with a different tag value, AWS KMS replaces the current tag value with the specified one. When you assign tags to an AWS resource, AWS generates a cost allocation report with usage and costs aggregated by tags. Tags can also be used to control access to a KMS key. For details, see `Tagging keys <https://docs.aws.amazon.com/kms/latest/developerguide/tagging-keys.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a43b13aecc4a6c9b9c5cce2bd96d2ececdc7c64b21c374cf96c4ab5ead30546b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnReplicaKeyProps(
            key_policy=key_policy,
            primary_key_arn=primary_key_arn,
            description=description,
            enabled=enabled,
            pending_window_in_days=pending_window_in_days,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e24eab003d1d7413d435432417d9c001c3be699c66c07b278b9d5cb7ab69fec)
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
            type_hints = typing.get_type_hints(_typecheckingstub__506b80402bbe68662639797e0c6aabbb40195789ec9827424d8c8b8a760fa7c3)
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
        '''The Amazon Resource Name (ARN) of the replica key, such as ``arn:aws:kms:us-west-2:111122223333:key/mrk-1234abcd12ab34cd56ef1234567890ab`` .

        The key ARNs of related multi-Region keys differ only in the Region value. For information about the key ARNs of multi-Region keys, see `How multi-Region keys work <https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html#mrk-how-it-works>`_ in the *AWS Key Management Service Developer Guide* .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrKeyId")
    def attr_key_id(self) -> builtins.str:
        '''The key ID of the replica key, such as ``mrk-1234abcd12ab34cd56ef1234567890ab`` .

        Related multi-Region keys have the same key ID. For information about the key IDs of multi-Region keys, see `How multi-Region keys work <https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html#mrk-how-it-works>`_ in the *AWS Key Management Service Developer Guide* .

        :cloudformationAttribute: KeyId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrKeyId"))

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
    @jsii.member(jsii_name="keyPolicy")
    def key_policy(self) -> typing.Any:
        '''The key policy that authorizes use of the replica key.'''
        return typing.cast(typing.Any, jsii.get(self, "keyPolicy"))

    @key_policy.setter
    def key_policy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54fc1b22cb7e48927490c2ff73a5afea9bb5bb4dd8e62a2a6f805d4bb26f967d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="primaryKeyArn")
    def primary_key_arn(self) -> builtins.str:
        '''Specifies the multi-Region primary key to replicate.'''
        return typing.cast(builtins.str, jsii.get(self, "primaryKeyArn"))

    @primary_key_arn.setter
    def primary_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15fbb1b757e713b4a793995a5eb68370a6a6f742705620d66815b734fa8b2547)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the KMS key.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__416fb26a5b9f08dd98d1c61865eacaf89a14839e250c7f61ec3485d272103112)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the replica key is enabled.

        Disabled KMS keys cannot be used in cryptographic operations.
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb76d39656831fe315be03ed1109d35bd47e49d418dd22bdc531e5665db1e4c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="pendingWindowInDays")
    def pending_window_in_days(self) -> typing.Optional[jsii.Number]:
        '''Specifies the number of days in the waiting period before AWS KMS deletes a replica key that has been removed from a CloudFormation stack.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "pendingWindowInDays"))

    @pending_window_in_days.setter
    def pending_window_in_days(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42cf7563707cf3efe01d1caeaa2ca0405b68188335ff4068637d0baa84d85621)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pendingWindowInDays", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Assigns one or more tags to the replica key.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc49d1ede5bfd6f35a0c93dafce91a41f79d39c2119895fac0fb0749478472b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_kms.CfnReplicaKeyProps",
    jsii_struct_bases=[],
    name_mapping={
        "key_policy": "keyPolicy",
        "primary_key_arn": "primaryKeyArn",
        "description": "description",
        "enabled": "enabled",
        "pending_window_in_days": "pendingWindowInDays",
        "tags": "tags",
    },
)
class CfnReplicaKeyProps:
    def __init__(
        self,
        *,
        key_policy: typing.Any,
        primary_key_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        pending_window_in_days: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnReplicaKey``.

        :param key_policy: The key policy that authorizes use of the replica key. The key policy is not a shared property of multi-Region keys. You can specify the same key policy or a different key policy for each key in a set of related multi-Region keys. AWS KMS does not synchronize this property. The key policy must conform to the following rules. - The key policy must give the caller `PutKeyPolicy <https://docs.aws.amazon.com/kms/latest/APIReference/API_PutKeyPolicy.html>`_ permission on the KMS key. This reduces the risk that the KMS key becomes unmanageable. For more information, refer to the scenario in the `Default key policy <https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default-allow-root-enable-iam>`_ section of the **AWS Key Management Service Developer Guide** . - Each statement in the key policy must contain one or more principals. The principals in the key policy must exist and be visible to AWS KMS . When you create a new AWS principal (for example, an IAM user or role), you might need to enforce a delay before including the new principal in a key policy because the new principal might not be immediately visible to AWS KMS . For more information, see `Changes that I make are not always immediately visible <https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_general.html#troubleshoot_general_eventual-consistency>`_ in the *AWS Identity and Access Management User Guide* . A key policy document can include only the following characters: - Printable ASCII characters from the space character ( ``\\u0020`` ) through the end of the ASCII character range. - Printable characters in the Basic Latin and Latin-1 Supplement character set (through ``\\u00FF`` ). - The tab ( ``\\u0009`` ), line feed ( ``\\u000A`` ), and carriage return ( ``\\u000D`` ) special characters *Minimum* : ``1`` *Maximum* : ``32768``
        :param primary_key_arn: Specifies the multi-Region primary key to replicate. The primary key must be in a different AWS Region of the same AWS partition. You can create only one replica of a given primary key in each AWS Region . .. epigraph:: If you change the ``PrimaryKeyArn`` value of a replica key, the existing replica key is scheduled for deletion and a new replica key is created based on the specified primary key. While it is scheduled for deletion, the existing replica key becomes unusable. You can cancel the scheduled deletion of the key outside of CloudFormation. However, if you inadvertently delete a replica key, you can decrypt ciphertext encrypted by that replica key by using any related multi-Region key. If necessary, you can recreate the replica in the same Region after the previous one is completely deleted. For details, see `Deleting multi-Region keys <https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-delete.html>`_ in the *AWS Key Management Service Developer Guide* Specify the key ARN of an existing multi-Region primary key. For example, ``arn:aws:kms:us-east-2:111122223333:key/mrk-1234abcd12ab34cd56ef1234567890ab`` .
        :param description: A description of the KMS key. The default value is an empty string (no description). The description is not a shared property of multi-Region keys. You can specify the same description or a different description for each key in a set of related multi-Region keys. AWS Key Management Service does not synchronize this property.
        :param enabled: Specifies whether the replica key is enabled. Disabled KMS keys cannot be used in cryptographic operations. When ``Enabled`` is ``true`` , the *key state* of the KMS key is ``Enabled`` . When ``Enabled`` is ``false`` , the key state of the KMS key is ``Disabled`` . The default value is ``true`` . The actual key state of the replica might be affected by actions taken outside of CloudFormation, such as running the `EnableKey <https://docs.aws.amazon.com/kms/latest/APIReference/API_EnableKey.html>`_ , `DisableKey <https://docs.aws.amazon.com/kms/latest/APIReference/API_DisableKey.html>`_ , or `ScheduleKeyDeletion <https://docs.aws.amazon.com/kms/latest/APIReference/API_ScheduleKeyDeletion.html>`_ operations. Also, while the replica key is being created, its key state is ``Creating`` . When the process is complete, the key state of the replica key changes to ``Enabled`` . For information about the key states of a KMS key, see `Key state: Effect on your KMS key <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`_ in the *AWS Key Management Service Developer Guide* .
        :param pending_window_in_days: Specifies the number of days in the waiting period before AWS KMS deletes a replica key that has been removed from a CloudFormation stack. Enter a value between 7 and 30 days. The default value is 30 days. When you remove a replica key from a CloudFormation stack, AWS KMS schedules the replica key for deletion and starts the mandatory waiting period. The ``PendingWindowInDays`` property determines the length of waiting period. During the waiting period, the key state of replica key is ``Pending Deletion`` , which prevents it from being used in cryptographic operations. When the waiting period expires, AWS KMS permanently deletes the replica key. If the KMS key is a multi-Region primary key with replica keys, the waiting period begins when the last of its replica keys is deleted. Otherwise, the waiting period begins immediately. You cannot use a CloudFormation template to cancel deletion of the replica after you remove it from the stack, regardless of the waiting period. However, if you specify a replica key in your template that is based on the same primary key as the original replica key, CloudFormation creates a new replica key with the same key ID, key material, and other shared properties of the original replica key. This new replica key can decrypt ciphertext that was encrypted under the original replica key, or any related multi-Region key. For detailed information about deleting multi-Region keys, see `Deleting multi-Region keys <https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-delete.html>`_ in the *AWS Key Management Service Developer Guide* . For information about the ``PendingDeletion`` key state, see `Key state: Effect on your KMS key <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`_ in the *AWS Key Management Service Developer Guide* . For more information about deleting KMS keys, see the `ScheduleKeyDeletion <https://docs.aws.amazon.com/kms/latest/APIReference/API_ScheduleKeyDeletion.html>`_ operation in the *AWS Key Management Service API Reference* and `Deleting KMS keys <https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html>`_ in the *AWS Key Management Service Developer Guide* .
        :param tags: Assigns one or more tags to the replica key. .. epigraph:: Tagging or untagging a KMS key can allow or deny permission to the KMS key. For details, see `ABAC for AWS KMS <https://docs.aws.amazon.com/kms/latest/developerguide/abac.html>`_ in the *AWS Key Management Service Developer Guide* . Tags are not a shared property of multi-Region keys. You can specify the same tags or different tags for each key in a set of related multi-Region keys. AWS KMS does not synchronize this property. Each tag consists of a tag key and a tag value. Both the tag key and the tag value are required, but the tag value can be an empty (null) string. You cannot have more than one tag on a KMS key with the same tag key. If you specify an existing tag key with a different tag value, AWS KMS replaces the current tag value with the specified one. When you assign tags to an AWS resource, AWS generates a cost allocation report with usage and costs aggregated by tags. Tags can also be used to control access to a KMS key. For details, see `Tagging keys <https://docs.aws.amazon.com/kms/latest/developerguide/tagging-keys.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-replicakey.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_kms as kms
            
            # key_policy: Any
            
            cfn_replica_key_props = kms.CfnReplicaKeyProps(
                key_policy=key_policy,
                primary_key_arn="primaryKeyArn",
            
                # the properties below are optional
                description="description",
                enabled=False,
                pending_window_in_days=123,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e439eab3a0ecab69adc7fd26c12adbbe28fdefe26f6d89d9b6429b95ea8ffb03)
            check_type(argname="argument key_policy", value=key_policy, expected_type=type_hints["key_policy"])
            check_type(argname="argument primary_key_arn", value=primary_key_arn, expected_type=type_hints["primary_key_arn"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument pending_window_in_days", value=pending_window_in_days, expected_type=type_hints["pending_window_in_days"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key_policy": key_policy,
            "primary_key_arn": primary_key_arn,
        }
        if description is not None:
            self._values["description"] = description
        if enabled is not None:
            self._values["enabled"] = enabled
        if pending_window_in_days is not None:
            self._values["pending_window_in_days"] = pending_window_in_days
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def key_policy(self) -> typing.Any:
        '''The key policy that authorizes use of the replica key.

        The key policy is not a shared property of multi-Region keys. You can specify the same key policy or a different key policy for each key in a set of related multi-Region keys. AWS KMS does not synchronize this property.

        The key policy must conform to the following rules.

        - The key policy must give the caller `PutKeyPolicy <https://docs.aws.amazon.com/kms/latest/APIReference/API_PutKeyPolicy.html>`_ permission on the KMS key. This reduces the risk that the KMS key becomes unmanageable. For more information, refer to the scenario in the `Default key policy <https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default-allow-root-enable-iam>`_ section of the **AWS Key Management Service Developer Guide** .
        - Each statement in the key policy must contain one or more principals. The principals in the key policy must exist and be visible to AWS KMS . When you create a new AWS principal (for example, an IAM user or role), you might need to enforce a delay before including the new principal in a key policy because the new principal might not be immediately visible to AWS KMS . For more information, see `Changes that I make are not always immediately visible <https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_general.html#troubleshoot_general_eventual-consistency>`_ in the *AWS Identity and Access Management User Guide* .

        A key policy document can include only the following characters:

        - Printable ASCII characters from the space character ( ``\\u0020`` ) through the end of the ASCII character range.
        - Printable characters in the Basic Latin and Latin-1 Supplement character set (through ``\\u00FF`` ).
        - The tab ( ``\\u0009`` ), line feed ( ``\\u000A`` ), and carriage return ( ``\\u000D`` ) special characters

        *Minimum* : ``1``

        *Maximum* : ``32768``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-replicakey.html#cfn-kms-replicakey-keypolicy
        '''
        result = self._values.get("key_policy")
        assert result is not None, "Required property 'key_policy' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def primary_key_arn(self) -> builtins.str:
        '''Specifies the multi-Region primary key to replicate.

        The primary key must be in a different AWS Region of the same AWS partition. You can create only one replica of a given primary key in each AWS Region .
        .. epigraph::

           If you change the ``PrimaryKeyArn`` value of a replica key, the existing replica key is scheduled for deletion and a new replica key is created based on the specified primary key. While it is scheduled for deletion, the existing replica key becomes unusable. You can cancel the scheduled deletion of the key outside of CloudFormation.

           However, if you inadvertently delete a replica key, you can decrypt ciphertext encrypted by that replica key by using any related multi-Region key. If necessary, you can recreate the replica in the same Region after the previous one is completely deleted. For details, see `Deleting multi-Region keys <https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-delete.html>`_ in the *AWS Key Management Service Developer Guide*

        Specify the key ARN of an existing multi-Region primary key. For example, ``arn:aws:kms:us-east-2:111122223333:key/mrk-1234abcd12ab34cd56ef1234567890ab`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-replicakey.html#cfn-kms-replicakey-primarykeyarn
        '''
        result = self._values.get("primary_key_arn")
        assert result is not None, "Required property 'primary_key_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the KMS key.

        The default value is an empty string (no description).

        The description is not a shared property of multi-Region keys. You can specify the same description or a different description for each key in a set of related multi-Region keys. AWS Key Management Service does not synchronize this property.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-replicakey.html#cfn-kms-replicakey-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the replica key is enabled. Disabled KMS keys cannot be used in cryptographic operations.

        When ``Enabled`` is ``true`` , the *key state* of the KMS key is ``Enabled`` . When ``Enabled`` is ``false`` , the key state of the KMS key is ``Disabled`` . The default value is ``true`` .

        The actual key state of the replica might be affected by actions taken outside of CloudFormation, such as running the `EnableKey <https://docs.aws.amazon.com/kms/latest/APIReference/API_EnableKey.html>`_ , `DisableKey <https://docs.aws.amazon.com/kms/latest/APIReference/API_DisableKey.html>`_ , or `ScheduleKeyDeletion <https://docs.aws.amazon.com/kms/latest/APIReference/API_ScheduleKeyDeletion.html>`_ operations. Also, while the replica key is being created, its key state is ``Creating`` . When the process is complete, the key state of the replica key changes to ``Enabled`` .

        For information about the key states of a KMS key, see `Key state: Effect on your KMS key <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`_ in the *AWS Key Management Service Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-replicakey.html#cfn-kms-replicakey-enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def pending_window_in_days(self) -> typing.Optional[jsii.Number]:
        '''Specifies the number of days in the waiting period before AWS KMS deletes a replica key that has been removed from a CloudFormation stack.

        Enter a value between 7 and 30 days. The default value is 30 days.

        When you remove a replica key from a CloudFormation stack, AWS KMS schedules the replica key for deletion and starts the mandatory waiting period. The ``PendingWindowInDays`` property determines the length of waiting period. During the waiting period, the key state of replica key is ``Pending Deletion`` , which prevents it from being used in cryptographic operations. When the waiting period expires, AWS KMS permanently deletes the replica key.

        If the KMS key is a multi-Region primary key with replica keys, the waiting period begins when the last of its replica keys is deleted. Otherwise, the waiting period begins immediately.

        You cannot use a CloudFormation template to cancel deletion of the replica after you remove it from the stack, regardless of the waiting period. However, if you specify a replica key in your template that is based on the same primary key as the original replica key, CloudFormation creates a new replica key with the same key ID, key material, and other shared properties of the original replica key. This new replica key can decrypt ciphertext that was encrypted under the original replica key, or any related multi-Region key.

        For detailed information about deleting multi-Region keys, see `Deleting multi-Region keys <https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-delete.html>`_ in the *AWS Key Management Service Developer Guide* .

        For information about the ``PendingDeletion`` key state, see `Key state: Effect on your KMS key <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`_ in the *AWS Key Management Service Developer Guide* . For more information about deleting KMS keys, see the `ScheduleKeyDeletion <https://docs.aws.amazon.com/kms/latest/APIReference/API_ScheduleKeyDeletion.html>`_ operation in the *AWS Key Management Service API Reference* and `Deleting KMS keys <https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html>`_ in the *AWS Key Management Service Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-replicakey.html#cfn-kms-replicakey-pendingwindowindays
        '''
        result = self._values.get("pending_window_in_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Assigns one or more tags to the replica key.

        .. epigraph::

           Tagging or untagging a KMS key can allow or deny permission to the KMS key. For details, see `ABAC for AWS KMS <https://docs.aws.amazon.com/kms/latest/developerguide/abac.html>`_ in the *AWS Key Management Service Developer Guide* .

        Tags are not a shared property of multi-Region keys. You can specify the same tags or different tags for each key in a set of related multi-Region keys. AWS KMS does not synchronize this property.

        Each tag consists of a tag key and a tag value. Both the tag key and the tag value are required, but the tag value can be an empty (null) string. You cannot have more than one tag on a KMS key with the same tag key. If you specify an existing tag key with a different tag value, AWS KMS replaces the current tag value with the specified one.

        When you assign tags to an AWS resource, AWS generates a cost allocation report with usage and costs aggregated by tags. Tags can also be used to control access to a KMS key. For details, see `Tagging keys <https://docs.aws.amazon.com/kms/latest/developerguide/tagging-keys.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-replicakey.html#cfn-kms-replicakey-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnReplicaKeyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.aws_kms.IKey")
class IKey(_IResource_c80c4260, typing_extensions.Protocol):
    '''A KMS Key, either managed by this CDK app, or imported.'''

    @builtins.property
    @jsii.member(jsii_name="keyArn")
    def key_arn(self) -> builtins.str:
        '''The ARN of the key.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="keyId")
    def key_id(self) -> builtins.str:
        '''The ID of the key (the part that looks something like: 1234abcd-12ab-34cd-56ef-1234567890ab).

        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="addAlias")
    def add_alias(self, alias: builtins.str) -> "Alias":
        '''Defines a new alias for the key.

        :param alias: -
        '''
        ...

    @jsii.member(jsii_name="addToResourcePolicy")
    def add_to_resource_policy(
        self,
        statement: _PolicyStatement_0fe33853,
        allow_no_op: typing.Optional[builtins.bool] = None,
    ) -> _AddToResourcePolicyResult_1d0a53ad:
        '''Adds a statement to the KMS key resource policy.

        :param statement: The policy statement to add.
        :param allow_no_op: If this is set to ``false`` and there is no policy defined (i.e. external key), the operation will fail. Otherwise, it will no-op.
        '''
        ...

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Grant the indicated permissions on this key to the given principal.

        :param grantee: -
        :param actions: -
        '''
        ...

    @jsii.member(jsii_name="grantDecrypt")
    def grant_decrypt(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant decryption permissions using this key to the given principal.

        :param grantee: -
        '''
        ...

    @jsii.member(jsii_name="grantEncrypt")
    def grant_encrypt(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant encryption permissions using this key to the given principal.

        :param grantee: -
        '''
        ...

    @jsii.member(jsii_name="grantEncryptDecrypt")
    def grant_encrypt_decrypt(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant encryption and decryption permissions using this key to the given principal.

        :param grantee: -
        '''
        ...

    @jsii.member(jsii_name="grantGenerateMac")
    def grant_generate_mac(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant permissions to generating MACs to the given principal.

        :param grantee: -
        '''
        ...

    @jsii.member(jsii_name="grantVerifyMac")
    def grant_verify_mac(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant permissions to verifying MACs to the given principal.

        :param grantee: -
        '''
        ...


class _IKeyProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''A KMS Key, either managed by this CDK app, or imported.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_kms.IKey"

    @builtins.property
    @jsii.member(jsii_name="keyArn")
    def key_arn(self) -> builtins.str:
        '''The ARN of the key.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "keyArn"))

    @builtins.property
    @jsii.member(jsii_name="keyId")
    def key_id(self) -> builtins.str:
        '''The ID of the key (the part that looks something like: 1234abcd-12ab-34cd-56ef-1234567890ab).

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "keyId"))

    @jsii.member(jsii_name="addAlias")
    def add_alias(self, alias: builtins.str) -> "Alias":
        '''Defines a new alias for the key.

        :param alias: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2ffddf2bf6b08c78a62cc0dfd610a5f18de25ac8525da51ce3683ae56ea6333)
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
        return typing.cast("Alias", jsii.invoke(self, "addAlias", [alias]))

    @jsii.member(jsii_name="addToResourcePolicy")
    def add_to_resource_policy(
        self,
        statement: _PolicyStatement_0fe33853,
        allow_no_op: typing.Optional[builtins.bool] = None,
    ) -> _AddToResourcePolicyResult_1d0a53ad:
        '''Adds a statement to the KMS key resource policy.

        :param statement: The policy statement to add.
        :param allow_no_op: If this is set to ``false`` and there is no policy defined (i.e. external key), the operation will fail. Otherwise, it will no-op.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49ab7698d2a79e6b83d905354157adf61cc66dcdc514e2f6586029179411a56c)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
            check_type(argname="argument allow_no_op", value=allow_no_op, expected_type=type_hints["allow_no_op"])
        return typing.cast(_AddToResourcePolicyResult_1d0a53ad, jsii.invoke(self, "addToResourcePolicy", [statement, allow_no_op]))

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Grant the indicated permissions on this key to the given principal.

        :param grantee: -
        :param actions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e75995ff61f7b73643112ecb31c0f51795b9a98794730d4be368915f8c2593c2)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grant", [grantee, *actions]))

    @jsii.member(jsii_name="grantDecrypt")
    def grant_decrypt(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant decryption permissions using this key to the given principal.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39902b1c75983f537dc01c509a72cacad7b1f7eac41eb11b78961dad89057e68)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantDecrypt", [grantee]))

    @jsii.member(jsii_name="grantEncrypt")
    def grant_encrypt(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant encryption permissions using this key to the given principal.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19d45c86cc60f7439a524a94d75c39b726b3b12a4723b2d320f194039f842fcd)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantEncrypt", [grantee]))

    @jsii.member(jsii_name="grantEncryptDecrypt")
    def grant_encrypt_decrypt(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant encryption and decryption permissions using this key to the given principal.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f2582b1d436c32b0e7fbd6af00bad050f74f9e18f1406e20625022b2a13d294)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantEncryptDecrypt", [grantee]))

    @jsii.member(jsii_name="grantGenerateMac")
    def grant_generate_mac(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant permissions to generating MACs to the given principal.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__678d44f30b3f7854df209779d1ab6c27a0eac432204e7f4ac90a02792d307f03)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantGenerateMac", [grantee]))

    @jsii.member(jsii_name="grantVerifyMac")
    def grant_verify_mac(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant permissions to verifying MACs to the given principal.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e10fb25b1b8146054e097c61432d71d4ae4493eb15e2a482f90f513e686b24ee)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantVerifyMac", [grantee]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IKey).__jsii_proxy_class__ = lambda : _IKeyProxy


@jsii.implements(IKey)
class Key(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_kms.Key",
):
    '''Defines a KMS key.

    :resource: AWS::KMS::Key
    :exampleMetadata: infused

    Example::

        # destination_bucket: s3.Bucket
        
        source_bucket = s3.Bucket.from_bucket_attributes(self, "SourceBucket",
            bucket_arn="arn:aws:s3:::my-source-bucket-name",
            encryption_key=kms.Key.from_key_arn(self, "SourceBucketEncryptionKey", "arn:aws:kms:us-east-1:123456789012:key/<key-id>")
        )
        deployment = s3deploy.BucketDeployment(self, "DeployFiles",
            sources=[s3deploy.Source.bucket(source_bucket, "source.zip")],
            destination_bucket=destination_bucket
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        admins: typing.Optional[typing.Sequence[_IPrincipal_539bb2fd]] = None,
        alias: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[builtins.bool] = None,
        enable_key_rotation: typing.Optional[builtins.bool] = None,
        key_spec: typing.Optional["KeySpec"] = None,
        key_usage: typing.Optional["KeyUsage"] = None,
        pending_window: typing.Optional[_Duration_4839e8c3] = None,
        policy: typing.Optional[_PolicyDocument_3ac34393] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
        rotation_period: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param admins: A list of principals to add as key administrators to the key policy. Key administrators have permissions to manage the key (e.g., change permissions, revoke), but do not have permissions to use the key in cryptographic operations (e.g., encrypt, decrypt). These principals will be added to the default key policy (if none specified), or to the specified policy (if provided). Default: []
        :param alias: Initial alias to add to the key. More aliases can be added later by calling ``addAlias``. Default: - No alias is added for the key.
        :param description: A description of the key. Use a description that helps your users decide whether the key is appropriate for a particular task. Default: - No description.
        :param enabled: Indicates whether the key is available for use. Default: - Key is enabled.
        :param enable_key_rotation: Indicates whether AWS KMS rotates the key. Default: false
        :param key_spec: The cryptographic configuration of the key. The valid value depends on usage of the key. IMPORTANT: If you change this property of an existing key, the existing key is scheduled for deletion and a new key is created with the specified value. Default: KeySpec.SYMMETRIC_DEFAULT
        :param key_usage: The cryptographic operations for which the key can be used. IMPORTANT: If you change this property of an existing key, the existing key is scheduled for deletion and a new key is created with the specified value. Default: KeyUsage.ENCRYPT_DECRYPT
        :param pending_window: Specifies the number of days in the waiting period before AWS KMS deletes a CMK that has been removed from a CloudFormation stack. When you remove a customer master key (CMK) from a CloudFormation stack, AWS KMS schedules the CMK for deletion and starts the mandatory waiting period. The PendingWindowInDays property determines the length of waiting period. During the waiting period, the key state of CMK is Pending Deletion, which prevents the CMK from being used in cryptographic operations. When the waiting period expires, AWS KMS permanently deletes the CMK. Enter a value between 7 and 30 days. Default: - 30 days
        :param policy: Custom policy document to attach to the KMS key. NOTE - If the ``@aws-cdk/aws-kms:defaultKeyPolicies`` feature flag is set (the default for new projects), this policy will *override* the default key policy and become the only key policy for the key. If the feature flag is not set, this policy will be appended to the default key policy. Default: - A policy document with permissions for the account root to administer the key will be created.
        :param removal_policy: Whether the encryption key should be retained when it is removed from the Stack. This is useful when one wants to retain access to data that was encrypted with a key that is being retired. Default: RemovalPolicy.Retain
        :param rotation_period: The period between each automatic rotation. Default: - set by CFN to 365 days.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cde9534bdfe7c19d6e24354f8a0de8ca349632d3f565addcaed7e86a84dac7e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = KeyProps(
            admins=admins,
            alias=alias,
            description=description,
            enabled=enabled,
            enable_key_rotation=enable_key_rotation,
            key_spec=key_spec,
            key_usage=key_usage,
            pending_window=pending_window,
            policy=policy,
            removal_policy=removal_policy,
            rotation_period=rotation_period,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromCfnKey")
    @builtins.classmethod
    def from_cfn_key(cls, cfn_key: CfnKey) -> IKey:
        '''Create a mutable ``IKey`` based on a low-level ``CfnKey``.

        This is most useful when combined with the cloudformation-include module.
        This method is different than ``fromKeyArn()`` because the ``IKey``
        returned from this method is mutable;
        meaning, calling any mutating methods on it,
        like ``IKey.addToResourcePolicy()``,
        will actually be reflected in the resulting template,
        as opposed to the object returned from ``fromKeyArn()``,
        on which calling those methods would have no effect.

        :param cfn_key: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44fb03a49b50ed40c1e4dfe9c0db8eb33dbd35e3ee425ee8f32dde09abc3287c)
            check_type(argname="argument cfn_key", value=cfn_key, expected_type=type_hints["cfn_key"])
        return typing.cast(IKey, jsii.sinvoke(cls, "fromCfnKey", [cfn_key]))

    @jsii.member(jsii_name="fromKeyArn")
    @builtins.classmethod
    def from_key_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        key_arn: builtins.str,
    ) -> IKey:
        '''Import an externally defined KMS Key using its ARN.

        :param scope: the construct that will "own" the imported key.
        :param id: the id of the imported key in the construct tree.
        :param key_arn: the ARN of an existing KMS key.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9222dd19331f8774792b2f22b672882512022a23227af13133314719a32a929e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument key_arn", value=key_arn, expected_type=type_hints["key_arn"])
        return typing.cast(IKey, jsii.sinvoke(cls, "fromKeyArn", [scope, id, key_arn]))

    @jsii.member(jsii_name="fromLookup")
    @builtins.classmethod
    def from_lookup(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        alias_name: builtins.str,
    ) -> IKey:
        '''Import an existing Key by querying the AWS environment this stack is deployed to.

        This function only needs to be used to use Keys not defined in your CDK
        application. If you are looking to share a Key between stacks, you can
        pass the ``Key`` object between stacks and use it as normal. In addition,
        it's not necessary to use this method if an interface accepts an ``IKey``.
        In this case, ``Alias.fromAliasName()`` can be used which returns an alias
        that extends ``IKey``.

        Calling this method will lead to a lookup when the CDK CLI is executed.
        You can therefore not use any values that will only be available at
        CloudFormation execution time (i.e., Tokens).

        The Key information will be cached in ``cdk.context.json`` and the same Key
        will be used on future runs. To refresh the lookup, you will have to
        evict the value from the cache using the ``cdk context`` command. See
        https://docs.aws.amazon.com/cdk/latest/guide/context.html for more information.

        :param scope: -
        :param id: -
        :param alias_name: The alias name of the Key. Must be in the format ``alias/<AliasName>``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54c731fe78f9388d4b31695080a02f67600ec386d3b55f25a7274b86edbd4673)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = KeyLookupOptions(alias_name=alias_name)

        return typing.cast(IKey, jsii.sinvoke(cls, "fromLookup", [scope, id, options]))

    @jsii.member(jsii_name="addAlias")
    def add_alias(self, alias_name: builtins.str) -> "Alias":
        '''Defines a new alias for the key.

        :param alias_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c455c06c17802eaffea2f6642f95411cde639deb7ec10fa1d1e54bc6d7babe0)
            check_type(argname="argument alias_name", value=alias_name, expected_type=type_hints["alias_name"])
        return typing.cast("Alias", jsii.invoke(self, "addAlias", [alias_name]))

    @jsii.member(jsii_name="addToResourcePolicy")
    def add_to_resource_policy(
        self,
        statement: _PolicyStatement_0fe33853,
        allow_no_op: typing.Optional[builtins.bool] = None,
    ) -> _AddToResourcePolicyResult_1d0a53ad:
        '''Adds a statement to the KMS key resource policy.

        :param statement: The policy statement to add.
        :param allow_no_op: If this is set to ``false`` and there is no policy defined (i.e. external key), the operation will fail. Otherwise, it will no-op.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f20e8e11b4cff0f78acc743ad38d02a945f8e93be1f7bfc67153d317f711d06c)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
            check_type(argname="argument allow_no_op", value=allow_no_op, expected_type=type_hints["allow_no_op"])
        return typing.cast(_AddToResourcePolicyResult_1d0a53ad, jsii.invoke(self, "addToResourcePolicy", [statement, allow_no_op]))

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Grant the indicated permissions on this key to the given principal.

        This modifies both the principal's policy as well as the resource policy,
        since the default CloudFormation setup for KMS keys is that the policy
        must not be empty and so default grants won't work.

        :param grantee: -
        :param actions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3078f1361f1b59b619c5946b92259b4d2eefa0ae12e2e3b01160eae5ce37ceed)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grant", [grantee, *actions]))

    @jsii.member(jsii_name="grantAdmin")
    def grant_admin(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant admins permissions using this key to the given principal.

        Key administrators have permissions to manage the key (e.g., change permissions, revoke), but do not have permissions
        to use the key in cryptographic operations (e.g., encrypt, decrypt).

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__767164803c663312dbd0dc562333e5aa71475360f03804af0d572d5e1e00b889)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantAdmin", [grantee]))

    @jsii.member(jsii_name="grantDecrypt")
    def grant_decrypt(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant decryption permissions using this key to the given principal.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21f59a965699a16e14a1c50712dea7dfff44afb1561561c2ca8c3dc2d510da1d)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantDecrypt", [grantee]))

    @jsii.member(jsii_name="grantEncrypt")
    def grant_encrypt(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant encryption permissions using this key to the given principal.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b813a815a19cfcc384a90657fd701837adf5051ac8297faee4ede086e7e8ce8)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantEncrypt", [grantee]))

    @jsii.member(jsii_name="grantEncryptDecrypt")
    def grant_encrypt_decrypt(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant encryption and decryption permissions using this key to the given principal.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14a8599a061fbde74d692dfefcfd2f5f92f1a86fc2beee05e7d53c877d7deb03)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantEncryptDecrypt", [grantee]))

    @jsii.member(jsii_name="grantGenerateMac")
    def grant_generate_mac(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant permissions to generating MACs to the given principal.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__440bf3733f200027c74618bbc6f89d59b060f4aa9d88bb6dbfb057771091f628)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantGenerateMac", [grantee]))

    @jsii.member(jsii_name="grantVerifyMac")
    def grant_verify_mac(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant permissions to verifying MACs to the given principal.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de56bfcabbb83e3ba315f07ba084787bd71e82306a46ddc61555bc4f07b77538)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantVerifyMac", [grantee]))

    @builtins.property
    @jsii.member(jsii_name="keyArn")
    def key_arn(self) -> builtins.str:
        '''The ARN of the key.'''
        return typing.cast(builtins.str, jsii.get(self, "keyArn"))

    @builtins.property
    @jsii.member(jsii_name="keyId")
    def key_id(self) -> builtins.str:
        '''The ID of the key (the part that looks something like: 1234abcd-12ab-34cd-56ef-1234567890ab).'''
        return typing.cast(builtins.str, jsii.get(self, "keyId"))

    @builtins.property
    @jsii.member(jsii_name="trustAccountIdentities")
    def _trust_account_identities(self) -> builtins.bool:
        '''Optional property to control trusting account identities.

        If specified, grants will default identity policies instead of to both
        resource and identity policies. This matches the default behavior when creating
        KMS keys via the API or console.
        '''
        return typing.cast(builtins.bool, jsii.get(self, "trustAccountIdentities"))

    @builtins.property
    @jsii.member(jsii_name="policy")
    def _policy(self) -> typing.Optional[_PolicyDocument_3ac34393]:
        '''Optional policy document that represents the resource policy of this key.

        If specified, addToResourcePolicy can be used to edit this policy.
        Otherwise this method will no-op.
        '''
        return typing.cast(typing.Optional[_PolicyDocument_3ac34393], jsii.get(self, "policy"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_kms.KeyLookupOptions",
    jsii_struct_bases=[],
    name_mapping={"alias_name": "aliasName"},
)
class KeyLookupOptions:
    def __init__(self, *, alias_name: builtins.str) -> None:
        '''Properties for looking up an existing Key.

        :param alias_name: The alias name of the Key. Must be in the format ``alias/<AliasName>``.

        :exampleMetadata: infused

        Example::

            my_key_lookup = kms.Key.from_lookup(self, "MyKeyLookup",
                alias_name="alias/KeyAlias"
            )
            
            role = iam.Role(self, "MyRole",
                assumed_by=iam.ServicePrincipal("lambda.amazonaws.com")
            )
            my_key_lookup.grant_encrypt_decrypt(role)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f5a93b8499d8ef4842a85d33ca3d3de5edce426bd92f9899e4dcda2ebfcf7e0)
            check_type(argname="argument alias_name", value=alias_name, expected_type=type_hints["alias_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alias_name": alias_name,
        }

    @builtins.property
    def alias_name(self) -> builtins.str:
        '''The alias name of the Key.

        Must be in the format ``alias/<AliasName>``.
        '''
        result = self._values.get("alias_name")
        assert result is not None, "Required property 'alias_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyLookupOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_kms.KeyProps",
    jsii_struct_bases=[],
    name_mapping={
        "admins": "admins",
        "alias": "alias",
        "description": "description",
        "enabled": "enabled",
        "enable_key_rotation": "enableKeyRotation",
        "key_spec": "keySpec",
        "key_usage": "keyUsage",
        "pending_window": "pendingWindow",
        "policy": "policy",
        "removal_policy": "removalPolicy",
        "rotation_period": "rotationPeriod",
    },
)
class KeyProps:
    def __init__(
        self,
        *,
        admins: typing.Optional[typing.Sequence[_IPrincipal_539bb2fd]] = None,
        alias: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[builtins.bool] = None,
        enable_key_rotation: typing.Optional[builtins.bool] = None,
        key_spec: typing.Optional["KeySpec"] = None,
        key_usage: typing.Optional["KeyUsage"] = None,
        pending_window: typing.Optional[_Duration_4839e8c3] = None,
        policy: typing.Optional[_PolicyDocument_3ac34393] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
        rotation_period: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''Construction properties for a KMS Key object.

        :param admins: A list of principals to add as key administrators to the key policy. Key administrators have permissions to manage the key (e.g., change permissions, revoke), but do not have permissions to use the key in cryptographic operations (e.g., encrypt, decrypt). These principals will be added to the default key policy (if none specified), or to the specified policy (if provided). Default: []
        :param alias: Initial alias to add to the key. More aliases can be added later by calling ``addAlias``. Default: - No alias is added for the key.
        :param description: A description of the key. Use a description that helps your users decide whether the key is appropriate for a particular task. Default: - No description.
        :param enabled: Indicates whether the key is available for use. Default: - Key is enabled.
        :param enable_key_rotation: Indicates whether AWS KMS rotates the key. Default: false
        :param key_spec: The cryptographic configuration of the key. The valid value depends on usage of the key. IMPORTANT: If you change this property of an existing key, the existing key is scheduled for deletion and a new key is created with the specified value. Default: KeySpec.SYMMETRIC_DEFAULT
        :param key_usage: The cryptographic operations for which the key can be used. IMPORTANT: If you change this property of an existing key, the existing key is scheduled for deletion and a new key is created with the specified value. Default: KeyUsage.ENCRYPT_DECRYPT
        :param pending_window: Specifies the number of days in the waiting period before AWS KMS deletes a CMK that has been removed from a CloudFormation stack. When you remove a customer master key (CMK) from a CloudFormation stack, AWS KMS schedules the CMK for deletion and starts the mandatory waiting period. The PendingWindowInDays property determines the length of waiting period. During the waiting period, the key state of CMK is Pending Deletion, which prevents the CMK from being used in cryptographic operations. When the waiting period expires, AWS KMS permanently deletes the CMK. Enter a value between 7 and 30 days. Default: - 30 days
        :param policy: Custom policy document to attach to the KMS key. NOTE - If the ``@aws-cdk/aws-kms:defaultKeyPolicies`` feature flag is set (the default for new projects), this policy will *override* the default key policy and become the only key policy for the key. If the feature flag is not set, this policy will be appended to the default key policy. Default: - A policy document with permissions for the account root to administer the key will be created.
        :param removal_policy: Whether the encryption key should be retained when it is removed from the Stack. This is useful when one wants to retain access to data that was encrypted with a key that is being retired. Default: RemovalPolicy.Retain
        :param rotation_period: The period between each automatic rotation. Default: - set by CFN to 365 days.

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_kms as kms
            
            
            source_output = codepipeline.Artifact()
            target_bucket = s3.Bucket(self, "MyBucket")
            key = kms.Key(self, "EnvVarEncryptKey",
                description="sample key"
            )
            
            pipeline = codepipeline.Pipeline(self, "MyPipeline")
            deploy_action = codepipeline_actions.S3DeployAction(
                action_name="S3Deploy",
                bucket=target_bucket,
                input=source_output,
                encryption_key=key
            )
            deploy_stage = pipeline.add_stage(
                stage_name="Deploy",
                actions=[deploy_action]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3cbd21baa1113e5b2864ce6b440a0d87704642442943c3a554ab23ae712d828)
            check_type(argname="argument admins", value=admins, expected_type=type_hints["admins"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument enable_key_rotation", value=enable_key_rotation, expected_type=type_hints["enable_key_rotation"])
            check_type(argname="argument key_spec", value=key_spec, expected_type=type_hints["key_spec"])
            check_type(argname="argument key_usage", value=key_usage, expected_type=type_hints["key_usage"])
            check_type(argname="argument pending_window", value=pending_window, expected_type=type_hints["pending_window"])
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument rotation_period", value=rotation_period, expected_type=type_hints["rotation_period"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if admins is not None:
            self._values["admins"] = admins
        if alias is not None:
            self._values["alias"] = alias
        if description is not None:
            self._values["description"] = description
        if enabled is not None:
            self._values["enabled"] = enabled
        if enable_key_rotation is not None:
            self._values["enable_key_rotation"] = enable_key_rotation
        if key_spec is not None:
            self._values["key_spec"] = key_spec
        if key_usage is not None:
            self._values["key_usage"] = key_usage
        if pending_window is not None:
            self._values["pending_window"] = pending_window
        if policy is not None:
            self._values["policy"] = policy
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if rotation_period is not None:
            self._values["rotation_period"] = rotation_period

    @builtins.property
    def admins(self) -> typing.Optional[typing.List[_IPrincipal_539bb2fd]]:
        '''A list of principals to add as key administrators to the key policy.

        Key administrators have permissions to manage the key (e.g., change permissions, revoke), but do not have permissions
        to use the key in cryptographic operations (e.g., encrypt, decrypt).

        These principals will be added to the default key policy (if none specified), or to the specified policy (if provided).

        :default: []
        '''
        result = self._values.get("admins")
        return typing.cast(typing.Optional[typing.List[_IPrincipal_539bb2fd]], result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Initial alias to add to the key.

        More aliases can be added later by calling ``addAlias``.

        :default: - No alias is added for the key.
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the key.

        Use a description that helps your users decide
        whether the key is appropriate for a particular task.

        :default: - No description.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether the key is available for use.

        :default: - Key is enabled.
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_key_rotation(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether AWS KMS rotates the key.

        :default: false
        '''
        result = self._values.get("enable_key_rotation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def key_spec(self) -> typing.Optional["KeySpec"]:
        '''The cryptographic configuration of the key. The valid value depends on usage of the key.

        IMPORTANT: If you change this property of an existing key, the existing key is scheduled for deletion
        and a new key is created with the specified value.

        :default: KeySpec.SYMMETRIC_DEFAULT
        '''
        result = self._values.get("key_spec")
        return typing.cast(typing.Optional["KeySpec"], result)

    @builtins.property
    def key_usage(self) -> typing.Optional["KeyUsage"]:
        '''The cryptographic operations for which the key can be used.

        IMPORTANT: If you change this property of an existing key, the existing key is scheduled for deletion
        and a new key is created with the specified value.

        :default: KeyUsage.ENCRYPT_DECRYPT
        '''
        result = self._values.get("key_usage")
        return typing.cast(typing.Optional["KeyUsage"], result)

    @builtins.property
    def pending_window(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Specifies the number of days in the waiting period before AWS KMS deletes a CMK that has been removed from a CloudFormation stack.

        When you remove a customer master key (CMK) from a CloudFormation stack, AWS KMS schedules the CMK for deletion
        and starts the mandatory waiting period. The PendingWindowInDays property determines the length of waiting period.
        During the waiting period, the key state of CMK is Pending Deletion, which prevents the CMK from being used in
        cryptographic operations. When the waiting period expires, AWS KMS permanently deletes the CMK.

        Enter a value between 7 and 30 days.

        :default: - 30 days

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-pendingwindowindays
        '''
        result = self._values.get("pending_window")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def policy(self) -> typing.Optional[_PolicyDocument_3ac34393]:
        '''Custom policy document to attach to the KMS key.

        NOTE - If the ``@aws-cdk/aws-kms:defaultKeyPolicies`` feature flag is set (the default for new projects),
        this policy will *override* the default key policy and become the only key policy for the key. If the
        feature flag is not set, this policy will be appended to the default key policy.

        :default:

        - A policy document with permissions for the account root to
        administer the key will be created.
        '''
        result = self._values.get("policy")
        return typing.cast(typing.Optional[_PolicyDocument_3ac34393], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[_RemovalPolicy_9f93c814]:
        '''Whether the encryption key should be retained when it is removed from the Stack.

        This is useful when one wants to
        retain access to data that was encrypted with a key that is being retired.

        :default: RemovalPolicy.Retain
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_RemovalPolicy_9f93c814], result)

    @builtins.property
    def rotation_period(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The period between each automatic rotation.

        :default: - set by CFN to 365 days.
        '''
        result = self._values.get("rotation_period")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_kms.KeySpec")
class KeySpec(enum.Enum):
    '''The key spec, represents the cryptographic configuration of keys.

    :exampleMetadata: infused

    Example::

        key = kms.Key(self, "MyKey",
            key_spec=kms.KeySpec.ECC_SECG_P256K1,  # Default to SYMMETRIC_DEFAULT
            key_usage=kms.KeyUsage.SIGN_VERIFY
        )
    '''

    SYMMETRIC_DEFAULT = "SYMMETRIC_DEFAULT"
    '''The default key spec.

    Valid usage: ENCRYPT_DECRYPT
    '''
    RSA_2048 = "RSA_2048"
    '''RSA with 2048 bits of key.

    Valid usage: ENCRYPT_DECRYPT and SIGN_VERIFY
    '''
    RSA_3072 = "RSA_3072"
    '''RSA with 3072 bits of key.

    Valid usage: ENCRYPT_DECRYPT and SIGN_VERIFY
    '''
    RSA_4096 = "RSA_4096"
    '''RSA with 4096 bits of key.

    Valid usage: ENCRYPT_DECRYPT and SIGN_VERIFY
    '''
    ECC_NIST_P256 = "ECC_NIST_P256"
    '''NIST FIPS 186-4, Section 6.4, ECDSA signature using the curve specified by the key and SHA-256 for the message digest.

    Valid usage: SIGN_VERIFY
    '''
    ECC_NIST_P384 = "ECC_NIST_P384"
    '''NIST FIPS 186-4, Section 6.4, ECDSA signature using the curve specified by the key and SHA-384 for the message digest.

    Valid usage: SIGN_VERIFY
    '''
    ECC_NIST_P521 = "ECC_NIST_P521"
    '''NIST FIPS 186-4, Section 6.4, ECDSA signature using the curve specified by the key and SHA-512 for the message digest.

    Valid usage: SIGN_VERIFY
    '''
    ECC_SECG_P256K1 = "ECC_SECG_P256K1"
    '''Standards for Efficient Cryptography 2, Section 2.4.1, ECDSA signature on the Koblitz curve.

    Valid usage: SIGN_VERIFY
    '''
    HMAC_224 = "HMAC_224"
    '''Hash-Based Message Authentication Code as defined in RFC 2104 using the message digest function SHA224.

    Valid usage: GENERATE_VERIFY_MAC
    '''
    HMAC_256 = "HMAC_256"
    '''Hash-Based Message Authentication Code as defined in RFC 2104 using the message digest function SHA256.

    Valid usage: GENERATE_VERIFY_MAC
    '''
    HMAC_384 = "HMAC_384"
    '''Hash-Based Message Authentication Code as defined in RFC 2104 using the message digest function SHA384.

    Valid usage: GENERATE_VERIFY_MAC
    '''
    HMAC_512 = "HMAC_512"
    '''Hash-Based Message Authentication Code as defined in RFC 2104 using the message digest function SHA512.

    Valid usage: GENERATE_VERIFY_MAC
    '''
    SM2 = "SM2"
    '''Elliptic curve key spec available only in China Regions.

    Valid usage: ENCRYPT_DECRYPT and SIGN_VERIFY
    '''


@jsii.enum(jsii_type="aws-cdk-lib.aws_kms.KeyUsage")
class KeyUsage(enum.Enum):
    '''The key usage, represents the cryptographic operations of keys.

    :exampleMetadata: infused

    Example::

        key = kms.Key(self, "MyKey",
            key_spec=kms.KeySpec.ECC_SECG_P256K1,  # Default to SYMMETRIC_DEFAULT
            key_usage=kms.KeyUsage.SIGN_VERIFY
        )
    '''

    ENCRYPT_DECRYPT = "ENCRYPT_DECRYPT"
    '''Encryption and decryption.'''
    SIGN_VERIFY = "SIGN_VERIFY"
    '''Signing and verification.'''
    GENERATE_VERIFY_MAC = "GENERATE_VERIFY_MAC"
    '''Generating and verifying MACs.'''


class ViaServicePrincipal(
    _PrincipalBase_b5077813,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_kms.ViaServicePrincipal",
):
    '''A principal to allow access to a key if it's being used through another AWS service.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iam as iam
        from aws_cdk import aws_kms as kms
        
        # principal: iam.IPrincipal
        
        via_service_principal = kms.ViaServicePrincipal("serviceName", principal)
    '''

    def __init__(
        self,
        service_name: builtins.str,
        base_principal: typing.Optional[_IPrincipal_539bb2fd] = None,
    ) -> None:
        '''
        :param service_name: -
        :param base_principal: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__590dd135e934b0f55ab30f9bfcb69bed4ccb0a3ef22f6f3ee9850c4658e2e172)
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
            check_type(argname="argument base_principal", value=base_principal, expected_type=type_hints["base_principal"])
        jsii.create(self.__class__, self, [service_name, base_principal])

    @jsii.member(jsii_name="dedupeString")
    def dedupe_string(self) -> typing.Optional[builtins.str]:
        '''Return whether or not this principal is equal to the given principal.'''
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "dedupeString", []))

    @builtins.property
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> _PrincipalPolicyFragment_6a855d11:
        '''Return the policy fragment that identifies this principal in a Policy.'''
        return typing.cast(_PrincipalPolicyFragment_6a855d11, jsii.get(self, "policyFragment"))


@jsii.interface(jsii_type="aws-cdk-lib.aws_kms.IAlias")
class IAlias(IKey, typing_extensions.Protocol):
    '''A KMS Key alias.

    An alias can be used in all places that expect a key.
    '''

    @builtins.property
    @jsii.member(jsii_name="aliasName")
    def alias_name(self) -> builtins.str:
        '''The name of the alias.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="aliasTargetKey")
    def alias_target_key(self) -> IKey:
        '''The Key to which the Alias refers.

        :attribute: true
        '''
        ...


class _IAliasProxy(
    jsii.proxy_for(IKey), # type: ignore[misc]
):
    '''A KMS Key alias.

    An alias can be used in all places that expect a key.
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_kms.IAlias"

    @builtins.property
    @jsii.member(jsii_name="aliasName")
    def alias_name(self) -> builtins.str:
        '''The name of the alias.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "aliasName"))

    @builtins.property
    @jsii.member(jsii_name="aliasTargetKey")
    def alias_target_key(self) -> IKey:
        '''The Key to which the Alias refers.

        :attribute: true
        '''
        return typing.cast(IKey, jsii.get(self, "aliasTargetKey"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAlias).__jsii_proxy_class__ = lambda : _IAliasProxy


@jsii.implements(IAlias)
class Alias(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_kms.Alias",
):
    '''Defines a display name for a customer master key (CMK) in AWS Key Management Service (AWS KMS).

    Using an alias to refer to a key can help you simplify key
    management. For example, when rotating keys, you can just update the alias
    mapping instead of tracking and changing key IDs. For more information, see
    Working with Aliases in the AWS Key Management Service Developer Guide.

    You can also add an alias for a key by calling ``key.addAlias(alias)``.

    :resource: AWS::KMS::Alias
    :exampleMetadata: infused

    Example::

        # Passing an encrypted replication bucket created in a different stack.
        app = App()
        replication_stack = Stack(app, "ReplicationStack",
            env=Environment(
                region="us-west-1"
            )
        )
        key = kms.Key(replication_stack, "ReplicationKey")
        alias = kms.Alias(replication_stack, "ReplicationAlias",
            # aliasName is required
            alias_name=PhysicalName.GENERATE_IF_NEEDED,
            target_key=key
        )
        replication_bucket = s3.Bucket(replication_stack, "ReplicationBucket",
            bucket_name=PhysicalName.GENERATE_IF_NEEDED,
            encryption_key=alias
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        alias_name: builtins.str,
        target_key: IKey,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param alias_name: The name of the alias. The name must start with alias followed by a forward slash, such as alias/. You can't specify aliases that begin with alias/AWS. These aliases are reserved.
        :param target_key: The ID of the key for which you are creating the alias. Specify the key's globally unique identifier or Amazon Resource Name (ARN). You can't specify another alias.
        :param removal_policy: Policy to apply when the alias is removed from this stack. Default: - The alias will be deleted
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__082e4e34e1b8d1c0e2ca7a3f88ca2fd4db45a02c06b37aa49a92c334ec48b156)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = AliasProps(
            alias_name=alias_name, target_key=target_key, removal_policy=removal_policy
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromAliasAttributes")
    @builtins.classmethod
    def from_alias_attributes(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        alias_name: builtins.str,
        alias_target_key: IKey,
    ) -> IAlias:
        '''Import an existing KMS Alias defined outside the CDK app.

        :param scope: The parent creating construct (usually ``this``).
        :param id: The construct's name.
        :param alias_name: Specifies the alias name. This value must begin with alias/ followed by a name (i.e. alias/ExampleAlias)
        :param alias_target_key: The customer master key (CMK) to which the Alias refers.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1aa4cb540c0255b690750a7c543fa0e6d01be800bf1f1a6d2e27a9ae9821eb9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = AliasAttributes(
            alias_name=alias_name, alias_target_key=alias_target_key
        )

        return typing.cast(IAlias, jsii.sinvoke(cls, "fromAliasAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="fromAliasName")
    @builtins.classmethod
    def from_alias_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        alias_name: builtins.str,
    ) -> IAlias:
        '''Import an existing KMS Alias defined outside the CDK app, by the alias name.

        This method should be used
        instead of 'fromAliasAttributes' when the underlying KMS Key ARN is not available.
        This Alias will not have a direct reference to the KMS Key, so addAlias and grant* methods are not supported.

        :param scope: The parent creating construct (usually ``this``).
        :param id: The construct's name.
        :param alias_name: The full name of the KMS Alias (e.g., 'alias/aws/s3', 'alias/myKeyAlias').
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f63f0eacb8d2b482050e953fb9bae15526c96706289c5ec85ff0005315101f4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument alias_name", value=alias_name, expected_type=type_hints["alias_name"])
        return typing.cast(IAlias, jsii.sinvoke(cls, "fromAliasName", [scope, id, alias_name]))

    @jsii.member(jsii_name="addAlias")
    def add_alias(self, alias: builtins.str) -> "Alias":
        '''Defines a new alias for the key.

        :param alias: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee86459b88002347db31460bea5798240197a80fb17a5bf97c67ed7482f84ae3)
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
        return typing.cast("Alias", jsii.invoke(self, "addAlias", [alias]))

    @jsii.member(jsii_name="addToResourcePolicy")
    def add_to_resource_policy(
        self,
        statement: _PolicyStatement_0fe33853,
        allow_no_op: typing.Optional[builtins.bool] = None,
    ) -> _AddToResourcePolicyResult_1d0a53ad:
        '''Adds a statement to the KMS key resource policy.

        :param statement: -
        :param allow_no_op: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b22b27f4615124191ddcb7d43f313a681be5bf126396931e72f2a8086f28d15d)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
            check_type(argname="argument allow_no_op", value=allow_no_op, expected_type=type_hints["allow_no_op"])
        return typing.cast(_AddToResourcePolicyResult_1d0a53ad, jsii.invoke(self, "addToResourcePolicy", [statement, allow_no_op]))

    @jsii.member(jsii_name="generatePhysicalName")
    def _generate_physical_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.invoke(self, "generatePhysicalName", []))

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Grant the indicated permissions on this key to the given principal.

        :param grantee: -
        :param actions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90c67882778cd60cf1af18413a9aaf1ca290ab5a87d50f8929fa64ac66b8923a)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grant", [grantee, *actions]))

    @jsii.member(jsii_name="grantDecrypt")
    def grant_decrypt(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant decryption permissions using this key to the given principal.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76283f5eae879bc6cabdbf046c1d68b45cbf7e0222f84edb498c04a69b69ad79)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantDecrypt", [grantee]))

    @jsii.member(jsii_name="grantEncrypt")
    def grant_encrypt(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant encryption permissions using this key to the given principal.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1eddbd590dc8e102f7834fb50d2514218d6a3b73d838b34d7fa52ce858c2c8a)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantEncrypt", [grantee]))

    @jsii.member(jsii_name="grantEncryptDecrypt")
    def grant_encrypt_decrypt(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant encryption and decryption permissions using this key to the given principal.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__765b50233677797d65a2ccab14fdf25c84306d9da9ab54635a10428ed6a23546)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantEncryptDecrypt", [grantee]))

    @jsii.member(jsii_name="grantGenerateMac")
    def grant_generate_mac(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant permissions to generating MACs to the given principal.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a08117fd4a61f5dbdfb60de37f9aafd66666c36ccbd553402d5504cdd79a06f2)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantGenerateMac", [grantee]))

    @jsii.member(jsii_name="grantVerifyMac")
    def grant_verify_mac(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant permissions to verifying MACs to the given principal.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__889887809ebfcb10b086b9443331082b607fe1c8b476e14ebc492583598f19a2)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantVerifyMac", [grantee]))

    @builtins.property
    @jsii.member(jsii_name="aliasArn")
    def alias_arn(self) -> builtins.str:
        '''The ARN of the alias.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "aliasArn"))

    @builtins.property
    @jsii.member(jsii_name="aliasName")
    def alias_name(self) -> builtins.str:
        '''The name of the alias.'''
        return typing.cast(builtins.str, jsii.get(self, "aliasName"))

    @builtins.property
    @jsii.member(jsii_name="aliasTargetKey")
    def alias_target_key(self) -> IKey:
        '''The Key to which the Alias refers.'''
        return typing.cast(IKey, jsii.get(self, "aliasTargetKey"))

    @builtins.property
    @jsii.member(jsii_name="keyArn")
    def key_arn(self) -> builtins.str:
        '''(deprecated) The ARN of the alias.

        :deprecated: use ``aliasArn`` instead

        :stability: deprecated
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "keyArn"))

    @builtins.property
    @jsii.member(jsii_name="keyId")
    def key_id(self) -> builtins.str:
        '''The ID of the key (the part that looks something like: 1234abcd-12ab-34cd-56ef-1234567890ab).'''
        return typing.cast(builtins.str, jsii.get(self, "keyId"))


__all__ = [
    "Alias",
    "AliasAttributes",
    "AliasProps",
    "CfnAlias",
    "CfnAliasProps",
    "CfnKey",
    "CfnKeyProps",
    "CfnReplicaKey",
    "CfnReplicaKeyProps",
    "IAlias",
    "IKey",
    "Key",
    "KeyLookupOptions",
    "KeyProps",
    "KeySpec",
    "KeyUsage",
    "ViaServicePrincipal",
]

publication.publish()

def _typecheckingstub__b4044a422b77633efb024676d8b64edc24f9f3e6dda3050cda6f5bb78c388993(
    *,
    alias_name: builtins.str,
    alias_target_key: IKey,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e903bf066a426ef7752d4c25658bc63605bb655d804e5468ef9fa75e0fe87f57(
    *,
    alias_name: builtins.str,
    target_key: IKey,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ed5a3924f89c3ad638de218f71940a644d4f9331e3a66f708de865cc3551205(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    alias_name: builtins.str,
    target_key_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91d92bc86df739cdbb4a623f1bec0006f2c4e912b1d6817e7e5fc8fc28d6d61d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be1861ad699c79ab6c6405435694534bc0b254bb6fe02fa309564e05b8ab5a6f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__293c0aafbebd8a831d41848f3d7035971f2665e6401dfe8705989d1abae2c2c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e12c32dedd31d49587e236bb886a73e1a0ef34730815c73039721efa393b6fb2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbfd3a4fafdacbfbfd8d6fce574bc924973ce57499da64b6659e12ea905b460f(
    *,
    alias_name: builtins.str,
    target_key_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ea678e9e5a947601d16e5bb11fec3683fbb15bba768bee0b88be7e196d8783c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    bypass_policy_lockout_safety_check: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    description: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    enable_key_rotation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    key_policy: typing.Any = None,
    key_spec: typing.Optional[builtins.str] = None,
    key_usage: typing.Optional[builtins.str] = None,
    multi_region: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    origin: typing.Optional[builtins.str] = None,
    pending_window_in_days: typing.Optional[jsii.Number] = None,
    rotation_period_in_days: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6311cde99d8265c1aa77cad19077d4dc11fa11a16a0a5d601158013e78b4de6(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7468635e1eaf46c92748f2c14a3230215aa887e54ed03c370eee59b7ed05117b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba782ca88c8b210d0c18f73ecee5e7266ed06b7428c903676aca9b26b6490443(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01ec2bc212e875693eedcd62e8c0a2303fbbcbb0c0520e369d7b6372f89ba8ef(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d16a27f134df94f3471ae307ddaf158320e92fc426e0a715a044c762a591e56(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1949abfe35e26dd5174b35137bea94a550270331496fd2f865d63e22360c88de(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd3f4724ca140c9b1dca16904dd53ab0905d0688de411b0f60d4f538cb2ac4a2(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00b8e7e0c6c26ba4d81ad2ec83a06ba02111a601de28c48a34e711a20bdb960d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3644201e513b7c747f1fac050f42c4761013ce447fd095d4670a875776c68562(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a81f5a9d29ef2c8fdbd0a5b47659d6f998118db687737549f32e443f43446da(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e82f572625e8bbed987a6ede9a751d501f7398289c234e243ea2f716f23608b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d3e524eda3827ec1d53e329afc207f3ef954caf7cf407b25faef721f3a2016d(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b766cb0a8ed53bed340510bfb429fb6a5f36d2f63f9c7718fb1f0c92f2fbc59(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b85648b8166c62900697e128ab3a35c1360fdab37323145ed7b7c76dd91c4576(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52751771c8b3e52917eaf0c78bad67c065fa3f95795e92f5eab3e92ce5051178(
    *,
    bypass_policy_lockout_safety_check: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    description: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    enable_key_rotation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    key_policy: typing.Any = None,
    key_spec: typing.Optional[builtins.str] = None,
    key_usage: typing.Optional[builtins.str] = None,
    multi_region: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    origin: typing.Optional[builtins.str] = None,
    pending_window_in_days: typing.Optional[jsii.Number] = None,
    rotation_period_in_days: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a43b13aecc4a6c9b9c5cce2bd96d2ececdc7c64b21c374cf96c4ab5ead30546b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    key_policy: typing.Any,
    primary_key_arn: builtins.str,
    description: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    pending_window_in_days: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e24eab003d1d7413d435432417d9c001c3be699c66c07b278b9d5cb7ab69fec(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__506b80402bbe68662639797e0c6aabbb40195789ec9827424d8c8b8a760fa7c3(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54fc1b22cb7e48927490c2ff73a5afea9bb5bb4dd8e62a2a6f805d4bb26f967d(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15fbb1b757e713b4a793995a5eb68370a6a6f742705620d66815b734fa8b2547(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__416fb26a5b9f08dd98d1c61865eacaf89a14839e250c7f61ec3485d272103112(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb76d39656831fe315be03ed1109d35bd47e49d418dd22bdc531e5665db1e4c7(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42cf7563707cf3efe01d1caeaa2ca0405b68188335ff4068637d0baa84d85621(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc49d1ede5bfd6f35a0c93dafce91a41f79d39c2119895fac0fb0749478472b9(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e439eab3a0ecab69adc7fd26c12adbbe28fdefe26f6d89d9b6429b95ea8ffb03(
    *,
    key_policy: typing.Any,
    primary_key_arn: builtins.str,
    description: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    pending_window_in_days: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2ffddf2bf6b08c78a62cc0dfd610a5f18de25ac8525da51ce3683ae56ea6333(
    alias: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49ab7698d2a79e6b83d905354157adf61cc66dcdc514e2f6586029179411a56c(
    statement: _PolicyStatement_0fe33853,
    allow_no_op: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e75995ff61f7b73643112ecb31c0f51795b9a98794730d4be368915f8c2593c2(
    grantee: _IGrantable_71c4f5de,
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39902b1c75983f537dc01c509a72cacad7b1f7eac41eb11b78961dad89057e68(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19d45c86cc60f7439a524a94d75c39b726b3b12a4723b2d320f194039f842fcd(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f2582b1d436c32b0e7fbd6af00bad050f74f9e18f1406e20625022b2a13d294(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__678d44f30b3f7854df209779d1ab6c27a0eac432204e7f4ac90a02792d307f03(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e10fb25b1b8146054e097c61432d71d4ae4493eb15e2a482f90f513e686b24ee(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cde9534bdfe7c19d6e24354f8a0de8ca349632d3f565addcaed7e86a84dac7e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    admins: typing.Optional[typing.Sequence[_IPrincipal_539bb2fd]] = None,
    alias: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[builtins.bool] = None,
    enable_key_rotation: typing.Optional[builtins.bool] = None,
    key_spec: typing.Optional[KeySpec] = None,
    key_usage: typing.Optional[KeyUsage] = None,
    pending_window: typing.Optional[_Duration_4839e8c3] = None,
    policy: typing.Optional[_PolicyDocument_3ac34393] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    rotation_period: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44fb03a49b50ed40c1e4dfe9c0db8eb33dbd35e3ee425ee8f32dde09abc3287c(
    cfn_key: CfnKey,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9222dd19331f8774792b2f22b672882512022a23227af13133314719a32a929e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    key_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54c731fe78f9388d4b31695080a02f67600ec386d3b55f25a7274b86edbd4673(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    alias_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c455c06c17802eaffea2f6642f95411cde639deb7ec10fa1d1e54bc6d7babe0(
    alias_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f20e8e11b4cff0f78acc743ad38d02a945f8e93be1f7bfc67153d317f711d06c(
    statement: _PolicyStatement_0fe33853,
    allow_no_op: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3078f1361f1b59b619c5946b92259b4d2eefa0ae12e2e3b01160eae5ce37ceed(
    grantee: _IGrantable_71c4f5de,
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__767164803c663312dbd0dc562333e5aa71475360f03804af0d572d5e1e00b889(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21f59a965699a16e14a1c50712dea7dfff44afb1561561c2ca8c3dc2d510da1d(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b813a815a19cfcc384a90657fd701837adf5051ac8297faee4ede086e7e8ce8(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14a8599a061fbde74d692dfefcfd2f5f92f1a86fc2beee05e7d53c877d7deb03(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__440bf3733f200027c74618bbc6f89d59b060f4aa9d88bb6dbfb057771091f628(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de56bfcabbb83e3ba315f07ba084787bd71e82306a46ddc61555bc4f07b77538(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f5a93b8499d8ef4842a85d33ca3d3de5edce426bd92f9899e4dcda2ebfcf7e0(
    *,
    alias_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3cbd21baa1113e5b2864ce6b440a0d87704642442943c3a554ab23ae712d828(
    *,
    admins: typing.Optional[typing.Sequence[_IPrincipal_539bb2fd]] = None,
    alias: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[builtins.bool] = None,
    enable_key_rotation: typing.Optional[builtins.bool] = None,
    key_spec: typing.Optional[KeySpec] = None,
    key_usage: typing.Optional[KeyUsage] = None,
    pending_window: typing.Optional[_Duration_4839e8c3] = None,
    policy: typing.Optional[_PolicyDocument_3ac34393] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    rotation_period: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__590dd135e934b0f55ab30f9bfcb69bed4ccb0a3ef22f6f3ee9850c4658e2e172(
    service_name: builtins.str,
    base_principal: typing.Optional[_IPrincipal_539bb2fd] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__082e4e34e1b8d1c0e2ca7a3f88ca2fd4db45a02c06b37aa49a92c334ec48b156(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    alias_name: builtins.str,
    target_key: IKey,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1aa4cb540c0255b690750a7c543fa0e6d01be800bf1f1a6d2e27a9ae9821eb9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    alias_name: builtins.str,
    alias_target_key: IKey,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f63f0eacb8d2b482050e953fb9bae15526c96706289c5ec85ff0005315101f4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    alias_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee86459b88002347db31460bea5798240197a80fb17a5bf97c67ed7482f84ae3(
    alias: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b22b27f4615124191ddcb7d43f313a681be5bf126396931e72f2a8086f28d15d(
    statement: _PolicyStatement_0fe33853,
    allow_no_op: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90c67882778cd60cf1af18413a9aaf1ca290ab5a87d50f8929fa64ac66b8923a(
    grantee: _IGrantable_71c4f5de,
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76283f5eae879bc6cabdbf046c1d68b45cbf7e0222f84edb498c04a69b69ad79(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1eddbd590dc8e102f7834fb50d2514218d6a3b73d838b34d7fa52ce858c2c8a(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__765b50233677797d65a2ccab14fdf25c84306d9da9ab54635a10428ed6a23546(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a08117fd4a61f5dbdfb60de37f9aafd66666c36ccbd553402d5504cdd79a06f2(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__889887809ebfcb10b086b9443331082b607fe1c8b476e14ebc492583598f19a2(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass
