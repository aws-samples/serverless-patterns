'''
# AWS Identity and Access Management Construct Library

## Security and Safety Dev Guide

For a detailed guide on CDK security and safety please see the [CDK Security And
Safety Dev Guide](https://github.com/aws/aws-cdk/wiki/Security-And-Safety-Dev-Guide)

The guide will cover topics like:

* What permissions to extend to CDK deployments
* How to control the permissions of CDK deployments via IAM identities and policies
* How to use CDK to configure the IAM identities and policies of deployed applications
* Using Permissions Boundaries with CDK

## Overview

Define a role and add permissions to it. This will automatically create and
attach an IAM policy to the role:

```python
role = Role(self, "MyRole",
    assumed_by=ServicePrincipal("sns.amazonaws.com")
)

role.add_to_policy(PolicyStatement(
    resources=["*"],
    actions=["lambda:InvokeFunction"]
))
```

Define a policy and attach it to groups, users and roles. Note that it is possible to attach
the policy either by calling `xxx.attachInlinePolicy(policy)` or `policy.attachToXxx(xxx)`.

```python
user = User(self, "MyUser", password=SecretValue.plain_text("1234"))
group = Group(self, "MyGroup")

policy = Policy(self, "MyPolicy")
policy.attach_to_user(user)
group.attach_inline_policy(policy)
```

Managed policies can be attached using `xxx.addManagedPolicy(ManagedPolicy.fromAwsManagedPolicyName(policyName))`:

```python
group = Group(self, "MyGroup")
group.add_managed_policy(ManagedPolicy.from_aws_managed_policy_name("AdministratorAccess"))
```

## Granting permissions to resources

Many of the AWS CDK resources have `grant*` methods that allow you to grant other resources access to that resource. As an example, the following code gives a Lambda function write permissions (Put, Update, Delete) to a DynamoDB table.

```python
# fn: lambda.Function
# table: dynamodb.Table


table.grant_write_data(fn)
```

The more generic `grant` method allows you to give specific permissions to a resource:

```python
# fn: lambda.Function
# table: dynamodb.Table


table.grant(fn, "dynamodb:PutItem")
```

The `grant*` methods accept an `IGrantable` object. This interface is implemented by IAM principal resources (groups, users and roles), policies, managed policies and resources that assume a role such as a Lambda function, EC2 instance or a Codebuild project.

You can find which `grant*` methods exist for a resource in the [AWS CDK API Reference](https://docs.aws.amazon.com/cdk/api/latest/docs/aws-construct-library.html).

## Roles

Many AWS resources require *Roles* to operate. These Roles define the AWS API
calls an instance or other AWS service is allowed to make.

Creating Roles and populating them with the right permissions *Statements* is
a necessary but tedious part of setting up AWS infrastructure. In order to
help you focus on your business logic, CDK will take care of creating
roles and populating them with least-privilege permissions automatically.

All constructs that require Roles will create one for you if don't specify
one at construction time. Permissions will be added to that role
automatically if you associate the construct with other constructs from the
AWS Construct Library (for example, if you tell an *AWS CodePipeline* to trigger
an *AWS Lambda Function*, the Pipeline's Role will automatically get
`lambda:InvokeFunction` permissions on that particular Lambda Function),
or if you explicitly grant permissions using `grant` functions (see the
previous section).

### Opting out of automatic permissions management

You may prefer to manage a Role's permissions yourself instead of having the
CDK automatically manage them for you. This may happen in one of the
following cases:

* You don't like the permissions that CDK automatically generates and
  want to substitute your own set.
* The least-permissions policy that the CDK generates is becoming too
  big for IAM to store, and you need to add some wildcards to keep the
  policy size down.

To prevent constructs from updating your Role's policy, pass the object
returned by `myRole.withoutPolicyUpdates()` instead of `myRole` itself.

For example, to have an AWS CodePipeline *not* automatically add the required
permissions to trigger the expected targets, do the following:

```python
role = iam.Role(self, "Role",
    assumed_by=iam.ServicePrincipal("codepipeline.amazonaws.com"),
    # custom description if desired
    description="This is a custom role..."
)

codepipeline.Pipeline(self, "Pipeline",
    # Give the Pipeline an immutable view of the Role
    role=role.without_policy_updates()
)

# You now have to manage the Role policies yourself
role.add_to_policy(iam.PolicyStatement(
    actions=[],
    resources=[]
))
```

### Using existing roles

If there are Roles in your account that have already been created which you
would like to use in your CDK application, you can use `Role.fromRoleArn` to
import them, as follows:

```python
role = iam.Role.from_role_arn(self, "Role", "arn:aws:iam::123456789012:role/MyExistingRole",
    # Set 'mutable' to 'false' to use the role as-is and prevent adding new
    # policies to it. The default is 'true', which means the role may be
    # modified as part of the deployment.
    mutable=False
)
```

### Customizing role creation

It is best practice to allow CDK to manage IAM roles and permissions. You can prevent CDK from
creating roles by using the `customizeRoles` method for special cases. One such case is using CDK in
an environment where role creation is not allowed or needs to be managed through a process outside
of the CDK application.

An example of how to opt in to this behavior is below:

```python
# stack: Stack

iam.Role.customize_roles(stack)
```

CDK will not create any IAM roles or policies with the `stack` scope. `cdk synth` will fail and
it will generate a policy report to the cloud assembly (i.e. cdk.out). The `iam-policy-report.txt`
report will contain a list of IAM roles and associated permissions that would have been created.
This report can be used to create the roles with the appropriate permissions outside of
the CDK application.

Once the missing roles have been created, their names can be added to the `usePrecreatedRoles`
property, like shown below:

```python
# app: App

stack = Stack(app, "MyStack")
iam.Role.customize_roles(self,
    use_precreated_roles={
        "MyStack/MyRole": "my-precreated-role-name"
    }
)

iam.Role(self, "MyRole",
    assumed_by=iam.ServicePrincipal("sns.amazonaws.com")
)
```

If any IAM policies reference deploy time values (i.e. ARN of a resource that hasn't been created
yet) you will have to modify the generated report to be more generic. For example, given the
following CDK code:

```python
# app: App

stack = Stack(app, "MyStack")
iam.Role.customize_roles(stack)

fn = lambda_.Function(self, "MyLambda",
    code=lambda_.InlineCode("foo"),
    handler="index.handler",
    runtime=lambda_.Runtime.NODEJS_LATEST
)

bucket = s3.Bucket(self, "Bucket")
bucket.grant_read(fn)
```

The following report will be generated.

```txt
<missing role> (MyStack/MyLambda/ServiceRole)

AssumeRole Policy:
[
  {
    "Action": "sts:AssumeRole",
    "Effect": "Allow",
    "Principal": {
      "Service": "lambda.amazonaws.com"
    }
  }
]

Managed Policy ARNs:
[
  "arn:(PARTITION):iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
]

Managed Policies Statements:
NONE

Identity Policy Statements:
[
  {
    "Action": [
      "s3:GetObject*",
      "s3:GetBucket*",
      "s3:List*"
    ],
    "Effect": "Allow",
    "Resource": [
      "(MyStack/Bucket/Resource.Arn)",
      "(MyStack/Bucket/Resource.Arn)/*"
    ]
  }
]
```

You would then need to create the role with the inline & managed policies in the report and then
come back and update the `customizeRoles` with the role name.

```python
# app: App

stack = Stack(app, "MyStack")
iam.Role.customize_roles(self,
    use_precreated_roles={
        "MyStack/MyLambda/ServiceRole": "my-role-name"
    }
)
```

For more information on configuring permissions see the [Security And Safety Dev
Guide](https://github.com/aws/aws-cdk/wiki/Security-And-Safety-Dev-Guide)

#### Generating a permissions report

It is also possible to generate the report *without* preventing the role/policy creation.

```python
# stack: Stack

iam.Role.customize_roles(self,
    prevent_synthesis=False
)
```

## Configuring an ExternalId

If you need to create Roles that will be assumed by third parties, it is generally a good idea to [require an `ExternalId`
to assume them](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html).  Configuring
an `ExternalId` works like this:

```python
role = iam.Role(self, "MyRole",
    assumed_by=iam.AccountPrincipal("123456789012"),
    external_ids=["SUPPLY-ME"]
)
```

## SourceArn and SourceAccount

If you need to create resource policies using `aws:SourceArn` and `aws:SourceAccount` for cross-service resource access,
use `addSourceArnCondition` and `addSourceAccountCondition` to create the conditions.

See [Cross-service confused deputy prevention for more details](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html#cross-service-confused-deputy-prevention).

## Principals vs Identities

When we say *Principal*, we mean an entity you grant permissions to. This
entity can be an AWS Service, a Role, or something more abstract such as "all
users in this account" or even "all users in this organization". An
*Identity* is an IAM representing a single IAM entity that can have
a policy attached, one of `Role`, `User`, or `Group`.

## IAM Principals

When defining policy statements as part of an AssumeRole policy or as part of a
resource policy, statements would usually refer to a specific IAM principal
under `Principal`.

IAM principals are modeled as classes that derive from the `iam.PolicyPrincipal`
abstract class. Principal objects include principal type (string) and value
(array of string), optional set of conditions and the action that this principal
requires when it is used in an assume role policy document.

To add a principal to a policy statement you can either use the abstract
`statement.addPrincipal`, one of the concrete `addXxxPrincipal` methods:

* `addAwsPrincipal`, `addArnPrincipal` or `new ArnPrincipal(arn)` for `{ "AWS": arn }`
* `addAwsAccountPrincipal` or `new AccountPrincipal(accountId)` for `{ "AWS": account-arn }`
* `addServicePrincipal` or `new ServicePrincipal(service)` for `{ "Service": service }`
* `addAccountRootPrincipal` or `new AccountRootPrincipal()` for `{ "AWS": { "Ref: "AWS::AccountId" } }`
* `addCanonicalUserPrincipal` or `new CanonicalUserPrincipal(id)` for `{ "CanonicalUser": id }`
* `addFederatedPrincipal` or `new FederatedPrincipal(federated, conditions, assumeAction)` for
  `{ "Federated": arn }` and a set of optional conditions and the assume role action to use.
* `addAnyPrincipal` or `new AnyPrincipal` for `{ "AWS": "*" }`

If multiple principals are added to the policy statement, they will be merged together:

```python
statement = iam.PolicyStatement()
statement.add_service_principal("cloudwatch.amazonaws.com")
statement.add_service_principal("ec2.amazonaws.com")
statement.add_arn_principal("arn:aws:boom:boom")
```

Will result in:

```json
{
  "Principal": {
    "Service": [ "cloudwatch.amazonaws.com", "ec2.amazonaws.com" ],
    "AWS": "arn:aws:boom:boom"
  }
}
```

The `CompositePrincipal` class can also be used to define complex principals, for example:

```python
role = iam.Role(self, "MyRole",
    assumed_by=iam.CompositePrincipal(
        iam.ServicePrincipal("ec2.amazonaws.com"),
        iam.AccountPrincipal("1818188181818187272"))
)
```

The `PrincipalWithConditions` class can be used to add conditions to a
principal, especially those that don't take a `conditions` parameter in their
constructor. The `principal.withConditions()` method can be used to create a
`PrincipalWithConditions` from an existing principal, for example:

```python
principal = iam.AccountPrincipal("123456789000").with_conditions({"StringEquals": {"foo": "baz"}})
```

> NOTE: If you need to define an IAM condition that uses a token (such as a
> deploy-time attribute of another resource) in a JSON map key, use `CfnJson` to
> render this condition. See [this test](./test/integ.condition-with-ref.ts) for
> an example.

The `WebIdentityPrincipal` class can be used as a principal for web identities like
Cognito, Amazon, Google or Facebook, for example:

```python
principal = iam.WebIdentityPrincipal("cognito-identity.amazonaws.com", {
    "StringEquals": {"cognito-identity.amazonaws.com:aud": "us-east-2:12345678-abcd-abcd-abcd-123456"},
    "ForAnyValue:StringLike": {"cognito-identity.amazonaws.com:amr": "unauthenticated"}
})
```

If your identity provider is configured to assume a Role with [session
tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html), you
need to call `.withSessionTags()` to add the required permissions to the Role's
policy document:

```python
iam.Role(self, "Role",
    assumed_by=iam.WebIdentityPrincipal("cognito-identity.amazonaws.com", {
        "StringEquals": {
            "cognito-identity.amazonaws.com:aud": "us-east-2:12345678-abcd-abcd-abcd-123456"
        },
        "ForAnyValue:StringLike": {
            "cognito-identity.amazonaws.com:amr": "unauthenticated"
        }
    }).with_session_tags()
)
```

### Granting a principal permission to assume a role

A principal can be granted permission to assume a role using `grantAssumeRole`.

Note that this does not apply to service principals or account principals as they must be added to the role trust policy via `assumeRolePolicy`.

```python
user = iam.User(self, "user")
role = iam.Role(self, "role",
    assumed_by=iam.AccountPrincipal(self.account)
)

role.grant_assume_role(user)
```

### Granting service and account principals permission to assume a role

Service principals and account principals can be granted permission to assume a role using `assumeRolePolicy` which modifies the role trust policy.

```python
role = iam.Role(self, "role",
    assumed_by=iam.AccountPrincipal(self.account)
)

role.assume_role_policy.add_statements(iam.PolicyStatement(
    actions=["sts:AssumeRole"],
    principals=[
        iam.AccountPrincipal("123456789"),
        iam.ServicePrincipal("beep-boop.amazonaws.com")
    ]
))
```

## Parsing JSON Policy Documents

The `PolicyDocument.fromJson` and `PolicyStatement.fromJson` static methods can be used to parse JSON objects. For example:

```python
policy_document = {
    "Version": "2012-10-17",
    "Statement": [{
        "Sid": "FirstStatement",
        "Effect": "Allow",
        "Action": ["iam:ChangePassword"],
        "Resource": ["*"]
    }, {
        "Sid": "SecondStatement",
        "Effect": "Allow",
        "Action": ["s3:ListAllMyBuckets"],
        "Resource": ["*"]
    }, {
        "Sid": "ThirdStatement",
        "Effect": "Allow",
        "Action": ["s3:List*", "s3:Get*"
        ],
        "Resource": ["arn:aws:s3:::confidential-data", "arn:aws:s3:::confidential-data/*"
        ],
        "Condition": {"Bool": {"aws:_multi_factor_auth_present": "true"}}
    }
    ]
}

custom_policy_document = iam.PolicyDocument.from_json(policy_document)

# You can pass this document as an initial document to a ManagedPolicy
# or inline Policy.
new_managed_policy = iam.ManagedPolicy(self, "MyNewManagedPolicy",
    document=custom_policy_document
)
new_policy = iam.Policy(self, "MyNewPolicy",
    document=custom_policy_document
)
```

## Permissions Boundaries

[Permissions
Boundaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)
can be used as a mechanism to prevent privilege escalation by creating new
`Role`s. Permissions Boundaries are a Managed Policy, attached to Roles or
Users, that represent the *maximum* set of permissions they can have. The
effective set of permissions of a Role (or User) will be the intersection of
the Identity Policy and the Permissions Boundary attached to the Role (or
User). Permissions Boundaries are typically created by account
Administrators, and their use on newly created `Role`s will be enforced by
IAM policies.

### Bootstrap Permissions Boundary

If a permissions boundary has been enforced as part of CDK bootstrap, all IAM
Roles and Users that are created as part of the CDK application must be created
with the permissions boundary attached. The most common scenario will be to
apply the enforced permissions boundary to the entire CDK app. This can be done
either by adding the value to `cdk.json` or directly in the `App` constructor.

For example if your organization has created and is enforcing a permissions
boundary with the name
`cdk-${Qualifier}-PermissionsBoundary`

```json
{
  "context": {
     "@aws-cdk/core:permissionsBoundary": {
	   "name": "cdk-${Qualifier}-PermissionsBoundary"
	 }
  }
}
```

OR

```python
App(
    context={
        "PERMISSIONS_BOUNDARY_CONTEXT_KEY": {
            "name": "cdk-${Qualifier}-PermissionsBoundary"
        }
    }
)
```

Another scenario might be if your organization enforces different permissions
boundaries for different environments. For example your CDK application may have

* `DevStage` that deploys to a personal dev environment where you have elevated
  privileges
* `BetaStage` that deploys to a beta environment which and has a relaxed
  permissions boundary
* `GammaStage` that deploys to a gamma environment which has the prod
  permissions boundary
* `ProdStage` that deploys to the prod environment and has the prod permissions
  boundary

```python
# app: App


Stage(app, "DevStage")

Stage(app, "BetaStage",
    permissions_boundary=PermissionsBoundary.from_name("beta-permissions-boundary")
)

Stage(app, "GammaStage",
    permissions_boundary=PermissionsBoundary.from_name("prod-permissions-boundary")
)

Stage(app, "ProdStage",
    permissions_boundary=PermissionsBoundary.from_name("prod-permissions-boundary")
)
```

The provided name can include placeholders for the partition, region, qualifier, and account
These placeholders will be replaced with the actual values if available. This requires
that the Stack has the environment specified, it does not work with environment.

* '${AWS::Partition}'
* '${AWS::Region}'
* '${AWS::AccountId}'
* '${Qualifier}'

```python
# app: App


prod_stage = Stage(app, "ProdStage",
    permissions_boundary=PermissionsBoundary.from_name("cdk-${Qualifier}-PermissionsBoundary-${AWS::AccountId}-${AWS::Region}")
)

Stack(prod_stage, "ProdStack",
    synthesizer=DefaultStackSynthesizer(
        qualifier="custom"
    )
)
```

For more information on configuring permissions see the [Security And Safety Dev
Guide](https://github.com/aws/aws-cdk/wiki/Security-And-Safety-Dev-Guide)

### Custom Permissions Boundary

It is possible to attach Permissions Boundaries to all Roles created in a construct
tree all at once:

```python
# Directly apply the boundary to a Role you create
# role: iam.Role

# Apply the boundary to an Role that was implicitly created for you
# fn: lambda.Function

# Remove a Permissions Boundary that is inherited, for example from the Stack level
# custom_resource: CustomResource
# This imports an existing policy.
boundary = iam.ManagedPolicy.from_managed_policy_arn(self, "Boundary", "arn:aws:iam::123456789012:policy/boundary")

# This creates a new boundary
boundary2 = iam.ManagedPolicy(self, "Boundary2",
    statements=[
        iam.PolicyStatement(
            effect=iam.Effect.DENY,
            actions=["iam:*"],
            resources=["*"]
        )
    ]
)
iam.PermissionsBoundary.of(role).apply(boundary)
iam.PermissionsBoundary.of(fn).apply(boundary)

# Apply the boundary to all Roles in a stack
iam.PermissionsBoundary.of(self).apply(boundary)
iam.PermissionsBoundary.of(custom_resource).clear()
```

## OpenID Connect Providers

OIDC identity providers are entities in IAM that describe an external identity
provider (IdP) service that supports the [OpenID Connect](http://openid.net/connect) (OIDC) standard, such
as Google or Salesforce. You use an IAM OIDC identity provider when you want to
establish trust between an OIDC-compatible IdP and your AWS account. This is
useful when creating a mobile app or web application that requires access to AWS
resources, but you don't want to create custom sign-in code or manage your own
user identities. For more information about this scenario, see [About Web
Identity Federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc.html) and the relevant documentation in the [Amazon Cognito
Identity Pools Developer Guide](https://docs.aws.amazon.com/cognito/latest/developerguide/open-id.html).

The following examples defines an OpenID Connect provider. Two client IDs
(audiences) are will be able to send authentication requests to
[https://openid/connect](https://openid/connect).

```python
provider = iam.OpenIdConnectProvider(self, "MyProvider",
    url="https://openid/connect",
    client_ids=["myclient1", "myclient2"]
)
```

You can specify an optional list of `thumbprints`. If not specified, the
thumbprint of the root certificate authority (CA) will automatically be obtained
from the host as described
[here](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc_verify-thumbprint.html).

Once you define an OpenID connect provider, you can use it with AWS services
that expect an IAM OIDC provider. For example, when you define an [Amazon
Cognito identity
pool](https://docs.aws.amazon.com/cognito/latest/developerguide/open-id.html)
you can reference the provider's ARN as follows:

```python
import aws_cdk.aws_cognito as cognito

# my_provider: iam.OpenIdConnectProvider

cognito.CfnIdentityPool(self, "IdentityPool",
    open_id_connect_provider_arns=[my_provider.open_id_connect_provider_arn],
    # And the other properties for your identity pool
    allow_unauthenticated_identities=False
)
```

The `OpenIdConnectPrincipal` class can be used as a principal used with a `OpenIdConnectProvider`, for example:

```python
provider = iam.OpenIdConnectProvider(self, "MyProvider",
    url="https://openid/connect",
    client_ids=["myclient1", "myclient2"]
)
principal = iam.OpenIdConnectPrincipal(provider)
```

## SAML provider

An IAM SAML 2.0 identity provider is an entity in IAM that describes an external
identity provider (IdP) service that supports the SAML 2.0 (Security Assertion
Markup Language 2.0) standard. You use an IAM identity provider when you want
to establish trust between a SAML-compatible IdP such as Shibboleth or Active
Directory Federation Services and AWS, so that users in your organization can
access AWS resources. IAM SAML identity providers are used as principals in an
IAM trust policy.

```python
iam.SamlProvider(self, "Provider",
    metadata_document=iam.SamlMetadataDocument.from_file("/path/to/saml-metadata-document.xml")
)
```

The `SamlPrincipal` class can be used as a principal with a `SamlProvider`:

```python
provider = iam.SamlProvider(self, "Provider",
    metadata_document=iam.SamlMetadataDocument.from_file("/path/to/saml-metadata-document.xml")
)
principal = iam.SamlPrincipal(provider, {
    "StringEquals": {
        "SAML:iss": "issuer"
    }
})
```

When creating a role for programmatic and AWS Management Console access, use the `SamlConsolePrincipal`
class:

```python
provider = iam.SamlProvider(self, "Provider",
    metadata_document=iam.SamlMetadataDocument.from_file("/path/to/saml-metadata-document.xml")
)
iam.Role(self, "Role",
    assumed_by=iam.SamlConsolePrincipal(provider)
)
```

## Users

IAM manages users for your AWS account. To create a new user:

```python
user = iam.User(self, "MyUser")
```

To import an existing user by name [with path](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-friendly-names):

```python
user = iam.User.from_user_name(self, "MyImportedUserByName", "johnsmith")
```

To import an existing user by ARN:

```python
user = iam.User.from_user_arn(self, "MyImportedUserByArn", "arn:aws:iam::123456789012:user/johnsmith")
```

To import an existing user by attributes:

```python
user = iam.User.from_user_attributes(self, "MyImportedUserByAttributes",
    user_arn="arn:aws:iam::123456789012:user/johnsmith"
)
```

### Access Keys

The ability for a user to make API calls via the CLI or an SDK is enabled by the user having an
access key pair. To create an access key:

```python
user = iam.User(self, "MyUser")
access_key = iam.AccessKey(self, "MyAccessKey", user=user)
```

You can force CloudFormation to rotate the access key by providing a monotonically increasing `serial`
property. Simply provide a higher serial value than any number used previously:

```python
user = iam.User(self, "MyUser")
access_key = iam.AccessKey(self, "MyAccessKey", user=user, serial=1)
```

An access key may only be associated with a single user and cannot be "moved" between users. Changing
the user associated with an access key replaces the access key (and its ID and secret value).

## Groups

An IAM user group is a collection of IAM users. User groups let you specify permissions for multiple users.

```python
group = iam.Group(self, "MyGroup")
```

To import an existing group by ARN:

```python
group = iam.Group.from_group_arn(self, "MyImportedGroupByArn", "arn:aws:iam::account-id:group/group-name")
```

To import an existing group by name [with path](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-friendly-names):

```python
group = iam.Group.from_group_name(self, "MyImportedGroupByName", "group-name")
```

To add a user to a group (both for a new and imported user/group):

```python
user = iam.User(self, "MyUser") # or User.fromUserName(this, 'User', 'johnsmith');
group = iam.Group(self, "MyGroup") # or Group.fromGroupArn(this, 'Group', 'arn:aws:iam::account-id:group/group-name');

user.add_to_group(group)
# or
group.add_user(user)
```

## Instance Profiles

An IAM instance profile is a container for an IAM role that you can use to pass role information to an EC2 instance when the instance starts. By default, an instance profile must be created with a role:

```python
role = iam.Role(self, "Role",
    assumed_by=iam.ServicePrincipal("ec2.amazonaws.com")
)

instance_profile = iam.InstanceProfile(self, "InstanceProfile",
    role=role
)
```

An instance profile can also optionally be created with an instance profile name and/or a [path](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-friendly-names) to the instance profile:

```python
role = iam.Role(self, "Role",
    assumed_by=iam.ServicePrincipal("ec2.amazonaws.com")
)

instance_profile = iam.InstanceProfile(self, "InstanceProfile",
    role=role,
    instance_profile_name="MyInstanceProfile",
    path="/sample/path/"
)
```

To import an existing instance profile by name:

```python
instance_profile = iam.InstanceProfile.from_instance_profile_name(self, "ImportedInstanceProfile", "MyInstanceProfile")
```

To import an existing instance profile by ARN:

```python
instance_profile = iam.InstanceProfile.from_instance_profile_arn(self, "ImportedInstanceProfile", "arn:aws:iam::account-id:instance-profile/MyInstanceProfile")
```

To import an existing instance profile with an associated role:

```python
role = iam.Role(self, "Role",
    assumed_by=iam.ServicePrincipal("ec2.amazonaws.com")
)

instance_profile = iam.InstanceProfile.from_instance_profile_attributes(self, "ImportedInstanceProfile",
    instance_profile_arn="arn:aws:iam::account-id:instance-profile/MyInstanceProfile",
    role=role
)
```

## Features

* Policy name uniqueness is enforced. If two policies by the same name are attached to the same
  principal, the attachment will fail.
* Policy names are not required - the CDK logical ID will be used and ensured to be unique.
* Policies are validated during synthesis to ensure that they have actions, and that policies
  attached to IAM principals specify relevant resources, while policies attached to resources
  specify which IAM principals they apply to.
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
    IResolveContext as _IResolveContext_b2df1921,
    IResource as _IResource_c80c4260,
    ITaggable as _ITaggable_36806126,
    Resource as _Resource_45bc6135,
    SecretValue as _SecretValue_3dd0ddae,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.AccessKeyProps",
    jsii_struct_bases=[],
    name_mapping={"user": "user", "serial": "serial", "status": "status"},
)
class AccessKeyProps:
    def __init__(
        self,
        *,
        user: "IUser",
        serial: typing.Optional[jsii.Number] = None,
        status: typing.Optional["AccessKeyStatus"] = None,
    ) -> None:
        '''Properties for defining an IAM access key.

        :param user: The IAM user this key will belong to. Changing this value will result in the access key being deleted and a new access key (with a different ID and secret value) being assigned to the new user.
        :param serial: A CloudFormation-specific value that signifies the access key should be replaced/rotated. This value can only be incremented. Incrementing this value will cause CloudFormation to replace the Access Key resource. Default: - No serial value
        :param status: The status of the access key. An Active access key is allowed to be used to make API calls; An Inactive key cannot. Default: - The access key is active

        :exampleMetadata: infused

        Example::

            # Creates a new IAM user, access and secret keys, and stores the secret access key in a Secret.
            user = iam.User(self, "User")
            access_key = iam.AccessKey(self, "AccessKey", user=user)
            secret = secretsmanager.Secret(self, "Secret",
                secret_string_value=access_key.secret_access_key
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7aec9396799d928b7043c068a165e3ad161cc590afe8defeb0ce4ae06ecd9ae)
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
            check_type(argname="argument serial", value=serial, expected_type=type_hints["serial"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "user": user,
        }
        if serial is not None:
            self._values["serial"] = serial
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def user(self) -> "IUser":
        '''The IAM user this key will belong to.

        Changing this value will result in the access key being deleted and a new
        access key (with a different ID and secret value) being assigned to the new
        user.
        '''
        result = self._values.get("user")
        assert result is not None, "Required property 'user' is missing"
        return typing.cast("IUser", result)

    @builtins.property
    def serial(self) -> typing.Optional[jsii.Number]:
        '''A CloudFormation-specific value that signifies the access key should be replaced/rotated.

        This value can only be incremented. Incrementing this
        value will cause CloudFormation to replace the Access Key resource.

        :default: - No serial value
        '''
        result = self._values.get("serial")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def status(self) -> typing.Optional["AccessKeyStatus"]:
        '''The status of the access key.

        An Active access key is allowed to be used
        to make API calls; An Inactive key cannot.

        :default: - The access key is active
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional["AccessKeyStatus"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessKeyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_iam.AccessKeyStatus")
class AccessKeyStatus(enum.Enum):
    '''Valid statuses for an IAM Access Key.'''

    ACTIVE = "ACTIVE"
    '''An active access key.

    An active key can be used to make API calls.
    '''
    INACTIVE = "INACTIVE"
    '''An inactive access key.

    An inactive key cannot be used to make API calls.
    '''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.AddToPrincipalPolicyResult",
    jsii_struct_bases=[],
    name_mapping={
        "statement_added": "statementAdded",
        "policy_dependable": "policyDependable",
    },
)
class AddToPrincipalPolicyResult:
    def __init__(
        self,
        *,
        statement_added: builtins.bool,
        policy_dependable: typing.Optional[_constructs_77d1e7e8.IDependable] = None,
    ) -> None:
        '''Result of calling ``addToPrincipalPolicy``.

        :param statement_added: Whether the statement was added to the identity's policies.
        :param policy_dependable: Dependable which allows depending on the policy change being applied. Default: - Required if ``statementAdded`` is true.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            import constructs as constructs
            
            # dependable: constructs.IDependable
            
            add_to_principal_policy_result = iam.AddToPrincipalPolicyResult(
                statement_added=False,
            
                # the properties below are optional
                policy_dependable=dependable
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c4bef18bd7824d787c934ed761d1626296453e8109e28b61a0c4634f48435dd)
            check_type(argname="argument statement_added", value=statement_added, expected_type=type_hints["statement_added"])
            check_type(argname="argument policy_dependable", value=policy_dependable, expected_type=type_hints["policy_dependable"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "statement_added": statement_added,
        }
        if policy_dependable is not None:
            self._values["policy_dependable"] = policy_dependable

    @builtins.property
    def statement_added(self) -> builtins.bool:
        '''Whether the statement was added to the identity's policies.'''
        result = self._values.get("statement_added")
        assert result is not None, "Required property 'statement_added' is missing"
        return typing.cast(builtins.bool, result)

    @builtins.property
    def policy_dependable(self) -> typing.Optional[_constructs_77d1e7e8.IDependable]:
        '''Dependable which allows depending on the policy change being applied.

        :default: - Required if ``statementAdded`` is true.
        '''
        result = self._values.get("policy_dependable")
        return typing.cast(typing.Optional[_constructs_77d1e7e8.IDependable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AddToPrincipalPolicyResult(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.AddToResourcePolicyResult",
    jsii_struct_bases=[],
    name_mapping={
        "statement_added": "statementAdded",
        "policy_dependable": "policyDependable",
    },
)
class AddToResourcePolicyResult:
    def __init__(
        self,
        *,
        statement_added: builtins.bool,
        policy_dependable: typing.Optional[_constructs_77d1e7e8.IDependable] = None,
    ) -> None:
        '''Result of calling addToResourcePolicy.

        :param statement_added: Whether the statement was added.
        :param policy_dependable: Dependable which allows depending on the policy change being applied. Default: - If ``statementAdded`` is true, the resource object itself. Otherwise, no dependable.

        :exampleMetadata: infused

        Example::

            bucket = s3.Bucket.from_bucket_name(self, "existingBucket", "bucket-name")
            
            # No policy statement will be added to the resource
            result = bucket.add_to_resource_policy(
                iam.PolicyStatement(
                    actions=["s3:GetObject"],
                    resources=[bucket.arn_for_objects("file.txt")],
                    principals=[iam.AccountRootPrincipal()]
                ))
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__828f1cacd29f05b4eed40f202f7b5da1fdf626701e78525463598fc447b5869a)
            check_type(argname="argument statement_added", value=statement_added, expected_type=type_hints["statement_added"])
            check_type(argname="argument policy_dependable", value=policy_dependable, expected_type=type_hints["policy_dependable"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "statement_added": statement_added,
        }
        if policy_dependable is not None:
            self._values["policy_dependable"] = policy_dependable

    @builtins.property
    def statement_added(self) -> builtins.bool:
        '''Whether the statement was added.'''
        result = self._values.get("statement_added")
        assert result is not None, "Required property 'statement_added' is missing"
        return typing.cast(builtins.bool, result)

    @builtins.property
    def policy_dependable(self) -> typing.Optional[_constructs_77d1e7e8.IDependable]:
        '''Dependable which allows depending on the policy change being applied.

        :default:

        - If ``statementAdded`` is true, the resource object itself.
        Otherwise, no dependable.
        '''
        result = self._values.get("policy_dependable")
        return typing.cast(typing.Optional[_constructs_77d1e7e8.IDependable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AddToResourcePolicyResult(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnAccessKey(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.CfnAccessKey",
):
    '''Creates a new AWS secret access key and corresponding AWS access key ID for the specified user.

    The default status for new keys is ``Active`` .

    For information about quotas on the number of keys you can create, see `IAM and AWS STS quotas <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html>`_ in the *IAM User Guide* .
    .. epigraph::

       To ensure the security of your AWS account , the secret access key is accessible only during key and user creation. You must save the key (for example, in a text file) if you want to be able to access it again. If a secret key is lost, you can rotate access keys by increasing the value of the ``serial`` property.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-accesskey.html
    :cloudformationResource: AWS::IAM::AccessKey
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iam as iam
        
        cfn_access_key = iam.CfnAccessKey(self, "MyCfnAccessKey",
            user_name="userName",
        
            # the properties below are optional
            serial=123,
            status="status"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        user_name: builtins.str,
        serial: typing.Optional[jsii.Number] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param user_name: The name of the IAM user that the new key will belong to. This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        :param serial: This value is specific to CloudFormation and can only be *incremented* . Incrementing this value notifies CloudFormation that you want to rotate your access key. When you update your stack, CloudFormation will replace the existing access key with a new key.
        :param status: The status of the access key. ``Active`` means that the key is valid for API calls, while ``Inactive`` means it is not.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d6875d360f4b68d81822160010f3dcab4fad75219310207a67ebdbd76b5d610)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAccessKeyProps(user_name=user_name, serial=serial, status=status)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__253c114f9b2f2b6b08dd9a5564956df556fd7f0ff623cf82d94801cb17f499b2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ab5857eebc55e10a0edcb4b0c6f013af1342700cb0a55e89483e6f8b6d574741)
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
    @jsii.member(jsii_name="attrSecretAccessKey")
    def attr_secret_access_key(self) -> builtins.str:
        '''Returns the secret access key for the specified AWS::IAM::AccessKey resource.

        For example: wJalrXUtnFEMI/K7MDENG/bPxRfiCYzEXAMPLEKEY.

        :cloudformationAttribute: SecretAccessKey
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSecretAccessKey"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="userName")
    def user_name(self) -> builtins.str:
        '''The name of the IAM user that the new key will belong to.'''
        return typing.cast(builtins.str, jsii.get(self, "userName"))

    @user_name.setter
    def user_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3405535e039979434b63eda6cd780e7a68f3036e83c19773aa4cce38e62cfcc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userName", value)

    @builtins.property
    @jsii.member(jsii_name="serial")
    def serial(self) -> typing.Optional[jsii.Number]:
        '''This value is specific to CloudFormation and can only be *incremented* .'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "serial"))

    @serial.setter
    def serial(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de65be3bea4fb6cb4947339490001a6cb74c0e6991d864cd5de95395f19d977b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serial", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of the access key.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c8207c22274bc6fabc3862c3b573f9d71344e354dbd17a00318aa43fa18cb7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.CfnAccessKeyProps",
    jsii_struct_bases=[],
    name_mapping={"user_name": "userName", "serial": "serial", "status": "status"},
)
class CfnAccessKeyProps:
    def __init__(
        self,
        *,
        user_name: builtins.str,
        serial: typing.Optional[jsii.Number] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnAccessKey``.

        :param user_name: The name of the IAM user that the new key will belong to. This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        :param serial: This value is specific to CloudFormation and can only be *incremented* . Incrementing this value notifies CloudFormation that you want to rotate your access key. When you update your stack, CloudFormation will replace the existing access key with a new key.
        :param status: The status of the access key. ``Active`` means that the key is valid for API calls, while ``Inactive`` means it is not.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-accesskey.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            
            cfn_access_key_props = iam.CfnAccessKeyProps(
                user_name="userName",
            
                # the properties below are optional
                serial=123,
                status="status"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8155aca561d14186aae77c5658124546588f321eecca8d6e53a5467862dbddc5)
            check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
            check_type(argname="argument serial", value=serial, expected_type=type_hints["serial"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "user_name": user_name,
        }
        if serial is not None:
            self._values["serial"] = serial
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def user_name(self) -> builtins.str:
        '''The name of the IAM user that the new key will belong to.

        This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-accesskey.html#cfn-iam-accesskey-username
        '''
        result = self._values.get("user_name")
        assert result is not None, "Required property 'user_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def serial(self) -> typing.Optional[jsii.Number]:
        '''This value is specific to CloudFormation and can only be *incremented* .

        Incrementing this value notifies CloudFormation that you want to rotate your access key. When you update your stack, CloudFormation will replace the existing access key with a new key.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-accesskey.html#cfn-iam-accesskey-serial
        '''
        result = self._values.get("serial")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of the access key.

        ``Active`` means that the key is valid for API calls, while ``Inactive`` means it is not.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-accesskey.html#cfn-iam-accesskey-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAccessKeyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.CfnGroup",
):
    '''Creates a new group.

    For information about the number of groups you can create, see `Limitations on IAM Entities <https://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html>`_ in the *IAM User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-group.html
    :cloudformationResource: AWS::IAM::Group
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iam as iam
        
        # policy_document: Any
        
        cfn_group = iam.CfnGroup(self, "MyCfnGroup",
            group_name="groupName",
            managed_policy_arns=["managedPolicyArns"],
            path="path",
            policies=[iam.CfnGroup.PolicyProperty(
                policy_document=policy_document,
                policy_name="policyName"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        group_name: typing.Optional[builtins.str] = None,
        managed_policy_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        path: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGroup.PolicyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param group_name: The name of the group to create. Do not include the path in this value. The group name must be unique within the account. Group names are not distinguished by case. For example, you cannot create groups named both "ADMINS" and "admins". If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the group name. .. epigraph:: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name. If you specify a name, you must specify the ``CAPABILITY_NAMED_IAM`` value to acknowledge your template's capabilities. For more information, see `Acknowledging IAM Resources in AWS CloudFormation Templates <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-capabilities>`_ . .. epigraph:: Naming an IAM resource can cause an unrecoverable error if you reuse the same template in multiple Regions. To prevent this, we recommend using ``Fn::Join`` and ``AWS::Region`` to create a Region-specific name, as in the following example: ``{"Fn::Join": ["", [{"Ref": "AWS::Region"}, {"Ref": "MyResourceName"}]]}`` .
        :param managed_policy_arns: The Amazon Resource Name (ARN) of the IAM policy you want to attach. For more information about ARNs, see `Amazon Resource Names (ARNs) <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .
        :param path: The path to the group. For more information about paths, see `IAM identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`_ in the *IAM User Guide* . This parameter is optional. If it is not included, it defaults to a slash (/). This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! ( ``\\u0021`` ) through the DEL character ( ``\\u007F`` ), including most punctuation characters, digits, and upper and lowercased letters.
        :param policies: Adds or updates an inline policy document that is embedded in the specified IAM group. To view AWS::IAM::Group snippets, see `Declaring an IAM Group Resource <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-iam.html#scenario-iam-group>`_ . .. epigraph:: The name of each inline policy for a role, user, or group must be unique. If you don't choose unique names, updates to the IAM identity will fail. For information about limits on the number of inline policies that you can embed in a group, see `Limitations on IAM Entities <https://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html>`_ in the *IAM User Guide* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20b2c419e0a9df4f72befe689959dc5d68aff361365a09c398c4a5645df50b18)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGroupProps(
            group_name=group_name,
            managed_policy_arns=managed_policy_arns,
            path=path,
            policies=policies,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cd8f3cc95c07c18415e709564850ea545ed675e3f0b6e3505e763a15b48e963)
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
            type_hints = typing.get_type_hints(_typecheckingstub__89278b67425b9a0f94f61235c7282945d071b501bc7b15f85a485662ff826258)
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
        '''Returns the Amazon Resource Name (ARN) for the specified ``AWS::IAM::Group`` resource.

        For example: ``arn:aws:iam::123456789012:group/mystack-mygroup-1DZETITOWEKVO`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="groupName")
    def group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the group to create.

        Do not include the path in this value.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupName"))

    @group_name.setter
    def group_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01be7e8dfd9fda0df1899d3026531e8a38a22b7e1f2d6027c883cf4d505c3d51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupName", value)

    @builtins.property
    @jsii.member(jsii_name="managedPolicyArns")
    def managed_policy_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Amazon Resource Name (ARN) of the IAM policy you want to attach.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "managedPolicyArns"))

    @managed_policy_arns.setter
    def managed_policy_arns(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a267baaf187cde3f3930ebef9cdd1a754591f3f54b47d9729cc1d9bb3a93458)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedPolicyArns", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> typing.Optional[builtins.str]:
        '''The path to the group.

        For more information about paths, see `IAM identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`_ in the *IAM User Guide* .
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "path"))

    @path.setter
    def path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b014a61027fdb2afb518b56e4a64ca65934df00a511ae153c21193094d07e4ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="policies")
    def policies(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGroup.PolicyProperty"]]]]:
        '''Adds or updates an inline policy document that is embedded in the specified IAM group.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGroup.PolicyProperty"]]]], jsii.get(self, "policies"))

    @policies.setter
    def policies(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGroup.PolicyProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a23f252d3f662bbd9b85e3ee272df167b08d0ce70d4a20ac116d5b1cb15a44e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policies", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iam.CfnGroup.PolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "policy_document": "policyDocument",
            "policy_name": "policyName",
        },
    )
    class PolicyProperty:
        def __init__(
            self,
            *,
            policy_document: typing.Any,
            policy_name: builtins.str,
        ) -> None:
            '''Contains information about an attached policy.

            An attached policy is a managed policy that has been attached to a user, group, or role.

            For more information about managed policies, see `Managed Policies and Inline Policies <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`_ in the *IAM User Guide* .

            :param policy_document: The policy document.
            :param policy_name: The friendly name (not ARN) identifying the policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group-policy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iam as iam
                
                # policy_document: Any
                
                policy_property = iam.CfnGroup.PolicyProperty(
                    policy_document=policy_document,
                    policy_name="policyName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5381732fad8dcd5499b3b303273fdd9097ec896987b47080216d0c734f18d9a8)
                check_type(argname="argument policy_document", value=policy_document, expected_type=type_hints["policy_document"])
                check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "policy_document": policy_document,
                "policy_name": policy_name,
            }

        @builtins.property
        def policy_document(self) -> typing.Any:
            '''The policy document.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group-policy.html#cfn-iam-group-policy-policydocument
            '''
            result = self._values.get("policy_document")
            assert result is not None, "Required property 'policy_document' is missing"
            return typing.cast(typing.Any, result)

        @builtins.property
        def policy_name(self) -> builtins.str:
            '''The friendly name (not ARN) identifying the policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group-policy.html#cfn-iam-group-policy-policyname
            '''
            result = self._values.get("policy_name")
            assert result is not None, "Required property 'policy_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnGroupPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.CfnGroupPolicy",
):
    '''Adds or updates an inline policy document that is embedded in the specified IAM group.

    A group can also have managed policies attached to it. To attach a managed policy to a group, use ```AWS::IAM::Group`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html>`_ . To create a new managed policy, use ```AWS::IAM::ManagedPolicy`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html>`_ . For information about policies, see `Managed policies and inline policies <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`_ in the *IAM User Guide* .

    For information about the maximum number of inline policies that you can embed in a group, see `IAM and AWS STS quotas <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html>`_ in the *IAM User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-grouppolicy.html
    :cloudformationResource: AWS::IAM::GroupPolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iam as iam
        
        # policy_document: Any
        
        cfn_group_policy = iam.CfnGroupPolicy(self, "MyCfnGroupPolicy",
            group_name="groupName",
            policy_name="policyName",
        
            # the properties below are optional
            policy_document=policy_document
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        group_name: builtins.str,
        policy_name: builtins.str,
        policy_document: typing.Any = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param group_name: The name of the group to associate the policy with. This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-.
        :param policy_name: The name of the policy document. This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        :param policy_document: The policy document. You must provide policies in JSON format in IAM. However, for AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it to IAM. The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ used to validate this parameter is a string of characters consisting of the following: - Any printable ASCII character ranging from the space character ( ``\\u0020`` ) through the end of the ASCII character range - The printable characters in the Basic Latin and Latin-1 Supplement character set (through ``\\u00FF`` ) - The special characters tab ( ``\\u0009`` ), line feed ( ``\\u000A`` ), and carriage return ( ``\\u000D`` )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f890caaa5f6b29722a17bf5c714640d202cb740a7f07aec5a5ced9b53eed348)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGroupPolicyProps(
            group_name=group_name,
            policy_name=policy_name,
            policy_document=policy_document,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79a0026280df7e0717ed9e16473b60d33a900f8870446901848eb1af15bc48c1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ef5341af0b1e6f12f150e9d4694149341aec7aa000971cb5f25b0b9672a631cd)
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
    @jsii.member(jsii_name="groupName")
    def group_name(self) -> builtins.str:
        '''The name of the group to associate the policy with.'''
        return typing.cast(builtins.str, jsii.get(self, "groupName"))

    @group_name.setter
    def group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__789fa1310fa5f0c8a58c7721ec65bb7fb38294aa983f688e92a477a4ecf7a44c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupName", value)

    @builtins.property
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        '''The name of the policy document.'''
        return typing.cast(builtins.str, jsii.get(self, "policyName"))

    @policy_name.setter
    def policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98fde951f7da16e6788d849111dc918395ada4b5134156e2bc4d29caf92e119f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyName", value)

    @builtins.property
    @jsii.member(jsii_name="policyDocument")
    def policy_document(self) -> typing.Any:
        '''The policy document.'''
        return typing.cast(typing.Any, jsii.get(self, "policyDocument"))

    @policy_document.setter
    def policy_document(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__252a63b1958f4306e76e5da346149aa1087fd66fc85306f6c6c58ab5571644a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyDocument", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.CfnGroupPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "group_name": "groupName",
        "policy_name": "policyName",
        "policy_document": "policyDocument",
    },
)
class CfnGroupPolicyProps:
    def __init__(
        self,
        *,
        group_name: builtins.str,
        policy_name: builtins.str,
        policy_document: typing.Any = None,
    ) -> None:
        '''Properties for defining a ``CfnGroupPolicy``.

        :param group_name: The name of the group to associate the policy with. This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-.
        :param policy_name: The name of the policy document. This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        :param policy_document: The policy document. You must provide policies in JSON format in IAM. However, for AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it to IAM. The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ used to validate this parameter is a string of characters consisting of the following: - Any printable ASCII character ranging from the space character ( ``\\u0020`` ) through the end of the ASCII character range - The printable characters in the Basic Latin and Latin-1 Supplement character set (through ``\\u00FF`` ) - The special characters tab ( ``\\u0009`` ), line feed ( ``\\u000A`` ), and carriage return ( ``\\u000D`` )

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-grouppolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            
            # policy_document: Any
            
            cfn_group_policy_props = iam.CfnGroupPolicyProps(
                group_name="groupName",
                policy_name="policyName",
            
                # the properties below are optional
                policy_document=policy_document
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa640a2b964f19199ce54686b7fd65c710619c4f560d010f4b3ceaac824c022b)
            check_type(argname="argument group_name", value=group_name, expected_type=type_hints["group_name"])
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
            check_type(argname="argument policy_document", value=policy_document, expected_type=type_hints["policy_document"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "group_name": group_name,
            "policy_name": policy_name,
        }
        if policy_document is not None:
            self._values["policy_document"] = policy_document

    @builtins.property
    def group_name(self) -> builtins.str:
        '''The name of the group to associate the policy with.

        This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-grouppolicy.html#cfn-iam-grouppolicy-groupname
        '''
        result = self._values.get("group_name")
        assert result is not None, "Required property 'group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_name(self) -> builtins.str:
        '''The name of the policy document.

        This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-grouppolicy.html#cfn-iam-grouppolicy-policyname
        '''
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_document(self) -> typing.Any:
        '''The policy document.

        You must provide policies in JSON format in IAM. However, for AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it to IAM.

        The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ used to validate this parameter is a string of characters consisting of the following:

        - Any printable ASCII character ranging from the space character ( ``\\u0020`` ) through the end of the ASCII character range
        - The printable characters in the Basic Latin and Latin-1 Supplement character set (through ``\\u00FF`` )
        - The special characters tab ( ``\\u0009`` ), line feed ( ``\\u000A`` ), and carriage return ( ``\\u000D`` )

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-grouppolicy.html#cfn-iam-grouppolicy-policydocument
        '''
        result = self._values.get("policy_document")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.CfnGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "group_name": "groupName",
        "managed_policy_arns": "managedPolicyArns",
        "path": "path",
        "policies": "policies",
    },
)
class CfnGroupProps:
    def __init__(
        self,
        *,
        group_name: typing.Optional[builtins.str] = None,
        managed_policy_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        path: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGroup.PolicyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnGroup``.

        :param group_name: The name of the group to create. Do not include the path in this value. The group name must be unique within the account. Group names are not distinguished by case. For example, you cannot create groups named both "ADMINS" and "admins". If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the group name. .. epigraph:: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name. If you specify a name, you must specify the ``CAPABILITY_NAMED_IAM`` value to acknowledge your template's capabilities. For more information, see `Acknowledging IAM Resources in AWS CloudFormation Templates <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-capabilities>`_ . .. epigraph:: Naming an IAM resource can cause an unrecoverable error if you reuse the same template in multiple Regions. To prevent this, we recommend using ``Fn::Join`` and ``AWS::Region`` to create a Region-specific name, as in the following example: ``{"Fn::Join": ["", [{"Ref": "AWS::Region"}, {"Ref": "MyResourceName"}]]}`` .
        :param managed_policy_arns: The Amazon Resource Name (ARN) of the IAM policy you want to attach. For more information about ARNs, see `Amazon Resource Names (ARNs) <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .
        :param path: The path to the group. For more information about paths, see `IAM identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`_ in the *IAM User Guide* . This parameter is optional. If it is not included, it defaults to a slash (/). This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! ( ``\\u0021`` ) through the DEL character ( ``\\u007F`` ), including most punctuation characters, digits, and upper and lowercased letters.
        :param policies: Adds or updates an inline policy document that is embedded in the specified IAM group. To view AWS::IAM::Group snippets, see `Declaring an IAM Group Resource <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-iam.html#scenario-iam-group>`_ . .. epigraph:: The name of each inline policy for a role, user, or group must be unique. If you don't choose unique names, updates to the IAM identity will fail. For information about limits on the number of inline policies that you can embed in a group, see `Limitations on IAM Entities <https://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html>`_ in the *IAM User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-group.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            
            # policy_document: Any
            
            cfn_group_props = iam.CfnGroupProps(
                group_name="groupName",
                managed_policy_arns=["managedPolicyArns"],
                path="path",
                policies=[iam.CfnGroup.PolicyProperty(
                    policy_document=policy_document,
                    policy_name="policyName"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83c00814903fe43cbe21eca7faddcd90dcea9ec971aac6d8d2daf6b50f845df0)
            check_type(argname="argument group_name", value=group_name, expected_type=type_hints["group_name"])
            check_type(argname="argument managed_policy_arns", value=managed_policy_arns, expected_type=type_hints["managed_policy_arns"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument policies", value=policies, expected_type=type_hints["policies"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if group_name is not None:
            self._values["group_name"] = group_name
        if managed_policy_arns is not None:
            self._values["managed_policy_arns"] = managed_policy_arns
        if path is not None:
            self._values["path"] = path
        if policies is not None:
            self._values["policies"] = policies

    @builtins.property
    def group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the group to create. Do not include the path in this value.

        The group name must be unique within the account. Group names are not distinguished by case. For example, you cannot create groups named both "ADMINS" and "admins". If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the group name.
        .. epigraph::

           If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.

        If you specify a name, you must specify the ``CAPABILITY_NAMED_IAM`` value to acknowledge your template's capabilities. For more information, see `Acknowledging IAM Resources in AWS CloudFormation Templates <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-capabilities>`_ .
        .. epigraph::

           Naming an IAM resource can cause an unrecoverable error if you reuse the same template in multiple Regions. To prevent this, we recommend using ``Fn::Join`` and ``AWS::Region`` to create a Region-specific name, as in the following example: ``{"Fn::Join": ["", [{"Ref": "AWS::Region"}, {"Ref": "MyResourceName"}]]}`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-group.html#cfn-iam-group-groupname
        '''
        result = self._values.get("group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def managed_policy_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Amazon Resource Name (ARN) of the IAM policy you want to attach.

        For more information about ARNs, see `Amazon Resource Names (ARNs) <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-group.html#cfn-iam-group-managedpolicyarns
        '''
        result = self._values.get("managed_policy_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''The path to the group. For more information about paths, see `IAM identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`_ in the *IAM User Guide* .

        This parameter is optional. If it is not included, it defaults to a slash (/).

        This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! ( ``\\u0021`` ) through the DEL character ( ``\\u007F`` ), including most punctuation characters, digits, and upper and lowercased letters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-group.html#cfn-iam-group-path
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policies(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGroup.PolicyProperty]]]]:
        '''Adds or updates an inline policy document that is embedded in the specified IAM group.

        To view AWS::IAM::Group snippets, see `Declaring an IAM Group Resource <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-iam.html#scenario-iam-group>`_ .
        .. epigraph::

           The name of each inline policy for a role, user, or group must be unique. If you don't choose unique names, updates to the IAM identity will fail.

        For information about limits on the number of inline policies that you can embed in a group, see `Limitations on IAM Entities <https://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html>`_ in the *IAM User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-group.html#cfn-iam-group-policies
        '''
        result = self._values.get("policies")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGroup.PolicyProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnInstanceProfile(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.CfnInstanceProfile",
):
    '''Creates a new instance profile. For information about instance profiles, see `Using instance profiles <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html>`_ .

    For information about the number of instance profiles you can create, see `IAM object quotas <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html>`_ in the *IAM User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html
    :cloudformationResource: AWS::IAM::InstanceProfile
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iam as iam
        
        cfn_instance_profile = iam.CfnInstanceProfile(self, "MyCfnInstanceProfile",
            roles=["roles"],
        
            # the properties below are optional
            instance_profile_name="instanceProfileName",
            path="path"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        roles: typing.Sequence[builtins.str],
        instance_profile_name: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param roles: The name of the role to associate with the instance profile. Only one role can be assigned to an EC2 instance at a time, and all applications on the instance share the same role and permissions.
        :param instance_profile_name: The name of the instance profile to create. This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        :param path: The path to the instance profile. For more information about paths, see `IAM Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`_ in the *IAM User Guide* . This parameter is optional. If it is not included, it defaults to a slash (/). This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! ( ``\\u0021`` ) through the DEL character ( ``\\u007F`` ), including most punctuation characters, digits, and upper and lowercased letters.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31ec5f0ea7f9ac49e8ad53cc5faa514c2ff04ae0962ad9e9fb0274b3c7f7b0b4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnInstanceProfileProps(
            roles=roles, instance_profile_name=instance_profile_name, path=path
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__014a9e16c0ce84f545ddc2fd74080cc35e47d194639e0b8133383c054c81a206)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7ea1d50531a33bafd660573c8a2e3a8e5e0215acf7462185f0959ea67f61bee5)
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
        '''Returns the Amazon Resource Name (ARN) for the instance profile. For example:.

        ``{"Fn::GetAtt" : ["MyProfile", "Arn"] }``

        This returns a value such as ``arn:aws:iam::1234567890:instance-profile/MyProfile-ASDNSDLKJ`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="roles")
    def roles(self) -> typing.List[builtins.str]:
        '''The name of the role to associate with the instance profile.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "roles"))

    @roles.setter
    def roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__785f95fb95c2bbe41d514dea64d18cfcbfa66bffbfa2d083ae501bdd37a0fe4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roles", value)

    @builtins.property
    @jsii.member(jsii_name="instanceProfileName")
    def instance_profile_name(self) -> typing.Optional[builtins.str]:
        '''The name of the instance profile to create.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceProfileName"))

    @instance_profile_name.setter
    def instance_profile_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94d5332482fea97767ec730f2c1930a5e4ec68efce72124dd1cfd7a7c5f40bba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceProfileName", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> typing.Optional[builtins.str]:
        '''The path to the instance profile.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "path"))

    @path.setter
    def path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbfe487716a390ca26e092b03b19bce39babeaa672e667fad6be4aed43f11cf4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.CfnInstanceProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "roles": "roles",
        "instance_profile_name": "instanceProfileName",
        "path": "path",
    },
)
class CfnInstanceProfileProps:
    def __init__(
        self,
        *,
        roles: typing.Sequence[builtins.str],
        instance_profile_name: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnInstanceProfile``.

        :param roles: The name of the role to associate with the instance profile. Only one role can be assigned to an EC2 instance at a time, and all applications on the instance share the same role and permissions.
        :param instance_profile_name: The name of the instance profile to create. This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        :param path: The path to the instance profile. For more information about paths, see `IAM Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`_ in the *IAM User Guide* . This parameter is optional. If it is not included, it defaults to a slash (/). This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! ( ``\\u0021`` ) through the DEL character ( ``\\u007F`` ), including most punctuation characters, digits, and upper and lowercased letters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            
            cfn_instance_profile_props = iam.CfnInstanceProfileProps(
                roles=["roles"],
            
                # the properties below are optional
                instance_profile_name="instanceProfileName",
                path="path"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13af24b231dab76416337b37eed1fc0eb441fa93214942c4f328be745d78987f)
            check_type(argname="argument roles", value=roles, expected_type=type_hints["roles"])
            check_type(argname="argument instance_profile_name", value=instance_profile_name, expected_type=type_hints["instance_profile_name"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "roles": roles,
        }
        if instance_profile_name is not None:
            self._values["instance_profile_name"] = instance_profile_name
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def roles(self) -> typing.List[builtins.str]:
        '''The name of the role to associate with the instance profile.

        Only one role can be assigned to an EC2 instance at a time, and all applications on the instance share the same role and permissions.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html#cfn-iam-instanceprofile-roles
        '''
        result = self._values.get("roles")
        assert result is not None, "Required property 'roles' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def instance_profile_name(self) -> typing.Optional[builtins.str]:
        '''The name of the instance profile to create.

        This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html#cfn-iam-instanceprofile-instanceprofilename
        '''
        result = self._values.get("instance_profile_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''The path to the instance profile.

        For more information about paths, see `IAM Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`_ in the *IAM User Guide* .

        This parameter is optional. If it is not included, it defaults to a slash (/).

        This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! ( ``\\u0021`` ) through the DEL character ( ``\\u007F`` ), including most punctuation characters, digits, and upper and lowercased letters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html#cfn-iam-instanceprofile-path
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInstanceProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnManagedPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.CfnManagedPolicy",
):
    '''Creates a new managed policy for your AWS account .

    This operation creates a policy version with a version identifier of ``v1`` and sets v1 as the policy's default version. For more information about policy versions, see `Versioning for managed policies <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-versions.html>`_ in the *IAM User Guide* .

    As a best practice, you can validate your IAM policies. To learn more, see `Validating IAM policies <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_policy-validator.html>`_ in the *IAM User Guide* .

    For more information about managed policies in general, see `Managed policies and inline policies <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`_ in the *IAM User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html
    :cloudformationResource: AWS::IAM::ManagedPolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iam as iam
        
        # policy_document: Any
        
        cfn_managed_policy = iam.CfnManagedPolicy(self, "MyCfnManagedPolicy",
            policy_document=policy_document,
        
            # the properties below are optional
            description="description",
            groups=["groups"],
            managed_policy_name="managedPolicyName",
            path="path",
            roles=["roles"],
            users=["users"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        policy_document: typing.Any,
        description: typing.Optional[builtins.str] = None,
        groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        managed_policy_name: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        users: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param policy_document: The JSON policy document that you want to use as the content for the new policy. You must provide policies in JSON format in IAM. However, for AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it to IAM. The maximum length of the policy document that you can pass in this operation, including whitespace, is listed below. To view the maximum character counts of a managed policy with no whitespaces, see `IAM and AWS STS character quotas <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html#reference_iam-quotas-entity-length>`_ . To learn more about JSON policy grammar, see `Grammar of the IAM JSON policy language <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_grammar.html>`_ in the *IAM User Guide* . The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ used to validate this parameter is a string of characters consisting of the following: - Any printable ASCII character ranging from the space character ( ``\\u0020`` ) through the end of the ASCII character range - The printable characters in the Basic Latin and Latin-1 Supplement character set (through ``\\u00FF`` ) - The special characters tab ( ``\\u0009`` ), line feed ( ``\\u000A`` ), and carriage return ( ``\\u000D`` )
        :param description: A friendly description of the policy. Typically used to store information about the permissions defined in the policy. For example, "Grants access to production DynamoDB tables." The policy description is immutable. After a value is assigned, it cannot be changed.
        :param groups: The name (friendly name, not ARN) of the group to attach the policy to. This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        :param managed_policy_name: The friendly name of the policy. .. epigraph:: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name. If you specify a name, you must specify the ``CAPABILITY_NAMED_IAM`` value to acknowledge your template's capabilities. For more information, see `Acknowledging IAM Resources in AWS CloudFormation Templates <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-capabilities>`_ . .. epigraph:: Naming an IAM resource can cause an unrecoverable error if you reuse the same template in multiple Regions. To prevent this, we recommend using ``Fn::Join`` and ``AWS::Region`` to create a Region-specific name, as in the following example: ``{"Fn::Join": ["", [{"Ref": "AWS::Region"}, {"Ref": "MyResourceName"}]]}`` .
        :param path: The path for the policy. For more information about paths, see `IAM identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`_ in the *IAM User Guide* . This parameter is optional. If it is not included, it defaults to a slash (/). This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! ( ``\\u0021`` ) through the DEL character ( ``\\u007F`` ), including most punctuation characters, digits, and upper and lowercased letters. .. epigraph:: You cannot use an asterisk (*) in the path name. Default: - "/"
        :param roles: The name (friendly name, not ARN) of the role to attach the policy to. This parameter allows (per its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@- .. epigraph:: If an external policy (such as ``AWS::IAM::Policy`` or ``AWS::IAM::ManagedPolicy`` ) has a ``Ref`` to a role and if a resource (such as ``AWS::ECS::Service`` ) also has a ``Ref`` to the same role, add a ``DependsOn`` attribute to the resource to make the resource depend on the external policy. This dependency ensures that the role's policy is available throughout the resource's lifecycle. For example, when you delete a stack with an ``AWS::ECS::Service`` resource, the ``DependsOn`` attribute ensures that AWS CloudFormation deletes the ``AWS::ECS::Service`` resource before deleting its role's policy.
        :param users: The name (friendly name, not ARN) of the IAM user to attach the policy to. This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a8c17449d46e088e632540cdf9eb1a587f03d90f16e24cec8b7c30c9962df64)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnManagedPolicyProps(
            policy_document=policy_document,
            description=description,
            groups=groups,
            managed_policy_name=managed_policy_name,
            path=path,
            roles=roles,
            users=users,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a722cb81ff9cd42fafa9ac5e408b6c1bfdb242f04cc4ae98a8ea3a1b79fdbfd2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__49691612ad6d051c64843fc36b88e2a32e132ab38af6120ecf52699776f24808)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAttachmentCount")
    def attr_attachment_count(self) -> jsii.Number:
        '''The number of principal entities (users, groups, and roles) that the policy is attached to.

        :cloudformationAttribute: AttachmentCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrAttachmentCount"))

    @builtins.property
    @jsii.member(jsii_name="attrCreateDate")
    def attr_create_date(self) -> builtins.str:
        '''The date and time, in `ISO 8601 date-time format <https://docs.aws.amazon.com/http://www.iso.org/iso/iso8601>`_ , when the policy was created.

        :cloudformationAttribute: CreateDate
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreateDate"))

    @builtins.property
    @jsii.member(jsii_name="attrDefaultVersionId")
    def attr_default_version_id(self) -> builtins.str:
        '''The identifier for the version of the policy that is set as the default (operative) version.

        For more information about policy versions, see `Versioning for managed policies <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-versions.html>`_ in the *IAM User Guide* .

        :cloudformationAttribute: DefaultVersionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDefaultVersionId"))

    @builtins.property
    @jsii.member(jsii_name="attrIsAttachable")
    def attr_is_attachable(self) -> _IResolvable_da3f097b:
        '''Specifies whether the policy can be attached to an IAM user, group, or role.

        :cloudformationAttribute: IsAttachable
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrIsAttachable"))

    @builtins.property
    @jsii.member(jsii_name="attrPermissionsBoundaryUsageCount")
    def attr_permissions_boundary_usage_count(self) -> jsii.Number:
        '''The number of entities (users and roles) for which the policy is used as the permissions boundary.

        For more information about permissions boundaries, see `Permissions boundaries for IAM identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`_ in the *IAM User Guide* .

        :cloudformationAttribute: PermissionsBoundaryUsageCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrPermissionsBoundaryUsageCount"))

    @builtins.property
    @jsii.member(jsii_name="attrPolicyArn")
    def attr_policy_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: PolicyArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPolicyArn"))

    @builtins.property
    @jsii.member(jsii_name="attrPolicyId")
    def attr_policy_id(self) -> builtins.str:
        '''The stable and unique string identifying the policy.

        For more information about IDs, see `IAM identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`_ in the *IAM User Guide* .

        :cloudformationAttribute: PolicyId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPolicyId"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdateDate")
    def attr_update_date(self) -> builtins.str:
        '''The date and time, in `ISO 8601 date-time format <https://docs.aws.amazon.com/http://www.iso.org/iso/iso8601>`_ , when the policy was last updated.

        When a policy has only one version, this field contains the date and time when the policy was created. When a policy has more than one version, this field contains the date and time when the most recent policy version was created.

        :cloudformationAttribute: UpdateDate
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdateDate"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="policyDocument")
    def policy_document(self) -> typing.Any:
        '''The JSON policy document that you want to use as the content for the new policy.'''
        return typing.cast(typing.Any, jsii.get(self, "policyDocument"))

    @policy_document.setter
    def policy_document(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57f5af0ac55173154c340115659691a27fc295c9250c8d5ca198109f64466ee8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyDocument", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A friendly description of the policy.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cc04fd5744afbd3cf5d35eec5e89c42dc47f150557ef85988e2e74ea873c422)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="groups")
    def groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The name (friendly name, not ARN) of the group to attach the policy to.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groups"))

    @groups.setter
    def groups(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc185a3adf8688a003c343f2c7f2d2213871db292b02bf41ab584d89834d560d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groups", value)

    @builtins.property
    @jsii.member(jsii_name="managedPolicyName")
    def managed_policy_name(self) -> typing.Optional[builtins.str]:
        '''The friendly name of the policy.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managedPolicyName"))

    @managed_policy_name.setter
    def managed_policy_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad4dd76c35346216139c78ee6af3ca0521328f8eeab6374f6ea5d0c3af2b9886)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedPolicyName", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> typing.Optional[builtins.str]:
        '''The path for the policy.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "path"))

    @path.setter
    def path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55edad48d274800976c6721903c6c5c63dd8559011473654245716943a0e2895)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="roles")
    def roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The name (friendly name, not ARN) of the role to attach the policy to.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "roles"))

    @roles.setter
    def roles(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1de9b6a5aa5082e09fb07840ea3cdfca3eb8553aa46fd492dbb181b5362f13b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roles", value)

    @builtins.property
    @jsii.member(jsii_name="users")
    def users(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The name (friendly name, not ARN) of the IAM user to attach the policy to.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "users"))

    @users.setter
    def users(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ad59cd00d0e0ac909d310dbcbbd6e052d1f131f984c456d7dec6c6d0f890843)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "users", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.CfnManagedPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "policy_document": "policyDocument",
        "description": "description",
        "groups": "groups",
        "managed_policy_name": "managedPolicyName",
        "path": "path",
        "roles": "roles",
        "users": "users",
    },
)
class CfnManagedPolicyProps:
    def __init__(
        self,
        *,
        policy_document: typing.Any,
        description: typing.Optional[builtins.str] = None,
        groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        managed_policy_name: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        users: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnManagedPolicy``.

        :param policy_document: The JSON policy document that you want to use as the content for the new policy. You must provide policies in JSON format in IAM. However, for AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it to IAM. The maximum length of the policy document that you can pass in this operation, including whitespace, is listed below. To view the maximum character counts of a managed policy with no whitespaces, see `IAM and AWS STS character quotas <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html#reference_iam-quotas-entity-length>`_ . To learn more about JSON policy grammar, see `Grammar of the IAM JSON policy language <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_grammar.html>`_ in the *IAM User Guide* . The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ used to validate this parameter is a string of characters consisting of the following: - Any printable ASCII character ranging from the space character ( ``\\u0020`` ) through the end of the ASCII character range - The printable characters in the Basic Latin and Latin-1 Supplement character set (through ``\\u00FF`` ) - The special characters tab ( ``\\u0009`` ), line feed ( ``\\u000A`` ), and carriage return ( ``\\u000D`` )
        :param description: A friendly description of the policy. Typically used to store information about the permissions defined in the policy. For example, "Grants access to production DynamoDB tables." The policy description is immutable. After a value is assigned, it cannot be changed.
        :param groups: The name (friendly name, not ARN) of the group to attach the policy to. This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        :param managed_policy_name: The friendly name of the policy. .. epigraph:: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name. If you specify a name, you must specify the ``CAPABILITY_NAMED_IAM`` value to acknowledge your template's capabilities. For more information, see `Acknowledging IAM Resources in AWS CloudFormation Templates <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-capabilities>`_ . .. epigraph:: Naming an IAM resource can cause an unrecoverable error if you reuse the same template in multiple Regions. To prevent this, we recommend using ``Fn::Join`` and ``AWS::Region`` to create a Region-specific name, as in the following example: ``{"Fn::Join": ["", [{"Ref": "AWS::Region"}, {"Ref": "MyResourceName"}]]}`` .
        :param path: The path for the policy. For more information about paths, see `IAM identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`_ in the *IAM User Guide* . This parameter is optional. If it is not included, it defaults to a slash (/). This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! ( ``\\u0021`` ) through the DEL character ( ``\\u007F`` ), including most punctuation characters, digits, and upper and lowercased letters. .. epigraph:: You cannot use an asterisk (*) in the path name. Default: - "/"
        :param roles: The name (friendly name, not ARN) of the role to attach the policy to. This parameter allows (per its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@- .. epigraph:: If an external policy (such as ``AWS::IAM::Policy`` or ``AWS::IAM::ManagedPolicy`` ) has a ``Ref`` to a role and if a resource (such as ``AWS::ECS::Service`` ) also has a ``Ref`` to the same role, add a ``DependsOn`` attribute to the resource to make the resource depend on the external policy. This dependency ensures that the role's policy is available throughout the resource's lifecycle. For example, when you delete a stack with an ``AWS::ECS::Service`` resource, the ``DependsOn`` attribute ensures that AWS CloudFormation deletes the ``AWS::ECS::Service`` resource before deleting its role's policy.
        :param users: The name (friendly name, not ARN) of the IAM user to attach the policy to. This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            
            # policy_document: Any
            
            cfn_managed_policy_props = iam.CfnManagedPolicyProps(
                policy_document=policy_document,
            
                # the properties below are optional
                description="description",
                groups=["groups"],
                managed_policy_name="managedPolicyName",
                path="path",
                roles=["roles"],
                users=["users"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7363835eb798096a2561a7a8a91d2914cb5cb1e71dbda6de66efc5952296bc7f)
            check_type(argname="argument policy_document", value=policy_document, expected_type=type_hints["policy_document"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument groups", value=groups, expected_type=type_hints["groups"])
            check_type(argname="argument managed_policy_name", value=managed_policy_name, expected_type=type_hints["managed_policy_name"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument roles", value=roles, expected_type=type_hints["roles"])
            check_type(argname="argument users", value=users, expected_type=type_hints["users"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_document": policy_document,
        }
        if description is not None:
            self._values["description"] = description
        if groups is not None:
            self._values["groups"] = groups
        if managed_policy_name is not None:
            self._values["managed_policy_name"] = managed_policy_name
        if path is not None:
            self._values["path"] = path
        if roles is not None:
            self._values["roles"] = roles
        if users is not None:
            self._values["users"] = users

    @builtins.property
    def policy_document(self) -> typing.Any:
        '''The JSON policy document that you want to use as the content for the new policy.

        You must provide policies in JSON format in IAM. However, for AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it to IAM.

        The maximum length of the policy document that you can pass in this operation, including whitespace, is listed below. To view the maximum character counts of a managed policy with no whitespaces, see `IAM and AWS STS character quotas <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html#reference_iam-quotas-entity-length>`_ .

        To learn more about JSON policy grammar, see `Grammar of the IAM JSON policy language <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_grammar.html>`_ in the *IAM User Guide* .

        The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ used to validate this parameter is a string of characters consisting of the following:

        - Any printable ASCII character ranging from the space character ( ``\\u0020`` ) through the end of the ASCII character range
        - The printable characters in the Basic Latin and Latin-1 Supplement character set (through ``\\u00FF`` )
        - The special characters tab ( ``\\u0009`` ), line feed ( ``\\u000A`` ), and carriage return ( ``\\u000D`` )

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html#cfn-iam-managedpolicy-policydocument
        '''
        result = self._values.get("policy_document")
        assert result is not None, "Required property 'policy_document' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A friendly description of the policy.

        Typically used to store information about the permissions defined in the policy. For example, "Grants access to production DynamoDB tables."

        The policy description is immutable. After a value is assigned, it cannot be changed.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html#cfn-iam-managedpolicy-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The name (friendly name, not ARN) of the group to attach the policy to.

        This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html#cfn-iam-managedpolicy-groups
        '''
        result = self._values.get("groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def managed_policy_name(self) -> typing.Optional[builtins.str]:
        '''The friendly name of the policy.

        .. epigraph::

           If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.

        If you specify a name, you must specify the ``CAPABILITY_NAMED_IAM`` value to acknowledge your template's capabilities. For more information, see `Acknowledging IAM Resources in AWS CloudFormation Templates <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-capabilities>`_ .
        .. epigraph::

           Naming an IAM resource can cause an unrecoverable error if you reuse the same template in multiple Regions. To prevent this, we recommend using ``Fn::Join`` and ``AWS::Region`` to create a Region-specific name, as in the following example: ``{"Fn::Join": ["", [{"Ref": "AWS::Region"}, {"Ref": "MyResourceName"}]]}`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html#cfn-iam-managedpolicy-managedpolicyname
        '''
        result = self._values.get("managed_policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''The path for the policy.

        For more information about paths, see `IAM identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`_ in the *IAM User Guide* .

        This parameter is optional. If it is not included, it defaults to a slash (/).

        This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! ( ``\\u0021`` ) through the DEL character ( ``\\u007F`` ), including most punctuation characters, digits, and upper and lowercased letters.
        .. epigraph::

           You cannot use an asterisk (*) in the path name.

        :default: - "/"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html#cfn-iam-managedpolicy-path
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The name (friendly name, not ARN) of the role to attach the policy to.

        This parameter allows (per its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        .. epigraph::

           If an external policy (such as ``AWS::IAM::Policy`` or ``AWS::IAM::ManagedPolicy`` ) has a ``Ref`` to a role and if a resource (such as ``AWS::ECS::Service`` ) also has a ``Ref`` to the same role, add a ``DependsOn`` attribute to the resource to make the resource depend on the external policy. This dependency ensures that the role's policy is available throughout the resource's lifecycle. For example, when you delete a stack with an ``AWS::ECS::Service`` resource, the ``DependsOn`` attribute ensures that AWS CloudFormation deletes the ``AWS::ECS::Service`` resource before deleting its role's policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html#cfn-iam-managedpolicy-roles
        '''
        result = self._values.get("roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def users(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The name (friendly name, not ARN) of the IAM user to attach the policy to.

        This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html#cfn-iam-managedpolicy-users
        '''
        result = self._values.get("users")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnManagedPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnOIDCProvider(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.CfnOIDCProvider",
):
    '''Creates or updates an IAM entity to describe an identity provider (IdP) that supports `OpenID Connect (OIDC) <https://docs.aws.amazon.com/http://openid.net/connect/>`_ .

    The OIDC provider that you create with this operation can be used as a principal in a role's trust policy. Such a policy establishes a trust relationship between AWS and the OIDC provider.

    When you create the IAM OIDC provider, you specify the following:

    - The URL of the OIDC identity provider (IdP) to trust
    - A list of client IDs (also known as audiences) that identify the application or applications that are allowed to authenticate using the OIDC provider
    - A list of tags that are attached to the specified IAM OIDC provider
    - A list of thumbprints of one or more server certificates that the IdP uses

    You get all of this information from the OIDC IdP that you want to use to access AWS .

    When you update the IAM OIDC provider, you specify the following:

    - The URL of the OIDC identity provider (IdP) to trust
    - A list of client IDs (also known as audiences) that replaces the existing list of client IDs associated with the OIDC IdP
    - A list of tags that replaces the existing list of tags attached to the specified IAM OIDC provider
    - A list of thumbprints that replaces the existing list of server certificates thumbprints that the IdP uses

    .. epigraph::

       The trust for the OIDC provider is derived from the IAM provider that this operation creates. Therefore, it is best to limit access to the `CreateOpenIDConnectProvider <https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateOpenIDConnectProvider.html>`_ operation to highly privileged users.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-oidcprovider.html
    :cloudformationResource: AWS::IAM::OIDCProvider
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iam as iam
        
        cfn_oIDCProvider = iam.CfnOIDCProvider(self, "MyCfnOIDCProvider",
            thumbprint_list=["thumbprintList"],
        
            # the properties below are optional
            client_id_list=["clientIdList"],
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            url="url"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        thumbprint_list: typing.Sequence[builtins.str],
        client_id_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param thumbprint_list: A list of certificate thumbprints that are associated with the specified IAM OIDC provider resource object. For more information, see `CreateOpenIDConnectProvider <https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateOpenIDConnectProvider.html>`_ .
        :param client_id_list: A list of client IDs (also known as audiences) that are associated with the specified IAM OIDC provider resource object. For more information, see `CreateOpenIDConnectProvider <https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateOpenIDConnectProvider.html>`_ .
        :param tags: A list of tags that are attached to the specified IAM OIDC provider. The returned list of tags is sorted by tag key. For more information about tagging, see `Tagging IAM resources <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`_ in the *IAM User Guide* .
        :param url: The URL that the IAM OIDC provider resource object is associated with. For more information, see `CreateOpenIDConnectProvider <https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateOpenIDConnectProvider.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5cc57bdb168ce990f6466a329942805a3eead54a8207df63d06106140ceabaf1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnOIDCProviderProps(
            thumbprint_list=thumbprint_list,
            client_id_list=client_id_list,
            tags=tags,
            url=url,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e414fee3e3f5f30b79be56e642403e70f811157ff8d43b791b5526b812061d8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4dae706f759e2af37c98017ae788d704bf61cf6db2c64c99cf832bc287eb6389)
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
        '''Returns the Amazon Resource Name (ARN) for the specified ``AWS::IAM::OIDCProvider`` resource.

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
    @jsii.member(jsii_name="thumbprintList")
    def thumbprint_list(self) -> typing.List[builtins.str]:
        '''A list of certificate thumbprints that are associated with the specified IAM OIDC provider resource object.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "thumbprintList"))

    @thumbprint_list.setter
    def thumbprint_list(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa3ed6dd0ef0854d834aaa2a169f05db6443763c0d3f9c4bd58c44fcdac5c427)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thumbprintList", value)

    @builtins.property
    @jsii.member(jsii_name="clientIdList")
    def client_id_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of client IDs (also known as audiences) that are associated with the specified IAM OIDC provider resource object.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "clientIdList"))

    @client_id_list.setter
    def client_id_list(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65ff0b468eb305f1d15390d9c9c9f031b03af51fdd4c6edcd5f1c7b3fabe5e02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientIdList", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags that are attached to the specified IAM OIDC provider.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4db8fa394e822c865ec6e624ef31a1dd1aaba19da7971d0044ad1d1d5a060d70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> typing.Optional[builtins.str]:
        '''The URL that the IAM OIDC provider resource object is associated with.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "url"))

    @url.setter
    def url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__047a9e084da3802dd407fe84ef685690e55704bff14429720999a139e667481e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.CfnOIDCProviderProps",
    jsii_struct_bases=[],
    name_mapping={
        "thumbprint_list": "thumbprintList",
        "client_id_list": "clientIdList",
        "tags": "tags",
        "url": "url",
    },
)
class CfnOIDCProviderProps:
    def __init__(
        self,
        *,
        thumbprint_list: typing.Sequence[builtins.str],
        client_id_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnOIDCProvider``.

        :param thumbprint_list: A list of certificate thumbprints that are associated with the specified IAM OIDC provider resource object. For more information, see `CreateOpenIDConnectProvider <https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateOpenIDConnectProvider.html>`_ .
        :param client_id_list: A list of client IDs (also known as audiences) that are associated with the specified IAM OIDC provider resource object. For more information, see `CreateOpenIDConnectProvider <https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateOpenIDConnectProvider.html>`_ .
        :param tags: A list of tags that are attached to the specified IAM OIDC provider. The returned list of tags is sorted by tag key. For more information about tagging, see `Tagging IAM resources <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`_ in the *IAM User Guide* .
        :param url: The URL that the IAM OIDC provider resource object is associated with. For more information, see `CreateOpenIDConnectProvider <https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateOpenIDConnectProvider.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-oidcprovider.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            
            cfn_oIDCProvider_props = iam.CfnOIDCProviderProps(
                thumbprint_list=["thumbprintList"],
            
                # the properties below are optional
                client_id_list=["clientIdList"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                url="url"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7712735ff8576b291ddb9c7e92ce8078bf6f1d87729109296c1be6414cb3532d)
            check_type(argname="argument thumbprint_list", value=thumbprint_list, expected_type=type_hints["thumbprint_list"])
            check_type(argname="argument client_id_list", value=client_id_list, expected_type=type_hints["client_id_list"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "thumbprint_list": thumbprint_list,
        }
        if client_id_list is not None:
            self._values["client_id_list"] = client_id_list
        if tags is not None:
            self._values["tags"] = tags
        if url is not None:
            self._values["url"] = url

    @builtins.property
    def thumbprint_list(self) -> typing.List[builtins.str]:
        '''A list of certificate thumbprints that are associated with the specified IAM OIDC provider resource object.

        For more information, see `CreateOpenIDConnectProvider <https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateOpenIDConnectProvider.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-oidcprovider.html#cfn-iam-oidcprovider-thumbprintlist
        '''
        result = self._values.get("thumbprint_list")
        assert result is not None, "Required property 'thumbprint_list' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def client_id_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of client IDs (also known as audiences) that are associated with the specified IAM OIDC provider resource object.

        For more information, see `CreateOpenIDConnectProvider <https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateOpenIDConnectProvider.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-oidcprovider.html#cfn-iam-oidcprovider-clientidlist
        '''
        result = self._values.get("client_id_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags that are attached to the specified IAM OIDC provider.

        The returned list of tags is sorted by tag key. For more information about tagging, see `Tagging IAM resources <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`_ in the *IAM User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-oidcprovider.html#cfn-iam-oidcprovider-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def url(self) -> typing.Optional[builtins.str]:
        '''The URL that the IAM OIDC provider resource object is associated with.

        For more information, see `CreateOpenIDConnectProvider <https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateOpenIDConnectProvider.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-oidcprovider.html#cfn-iam-oidcprovider-url
        '''
        result = self._values.get("url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnOIDCProviderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.CfnPolicy",
):
    '''Adds or updates an inline policy document that is embedded in the specified IAM group, user or role.

    An IAM user can also have a managed policy attached to it. For information about policies, see `Managed Policies and Inline Policies <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`_ in the *IAM User Guide* .

    The Groups, Roles, and Users properties are optional. However, you must specify at least one of these properties.

    For information about policy documents see `Creating IAM policies <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html>`_ in the *IAM User Guide* .

    For information about limits on the number of inline policies that you can embed in an identity, see `Limitations on IAM Entities <https://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html>`_ in the *IAM User Guide* .
    .. epigraph::

       This resource does not support `drift detection <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`_ . The following inline policy resource types support drift detection:

       - ```AWS::IAM::GroupPolicy`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-grouppolicy.html>`_
       - ```AWS::IAM::RolePolicy`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-rolepolicy.html>`_
       - ```AWS::IAM::UserPolicy`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-userpolicy.html>`_

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html
    :cloudformationResource: AWS::IAM::Policy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iam as iam
        
        # policy_document: Any
        
        cfn_policy = iam.CfnPolicy(self, "MyCfnPolicy",
            policy_document=policy_document,
            policy_name="policyName",
        
            # the properties below are optional
            groups=["groups"],
            roles=["roles"],
            users=["users"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        policy_document: typing.Any,
        policy_name: builtins.str,
        groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        users: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param policy_document: The policy document. You must provide policies in JSON format in IAM. However, for AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it to IAM. The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ used to validate this parameter is a string of characters consisting of the following: - Any printable ASCII character ranging from the space character ( ``\\u0020`` ) through the end of the ASCII character range - The printable characters in the Basic Latin and Latin-1 Supplement character set (through ``\\u00FF`` ) - The special characters tab ( ``\\u0009`` ), line feed ( ``\\u000A`` ), and carriage return ( ``\\u000D`` )
        :param policy_name: The name of the policy document. This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        :param groups: The name of the group to associate the policy with. This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-.
        :param roles: The name of the role to associate the policy with. This parameter allows (per its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@- .. epigraph:: If an external policy (such as ``AWS::IAM::Policy`` or ``AWS::IAM::ManagedPolicy`` ) has a ``Ref`` to a role and if a resource (such as ``AWS::ECS::Service`` ) also has a ``Ref`` to the same role, add a ``DependsOn`` attribute to the resource to make the resource depend on the external policy. This dependency ensures that the role's policy is available throughout the resource's lifecycle. For example, when you delete a stack with an ``AWS::ECS::Service`` resource, the ``DependsOn`` attribute ensures that AWS CloudFormation deletes the ``AWS::ECS::Service`` resource before deleting its role's policy.
        :param users: The name of the user to associate the policy with. This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb67178fe7e1b31e1be07438cbe12957995260af0ad90c58a3ab490fe6dfe65e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPolicyProps(
            policy_document=policy_document,
            policy_name=policy_name,
            groups=groups,
            roles=roles,
            users=users,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b0b1b065d832052b886db644c3488c7bc10240091ef05927590351b7bc53eb1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__85f1de37bbcdfc836c215c1a1844169c37747c39945f4381b39bfd452963ff73)
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
    @jsii.member(jsii_name="policyDocument")
    def policy_document(self) -> typing.Any:
        '''The policy document.'''
        return typing.cast(typing.Any, jsii.get(self, "policyDocument"))

    @policy_document.setter
    def policy_document(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06044458de4bf8f3f6bd0026d2e0c44680c55d70af59396fc7616d84dab9d26d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyDocument", value)

    @builtins.property
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        '''The name of the policy document.'''
        return typing.cast(builtins.str, jsii.get(self, "policyName"))

    @policy_name.setter
    def policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecc19153b06dcc252bfb1ae6146652d56fcd1825369497489a00194a960696d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyName", value)

    @builtins.property
    @jsii.member(jsii_name="groups")
    def groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The name of the group to associate the policy with.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groups"))

    @groups.setter
    def groups(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cb77529b0bb4edf27e46d46d8fcaedafea19611a49ee1c83bfdd3a98234745e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groups", value)

    @builtins.property
    @jsii.member(jsii_name="roles")
    def roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The name of the role to associate the policy with.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "roles"))

    @roles.setter
    def roles(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87a89a5b9d5419ceb30e8217d4489eae0857ac493147f2a7af32a527ec688a14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roles", value)

    @builtins.property
    @jsii.member(jsii_name="users")
    def users(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The name of the user to associate the policy with.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "users"))

    @users.setter
    def users(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c25ce8e0b5d932098589ac1c033a96eed27019fa02e7aea82f7eaacbdd509100)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "users", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.CfnPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "policy_document": "policyDocument",
        "policy_name": "policyName",
        "groups": "groups",
        "roles": "roles",
        "users": "users",
    },
)
class CfnPolicyProps:
    def __init__(
        self,
        *,
        policy_document: typing.Any,
        policy_name: builtins.str,
        groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        users: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPolicy``.

        :param policy_document: The policy document. You must provide policies in JSON format in IAM. However, for AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it to IAM. The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ used to validate this parameter is a string of characters consisting of the following: - Any printable ASCII character ranging from the space character ( ``\\u0020`` ) through the end of the ASCII character range - The printable characters in the Basic Latin and Latin-1 Supplement character set (through ``\\u00FF`` ) - The special characters tab ( ``\\u0009`` ), line feed ( ``\\u000A`` ), and carriage return ( ``\\u000D`` )
        :param policy_name: The name of the policy document. This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        :param groups: The name of the group to associate the policy with. This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-.
        :param roles: The name of the role to associate the policy with. This parameter allows (per its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@- .. epigraph:: If an external policy (such as ``AWS::IAM::Policy`` or ``AWS::IAM::ManagedPolicy`` ) has a ``Ref`` to a role and if a resource (such as ``AWS::ECS::Service`` ) also has a ``Ref`` to the same role, add a ``DependsOn`` attribute to the resource to make the resource depend on the external policy. This dependency ensures that the role's policy is available throughout the resource's lifecycle. For example, when you delete a stack with an ``AWS::ECS::Service`` resource, the ``DependsOn`` attribute ensures that AWS CloudFormation deletes the ``AWS::ECS::Service`` resource before deleting its role's policy.
        :param users: The name of the user to associate the policy with. This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            
            # policy_document: Any
            
            cfn_policy_props = iam.CfnPolicyProps(
                policy_document=policy_document,
                policy_name="policyName",
            
                # the properties below are optional
                groups=["groups"],
                roles=["roles"],
                users=["users"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__368d6e95de387252f469d8428e0a4cbe73ffdab170f90c7194b6f3e54f8b875c)
            check_type(argname="argument policy_document", value=policy_document, expected_type=type_hints["policy_document"])
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
            check_type(argname="argument groups", value=groups, expected_type=type_hints["groups"])
            check_type(argname="argument roles", value=roles, expected_type=type_hints["roles"])
            check_type(argname="argument users", value=users, expected_type=type_hints["users"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_document": policy_document,
            "policy_name": policy_name,
        }
        if groups is not None:
            self._values["groups"] = groups
        if roles is not None:
            self._values["roles"] = roles
        if users is not None:
            self._values["users"] = users

    @builtins.property
    def policy_document(self) -> typing.Any:
        '''The policy document.

        You must provide policies in JSON format in IAM. However, for AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it to IAM.

        The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ used to validate this parameter is a string of characters consisting of the following:

        - Any printable ASCII character ranging from the space character ( ``\\u0020`` ) through the end of the ASCII character range
        - The printable characters in the Basic Latin and Latin-1 Supplement character set (through ``\\u00FF`` )
        - The special characters tab ( ``\\u0009`` ), line feed ( ``\\u000A`` ), and carriage return ( ``\\u000D`` )

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html#cfn-iam-policy-policydocument
        '''
        result = self._values.get("policy_document")
        assert result is not None, "Required property 'policy_document' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def policy_name(self) -> builtins.str:
        '''The name of the policy document.

        This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html#cfn-iam-policy-policyname
        '''
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The name of the group to associate the policy with.

        This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html#cfn-iam-policy-groups
        '''
        result = self._values.get("groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The name of the role to associate the policy with.

        This parameter allows (per its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        .. epigraph::

           If an external policy (such as ``AWS::IAM::Policy`` or ``AWS::IAM::ManagedPolicy`` ) has a ``Ref`` to a role and if a resource (such as ``AWS::ECS::Service`` ) also has a ``Ref`` to the same role, add a ``DependsOn`` attribute to the resource to make the resource depend on the external policy. This dependency ensures that the role's policy is available throughout the resource's lifecycle. For example, when you delete a stack with an ``AWS::ECS::Service`` resource, the ``DependsOn`` attribute ensures that AWS CloudFormation deletes the ``AWS::ECS::Service`` resource before deleting its role's policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html#cfn-iam-policy-roles
        '''
        result = self._values.get("roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def users(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The name of the user to associate the policy with.

        This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html#cfn-iam-policy-users
        '''
        result = self._values.get("users")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnRole(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.CfnRole",
):
    '''Creates a new role for your AWS account .

    For more information about roles, see `IAM roles <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html>`_ in the *IAM User Guide* . For information about quotas for role names and the number of roles you can create, see `IAM and AWS STS quotas <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html>`_ in the *IAM User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html
    :cloudformationResource: AWS::IAM::Role
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iam as iam
        
        # assume_role_policy_document: Any
        # policy_document: Any
        
        cfn_role = iam.CfnRole(self, "MyCfnRole",
            assume_role_policy_document=assume_role_policy_document,
        
            # the properties below are optional
            description="description",
            managed_policy_arns=["managedPolicyArns"],
            max_session_duration=123,
            path="path",
            permissions_boundary="permissionsBoundary",
            policies=[iam.CfnRole.PolicyProperty(
                policy_document=policy_document,
                policy_name="policyName"
            )],
            role_name="roleName",
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
        assume_role_policy_document: typing.Any,
        description: typing.Optional[builtins.str] = None,
        managed_policy_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        max_session_duration: typing.Optional[jsii.Number] = None,
        path: typing.Optional[builtins.str] = None,
        permissions_boundary: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRole.PolicyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        role_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param assume_role_policy_document: The trust policy that is associated with this role. Trust policies define which entities can assume the role. You can associate only one trust policy with a role. For an example of a policy that can be used to assume a role, see `Template Examples <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#aws-resource-iam-role--examples>`_ . For more information about the elements that you can use in an IAM policy, see `IAM Policy Elements Reference <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html>`_ in the *IAM User Guide* .
        :param description: A description of the role that you provide.
        :param managed_policy_arns: A list of Amazon Resource Names (ARNs) of the IAM managed policies that you want to attach to the role. For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .
        :param max_session_duration: The maximum session duration (in seconds) that you want to set for the specified role. If you do not specify a value for this setting, the default value of one hour is applied. This setting can have a value from 1 hour to 12 hours. Anyone who assumes the role from the AWS CLI or API can use the ``DurationSeconds`` API parameter or the ``duration-seconds`` AWS CLI parameter to request a longer session. The ``MaxSessionDuration`` setting determines the maximum duration that can be requested using the ``DurationSeconds`` parameter. If users don't specify a value for the ``DurationSeconds`` parameter, their security credentials are valid for one hour by default. This applies when you use the ``AssumeRole*`` API operations or the ``assume-role*`` AWS CLI operations but does not apply when you use those operations to create a console URL. For more information, see `Using IAM roles <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html>`_ in the *IAM User Guide* .
        :param path: The path to the role. For more information about paths, see `IAM Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`_ in the *IAM User Guide* . This parameter is optional. If it is not included, it defaults to a slash (/). This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! ( ``\\u0021`` ) through the DEL character ( ``\\u007F`` ), including most punctuation characters, digits, and upper and lowercased letters. Default: - "/"
        :param permissions_boundary: The ARN of the policy used to set the permissions boundary for the role. For more information about permissions boundaries, see `Permissions boundaries for IAM identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`_ in the *IAM User Guide* .
        :param policies: Adds or updates an inline policy document that is embedded in the specified IAM role. When you embed an inline policy in a role, the inline policy is used as part of the role's access (permissions) policy. The role's trust policy is created at the same time as the role. You can update a role's trust policy later. For more information about IAM roles, go to `Using Roles to Delegate Permissions and Federate Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-toplevel.html>`_ . A role can also have an attached managed policy. For information about policies, see `Managed Policies and Inline Policies <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`_ in the *IAM User Guide* . For information about limits on the number of inline policies that you can embed with a role, see `Limitations on IAM Entities <https://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html>`_ in the *IAM User Guide* . .. epigraph:: If an external policy (such as ``AWS::IAM::Policy`` or ``AWS::IAM::ManagedPolicy`` ) has a ``Ref`` to a role and if a resource (such as ``AWS::ECS::Service`` ) also has a ``Ref`` to the same role, add a ``DependsOn`` attribute to the resource to make the resource depend on the external policy. This dependency ensures that the role's policy is available throughout the resource's lifecycle. For example, when you delete a stack with an ``AWS::ECS::Service`` resource, the ``DependsOn`` attribute ensures that AWS CloudFormation deletes the ``AWS::ECS::Service`` resource before deleting its role's policy.
        :param role_name: A name for the IAM role, up to 64 characters in length. For valid values, see the ``RoleName`` parameter for the ```CreateRole`` <https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html>`_ action in the *IAM User Guide* . This parameter allows (per its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-. The role name must be unique within the account. Role names are not distinguished by case. For example, you cannot create roles named both "Role1" and "role1". If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the role name. If you specify a name, you must specify the ``CAPABILITY_NAMED_IAM`` value to acknowledge your template's capabilities. For more information, see `Acknowledging IAM Resources in AWS CloudFormation Templates <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-capabilities>`_ . .. epigraph:: Naming an IAM resource can cause an unrecoverable error if you reuse the same template in multiple Regions. To prevent this, we recommend using ``Fn::Join`` and ``AWS::Region`` to create a Region-specific name, as in the following example: ``{"Fn::Join": ["", [{"Ref": "AWS::Region"}, {"Ref": "MyResourceName"}]]}`` .
        :param tags: A list of tags that are attached to the role. For more information about tagging, see `Tagging IAM resources <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`_ in the *IAM User Guide* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b418623e6c6b819228e2a7c5d9c5341241e5b0e738f77eeabd6cacec7c6fab32)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRoleProps(
            assume_role_policy_document=assume_role_policy_document,
            description=description,
            managed_policy_arns=managed_policy_arns,
            max_session_duration=max_session_duration,
            path=path,
            permissions_boundary=permissions_boundary,
            policies=policies,
            role_name=role_name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ab1ed2eb652f78c921a94468eea54161c2d72210612c21a2d7221190717d546)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6c17ebfb69a2f5ed9dd9290d6026b842dd5e032f3f0f7aa29ccc996da3be8aa3)
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
        '''Returns the Amazon Resource Name (ARN) for the role. For example:.

        ``{"Fn::GetAtt" : ["MyRole", "Arn"] }``

        This will return a value such as ``arn:aws:iam::1234567890:role/MyRole-AJJHDSKSDF`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrRoleId")
    def attr_role_id(self) -> builtins.str:
        '''Returns the stable and unique string identifying the role. For example, ``AIDAJQABLZS4A3QDU576Q`` .

        For more information about IDs, see `IAM Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html>`_ in the *IAM User Guide* .

        :cloudformationAttribute: RoleId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRoleId"))

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
    @jsii.member(jsii_name="assumeRolePolicyDocument")
    def assume_role_policy_document(self) -> typing.Any:
        '''The trust policy that is associated with this role.'''
        return typing.cast(typing.Any, jsii.get(self, "assumeRolePolicyDocument"))

    @assume_role_policy_document.setter
    def assume_role_policy_document(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f64edf2fd513d8eaa71e570374ea6368333dca94e9bcd75c06e0cd57bf703237)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assumeRolePolicyDocument", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the role that you provide.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c2a9dbc73d67aad806d2048aa4381abc22ed38266fbe7ad4d0f9363cfdac4a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="managedPolicyArns")
    def managed_policy_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of Amazon Resource Names (ARNs) of the IAM managed policies that you want to attach to the role.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "managedPolicyArns"))

    @managed_policy_arns.setter
    def managed_policy_arns(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84c396c36f658a4080b46dfbbcb0f9163ca138b4afaf4da438a00378beffede7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedPolicyArns", value)

    @builtins.property
    @jsii.member(jsii_name="maxSessionDuration")
    def max_session_duration(self) -> typing.Optional[jsii.Number]:
        '''The maximum session duration (in seconds) that you want to set for the specified role.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxSessionDuration"))

    @max_session_duration.setter
    def max_session_duration(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6431acc0b99ad558bc7b549bbfe3e581f937dce92da78253920c201c8cc22e0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxSessionDuration", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> typing.Optional[builtins.str]:
        '''The path to the role.

        For more information about paths, see `IAM Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`_ in the *IAM User Guide* .
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "path"))

    @path.setter
    def path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d420d46f77d7cfcfcd09009a0f2eadf9ebada83d085948137f30c8ee4abdd4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="permissionsBoundary")
    def permissions_boundary(self) -> typing.Optional[builtins.str]:
        '''The ARN of the policy used to set the permissions boundary for the role.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "permissionsBoundary"))

    @permissions_boundary.setter
    def permissions_boundary(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6141e4bbefd436f5eddad46690a81845abcebab51fabb169abf1431f02795db1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionsBoundary", value)

    @builtins.property
    @jsii.member(jsii_name="policies")
    def policies(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRole.PolicyProperty"]]]]:
        '''Adds or updates an inline policy document that is embedded in the specified IAM role.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRole.PolicyProperty"]]]], jsii.get(self, "policies"))

    @policies.setter
    def policies(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRole.PolicyProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de13ceb9aac4a8cea0907c7e4ba81eeca369f4f35bfc0f1d48beddf9ab76811f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policies", value)

    @builtins.property
    @jsii.member(jsii_name="roleName")
    def role_name(self) -> typing.Optional[builtins.str]:
        '''A name for the IAM role, up to 64 characters in length.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleName"))

    @role_name.setter
    def role_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__435e72316ea55d9adabad0902ac623255b110529fcd748e3ac74055cff795bef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleName", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags that are attached to the role.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c0657eba6af54757d6f74532e2ed61efbdc50fb773a54687878cfd7c7f8dda5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iam.CfnRole.PolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "policy_document": "policyDocument",
            "policy_name": "policyName",
        },
    )
    class PolicyProperty:
        def __init__(
            self,
            *,
            policy_document: typing.Any,
            policy_name: builtins.str,
        ) -> None:
            '''Contains information about an attached policy.

            An attached policy is a managed policy that has been attached to a user, group, or role.

            For more information about managed policies, refer to `Managed Policies and Inline Policies <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`_ in the *IAM User Guide* .

            :param policy_document: The entire contents of the policy that defines permissions. For more information, see `Overview of JSON policies <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-json>`_ .
            :param policy_name: The friendly name (not ARN) identifying the policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-role-policy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iam as iam
                
                # policy_document: Any
                
                policy_property = iam.CfnRole.PolicyProperty(
                    policy_document=policy_document,
                    policy_name="policyName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e339dba71f34d8ac881f4a2583a5b3e824a8bb93f479517aebabc1977c8c2ba1)
                check_type(argname="argument policy_document", value=policy_document, expected_type=type_hints["policy_document"])
                check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "policy_document": policy_document,
                "policy_name": policy_name,
            }

        @builtins.property
        def policy_document(self) -> typing.Any:
            '''The entire contents of the policy that defines permissions.

            For more information, see `Overview of JSON policies <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-json>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-role-policy.html#cfn-iam-role-policy-policydocument
            '''
            result = self._values.get("policy_document")
            assert result is not None, "Required property 'policy_document' is missing"
            return typing.cast(typing.Any, result)

        @builtins.property
        def policy_name(self) -> builtins.str:
            '''The friendly name (not ARN) identifying the policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-role-policy.html#cfn-iam-role-policy-policyname
            '''
            result = self._values.get("policy_name")
            assert result is not None, "Required property 'policy_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnRolePolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.CfnRolePolicy",
):
    '''Adds or updates an inline policy document that is embedded in the specified IAM role.

    When you embed an inline policy in a role, the inline policy is used as part of the role's access (permissions) policy. The role's trust policy is created at the same time as the role, using ```CreateRole`` <https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html>`_ . You can update a role's trust policy using ```UpdateAssumeRolePolicy`` <https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateAssumeRolePolicy.html>`_ . For information about roles, see `IAM roles <https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-toplevel.html>`_ in the *IAM User Guide* .

    A role can also have a managed policy attached to it. To attach a managed policy to a role, use ```AWS::IAM::Role`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html>`_ . To create a new managed policy, use ```AWS::IAM::ManagedPolicy`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html>`_ . For information about policies, see `Managed policies and inline policies <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`_ in the *IAM User Guide* .

    For information about the maximum number of inline policies that you can embed with a role, see `IAM and AWS STS quotas <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html>`_ in the *IAM User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-rolepolicy.html
    :cloudformationResource: AWS::IAM::RolePolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iam as iam
        
        # policy_document: Any
        
        cfn_role_policy = iam.CfnRolePolicy(self, "MyCfnRolePolicy",
            policy_name="policyName",
            role_name="roleName",
        
            # the properties below are optional
            policy_document=policy_document
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        policy_name: builtins.str,
        role_name: builtins.str,
        policy_document: typing.Any = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param policy_name: The name of the policy document. This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        :param role_name: The name of the role to associate the policy with. This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        :param policy_document: The policy document. You must provide policies in JSON format in IAM. However, for AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it to IAM. The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ used to validate this parameter is a string of characters consisting of the following: - Any printable ASCII character ranging from the space character ( ``\\u0020`` ) through the end of the ASCII character range - The printable characters in the Basic Latin and Latin-1 Supplement character set (through ``\\u00FF`` ) - The special characters tab ( ``\\u0009`` ), line feed ( ``\\u000A`` ), and carriage return ( ``\\u000D`` )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1532590762c98b830f41db58b5d7333f7f995a90f128be89292c180ecefabf3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRolePolicyProps(
            policy_name=policy_name,
            role_name=role_name,
            policy_document=policy_document,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f878b18113dc1f16c459595683f03c065b56afd62d2918c65c6cde7539984412)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0db54a249a715ade4f26735343ca5a55eb1952e807ce57e2d7ec4b843c350641)
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
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        '''The name of the policy document.'''
        return typing.cast(builtins.str, jsii.get(self, "policyName"))

    @policy_name.setter
    def policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7042bd66e9ba283ac19987752cc24a822d1f227ca8217dbbae1ca253f583b373)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyName", value)

    @builtins.property
    @jsii.member(jsii_name="roleName")
    def role_name(self) -> builtins.str:
        '''The name of the role to associate the policy with.'''
        return typing.cast(builtins.str, jsii.get(self, "roleName"))

    @role_name.setter
    def role_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c89cdd638f3704d6ca88c2e6c9c5c301322b1ed12de337f2ec3c4bfdee661f0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleName", value)

    @builtins.property
    @jsii.member(jsii_name="policyDocument")
    def policy_document(self) -> typing.Any:
        '''The policy document.'''
        return typing.cast(typing.Any, jsii.get(self, "policyDocument"))

    @policy_document.setter
    def policy_document(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2153da01bebec26c385aa83a08c1b544e6c1e15dfda33c546698c885cbf1e9b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyDocument", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.CfnRolePolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "policy_name": "policyName",
        "role_name": "roleName",
        "policy_document": "policyDocument",
    },
)
class CfnRolePolicyProps:
    def __init__(
        self,
        *,
        policy_name: builtins.str,
        role_name: builtins.str,
        policy_document: typing.Any = None,
    ) -> None:
        '''Properties for defining a ``CfnRolePolicy``.

        :param policy_name: The name of the policy document. This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        :param role_name: The name of the role to associate the policy with. This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        :param policy_document: The policy document. You must provide policies in JSON format in IAM. However, for AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it to IAM. The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ used to validate this parameter is a string of characters consisting of the following: - Any printable ASCII character ranging from the space character ( ``\\u0020`` ) through the end of the ASCII character range - The printable characters in the Basic Latin and Latin-1 Supplement character set (through ``\\u00FF`` ) - The special characters tab ( ``\\u0009`` ), line feed ( ``\\u000A`` ), and carriage return ( ``\\u000D`` )

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-rolepolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            
            # policy_document: Any
            
            cfn_role_policy_props = iam.CfnRolePolicyProps(
                policy_name="policyName",
                role_name="roleName",
            
                # the properties below are optional
                policy_document=policy_document
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0668a03621626b1e6c6578349ef013dbc6d934f3d76b7973db1350fe9541efc)
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
            check_type(argname="argument role_name", value=role_name, expected_type=type_hints["role_name"])
            check_type(argname="argument policy_document", value=policy_document, expected_type=type_hints["policy_document"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_name": policy_name,
            "role_name": role_name,
        }
        if policy_document is not None:
            self._values["policy_document"] = policy_document

    @builtins.property
    def policy_name(self) -> builtins.str:
        '''The name of the policy document.

        This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-rolepolicy.html#cfn-iam-rolepolicy-policyname
        '''
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_name(self) -> builtins.str:
        '''The name of the role to associate the policy with.

        This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-rolepolicy.html#cfn-iam-rolepolicy-rolename
        '''
        result = self._values.get("role_name")
        assert result is not None, "Required property 'role_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_document(self) -> typing.Any:
        '''The policy document.

        You must provide policies in JSON format in IAM. However, for AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it to IAM.

        The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ used to validate this parameter is a string of characters consisting of the following:

        - Any printable ASCII character ranging from the space character ( ``\\u0020`` ) through the end of the ASCII character range
        - The printable characters in the Basic Latin and Latin-1 Supplement character set (through ``\\u00FF`` )
        - The special characters tab ( ``\\u0009`` ), line feed ( ``\\u000A`` ), and carriage return ( ``\\u000D`` )

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-rolepolicy.html#cfn-iam-rolepolicy-policydocument
        '''
        result = self._values.get("policy_document")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRolePolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.CfnRoleProps",
    jsii_struct_bases=[],
    name_mapping={
        "assume_role_policy_document": "assumeRolePolicyDocument",
        "description": "description",
        "managed_policy_arns": "managedPolicyArns",
        "max_session_duration": "maxSessionDuration",
        "path": "path",
        "permissions_boundary": "permissionsBoundary",
        "policies": "policies",
        "role_name": "roleName",
        "tags": "tags",
    },
)
class CfnRoleProps:
    def __init__(
        self,
        *,
        assume_role_policy_document: typing.Any,
        description: typing.Optional[builtins.str] = None,
        managed_policy_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        max_session_duration: typing.Optional[jsii.Number] = None,
        path: typing.Optional[builtins.str] = None,
        permissions_boundary: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRole.PolicyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        role_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRole``.

        :param assume_role_policy_document: The trust policy that is associated with this role. Trust policies define which entities can assume the role. You can associate only one trust policy with a role. For an example of a policy that can be used to assume a role, see `Template Examples <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#aws-resource-iam-role--examples>`_ . For more information about the elements that you can use in an IAM policy, see `IAM Policy Elements Reference <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html>`_ in the *IAM User Guide* .
        :param description: A description of the role that you provide.
        :param managed_policy_arns: A list of Amazon Resource Names (ARNs) of the IAM managed policies that you want to attach to the role. For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .
        :param max_session_duration: The maximum session duration (in seconds) that you want to set for the specified role. If you do not specify a value for this setting, the default value of one hour is applied. This setting can have a value from 1 hour to 12 hours. Anyone who assumes the role from the AWS CLI or API can use the ``DurationSeconds`` API parameter or the ``duration-seconds`` AWS CLI parameter to request a longer session. The ``MaxSessionDuration`` setting determines the maximum duration that can be requested using the ``DurationSeconds`` parameter. If users don't specify a value for the ``DurationSeconds`` parameter, their security credentials are valid for one hour by default. This applies when you use the ``AssumeRole*`` API operations or the ``assume-role*`` AWS CLI operations but does not apply when you use those operations to create a console URL. For more information, see `Using IAM roles <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html>`_ in the *IAM User Guide* .
        :param path: The path to the role. For more information about paths, see `IAM Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`_ in the *IAM User Guide* . This parameter is optional. If it is not included, it defaults to a slash (/). This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! ( ``\\u0021`` ) through the DEL character ( ``\\u007F`` ), including most punctuation characters, digits, and upper and lowercased letters. Default: - "/"
        :param permissions_boundary: The ARN of the policy used to set the permissions boundary for the role. For more information about permissions boundaries, see `Permissions boundaries for IAM identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`_ in the *IAM User Guide* .
        :param policies: Adds or updates an inline policy document that is embedded in the specified IAM role. When you embed an inline policy in a role, the inline policy is used as part of the role's access (permissions) policy. The role's trust policy is created at the same time as the role. You can update a role's trust policy later. For more information about IAM roles, go to `Using Roles to Delegate Permissions and Federate Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-toplevel.html>`_ . A role can also have an attached managed policy. For information about policies, see `Managed Policies and Inline Policies <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`_ in the *IAM User Guide* . For information about limits on the number of inline policies that you can embed with a role, see `Limitations on IAM Entities <https://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html>`_ in the *IAM User Guide* . .. epigraph:: If an external policy (such as ``AWS::IAM::Policy`` or ``AWS::IAM::ManagedPolicy`` ) has a ``Ref`` to a role and if a resource (such as ``AWS::ECS::Service`` ) also has a ``Ref`` to the same role, add a ``DependsOn`` attribute to the resource to make the resource depend on the external policy. This dependency ensures that the role's policy is available throughout the resource's lifecycle. For example, when you delete a stack with an ``AWS::ECS::Service`` resource, the ``DependsOn`` attribute ensures that AWS CloudFormation deletes the ``AWS::ECS::Service`` resource before deleting its role's policy.
        :param role_name: A name for the IAM role, up to 64 characters in length. For valid values, see the ``RoleName`` parameter for the ```CreateRole`` <https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html>`_ action in the *IAM User Guide* . This parameter allows (per its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-. The role name must be unique within the account. Role names are not distinguished by case. For example, you cannot create roles named both "Role1" and "role1". If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the role name. If you specify a name, you must specify the ``CAPABILITY_NAMED_IAM`` value to acknowledge your template's capabilities. For more information, see `Acknowledging IAM Resources in AWS CloudFormation Templates <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-capabilities>`_ . .. epigraph:: Naming an IAM resource can cause an unrecoverable error if you reuse the same template in multiple Regions. To prevent this, we recommend using ``Fn::Join`` and ``AWS::Region`` to create a Region-specific name, as in the following example: ``{"Fn::Join": ["", [{"Ref": "AWS::Region"}, {"Ref": "MyResourceName"}]]}`` .
        :param tags: A list of tags that are attached to the role. For more information about tagging, see `Tagging IAM resources <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`_ in the *IAM User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            
            # assume_role_policy_document: Any
            # policy_document: Any
            
            cfn_role_props = iam.CfnRoleProps(
                assume_role_policy_document=assume_role_policy_document,
            
                # the properties below are optional
                description="description",
                managed_policy_arns=["managedPolicyArns"],
                max_session_duration=123,
                path="path",
                permissions_boundary="permissionsBoundary",
                policies=[iam.CfnRole.PolicyProperty(
                    policy_document=policy_document,
                    policy_name="policyName"
                )],
                role_name="roleName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5103775c44bc4d8c2381a2d9cd5bbb47d14617e4000af5af24e41da605c8820f)
            check_type(argname="argument assume_role_policy_document", value=assume_role_policy_document, expected_type=type_hints["assume_role_policy_document"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument managed_policy_arns", value=managed_policy_arns, expected_type=type_hints["managed_policy_arns"])
            check_type(argname="argument max_session_duration", value=max_session_duration, expected_type=type_hints["max_session_duration"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument permissions_boundary", value=permissions_boundary, expected_type=type_hints["permissions_boundary"])
            check_type(argname="argument policies", value=policies, expected_type=type_hints["policies"])
            check_type(argname="argument role_name", value=role_name, expected_type=type_hints["role_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "assume_role_policy_document": assume_role_policy_document,
        }
        if description is not None:
            self._values["description"] = description
        if managed_policy_arns is not None:
            self._values["managed_policy_arns"] = managed_policy_arns
        if max_session_duration is not None:
            self._values["max_session_duration"] = max_session_duration
        if path is not None:
            self._values["path"] = path
        if permissions_boundary is not None:
            self._values["permissions_boundary"] = permissions_boundary
        if policies is not None:
            self._values["policies"] = policies
        if role_name is not None:
            self._values["role_name"] = role_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def assume_role_policy_document(self) -> typing.Any:
        '''The trust policy that is associated with this role.

        Trust policies define which entities can assume the role. You can associate only one trust policy with a role. For an example of a policy that can be used to assume a role, see `Template Examples <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#aws-resource-iam-role--examples>`_ . For more information about the elements that you can use in an IAM policy, see `IAM Policy Elements Reference <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html>`_ in the *IAM User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-assumerolepolicydocument
        '''
        result = self._values.get("assume_role_policy_document")
        assert result is not None, "Required property 'assume_role_policy_document' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the role that you provide.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def managed_policy_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of Amazon Resource Names (ARNs) of the IAM managed policies that you want to attach to the role.

        For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-managedpolicyarns
        '''
        result = self._values.get("managed_policy_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def max_session_duration(self) -> typing.Optional[jsii.Number]:
        '''The maximum session duration (in seconds) that you want to set for the specified role.

        If you do not specify a value for this setting, the default value of one hour is applied. This setting can have a value from 1 hour to 12 hours.

        Anyone who assumes the role from the AWS CLI or API can use the ``DurationSeconds`` API parameter or the ``duration-seconds`` AWS CLI parameter to request a longer session. The ``MaxSessionDuration`` setting determines the maximum duration that can be requested using the ``DurationSeconds`` parameter. If users don't specify a value for the ``DurationSeconds`` parameter, their security credentials are valid for one hour by default. This applies when you use the ``AssumeRole*`` API operations or the ``assume-role*`` AWS CLI operations but does not apply when you use those operations to create a console URL. For more information, see `Using IAM roles <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html>`_ in the *IAM User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-maxsessionduration
        '''
        result = self._values.get("max_session_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''The path to the role. For more information about paths, see `IAM Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`_ in the *IAM User Guide* .

        This parameter is optional. If it is not included, it defaults to a slash (/).

        This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! ( ``\\u0021`` ) through the DEL character ( ``\\u007F`` ), including most punctuation characters, digits, and upper and lowercased letters.

        :default: - "/"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-path
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permissions_boundary(self) -> typing.Optional[builtins.str]:
        '''The ARN of the policy used to set the permissions boundary for the role.

        For more information about permissions boundaries, see `Permissions boundaries for IAM identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`_ in the *IAM User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-permissionsboundary
        '''
        result = self._values.get("permissions_boundary")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policies(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnRole.PolicyProperty]]]]:
        '''Adds or updates an inline policy document that is embedded in the specified IAM role.

        When you embed an inline policy in a role, the inline policy is used as part of the role's access (permissions) policy. The role's trust policy is created at the same time as the role. You can update a role's trust policy later. For more information about IAM roles, go to `Using Roles to Delegate Permissions and Federate Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-toplevel.html>`_ .

        A role can also have an attached managed policy. For information about policies, see `Managed Policies and Inline Policies <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`_ in the *IAM User Guide* .

        For information about limits on the number of inline policies that you can embed with a role, see `Limitations on IAM Entities <https://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html>`_ in the *IAM User Guide* .
        .. epigraph::

           If an external policy (such as ``AWS::IAM::Policy`` or ``AWS::IAM::ManagedPolicy`` ) has a ``Ref`` to a role and if a resource (such as ``AWS::ECS::Service`` ) also has a ``Ref`` to the same role, add a ``DependsOn`` attribute to the resource to make the resource depend on the external policy. This dependency ensures that the role's policy is available throughout the resource's lifecycle. For example, when you delete a stack with an ``AWS::ECS::Service`` resource, the ``DependsOn`` attribute ensures that AWS CloudFormation deletes the ``AWS::ECS::Service`` resource before deleting its role's policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-policies
        '''
        result = self._values.get("policies")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnRole.PolicyProperty]]]], result)

    @builtins.property
    def role_name(self) -> typing.Optional[builtins.str]:
        '''A name for the IAM role, up to 64 characters in length.

        For valid values, see the ``RoleName`` parameter for the ```CreateRole`` <https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html>`_ action in the *IAM User Guide* .

        This parameter allows (per its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-. The role name must be unique within the account. Role names are not distinguished by case. For example, you cannot create roles named both "Role1" and "role1".

        If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the role name.

        If you specify a name, you must specify the ``CAPABILITY_NAMED_IAM`` value to acknowledge your template's capabilities. For more information, see `Acknowledging IAM Resources in AWS CloudFormation Templates <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-capabilities>`_ .
        .. epigraph::

           Naming an IAM resource can cause an unrecoverable error if you reuse the same template in multiple Regions. To prevent this, we recommend using ``Fn::Join`` and ``AWS::Region`` to create a Region-specific name, as in the following example: ``{"Fn::Join": ["", [{"Ref": "AWS::Region"}, {"Ref": "MyResourceName"}]]}`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-rolename
        '''
        result = self._values.get("role_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags that are attached to the role.

        For more information about tagging, see `Tagging IAM resources <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`_ in the *IAM User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRoleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnSAMLProvider(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.CfnSAMLProvider",
):
    '''Creates an IAM resource that describes an identity provider (IdP) that supports SAML 2.0.

    The SAML provider resource that you create with this operation can be used as a principal in an IAM role's trust policy. Such a policy can enable federated users who sign in using the SAML IdP to assume the role. You can create an IAM role that supports Web-based single sign-on (SSO) to the AWS Management Console or one that supports API access to AWS .

    When you create the SAML provider resource, you upload a SAML metadata document that you get from your IdP. That document includes the issuer's name, expiration information, and keys that can be used to validate the SAML authentication response (assertions) that the IdP sends. You must generate the metadata document using the identity management software that is used as your organization's IdP.
    .. epigraph::

       This operation requires `Signature Version 4 <https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html>`_ .

    For more information, see `Enabling SAML 2.0 federated users to access the AWS Management Console <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-saml.html>`_ and `About SAML 2.0-based federation <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html>`_ in the *IAM User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-samlprovider.html
    :cloudformationResource: AWS::IAM::SAMLProvider
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iam as iam
        
        cfn_sAMLProvider = iam.CfnSAMLProvider(self, "MyCfnSAMLProvider",
            saml_metadata_document="samlMetadataDocument",
        
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
        saml_metadata_document: builtins.str,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param saml_metadata_document: An XML document generated by an identity provider (IdP) that supports SAML 2.0. The document includes the issuer's name, expiration information, and keys that can be used to validate the SAML authentication response (assertions) that are received from the IdP. You must generate the metadata document using the identity management software that is used as your organization's IdP. For more information, see `About SAML 2.0-based federation <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html>`_ in the *IAM User Guide*
        :param name: The name of the provider to create. This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        :param tags: A list of tags that you want to attach to the new IAM SAML provider. Each tag consists of a key name and an associated value. For more information about tagging, see `Tagging IAM resources <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`_ in the *IAM User Guide* . .. epigraph:: If any one of the tags is invalid or if you exceed the allowed maximum number of tags, then the entire request fails and the resource is not created.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f64934981377388842130b01da042285d0dfa38ef82a7537c7ff86f5d1f3f009)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSAMLProviderProps(
            saml_metadata_document=saml_metadata_document, name=name, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__125ecb4c71203c76b16de524888c31f4d67c2ec1eb117d698f7d362c7d8fe450)
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
            type_hints = typing.get_type_hints(_typecheckingstub__aa493901e136133decf51345379fd4b5dd35432e35f354e5dd453eb7daa8245b)
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
        '''Returns the Amazon Resource Name (ARN) for the specified ``AWS::IAM::SAMLProvider`` resource.

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
    @jsii.member(jsii_name="samlMetadataDocument")
    def saml_metadata_document(self) -> builtins.str:
        '''An XML document generated by an identity provider (IdP) that supports SAML 2.0. The document includes the issuer's name, expiration information, and keys that can be used to validate the SAML authentication response (assertions) that are received from the IdP. You must generate the metadata document using the identity management software that is used as your organization's IdP.'''
        return typing.cast(builtins.str, jsii.get(self, "samlMetadataDocument"))

    @saml_metadata_document.setter
    def saml_metadata_document(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c9b70ef0e0ed94f53ecf2221518796deaf4c5a9353a14b0183e26bbe0e0d57c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "samlMetadataDocument", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the provider to create.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf699aa7d755e072f3b60499335fb6469de4ed3bdb0605652b9c3269877e220a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags that you want to attach to the new IAM SAML provider.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b139c04642da2a9b428a58eb37077beb7f9b79971517b5fd95e8c7dbfa322e67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.CfnSAMLProviderProps",
    jsii_struct_bases=[],
    name_mapping={
        "saml_metadata_document": "samlMetadataDocument",
        "name": "name",
        "tags": "tags",
    },
)
class CfnSAMLProviderProps:
    def __init__(
        self,
        *,
        saml_metadata_document: builtins.str,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSAMLProvider``.

        :param saml_metadata_document: An XML document generated by an identity provider (IdP) that supports SAML 2.0. The document includes the issuer's name, expiration information, and keys that can be used to validate the SAML authentication response (assertions) that are received from the IdP. You must generate the metadata document using the identity management software that is used as your organization's IdP. For more information, see `About SAML 2.0-based federation <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html>`_ in the *IAM User Guide*
        :param name: The name of the provider to create. This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        :param tags: A list of tags that you want to attach to the new IAM SAML provider. Each tag consists of a key name and an associated value. For more information about tagging, see `Tagging IAM resources <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`_ in the *IAM User Guide* . .. epigraph:: If any one of the tags is invalid or if you exceed the allowed maximum number of tags, then the entire request fails and the resource is not created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-samlprovider.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            
            cfn_sAMLProvider_props = iam.CfnSAMLProviderProps(
                saml_metadata_document="samlMetadataDocument",
            
                # the properties below are optional
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__753bbb479e0c0a542a8456d357a3312bedbcc25e8753ca69dabd0ebf09aa6de7)
            check_type(argname="argument saml_metadata_document", value=saml_metadata_document, expected_type=type_hints["saml_metadata_document"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "saml_metadata_document": saml_metadata_document,
        }
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def saml_metadata_document(self) -> builtins.str:
        '''An XML document generated by an identity provider (IdP) that supports SAML 2.0. The document includes the issuer's name, expiration information, and keys that can be used to validate the SAML authentication response (assertions) that are received from the IdP. You must generate the metadata document using the identity management software that is used as your organization's IdP.

        For more information, see `About SAML 2.0-based federation <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html>`_ in the *IAM User Guide*

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-samlprovider.html#cfn-iam-samlprovider-samlmetadatadocument
        '''
        result = self._values.get("saml_metadata_document")
        assert result is not None, "Required property 'saml_metadata_document' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the provider to create.

        This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-samlprovider.html#cfn-iam-samlprovider-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags that you want to attach to the new IAM SAML provider.

        Each tag consists of a key name and an associated value. For more information about tagging, see `Tagging IAM resources <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`_ in the *IAM User Guide* .
        .. epigraph::

           If any one of the tags is invalid or if you exceed the allowed maximum number of tags, then the entire request fails and the resource is not created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-samlprovider.html#cfn-iam-samlprovider-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSAMLProviderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnServerCertificate(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.CfnServerCertificate",
):
    '''Uploads a server certificate entity for the AWS account .

    The server certificate entity includes a public key certificate, a private key, and an optional certificate chain, which should all be PEM-encoded.

    We recommend that you use `AWS Certificate Manager <https://docs.aws.amazon.com/acm/>`_ to provision, manage, and deploy your server certificates. With ACM you can request a certificate, deploy it to AWS resources, and let ACM handle certificate renewals for you. Certificates provided by ACM are free. For more information about using ACM, see the `AWS Certificate Manager User Guide <https://docs.aws.amazon.com/acm/latest/userguide/>`_ .

    For more information about working with server certificates, see `Working with server certificates <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html>`_ in the *IAM User Guide* . This topic includes a list of AWS services that can use the server certificates that you manage with IAM.

    For information about the number of server certificates you can upload, see `IAM and AWS STS quotas <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html>`_ in the *IAM User Guide* .
    .. epigraph::

       Because the body of the public key certificate, private key, and the certificate chain can be large, you should use POST rather than GET when calling ``UploadServerCertificate`` . For information about setting up signatures and authorization through the API, see `Signing AWS API requests <https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html>`_ in the *AWS General Reference* . For general information about using the Query API with IAM, see `Calling the API by making HTTP query requests <https://docs.aws.amazon.com/IAM/latest/UserGuide/programming.html>`_ in the *IAM User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servercertificate.html
    :cloudformationResource: AWS::IAM::ServerCertificate
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iam as iam
        
        cfn_server_certificate = iam.CfnServerCertificate(self, "MyCfnServerCertificate",
            certificate_body="certificateBody",
            certificate_chain="certificateChain",
            path="path",
            private_key="privateKey",
            server_certificate_name="serverCertificateName",
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
        certificate_body: typing.Optional[builtins.str] = None,
        certificate_chain: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        private_key: typing.Optional[builtins.str] = None,
        server_certificate_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param certificate_body: The contents of the public key certificate.
        :param certificate_chain: The contents of the public key certificate chain.
        :param path: The path for the server certificate. For more information about paths, see `IAM identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`_ in the *IAM User Guide* . This parameter is optional. If it is not included, it defaults to a slash (/). This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! ( ``\\u0021`` ) through the DEL character ( ``\\u007F`` ), including most punctuation characters, digits, and upper and lowercased letters. .. epigraph:: If you are uploading a server certificate specifically for use with Amazon CloudFront distributions, you must specify a path using the ``path`` parameter. The path must begin with ``/cloudfront`` and must include a trailing slash (for example, ``/cloudfront/test/`` ).
        :param private_key: The contents of the private key in PEM-encoded format. The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ used to validate this parameter is a string of characters consisting of the following: - Any printable ASCII character ranging from the space character ( ``\\u0020`` ) through the end of the ASCII character range - The printable characters in the Basic Latin and Latin-1 Supplement character set (through ``\\u00FF`` ) - The special characters tab ( ``\\u0009`` ), line feed ( ``\\u000A`` ), and carriage return ( ``\\u000D`` )
        :param server_certificate_name: The name for the server certificate. Do not include the path in this value. The name of the certificate cannot contain any spaces. This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        :param tags: A list of tags that are attached to the server certificate. For more information about tagging, see `Tagging IAM resources <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`_ in the *IAM User Guide* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6cf37b70ff9a27f22bc984fc19e96b2e42e00f83cc2e2efd66e3b46e76e4b5b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnServerCertificateProps(
            certificate_body=certificate_body,
            certificate_chain=certificate_chain,
            path=path,
            private_key=private_key,
            server_certificate_name=server_certificate_name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__366b62f33040d7a5e531fab130ce2a8bbbba719ed080e892236f3127f59f0273)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4a54a0dba3e2e40002701a3afd9e2e4bf8ce9a72d2137a4aaa4aa728c81f007a)
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
        '''Returns the Amazon Resource Name (ARN) for the specified ``AWS::IAM::ServerCertificate`` resource.

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
    @jsii.member(jsii_name="certificateBody")
    def certificate_body(self) -> typing.Optional[builtins.str]:
        '''The contents of the public key certificate.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateBody"))

    @certificate_body.setter
    def certificate_body(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87c7211629136fb42c02f367b9448da78ab4e5abfd4d9e04ab0caad5325bb2b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateBody", value)

    @builtins.property
    @jsii.member(jsii_name="certificateChain")
    def certificate_chain(self) -> typing.Optional[builtins.str]:
        '''The contents of the public key certificate chain.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateChain"))

    @certificate_chain.setter
    def certificate_chain(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4ff303b49caa7890566d08d6a2a60ec1a95e65e81edd71a7aa6f85f708e4fdd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateChain", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> typing.Optional[builtins.str]:
        '''The path for the server certificate.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "path"))

    @path.setter
    def path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77ad8bd4800869c88771ef98910278fbbe26e1520e96f812fdbc0837580817e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="privateKey")
    def private_key(self) -> typing.Optional[builtins.str]:
        '''The contents of the private key in PEM-encoded format.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKey"))

    @private_key.setter
    def private_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4203fd09b7317247f69586ca724e62c2ea809be65e02471885451dfe4324b20)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKey", value)

    @builtins.property
    @jsii.member(jsii_name="serverCertificateName")
    def server_certificate_name(self) -> typing.Optional[builtins.str]:
        '''The name for the server certificate.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverCertificateName"))

    @server_certificate_name.setter
    def server_certificate_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54cd160d96a28915ae295954600508a01387f155ef6c01892d38e609428f5648)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverCertificateName", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags that are attached to the server certificate.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__579aa0e0cc52787dc34d6f715f95942533f29fc470256c2e7e0cd454c26ae2f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.CfnServerCertificateProps",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_body": "certificateBody",
        "certificate_chain": "certificateChain",
        "path": "path",
        "private_key": "privateKey",
        "server_certificate_name": "serverCertificateName",
        "tags": "tags",
    },
)
class CfnServerCertificateProps:
    def __init__(
        self,
        *,
        certificate_body: typing.Optional[builtins.str] = None,
        certificate_chain: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        private_key: typing.Optional[builtins.str] = None,
        server_certificate_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnServerCertificate``.

        :param certificate_body: The contents of the public key certificate.
        :param certificate_chain: The contents of the public key certificate chain.
        :param path: The path for the server certificate. For more information about paths, see `IAM identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`_ in the *IAM User Guide* . This parameter is optional. If it is not included, it defaults to a slash (/). This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! ( ``\\u0021`` ) through the DEL character ( ``\\u007F`` ), including most punctuation characters, digits, and upper and lowercased letters. .. epigraph:: If you are uploading a server certificate specifically for use with Amazon CloudFront distributions, you must specify a path using the ``path`` parameter. The path must begin with ``/cloudfront`` and must include a trailing slash (for example, ``/cloudfront/test/`` ).
        :param private_key: The contents of the private key in PEM-encoded format. The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ used to validate this parameter is a string of characters consisting of the following: - Any printable ASCII character ranging from the space character ( ``\\u0020`` ) through the end of the ASCII character range - The printable characters in the Basic Latin and Latin-1 Supplement character set (through ``\\u00FF`` ) - The special characters tab ( ``\\u0009`` ), line feed ( ``\\u000A`` ), and carriage return ( ``\\u000D`` )
        :param server_certificate_name: The name for the server certificate. Do not include the path in this value. The name of the certificate cannot contain any spaces. This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        :param tags: A list of tags that are attached to the server certificate. For more information about tagging, see `Tagging IAM resources <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`_ in the *IAM User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servercertificate.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            
            cfn_server_certificate_props = iam.CfnServerCertificateProps(
                certificate_body="certificateBody",
                certificate_chain="certificateChain",
                path="path",
                private_key="privateKey",
                server_certificate_name="serverCertificateName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c0fa14d93aea4f905649a3dfa7bcd3ea31e86d8c6ac197efe6a3040eb6155f7)
            check_type(argname="argument certificate_body", value=certificate_body, expected_type=type_hints["certificate_body"])
            check_type(argname="argument certificate_chain", value=certificate_chain, expected_type=type_hints["certificate_chain"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument private_key", value=private_key, expected_type=type_hints["private_key"])
            check_type(argname="argument server_certificate_name", value=server_certificate_name, expected_type=type_hints["server_certificate_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if certificate_body is not None:
            self._values["certificate_body"] = certificate_body
        if certificate_chain is not None:
            self._values["certificate_chain"] = certificate_chain
        if path is not None:
            self._values["path"] = path
        if private_key is not None:
            self._values["private_key"] = private_key
        if server_certificate_name is not None:
            self._values["server_certificate_name"] = server_certificate_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def certificate_body(self) -> typing.Optional[builtins.str]:
        '''The contents of the public key certificate.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servercertificate.html#cfn-iam-servercertificate-certificatebody
        '''
        result = self._values.get("certificate_body")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_chain(self) -> typing.Optional[builtins.str]:
        '''The contents of the public key certificate chain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servercertificate.html#cfn-iam-servercertificate-certificatechain
        '''
        result = self._values.get("certificate_chain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''The path for the server certificate.

        For more information about paths, see `IAM identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`_ in the *IAM User Guide* .

        This parameter is optional. If it is not included, it defaults to a slash (/). This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! ( ``\\u0021`` ) through the DEL character ( ``\\u007F`` ), including most punctuation characters, digits, and upper and lowercased letters.
        .. epigraph::

           If you are uploading a server certificate specifically for use with Amazon CloudFront distributions, you must specify a path using the ``path`` parameter. The path must begin with ``/cloudfront`` and must include a trailing slash (for example, ``/cloudfront/test/`` ).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servercertificate.html#cfn-iam-servercertificate-path
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_key(self) -> typing.Optional[builtins.str]:
        '''The contents of the private key in PEM-encoded format.

        The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ used to validate this parameter is a string of characters consisting of the following:

        - Any printable ASCII character ranging from the space character ( ``\\u0020`` ) through the end of the ASCII character range
        - The printable characters in the Basic Latin and Latin-1 Supplement character set (through ``\\u00FF`` )
        - The special characters tab ( ``\\u0009`` ), line feed ( ``\\u000A`` ), and carriage return ( ``\\u000D`` )

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servercertificate.html#cfn-iam-servercertificate-privatekey
        '''
        result = self._values.get("private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_certificate_name(self) -> typing.Optional[builtins.str]:
        '''The name for the server certificate.

        Do not include the path in this value. The name of the certificate cannot contain any spaces.

        This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servercertificate.html#cfn-iam-servercertificate-servercertificatename
        '''
        result = self._values.get("server_certificate_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags that are attached to the server certificate.

        For more information about tagging, see `Tagging IAM resources <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`_ in the *IAM User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servercertificate.html#cfn-iam-servercertificate-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServerCertificateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnServiceLinkedRole(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.CfnServiceLinkedRole",
):
    '''Creates an IAM role that is linked to a specific AWS service.

    The service controls the attached policies and when the role can be deleted. This helps ensure that the service is not broken by an unexpectedly changed or deleted role, which could put your AWS resources into an unknown state. Allowing the service to control the role helps improve service stability and proper cleanup when a service and its role are no longer needed. For more information, see `Using service-linked roles <https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html>`_ in the *IAM User Guide* .

    To attach a policy to this service-linked role, you must make the request using the AWS service that depends on this role.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servicelinkedrole.html
    :cloudformationResource: AWS::IAM::ServiceLinkedRole
    :exampleMetadata: infused

    Example::

        slr = iam.CfnServiceLinkedRole(self, "ElasticSLR",
            aws_service_name="es.amazonaws.com"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        aws_service_name: typing.Optional[builtins.str] = None,
        custom_suffix: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param aws_service_name: The service principal for the AWS service to which this role is attached. You use a string similar to a URL but without the http:// in front. For example: ``elasticbeanstalk.amazonaws.com`` . Service principals are unique and case-sensitive. To find the exact service principal for your service-linked role, see `AWS services that work with IAM <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html>`_ in the *IAM User Guide* . Look for the services that have *Yes* in the *Service-Linked Role* column. Choose the *Yes* link to view the service-linked role documentation for that service.
        :param custom_suffix: A string that you provide, which is combined with the service-provided prefix to form the complete role name. If you make multiple requests for the same service, then you must supply a different ``CustomSuffix`` for each request. Otherwise the request fails with a duplicate role name error. For example, you could add ``-1`` or ``-debug`` to the suffix. Some services do not support the ``CustomSuffix`` parameter. If you provide an optional suffix and the operation fails, try the operation again without the suffix.
        :param description: The description of the role.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d428bb539fd6df78e6e28b0695f366af555fe1f958879857ee30c8067e2af789)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnServiceLinkedRoleProps(
            aws_service_name=aws_service_name,
            custom_suffix=custom_suffix,
            description=description,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cc7c392a2b0731277a0218b6b90c103a720e9d973fe65098c66c9cbdbc1777d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7f0f81638df3b5467a6f2750e681e60bb99239f2a978002ef69aae000229a742)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrRoleName")
    def attr_role_name(self) -> builtins.str:
        '''Returns the friendly name that identifies the role.

        For example, ``AWSServiceRoleForAutoScaling`` or ``AWSServiceRoleForAutoScaling_TestSuffix`` if a ``CustomSuffix`` is specified.

        :cloudformationAttribute: RoleName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRoleName"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="awsServiceName")
    def aws_service_name(self) -> typing.Optional[builtins.str]:
        '''The service principal for the AWS service to which this role is attached.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsServiceName"))

    @aws_service_name.setter
    def aws_service_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__894356a5067d4595c32429fb905a7c37dbca2ce428fa3c0743817d563a07b673)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsServiceName", value)

    @builtins.property
    @jsii.member(jsii_name="customSuffix")
    def custom_suffix(self) -> typing.Optional[builtins.str]:
        '''A string that you provide, which is combined with the service-provided prefix to form the complete role name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customSuffix"))

    @custom_suffix.setter
    def custom_suffix(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73b7c9779d86988f0dcb8c2282ce3fb8bd23b1db482b7081dbf555457bc45bdc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customSuffix", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the role.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__796fb2b9a69a72a7ee224d68a6ba88159e7107645a0f704a025f9b8bf7b3d6ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.CfnServiceLinkedRoleProps",
    jsii_struct_bases=[],
    name_mapping={
        "aws_service_name": "awsServiceName",
        "custom_suffix": "customSuffix",
        "description": "description",
    },
)
class CfnServiceLinkedRoleProps:
    def __init__(
        self,
        *,
        aws_service_name: typing.Optional[builtins.str] = None,
        custom_suffix: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnServiceLinkedRole``.

        :param aws_service_name: The service principal for the AWS service to which this role is attached. You use a string similar to a URL but without the http:// in front. For example: ``elasticbeanstalk.amazonaws.com`` . Service principals are unique and case-sensitive. To find the exact service principal for your service-linked role, see `AWS services that work with IAM <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html>`_ in the *IAM User Guide* . Look for the services that have *Yes* in the *Service-Linked Role* column. Choose the *Yes* link to view the service-linked role documentation for that service.
        :param custom_suffix: A string that you provide, which is combined with the service-provided prefix to form the complete role name. If you make multiple requests for the same service, then you must supply a different ``CustomSuffix`` for each request. Otherwise the request fails with a duplicate role name error. For example, you could add ``-1`` or ``-debug`` to the suffix. Some services do not support the ``CustomSuffix`` parameter. If you provide an optional suffix and the operation fails, try the operation again without the suffix.
        :param description: The description of the role.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servicelinkedrole.html
        :exampleMetadata: infused

        Example::

            slr = iam.CfnServiceLinkedRole(self, "ElasticSLR",
                aws_service_name="es.amazonaws.com"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dafce478a4346996727c8ffa75ed8a924def97e273b5d6cc9f321b9c8eea85d7)
            check_type(argname="argument aws_service_name", value=aws_service_name, expected_type=type_hints["aws_service_name"])
            check_type(argname="argument custom_suffix", value=custom_suffix, expected_type=type_hints["custom_suffix"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aws_service_name is not None:
            self._values["aws_service_name"] = aws_service_name
        if custom_suffix is not None:
            self._values["custom_suffix"] = custom_suffix
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def aws_service_name(self) -> typing.Optional[builtins.str]:
        '''The service principal for the AWS service to which this role is attached.

        You use a string similar to a URL but without the http:// in front. For example: ``elasticbeanstalk.amazonaws.com`` .

        Service principals are unique and case-sensitive. To find the exact service principal for your service-linked role, see `AWS services that work with IAM <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html>`_ in the *IAM User Guide* . Look for the services that have *Yes* in the *Service-Linked Role* column. Choose the *Yes* link to view the service-linked role documentation for that service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servicelinkedrole.html#cfn-iam-servicelinkedrole-awsservicename
        '''
        result = self._values.get("aws_service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_suffix(self) -> typing.Optional[builtins.str]:
        '''A string that you provide, which is combined with the service-provided prefix to form the complete role name.

        If you make multiple requests for the same service, then you must supply a different ``CustomSuffix`` for each request. Otherwise the request fails with a duplicate role name error. For example, you could add ``-1`` or ``-debug`` to the suffix.

        Some services do not support the ``CustomSuffix`` parameter. If you provide an optional suffix and the operation fails, try the operation again without the suffix.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servicelinkedrole.html#cfn-iam-servicelinkedrole-customsuffix
        '''
        result = self._values.get("custom_suffix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the role.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servicelinkedrole.html#cfn-iam-servicelinkedrole-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServiceLinkedRoleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnUser(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.CfnUser",
):
    '''Creates a new IAM user for your AWS account .

    For information about quotas for the number of IAM users you can create, see `IAM and AWS STS quotas <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html>`_ in the *IAM User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-user.html
    :cloudformationResource: AWS::IAM::User
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iam as iam
        
        # policy_document: Any
        
        cfn_user = iam.CfnUser(self, "MyCfnUser",
            groups=["groups"],
            login_profile=iam.CfnUser.LoginProfileProperty(
                password="password",
        
                # the properties below are optional
                password_reset_required=False
            ),
            managed_policy_arns=["managedPolicyArns"],
            path="path",
            permissions_boundary="permissionsBoundary",
            policies=[iam.CfnUser.PolicyProperty(
                policy_document=policy_document,
                policy_name="policyName"
            )],
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            user_name="userName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        login_profile: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnUser.LoginProfileProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        managed_policy_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        path: typing.Optional[builtins.str] = None,
        permissions_boundary: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnUser.PolicyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        user_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param groups: A list of group names to which you want to add the user.
        :param login_profile: Creates a password for the specified IAM user. A password allows an IAM user to access AWS services through the AWS Management Console . You can use the AWS CLI , the AWS API, or the *Users* page in the IAM console to create a password for any IAM user. Use `ChangePassword <https://docs.aws.amazon.com/IAM/latest/APIReference/API_ChangePassword.html>`_ to update your own existing password in the *My Security Credentials* page in the AWS Management Console . For more information about managing passwords, see `Managing passwords <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_ManagingLogins.html>`_ in the *IAM User Guide* .
        :param managed_policy_arns: A list of Amazon Resource Names (ARNs) of the IAM managed policies that you want to attach to the user. For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .
        :param path: The path for the user name. For more information about paths, see `IAM identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`_ in the *IAM User Guide* . This parameter is optional. If it is not included, it defaults to a slash (/). This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! ( ``\\u0021`` ) through the DEL character ( ``\\u007F`` ), including most punctuation characters, digits, and upper and lowercased letters.
        :param permissions_boundary: The ARN of the managed policy that is used to set the permissions boundary for the user. A permissions boundary policy defines the maximum permissions that identity-based policies can grant to an entity, but does not grant permissions. Permissions boundaries do not define the maximum permissions that a resource-based policy can grant to an entity. To learn more, see `Permissions boundaries for IAM entities <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`_ in the *IAM User Guide* . For more information about policy types, see `Policy types <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policy-types>`_ in the *IAM User Guide* .
        :param policies: Adds or updates an inline policy document that is embedded in the specified IAM user. To view AWS::IAM::User snippets, see `Declaring an IAM User Resource <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-iam.html#scenario-iam-user>`_ . .. epigraph:: The name of each policy for a role, user, or group must be unique. If you don't choose unique names, updates to the IAM identity will fail. For information about limits on the number of inline policies that you can embed in a user, see `Limitations on IAM Entities <https://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html>`_ in the *IAM User Guide* .
        :param tags: A list of tags that you want to attach to the new user. Each tag consists of a key name and an associated value. For more information about tagging, see `Tagging IAM resources <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`_ in the *IAM User Guide* . .. epigraph:: If any one of the tags is invalid or if you exceed the allowed maximum number of tags, then the entire request fails and the resource is not created.
        :param user_name: The name of the user to create. Do not include the path in this value. This parameter allows (per its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-. The user name must be unique within the account. User names are not distinguished by case. For example, you cannot create users named both "John" and "john". If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the user name. If you specify a name, you must specify the ``CAPABILITY_NAMED_IAM`` value to acknowledge your template's capabilities. For more information, see `Acknowledging IAM Resources in AWS CloudFormation Templates <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-capabilities>`_ . .. epigraph:: Naming an IAM resource can cause an unrecoverable error if you reuse the same template in multiple Regions. To prevent this, we recommend using ``Fn::Join`` and ``AWS::Region`` to create a Region-specific name, as in the following example: ``{"Fn::Join": ["", [{"Ref": "AWS::Region"}, {"Ref": "MyResourceName"}]]}`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b453e8e55124e84a27aa60acd149280051b756df30318da37839b1e4ca523687)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnUserProps(
            groups=groups,
            login_profile=login_profile,
            managed_policy_arns=managed_policy_arns,
            path=path,
            permissions_boundary=permissions_boundary,
            policies=policies,
            tags=tags,
            user_name=user_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c540efa10e05810a6302626e0a6f54b2963bab597096fea4ee0e6023d72f25a8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e0ee3dc7778b587a3d4c4511b986f6fc1c9c865253acfb48b0df1fe42cd5f082)
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
        '''Returns the Amazon Resource Name (ARN) for the specified ``AWS::IAM::User`` resource.

        For example: ``arn:aws:iam::123456789012:user/mystack-myuser-1CCXAFG2H2U4D`` .

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
    @jsii.member(jsii_name="groups")
    def groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of group names to which you want to add the user.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groups"))

    @groups.setter
    def groups(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a030f35db68335b8a550d10c248a4f289bc47052d3d3d7ad1feb6d43257f1398)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groups", value)

    @builtins.property
    @jsii.member(jsii_name="loginProfile")
    def login_profile(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnUser.LoginProfileProperty"]]:
        '''Creates a password for the specified IAM user.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnUser.LoginProfileProperty"]], jsii.get(self, "loginProfile"))

    @login_profile.setter
    def login_profile(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnUser.LoginProfileProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9ec71116c53dba6fcd83f943f62c54cf4a1829d2c1fbfb773b475eb2e580e43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loginProfile", value)

    @builtins.property
    @jsii.member(jsii_name="managedPolicyArns")
    def managed_policy_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of Amazon Resource Names (ARNs) of the IAM managed policies that you want to attach to the user.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "managedPolicyArns"))

    @managed_policy_arns.setter
    def managed_policy_arns(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d9bc7aa1272c0c2d7eca931089eb5238a71667de1dd61a5e39d1bb0d80b06ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedPolicyArns", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> typing.Optional[builtins.str]:
        '''The path for the user name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "path"))

    @path.setter
    def path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b45a0c327fbd95f77396687ff75f3c61c77223d854a371180accaa05cec25e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="permissionsBoundary")
    def permissions_boundary(self) -> typing.Optional[builtins.str]:
        '''The ARN of the managed policy that is used to set the permissions boundary for the user.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "permissionsBoundary"))

    @permissions_boundary.setter
    def permissions_boundary(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__766b6286be304f39fa6308bbe3eb6a8a552712c6becdc31706c5312027885dc7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionsBoundary", value)

    @builtins.property
    @jsii.member(jsii_name="policies")
    def policies(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnUser.PolicyProperty"]]]]:
        '''Adds or updates an inline policy document that is embedded in the specified IAM user.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnUser.PolicyProperty"]]]], jsii.get(self, "policies"))

    @policies.setter
    def policies(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnUser.PolicyProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25df8a318c9f526fd31465b78f732e159102acc489b971d41ccdbe1b91ff426e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policies", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags that you want to attach to the new user.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68bb5e640fe8f1d3df25a029bc80e69cb1904a783dae4c75d6eb193e37389a44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="userName")
    def user_name(self) -> typing.Optional[builtins.str]:
        '''The name of the user to create.

        Do not include the path in this value.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userName"))

    @user_name.setter
    def user_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__673a92f6f8c13a39a21d59717aefb8413279cd51db902ce34f4e3611efe7c1f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userName", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iam.CfnUser.LoginProfileProperty",
        jsii_struct_bases=[],
        name_mapping={
            "password": "password",
            "password_reset_required": "passwordResetRequired",
        },
    )
    class LoginProfileProperty:
        def __init__(
            self,
            *,
            password: builtins.str,
            password_reset_required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Creates a password for the specified user, giving the user the ability to access AWS services through the AWS Management Console .

            For more information about managing passwords, see `Managing Passwords <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_ManagingLogins.html>`_ in the *IAM User Guide* .

            :param password: The user's password.
            :param password_reset_required: Specifies whether the user is required to set a new password on next sign-in.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user-loginprofile.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iam as iam
                
                login_profile_property = iam.CfnUser.LoginProfileProperty(
                    password="password",
                
                    # the properties below are optional
                    password_reset_required=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9b9798165bbdd5df9e80975dc2c6efce6bd25d4f2cb0e4afb86f5dd32cb51e5a)
                check_type(argname="argument password", value=password, expected_type=type_hints["password"])
                check_type(argname="argument password_reset_required", value=password_reset_required, expected_type=type_hints["password_reset_required"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "password": password,
            }
            if password_reset_required is not None:
                self._values["password_reset_required"] = password_reset_required

        @builtins.property
        def password(self) -> builtins.str:
            '''The user's password.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user-loginprofile.html#cfn-iam-user-loginprofile-password
            '''
            result = self._values.get("password")
            assert result is not None, "Required property 'password' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def password_reset_required(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether the user is required to set a new password on next sign-in.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user-loginprofile.html#cfn-iam-user-loginprofile-passwordresetrequired
            '''
            result = self._values.get("password_reset_required")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoginProfileProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iam.CfnUser.PolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "policy_document": "policyDocument",
            "policy_name": "policyName",
        },
    )
    class PolicyProperty:
        def __init__(
            self,
            *,
            policy_document: typing.Any,
            policy_name: builtins.str,
        ) -> None:
            '''Contains information about an attached policy.

            An attached policy is a managed policy that has been attached to a user, group, or role.

            For more information about managed policies, refer to `Managed Policies and Inline Policies <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`_ in the *IAM User Guide* .

            :param policy_document: The entire contents of the policy that defines permissions. For more information, see `Overview of JSON policies <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-json>`_ .
            :param policy_name: The friendly name (not ARN) identifying the policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user-policy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iam as iam
                
                # policy_document: Any
                
                policy_property = iam.CfnUser.PolicyProperty(
                    policy_document=policy_document,
                    policy_name="policyName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e10d289e0033a52d00a2a3cfb4f5dd68a85b62b072e59b08358dbe810503669c)
                check_type(argname="argument policy_document", value=policy_document, expected_type=type_hints["policy_document"])
                check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "policy_document": policy_document,
                "policy_name": policy_name,
            }

        @builtins.property
        def policy_document(self) -> typing.Any:
            '''The entire contents of the policy that defines permissions.

            For more information, see `Overview of JSON policies <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-json>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user-policy.html#cfn-iam-user-policy-policydocument
            '''
            result = self._values.get("policy_document")
            assert result is not None, "Required property 'policy_document' is missing"
            return typing.cast(typing.Any, result)

        @builtins.property
        def policy_name(self) -> builtins.str:
            '''The friendly name (not ARN) identifying the policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user-policy.html#cfn-iam-user-policy-policyname
            '''
            result = self._values.get("policy_name")
            assert result is not None, "Required property 'policy_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnUserPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.CfnUserPolicy",
):
    '''Adds or updates an inline policy document that is embedded in the specified IAM user.

    An IAM user can also have a managed policy attached to it. To attach a managed policy to a user, use ```AWS::IAM::User`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html>`_ . To create a new managed policy, use ```AWS::IAM::ManagedPolicy`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html>`_ . For information about policies, see `Managed policies and inline policies <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`_ in the *IAM User Guide* .

    For information about the maximum number of inline policies that you can embed in a user, see `IAM and AWS STS quotas <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html>`_ in the *IAM User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-userpolicy.html
    :cloudformationResource: AWS::IAM::UserPolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iam as iam
        
        # policy_document: Any
        
        cfn_user_policy = iam.CfnUserPolicy(self, "MyCfnUserPolicy",
            policy_name="policyName",
            user_name="userName",
        
            # the properties below are optional
            policy_document=policy_document
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        policy_name: builtins.str,
        user_name: builtins.str,
        policy_document: typing.Any = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param policy_name: The name of the policy document. This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        :param user_name: The name of the user to associate the policy with. This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        :param policy_document: The policy document. You must provide policies in JSON format in IAM. However, for AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it to IAM. The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ used to validate this parameter is a string of characters consisting of the following: - Any printable ASCII character ranging from the space character ( ``\\u0020`` ) through the end of the ASCII character range - The printable characters in the Basic Latin and Latin-1 Supplement character set (through ``\\u00FF`` ) - The special characters tab ( ``\\u0009`` ), line feed ( ``\\u000A`` ), and carriage return ( ``\\u000D`` )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b09938208fba24d256ecd68450b14a065d6488754943e666f9c0528cd0571773)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnUserPolicyProps(
            policy_name=policy_name,
            user_name=user_name,
            policy_document=policy_document,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cde7256763c767d2775e466edc810c10426403d26df61b45c5e90e87328e04f1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3ce5c91a6c338867856c8d0c8e4fb1baca52b1340f6738e4b2d9310ae995e3d0)
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
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        '''The name of the policy document.'''
        return typing.cast(builtins.str, jsii.get(self, "policyName"))

    @policy_name.setter
    def policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1863a06ff9856e56ddfef1835185f36375de9aab427703c632667bf53aed26d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyName", value)

    @builtins.property
    @jsii.member(jsii_name="userName")
    def user_name(self) -> builtins.str:
        '''The name of the user to associate the policy with.'''
        return typing.cast(builtins.str, jsii.get(self, "userName"))

    @user_name.setter
    def user_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c87f136af227b9d80b9c996ebad3cd0115cf869a0b881cdc44f69822e5d676a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userName", value)

    @builtins.property
    @jsii.member(jsii_name="policyDocument")
    def policy_document(self) -> typing.Any:
        '''The policy document.'''
        return typing.cast(typing.Any, jsii.get(self, "policyDocument"))

    @policy_document.setter
    def policy_document(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__868920d1b0a57c789262fb64d7c1ce084d6f3da90f834b2da8cc620e6553bad8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyDocument", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.CfnUserPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "policy_name": "policyName",
        "user_name": "userName",
        "policy_document": "policyDocument",
    },
)
class CfnUserPolicyProps:
    def __init__(
        self,
        *,
        policy_name: builtins.str,
        user_name: builtins.str,
        policy_document: typing.Any = None,
    ) -> None:
        '''Properties for defining a ``CfnUserPolicy``.

        :param policy_name: The name of the policy document. This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        :param user_name: The name of the user to associate the policy with. This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        :param policy_document: The policy document. You must provide policies in JSON format in IAM. However, for AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it to IAM. The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ used to validate this parameter is a string of characters consisting of the following: - Any printable ASCII character ranging from the space character ( ``\\u0020`` ) through the end of the ASCII character range - The printable characters in the Basic Latin and Latin-1 Supplement character set (through ``\\u00FF`` ) - The special characters tab ( ``\\u0009`` ), line feed ( ``\\u000A`` ), and carriage return ( ``\\u000D`` )

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-userpolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            
            # policy_document: Any
            
            cfn_user_policy_props = iam.CfnUserPolicyProps(
                policy_name="policyName",
                user_name="userName",
            
                # the properties below are optional
                policy_document=policy_document
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe6f239efe54addc57c69dc765719968f9ffeb9e19e348f502085249d1739fd5)
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
            check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
            check_type(argname="argument policy_document", value=policy_document, expected_type=type_hints["policy_document"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_name": policy_name,
            "user_name": user_name,
        }
        if policy_document is not None:
            self._values["policy_document"] = policy_document

    @builtins.property
    def policy_name(self) -> builtins.str:
        '''The name of the policy document.

        This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-userpolicy.html#cfn-iam-userpolicy-policyname
        '''
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_name(self) -> builtins.str:
        '''The name of the user to associate the policy with.

        This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-userpolicy.html#cfn-iam-userpolicy-username
        '''
        result = self._values.get("user_name")
        assert result is not None, "Required property 'user_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_document(self) -> typing.Any:
        '''The policy document.

        You must provide policies in JSON format in IAM. However, for AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it to IAM.

        The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ used to validate this parameter is a string of characters consisting of the following:

        - Any printable ASCII character ranging from the space character ( ``\\u0020`` ) through the end of the ASCII character range
        - The printable characters in the Basic Latin and Latin-1 Supplement character set (through ``\\u00FF`` )
        - The special characters tab ( ``\\u0009`` ), line feed ( ``\\u000A`` ), and carriage return ( ``\\u000D`` )

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-userpolicy.html#cfn-iam-userpolicy-policydocument
        '''
        result = self._values.get("policy_document")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUserPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.CfnUserProps",
    jsii_struct_bases=[],
    name_mapping={
        "groups": "groups",
        "login_profile": "loginProfile",
        "managed_policy_arns": "managedPolicyArns",
        "path": "path",
        "permissions_boundary": "permissionsBoundary",
        "policies": "policies",
        "tags": "tags",
        "user_name": "userName",
    },
)
class CfnUserProps:
    def __init__(
        self,
        *,
        groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        login_profile: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnUser.LoginProfileProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        managed_policy_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        path: typing.Optional[builtins.str] = None,
        permissions_boundary: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnUser.PolicyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        user_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnUser``.

        :param groups: A list of group names to which you want to add the user.
        :param login_profile: Creates a password for the specified IAM user. A password allows an IAM user to access AWS services through the AWS Management Console . You can use the AWS CLI , the AWS API, or the *Users* page in the IAM console to create a password for any IAM user. Use `ChangePassword <https://docs.aws.amazon.com/IAM/latest/APIReference/API_ChangePassword.html>`_ to update your own existing password in the *My Security Credentials* page in the AWS Management Console . For more information about managing passwords, see `Managing passwords <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_ManagingLogins.html>`_ in the *IAM User Guide* .
        :param managed_policy_arns: A list of Amazon Resource Names (ARNs) of the IAM managed policies that you want to attach to the user. For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .
        :param path: The path for the user name. For more information about paths, see `IAM identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`_ in the *IAM User Guide* . This parameter is optional. If it is not included, it defaults to a slash (/). This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! ( ``\\u0021`` ) through the DEL character ( ``\\u007F`` ), including most punctuation characters, digits, and upper and lowercased letters.
        :param permissions_boundary: The ARN of the managed policy that is used to set the permissions boundary for the user. A permissions boundary policy defines the maximum permissions that identity-based policies can grant to an entity, but does not grant permissions. Permissions boundaries do not define the maximum permissions that a resource-based policy can grant to an entity. To learn more, see `Permissions boundaries for IAM entities <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`_ in the *IAM User Guide* . For more information about policy types, see `Policy types <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policy-types>`_ in the *IAM User Guide* .
        :param policies: Adds or updates an inline policy document that is embedded in the specified IAM user. To view AWS::IAM::User snippets, see `Declaring an IAM User Resource <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-iam.html#scenario-iam-user>`_ . .. epigraph:: The name of each policy for a role, user, or group must be unique. If you don't choose unique names, updates to the IAM identity will fail. For information about limits on the number of inline policies that you can embed in a user, see `Limitations on IAM Entities <https://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html>`_ in the *IAM User Guide* .
        :param tags: A list of tags that you want to attach to the new user. Each tag consists of a key name and an associated value. For more information about tagging, see `Tagging IAM resources <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`_ in the *IAM User Guide* . .. epigraph:: If any one of the tags is invalid or if you exceed the allowed maximum number of tags, then the entire request fails and the resource is not created.
        :param user_name: The name of the user to create. Do not include the path in this value. This parameter allows (per its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-. The user name must be unique within the account. User names are not distinguished by case. For example, you cannot create users named both "John" and "john". If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the user name. If you specify a name, you must specify the ``CAPABILITY_NAMED_IAM`` value to acknowledge your template's capabilities. For more information, see `Acknowledging IAM Resources in AWS CloudFormation Templates <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-capabilities>`_ . .. epigraph:: Naming an IAM resource can cause an unrecoverable error if you reuse the same template in multiple Regions. To prevent this, we recommend using ``Fn::Join`` and ``AWS::Region`` to create a Region-specific name, as in the following example: ``{"Fn::Join": ["", [{"Ref": "AWS::Region"}, {"Ref": "MyResourceName"}]]}`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-user.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            
            # policy_document: Any
            
            cfn_user_props = iam.CfnUserProps(
                groups=["groups"],
                login_profile=iam.CfnUser.LoginProfileProperty(
                    password="password",
            
                    # the properties below are optional
                    password_reset_required=False
                ),
                managed_policy_arns=["managedPolicyArns"],
                path="path",
                permissions_boundary="permissionsBoundary",
                policies=[iam.CfnUser.PolicyProperty(
                    policy_document=policy_document,
                    policy_name="policyName"
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                user_name="userName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b4312dc8ff103705c67491ae6f470e2644acffd396e5635261bf47e9a8a945f)
            check_type(argname="argument groups", value=groups, expected_type=type_hints["groups"])
            check_type(argname="argument login_profile", value=login_profile, expected_type=type_hints["login_profile"])
            check_type(argname="argument managed_policy_arns", value=managed_policy_arns, expected_type=type_hints["managed_policy_arns"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument permissions_boundary", value=permissions_boundary, expected_type=type_hints["permissions_boundary"])
            check_type(argname="argument policies", value=policies, expected_type=type_hints["policies"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if groups is not None:
            self._values["groups"] = groups
        if login_profile is not None:
            self._values["login_profile"] = login_profile
        if managed_policy_arns is not None:
            self._values["managed_policy_arns"] = managed_policy_arns
        if path is not None:
            self._values["path"] = path
        if permissions_boundary is not None:
            self._values["permissions_boundary"] = permissions_boundary
        if policies is not None:
            self._values["policies"] = policies
        if tags is not None:
            self._values["tags"] = tags
        if user_name is not None:
            self._values["user_name"] = user_name

    @builtins.property
    def groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of group names to which you want to add the user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-user.html#cfn-iam-user-groups
        '''
        result = self._values.get("groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def login_profile(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnUser.LoginProfileProperty]]:
        '''Creates a password for the specified IAM user.

        A password allows an IAM user to access AWS services through the AWS Management Console .

        You can use the AWS CLI , the AWS API, or the *Users* page in the IAM console to create a password for any IAM user. Use `ChangePassword <https://docs.aws.amazon.com/IAM/latest/APIReference/API_ChangePassword.html>`_ to update your own existing password in the *My Security Credentials* page in the AWS Management Console .

        For more information about managing passwords, see `Managing passwords <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_ManagingLogins.html>`_ in the *IAM User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-user.html#cfn-iam-user-loginprofile
        '''
        result = self._values.get("login_profile")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnUser.LoginProfileProperty]], result)

    @builtins.property
    def managed_policy_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of Amazon Resource Names (ARNs) of the IAM managed policies that you want to attach to the user.

        For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-user.html#cfn-iam-user-managedpolicyarns
        '''
        result = self._values.get("managed_policy_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''The path for the user name.

        For more information about paths, see `IAM identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`_ in the *IAM User Guide* .

        This parameter is optional. If it is not included, it defaults to a slash (/).

        This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! ( ``\\u0021`` ) through the DEL character ( ``\\u007F`` ), including most punctuation characters, digits, and upper and lowercased letters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-user.html#cfn-iam-user-path
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permissions_boundary(self) -> typing.Optional[builtins.str]:
        '''The ARN of the managed policy that is used to set the permissions boundary for the user.

        A permissions boundary policy defines the maximum permissions that identity-based policies can grant to an entity, but does not grant permissions. Permissions boundaries do not define the maximum permissions that a resource-based policy can grant to an entity. To learn more, see `Permissions boundaries for IAM entities <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`_ in the *IAM User Guide* .

        For more information about policy types, see `Policy types <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policy-types>`_ in the *IAM User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-user.html#cfn-iam-user-permissionsboundary
        '''
        result = self._values.get("permissions_boundary")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policies(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnUser.PolicyProperty]]]]:
        '''Adds or updates an inline policy document that is embedded in the specified IAM user.

        To view AWS::IAM::User snippets, see `Declaring an IAM User Resource <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-iam.html#scenario-iam-user>`_ .
        .. epigraph::

           The name of each policy for a role, user, or group must be unique. If you don't choose unique names, updates to the IAM identity will fail.

        For information about limits on the number of inline policies that you can embed in a user, see `Limitations on IAM Entities <https://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html>`_ in the *IAM User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-user.html#cfn-iam-user-policies
        '''
        result = self._values.get("policies")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnUser.PolicyProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags that you want to attach to the new user.

        Each tag consists of a key name and an associated value. For more information about tagging, see `Tagging IAM resources <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`_ in the *IAM User Guide* .
        .. epigraph::

           If any one of the tags is invalid or if you exceed the allowed maximum number of tags, then the entire request fails and the resource is not created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-user.html#cfn-iam-user-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def user_name(self) -> typing.Optional[builtins.str]:
        '''The name of the user to create. Do not include the path in this value.

        This parameter allows (per its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-. The user name must be unique within the account. User names are not distinguished by case. For example, you cannot create users named both "John" and "john".

        If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the user name.

        If you specify a name, you must specify the ``CAPABILITY_NAMED_IAM`` value to acknowledge your template's capabilities. For more information, see `Acknowledging IAM Resources in AWS CloudFormation Templates <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-capabilities>`_ .
        .. epigraph::

           Naming an IAM resource can cause an unrecoverable error if you reuse the same template in multiple Regions. To prevent this, we recommend using ``Fn::Join`` and ``AWS::Region`` to create a Region-specific name, as in the following example: ``{"Fn::Join": ["", [{"Ref": "AWS::Region"}, {"Ref": "MyResourceName"}]]}`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-user.html#cfn-iam-user-username
        '''
        result = self._values.get("user_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUserProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnUserToGroupAddition(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.CfnUserToGroupAddition",
):
    '''Adds the specified user to the specified group.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-usertogroupaddition.html
    :cloudformationResource: AWS::IAM::UserToGroupAddition
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iam as iam
        
        cfn_user_to_group_addition = iam.CfnUserToGroupAddition(self, "MyCfnUserToGroupAddition",
            group_name="groupName",
            users=["users"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        group_name: builtins.str,
        users: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param group_name: The name of the group to update. This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        :param users: A list of the names of the users that you want to add to the group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cff069f9e69e3551ebb007914281abb14f05e8d822825ab91577ecf95414ffb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnUserToGroupAdditionProps(group_name=group_name, users=users)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__839f86071dc7f367d40ea9ba8b644702b8c3f40d83e2a8d6821a097013d1a603)
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
            type_hints = typing.get_type_hints(_typecheckingstub__34d58a01767f256628192ca708cd20a48bd1b0ad6795595846565c2c84e235e8)
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
    @jsii.member(jsii_name="groupName")
    def group_name(self) -> builtins.str:
        '''The name of the group to update.'''
        return typing.cast(builtins.str, jsii.get(self, "groupName"))

    @group_name.setter
    def group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80988c0737b217a15fbc51dd191617d213752314ac76d041cba72fa2fbca3c04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupName", value)

    @builtins.property
    @jsii.member(jsii_name="users")
    def users(self) -> typing.List[builtins.str]:
        '''A list of the names of the users that you want to add to the group.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "users"))

    @users.setter
    def users(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9633608428e6d8df416ba93dfbf3f5248605fc8d2d8dc1be95067a291eb4223e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "users", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.CfnUserToGroupAdditionProps",
    jsii_struct_bases=[],
    name_mapping={"group_name": "groupName", "users": "users"},
)
class CfnUserToGroupAdditionProps:
    def __init__(
        self,
        *,
        group_name: builtins.str,
        users: typing.Sequence[builtins.str],
    ) -> None:
        '''Properties for defining a ``CfnUserToGroupAddition``.

        :param group_name: The name of the group to update. This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        :param users: A list of the names of the users that you want to add to the group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-usertogroupaddition.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            
            cfn_user_to_group_addition_props = iam.CfnUserToGroupAdditionProps(
                group_name="groupName",
                users=["users"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be028fcc46f0c07bb061d985679cb1824767d764103c011f6956ac7bb2f20043)
            check_type(argname="argument group_name", value=group_name, expected_type=type_hints["group_name"])
            check_type(argname="argument users", value=users, expected_type=type_hints["users"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "group_name": group_name,
            "users": users,
        }

    @builtins.property
    def group_name(self) -> builtins.str:
        '''The name of the group to update.

        This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-usertogroupaddition.html#cfn-iam-usertogroupaddition-groupname
        '''
        result = self._values.get("group_name")
        assert result is not None, "Required property 'group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def users(self) -> typing.List[builtins.str]:
        '''A list of the names of the users that you want to add to the group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-usertogroupaddition.html#cfn-iam-usertogroupaddition-users
        '''
        result = self._values.get("users")
        assert result is not None, "Required property 'users' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUserToGroupAdditionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnVirtualMFADevice(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.CfnVirtualMFADevice",
):
    '''Creates a new virtual MFA device for the AWS account .

    After creating the virtual MFA, use `EnableMFADevice <https://docs.aws.amazon.com/IAM/latest/APIReference/API_EnableMFADevice.html>`_ to attach the MFA device to an IAM user. For more information about creating and working with virtual MFA devices, see `Using a virtual MFA device <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_VirtualMFA.html>`_ in the *IAM User Guide* .

    For information about the maximum number of MFA devices you can create, see `IAM and AWS STS quotas <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html>`_ in the *IAM User Guide* .
    .. epigraph::

       The seed information contained in the QR code and the Base32 string should be treated like any other secret access information. In other words, protect the seed information as you would your AWS access keys or your passwords. After you provision your virtual device, you should ensure that the information is destroyed following secure procedures.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-virtualmfadevice.html
    :cloudformationResource: AWS::IAM::VirtualMFADevice
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iam as iam
        
        cfn_virtual_mFADevice = iam.CfnVirtualMFADevice(self, "MyCfnVirtualMFADevice",
            users=["users"],
        
            # the properties below are optional
            path="path",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            virtual_mfa_device_name="virtualMfaDeviceName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        users: typing.Sequence[builtins.str],
        path: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        virtual_mfa_device_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param users: The IAM user associated with this virtual MFA device.
        :param path: The path for the virtual MFA device. For more information about paths, see `IAM identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`_ in the *IAM User Guide* . This parameter is optional. If it is not included, it defaults to a slash (/). This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! ( ``\\u0021`` ) through the DEL character ( ``\\u007F`` ), including most punctuation characters, digits, and upper and lowercased letters.
        :param tags: A list of tags that you want to attach to the new IAM virtual MFA device. Each tag consists of a key name and an associated value. For more information about tagging, see `Tagging IAM resources <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`_ in the *IAM User Guide* . .. epigraph:: If any one of the tags is invalid or if you exceed the allowed maximum number of tags, then the entire request fails and the resource is not created.
        :param virtual_mfa_device_name: The name of the virtual MFA device, which must be unique. Use with path to uniquely identify a virtual MFA device. This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e13769e4d8767c55f844c7fd4df38f85edde39c6b8cf55033fe2d0cc49399a99)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnVirtualMFADeviceProps(
            users=users,
            path=path,
            tags=tags,
            virtual_mfa_device_name=virtual_mfa_device_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50929ddeddd60b35f52c962b9e82522e8bb65a7b719ace39001073ce2996743c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__95acd7cc3c337be75e6e1344aafe2900ca56480c92605d270e827237b04933d9)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrSerialNumber")
    def attr_serial_number(self) -> builtins.str:
        '''Returns the serial number for the specified ``AWS::IAM::VirtualMFADevice`` resource.

        :cloudformationAttribute: SerialNumber
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSerialNumber"))

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
    @jsii.member(jsii_name="users")
    def users(self) -> typing.List[builtins.str]:
        '''The IAM user associated with this virtual MFA device.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "users"))

    @users.setter
    def users(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62933eb2630cbda8cd521b55437211294e28433e9f2916bffa9f4987d4a9aa8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "users", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> typing.Optional[builtins.str]:
        '''The path for the virtual MFA device.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "path"))

    @path.setter
    def path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ed4aacd2a4d70c96cd36de260e15008f2e50d943134027a7f4ea4a75e1d03c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags that you want to attach to the new IAM virtual MFA device.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cf1f893827aab77cb8d7fec4a522878bd879b2f8a49198a93c51cf414124229)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="virtualMfaDeviceName")
    def virtual_mfa_device_name(self) -> typing.Optional[builtins.str]:
        '''The name of the virtual MFA device, which must be unique.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualMfaDeviceName"))

    @virtual_mfa_device_name.setter
    def virtual_mfa_device_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5456135f25b9d08fb97dae8235054f6111c0d6ff6cb6ca028c6c552d38b10cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualMfaDeviceName", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.CfnVirtualMFADeviceProps",
    jsii_struct_bases=[],
    name_mapping={
        "users": "users",
        "path": "path",
        "tags": "tags",
        "virtual_mfa_device_name": "virtualMfaDeviceName",
    },
)
class CfnVirtualMFADeviceProps:
    def __init__(
        self,
        *,
        users: typing.Sequence[builtins.str],
        path: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        virtual_mfa_device_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnVirtualMFADevice``.

        :param users: The IAM user associated with this virtual MFA device.
        :param path: The path for the virtual MFA device. For more information about paths, see `IAM identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`_ in the *IAM User Guide* . This parameter is optional. If it is not included, it defaults to a slash (/). This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! ( ``\\u0021`` ) through the DEL character ( ``\\u007F`` ), including most punctuation characters, digits, and upper and lowercased letters.
        :param tags: A list of tags that you want to attach to the new IAM virtual MFA device. Each tag consists of a key name and an associated value. For more information about tagging, see `Tagging IAM resources <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`_ in the *IAM User Guide* . .. epigraph:: If any one of the tags is invalid or if you exceed the allowed maximum number of tags, then the entire request fails and the resource is not created.
        :param virtual_mfa_device_name: The name of the virtual MFA device, which must be unique. Use with path to uniquely identify a virtual MFA device. This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-virtualmfadevice.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            
            cfn_virtual_mFADevice_props = iam.CfnVirtualMFADeviceProps(
                users=["users"],
            
                # the properties below are optional
                path="path",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                virtual_mfa_device_name="virtualMfaDeviceName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5ed743528ff356ce758fcb44914dce08240fea9458cd411d40223e93fcbbd55)
            check_type(argname="argument users", value=users, expected_type=type_hints["users"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument virtual_mfa_device_name", value=virtual_mfa_device_name, expected_type=type_hints["virtual_mfa_device_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "users": users,
        }
        if path is not None:
            self._values["path"] = path
        if tags is not None:
            self._values["tags"] = tags
        if virtual_mfa_device_name is not None:
            self._values["virtual_mfa_device_name"] = virtual_mfa_device_name

    @builtins.property
    def users(self) -> typing.List[builtins.str]:
        '''The IAM user associated with this virtual MFA device.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-virtualmfadevice.html#cfn-iam-virtualmfadevice-users
        '''
        result = self._values.get("users")
        assert result is not None, "Required property 'users' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''The path for the virtual MFA device.

        For more information about paths, see `IAM identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`_ in the *IAM User Guide* .

        This parameter is optional. If it is not included, it defaults to a slash (/).

        This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! ( ``\\u0021`` ) through the DEL character ( ``\\u007F`` ), including most punctuation characters, digits, and upper and lowercased letters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-virtualmfadevice.html#cfn-iam-virtualmfadevice-path
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags that you want to attach to the new IAM virtual MFA device.

        Each tag consists of a key name and an associated value. For more information about tagging, see `Tagging IAM resources <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`_ in the *IAM User Guide* .
        .. epigraph::

           If any one of the tags is invalid or if you exceed the allowed maximum number of tags, then the entire request fails and the resource is not created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-virtualmfadevice.html#cfn-iam-virtualmfadevice-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def virtual_mfa_device_name(self) -> typing.Optional[builtins.str]:
        '''The name of the virtual MFA device, which must be unique.

        Use with path to uniquely identify a virtual MFA device.

        This parameter allows (through its `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-virtualmfadevice.html#cfn-iam-virtualmfadevice-virtualmfadevicename
        '''
        result = self._values.get("virtual_mfa_device_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVirtualMFADeviceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.CommonGrantOptions",
    jsii_struct_bases=[],
    name_mapping={
        "actions": "actions",
        "grantee": "grantee",
        "resource_arns": "resourceArns",
        "conditions": "conditions",
    },
)
class CommonGrantOptions:
    def __init__(
        self,
        *,
        actions: typing.Sequence[builtins.str],
        grantee: "IGrantable",
        resource_arns: typing.Sequence[builtins.str],
        conditions: typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Basic options for a grant operation.

        :param actions: The actions to grant.
        :param grantee: The principal to grant to. Default: if principal is undefined, no work is done.
        :param resource_arns: The resource ARNs to grant to.
        :param conditions: Any conditions to attach to the grant. Default: - No conditions

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            
            # conditions: Any
            # grantable: iam.IGrantable
            
            common_grant_options = iam.CommonGrantOptions(
                actions=["actions"],
                grantee=grantable,
                resource_arns=["resourceArns"],
            
                # the properties below are optional
                conditions={
                    "conditions_key": {
                        "conditions_key": conditions
                    }
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53036310adac5dd1bbf375726f6d4951d790e671d970614b44aa288195097a24)
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument resource_arns", value=resource_arns, expected_type=type_hints["resource_arns"])
            check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "actions": actions,
            "grantee": grantee,
            "resource_arns": resource_arns,
        }
        if conditions is not None:
            self._values["conditions"] = conditions

    @builtins.property
    def actions(self) -> typing.List[builtins.str]:
        '''The actions to grant.'''
        result = self._values.get("actions")
        assert result is not None, "Required property 'actions' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def grantee(self) -> "IGrantable":
        '''The principal to grant to.

        :default: if principal is undefined, no work is done.
        '''
        result = self._values.get("grantee")
        assert result is not None, "Required property 'grantee' is missing"
        return typing.cast("IGrantable", result)

    @builtins.property
    def resource_arns(self) -> typing.List[builtins.str]:
        '''The resource ARNs to grant to.'''
        result = self._values.get("resource_arns")
        assert result is not None, "Required property 'resource_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def conditions(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]]:
        '''Any conditions to attach to the grant.

        :default: - No conditions
        '''
        result = self._values.get("conditions")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CommonGrantOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComparablePrincipal(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.ComparablePrincipal",
):
    '''Helper class for working with ``IComparablePrincipal``s.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iam as iam
        
        comparable_principal = iam.ComparablePrincipal()
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="dedupeStringFor")
    @builtins.classmethod
    def dedupe_string_for(cls, x: "IPrincipal") -> typing.Optional[builtins.str]:
        '''Return the dedupeString of the given principal, if available.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e05d9e2d20ba422910a4ba52987ae06003b821061dcd5fb66ea08234a5add520)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(typing.Optional[builtins.str], jsii.sinvoke(cls, "dedupeStringFor", [x]))

    @jsii.member(jsii_name="isComparablePrincipal")
    @builtins.classmethod
    def is_comparable_principal(cls, x: "IPrincipal") -> builtins.bool:
        '''Whether or not the given principal is a comparable principal.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed18f5361eb860ae94547e85443180c995c1de1d28ef2ccda9f79c39983c1afb)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isComparablePrincipal", [x]))


@jsii.implements(_constructs_77d1e7e8.IDependable)
class CompositeDependable(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.CompositeDependable",
):
    '''Composite dependable.

    Not as simple as eagerly getting the dependency roots from the
    inner dependables, as they may be mutable so we need to defer
    the query.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iam as iam
        import constructs as constructs
        
        # dependable: constructs.IDependable
        
        composite_dependable = iam.CompositeDependable(dependable)
    '''

    def __init__(self, *dependables: _constructs_77d1e7e8.IDependable) -> None:
        '''
        :param dependables: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11451a597e4f52017e14ede781ef9eadbc8d06d5380bf40a47e9667cf431ab84)
            check_type(argname="argument dependables", value=dependables, expected_type=typing.Tuple[type_hints["dependables"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        jsii.create(self.__class__, self, [*dependables])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.CustomizeRolesOptions",
    jsii_struct_bases=[],
    name_mapping={
        "prevent_synthesis": "preventSynthesis",
        "use_precreated_roles": "usePrecreatedRoles",
    },
)
class CustomizeRolesOptions:
    def __init__(
        self,
        *,
        prevent_synthesis: typing.Optional[builtins.bool] = None,
        use_precreated_roles: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Options for customizing IAM role creation.

        :param prevent_synthesis: Whether or not to synthesize the resource into the CFN template. Set this to ``false`` if you still want to create the resources *and* you also want to create the policy report. Default: true
        :param use_precreated_roles: A list of precreated IAM roles to substitute for roles that CDK is creating. The constructPath can be either a relative or absolute path from the scope that ``customizeRoles`` is used on to the role being created. Default: - there are no precreated roles. Synthesis will fail if ``preventSynthesis=true``

        :exampleMetadata: infused

        Example::

            # app: App
            
            stack = Stack(app, "MyStack")
            iam.Role.customize_roles(self,
                use_precreated_roles={
                    "MyStack/MyLambda/ServiceRole": "my-role-name"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1882c00172b4072d4822b976aed7e86da105b2fb611d32539f72c644071f16d4)
            check_type(argname="argument prevent_synthesis", value=prevent_synthesis, expected_type=type_hints["prevent_synthesis"])
            check_type(argname="argument use_precreated_roles", value=use_precreated_roles, expected_type=type_hints["use_precreated_roles"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if prevent_synthesis is not None:
            self._values["prevent_synthesis"] = prevent_synthesis
        if use_precreated_roles is not None:
            self._values["use_precreated_roles"] = use_precreated_roles

    @builtins.property
    def prevent_synthesis(self) -> typing.Optional[builtins.bool]:
        '''Whether or not to synthesize the resource into the CFN template.

        Set this to ``false`` if you still want to create the resources *and*
        you also want to create the policy report.

        :default: true
        '''
        result = self._values.get("prevent_synthesis")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def use_precreated_roles(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of precreated IAM roles to substitute for roles that CDK is creating.

        The constructPath can be either a relative or absolute path
        from the scope that ``customizeRoles`` is used on to the role being created.

        :default: - there are no precreated roles. Synthesis will fail if ``preventSynthesis=true``

        Example::

            # app: App
            
            
            stack = Stack(app, "MyStack")
            iam.Role(stack, "MyRole",
                assumed_by=iam.AccountPrincipal("1111111111")
            )
            
            iam.Role.customize_roles(stack,
                use_precreated_roles={
                    # absolute path
                    "MyStack/MyRole": "my-precreated-role-name",
                    # or relative path from `stack`
                    "MyRole": "my-precreated-role"
                }
            )
        '''
        result = self._values.get("use_precreated_roles")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomizeRolesOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_iam.Effect")
class Effect(enum.Enum):
    '''The Effect element of an IAM policy.

    :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_effect.html
    :exampleMetadata: infused

    Example::

        # books: apigateway.Resource
        # iam_user: iam.User
        
        
        get_books = books.add_method("GET", apigateway.HttpIntegration("http://amazon.com"),
            authorization_type=apigateway.AuthorizationType.IAM
        )
        
        iam_user.attach_inline_policy(iam.Policy(self, "AllowBooks",
            statements=[
                iam.PolicyStatement(
                    actions=["execute-api:Invoke"],
                    effect=iam.Effect.ALLOW,
                    resources=[get_books.method_arn]
                )
            ]
        ))
    '''

    ALLOW = "ALLOW"
    '''Allows access to a resource in an IAM policy statement.

    By default, access to resources are denied.
    '''
    DENY = "DENY"
    '''Explicitly deny access to a resource.

    By default, all requests are denied implicitly.

    :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html
    '''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.FromRoleArnOptions",
    jsii_struct_bases=[],
    name_mapping={
        "add_grants_to_resources": "addGrantsToResources",
        "default_policy_name": "defaultPolicyName",
        "mutable": "mutable",
    },
)
class FromRoleArnOptions:
    def __init__(
        self,
        *,
        add_grants_to_resources: typing.Optional[builtins.bool] = None,
        default_policy_name: typing.Optional[builtins.str] = None,
        mutable: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options allowing customizing the behavior of ``Role.fromRoleArn``.

        :param add_grants_to_resources: For immutable roles: add grants to resources instead of dropping them. If this is ``false`` or not specified, grant permissions added to this role are ignored. It is your own responsibility to make sure the role has the required permissions. If this is ``true``, any grant permissions will be added to the resource instead. Default: false
        :param default_policy_name: Any policies created by this role will use this value as their ID, if specified. Specify this if importing the same role in multiple stacks, and granting it different permissions in at least two stacks. If this is not specified (or if the same name is specified in more than one stack), a CloudFormation issue will result in the policy created in whichever stack is deployed last overwriting the policies created by the others. Default: 'Policy'
        :param mutable: Whether the imported role can be modified by attaching policy resources to it. Default: true

        :exampleMetadata: infused

        Example::

            role = iam.Role.from_role_arn(self, "Role", "arn:aws:iam::123456789012:role/MyExistingRole",
                # Set 'mutable' to 'false' to use the role as-is and prevent adding new
                # policies to it. The default is 'true', which means the role may be
                # modified as part of the deployment.
                mutable=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f2caa0021d06fd2643ae1baf77362146ac3d8099ebadae2a932738c2a2a8792)
            check_type(argname="argument add_grants_to_resources", value=add_grants_to_resources, expected_type=type_hints["add_grants_to_resources"])
            check_type(argname="argument default_policy_name", value=default_policy_name, expected_type=type_hints["default_policy_name"])
            check_type(argname="argument mutable", value=mutable, expected_type=type_hints["mutable"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if add_grants_to_resources is not None:
            self._values["add_grants_to_resources"] = add_grants_to_resources
        if default_policy_name is not None:
            self._values["default_policy_name"] = default_policy_name
        if mutable is not None:
            self._values["mutable"] = mutable

    @builtins.property
    def add_grants_to_resources(self) -> typing.Optional[builtins.bool]:
        '''For immutable roles: add grants to resources instead of dropping them.

        If this is ``false`` or not specified, grant permissions added to this role are ignored.
        It is your own responsibility to make sure the role has the required permissions.

        If this is ``true``, any grant permissions will be added to the resource instead.

        :default: false
        '''
        result = self._values.get("add_grants_to_resources")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def default_policy_name(self) -> typing.Optional[builtins.str]:
        '''Any policies created by this role will use this value as their ID, if specified.

        Specify this if importing the same role in multiple stacks, and granting it
        different permissions in at least two stacks. If this is not specified
        (or if the same name is specified in more than one stack),
        a CloudFormation issue will result in the policy created in whichever stack
        is deployed last overwriting the policies created by the others.

        :default: 'Policy'
        '''
        result = self._values.get("default_policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mutable(self) -> typing.Optional[builtins.bool]:
        '''Whether the imported role can be modified by attaching policy resources to it.

        :default: true
        '''
        result = self._values.get("mutable")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FromRoleArnOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.FromRoleNameOptions",
    jsii_struct_bases=[FromRoleArnOptions],
    name_mapping={
        "add_grants_to_resources": "addGrantsToResources",
        "default_policy_name": "defaultPolicyName",
        "mutable": "mutable",
    },
)
class FromRoleNameOptions(FromRoleArnOptions):
    def __init__(
        self,
        *,
        add_grants_to_resources: typing.Optional[builtins.bool] = None,
        default_policy_name: typing.Optional[builtins.str] = None,
        mutable: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options allowing customizing the behavior of ``Role.fromRoleName``.

        :param add_grants_to_resources: For immutable roles: add grants to resources instead of dropping them. If this is ``false`` or not specified, grant permissions added to this role are ignored. It is your own responsibility to make sure the role has the required permissions. If this is ``true``, any grant permissions will be added to the resource instead. Default: false
        :param default_policy_name: Any policies created by this role will use this value as their ID, if specified. Specify this if importing the same role in multiple stacks, and granting it different permissions in at least two stacks. If this is not specified (or if the same name is specified in more than one stack), a CloudFormation issue will result in the policy created in whichever stack is deployed last overwriting the policies created by the others. Default: 'Policy'
        :param mutable: Whether the imported role can be modified by attaching policy resources to it. Default: true

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            
            from_role_name_options = iam.FromRoleNameOptions(
                add_grants_to_resources=False,
                default_policy_name="defaultPolicyName",
                mutable=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8d60e61efe2fd0be1638c155ae6ceb97e4047a546e091855a6300b0267cc06a)
            check_type(argname="argument add_grants_to_resources", value=add_grants_to_resources, expected_type=type_hints["add_grants_to_resources"])
            check_type(argname="argument default_policy_name", value=default_policy_name, expected_type=type_hints["default_policy_name"])
            check_type(argname="argument mutable", value=mutable, expected_type=type_hints["mutable"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if add_grants_to_resources is not None:
            self._values["add_grants_to_resources"] = add_grants_to_resources
        if default_policy_name is not None:
            self._values["default_policy_name"] = default_policy_name
        if mutable is not None:
            self._values["mutable"] = mutable

    @builtins.property
    def add_grants_to_resources(self) -> typing.Optional[builtins.bool]:
        '''For immutable roles: add grants to resources instead of dropping them.

        If this is ``false`` or not specified, grant permissions added to this role are ignored.
        It is your own responsibility to make sure the role has the required permissions.

        If this is ``true``, any grant permissions will be added to the resource instead.

        :default: false
        '''
        result = self._values.get("add_grants_to_resources")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def default_policy_name(self) -> typing.Optional[builtins.str]:
        '''Any policies created by this role will use this value as their ID, if specified.

        Specify this if importing the same role in multiple stacks, and granting it
        different permissions in at least two stacks. If this is not specified
        (or if the same name is specified in more than one stack),
        a CloudFormation issue will result in the policy created in whichever stack
        is deployed last overwriting the policies created by the others.

        :default: 'Policy'
        '''
        result = self._values.get("default_policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mutable(self) -> typing.Optional[builtins.bool]:
        '''Whether the imported role can be modified by attaching policy resources to it.

        :default: true
        '''
        result = self._values.get("mutable")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FromRoleNameOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_constructs_77d1e7e8.IDependable)
class Grant(metaclass=jsii.JSIIMeta, jsii_type="aws-cdk-lib.aws_iam.Grant"):
    '''Result of a grant() operation.

    This class is not instantiable by consumers on purpose, so that they will be
    required to call the Grant factory functions.

    :exampleMetadata: infused

    Example::

        # instance: ec2.Instance
        # volume: ec2.Volume
        
        
        attach_grant = volume.grant_attach_volume_by_resource_tag(instance.grant_principal, [instance])
        detach_grant = volume.grant_detach_volume_by_resource_tag(instance.grant_principal, [instance])
    '''

    @jsii.member(jsii_name="addToPrincipal")
    @builtins.classmethod
    def add_to_principal(
        cls,
        *,
        scope: typing.Optional[_constructs_77d1e7e8.IConstruct] = None,
        actions: typing.Sequence[builtins.str],
        grantee: "IGrantable",
        resource_arns: typing.Sequence[builtins.str],
        conditions: typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]] = None,
    ) -> "Grant":
        '''Try to grant the given permissions to the given principal.

        Absence of a principal leads to a warning, but failing to add
        the permissions to a present principal is not an error.

        :param scope: Construct to report warnings on in case grant could not be registered. Default: - the construct in which this construct is defined
        :param actions: The actions to grant.
        :param grantee: The principal to grant to. Default: if principal is undefined, no work is done.
        :param resource_arns: The resource ARNs to grant to.
        :param conditions: Any conditions to attach to the grant. Default: - No conditions
        '''
        options = GrantOnPrincipalOptions(
            scope=scope,
            actions=actions,
            grantee=grantee,
            resource_arns=resource_arns,
            conditions=conditions,
        )

        return typing.cast("Grant", jsii.sinvoke(cls, "addToPrincipal", [options]))

    @jsii.member(jsii_name="addToPrincipalAndResource")
    @builtins.classmethod
    def add_to_principal_and_resource(
        cls,
        *,
        resource: "IResourceWithPolicy",
        resource_policy_principal: typing.Optional["IPrincipal"] = None,
        resource_self_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        actions: typing.Sequence[builtins.str],
        grantee: "IGrantable",
        resource_arns: typing.Sequence[builtins.str],
        conditions: typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]] = None,
    ) -> "Grant":
        '''Add a grant both on the principal and on the resource.

        As long as any principal is given, granting on the principal may fail (in
        case of a non-identity principal), but granting on the resource will
        never fail.

        Statement will be the resource statement.

        :param resource: The resource with a resource policy. The statement will always be added to the resource policy.
        :param resource_policy_principal: The principal to use in the statement for the resource policy. Default: - the principal of the grantee will be used
        :param resource_self_arns: When referring to the resource in a resource policy, use this as ARN. (Depending on the resource type, this needs to be '*' in a resource policy). Default: Same as regular resource ARNs
        :param actions: The actions to grant.
        :param grantee: The principal to grant to. Default: if principal is undefined, no work is done.
        :param resource_arns: The resource ARNs to grant to.
        :param conditions: Any conditions to attach to the grant. Default: - No conditions
        '''
        options = GrantOnPrincipalAndResourceOptions(
            resource=resource,
            resource_policy_principal=resource_policy_principal,
            resource_self_arns=resource_self_arns,
            actions=actions,
            grantee=grantee,
            resource_arns=resource_arns,
            conditions=conditions,
        )

        return typing.cast("Grant", jsii.sinvoke(cls, "addToPrincipalAndResource", [options]))

    @jsii.member(jsii_name="addToPrincipalOrResource")
    @builtins.classmethod
    def add_to_principal_or_resource(
        cls,
        *,
        resource: "IResourceWithPolicy",
        resource_self_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        actions: typing.Sequence[builtins.str],
        grantee: "IGrantable",
        resource_arns: typing.Sequence[builtins.str],
        conditions: typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]] = None,
    ) -> "Grant":
        '''Grant the given permissions to the principal.

        The permissions will be added to the principal policy primarily, falling
        back to the resource policy if necessary. The permissions must be granted
        somewhere.

        - Trying to grant permissions to a principal that does not admit adding to
          the principal policy while not providing a resource with a resource policy
          is an error.
        - Trying to grant permissions to an absent principal (possible in the
          case of imported resources) leads to a warning being added to the
          resource construct.

        :param resource: The resource with a resource policy. The statement will be added to the resource policy if it couldn't be added to the principal policy.
        :param resource_self_arns: When referring to the resource in a resource policy, use this as ARN. (Depending on the resource type, this needs to be '*' in a resource policy). Default: Same as regular resource ARNs
        :param actions: The actions to grant.
        :param grantee: The principal to grant to. Default: if principal is undefined, no work is done.
        :param resource_arns: The resource ARNs to grant to.
        :param conditions: Any conditions to attach to the grant. Default: - No conditions
        '''
        options = GrantWithResourceOptions(
            resource=resource,
            resource_self_arns=resource_self_arns,
            actions=actions,
            grantee=grantee,
            resource_arns=resource_arns,
            conditions=conditions,
        )

        return typing.cast("Grant", jsii.sinvoke(cls, "addToPrincipalOrResource", [options]))

    @jsii.member(jsii_name="drop")
    @builtins.classmethod
    def drop(cls, grantee: "IGrantable", _intent: builtins.str) -> "Grant":
        '''Returns a "no-op" ``Grant`` object which represents a "dropped grant".

        This can be used for e.g. imported resources where you may not be able to modify
        the resource's policy or some underlying policy which you don't know about.

        :param grantee: The intended grantee.
        :param _intent: The user's intent (will be ignored at the moment).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ae645e99a39c5eb8dbdb0a66396e18ca51afd239a00e07d929768a9a716ccce)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument _intent", value=_intent, expected_type=type_hints["_intent"])
        return typing.cast("Grant", jsii.sinvoke(cls, "drop", [grantee, _intent]))

    @jsii.member(jsii_name="applyBefore")
    def apply_before(self, *constructs: _constructs_77d1e7e8.IConstruct) -> None:
        '''Make sure this grant is applied before the given constructs are deployed.

        The same as construct.node.addDependency(grant), but slightly nicer to read.

        :param constructs: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6318dcb5bbc942b36daa3ec8cb25267c59a79903d43165acc5d48f60d4ef308)
            check_type(argname="argument constructs", value=constructs, expected_type=typing.Tuple[type_hints["constructs"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "applyBefore", [*constructs]))

    @jsii.member(jsii_name="assertSuccess")
    def assert_success(self) -> None:
        '''Throw an error if this grant wasn't successful.'''
        return typing.cast(None, jsii.invoke(self, "assertSuccess", []))

    @jsii.member(jsii_name="combine")
    def combine(self, rhs: "Grant") -> "Grant":
        '''Combine two grants into a new one.

        :param rhs: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18a4ff4a989416437955a50d12b650943c445c1bd75cbc2f47d19390462e1842)
            check_type(argname="argument rhs", value=rhs, expected_type=type_hints["rhs"])
        return typing.cast("Grant", jsii.invoke(self, "combine", [rhs]))

    @builtins.property
    @jsii.member(jsii_name="principalStatements")
    def principal_statements(self) -> typing.List["PolicyStatement"]:
        '''The statements that were added to the principal's policy.'''
        return typing.cast(typing.List["PolicyStatement"], jsii.get(self, "principalStatements"))

    @builtins.property
    @jsii.member(jsii_name="resourceStatements")
    def resource_statements(self) -> typing.List["PolicyStatement"]:
        '''The statements that were added to the principal's policy.'''
        return typing.cast(typing.List["PolicyStatement"], jsii.get(self, "resourceStatements"))

    @builtins.property
    @jsii.member(jsii_name="success")
    def success(self) -> builtins.bool:
        '''Whether the grant operation was successful.'''
        return typing.cast(builtins.bool, jsii.get(self, "success"))

    @builtins.property
    @jsii.member(jsii_name="principalStatement")
    def principal_statement(self) -> typing.Optional["PolicyStatement"]:
        '''(deprecated) The statement that was added to the principal's policy.

        :deprecated: Use ``principalStatements`` instead

        :stability: deprecated
        '''
        return typing.cast(typing.Optional["PolicyStatement"], jsii.get(self, "principalStatement"))

    @builtins.property
    @jsii.member(jsii_name="resourceStatement")
    def resource_statement(self) -> typing.Optional["PolicyStatement"]:
        '''(deprecated) The statement that was added to the resource policy.

        :deprecated: Use ``resourceStatements`` instead

        :stability: deprecated
        '''
        return typing.cast(typing.Optional["PolicyStatement"], jsii.get(self, "resourceStatement"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.GrantOnPrincipalAndResourceOptions",
    jsii_struct_bases=[CommonGrantOptions],
    name_mapping={
        "actions": "actions",
        "grantee": "grantee",
        "resource_arns": "resourceArns",
        "conditions": "conditions",
        "resource": "resource",
        "resource_policy_principal": "resourcePolicyPrincipal",
        "resource_self_arns": "resourceSelfArns",
    },
)
class GrantOnPrincipalAndResourceOptions(CommonGrantOptions):
    def __init__(
        self,
        *,
        actions: typing.Sequence[builtins.str],
        grantee: "IGrantable",
        resource_arns: typing.Sequence[builtins.str],
        conditions: typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]] = None,
        resource: "IResourceWithPolicy",
        resource_policy_principal: typing.Optional["IPrincipal"] = None,
        resource_self_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Options for a grant operation to both identity and resource.

        :param actions: The actions to grant.
        :param grantee: The principal to grant to. Default: if principal is undefined, no work is done.
        :param resource_arns: The resource ARNs to grant to.
        :param conditions: Any conditions to attach to the grant. Default: - No conditions
        :param resource: The resource with a resource policy. The statement will always be added to the resource policy.
        :param resource_policy_principal: The principal to use in the statement for the resource policy. Default: - the principal of the grantee will be used
        :param resource_self_arns: When referring to the resource in a resource policy, use this as ARN. (Depending on the resource type, this needs to be '*' in a resource policy). Default: Same as regular resource ARNs

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            
            # conditions: Any
            # grantable: iam.IGrantable
            # principal: iam.IPrincipal
            # resource_with_policy: iam.IResourceWithPolicy
            
            grant_on_principal_and_resource_options = iam.GrantOnPrincipalAndResourceOptions(
                actions=["actions"],
                grantee=grantable,
                resource=resource_with_policy,
                resource_arns=["resourceArns"],
            
                # the properties below are optional
                conditions={
                    "conditions_key": {
                        "conditions_key": conditions
                    }
                },
                resource_policy_principal=principal,
                resource_self_arns=["resourceSelfArns"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a60e5877e638d22c44d2e72be768df7f85caf47bec9ab2e6b2adcce826a6aae0)
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument resource_arns", value=resource_arns, expected_type=type_hints["resource_arns"])
            check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
            check_type(argname="argument resource_policy_principal", value=resource_policy_principal, expected_type=type_hints["resource_policy_principal"])
            check_type(argname="argument resource_self_arns", value=resource_self_arns, expected_type=type_hints["resource_self_arns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "actions": actions,
            "grantee": grantee,
            "resource_arns": resource_arns,
            "resource": resource,
        }
        if conditions is not None:
            self._values["conditions"] = conditions
        if resource_policy_principal is not None:
            self._values["resource_policy_principal"] = resource_policy_principal
        if resource_self_arns is not None:
            self._values["resource_self_arns"] = resource_self_arns

    @builtins.property
    def actions(self) -> typing.List[builtins.str]:
        '''The actions to grant.'''
        result = self._values.get("actions")
        assert result is not None, "Required property 'actions' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def grantee(self) -> "IGrantable":
        '''The principal to grant to.

        :default: if principal is undefined, no work is done.
        '''
        result = self._values.get("grantee")
        assert result is not None, "Required property 'grantee' is missing"
        return typing.cast("IGrantable", result)

    @builtins.property
    def resource_arns(self) -> typing.List[builtins.str]:
        '''The resource ARNs to grant to.'''
        result = self._values.get("resource_arns")
        assert result is not None, "Required property 'resource_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def conditions(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]]:
        '''Any conditions to attach to the grant.

        :default: - No conditions
        '''
        result = self._values.get("conditions")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]], result)

    @builtins.property
    def resource(self) -> "IResourceWithPolicy":
        '''The resource with a resource policy.

        The statement will always be added to the resource policy.
        '''
        result = self._values.get("resource")
        assert result is not None, "Required property 'resource' is missing"
        return typing.cast("IResourceWithPolicy", result)

    @builtins.property
    def resource_policy_principal(self) -> typing.Optional["IPrincipal"]:
        '''The principal to use in the statement for the resource policy.

        :default: - the principal of the grantee will be used
        '''
        result = self._values.get("resource_policy_principal")
        return typing.cast(typing.Optional["IPrincipal"], result)

    @builtins.property
    def resource_self_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''When referring to the resource in a resource policy, use this as ARN.

        (Depending on the resource type, this needs to be '*' in a resource policy).

        :default: Same as regular resource ARNs
        '''
        result = self._values.get("resource_self_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrantOnPrincipalAndResourceOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.GrantOnPrincipalOptions",
    jsii_struct_bases=[CommonGrantOptions],
    name_mapping={
        "actions": "actions",
        "grantee": "grantee",
        "resource_arns": "resourceArns",
        "conditions": "conditions",
        "scope": "scope",
    },
)
class GrantOnPrincipalOptions(CommonGrantOptions):
    def __init__(
        self,
        *,
        actions: typing.Sequence[builtins.str],
        grantee: "IGrantable",
        resource_arns: typing.Sequence[builtins.str],
        conditions: typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]] = None,
        scope: typing.Optional[_constructs_77d1e7e8.IConstruct] = None,
    ) -> None:
        '''Options for a grant operation that only applies to principals.

        :param actions: The actions to grant.
        :param grantee: The principal to grant to. Default: if principal is undefined, no work is done.
        :param resource_arns: The resource ARNs to grant to.
        :param conditions: Any conditions to attach to the grant. Default: - No conditions
        :param scope: Construct to report warnings on in case grant could not be registered. Default: - the construct in which this construct is defined

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            import constructs as constructs
            
            # conditions: Any
            # construct: constructs.Construct
            # grantable: iam.IGrantable
            
            grant_on_principal_options = iam.GrantOnPrincipalOptions(
                actions=["actions"],
                grantee=grantable,
                resource_arns=["resourceArns"],
            
                # the properties below are optional
                conditions={
                    "conditions_key": {
                        "conditions_key": conditions
                    }
                },
                scope=construct
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e1d68e4e0e483e95fcca600944e0e8047f1278ed2d44d2d239ae6584b491dcc)
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument resource_arns", value=resource_arns, expected_type=type_hints["resource_arns"])
            check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "actions": actions,
            "grantee": grantee,
            "resource_arns": resource_arns,
        }
        if conditions is not None:
            self._values["conditions"] = conditions
        if scope is not None:
            self._values["scope"] = scope

    @builtins.property
    def actions(self) -> typing.List[builtins.str]:
        '''The actions to grant.'''
        result = self._values.get("actions")
        assert result is not None, "Required property 'actions' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def grantee(self) -> "IGrantable":
        '''The principal to grant to.

        :default: if principal is undefined, no work is done.
        '''
        result = self._values.get("grantee")
        assert result is not None, "Required property 'grantee' is missing"
        return typing.cast("IGrantable", result)

    @builtins.property
    def resource_arns(self) -> typing.List[builtins.str]:
        '''The resource ARNs to grant to.'''
        result = self._values.get("resource_arns")
        assert result is not None, "Required property 'resource_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def conditions(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]]:
        '''Any conditions to attach to the grant.

        :default: - No conditions
        '''
        result = self._values.get("conditions")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]], result)

    @builtins.property
    def scope(self) -> typing.Optional[_constructs_77d1e7e8.IConstruct]:
        '''Construct to report warnings on in case grant could not be registered.

        :default: - the construct in which this construct is defined
        '''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[_constructs_77d1e7e8.IConstruct], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrantOnPrincipalOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.GrantWithResourceOptions",
    jsii_struct_bases=[CommonGrantOptions],
    name_mapping={
        "actions": "actions",
        "grantee": "grantee",
        "resource_arns": "resourceArns",
        "conditions": "conditions",
        "resource": "resource",
        "resource_self_arns": "resourceSelfArns",
    },
)
class GrantWithResourceOptions(CommonGrantOptions):
    def __init__(
        self,
        *,
        actions: typing.Sequence[builtins.str],
        grantee: "IGrantable",
        resource_arns: typing.Sequence[builtins.str],
        conditions: typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]] = None,
        resource: "IResourceWithPolicy",
        resource_self_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Options for a grant operation.

        :param actions: The actions to grant.
        :param grantee: The principal to grant to. Default: if principal is undefined, no work is done.
        :param resource_arns: The resource ARNs to grant to.
        :param conditions: Any conditions to attach to the grant. Default: - No conditions
        :param resource: The resource with a resource policy. The statement will be added to the resource policy if it couldn't be added to the principal policy.
        :param resource_self_arns: When referring to the resource in a resource policy, use this as ARN. (Depending on the resource type, this needs to be '*' in a resource policy). Default: Same as regular resource ARNs

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            
            # conditions: Any
            # grantable: iam.IGrantable
            # resource_with_policy: iam.IResourceWithPolicy
            
            grant_with_resource_options = iam.GrantWithResourceOptions(
                actions=["actions"],
                grantee=grantable,
                resource=resource_with_policy,
                resource_arns=["resourceArns"],
            
                # the properties below are optional
                conditions={
                    "conditions_key": {
                        "conditions_key": conditions
                    }
                },
                resource_self_arns=["resourceSelfArns"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d76f68f1d67dcad526c87768d88423a4092a0ef3127be7cb53462044851e0ea2)
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument resource_arns", value=resource_arns, expected_type=type_hints["resource_arns"])
            check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
            check_type(argname="argument resource_self_arns", value=resource_self_arns, expected_type=type_hints["resource_self_arns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "actions": actions,
            "grantee": grantee,
            "resource_arns": resource_arns,
            "resource": resource,
        }
        if conditions is not None:
            self._values["conditions"] = conditions
        if resource_self_arns is not None:
            self._values["resource_self_arns"] = resource_self_arns

    @builtins.property
    def actions(self) -> typing.List[builtins.str]:
        '''The actions to grant.'''
        result = self._values.get("actions")
        assert result is not None, "Required property 'actions' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def grantee(self) -> "IGrantable":
        '''The principal to grant to.

        :default: if principal is undefined, no work is done.
        '''
        result = self._values.get("grantee")
        assert result is not None, "Required property 'grantee' is missing"
        return typing.cast("IGrantable", result)

    @builtins.property
    def resource_arns(self) -> typing.List[builtins.str]:
        '''The resource ARNs to grant to.'''
        result = self._values.get("resource_arns")
        assert result is not None, "Required property 'resource_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def conditions(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]]:
        '''Any conditions to attach to the grant.

        :default: - No conditions
        '''
        result = self._values.get("conditions")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]], result)

    @builtins.property
    def resource(self) -> "IResourceWithPolicy":
        '''The resource with a resource policy.

        The statement will be added to the resource policy if it couldn't be
        added to the principal policy.
        '''
        result = self._values.get("resource")
        assert result is not None, "Required property 'resource' is missing"
        return typing.cast("IResourceWithPolicy", result)

    @builtins.property
    def resource_self_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''When referring to the resource in a resource policy, use this as ARN.

        (Depending on the resource type, this needs to be '*' in a resource policy).

        :default: Same as regular resource ARNs
        '''
        result = self._values.get("resource_self_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrantWithResourceOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.GroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "group_name": "groupName",
        "managed_policies": "managedPolicies",
        "path": "path",
    },
)
class GroupProps:
    def __init__(
        self,
        *,
        group_name: typing.Optional[builtins.str] = None,
        managed_policies: typing.Optional[typing.Sequence["IManagedPolicy"]] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining an IAM group.

        :param group_name: A name for the IAM group. For valid values, see the GroupName parameter for the CreateGroup action in the IAM API Reference. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the group name. If you specify a name, you must specify the CAPABILITY_NAMED_IAM value to acknowledge your template's capabilities. For more information, see Acknowledging IAM Resources in AWS CloudFormation Templates. Default: Generated by CloudFormation (recommended)
        :param managed_policies: A list of managed policies associated with this role. You can add managed policies later using ``addManagedPolicy(ManagedPolicy.fromAwsManagedPolicyName(policyName))``. Default: - No managed policies.
        :param path: The path to the group. For more information about paths, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/index.html?Using_Identifiers.html>`_ in the IAM User Guide. Default: /

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            
            # managed_policy: iam.ManagedPolicy
            
            group_props = iam.GroupProps(
                group_name="groupName",
                managed_policies=[managed_policy],
                path="path"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7889ad6c97f3c96c3ead5d27bd1231fba11aadae1700a9dcd088123609e9b9a5)
            check_type(argname="argument group_name", value=group_name, expected_type=type_hints["group_name"])
            check_type(argname="argument managed_policies", value=managed_policies, expected_type=type_hints["managed_policies"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if group_name is not None:
            self._values["group_name"] = group_name
        if managed_policies is not None:
            self._values["managed_policies"] = managed_policies
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def group_name(self) -> typing.Optional[builtins.str]:
        '''A name for the IAM group.

        For valid values, see the GroupName parameter
        for the CreateGroup action in the IAM API Reference. If you don't specify
        a name, AWS CloudFormation generates a unique physical ID and uses that
        ID for the group name.

        If you specify a name, you must specify the CAPABILITY_NAMED_IAM value to
        acknowledge your template's capabilities. For more information, see
        Acknowledging IAM Resources in AWS CloudFormation Templates.

        :default: Generated by CloudFormation (recommended)
        '''
        result = self._values.get("group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def managed_policies(self) -> typing.Optional[typing.List["IManagedPolicy"]]:
        '''A list of managed policies associated with this role.

        You can add managed policies later using
        ``addManagedPolicy(ManagedPolicy.fromAwsManagedPolicyName(policyName))``.

        :default: - No managed policies.
        '''
        result = self._values.get("managed_policies")
        return typing.cast(typing.Optional[typing.List["IManagedPolicy"]], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''The path to the group.

        For more information about paths, see `IAM
        Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/index.html?Using_Identifiers.html>`_
        in the IAM User Guide.

        :default: /
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.aws_iam.IAccessKey")
class IAccessKey(_IResource_c80c4260, typing_extensions.Protocol):
    '''Represents an IAM Access Key.

    :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html
    '''

    @builtins.property
    @jsii.member(jsii_name="accessKeyId")
    def access_key_id(self) -> builtins.str:
        '''The Access Key ID.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="secretAccessKey")
    def secret_access_key(self) -> _SecretValue_3dd0ddae:
        '''The Secret Access Key.

        :attribute: true
        '''
        ...


class _IAccessKeyProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''Represents an IAM Access Key.

    :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_iam.IAccessKey"

    @builtins.property
    @jsii.member(jsii_name="accessKeyId")
    def access_key_id(self) -> builtins.str:
        '''The Access Key ID.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "accessKeyId"))

    @builtins.property
    @jsii.member(jsii_name="secretAccessKey")
    def secret_access_key(self) -> _SecretValue_3dd0ddae:
        '''The Secret Access Key.

        :attribute: true
        '''
        return typing.cast(_SecretValue_3dd0ddae, jsii.get(self, "secretAccessKey"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAccessKey).__jsii_proxy_class__ = lambda : _IAccessKeyProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_iam.IGrantable")
class IGrantable(typing_extensions.Protocol):
    '''Any object that has an associated principal that a permission can be granted to.'''

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> "IPrincipal":
        '''The principal to grant permissions to.'''
        ...


class _IGrantableProxy:
    '''Any object that has an associated principal that a permission can be granted to.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_iam.IGrantable"

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> "IPrincipal":
        '''The principal to grant permissions to.'''
        return typing.cast("IPrincipal", jsii.get(self, "grantPrincipal"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGrantable).__jsii_proxy_class__ = lambda : _IGrantableProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_iam.IInstanceProfile")
class IInstanceProfile(_IResource_c80c4260, typing_extensions.Protocol):
    '''Represents an IAM Instance Profile.'''

    @builtins.property
    @jsii.member(jsii_name="instanceProfileArn")
    def instance_profile_arn(self) -> builtins.str:
        '''The InstanceProfile's ARN.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="instanceProfileName")
    def instance_profile_name(self) -> builtins.str:
        '''The InstanceProfile's name.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> typing.Optional["IRole"]:
        '''The role associated with the InstanceProfile.'''
        ...


class _IInstanceProfileProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''Represents an IAM Instance Profile.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_iam.IInstanceProfile"

    @builtins.property
    @jsii.member(jsii_name="instanceProfileArn")
    def instance_profile_arn(self) -> builtins.str:
        '''The InstanceProfile's ARN.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceProfileArn"))

    @builtins.property
    @jsii.member(jsii_name="instanceProfileName")
    def instance_profile_name(self) -> builtins.str:
        '''The InstanceProfile's name.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceProfileName"))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> typing.Optional["IRole"]:
        '''The role associated with the InstanceProfile.'''
        return typing.cast(typing.Optional["IRole"], jsii.get(self, "role"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInstanceProfile).__jsii_proxy_class__ = lambda : _IInstanceProfileProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_iam.IManagedPolicy")
class IManagedPolicy(typing_extensions.Protocol):
    '''A managed policy.'''

    @builtins.property
    @jsii.member(jsii_name="managedPolicyArn")
    def managed_policy_arn(self) -> builtins.str:
        '''The ARN of the managed policy.

        :attribute: true
        '''
        ...


class _IManagedPolicyProxy:
    '''A managed policy.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_iam.IManagedPolicy"

    @builtins.property
    @jsii.member(jsii_name="managedPolicyArn")
    def managed_policy_arn(self) -> builtins.str:
        '''The ARN of the managed policy.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "managedPolicyArn"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IManagedPolicy).__jsii_proxy_class__ = lambda : _IManagedPolicyProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_iam.IOpenIdConnectProvider")
class IOpenIdConnectProvider(_IResource_c80c4260, typing_extensions.Protocol):
    '''Represents an IAM OpenID Connect provider.'''

    @builtins.property
    @jsii.member(jsii_name="openIdConnectProviderArn")
    def open_id_connect_provider_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM OpenID Connect provider.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="openIdConnectProviderIssuer")
    def open_id_connect_provider_issuer(self) -> builtins.str:
        '''The issuer for OIDC Provider.'''
        ...


class _IOpenIdConnectProviderProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''Represents an IAM OpenID Connect provider.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_iam.IOpenIdConnectProvider"

    @builtins.property
    @jsii.member(jsii_name="openIdConnectProviderArn")
    def open_id_connect_provider_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM OpenID Connect provider.'''
        return typing.cast(builtins.str, jsii.get(self, "openIdConnectProviderArn"))

    @builtins.property
    @jsii.member(jsii_name="openIdConnectProviderIssuer")
    def open_id_connect_provider_issuer(self) -> builtins.str:
        '''The issuer for OIDC Provider.'''
        return typing.cast(builtins.str, jsii.get(self, "openIdConnectProviderIssuer"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOpenIdConnectProvider).__jsii_proxy_class__ = lambda : _IOpenIdConnectProviderProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_iam.IPolicy")
class IPolicy(_IResource_c80c4260, typing_extensions.Protocol):
    '''Represents an IAM Policy.

    :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage.html
    '''

    @builtins.property
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        '''The name of this policy.

        :attribute: true
        '''
        ...


class _IPolicyProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''Represents an IAM Policy.

    :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage.html
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_iam.IPolicy"

    @builtins.property
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        '''The name of this policy.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "policyName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPolicy).__jsii_proxy_class__ = lambda : _IPolicyProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_iam.IPrincipal")
class IPrincipal(IGrantable, typing_extensions.Protocol):
    '''Represents a logical IAM principal.

    An IPrincipal describes a logical entity that can perform AWS API calls
    against sets of resources, optionally under certain conditions.

    Examples of simple principals are IAM objects that you create, such
    as Users or Roles.

    An example of a more complex principals is a ``ServicePrincipal`` (such as
    ``new ServicePrincipal("sns.amazonaws.com")``, which represents the Simple
    Notifications Service).

    A single logical Principal may also map to a set of physical principals.
    For example, ``new OrganizationPrincipal('o-1234')`` represents all
    identities that are part of the given AWS Organization.
    '''

    @builtins.property
    @jsii.member(jsii_name="assumeRoleAction")
    def assume_role_action(self) -> builtins.str:
        '''When this Principal is used in an AssumeRole policy, the action to use.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> "PrincipalPolicyFragment":
        '''Return the policy fragment that identifies this principal in a Policy.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="principalAccount")
    def principal_account(self) -> typing.Optional[builtins.str]:
        '''The AWS account ID of this principal.

        Can be undefined when the account is not known
        (for example, for service principals).
        Can be a Token - in that case,
        it's assumed to be AWS::AccountId.
        '''
        ...

    @jsii.member(jsii_name="addToPrincipalPolicy")
    def add_to_principal_policy(
        self,
        statement: "PolicyStatement",
    ) -> AddToPrincipalPolicyResult:
        '''Add to the policy of this principal.

        :param statement: -
        '''
        ...


class _IPrincipalProxy(
    jsii.proxy_for(IGrantable), # type: ignore[misc]
):
    '''Represents a logical IAM principal.

    An IPrincipal describes a logical entity that can perform AWS API calls
    against sets of resources, optionally under certain conditions.

    Examples of simple principals are IAM objects that you create, such
    as Users or Roles.

    An example of a more complex principals is a ``ServicePrincipal`` (such as
    ``new ServicePrincipal("sns.amazonaws.com")``, which represents the Simple
    Notifications Service).

    A single logical Principal may also map to a set of physical principals.
    For example, ``new OrganizationPrincipal('o-1234')`` represents all
    identities that are part of the given AWS Organization.
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_iam.IPrincipal"

    @builtins.property
    @jsii.member(jsii_name="assumeRoleAction")
    def assume_role_action(self) -> builtins.str:
        '''When this Principal is used in an AssumeRole policy, the action to use.'''
        return typing.cast(builtins.str, jsii.get(self, "assumeRoleAction"))

    @builtins.property
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> "PrincipalPolicyFragment":
        '''Return the policy fragment that identifies this principal in a Policy.'''
        return typing.cast("PrincipalPolicyFragment", jsii.get(self, "policyFragment"))

    @builtins.property
    @jsii.member(jsii_name="principalAccount")
    def principal_account(self) -> typing.Optional[builtins.str]:
        '''The AWS account ID of this principal.

        Can be undefined when the account is not known
        (for example, for service principals).
        Can be a Token - in that case,
        it's assumed to be AWS::AccountId.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "principalAccount"))

    @jsii.member(jsii_name="addToPrincipalPolicy")
    def add_to_principal_policy(
        self,
        statement: "PolicyStatement",
    ) -> AddToPrincipalPolicyResult:
        '''Add to the policy of this principal.

        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c10aadcc3756f5f6d5486d7ecd5cabd7845be5964af1722a9d4962d586babd4)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(AddToPrincipalPolicyResult, jsii.invoke(self, "addToPrincipalPolicy", [statement]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPrincipal).__jsii_proxy_class__ = lambda : _IPrincipalProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_iam.IResourceWithPolicy")
class IResourceWithPolicy(_IResource_c80c4260, typing_extensions.Protocol):
    '''A resource with a resource policy that can be added to.'''

    @jsii.member(jsii_name="addToResourcePolicy")
    def add_to_resource_policy(
        self,
        statement: "PolicyStatement",
    ) -> AddToResourcePolicyResult:
        '''Add a statement to the resource's resource policy.

        :param statement: -
        '''
        ...


class _IResourceWithPolicyProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''A resource with a resource policy that can be added to.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_iam.IResourceWithPolicy"

    @jsii.member(jsii_name="addToResourcePolicy")
    def add_to_resource_policy(
        self,
        statement: "PolicyStatement",
    ) -> AddToResourcePolicyResult:
        '''Add a statement to the resource's resource policy.

        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc0b619bfbc345bc9140fcc58d59f27472a211b09306f5c2e6b0147efcef6b18)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(AddToResourcePolicyResult, jsii.invoke(self, "addToResourcePolicy", [statement]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResourceWithPolicy).__jsii_proxy_class__ = lambda : _IResourceWithPolicyProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_iam.ISamlProvider")
class ISamlProvider(_IResource_c80c4260, typing_extensions.Protocol):
    '''A SAML provider.'''

    @builtins.property
    @jsii.member(jsii_name="samlProviderArn")
    def saml_provider_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the provider.

        :attribute: true
        '''
        ...


class _ISamlProviderProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''A SAML provider.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_iam.ISamlProvider"

    @builtins.property
    @jsii.member(jsii_name="samlProviderArn")
    def saml_provider_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the provider.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "samlProviderArn"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISamlProvider).__jsii_proxy_class__ = lambda : _ISamlProviderProxy


@jsii.implements(IInstanceProfile)
class InstanceProfile(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.InstanceProfile",
):
    '''IAM Instance Profile.

    :exampleMetadata: infused

    Example::

        role = iam.Role(self, "Role",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com")
        )
        
        instance_profile = iam.InstanceProfile.from_instance_profile_attributes(self, "ImportedInstanceProfile",
            instance_profile_arn="arn:aws:iam::account-id:instance-profile/MyInstanceProfile",
            role=role
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        instance_profile_name: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        role: typing.Optional["IRole"] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param instance_profile_name: The name of the InstanceProfile to create. Default: - generated by CloudFormation
        :param path: The path to the InstanceProfile. Default: /
        :param role: An IAM role to associate with the instance profile that is used by EC2 instances. The role must be assumable by the service principal ``ec2.amazonaws.com``: Default: - a role will be automatically created, it can be accessed via the ``role`` property
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47902e96d39fe1f772c15032b60b34efd5f4ebb64e4f7d08d924c04ab8393203)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = InstanceProfileProps(
            instance_profile_name=instance_profile_name, path=path, role=role
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromInstanceProfileArn")
    @builtins.classmethod
    def from_instance_profile_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        instance_profile_arn: builtins.str,
    ) -> IInstanceProfile:
        '''Import an existing InstanceProfile from an InstanceProfile ARN.

        If the ARN comes from a Token, the InstanceProfile cannot have a path; if so, any attempt
        to reference its instanceProfileName will fail.

        :param scope: construct scope.
        :param id: construct id.
        :param instance_profile_arn: the ARN of the exiting InstanceProfile to import.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c5f92c9eb36073e3604dae6b3449d6b3ce102597766d24026143d8edc87c0a1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument instance_profile_arn", value=instance_profile_arn, expected_type=type_hints["instance_profile_arn"])
        return typing.cast(IInstanceProfile, jsii.sinvoke(cls, "fromInstanceProfileArn", [scope, id, instance_profile_arn]))

    @jsii.member(jsii_name="fromInstanceProfileAttributes")
    @builtins.classmethod
    def from_instance_profile_attributes(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        instance_profile_arn: builtins.str,
        role: typing.Optional["IRole"] = None,
    ) -> IInstanceProfile:
        '''Import an existing InstanceProfile from given InstanceProfile attributes.

        If the ARN comes from a Token, the InstanceProfile cannot have a path; if so, any attempt
        to reference its instanceProfileName will fail.

        :param scope: construct scope.
        :param id: construct id.
        :param instance_profile_arn: The ARN of the InstanceProfile. Format: arn::iam:::instance-profile/
        :param role: The role associated with the InstanceProfile. Default: - no role
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4829ea04dde958ee082c71fd13dbdde279a49cce33d5b0cd09b7c5dc1a90e0a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = InstanceProfileAttributes(
            instance_profile_arn=instance_profile_arn, role=role
        )

        return typing.cast(IInstanceProfile, jsii.sinvoke(cls, "fromInstanceProfileAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="fromInstanceProfileName")
    @builtins.classmethod
    def from_instance_profile_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        instance_profile_name: builtins.str,
    ) -> IInstanceProfile:
        '''Import an existing InstanceProfile from an InstanceProfile name.

        :param scope: construct scope.
        :param id: construct id.
        :param instance_profile_name: the name of the existing InstanceProfile to import.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7870e30876638f54c4d41cd7645fabe3356a94b6ede305036ccf59d622f572e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument instance_profile_name", value=instance_profile_name, expected_type=type_hints["instance_profile_name"])
        return typing.cast(IInstanceProfile, jsii.sinvoke(cls, "fromInstanceProfileName", [scope, id, instance_profile_name]))

    @builtins.property
    @jsii.member(jsii_name="instanceProfileArn")
    def instance_profile_arn(self) -> builtins.str:
        '''Returns the ARN of this InstanceProfile.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceProfileArn"))

    @builtins.property
    @jsii.member(jsii_name="instanceProfileName")
    def instance_profile_name(self) -> builtins.str:
        '''Returns the name of this InstanceProfile.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceProfileName"))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> typing.Optional["IRole"]:
        '''Returns the role associated with this InstanceProfile.'''
        return typing.cast(typing.Optional["IRole"], jsii.get(self, "role"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.InstanceProfileAttributes",
    jsii_struct_bases=[],
    name_mapping={"instance_profile_arn": "instanceProfileArn", "role": "role"},
)
class InstanceProfileAttributes:
    def __init__(
        self,
        *,
        instance_profile_arn: builtins.str,
        role: typing.Optional["IRole"] = None,
    ) -> None:
        '''Attributes of an Instance Profile.

        :param instance_profile_arn: The ARN of the InstanceProfile. Format: arn::iam:::instance-profile/
        :param role: The role associated with the InstanceProfile. Default: - no role

        :exampleMetadata: infused

        Example::

            role = iam.Role(self, "Role",
                assumed_by=iam.ServicePrincipal("ec2.amazonaws.com")
            )
            
            instance_profile = iam.InstanceProfile.from_instance_profile_attributes(self, "ImportedInstanceProfile",
                instance_profile_arn="arn:aws:iam::account-id:instance-profile/MyInstanceProfile",
                role=role
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb6dd6d0c3541471c82745ecbcf8e73c173fa6246fd7249b3a9e71e7c5b84388)
            check_type(argname="argument instance_profile_arn", value=instance_profile_arn, expected_type=type_hints["instance_profile_arn"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_profile_arn": instance_profile_arn,
        }
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def instance_profile_arn(self) -> builtins.str:
        '''The ARN of the InstanceProfile.

        Format: arn::iam:::instance-profile/
        '''
        result = self._values.get("instance_profile_arn")
        assert result is not None, "Required property 'instance_profile_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role(self) -> typing.Optional["IRole"]:
        '''The role associated with the InstanceProfile.

        :default: - no role
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional["IRole"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstanceProfileAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.InstanceProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_profile_name": "instanceProfileName",
        "path": "path",
        "role": "role",
    },
)
class InstanceProfileProps:
    def __init__(
        self,
        *,
        instance_profile_name: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        role: typing.Optional["IRole"] = None,
    ) -> None:
        '''Properties of an Instance Profile.

        :param instance_profile_name: The name of the InstanceProfile to create. Default: - generated by CloudFormation
        :param path: The path to the InstanceProfile. Default: /
        :param role: An IAM role to associate with the instance profile that is used by EC2 instances. The role must be assumable by the service principal ``ec2.amazonaws.com``: Default: - a role will be automatically created, it can be accessed via the ``role`` property

        :exampleMetadata: infused

        Example::

            role = iam.Role(self, "Role",
                assumed_by=iam.ServicePrincipal("ec2.amazonaws.com")
            )
            
            instance_profile = iam.InstanceProfile(self, "InstanceProfile",
                role=role,
                instance_profile_name="MyInstanceProfile",
                path="/sample/path/"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac5e12eff086b0ebec934d941ac660747a3807a1f2e371ed4b509707ab23e345)
            check_type(argname="argument instance_profile_name", value=instance_profile_name, expected_type=type_hints["instance_profile_name"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if instance_profile_name is not None:
            self._values["instance_profile_name"] = instance_profile_name
        if path is not None:
            self._values["path"] = path
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def instance_profile_name(self) -> typing.Optional[builtins.str]:
        '''The name of the InstanceProfile to create.

        :default: - generated by CloudFormation
        '''
        result = self._values.get("instance_profile_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''The path to the InstanceProfile.

        :default: /
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional["IRole"]:
        '''An IAM role to associate with the instance profile that is used by EC2 instances.

        The role must be assumable by the service principal ``ec2.amazonaws.com``:

        :default: - a role will be automatically created, it can be accessed via the ``role`` property

        Example::

            role = iam.Role(self, "MyRole",
                assumed_by=iam.ServicePrincipal("ec2.amazonaws.com")
            )
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional["IRole"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstanceProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IManagedPolicy, IGrantable)
class ManagedPolicy(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.ManagedPolicy",
):
    '''Managed policy.

    :exampleMetadata: infused

    Example::

        # build: gamelift.Build
        
        role = iam.Role(self, "Role",
            assumed_by=iam.CompositePrincipal(iam.ServicePrincipal("gamelift.amazonaws.com"))
        )
        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("CloudWatchAgentServerPolicy"))
        
        fleet = gamelift.BuildFleet(self, "Game server fleet",
            fleet_name="test-fleet",
            content=build,
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.C5, ec2.InstanceSize.LARGE),
            runtime_configuration=gamelift.RuntimeConfiguration(
                server_processes=[gamelift.ServerProcess(
                    launch_path="/local/game/GameLiftExampleServer.x86_64"
                )]
            ),
            role=role
        )
        
        # Actions can also be grantted through dedicated method
        fleet.grant(role, "gamelift:ListFleets")
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        document: typing.Optional["PolicyDocument"] = None,
        groups: typing.Optional[typing.Sequence["IGroup"]] = None,
        managed_policy_name: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        roles: typing.Optional[typing.Sequence["IRole"]] = None,
        statements: typing.Optional[typing.Sequence["PolicyStatement"]] = None,
        users: typing.Optional[typing.Sequence["IUser"]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param description: A description of the managed policy. Typically used to store information about the permissions defined in the policy. For example, "Grants access to production DynamoDB tables." The policy description is immutable. After a value is assigned, it cannot be changed. Default: - empty
        :param document: Initial PolicyDocument to use for this ManagedPolicy. If omited, any ``PolicyStatement`` provided in the ``statements`` property will be applied against the empty default ``PolicyDocument``. Default: - An empty policy.
        :param groups: Groups to attach this policy to. You can also use ``attachToGroup(group)`` to attach this policy to a group. Default: - No groups.
        :param managed_policy_name: The name of the managed policy. If you specify multiple policies for an entity, specify unique names. For example, if you specify a list of policies for an IAM role, each policy must have a unique name. Default: - A name is automatically generated.
        :param path: The path for the policy. This parameter allows (through its regex pattern) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (\\u0021) through the DEL character (\\u007F), including most punctuation characters, digits, and upper and lowercased letters. For more information about paths, see IAM Identifiers in the IAM User Guide. Default: - "/"
        :param roles: Roles to attach this policy to. You can also use ``attachToRole(role)`` to attach this policy to a role. Default: - No roles.
        :param statements: Initial set of permissions to add to this policy document. You can also use ``addPermission(statement)`` to add permissions later. Default: - No statements.
        :param users: Users to attach this policy to. You can also use ``attachToUser(user)`` to attach this policy to a user. Default: - No users.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cd427eaa6d6959043bb705f947d652220f35431c484ef548899b9f81e573c2d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ManagedPolicyProps(
            description=description,
            document=document,
            groups=groups,
            managed_policy_name=managed_policy_name,
            path=path,
            roles=roles,
            statements=statements,
            users=users,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromAwsManagedPolicyName")
    @builtins.classmethod
    def from_aws_managed_policy_name(
        cls,
        managed_policy_name: builtins.str,
    ) -> IManagedPolicy:
        '''Import a managed policy from one of the policies that AWS manages.

        For this managed policy, you only need to know the name to be able to use it.

        Some managed policy names start with "service-role/", some start with
        "job-function/", and some don't start with anything. Include the
        prefix when constructing this object.

        :param managed_policy_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04dc3b9def232bf73e8992c95959e8ca96d18af4cafb5db34a590a221cb825ca)
            check_type(argname="argument managed_policy_name", value=managed_policy_name, expected_type=type_hints["managed_policy_name"])
        return typing.cast(IManagedPolicy, jsii.sinvoke(cls, "fromAwsManagedPolicyName", [managed_policy_name]))

    @jsii.member(jsii_name="fromManagedPolicyArn")
    @builtins.classmethod
    def from_managed_policy_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        managed_policy_arn: builtins.str,
    ) -> IManagedPolicy:
        '''Import an external managed policy by ARN.

        For this managed policy, you only need to know the ARN to be able to use it.
        This can be useful if you got the ARN from a CloudFormation Export.

        If the imported Managed Policy ARN is a Token (such as a
        ``CfnParameter.valueAsString`` or a ``Fn.importValue()``) *and* the referenced
        managed policy has a ``path`` (like ``arn:...:policy/AdminPolicy/AdminAllow``), the
        ``managedPolicyName`` property will not resolve to the correct value. Instead it
        will resolve to the first path component. We unfortunately cannot express
        the correct calculation of the full path name as a CloudFormation
        expression. In this scenario the Managed Policy ARN should be supplied without the
        ``path`` in order to resolve the correct managed policy resource.

        :param scope: construct scope.
        :param id: construct id.
        :param managed_policy_arn: the ARN of the managed policy to import.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b433b3584cc62234ee457168b3f3d2db5b0b227fe9dc2240edd9ce3eecb779a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument managed_policy_arn", value=managed_policy_arn, expected_type=type_hints["managed_policy_arn"])
        return typing.cast(IManagedPolicy, jsii.sinvoke(cls, "fromManagedPolicyArn", [scope, id, managed_policy_arn]))

    @jsii.member(jsii_name="fromManagedPolicyName")
    @builtins.classmethod
    def from_managed_policy_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        managed_policy_name: builtins.str,
    ) -> IManagedPolicy:
        '''Import a customer managed policy from the managedPolicyName.

        For this managed policy, you only need to know the name to be able to use it.

        :param scope: -
        :param id: -
        :param managed_policy_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__324e775a0f29673011a6cd38f79e52c1bb0c3c5c895f02fcfd38496e4fe98322)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument managed_policy_name", value=managed_policy_name, expected_type=type_hints["managed_policy_name"])
        return typing.cast(IManagedPolicy, jsii.sinvoke(cls, "fromManagedPolicyName", [scope, id, managed_policy_name]))

    @jsii.member(jsii_name="addStatements")
    def add_statements(self, *statement: "PolicyStatement") -> None:
        '''Adds a statement to the policy document.

        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc09c2f794b8d270cf58515acd36f16f22c50e8e485667751a6b6bf5441cdcef)
            check_type(argname="argument statement", value=statement, expected_type=typing.Tuple[type_hints["statement"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addStatements", [*statement]))

    @jsii.member(jsii_name="attachToGroup")
    def attach_to_group(self, group: "IGroup") -> None:
        '''Attaches this policy to a group.

        :param group: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53947185e012309c9619b70da30bfebeef3a52fedd6d8eca19e9a8e96853c82e)
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
        return typing.cast(None, jsii.invoke(self, "attachToGroup", [group]))

    @jsii.member(jsii_name="attachToRole")
    def attach_to_role(self, role: "IRole") -> None:
        '''Attaches this policy to a role.

        :param role: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3b5752936a78a06ee1095be0dc5362932d7db4aa0245a456f4cfea45bef91c9)
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        return typing.cast(None, jsii.invoke(self, "attachToRole", [role]))

    @jsii.member(jsii_name="attachToUser")
    def attach_to_user(self, user: "IUser") -> None:
        '''Attaches this policy to a user.

        :param user: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3b5f4b1c957b78ec0d5ae0e80dc7f2471a55d293c6a67e32ef5a2046d89543d)
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
        return typing.cast(None, jsii.invoke(self, "attachToUser", [user]))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''The description of this policy.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="document")
    def document(self) -> "PolicyDocument":
        '''The policy document.'''
        return typing.cast("PolicyDocument", jsii.get(self, "document"))

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> IPrincipal:
        '''The principal to grant permissions to.'''
        return typing.cast(IPrincipal, jsii.get(self, "grantPrincipal"))

    @builtins.property
    @jsii.member(jsii_name="managedPolicyArn")
    def managed_policy_arn(self) -> builtins.str:
        '''Returns the ARN of this managed policy.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "managedPolicyArn"))

    @builtins.property
    @jsii.member(jsii_name="managedPolicyName")
    def managed_policy_name(self) -> builtins.str:
        '''The name of this policy.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "managedPolicyName"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        '''The path of this policy.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "path"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.ManagedPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "document": "document",
        "groups": "groups",
        "managed_policy_name": "managedPolicyName",
        "path": "path",
        "roles": "roles",
        "statements": "statements",
        "users": "users",
    },
)
class ManagedPolicyProps:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        document: typing.Optional["PolicyDocument"] = None,
        groups: typing.Optional[typing.Sequence["IGroup"]] = None,
        managed_policy_name: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        roles: typing.Optional[typing.Sequence["IRole"]] = None,
        statements: typing.Optional[typing.Sequence["PolicyStatement"]] = None,
        users: typing.Optional[typing.Sequence["IUser"]] = None,
    ) -> None:
        '''Properties for defining an IAM managed policy.

        :param description: A description of the managed policy. Typically used to store information about the permissions defined in the policy. For example, "Grants access to production DynamoDB tables." The policy description is immutable. After a value is assigned, it cannot be changed. Default: - empty
        :param document: Initial PolicyDocument to use for this ManagedPolicy. If omited, any ``PolicyStatement`` provided in the ``statements`` property will be applied against the empty default ``PolicyDocument``. Default: - An empty policy.
        :param groups: Groups to attach this policy to. You can also use ``attachToGroup(group)`` to attach this policy to a group. Default: - No groups.
        :param managed_policy_name: The name of the managed policy. If you specify multiple policies for an entity, specify unique names. For example, if you specify a list of policies for an IAM role, each policy must have a unique name. Default: - A name is automatically generated.
        :param path: The path for the policy. This parameter allows (through its regex pattern) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (\\u0021) through the DEL character (\\u007F), including most punctuation characters, digits, and upper and lowercased letters. For more information about paths, see IAM Identifiers in the IAM User Guide. Default: - "/"
        :param roles: Roles to attach this policy to. You can also use ``attachToRole(role)`` to attach this policy to a role. Default: - No roles.
        :param statements: Initial set of permissions to add to this policy document. You can also use ``addPermission(statement)`` to add permissions later. Default: - No statements.
        :param users: Users to attach this policy to. You can also use ``attachToUser(user)`` to attach this policy to a user. Default: - No users.

        :exampleMetadata: infused

        Example::

            policy_document = {
                "Version": "2012-10-17",
                "Statement": [{
                    "Sid": "FirstStatement",
                    "Effect": "Allow",
                    "Action": ["iam:ChangePassword"],
                    "Resource": ["*"]
                }, {
                    "Sid": "SecondStatement",
                    "Effect": "Allow",
                    "Action": ["s3:ListAllMyBuckets"],
                    "Resource": ["*"]
                }, {
                    "Sid": "ThirdStatement",
                    "Effect": "Allow",
                    "Action": ["s3:List*", "s3:Get*"
                    ],
                    "Resource": ["arn:aws:s3:::confidential-data", "arn:aws:s3:::confidential-data/*"
                    ],
                    "Condition": {"Bool": {"aws:_multi_factor_auth_present": "true"}}
                }
                ]
            }
            
            custom_policy_document = iam.PolicyDocument.from_json(policy_document)
            
            # You can pass this document as an initial document to a ManagedPolicy
            # or inline Policy.
            new_managed_policy = iam.ManagedPolicy(self, "MyNewManagedPolicy",
                document=custom_policy_document
            )
            new_policy = iam.Policy(self, "MyNewPolicy",
                document=custom_policy_document
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ac402af2b963b15f12c561030bd732418fdef258857572111b9a81189e27e35)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument document", value=document, expected_type=type_hints["document"])
            check_type(argname="argument groups", value=groups, expected_type=type_hints["groups"])
            check_type(argname="argument managed_policy_name", value=managed_policy_name, expected_type=type_hints["managed_policy_name"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument roles", value=roles, expected_type=type_hints["roles"])
            check_type(argname="argument statements", value=statements, expected_type=type_hints["statements"])
            check_type(argname="argument users", value=users, expected_type=type_hints["users"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if document is not None:
            self._values["document"] = document
        if groups is not None:
            self._values["groups"] = groups
        if managed_policy_name is not None:
            self._values["managed_policy_name"] = managed_policy_name
        if path is not None:
            self._values["path"] = path
        if roles is not None:
            self._values["roles"] = roles
        if statements is not None:
            self._values["statements"] = statements
        if users is not None:
            self._values["users"] = users

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the managed policy.

        Typically used to store information about the
        permissions defined in the policy. For example, "Grants access to production DynamoDB tables."
        The policy description is immutable. After a value is assigned, it cannot be changed.

        :default: - empty
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def document(self) -> typing.Optional["PolicyDocument"]:
        '''Initial PolicyDocument to use for this ManagedPolicy.

        If omited, any
        ``PolicyStatement`` provided in the ``statements`` property will be applied
        against the empty default ``PolicyDocument``.

        :default: - An empty policy.
        '''
        result = self._values.get("document")
        return typing.cast(typing.Optional["PolicyDocument"], result)

    @builtins.property
    def groups(self) -> typing.Optional[typing.List["IGroup"]]:
        '''Groups to attach this policy to.

        You can also use ``attachToGroup(group)`` to attach this policy to a group.

        :default: - No groups.
        '''
        result = self._values.get("groups")
        return typing.cast(typing.Optional[typing.List["IGroup"]], result)

    @builtins.property
    def managed_policy_name(self) -> typing.Optional[builtins.str]:
        '''The name of the managed policy.

        If you specify multiple policies for an entity,
        specify unique names. For example, if you specify a list of policies for
        an IAM role, each policy must have a unique name.

        :default: - A name is automatically generated.
        '''
        result = self._values.get("managed_policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''The path for the policy.

        This parameter allows (through its regex pattern) a string of characters
        consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes.
        In addition, it can contain any ASCII character from the ! (\\u0021) through the DEL character (\\u007F),
        including most punctuation characters, digits, and upper and lowercased letters.

        For more information about paths, see IAM Identifiers in the IAM User Guide.

        :default: - "/"
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def roles(self) -> typing.Optional[typing.List["IRole"]]:
        '''Roles to attach this policy to.

        You can also use ``attachToRole(role)`` to attach this policy to a role.

        :default: - No roles.
        '''
        result = self._values.get("roles")
        return typing.cast(typing.Optional[typing.List["IRole"]], result)

    @builtins.property
    def statements(self) -> typing.Optional[typing.List["PolicyStatement"]]:
        '''Initial set of permissions to add to this policy document.

        You can also use ``addPermission(statement)`` to add permissions later.

        :default: - No statements.
        '''
        result = self._values.get("statements")
        return typing.cast(typing.Optional[typing.List["PolicyStatement"]], result)

    @builtins.property
    def users(self) -> typing.Optional[typing.List["IUser"]]:
        '''Users to attach this policy to.

        You can also use ``attachToUser(user)`` to attach this policy to a user.

        :default: - No users.
        '''
        result = self._values.get("users")
        return typing.cast(typing.Optional[typing.List["IUser"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IOpenIdConnectProvider)
class OpenIdConnectProvider(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.OpenIdConnectProvider",
):
    '''IAM OIDC identity providers are entities in IAM that describe an external identity provider (IdP) service that supports the OpenID Connect (OIDC) standard, such as Google or Salesforce.

    You use an IAM OIDC identity provider
    when you want to establish trust between an OIDC-compatible IdP and your AWS
    account. This is useful when creating a mobile app or web application that
    requires access to AWS resources, but you don't want to create custom sign-in
    code or manage your own user identities.

    :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc.html
    :resource: AWS::CloudFormation::CustomResource
    :exampleMetadata: infused

    Example::

        provider = iam.OpenIdConnectProvider(self, "MyProvider",
            url="https://openid/connect",
            client_ids=["myclient1", "myclient2"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        url: builtins.str,
        client_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        thumbprints: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Defines an OpenID Connect provider.

        :param scope: The definition scope.
        :param id: Construct ID.
        :param url: The URL of the identity provider. The URL must begin with https:// and should correspond to the iss claim in the provider's OpenID Connect ID tokens. Per the OIDC standard, path components are allowed but query parameters are not. Typically the URL consists of only a hostname, like https://server.example.org or https://example.com. You cannot register the same provider multiple times in a single AWS account. If you try to submit a URL that has already been used for an OpenID Connect provider in the AWS account, you will get an error.
        :param client_ids: A list of client IDs (also known as audiences). When a mobile or web app registers with an OpenID Connect provider, they establish a value that identifies the application. (This is the value that's sent as the client_id parameter on OAuth requests.) You can register multiple client IDs with the same provider. For example, you might have multiple applications that use the same OIDC provider. You cannot register more than 100 client IDs with a single IAM OIDC provider. Client IDs are up to 255 characters long. Default: - no clients are allowed
        :param thumbprints: A list of server certificate thumbprints for the OpenID Connect (OIDC) identity provider's server certificates. Typically this list includes only one entry. However, IAM lets you have up to five thumbprints for an OIDC provider. This lets you maintain multiple thumbprints if the identity provider is rotating certificates. The server certificate thumbprint is the hex-encoded SHA-1 hash value of the X.509 certificate used by the domain where the OpenID Connect provider makes its keys available. It is always a 40-character string. You must provide at least one thumbprint when creating an IAM OIDC provider. For example, assume that the OIDC provider is server.example.com and the provider stores its keys at https://keys.server.example.com/openid-connect. In that case, the thumbprint string would be the hex-encoded SHA-1 hash value of the certificate used by https://keys.server.example.com. Default: - If no thumbprints are specified (an empty array or ``undefined``), the thumbprint of the root certificate authority will be obtained from the provider's server as described in https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc_verify-thumbprint.html
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__270fe9db45fea69c973ea36d667d5236d0463996999ebebabf67dbaafe739d10)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = OpenIdConnectProviderProps(
            url=url, client_ids=client_ids, thumbprints=thumbprints
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromOpenIdConnectProviderArn")
    @builtins.classmethod
    def from_open_id_connect_provider_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        open_id_connect_provider_arn: builtins.str,
    ) -> IOpenIdConnectProvider:
        '''Imports an Open ID connect provider from an ARN.

        :param scope: The definition scope.
        :param id: ID of the construct.
        :param open_id_connect_provider_arn: the ARN to import.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b937a1209414da4def854fd0c371550ec506b47f8d3f8c931bee67604e5589a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument open_id_connect_provider_arn", value=open_id_connect_provider_arn, expected_type=type_hints["open_id_connect_provider_arn"])
        return typing.cast(IOpenIdConnectProvider, jsii.sinvoke(cls, "fromOpenIdConnectProviderArn", [scope, id, open_id_connect_provider_arn]))

    @builtins.property
    @jsii.member(jsii_name="openIdConnectProviderArn")
    def open_id_connect_provider_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM OpenID Connect provider.'''
        return typing.cast(builtins.str, jsii.get(self, "openIdConnectProviderArn"))

    @builtins.property
    @jsii.member(jsii_name="openIdConnectProviderIssuer")
    def open_id_connect_provider_issuer(self) -> builtins.str:
        '''The issuer for OIDC Provider.'''
        return typing.cast(builtins.str, jsii.get(self, "openIdConnectProviderIssuer"))

    @builtins.property
    @jsii.member(jsii_name="openIdConnectProviderthumbprints")
    def open_id_connect_providerthumbprints(self) -> builtins.str:
        '''The thumbprints configured for this provider.'''
        return typing.cast(builtins.str, jsii.get(self, "openIdConnectProviderthumbprints"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.OpenIdConnectProviderProps",
    jsii_struct_bases=[],
    name_mapping={
        "url": "url",
        "client_ids": "clientIds",
        "thumbprints": "thumbprints",
    },
)
class OpenIdConnectProviderProps:
    def __init__(
        self,
        *,
        url: builtins.str,
        client_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        thumbprints: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Initialization properties for ``OpenIdConnectProvider``.

        :param url: The URL of the identity provider. The URL must begin with https:// and should correspond to the iss claim in the provider's OpenID Connect ID tokens. Per the OIDC standard, path components are allowed but query parameters are not. Typically the URL consists of only a hostname, like https://server.example.org or https://example.com. You cannot register the same provider multiple times in a single AWS account. If you try to submit a URL that has already been used for an OpenID Connect provider in the AWS account, you will get an error.
        :param client_ids: A list of client IDs (also known as audiences). When a mobile or web app registers with an OpenID Connect provider, they establish a value that identifies the application. (This is the value that's sent as the client_id parameter on OAuth requests.) You can register multiple client IDs with the same provider. For example, you might have multiple applications that use the same OIDC provider. You cannot register more than 100 client IDs with a single IAM OIDC provider. Client IDs are up to 255 characters long. Default: - no clients are allowed
        :param thumbprints: A list of server certificate thumbprints for the OpenID Connect (OIDC) identity provider's server certificates. Typically this list includes only one entry. However, IAM lets you have up to five thumbprints for an OIDC provider. This lets you maintain multiple thumbprints if the identity provider is rotating certificates. The server certificate thumbprint is the hex-encoded SHA-1 hash value of the X.509 certificate used by the domain where the OpenID Connect provider makes its keys available. It is always a 40-character string. You must provide at least one thumbprint when creating an IAM OIDC provider. For example, assume that the OIDC provider is server.example.com and the provider stores its keys at https://keys.server.example.com/openid-connect. In that case, the thumbprint string would be the hex-encoded SHA-1 hash value of the certificate used by https://keys.server.example.com. Default: - If no thumbprints are specified (an empty array or ``undefined``), the thumbprint of the root certificate authority will be obtained from the provider's server as described in https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc_verify-thumbprint.html

        :exampleMetadata: infused

        Example::

            provider = iam.OpenIdConnectProvider(self, "MyProvider",
                url="https://openid/connect",
                client_ids=["myclient1", "myclient2"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c07fc1633df440495e4513aa2acd1999d7e26f667e4c9d387ecfed34ba60aa34)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument client_ids", value=client_ids, expected_type=type_hints["client_ids"])
            check_type(argname="argument thumbprints", value=thumbprints, expected_type=type_hints["thumbprints"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "url": url,
        }
        if client_ids is not None:
            self._values["client_ids"] = client_ids
        if thumbprints is not None:
            self._values["thumbprints"] = thumbprints

    @builtins.property
    def url(self) -> builtins.str:
        '''The URL of the identity provider.

        The URL must begin with https:// and
        should correspond to the iss claim in the provider's OpenID Connect ID
        tokens. Per the OIDC standard, path components are allowed but query
        parameters are not. Typically the URL consists of only a hostname, like
        https://server.example.org or https://example.com.

        You cannot register the same provider multiple times in a single AWS
        account. If you try to submit a URL that has already been used for an
        OpenID Connect provider in the AWS account, you will get an error.
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of client IDs (also known as audiences).

        When a mobile or web app
        registers with an OpenID Connect provider, they establish a value that
        identifies the application. (This is the value that's sent as the client_id
        parameter on OAuth requests.)

        You can register multiple client IDs with the same provider. For example,
        you might have multiple applications that use the same OIDC provider. You
        cannot register more than 100 client IDs with a single IAM OIDC provider.

        Client IDs are up to 255 characters long.

        :default: - no clients are allowed
        '''
        result = self._values.get("client_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def thumbprints(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of server certificate thumbprints for the OpenID Connect (OIDC) identity provider's server certificates.

        Typically this list includes only one entry. However, IAM lets you have up
        to five thumbprints for an OIDC provider. This lets you maintain multiple
        thumbprints if the identity provider is rotating certificates.

        The server certificate thumbprint is the hex-encoded SHA-1 hash value of
        the X.509 certificate used by the domain where the OpenID Connect provider
        makes its keys available. It is always a 40-character string.

        You must provide at least one thumbprint when creating an IAM OIDC
        provider. For example, assume that the OIDC provider is server.example.com
        and the provider stores its keys at
        https://keys.server.example.com/openid-connect. In that case, the
        thumbprint string would be the hex-encoded SHA-1 hash value of the
        certificate used by https://keys.server.example.com.

        :default:

        - If no thumbprints are specified (an empty array or ``undefined``),
        the thumbprint of the root certificate authority will be obtained from the
        provider's server as described in https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc_verify-thumbprint.html
        '''
        result = self._values.get("thumbprints")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpenIdConnectProviderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PermissionsBoundary(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.PermissionsBoundary",
):
    '''Modify the Permissions Boundaries of Users and Roles in a construct tree.

    Example::

       policy = iam.ManagedPolicy.from_aws_managed_policy_name("ReadOnlyAccess")
       iam.PermissionsBoundary.of(self).apply(policy)

    :exampleMetadata: infused

    Example::

        # project: codebuild.Project
        
        iam.PermissionsBoundary.of(project).apply(codebuild.UntrustedCodeBoundaryPolicy(self, "Boundary"))
    '''

    @jsii.member(jsii_name="of")
    @builtins.classmethod
    def of(cls, scope: _constructs_77d1e7e8.IConstruct) -> "PermissionsBoundary":
        '''Access the Permissions Boundaries of a construct tree.

        :param scope: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c60cfb31fa5f1464742fd5bd4c6874bbac2f64c851f5a2c9446ae181b34b208)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast("PermissionsBoundary", jsii.sinvoke(cls, "of", [scope]))

    @jsii.member(jsii_name="apply")
    def apply(self, boundary_policy: IManagedPolicy) -> None:
        '''Apply the given policy as Permissions Boundary to all Roles and Users in the scope.

        Will override any Permissions Boundaries configured previously; in case
        a Permission Boundary is applied in multiple scopes, the Boundary applied
        closest to the Role wins.

        :param boundary_policy: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d84d00226fae280f509c83e8e2fe992e095759345570998cb685b91b3428566)
            check_type(argname="argument boundary_policy", value=boundary_policy, expected_type=type_hints["boundary_policy"])
        return typing.cast(None, jsii.invoke(self, "apply", [boundary_policy]))

    @jsii.member(jsii_name="clear")
    def clear(self) -> None:
        '''Remove previously applied Permissions Boundaries.'''
        return typing.cast(None, jsii.invoke(self, "clear", []))


@jsii.implements(IPolicy, IGrantable)
class Policy(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.Policy",
):
    '''The AWS::IAM::Policy resource associates an `inline <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#inline>`_ IAM policy with IAM users, roles, or groups. For more information about IAM policies, see `Overview of IAM Policies <http://docs.aws.amazon.com/IAM/latest/UserGuide/policies_overview.html>`_ in the IAM User Guide guide.

    :exampleMetadata: infused

    Example::

        # post_auth_fn: lambda.Function
        
        
        userpool = cognito.UserPool(self, "myuserpool",
            lambda_triggers=cognito.UserPoolTriggers(
                post_authentication=post_auth_fn
            )
        )
        
        # provide permissions to describe the user pool scoped to the ARN the user pool
        post_auth_fn.role.attach_inline_policy(iam.Policy(self, "userpool-policy",
            statements=[iam.PolicyStatement(
                actions=["cognito-idp:DescribeUserPool"],
                resources=[userpool.user_pool_arn]
            )]
        ))
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        document: typing.Optional["PolicyDocument"] = None,
        force: typing.Optional[builtins.bool] = None,
        groups: typing.Optional[typing.Sequence["IGroup"]] = None,
        policy_name: typing.Optional[builtins.str] = None,
        roles: typing.Optional[typing.Sequence["IRole"]] = None,
        statements: typing.Optional[typing.Sequence["PolicyStatement"]] = None,
        users: typing.Optional[typing.Sequence["IUser"]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param document: Initial PolicyDocument to use for this Policy. If omited, any ``PolicyStatement`` provided in the ``statements`` property will be applied against the empty default ``PolicyDocument``. Default: - An empty policy.
        :param force: Force creation of an ``AWS::IAM::Policy``. Unless set to ``true``, this ``Policy`` construct will not materialize to an ``AWS::IAM::Policy`` CloudFormation resource in case it would have no effect (for example, if it remains unattached to an IAM identity or if it has no statements). This is generally desired behavior, since it prevents creating invalid--and hence undeployable--CloudFormation templates. In cases where you know the policy must be created and it is actually an error if no statements have been added to it or it remains unattached to an IAM identity, you can set this to ``true``. Default: false
        :param groups: Groups to attach this policy to. You can also use ``attachToGroup(group)`` to attach this policy to a group. Default: - No groups.
        :param policy_name: The name of the policy. If you specify multiple policies for an entity, specify unique names. For example, if you specify a list of policies for an IAM role, each policy must have a unique name. Default: - Uses the logical ID of the policy resource, which is ensured to be unique within the stack.
        :param roles: Roles to attach this policy to. You can also use ``attachToRole(role)`` to attach this policy to a role. Default: - No roles.
        :param statements: Initial set of permissions to add to this policy document. You can also use ``addStatements(...statement)`` to add permissions later. Default: - No statements.
        :param users: Users to attach this policy to. You can also use ``attachToUser(user)`` to attach this policy to a user. Default: - No users.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf4aaba2f6acb5486adaf871c56e1317b1a2931936b56a78bf4633c14caba596)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = PolicyProps(
            document=document,
            force=force,
            groups=groups,
            policy_name=policy_name,
            roles=roles,
            statements=statements,
            users=users,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromPolicyName")
    @builtins.classmethod
    def from_policy_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        policy_name: builtins.str,
    ) -> IPolicy:
        '''Import a policy in this app based on its name.

        :param scope: -
        :param id: -
        :param policy_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11207539a0ef88ae02fb600ab0862501107d998ae3be0f5a08a9fc0466cc0948)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
        return typing.cast(IPolicy, jsii.sinvoke(cls, "fromPolicyName", [scope, id, policy_name]))

    @jsii.member(jsii_name="addStatements")
    def add_statements(self, *statement: "PolicyStatement") -> None:
        '''Adds a statement to the policy document.

        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__510252a6b115bef4c94f6ab3c402eb29a1b2012a86045ddad51b4825713e0799)
            check_type(argname="argument statement", value=statement, expected_type=typing.Tuple[type_hints["statement"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addStatements", [*statement]))

    @jsii.member(jsii_name="attachToGroup")
    def attach_to_group(self, group: "IGroup") -> None:
        '''Attaches this policy to a group.

        :param group: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d09ae4b9f8a7c9ca0442c9a4b6f69bce78f42c194de9b535704dc9718516fea)
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
        return typing.cast(None, jsii.invoke(self, "attachToGroup", [group]))

    @jsii.member(jsii_name="attachToRole")
    def attach_to_role(self, role: "IRole") -> None:
        '''Attaches this policy to a role.

        :param role: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__010ce98a5e97a30c0c893a505506c652f5ecdb76ee983e02c498a174717f3e82)
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        return typing.cast(None, jsii.invoke(self, "attachToRole", [role]))

    @jsii.member(jsii_name="attachToUser")
    def attach_to_user(self, user: "IUser") -> None:
        '''Attaches this policy to a user.

        :param user: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87f9ba31abd317367c4b853073e8d4e30843f460c3420b69165c6082b01547ae)
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
        return typing.cast(None, jsii.invoke(self, "attachToUser", [user]))

    @builtins.property
    @jsii.member(jsii_name="document")
    def document(self) -> "PolicyDocument":
        '''The policy document.'''
        return typing.cast("PolicyDocument", jsii.get(self, "document"))

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> IPrincipal:
        '''The principal to grant permissions to.'''
        return typing.cast(IPrincipal, jsii.get(self, "grantPrincipal"))

    @builtins.property
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        '''The name of this policy.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "policyName"))


@jsii.implements(_IResolvable_da3f097b)
class PolicyDocument(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.PolicyDocument",
):
    '''A PolicyDocument is a collection of statements.

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

    def __init__(
        self,
        *,
        assign_sids: typing.Optional[builtins.bool] = None,
        minimize: typing.Optional[builtins.bool] = None,
        statements: typing.Optional[typing.Sequence["PolicyStatement"]] = None,
    ) -> None:
        '''
        :param assign_sids: Automatically assign Statement Ids to all statements. Default: false
        :param minimize: Try to minimize the policy by merging statements. To avoid overrunning the maximum policy size, combine statements if they produce the same result. Merging happens according to the following rules: - The Effect of both statements is the same - Neither of the statements have a 'Sid' - Combine Principals if the rest of the statement is exactly the same. - Combine Resources if the rest of the statement is exactly the same. - Combine Actions if the rest of the statement is exactly the same. - We will never combine NotPrincipals, NotResources or NotActions, because doing so would change the meaning of the policy document. Default: - false, unless the feature flag ``@aws-cdk/aws-iam:minimizePolicies`` is set
        :param statements: Initial statements to add to the policy document. Default: - No statements
        '''
        props = PolicyDocumentProps(
            assign_sids=assign_sids, minimize=minimize, statements=statements
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="fromJson")
    @builtins.classmethod
    def from_json(cls, obj: typing.Any) -> "PolicyDocument":
        '''Creates a new PolicyDocument based on the object provided.

        This will accept an object created from the ``.toJSON()`` call

        :param obj: the PolicyDocument in object form.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__570b193deac1ab27a70fd71df51891425bc3ec3540e0a5cf7f8f9e585b276f20)
            check_type(argname="argument obj", value=obj, expected_type=type_hints["obj"])
        return typing.cast("PolicyDocument", jsii.sinvoke(cls, "fromJson", [obj]))

    @jsii.member(jsii_name="addStatements")
    def add_statements(self, *statement: "PolicyStatement") -> None:
        '''Adds a statement to the policy document.

        :param statement: the statement to add.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54360ff9757f011bcac10fedb199770d4d17ebf0453c3d234c0d5dc45d33e1c1)
            check_type(argname="argument statement", value=statement, expected_type=typing.Tuple[type_hints["statement"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addStatements", [*statement]))

    @jsii.member(jsii_name="resolve")
    def resolve(self, context: _IResolveContext_b2df1921) -> typing.Any:
        '''Produce the Token's value at resolution time.

        :param context: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2bffb5bcc0e0574448352039a95ee7ed66fbd29faff9f34b1c5e482d329f7e3)
            check_type(argname="argument context", value=context, expected_type=type_hints["context"])
        return typing.cast(typing.Any, jsii.invoke(self, "resolve", [context]))

    @jsii.member(jsii_name="toJSON")
    def to_json(self) -> typing.Any:
        '''JSON-ify the document.

        Used when JSON.stringify() is called
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "toJSON", []))

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''Encode the policy document as a string.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @jsii.member(jsii_name="validateForAnyPolicy")
    def validate_for_any_policy(self) -> typing.List[builtins.str]:
        '''Validate that all policy statements in the policy document satisfies the requirements for any policy.

        :return: An array of validation error messages, or an empty array if the document is valid.

        :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-json
        '''
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "validateForAnyPolicy", []))

    @jsii.member(jsii_name="validateForIdentityPolicy")
    def validate_for_identity_policy(self) -> typing.List[builtins.str]:
        '''Validate that all policy statements in the policy document satisfies the requirements for an identity-based policy.

        :return: An array of validation error messages, or an empty array if the document is valid.

        :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-json
        '''
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "validateForIdentityPolicy", []))

    @jsii.member(jsii_name="validateForResourcePolicy")
    def validate_for_resource_policy(self) -> typing.List[builtins.str]:
        '''Validate that all policy statements in the policy document satisfies the requirements for a resource-based policy.

        :return: An array of validation error messages, or an empty array if the document is valid.

        :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-json
        '''
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "validateForResourcePolicy", []))

    @builtins.property
    @jsii.member(jsii_name="creationStack")
    def creation_stack(self) -> typing.List[builtins.str]:
        '''The creation stack of this resolvable which will be appended to errors thrown during resolution.

        This may return an array with a single informational element indicating how
        to get this property populated, if it was skipped for performance reasons.
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "creationStack"))

    @builtins.property
    @jsii.member(jsii_name="isEmpty")
    def is_empty(self) -> builtins.bool:
        '''Whether the policy document contains any statements.'''
        return typing.cast(builtins.bool, jsii.get(self, "isEmpty"))

    @builtins.property
    @jsii.member(jsii_name="statementCount")
    def statement_count(self) -> jsii.Number:
        '''The number of statements already added to this policy.

        Can be used, for example, to generate unique "sid"s within the policy.
        '''
        return typing.cast(jsii.Number, jsii.get(self, "statementCount"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.PolicyDocumentProps",
    jsii_struct_bases=[],
    name_mapping={
        "assign_sids": "assignSids",
        "minimize": "minimize",
        "statements": "statements",
    },
)
class PolicyDocumentProps:
    def __init__(
        self,
        *,
        assign_sids: typing.Optional[builtins.bool] = None,
        minimize: typing.Optional[builtins.bool] = None,
        statements: typing.Optional[typing.Sequence["PolicyStatement"]] = None,
    ) -> None:
        '''Properties for a new PolicyDocument.

        :param assign_sids: Automatically assign Statement Ids to all statements. Default: false
        :param minimize: Try to minimize the policy by merging statements. To avoid overrunning the maximum policy size, combine statements if they produce the same result. Merging happens according to the following rules: - The Effect of both statements is the same - Neither of the statements have a 'Sid' - Combine Principals if the rest of the statement is exactly the same. - Combine Resources if the rest of the statement is exactly the same. - Combine Actions if the rest of the statement is exactly the same. - We will never combine NotPrincipals, NotResources or NotActions, because doing so would change the meaning of the policy document. Default: - false, unless the feature flag ``@aws-cdk/aws-iam:minimizePolicies`` is set
        :param statements: Initial statements to add to the policy document. Default: - No statements

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
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__148d80305c19bb7e6f27161227f29ccdccd87c5529111c191eee0c97d735d661)
            check_type(argname="argument assign_sids", value=assign_sids, expected_type=type_hints["assign_sids"])
            check_type(argname="argument minimize", value=minimize, expected_type=type_hints["minimize"])
            check_type(argname="argument statements", value=statements, expected_type=type_hints["statements"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if assign_sids is not None:
            self._values["assign_sids"] = assign_sids
        if minimize is not None:
            self._values["minimize"] = minimize
        if statements is not None:
            self._values["statements"] = statements

    @builtins.property
    def assign_sids(self) -> typing.Optional[builtins.bool]:
        '''Automatically assign Statement Ids to all statements.

        :default: false
        '''
        result = self._values.get("assign_sids")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def minimize(self) -> typing.Optional[builtins.bool]:
        '''Try to minimize the policy by merging statements.

        To avoid overrunning the maximum policy size, combine statements if they produce
        the same result. Merging happens according to the following rules:

        - The Effect of both statements is the same
        - Neither of the statements have a 'Sid'
        - Combine Principals if the rest of the statement is exactly the same.
        - Combine Resources if the rest of the statement is exactly the same.
        - Combine Actions if the rest of the statement is exactly the same.
        - We will never combine NotPrincipals, NotResources or NotActions, because doing
          so would change the meaning of the policy document.

        :default: - false, unless the feature flag ``@aws-cdk/aws-iam:minimizePolicies`` is set
        '''
        result = self._values.get("minimize")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def statements(self) -> typing.Optional[typing.List["PolicyStatement"]]:
        '''Initial statements to add to the policy document.

        :default: - No statements
        '''
        result = self._values.get("statements")
        return typing.cast(typing.Optional[typing.List["PolicyStatement"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PolicyDocumentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.PolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "document": "document",
        "force": "force",
        "groups": "groups",
        "policy_name": "policyName",
        "roles": "roles",
        "statements": "statements",
        "users": "users",
    },
)
class PolicyProps:
    def __init__(
        self,
        *,
        document: typing.Optional[PolicyDocument] = None,
        force: typing.Optional[builtins.bool] = None,
        groups: typing.Optional[typing.Sequence["IGroup"]] = None,
        policy_name: typing.Optional[builtins.str] = None,
        roles: typing.Optional[typing.Sequence["IRole"]] = None,
        statements: typing.Optional[typing.Sequence["PolicyStatement"]] = None,
        users: typing.Optional[typing.Sequence["IUser"]] = None,
    ) -> None:
        '''Properties for defining an IAM inline policy document.

        :param document: Initial PolicyDocument to use for this Policy. If omited, any ``PolicyStatement`` provided in the ``statements`` property will be applied against the empty default ``PolicyDocument``. Default: - An empty policy.
        :param force: Force creation of an ``AWS::IAM::Policy``. Unless set to ``true``, this ``Policy`` construct will not materialize to an ``AWS::IAM::Policy`` CloudFormation resource in case it would have no effect (for example, if it remains unattached to an IAM identity or if it has no statements). This is generally desired behavior, since it prevents creating invalid--and hence undeployable--CloudFormation templates. In cases where you know the policy must be created and it is actually an error if no statements have been added to it or it remains unattached to an IAM identity, you can set this to ``true``. Default: false
        :param groups: Groups to attach this policy to. You can also use ``attachToGroup(group)`` to attach this policy to a group. Default: - No groups.
        :param policy_name: The name of the policy. If you specify multiple policies for an entity, specify unique names. For example, if you specify a list of policies for an IAM role, each policy must have a unique name. Default: - Uses the logical ID of the policy resource, which is ensured to be unique within the stack.
        :param roles: Roles to attach this policy to. You can also use ``attachToRole(role)`` to attach this policy to a role. Default: - No roles.
        :param statements: Initial set of permissions to add to this policy document. You can also use ``addStatements(...statement)`` to add permissions later. Default: - No statements.
        :param users: Users to attach this policy to. You can also use ``attachToUser(user)`` to attach this policy to a user. Default: - No users.

        :exampleMetadata: infused

        Example::

            # books: apigateway.Resource
            # iam_user: iam.User
            
            
            get_books = books.add_method("GET", apigateway.HttpIntegration("http://amazon.com"),
                authorization_type=apigateway.AuthorizationType.IAM
            )
            
            iam_user.attach_inline_policy(iam.Policy(self, "AllowBooks",
                statements=[
                    iam.PolicyStatement(
                        actions=["execute-api:Invoke"],
                        effect=iam.Effect.ALLOW,
                        resources=[get_books.method_arn]
                    )
                ]
            ))
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a119470d7c78e863a14a450dfe2d14dd9454487e93601f2675b2fafe09790c2)
            check_type(argname="argument document", value=document, expected_type=type_hints["document"])
            check_type(argname="argument force", value=force, expected_type=type_hints["force"])
            check_type(argname="argument groups", value=groups, expected_type=type_hints["groups"])
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
            check_type(argname="argument roles", value=roles, expected_type=type_hints["roles"])
            check_type(argname="argument statements", value=statements, expected_type=type_hints["statements"])
            check_type(argname="argument users", value=users, expected_type=type_hints["users"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if document is not None:
            self._values["document"] = document
        if force is not None:
            self._values["force"] = force
        if groups is not None:
            self._values["groups"] = groups
        if policy_name is not None:
            self._values["policy_name"] = policy_name
        if roles is not None:
            self._values["roles"] = roles
        if statements is not None:
            self._values["statements"] = statements
        if users is not None:
            self._values["users"] = users

    @builtins.property
    def document(self) -> typing.Optional[PolicyDocument]:
        '''Initial PolicyDocument to use for this Policy.

        If omited, any
        ``PolicyStatement`` provided in the ``statements`` property will be applied
        against the empty default ``PolicyDocument``.

        :default: - An empty policy.
        '''
        result = self._values.get("document")
        return typing.cast(typing.Optional[PolicyDocument], result)

    @builtins.property
    def force(self) -> typing.Optional[builtins.bool]:
        '''Force creation of an ``AWS::IAM::Policy``.

        Unless set to ``true``, this ``Policy`` construct will not materialize to an
        ``AWS::IAM::Policy`` CloudFormation resource in case it would have no effect
        (for example, if it remains unattached to an IAM identity or if it has no
        statements). This is generally desired behavior, since it prevents
        creating invalid--and hence undeployable--CloudFormation templates.

        In cases where you know the policy must be created and it is actually
        an error if no statements have been added to it or it remains unattached to
        an IAM identity, you can set this to ``true``.

        :default: false
        '''
        result = self._values.get("force")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def groups(self) -> typing.Optional[typing.List["IGroup"]]:
        '''Groups to attach this policy to.

        You can also use ``attachToGroup(group)`` to attach this policy to a group.

        :default: - No groups.
        '''
        result = self._values.get("groups")
        return typing.cast(typing.Optional[typing.List["IGroup"]], result)

    @builtins.property
    def policy_name(self) -> typing.Optional[builtins.str]:
        '''The name of the policy.

        If you specify multiple policies for an entity,
        specify unique names. For example, if you specify a list of policies for
        an IAM role, each policy must have a unique name.

        :default:

        - Uses the logical ID of the policy resource, which is ensured
        to be unique within the stack.
        '''
        result = self._values.get("policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def roles(self) -> typing.Optional[typing.List["IRole"]]:
        '''Roles to attach this policy to.

        You can also use ``attachToRole(role)`` to attach this policy to a role.

        :default: - No roles.
        '''
        result = self._values.get("roles")
        return typing.cast(typing.Optional[typing.List["IRole"]], result)

    @builtins.property
    def statements(self) -> typing.Optional[typing.List["PolicyStatement"]]:
        '''Initial set of permissions to add to this policy document.

        You can also use ``addStatements(...statement)`` to add permissions later.

        :default: - No statements.
        '''
        result = self._values.get("statements")
        return typing.cast(typing.Optional[typing.List["PolicyStatement"]], result)

    @builtins.property
    def users(self) -> typing.Optional[typing.List["IUser"]]:
        '''Users to attach this policy to.

        You can also use ``attachToUser(user)`` to attach this policy to a user.

        :default: - No users.
        '''
        result = self._values.get("users")
        return typing.cast(typing.Optional[typing.List["IUser"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PolicyStatement(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.PolicyStatement",
):
    '''Represents a statement in an IAM policy document.

    :exampleMetadata: infused

    Example::

        # destination_bucket: s3.Bucket
        
        
        deployment = s3deploy.BucketDeployment(self, "DeployFiles",
            sources=[s3deploy.Source.asset(path.join(__dirname, "source-files"))],
            destination_bucket=destination_bucket
        )
        
        deployment.handler_role.add_to_policy(
            iam.PolicyStatement(
                actions=["kms:Decrypt", "kms:DescribeKey"],
                effect=iam.Effect.ALLOW,
                resources=["<encryption key ARN>"]
            ))
    '''

    def __init__(
        self,
        *,
        actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        conditions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        effect: typing.Optional[Effect] = None,
        not_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        not_principals: typing.Optional[typing.Sequence[IPrincipal]] = None,
        not_resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        principals: typing.Optional[typing.Sequence[IPrincipal]] = None,
        resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        sid: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param actions: List of actions to add to the statement. Default: - no actions
        :param conditions: Conditions to add to the statement. Default: - no condition
        :param effect: Whether to allow or deny the actions in this statement. Default: Effect.ALLOW
        :param not_actions: List of not actions to add to the statement. Default: - no not-actions
        :param not_principals: List of not principals to add to the statement. Default: - no not principals
        :param not_resources: NotResource ARNs to add to the statement. Default: - no not-resources
        :param principals: List of principals to add to the statement. Default: - no principals
        :param resources: Resource ARNs to add to the statement. Default: - no resources
        :param sid: The Sid (statement ID) is an optional identifier that you provide for the policy statement. You can assign a Sid value to each statement in a statement array. In services that let you specify an ID element, such as SQS and SNS, the Sid value is just a sub-ID of the policy document's ID. In IAM, the Sid value must be unique within a JSON policy. Default: - no sid
        '''
        props = PolicyStatementProps(
            actions=actions,
            conditions=conditions,
            effect=effect,
            not_actions=not_actions,
            not_principals=not_principals,
            not_resources=not_resources,
            principals=principals,
            resources=resources,
            sid=sid,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="fromJson")
    @builtins.classmethod
    def from_json(cls, obj: typing.Any) -> "PolicyStatement":
        '''Creates a new PolicyStatement based on the object provided.

        This will accept an object created from the ``.toJSON()`` call

        :param obj: the PolicyStatement in object form.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3310dd221a31143a87ae81db4017dcad81b1a99d3d920f2184101ed8e7186455)
            check_type(argname="argument obj", value=obj, expected_type=type_hints["obj"])
        return typing.cast("PolicyStatement", jsii.sinvoke(cls, "fromJson", [obj]))

    @jsii.member(jsii_name="addAccountCondition")
    def add_account_condition(self, account_id: builtins.str) -> None:
        '''Add a ``StringEquals`` condition that limits to a given account from ``sts:ExternalId``.

        This method can only be called once: subsequent calls will overwrite earlier calls.

        :param account_id: -

        :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__709bd112516bbfd3a8db442420a90bf80eae4cfd2a7d514a5612c6b3a447720c)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        return typing.cast(None, jsii.invoke(self, "addAccountCondition", [account_id]))

    @jsii.member(jsii_name="addAccountRootPrincipal")
    def add_account_root_principal(self) -> None:
        '''Adds an AWS account root user principal to this policy statement.'''
        return typing.cast(None, jsii.invoke(self, "addAccountRootPrincipal", []))

    @jsii.member(jsii_name="addActions")
    def add_actions(self, *actions: builtins.str) -> None:
        '''Specify allowed actions into the "Action" section of the policy statement.

        :param actions: actions that will be allowed.

        :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_action.html
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7570c3287006f9128c65d62789b1ef89599fe16f2b3a738f83cb5fa00aac1beb)
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addActions", [*actions]))

    @jsii.member(jsii_name="addAllResources")
    def add_all_resources(self) -> None:
        '''Adds a ``"*"`` resource to this statement.'''
        return typing.cast(None, jsii.invoke(self, "addAllResources", []))

    @jsii.member(jsii_name="addAnyPrincipal")
    def add_any_principal(self) -> None:
        '''Adds all identities in all accounts ("*") to this policy statement.'''
        return typing.cast(None, jsii.invoke(self, "addAnyPrincipal", []))

    @jsii.member(jsii_name="addArnPrincipal")
    def add_arn_principal(self, arn: builtins.str) -> None:
        '''Specify a principal using the ARN  identifier of the principal.

        You cannot specify IAM groups and instance profiles as principals.

        :param arn: ARN identifier of AWS account, IAM user, or IAM role (i.e. arn:aws:iam::123456789012:user/user-name).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__753e936d4d13cab9c5aa2f61d42cab848105cd421cf5e5027b920d5ad7ca0fdf)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
        return typing.cast(None, jsii.invoke(self, "addArnPrincipal", [arn]))

    @jsii.member(jsii_name="addAwsAccountPrincipal")
    def add_aws_account_principal(self, account_id: builtins.str) -> None:
        '''Specify AWS account ID as the principal entity to the "Principal" section of a policy statement.

        :param account_id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e93c2a641b144f46ca61b524c40ddbae1d4b77b9640fa4996e816f445d8f6edd)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        return typing.cast(None, jsii.invoke(self, "addAwsAccountPrincipal", [account_id]))

    @jsii.member(jsii_name="addCanonicalUserPrincipal")
    def add_canonical_user_principal(self, canonical_user_id: builtins.str) -> None:
        '''Adds a canonical user ID principal to this policy document.

        :param canonical_user_id: unique identifier assigned by AWS for every account.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__344be87a6a10a3974e50790a68d361cd386fe620caf5baa8dae7ef6f97881c28)
            check_type(argname="argument canonical_user_id", value=canonical_user_id, expected_type=type_hints["canonical_user_id"])
        return typing.cast(None, jsii.invoke(self, "addCanonicalUserPrincipal", [canonical_user_id]))

    @jsii.member(jsii_name="addCondition")
    def add_condition(self, key: builtins.str, value: typing.Any) -> None:
        '''Add a condition to the Policy.

        If multiple calls are made to add a condition with the same operator and field, only
        the last one wins. For example::

           # stmt: iam.PolicyStatement


           stmt.add_condition("StringEquals", {"aws:SomeField": "1"})
           stmt.add_condition("StringEquals", {"aws:SomeField": "2"})

        Will end up with the single condition ``StringEquals: { 'aws:SomeField': '2' }``.

        If you meant to add a condition to say that the field can be *either* ``1`` or ``2``, write
        this::

           # stmt: iam.PolicyStatement


           stmt.add_condition("StringEquals", {"aws:SomeField": ["1", "2"]})

        :param key: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db59aa35431ad83b8fa7e1c45f11c92108f81ccef5b7baab7a37414280719862)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "addCondition", [key, value]))

    @jsii.member(jsii_name="addConditions")
    def add_conditions(
        self,
        conditions: typing.Mapping[builtins.str, typing.Any],
    ) -> None:
        '''Add multiple conditions to the Policy.

        See the ``addCondition`` function for a caveat on calling this method multiple times.

        :param conditions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f76cf4da6bbc6e1cb542b1c4034ab81599d83ce4800b0a288a241ba0d4ac6ee)
            check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
        return typing.cast(None, jsii.invoke(self, "addConditions", [conditions]))

    @jsii.member(jsii_name="addFederatedPrincipal")
    def add_federated_principal(
        self,
        federated: typing.Any,
        conditions: typing.Mapping[builtins.str, typing.Any],
    ) -> None:
        '''Adds a federated identity provider such as Amazon Cognito to this policy statement.

        :param federated: federated identity provider (i.e. 'cognito-identity.amazonaws.com').
        :param conditions: The conditions under which the policy is in effect. See `the IAM documentation <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html>`_.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ee9dcc2ed7fe994d44a076dc07c103db4407fcda32a738035feb148a22879ba)
            check_type(argname="argument federated", value=federated, expected_type=type_hints["federated"])
            check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
        return typing.cast(None, jsii.invoke(self, "addFederatedPrincipal", [federated, conditions]))

    @jsii.member(jsii_name="addNotActions")
    def add_not_actions(self, *not_actions: builtins.str) -> None:
        '''Explicitly allow all actions except the specified list of actions into the "NotAction" section of the policy document.

        :param not_actions: actions that will be denied. All other actions will be permitted.

        :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_notaction.html
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b6b4424bff8556b7a98dfced6db44392158d11177b9f964fe1cb0cfb4532f85)
            check_type(argname="argument not_actions", value=not_actions, expected_type=typing.Tuple[type_hints["not_actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addNotActions", [*not_actions]))

    @jsii.member(jsii_name="addNotPrincipals")
    def add_not_principals(self, *not_principals: IPrincipal) -> None:
        '''Specify principals that is not allowed or denied access to the "NotPrincipal" section of a policy statement.

        :param not_principals: IAM principals that will be denied access.

        :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_notprincipal.html
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3b9cc21ab5c593c77deae20933faab5861db2f155f8bf91ced6fe1a382e51ba)
            check_type(argname="argument not_principals", value=not_principals, expected_type=typing.Tuple[type_hints["not_principals"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addNotPrincipals", [*not_principals]))

    @jsii.member(jsii_name="addNotResources")
    def add_not_resources(self, *arns: builtins.str) -> None:
        '''Specify resources that this policy statement will not apply to in the "NotResource" section of this policy statement.

        All resources except the specified list will be matched.

        :param arns: Amazon Resource Names (ARNs) of the resources that this policy statement does not apply to.

        :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_notresource.html
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b596ffa85ab5014633dac1d25489acd42c736f41cdba62b050ca048610a83ed2)
            check_type(argname="argument arns", value=arns, expected_type=typing.Tuple[type_hints["arns"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addNotResources", [*arns]))

    @jsii.member(jsii_name="addPrincipals")
    def add_principals(self, *principals: IPrincipal) -> None:
        '''Adds principals to the "Principal" section of a policy statement.

        :param principals: IAM principals that will be added.

        :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1783e9c91d9c307df264cec637ef147b4aa30b973ac302ab19a9f486211719bf)
            check_type(argname="argument principals", value=principals, expected_type=typing.Tuple[type_hints["principals"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addPrincipals", [*principals]))

    @jsii.member(jsii_name="addResources")
    def add_resources(self, *arns: builtins.str) -> None:
        '''Specify resources that this policy statement applies into the "Resource" section of this policy statement.

        :param arns: Amazon Resource Names (ARNs) of the resources that this policy statement applies to.

        :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_resource.html
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__feb2cb778edcb3c0b9cafd7458f0c6d0481e45f9d827da0b859be3f4f30d6393)
            check_type(argname="argument arns", value=arns, expected_type=typing.Tuple[type_hints["arns"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addResources", [*arns]))

    @jsii.member(jsii_name="addServicePrincipal")
    def add_service_principal(
        self,
        service: builtins.str,
        *,
        conditions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Adds a service principal to this policy statement.

        :param service: the service name for which a service principal is requested (e.g: ``s3.amazonaws.com``).
        :param conditions: Additional conditions to add to the Service Principal. Default: - No conditions
        :param region: The region in which you want to reference the service. This is only necessary for *cross-region* references to *opt-in* regions. In those cases, the region name needs to be included to reference the correct service principal. In all other cases, the global service principal name is sufficient. This field behaves differently depending on whether the ``@aws-cdk/aws-iam:standardizedServicePrincipals`` flag is set or not: - If the flag is set, the input service principal is assumed to be of the form ``SERVICE.amazonaws.com``. That value will always be returned, unless the given region is an opt-in region and the service principal is rendered in a stack in a different region, in which case ``SERVICE.REGION.amazonaws.com`` will be rendered. Under this regime, there is no downside to always specifying the region property: it will be rendered only if necessary. - If the flag is not set, the service principal will resolve to a single principal whose name comes from the ``@aws-cdk/region-info`` package, using the region to override the stack region. If there is no entry for this service principal in the database,, the input service name is returned literally. This is legacy behavior and is not recommended. Default: - the resolving Stack's region.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd372f80873e5e30ce5cf291cd80c7ce500c12643cde076cf4ddfbc1c05faea5)
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
        opts = ServicePrincipalOpts(conditions=conditions, region=region)

        return typing.cast(None, jsii.invoke(self, "addServicePrincipal", [service, opts]))

    @jsii.member(jsii_name="addSourceAccountCondition")
    def add_source_account_condition(self, account_id: builtins.str) -> None:
        '''Add an ``StringEquals`` condition that limits to a given account from ``aws:SourceAccount``.

        This method can only be called once: subsequent calls will overwrite earlier calls.

        :param account_id: -

        :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceaccount
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b4744c164be6f567bdcb8f9b4c6dd9ee9ed642a926a6200c6fcb6735c3499e4)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        return typing.cast(None, jsii.invoke(self, "addSourceAccountCondition", [account_id]))

    @jsii.member(jsii_name="addSourceArnCondition")
    def add_source_arn_condition(self, arn: builtins.str) -> None:
        '''Add an ``ArnEquals`` condition that limits to a given resource arn from ``aws:SourceArn``.

        This method can only be called once: subsequent calls will overwrite earlier calls.

        :param arn: -

        :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e49097a84ad9a7af8121131935195997223c04f9d2b394c9d8f88a9f6446dc9b)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
        return typing.cast(None, jsii.invoke(self, "addSourceArnCondition", [arn]))

    @jsii.member(jsii_name="copy")
    def copy(
        self,
        *,
        actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        conditions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        effect: typing.Optional[Effect] = None,
        not_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        not_principals: typing.Optional[typing.Sequence[IPrincipal]] = None,
        not_resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        principals: typing.Optional[typing.Sequence[IPrincipal]] = None,
        resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        sid: typing.Optional[builtins.str] = None,
    ) -> "PolicyStatement":
        '''Create a new ``PolicyStatement`` with the same exact properties as this one, except for the overrides.

        :param actions: List of actions to add to the statement. Default: - no actions
        :param conditions: Conditions to add to the statement. Default: - no condition
        :param effect: Whether to allow or deny the actions in this statement. Default: Effect.ALLOW
        :param not_actions: List of not actions to add to the statement. Default: - no not-actions
        :param not_principals: List of not principals to add to the statement. Default: - no not principals
        :param not_resources: NotResource ARNs to add to the statement. Default: - no not-resources
        :param principals: List of principals to add to the statement. Default: - no principals
        :param resources: Resource ARNs to add to the statement. Default: - no resources
        :param sid: The Sid (statement ID) is an optional identifier that you provide for the policy statement. You can assign a Sid value to each statement in a statement array. In services that let you specify an ID element, such as SQS and SNS, the Sid value is just a sub-ID of the policy document's ID. In IAM, the Sid value must be unique within a JSON policy. Default: - no sid
        '''
        overrides = PolicyStatementProps(
            actions=actions,
            conditions=conditions,
            effect=effect,
            not_actions=not_actions,
            not_principals=not_principals,
            not_resources=not_resources,
            principals=principals,
            resources=resources,
            sid=sid,
        )

        return typing.cast("PolicyStatement", jsii.invoke(self, "copy", [overrides]))

    @jsii.member(jsii_name="freeze")
    def freeze(self) -> "PolicyStatement":
        '''Make the PolicyStatement immutable.

        After calling this, any of the ``addXxx()`` methods will throw an exception.

        Libraries that lazily generate statement bodies can override this method to
        fill the actual PolicyStatement fields. Be aware that this method may be called
        multiple times.
        '''
        return typing.cast("PolicyStatement", jsii.invoke(self, "freeze", []))

    @jsii.member(jsii_name="toJSON")
    def to_json(self) -> typing.Any:
        '''JSON-ify the statement.

        Used when JSON.stringify() is called
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "toJSON", []))

    @jsii.member(jsii_name="toStatementJson")
    def to_statement_json(self) -> typing.Any:
        '''JSON-ify the policy statement.

        Used when JSON.stringify() is called
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "toStatementJson", []))

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''String representation of this policy statement.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @jsii.member(jsii_name="validateForAnyPolicy")
    def validate_for_any_policy(self) -> typing.List[builtins.str]:
        '''Validate that the policy statement satisfies base requirements for a policy.

        :return: An array of validation error messages, or an empty array if the statement is valid.
        '''
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "validateForAnyPolicy", []))

    @jsii.member(jsii_name="validateForIdentityPolicy")
    def validate_for_identity_policy(self) -> typing.List[builtins.str]:
        '''Validate that the policy statement satisfies all requirements for an identity-based policy.

        :return: An array of validation error messages, or an empty array if the statement is valid.
        '''
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "validateForIdentityPolicy", []))

    @jsii.member(jsii_name="validateForResourcePolicy")
    def validate_for_resource_policy(self) -> typing.List[builtins.str]:
        '''Validate that the policy statement satisfies all requirements for a resource-based policy.

        :return: An array of validation error messages, or an empty array if the statement is valid.
        '''
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "validateForResourcePolicy", []))

    @builtins.property
    @jsii.member(jsii_name="actions")
    def actions(self) -> typing.List[builtins.str]:
        '''The Actions added to this statement.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "actions"))

    @builtins.property
    @jsii.member(jsii_name="conditions")
    def conditions(self) -> typing.Any:
        '''The conditions added to this statement.'''
        return typing.cast(typing.Any, jsii.get(self, "conditions"))

    @builtins.property
    @jsii.member(jsii_name="frozen")
    def frozen(self) -> builtins.bool:
        '''Whether the PolicyStatement has been frozen.

        The statement object is frozen when ``freeze()`` is called.
        '''
        return typing.cast(builtins.bool, jsii.get(self, "frozen"))

    @builtins.property
    @jsii.member(jsii_name="hasPrincipal")
    def has_principal(self) -> builtins.bool:
        '''Indicates if this permission has a "Principal" section.'''
        return typing.cast(builtins.bool, jsii.get(self, "hasPrincipal"))

    @builtins.property
    @jsii.member(jsii_name="hasResource")
    def has_resource(self) -> builtins.bool:
        '''Indicates if this permission has at least one resource associated with it.'''
        return typing.cast(builtins.bool, jsii.get(self, "hasResource"))

    @builtins.property
    @jsii.member(jsii_name="notActions")
    def not_actions(self) -> typing.List[builtins.str]:
        '''The NotActions added to this statement.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "notActions"))

    @builtins.property
    @jsii.member(jsii_name="notPrincipals")
    def not_principals(self) -> typing.List[IPrincipal]:
        '''The NotPrincipals added to this statement.'''
        return typing.cast(typing.List[IPrincipal], jsii.get(self, "notPrincipals"))

    @builtins.property
    @jsii.member(jsii_name="notResources")
    def not_resources(self) -> typing.List[builtins.str]:
        '''The NotResources added to this statement.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "notResources"))

    @builtins.property
    @jsii.member(jsii_name="principals")
    def principals(self) -> typing.List[IPrincipal]:
        '''The Principals added to this statement.'''
        return typing.cast(typing.List[IPrincipal], jsii.get(self, "principals"))

    @builtins.property
    @jsii.member(jsii_name="resources")
    def resources(self) -> typing.List[builtins.str]:
        '''The Resources added to this statement.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resources"))

    @builtins.property
    @jsii.member(jsii_name="effect")
    def effect(self) -> Effect:
        '''Whether to allow or deny the actions in this statement Set effect for this statement.'''
        return typing.cast(Effect, jsii.get(self, "effect"))

    @effect.setter
    def effect(self, value: Effect) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0938212412c89f00c92be30674976489815687ff4590eef7d1e3a8d2b3605ff1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "effect", value)

    @builtins.property
    @jsii.member(jsii_name="sid")
    def sid(self) -> typing.Optional[builtins.str]:
        '''Statement ID for this statement Set Statement ID for this statement.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sid"))

    @sid.setter
    def sid(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ad1bd9e071f1c20bcba127bf551d42076cff1e619eeeecfffabbcefe7b69818)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sid", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.PolicyStatementProps",
    jsii_struct_bases=[],
    name_mapping={
        "actions": "actions",
        "conditions": "conditions",
        "effect": "effect",
        "not_actions": "notActions",
        "not_principals": "notPrincipals",
        "not_resources": "notResources",
        "principals": "principals",
        "resources": "resources",
        "sid": "sid",
    },
)
class PolicyStatementProps:
    def __init__(
        self,
        *,
        actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        conditions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        effect: typing.Optional[Effect] = None,
        not_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        not_principals: typing.Optional[typing.Sequence[IPrincipal]] = None,
        not_resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        principals: typing.Optional[typing.Sequence[IPrincipal]] = None,
        resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        sid: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Interface for creating a policy statement.

        :param actions: List of actions to add to the statement. Default: - no actions
        :param conditions: Conditions to add to the statement. Default: - no condition
        :param effect: Whether to allow or deny the actions in this statement. Default: Effect.ALLOW
        :param not_actions: List of not actions to add to the statement. Default: - no not-actions
        :param not_principals: List of not principals to add to the statement. Default: - no not principals
        :param not_resources: NotResource ARNs to add to the statement. Default: - no not-resources
        :param principals: List of principals to add to the statement. Default: - no principals
        :param resources: Resource ARNs to add to the statement. Default: - no resources
        :param sid: The Sid (statement ID) is an optional identifier that you provide for the policy statement. You can assign a Sid value to each statement in a statement array. In services that let you specify an ID element, such as SQS and SNS, the Sid value is just a sub-ID of the policy document's ID. In IAM, the Sid value must be unique within a JSON policy. Default: - no sid

        :exampleMetadata: infused

        Example::

            # destination_bucket: s3.Bucket
            
            
            deployment = s3deploy.BucketDeployment(self, "DeployFiles",
                sources=[s3deploy.Source.asset(path.join(__dirname, "source-files"))],
                destination_bucket=destination_bucket
            )
            
            deployment.handler_role.add_to_policy(
                iam.PolicyStatement(
                    actions=["kms:Decrypt", "kms:DescribeKey"],
                    effect=iam.Effect.ALLOW,
                    resources=["<encryption key ARN>"]
                ))
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1307ab5f5dd84b7184f36603f7af026efb2798812c35c96dbe60552fff14c3b)
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
            check_type(argname="argument effect", value=effect, expected_type=type_hints["effect"])
            check_type(argname="argument not_actions", value=not_actions, expected_type=type_hints["not_actions"])
            check_type(argname="argument not_principals", value=not_principals, expected_type=type_hints["not_principals"])
            check_type(argname="argument not_resources", value=not_resources, expected_type=type_hints["not_resources"])
            check_type(argname="argument principals", value=principals, expected_type=type_hints["principals"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
            check_type(argname="argument sid", value=sid, expected_type=type_hints["sid"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if actions is not None:
            self._values["actions"] = actions
        if conditions is not None:
            self._values["conditions"] = conditions
        if effect is not None:
            self._values["effect"] = effect
        if not_actions is not None:
            self._values["not_actions"] = not_actions
        if not_principals is not None:
            self._values["not_principals"] = not_principals
        if not_resources is not None:
            self._values["not_resources"] = not_resources
        if principals is not None:
            self._values["principals"] = principals
        if resources is not None:
            self._values["resources"] = resources
        if sid is not None:
            self._values["sid"] = sid

    @builtins.property
    def actions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of actions to add to the statement.

        :default: - no actions
        '''
        result = self._values.get("actions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def conditions(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Conditions to add to the statement.

        :default: - no condition
        '''
        result = self._values.get("conditions")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def effect(self) -> typing.Optional[Effect]:
        '''Whether to allow or deny the actions in this statement.

        :default: Effect.ALLOW
        '''
        result = self._values.get("effect")
        return typing.cast(typing.Optional[Effect], result)

    @builtins.property
    def not_actions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of not actions to add to the statement.

        :default: - no not-actions
        '''
        result = self._values.get("not_actions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def not_principals(self) -> typing.Optional[typing.List[IPrincipal]]:
        '''List of not principals to add to the statement.

        :default: - no not principals
        '''
        result = self._values.get("not_principals")
        return typing.cast(typing.Optional[typing.List[IPrincipal]], result)

    @builtins.property
    def not_resources(self) -> typing.Optional[typing.List[builtins.str]]:
        '''NotResource ARNs to add to the statement.

        :default: - no not-resources
        '''
        result = self._values.get("not_resources")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def principals(self) -> typing.Optional[typing.List[IPrincipal]]:
        '''List of principals to add to the statement.

        :default: - no principals
        '''
        result = self._values.get("principals")
        return typing.cast(typing.Optional[typing.List[IPrincipal]], result)

    @builtins.property
    def resources(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Resource ARNs to add to the statement.

        :default: - no resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def sid(self) -> typing.Optional[builtins.str]:
        '''The Sid (statement ID) is an optional identifier that you provide for the policy statement.

        You can assign a Sid value to each statement in a
        statement array. In services that let you specify an ID element, such as
        SQS and SNS, the Sid value is just a sub-ID of the policy document's ID. In
        IAM, the Sid value must be unique within a JSON policy.

        :default: - no sid
        '''
        result = self._values.get("sid")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PolicyStatementProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PrincipalPolicyFragment(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.PrincipalPolicyFragment",
):
    '''A collection of the fields in a PolicyStatement that can be used to identify a principal.

    This consists of the JSON used in the "Principal" field, and optionally a
    set of "Condition"s that need to be applied to the policy.

    Generally, a principal looks like::

       { '<TYPE>': ['ID', 'ID', ...] }

    And this is also the type of the field ``principalJson``.  However, there is a
    special type of principal that is just the string '*', which is treated
    differently by some services. To represent that principal, ``principalJson``
    should contain ``{ 'LiteralString': ['*'] }``.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iam as iam
        
        # conditions: Any
        
        principal_policy_fragment = iam.PrincipalPolicyFragment({
            "principal_json_key": ["principalJson"]
        }, {
            "conditions_key": conditions
        })
    '''

    def __init__(
        self,
        principal_json: typing.Mapping[builtins.str, typing.Sequence[builtins.str]],
        conditions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param principal_json: JSON of the "Principal" section in a policy statement.
        :param conditions: The conditions under which the policy is in effect. See `the IAM documentation <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html>`_. conditions that need to be applied to this policy
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__278426b331a0d887bf9449f77f6f9c562033abef58a3d7279c5604a1e1c928ea)
            check_type(argname="argument principal_json", value=principal_json, expected_type=type_hints["principal_json"])
            check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
        jsii.create(self.__class__, self, [principal_json, conditions])

    @builtins.property
    @jsii.member(jsii_name="conditions")
    def conditions(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''The conditions under which the policy is in effect.

        See `the IAM documentation <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html>`_.
        conditions that need to be applied to this policy
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "conditions"))

    @builtins.property
    @jsii.member(jsii_name="principalJson")
    def principal_json(self) -> typing.Mapping[builtins.str, typing.List[builtins.str]]:
        '''JSON of the "Principal" section in a policy statement.'''
        return typing.cast(typing.Mapping[builtins.str, typing.List[builtins.str]], jsii.get(self, "principalJson"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.RoleProps",
    jsii_struct_bases=[],
    name_mapping={
        "assumed_by": "assumedBy",
        "description": "description",
        "external_ids": "externalIds",
        "inline_policies": "inlinePolicies",
        "managed_policies": "managedPolicies",
        "max_session_duration": "maxSessionDuration",
        "path": "path",
        "permissions_boundary": "permissionsBoundary",
        "role_name": "roleName",
    },
)
class RoleProps:
    def __init__(
        self,
        *,
        assumed_by: IPrincipal,
        description: typing.Optional[builtins.str] = None,
        external_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        inline_policies: typing.Optional[typing.Mapping[builtins.str, PolicyDocument]] = None,
        managed_policies: typing.Optional[typing.Sequence[IManagedPolicy]] = None,
        max_session_duration: typing.Optional[_Duration_4839e8c3] = None,
        path: typing.Optional[builtins.str] = None,
        permissions_boundary: typing.Optional[IManagedPolicy] = None,
        role_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining an IAM Role.

        :param assumed_by: The IAM principal (i.e. ``new ServicePrincipal('sns.amazonaws.com')``) which can assume this role. You can later modify the assume role policy document by accessing it via the ``assumeRolePolicy`` property.
        :param description: A description of the role. It can be up to 1000 characters long. Default: - No description.
        :param external_ids: List of IDs that the role assumer needs to provide one of when assuming this role. If the configured and provided external IDs do not match, the AssumeRole operation will fail. Default: No external ID required
        :param inline_policies: A list of named policies to inline into this role. These policies will be created with the role, whereas those added by ``addToPolicy`` are added using a separate CloudFormation resource (allowing a way around circular dependencies that could otherwise be introduced). Default: - No policy is inlined in the Role resource.
        :param managed_policies: A list of managed policies associated with this role. You can add managed policies later using ``addManagedPolicy(ManagedPolicy.fromAwsManagedPolicyName(policyName))``. Default: - No managed policies.
        :param max_session_duration: The maximum session duration that you want to set for the specified role. This setting can have a value from 1 hour (3600sec) to 12 (43200sec) hours. Anyone who assumes the role from the AWS CLI or API can use the DurationSeconds API parameter or the duration-seconds CLI parameter to request a longer session. The MaxSessionDuration setting determines the maximum duration that can be requested using the DurationSeconds parameter. If users don't specify a value for the DurationSeconds parameter, their security credentials are valid for one hour by default. This applies when you use the AssumeRole* API operations or the assume-role* CLI operations but does not apply when you use those operations to create a console URL. Default: Duration.hours(1)
        :param path: The path associated with this role. For information about IAM paths, see Friendly Names and Paths in IAM User Guide. Default: /
        :param permissions_boundary: AWS supports permissions boundaries for IAM entities (users or roles). A permissions boundary is an advanced feature for using a managed policy to set the maximum permissions that an identity-based policy can grant to an IAM entity. An entity's permissions boundary allows it to perform only the actions that are allowed by both its identity-based policies and its permissions boundaries. Default: - No permissions boundary.
        :param role_name: A name for the IAM role. For valid values, see the RoleName parameter for the CreateRole action in the IAM API Reference. IMPORTANT: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name. If you specify a name, you must specify the CAPABILITY_NAMED_IAM value to acknowledge your template's capabilities. For more information, see Acknowledging IAM Resources in AWS CloudFormation Templates. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the role name.

        :exampleMetadata: infused

        Example::

            # Option 3: Create a new role that allows the account root principal to assume. Add this role in the `system:masters` and witch to this role from the AWS console.
            # cluster: eks.Cluster
            
            
            console_read_only_role = iam.Role(self, "ConsoleReadOnlyRole",
                assumed_by=iam.ArnPrincipal("arn_for_trusted_principal")
            )
            console_read_only_role.add_to_policy(iam.PolicyStatement(
                actions=["eks:AccessKubernetesApi", "eks:Describe*", "eks:List*"
                ],
                resources=[cluster.cluster_arn]
            ))
            
            # Add this role to system:masters RBAC group
            cluster.aws_auth.add_masters_role(console_read_only_role)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c9223cb9fa6dff45ee4fd7013629ab18542c2499a83f542c5405968fad2287c)
            check_type(argname="argument assumed_by", value=assumed_by, expected_type=type_hints["assumed_by"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument external_ids", value=external_ids, expected_type=type_hints["external_ids"])
            check_type(argname="argument inline_policies", value=inline_policies, expected_type=type_hints["inline_policies"])
            check_type(argname="argument managed_policies", value=managed_policies, expected_type=type_hints["managed_policies"])
            check_type(argname="argument max_session_duration", value=max_session_duration, expected_type=type_hints["max_session_duration"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument permissions_boundary", value=permissions_boundary, expected_type=type_hints["permissions_boundary"])
            check_type(argname="argument role_name", value=role_name, expected_type=type_hints["role_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "assumed_by": assumed_by,
        }
        if description is not None:
            self._values["description"] = description
        if external_ids is not None:
            self._values["external_ids"] = external_ids
        if inline_policies is not None:
            self._values["inline_policies"] = inline_policies
        if managed_policies is not None:
            self._values["managed_policies"] = managed_policies
        if max_session_duration is not None:
            self._values["max_session_duration"] = max_session_duration
        if path is not None:
            self._values["path"] = path
        if permissions_boundary is not None:
            self._values["permissions_boundary"] = permissions_boundary
        if role_name is not None:
            self._values["role_name"] = role_name

    @builtins.property
    def assumed_by(self) -> IPrincipal:
        '''The IAM principal (i.e. ``new ServicePrincipal('sns.amazonaws.com')``) which can assume this role.

        You can later modify the assume role policy document by accessing it via
        the ``assumeRolePolicy`` property.
        '''
        result = self._values.get("assumed_by")
        assert result is not None, "Required property 'assumed_by' is missing"
        return typing.cast(IPrincipal, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the role.

        It can be up to 1000 characters long.

        :default: - No description.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def external_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of IDs that the role assumer needs to provide one of when assuming this role.

        If the configured and provided external IDs do not match, the
        AssumeRole operation will fail.

        :default: No external ID required
        '''
        result = self._values.get("external_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def inline_policies(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, PolicyDocument]]:
        '''A list of named policies to inline into this role.

        These policies will be
        created with the role, whereas those added by ``addToPolicy`` are added
        using a separate CloudFormation resource (allowing a way around circular
        dependencies that could otherwise be introduced).

        :default: - No policy is inlined in the Role resource.
        '''
        result = self._values.get("inline_policies")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, PolicyDocument]], result)

    @builtins.property
    def managed_policies(self) -> typing.Optional[typing.List[IManagedPolicy]]:
        '''A list of managed policies associated with this role.

        You can add managed policies later using
        ``addManagedPolicy(ManagedPolicy.fromAwsManagedPolicyName(policyName))``.

        :default: - No managed policies.
        '''
        result = self._values.get("managed_policies")
        return typing.cast(typing.Optional[typing.List[IManagedPolicy]], result)

    @builtins.property
    def max_session_duration(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The maximum session duration that you want to set for the specified role.

        This setting can have a value from 1 hour (3600sec) to 12 (43200sec) hours.

        Anyone who assumes the role from the AWS CLI or API can use the
        DurationSeconds API parameter or the duration-seconds CLI parameter to
        request a longer session. The MaxSessionDuration setting determines the
        maximum duration that can be requested using the DurationSeconds
        parameter.

        If users don't specify a value for the DurationSeconds parameter, their
        security credentials are valid for one hour by default. This applies when
        you use the AssumeRole* API operations or the assume-role* CLI operations
        but does not apply when you use those operations to create a console URL.

        :default: Duration.hours(1)

        :link: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html
        '''
        result = self._values.get("max_session_duration")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''The path associated with this role.

        For information about IAM paths, see
        Friendly Names and Paths in IAM User Guide.

        :default: /
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permissions_boundary(self) -> typing.Optional[IManagedPolicy]:
        '''AWS supports permissions boundaries for IAM entities (users or roles).

        A permissions boundary is an advanced feature for using a managed policy
        to set the maximum permissions that an identity-based policy can grant to
        an IAM entity. An entity's permissions boundary allows it to perform only
        the actions that are allowed by both its identity-based policies and its
        permissions boundaries.

        :default: - No permissions boundary.

        :link: https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html
        '''
        result = self._values.get("permissions_boundary")
        return typing.cast(typing.Optional[IManagedPolicy], result)

    @builtins.property
    def role_name(self) -> typing.Optional[builtins.str]:
        '''A name for the IAM role.

        For valid values, see the RoleName parameter for
        the CreateRole action in the IAM API Reference.

        IMPORTANT: If you specify a name, you cannot perform updates that require
        replacement of this resource. You can perform updates that require no or
        some interruption. If you must replace the resource, specify a new name.

        If you specify a name, you must specify the CAPABILITY_NAMED_IAM value to
        acknowledge your template's capabilities. For more information, see
        Acknowledging IAM Resources in AWS CloudFormation Templates.

        :default:

        - AWS CloudFormation generates a unique physical ID and uses that ID
        for the role name.
        '''
        result = self._values.get("role_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RoleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SamlMetadataDocument(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_iam.SamlMetadataDocument",
):
    '''A SAML metadata document.

    :exampleMetadata: infused

    Example::

        provider = iam.SamlProvider(self, "Provider",
            metadata_document=iam.SamlMetadataDocument.from_file("/path/to/saml-metadata-document.xml")
        )
        principal = iam.SamlPrincipal(provider, {
            "StringEquals": {
                "SAML:iss": "issuer"
            }
        })
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="fromFile")
    @builtins.classmethod
    def from_file(cls, path: builtins.str) -> "SamlMetadataDocument":
        '''Create a SAML metadata document from a XML file.

        :param path: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91316381005170938f0843dfc46ecd2dcd5bff5e8a02bd3f549257a6766268ec)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        return typing.cast("SamlMetadataDocument", jsii.sinvoke(cls, "fromFile", [path]))

    @jsii.member(jsii_name="fromXml")
    @builtins.classmethod
    def from_xml(cls, xml: builtins.str) -> "SamlMetadataDocument":
        '''Create a SAML metadata document from a XML string.

        :param xml: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__539954bae3260c99c71a9ce3ae7c5beabd619c72716348d783fb02a4392e8980)
            check_type(argname="argument xml", value=xml, expected_type=type_hints["xml"])
        return typing.cast("SamlMetadataDocument", jsii.sinvoke(cls, "fromXml", [xml]))

    @builtins.property
    @jsii.member(jsii_name="xml")
    @abc.abstractmethod
    def xml(self) -> builtins.str:
        '''The XML content of the metadata document.'''
        ...


class _SamlMetadataDocumentProxy(SamlMetadataDocument):
    @builtins.property
    @jsii.member(jsii_name="xml")
    def xml(self) -> builtins.str:
        '''The XML content of the metadata document.'''
        return typing.cast(builtins.str, jsii.get(self, "xml"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, SamlMetadataDocument).__jsii_proxy_class__ = lambda : _SamlMetadataDocumentProxy


@jsii.implements(ISamlProvider)
class SamlProvider(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.SamlProvider",
):
    '''A SAML provider.

    :exampleMetadata: infused

    Example::

        provider = iam.SamlProvider(self, "Provider",
            metadata_document=iam.SamlMetadataDocument.from_file("/path/to/saml-metadata-document.xml")
        )
        iam.Role(self, "Role",
            assumed_by=iam.SamlConsolePrincipal(provider)
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        metadata_document: SamlMetadataDocument,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param metadata_document: An XML document generated by an identity provider (IdP) that supports SAML 2.0. The document includes the issuer's name, expiration information, and keys that can be used to validate the SAML authentication response (assertions) that are received from the IdP. You must generate the metadata document using the identity management software that is used as your organization's IdP.
        :param name: The name of the provider to create. This parameter allows a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@- Length must be between 1 and 128 characters. Default: - a CloudFormation generated name
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75c8a0ae91cf9a623b67a15b867de0473fa7870f3d3806ea585381a9a32222a2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = SamlProviderProps(metadata_document=metadata_document, name=name)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromSamlProviderArn")
    @builtins.classmethod
    def from_saml_provider_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        saml_provider_arn: builtins.str,
    ) -> ISamlProvider:
        '''Import an existing provider.

        :param scope: -
        :param id: -
        :param saml_provider_arn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b78da91cf00435dc5bff92bbb2857fe752f6a28b7483a3790b9a5fc1a88be6ab)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument saml_provider_arn", value=saml_provider_arn, expected_type=type_hints["saml_provider_arn"])
        return typing.cast(ISamlProvider, jsii.sinvoke(cls, "fromSamlProviderArn", [scope, id, saml_provider_arn]))

    @builtins.property
    @jsii.member(jsii_name="samlProviderArn")
    def saml_provider_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the provider.'''
        return typing.cast(builtins.str, jsii.get(self, "samlProviderArn"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.SamlProviderProps",
    jsii_struct_bases=[],
    name_mapping={"metadata_document": "metadataDocument", "name": "name"},
)
class SamlProviderProps:
    def __init__(
        self,
        *,
        metadata_document: SamlMetadataDocument,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for a SAML provider.

        :param metadata_document: An XML document generated by an identity provider (IdP) that supports SAML 2.0. The document includes the issuer's name, expiration information, and keys that can be used to validate the SAML authentication response (assertions) that are received from the IdP. You must generate the metadata document using the identity management software that is used as your organization's IdP.
        :param name: The name of the provider to create. This parameter allows a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@- Length must be between 1 and 128 characters. Default: - a CloudFormation generated name

        :exampleMetadata: infused

        Example::

            provider = iam.SamlProvider(self, "Provider",
                metadata_document=iam.SamlMetadataDocument.from_file("/path/to/saml-metadata-document.xml")
            )
            iam.Role(self, "Role",
                assumed_by=iam.SamlConsolePrincipal(provider)
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f0838242f105f982b040b1e4abc268b7e6230b1f40a59916bdce34e26df4782)
            check_type(argname="argument metadata_document", value=metadata_document, expected_type=type_hints["metadata_document"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metadata_document": metadata_document,
        }
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def metadata_document(self) -> SamlMetadataDocument:
        '''An XML document generated by an identity provider (IdP) that supports SAML 2.0. The document includes the issuer's name, expiration information, and keys that can be used to validate the SAML authentication response (assertions) that are received from the IdP. You must generate the metadata document using the identity management software that is used as your organization's IdP.'''
        result = self._values.get("metadata_document")
        assert result is not None, "Required property 'metadata_document' is missing"
        return typing.cast(SamlMetadataDocument, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the provider to create.

        This parameter allows a string of characters consisting of upper and
        lowercase alphanumeric characters with no spaces. You can also include
        any of the following characters: _+=,.@-

        Length must be between 1 and 128 characters.

        :default: - a CloudFormation generated name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SamlProviderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.ServicePrincipalOpts",
    jsii_struct_bases=[],
    name_mapping={"conditions": "conditions", "region": "region"},
)
class ServicePrincipalOpts:
    def __init__(
        self,
        *,
        conditions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Options for a service principal.

        :param conditions: Additional conditions to add to the Service Principal. Default: - No conditions
        :param region: The region in which you want to reference the service. This is only necessary for *cross-region* references to *opt-in* regions. In those cases, the region name needs to be included to reference the correct service principal. In all other cases, the global service principal name is sufficient. This field behaves differently depending on whether the ``@aws-cdk/aws-iam:standardizedServicePrincipals`` flag is set or not: - If the flag is set, the input service principal is assumed to be of the form ``SERVICE.amazonaws.com``. That value will always be returned, unless the given region is an opt-in region and the service principal is rendered in a stack in a different region, in which case ``SERVICE.REGION.amazonaws.com`` will be rendered. Under this regime, there is no downside to always specifying the region property: it will be rendered only if necessary. - If the flag is not set, the service principal will resolve to a single principal whose name comes from the ``@aws-cdk/region-info`` package, using the region to override the stack region. If there is no entry for this service principal in the database,, the input service name is returned literally. This is legacy behavior and is not recommended. Default: - the resolving Stack's region.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            
            # conditions: Any
            
            service_principal_opts = iam.ServicePrincipalOpts(
                conditions={
                    "conditions_key": conditions
                },
                region="region"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1a7b908a503ee76c237762d915d7a503778df01faaca4c8b3e6de46c413efea)
            check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if conditions is not None:
            self._values["conditions"] = conditions
        if region is not None:
            self._values["region"] = region

    @builtins.property
    def conditions(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Additional conditions to add to the Service Principal.

        :default: - No conditions
        '''
        result = self._values.get("conditions")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The region in which you want to reference the service.

        This is only necessary for *cross-region* references to *opt-in* regions. In those
        cases, the region name needs to be included to reference the correct service principal.
        In all other cases, the global service principal name is sufficient.

        This field behaves differently depending on whether the ``@aws-cdk/aws-iam:standardizedServicePrincipals``
        flag is set or not:

        - If the flag is set, the input service principal is assumed to be of the form ``SERVICE.amazonaws.com``.
          That value will always be returned, unless the given region is an opt-in region and the service
          principal is rendered in a stack in a different region, in which case ``SERVICE.REGION.amazonaws.com``
          will be rendered. Under this regime, there is no downside to always specifying the region property:
          it will be rendered only if necessary.
        - If the flag is not set, the service principal will resolve to a single principal
          whose name comes from the ``@aws-cdk/region-info`` package, using the region to override
          the stack region. If there is no entry for this service principal in the database,, the input
          service name is returned literally. This is legacy behavior and is not recommended.

        :default: - the resolving Stack's region.
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServicePrincipalOpts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IPrincipal)
class UnknownPrincipal(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.UnknownPrincipal",
):
    '''A principal for use in resources that need to have a role but it's unknown.

    Some resources have roles associated with them which they assume, such as
    Lambda Functions, CodeBuild projects, StepFunctions machines, etc.

    When those resources are imported, their actual roles are not always
    imported with them. When that happens, we use an instance of this class
    instead, which will add user warnings when statements are attempted to be
    added to it.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iam as iam
        import constructs as constructs
        
        # construct: constructs.Construct
        
        unknown_principal = iam.UnknownPrincipal(
            resource=construct
        )
    '''

    def __init__(self, *, resource: _constructs_77d1e7e8.IConstruct) -> None:
        '''
        :param resource: The resource the role proxy is for.
        '''
        props = UnknownPrincipalProps(resource=resource)

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="addToPolicy")
    def add_to_policy(self, statement: PolicyStatement) -> builtins.bool:
        '''Add to the policy of this principal.

        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0427f0b3c82f050501fde1f37f0708213ce2880cf76710cab2373a0fce6fbf0a)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(builtins.bool, jsii.invoke(self, "addToPolicy", [statement]))

    @jsii.member(jsii_name="addToPrincipalPolicy")
    def add_to_principal_policy(
        self,
        statement: PolicyStatement,
    ) -> AddToPrincipalPolicyResult:
        '''Add to the policy of this principal.

        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2eafec25f04d3417a92e78ef10e9bfbbdf9bad8c39e6cf6cafe9a65939952296)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(AddToPrincipalPolicyResult, jsii.invoke(self, "addToPrincipalPolicy", [statement]))

    @builtins.property
    @jsii.member(jsii_name="assumeRoleAction")
    def assume_role_action(self) -> builtins.str:
        '''When this Principal is used in an AssumeRole policy, the action to use.'''
        return typing.cast(builtins.str, jsii.get(self, "assumeRoleAction"))

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> IPrincipal:
        '''The principal to grant permissions to.'''
        return typing.cast(IPrincipal, jsii.get(self, "grantPrincipal"))

    @builtins.property
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> PrincipalPolicyFragment:
        '''Return the policy fragment that identifies this principal in a Policy.'''
        return typing.cast(PrincipalPolicyFragment, jsii.get(self, "policyFragment"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.UnknownPrincipalProps",
    jsii_struct_bases=[],
    name_mapping={"resource": "resource"},
)
class UnknownPrincipalProps:
    def __init__(self, *, resource: _constructs_77d1e7e8.IConstruct) -> None:
        '''Properties for an UnknownPrincipal.

        :param resource: The resource the role proxy is for.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            import constructs as constructs
            
            # construct: constructs.Construct
            
            unknown_principal_props = iam.UnknownPrincipalProps(
                resource=construct
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5de6fb03be5f0e87676deff413c87e5098f429f34e2caed17f1337c435ed431)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource": resource,
        }

    @builtins.property
    def resource(self) -> _constructs_77d1e7e8.IConstruct:
        '''The resource the role proxy is for.'''
        result = self._values.get("resource")
        assert result is not None, "Required property 'resource' is missing"
        return typing.cast(_constructs_77d1e7e8.IConstruct, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UnknownPrincipalProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.UserAttributes",
    jsii_struct_bases=[],
    name_mapping={"user_arn": "userArn"},
)
class UserAttributes:
    def __init__(self, *, user_arn: builtins.str) -> None:
        '''Represents a user defined outside of this stack.

        :param user_arn: The ARN of the user. Format: arn::iam:::user/

        :exampleMetadata: infused

        Example::

            user = iam.User.from_user_attributes(self, "MyImportedUserByAttributes",
                user_arn="arn:aws:iam::123456789012:user/johnsmith"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5246085f2e2073ef1bcc0015f7ac242968b5a4a77257c315904c1bf3c1dabd4a)
            check_type(argname="argument user_arn", value=user_arn, expected_type=type_hints["user_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "user_arn": user_arn,
        }

    @builtins.property
    def user_arn(self) -> builtins.str:
        '''The ARN of the user.

        Format: arn::iam:::user/
        '''
        result = self._values.get("user_arn")
        assert result is not None, "Required property 'user_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.UserProps",
    jsii_struct_bases=[],
    name_mapping={
        "groups": "groups",
        "managed_policies": "managedPolicies",
        "password": "password",
        "password_reset_required": "passwordResetRequired",
        "path": "path",
        "permissions_boundary": "permissionsBoundary",
        "user_name": "userName",
    },
)
class UserProps:
    def __init__(
        self,
        *,
        groups: typing.Optional[typing.Sequence["IGroup"]] = None,
        managed_policies: typing.Optional[typing.Sequence[IManagedPolicy]] = None,
        password: typing.Optional[_SecretValue_3dd0ddae] = None,
        password_reset_required: typing.Optional[builtins.bool] = None,
        path: typing.Optional[builtins.str] = None,
        permissions_boundary: typing.Optional[IManagedPolicy] = None,
        user_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining an IAM user.

        :param groups: Groups to add this user to. You can also use ``addToGroup`` to add this user to a group. Default: - No groups.
        :param managed_policies: A list of managed policies associated with this role. You can add managed policies later using ``addManagedPolicy(ManagedPolicy.fromAwsManagedPolicyName(policyName))``. Default: - No managed policies.
        :param password: The password for the user. This is required so the user can access the AWS Management Console. You can use ``SecretValue.unsafePlainText`` to specify a password in plain text or use ``secretsmanager.Secret.fromSecretAttributes`` to reference a secret in Secrets Manager. Default: - User won't be able to access the management console without a password.
        :param password_reset_required: Specifies whether the user is required to set a new password the next time the user logs in to the AWS Management Console. If this is set to 'true', you must also specify "initialPassword". Default: false
        :param path: The path for the user name. For more information about paths, see IAM Identifiers in the IAM User Guide. Default: /
        :param permissions_boundary: AWS supports permissions boundaries for IAM entities (users or roles). A permissions boundary is an advanced feature for using a managed policy to set the maximum permissions that an identity-based policy can grant to an IAM entity. An entity's permissions boundary allows it to perform only the actions that are allowed by both its identity-based policies and its permissions boundaries. Default: - No permissions boundary.
        :param user_name: A name for the IAM user. For valid values, see the UserName parameter for the CreateUser action in the IAM API Reference. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the user name. If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name. If you specify a name, you must specify the CAPABILITY_NAMED_IAM value to acknowledge your template's capabilities. For more information, see Acknowledging IAM Resources in AWS CloudFormation Templates. Default: - Generated by CloudFormation (recommended)

        :exampleMetadata: lit=aws-iam/test/example.attaching.lit.ts infused

        Example::

            user = User(self, "MyUser", password=SecretValue.plain_text("1234"))
            group = Group(self, "MyGroup")
            
            policy = Policy(self, "MyPolicy")
            policy.attach_to_user(user)
            group.attach_inline_policy(policy)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b49c33f300471f45a248f56a068fb48f78451f10631fedcb3e5890d72ce3fe05)
            check_type(argname="argument groups", value=groups, expected_type=type_hints["groups"])
            check_type(argname="argument managed_policies", value=managed_policies, expected_type=type_hints["managed_policies"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument password_reset_required", value=password_reset_required, expected_type=type_hints["password_reset_required"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument permissions_boundary", value=permissions_boundary, expected_type=type_hints["permissions_boundary"])
            check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if groups is not None:
            self._values["groups"] = groups
        if managed_policies is not None:
            self._values["managed_policies"] = managed_policies
        if password is not None:
            self._values["password"] = password
        if password_reset_required is not None:
            self._values["password_reset_required"] = password_reset_required
        if path is not None:
            self._values["path"] = path
        if permissions_boundary is not None:
            self._values["permissions_boundary"] = permissions_boundary
        if user_name is not None:
            self._values["user_name"] = user_name

    @builtins.property
    def groups(self) -> typing.Optional[typing.List["IGroup"]]:
        '''Groups to add this user to.

        You can also use ``addToGroup`` to add this
        user to a group.

        :default: - No groups.
        '''
        result = self._values.get("groups")
        return typing.cast(typing.Optional[typing.List["IGroup"]], result)

    @builtins.property
    def managed_policies(self) -> typing.Optional[typing.List[IManagedPolicy]]:
        '''A list of managed policies associated with this role.

        You can add managed policies later using
        ``addManagedPolicy(ManagedPolicy.fromAwsManagedPolicyName(policyName))``.

        :default: - No managed policies.
        '''
        result = self._values.get("managed_policies")
        return typing.cast(typing.Optional[typing.List[IManagedPolicy]], result)

    @builtins.property
    def password(self) -> typing.Optional[_SecretValue_3dd0ddae]:
        '''The password for the user. This is required so the user can access the AWS Management Console.

        You can use ``SecretValue.unsafePlainText`` to specify a password in plain text or
        use ``secretsmanager.Secret.fromSecretAttributes`` to reference a secret in
        Secrets Manager.

        :default: - User won't be able to access the management console without a password.
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[_SecretValue_3dd0ddae], result)

    @builtins.property
    def password_reset_required(self) -> typing.Optional[builtins.bool]:
        '''Specifies whether the user is required to set a new password the next time the user logs in to the AWS Management Console.

        If this is set to 'true', you must also specify "initialPassword".

        :default: false
        '''
        result = self._values.get("password_reset_required")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''The path for the user name.

        For more information about paths, see IAM
        Identifiers in the IAM User Guide.

        :default: /
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permissions_boundary(self) -> typing.Optional[IManagedPolicy]:
        '''AWS supports permissions boundaries for IAM entities (users or roles).

        A permissions boundary is an advanced feature for using a managed policy
        to set the maximum permissions that an identity-based policy can grant to
        an IAM entity. An entity's permissions boundary allows it to perform only
        the actions that are allowed by both its identity-based policies and its
        permissions boundaries.

        :default: - No permissions boundary.

        :link: https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html
        '''
        result = self._values.get("permissions_boundary")
        return typing.cast(typing.Optional[IManagedPolicy], result)

    @builtins.property
    def user_name(self) -> typing.Optional[builtins.str]:
        '''A name for the IAM user.

        For valid values, see the UserName parameter for
        the CreateUser action in the IAM API Reference. If you don't specify a
        name, AWS CloudFormation generates a unique physical ID and uses that ID
        for the user name.

        If you specify a name, you cannot perform updates that require
        replacement of this resource. You can perform updates that require no or
        some interruption. If you must replace the resource, specify a new name.

        If you specify a name, you must specify the CAPABILITY_NAMED_IAM value to
        acknowledge your template's capabilities. For more information, see
        Acknowledging IAM Resources in AWS CloudFormation Templates.

        :default: - Generated by CloudFormation (recommended)
        '''
        result = self._values.get("user_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.WithoutPolicyUpdatesOptions",
    jsii_struct_bases=[],
    name_mapping={"add_grants_to_resources": "addGrantsToResources"},
)
class WithoutPolicyUpdatesOptions:
    def __init__(
        self,
        *,
        add_grants_to_resources: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options for the ``withoutPolicyUpdates()`` modifier of a Role.

        :param add_grants_to_resources: Add grants to resources instead of dropping them. If this is ``false`` or not specified, grant permissions added to this role are ignored. It is your own responsibility to make sure the role has the required permissions. If this is ``true``, any grant permissions will be added to the resource instead. Default: false

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            
            without_policy_updates_options = iam.WithoutPolicyUpdatesOptions(
                add_grants_to_resources=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63c38b4a84c27c159038a7ab31110e5032bef8ddad181f04f0b754232fb1ed44)
            check_type(argname="argument add_grants_to_resources", value=add_grants_to_resources, expected_type=type_hints["add_grants_to_resources"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if add_grants_to_resources is not None:
            self._values["add_grants_to_resources"] = add_grants_to_resources

    @builtins.property
    def add_grants_to_resources(self) -> typing.Optional[builtins.bool]:
        '''Add grants to resources instead of dropping them.

        If this is ``false`` or not specified, grant permissions added to this role are ignored.
        It is your own responsibility to make sure the role has the required permissions.

        If this is ``true``, any grant permissions will be added to the resource instead.

        :default: false
        '''
        result = self._values.get("add_grants_to_resources")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WithoutPolicyUpdatesOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IAccessKey)
class AccessKey(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.AccessKey",
):
    '''Define a new IAM Access Key.

    :exampleMetadata: infused

    Example::

        # Creates a new IAM user, access and secret keys, and stores the secret access key in a Secret.
        user = iam.User(self, "User")
        access_key = iam.AccessKey(self, "AccessKey", user=user)
        secret = secretsmanager.Secret(self, "Secret",
            secret_string_value=access_key.secret_access_key
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        user: "IUser",
        serial: typing.Optional[jsii.Number] = None,
        status: typing.Optional[AccessKeyStatus] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param user: The IAM user this key will belong to. Changing this value will result in the access key being deleted and a new access key (with a different ID and secret value) being assigned to the new user.
        :param serial: A CloudFormation-specific value that signifies the access key should be replaced/rotated. This value can only be incremented. Incrementing this value will cause CloudFormation to replace the Access Key resource. Default: - No serial value
        :param status: The status of the access key. An Active access key is allowed to be used to make API calls; An Inactive key cannot. Default: - The access key is active
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__604f514db426465dbc092293e7b2e46f5358ddb17770a96f51ef7e6a5f6d15f4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = AccessKeyProps(user=user, serial=serial, status=status)

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="accessKeyId")
    def access_key_id(self) -> builtins.str:
        '''The Access Key ID.'''
        return typing.cast(builtins.str, jsii.get(self, "accessKeyId"))

    @builtins.property
    @jsii.member(jsii_name="secretAccessKey")
    def secret_access_key(self) -> _SecretValue_3dd0ddae:
        '''The Secret Access Key.'''
        return typing.cast(_SecretValue_3dd0ddae, jsii.get(self, "secretAccessKey"))


@jsii.interface(jsii_type="aws-cdk-lib.aws_iam.IAssumeRolePrincipal")
class IAssumeRolePrincipal(IPrincipal, typing_extensions.Protocol):
    '''A type of principal that has more control over its own representation in AssumeRolePolicyDocuments.

    More complex types of identity providers need more control over Role's policy documents
    than simply ``{ Effect: 'Allow', Action: 'AssumeRole', Principal: <Whatever> }``.

    If that control is necessary, they can implement ``IAssumeRolePrincipal`` to get full
    access to a Role's AssumeRolePolicyDocument.
    '''

    @jsii.member(jsii_name="addToAssumeRolePolicy")
    def add_to_assume_role_policy(self, document: PolicyDocument) -> None:
        '''Add the principal to the AssumeRolePolicyDocument.

        Add the statements to the AssumeRolePolicyDocument necessary to give this principal
        permissions to assume the given role.

        :param document: -
        '''
        ...


class _IAssumeRolePrincipalProxy(
    jsii.proxy_for(IPrincipal), # type: ignore[misc]
):
    '''A type of principal that has more control over its own representation in AssumeRolePolicyDocuments.

    More complex types of identity providers need more control over Role's policy documents
    than simply ``{ Effect: 'Allow', Action: 'AssumeRole', Principal: <Whatever> }``.

    If that control is necessary, they can implement ``IAssumeRolePrincipal`` to get full
    access to a Role's AssumeRolePolicyDocument.
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_iam.IAssumeRolePrincipal"

    @jsii.member(jsii_name="addToAssumeRolePolicy")
    def add_to_assume_role_policy(self, document: PolicyDocument) -> None:
        '''Add the principal to the AssumeRolePolicyDocument.

        Add the statements to the AssumeRolePolicyDocument necessary to give this principal
        permissions to assume the given role.

        :param document: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2773dd1c98b9bb45b356173892f3248a430e55c5ab0a22cb6e5df0bcdaa898a5)
            check_type(argname="argument document", value=document, expected_type=type_hints["document"])
        return typing.cast(None, jsii.invoke(self, "addToAssumeRolePolicy", [document]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAssumeRolePrincipal).__jsii_proxy_class__ = lambda : _IAssumeRolePrincipalProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_iam.IComparablePrincipal")
class IComparablePrincipal(IPrincipal, typing_extensions.Protocol):
    '''Interface for principals that can be compared.

    This only needs to be implemented for principals that could potentially be value-equal.
    Identity-equal principals will be handled correctly by default.
    '''

    @jsii.member(jsii_name="dedupeString")
    def dedupe_string(self) -> typing.Optional[builtins.str]:
        '''Return a string format of this principal which should be identical if the two principals are the same.'''
        ...


class _IComparablePrincipalProxy(
    jsii.proxy_for(IPrincipal), # type: ignore[misc]
):
    '''Interface for principals that can be compared.

    This only needs to be implemented for principals that could potentially be value-equal.
    Identity-equal principals will be handled correctly by default.
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_iam.IComparablePrincipal"

    @jsii.member(jsii_name="dedupeString")
    def dedupe_string(self) -> typing.Optional[builtins.str]:
        '''Return a string format of this principal which should be identical if the two principals are the same.'''
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "dedupeString", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IComparablePrincipal).__jsii_proxy_class__ = lambda : _IComparablePrincipalProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_iam.IIdentity")
class IIdentity(IPrincipal, _IResource_c80c4260, typing_extensions.Protocol):
    '''A construct that represents an IAM principal, such as a user, group or role.'''

    @jsii.member(jsii_name="addManagedPolicy")
    def add_managed_policy(self, policy: IManagedPolicy) -> None:
        '''Attaches a managed policy to this principal.

        :param policy: The managed policy.
        '''
        ...

    @jsii.member(jsii_name="attachInlinePolicy")
    def attach_inline_policy(self, policy: Policy) -> None:
        '''Attaches an inline policy to this principal.

        This is the same as calling ``policy.addToXxx(principal)``.

        :param policy: The policy resource to attach to this principal [disable-awslint:ref-via-interface].
        '''
        ...


class _IIdentityProxy(
    jsii.proxy_for(IPrincipal), # type: ignore[misc]
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''A construct that represents an IAM principal, such as a user, group or role.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_iam.IIdentity"

    @jsii.member(jsii_name="addManagedPolicy")
    def add_managed_policy(self, policy: IManagedPolicy) -> None:
        '''Attaches a managed policy to this principal.

        :param policy: The managed policy.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c19fda9308c83b1b61fd496fa74f5eddc104dfaf811b56cfe18d29e27da6971)
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
        return typing.cast(None, jsii.invoke(self, "addManagedPolicy", [policy]))

    @jsii.member(jsii_name="attachInlinePolicy")
    def attach_inline_policy(self, policy: Policy) -> None:
        '''Attaches an inline policy to this principal.

        This is the same as calling ``policy.addToXxx(principal)``.

        :param policy: The policy resource to attach to this principal [disable-awslint:ref-via-interface].
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a57592179e2cd5bb2a5698dd5de580c2c15bed0adf0f8f55b31f9abd9fd5846)
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
        return typing.cast(None, jsii.invoke(self, "attachInlinePolicy", [policy]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIdentity).__jsii_proxy_class__ = lambda : _IIdentityProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_iam.IRole")
class IRole(IIdentity, typing_extensions.Protocol):
    '''A Role object.'''

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''Returns the ARN of this role.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="roleName")
    def role_name(self) -> builtins.str:
        '''Returns the name of this role.

        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="grant")
    def grant(self, grantee: IPrincipal, *actions: builtins.str) -> Grant:
        '''Grant the actions defined in actions to the identity Principal on this resource.

        :param grantee: -
        :param actions: -
        '''
        ...

    @jsii.member(jsii_name="grantAssumeRole")
    def grant_assume_role(self, grantee: IPrincipal) -> Grant:
        '''Grant permissions to the given principal to assume this role.

        :param grantee: -
        '''
        ...

    @jsii.member(jsii_name="grantPassRole")
    def grant_pass_role(self, grantee: IPrincipal) -> Grant:
        '''Grant permissions to the given principal to pass this role.

        :param grantee: -
        '''
        ...


class _IRoleProxy(
    jsii.proxy_for(IIdentity), # type: ignore[misc]
):
    '''A Role object.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_iam.IRole"

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''Returns the ARN of this role.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @builtins.property
    @jsii.member(jsii_name="roleName")
    def role_name(self) -> builtins.str:
        '''Returns the name of this role.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleName"))

    @jsii.member(jsii_name="grant")
    def grant(self, grantee: IPrincipal, *actions: builtins.str) -> Grant:
        '''Grant the actions defined in actions to the identity Principal on this resource.

        :param grantee: -
        :param actions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67e856ddb493b4542dc716dcab0126ed6ac149cd365202cb608c313320eb7b58)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(Grant, jsii.invoke(self, "grant", [grantee, *actions]))

    @jsii.member(jsii_name="grantAssumeRole")
    def grant_assume_role(self, grantee: IPrincipal) -> Grant:
        '''Grant permissions to the given principal to assume this role.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0b3c996a892c638167074eb637574936aa29a63e5e76ed7d460ff90993815e6)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(Grant, jsii.invoke(self, "grantAssumeRole", [grantee]))

    @jsii.member(jsii_name="grantPassRole")
    def grant_pass_role(self, grantee: IPrincipal) -> Grant:
        '''Grant permissions to the given principal to pass this role.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a259325b943101480d852a30d681aee828d57198b8501de84e4d9963505af62)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(Grant, jsii.invoke(self, "grantPassRole", [grantee]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRole).__jsii_proxy_class__ = lambda : _IRoleProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_iam.IUser")
class IUser(IIdentity, typing_extensions.Protocol):
    '''Represents an IAM user.

    :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html
    '''

    @builtins.property
    @jsii.member(jsii_name="userArn")
    def user_arn(self) -> builtins.str:
        '''The user's ARN.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="userName")
    def user_name(self) -> builtins.str:
        '''The user's name.

        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="addToGroup")
    def add_to_group(self, group: "IGroup") -> None:
        '''Adds this user to a group.

        :param group: -
        '''
        ...


class _IUserProxy(
    jsii.proxy_for(IIdentity), # type: ignore[misc]
):
    '''Represents an IAM user.

    :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_iam.IUser"

    @builtins.property
    @jsii.member(jsii_name="userArn")
    def user_arn(self) -> builtins.str:
        '''The user's ARN.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "userArn"))

    @builtins.property
    @jsii.member(jsii_name="userName")
    def user_name(self) -> builtins.str:
        '''The user's name.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "userName"))

    @jsii.member(jsii_name="addToGroup")
    def add_to_group(self, group: "IGroup") -> None:
        '''Adds this user to a group.

        :param group: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17a32edfd359a804d50015e17cf8c5632c9a0e28c3542088534431b5ae1090e3)
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
        return typing.cast(None, jsii.invoke(self, "addToGroup", [group]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IUser).__jsii_proxy_class__ = lambda : _IUserProxy


@jsii.implements(IRole)
class LazyRole(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.LazyRole",
):
    '''An IAM role that only gets attached to the construct tree once it gets used, not before.

    This construct can be used to simplify logic in other constructs
    which need to create a role but only if certain configurations occur
    (such as when AutoScaling is configured). The role can be configured in one
    place, but if it never gets used it doesn't get instantiated and will
    not be synthesized or deployed.

    :resource: AWS::IAM::Role
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk as cdk
        from aws_cdk import aws_iam as iam
        
        # managed_policy: iam.ManagedPolicy
        # policy_document: iam.PolicyDocument
        # principal: iam.IPrincipal
        
        lazy_role = iam.LazyRole(self, "MyLazyRole",
            assumed_by=principal,
        
            # the properties below are optional
            description="description",
            external_ids=["externalIds"],
            inline_policies={
                "inline_policies_key": policy_document
            },
            managed_policies=[managed_policy],
            max_session_duration=cdk.Duration.minutes(30),
            path="path",
            permissions_boundary=managed_policy,
            role_name="roleName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        assumed_by: IPrincipal,
        description: typing.Optional[builtins.str] = None,
        external_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        inline_policies: typing.Optional[typing.Mapping[builtins.str, PolicyDocument]] = None,
        managed_policies: typing.Optional[typing.Sequence[IManagedPolicy]] = None,
        max_session_duration: typing.Optional[_Duration_4839e8c3] = None,
        path: typing.Optional[builtins.str] = None,
        permissions_boundary: typing.Optional[IManagedPolicy] = None,
        role_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param assumed_by: The IAM principal (i.e. ``new ServicePrincipal('sns.amazonaws.com')``) which can assume this role. You can later modify the assume role policy document by accessing it via the ``assumeRolePolicy`` property.
        :param description: A description of the role. It can be up to 1000 characters long. Default: - No description.
        :param external_ids: List of IDs that the role assumer needs to provide one of when assuming this role. If the configured and provided external IDs do not match, the AssumeRole operation will fail. Default: No external ID required
        :param inline_policies: A list of named policies to inline into this role. These policies will be created with the role, whereas those added by ``addToPolicy`` are added using a separate CloudFormation resource (allowing a way around circular dependencies that could otherwise be introduced). Default: - No policy is inlined in the Role resource.
        :param managed_policies: A list of managed policies associated with this role. You can add managed policies later using ``addManagedPolicy(ManagedPolicy.fromAwsManagedPolicyName(policyName))``. Default: - No managed policies.
        :param max_session_duration: The maximum session duration that you want to set for the specified role. This setting can have a value from 1 hour (3600sec) to 12 (43200sec) hours. Anyone who assumes the role from the AWS CLI or API can use the DurationSeconds API parameter or the duration-seconds CLI parameter to request a longer session. The MaxSessionDuration setting determines the maximum duration that can be requested using the DurationSeconds parameter. If users don't specify a value for the DurationSeconds parameter, their security credentials are valid for one hour by default. This applies when you use the AssumeRole* API operations or the assume-role* CLI operations but does not apply when you use those operations to create a console URL. Default: Duration.hours(1)
        :param path: The path associated with this role. For information about IAM paths, see Friendly Names and Paths in IAM User Guide. Default: /
        :param permissions_boundary: AWS supports permissions boundaries for IAM entities (users or roles). A permissions boundary is an advanced feature for using a managed policy to set the maximum permissions that an identity-based policy can grant to an IAM entity. An entity's permissions boundary allows it to perform only the actions that are allowed by both its identity-based policies and its permissions boundaries. Default: - No permissions boundary.
        :param role_name: A name for the IAM role. For valid values, see the RoleName parameter for the CreateRole action in the IAM API Reference. IMPORTANT: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name. If you specify a name, you must specify the CAPABILITY_NAMED_IAM value to acknowledge your template's capabilities. For more information, see Acknowledging IAM Resources in AWS CloudFormation Templates. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the role name.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__771573f5504b0120c9b82d20864766023cef9d916834720ff78de68c51d14153)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = LazyRoleProps(
            assumed_by=assumed_by,
            description=description,
            external_ids=external_ids,
            inline_policies=inline_policies,
            managed_policies=managed_policies,
            max_session_duration=max_session_duration,
            path=path,
            permissions_boundary=permissions_boundary,
            role_name=role_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addManagedPolicy")
    def add_managed_policy(self, policy: IManagedPolicy) -> None:
        '''Attaches a managed policy to this role.

        :param policy: The managed policy to attach.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43833b8b06cff5918ffc7655ee5b826bd75570f638200a98519f8c2ebf0372b5)
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
        return typing.cast(None, jsii.invoke(self, "addManagedPolicy", [policy]))

    @jsii.member(jsii_name="addToPolicy")
    def add_to_policy(self, statement: PolicyStatement) -> builtins.bool:
        '''Add to the policy of this principal.

        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c166a85c28147c9f37dcd0918c774393f73316341430625933ab60ba8c826890)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(builtins.bool, jsii.invoke(self, "addToPolicy", [statement]))

    @jsii.member(jsii_name="addToPrincipalPolicy")
    def add_to_principal_policy(
        self,
        statement: PolicyStatement,
    ) -> AddToPrincipalPolicyResult:
        '''Adds a permission to the role's default policy document.

        If there is no default policy attached to this role, it will be created.

        :param statement: The permission statement to add to the policy document.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__360ff356db658c7d68d451f8da5ae3d55112b9a2f638786bc4cdaea9658802b8)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(AddToPrincipalPolicyResult, jsii.invoke(self, "addToPrincipalPolicy", [statement]))

    @jsii.member(jsii_name="attachInlinePolicy")
    def attach_inline_policy(self, policy: Policy) -> None:
        '''Attaches a policy to this role.

        :param policy: The policy to attach.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22f70d75c15f0109cb998f8124e49401dae23a005cccc337014728056eeaa336)
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
        return typing.cast(None, jsii.invoke(self, "attachInlinePolicy", [policy]))

    @jsii.member(jsii_name="grant")
    def grant(self, identity: IPrincipal, *actions: builtins.str) -> Grant:
        '''Grant the actions defined in actions to the identity Principal on this resource.

        :param identity: -
        :param actions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31e7156ac8208f98f3be102fb3156e3f6bcdf5fe871d6df26b60c2e9cf69336f)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(Grant, jsii.invoke(self, "grant", [identity, *actions]))

    @jsii.member(jsii_name="grantAssumeRole")
    def grant_assume_role(self, identity: IPrincipal) -> Grant:
        '''Grant permissions to the given principal to assume this role.

        :param identity: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d09b1058d1d2350165fea6b922b2c0fe02ec3216af993738db1f47c4932c55f)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(Grant, jsii.invoke(self, "grantAssumeRole", [identity]))

    @jsii.member(jsii_name="grantPassRole")
    def grant_pass_role(self, identity: IPrincipal) -> Grant:
        '''Grant permissions to the given principal to pass this role.

        :param identity: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6367cadac69d2b22537737f04814197b71e654eb8d432cbd5b41e484577f1446)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(Grant, jsii.invoke(self, "grantPassRole", [identity]))

    @builtins.property
    @jsii.member(jsii_name="assumeRoleAction")
    def assume_role_action(self) -> builtins.str:
        '''When this Principal is used in an AssumeRole policy, the action to use.'''
        return typing.cast(builtins.str, jsii.get(self, "assumeRoleAction"))

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> IPrincipal:
        '''The principal to grant permissions to.'''
        return typing.cast(IPrincipal, jsii.get(self, "grantPrincipal"))

    @builtins.property
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> PrincipalPolicyFragment:
        '''Return the policy fragment that identifies this principal in a Policy.'''
        return typing.cast(PrincipalPolicyFragment, jsii.get(self, "policyFragment"))

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''Returns the ARN of this role.'''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @builtins.property
    @jsii.member(jsii_name="roleId")
    def role_id(self) -> builtins.str:
        '''Returns the stable and unique string identifying the role (i.e. AIDAJQABLZS4A3QDU576Q).

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleId"))

    @builtins.property
    @jsii.member(jsii_name="roleName")
    def role_name(self) -> builtins.str:
        '''Returns the name of this role.'''
        return typing.cast(builtins.str, jsii.get(self, "roleName"))

    @builtins.property
    @jsii.member(jsii_name="principalAccount")
    def principal_account(self) -> typing.Optional[builtins.str]:
        '''The AWS account ID of this principal.

        Can be undefined when the account is not known
        (for example, for service principals).
        Can be a Token - in that case,
        it's assumed to be AWS::AccountId.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "principalAccount"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iam.LazyRoleProps",
    jsii_struct_bases=[RoleProps],
    name_mapping={
        "assumed_by": "assumedBy",
        "description": "description",
        "external_ids": "externalIds",
        "inline_policies": "inlinePolicies",
        "managed_policies": "managedPolicies",
        "max_session_duration": "maxSessionDuration",
        "path": "path",
        "permissions_boundary": "permissionsBoundary",
        "role_name": "roleName",
    },
)
class LazyRoleProps(RoleProps):
    def __init__(
        self,
        *,
        assumed_by: IPrincipal,
        description: typing.Optional[builtins.str] = None,
        external_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        inline_policies: typing.Optional[typing.Mapping[builtins.str, PolicyDocument]] = None,
        managed_policies: typing.Optional[typing.Sequence[IManagedPolicy]] = None,
        max_session_duration: typing.Optional[_Duration_4839e8c3] = None,
        path: typing.Optional[builtins.str] = None,
        permissions_boundary: typing.Optional[IManagedPolicy] = None,
        role_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a LazyRole.

        :param assumed_by: The IAM principal (i.e. ``new ServicePrincipal('sns.amazonaws.com')``) which can assume this role. You can later modify the assume role policy document by accessing it via the ``assumeRolePolicy`` property.
        :param description: A description of the role. It can be up to 1000 characters long. Default: - No description.
        :param external_ids: List of IDs that the role assumer needs to provide one of when assuming this role. If the configured and provided external IDs do not match, the AssumeRole operation will fail. Default: No external ID required
        :param inline_policies: A list of named policies to inline into this role. These policies will be created with the role, whereas those added by ``addToPolicy`` are added using a separate CloudFormation resource (allowing a way around circular dependencies that could otherwise be introduced). Default: - No policy is inlined in the Role resource.
        :param managed_policies: A list of managed policies associated with this role. You can add managed policies later using ``addManagedPolicy(ManagedPolicy.fromAwsManagedPolicyName(policyName))``. Default: - No managed policies.
        :param max_session_duration: The maximum session duration that you want to set for the specified role. This setting can have a value from 1 hour (3600sec) to 12 (43200sec) hours. Anyone who assumes the role from the AWS CLI or API can use the DurationSeconds API parameter or the duration-seconds CLI parameter to request a longer session. The MaxSessionDuration setting determines the maximum duration that can be requested using the DurationSeconds parameter. If users don't specify a value for the DurationSeconds parameter, their security credentials are valid for one hour by default. This applies when you use the AssumeRole* API operations or the assume-role* CLI operations but does not apply when you use those operations to create a console URL. Default: Duration.hours(1)
        :param path: The path associated with this role. For information about IAM paths, see Friendly Names and Paths in IAM User Guide. Default: /
        :param permissions_boundary: AWS supports permissions boundaries for IAM entities (users or roles). A permissions boundary is an advanced feature for using a managed policy to set the maximum permissions that an identity-based policy can grant to an IAM entity. An entity's permissions boundary allows it to perform only the actions that are allowed by both its identity-based policies and its permissions boundaries. Default: - No permissions boundary.
        :param role_name: A name for the IAM role. For valid values, see the RoleName parameter for the CreateRole action in the IAM API Reference. IMPORTANT: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name. If you specify a name, you must specify the CAPABILITY_NAMED_IAM value to acknowledge your template's capabilities. For more information, see Acknowledging IAM Resources in AWS CloudFormation Templates. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the role name.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_iam as iam
            
            # managed_policy: iam.ManagedPolicy
            # policy_document: iam.PolicyDocument
            # principal: iam.IPrincipal
            
            lazy_role_props = iam.LazyRoleProps(
                assumed_by=principal,
            
                # the properties below are optional
                description="description",
                external_ids=["externalIds"],
                inline_policies={
                    "inline_policies_key": policy_document
                },
                managed_policies=[managed_policy],
                max_session_duration=cdk.Duration.minutes(30),
                path="path",
                permissions_boundary=managed_policy,
                role_name="roleName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__214cb969b47d061738027497a5718edc40a7ebc688fb6a11b0b38fef268c3b05)
            check_type(argname="argument assumed_by", value=assumed_by, expected_type=type_hints["assumed_by"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument external_ids", value=external_ids, expected_type=type_hints["external_ids"])
            check_type(argname="argument inline_policies", value=inline_policies, expected_type=type_hints["inline_policies"])
            check_type(argname="argument managed_policies", value=managed_policies, expected_type=type_hints["managed_policies"])
            check_type(argname="argument max_session_duration", value=max_session_duration, expected_type=type_hints["max_session_duration"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument permissions_boundary", value=permissions_boundary, expected_type=type_hints["permissions_boundary"])
            check_type(argname="argument role_name", value=role_name, expected_type=type_hints["role_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "assumed_by": assumed_by,
        }
        if description is not None:
            self._values["description"] = description
        if external_ids is not None:
            self._values["external_ids"] = external_ids
        if inline_policies is not None:
            self._values["inline_policies"] = inline_policies
        if managed_policies is not None:
            self._values["managed_policies"] = managed_policies
        if max_session_duration is not None:
            self._values["max_session_duration"] = max_session_duration
        if path is not None:
            self._values["path"] = path
        if permissions_boundary is not None:
            self._values["permissions_boundary"] = permissions_boundary
        if role_name is not None:
            self._values["role_name"] = role_name

    @builtins.property
    def assumed_by(self) -> IPrincipal:
        '''The IAM principal (i.e. ``new ServicePrincipal('sns.amazonaws.com')``) which can assume this role.

        You can later modify the assume role policy document by accessing it via
        the ``assumeRolePolicy`` property.
        '''
        result = self._values.get("assumed_by")
        assert result is not None, "Required property 'assumed_by' is missing"
        return typing.cast(IPrincipal, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the role.

        It can be up to 1000 characters long.

        :default: - No description.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def external_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of IDs that the role assumer needs to provide one of when assuming this role.

        If the configured and provided external IDs do not match, the
        AssumeRole operation will fail.

        :default: No external ID required
        '''
        result = self._values.get("external_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def inline_policies(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, PolicyDocument]]:
        '''A list of named policies to inline into this role.

        These policies will be
        created with the role, whereas those added by ``addToPolicy`` are added
        using a separate CloudFormation resource (allowing a way around circular
        dependencies that could otherwise be introduced).

        :default: - No policy is inlined in the Role resource.
        '''
        result = self._values.get("inline_policies")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, PolicyDocument]], result)

    @builtins.property
    def managed_policies(self) -> typing.Optional[typing.List[IManagedPolicy]]:
        '''A list of managed policies associated with this role.

        You can add managed policies later using
        ``addManagedPolicy(ManagedPolicy.fromAwsManagedPolicyName(policyName))``.

        :default: - No managed policies.
        '''
        result = self._values.get("managed_policies")
        return typing.cast(typing.Optional[typing.List[IManagedPolicy]], result)

    @builtins.property
    def max_session_duration(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The maximum session duration that you want to set for the specified role.

        This setting can have a value from 1 hour (3600sec) to 12 (43200sec) hours.

        Anyone who assumes the role from the AWS CLI or API can use the
        DurationSeconds API parameter or the duration-seconds CLI parameter to
        request a longer session. The MaxSessionDuration setting determines the
        maximum duration that can be requested using the DurationSeconds
        parameter.

        If users don't specify a value for the DurationSeconds parameter, their
        security credentials are valid for one hour by default. This applies when
        you use the AssumeRole* API operations or the assume-role* CLI operations
        but does not apply when you use those operations to create a console URL.

        :default: Duration.hours(1)

        :link: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html
        '''
        result = self._values.get("max_session_duration")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''The path associated with this role.

        For information about IAM paths, see
        Friendly Names and Paths in IAM User Guide.

        :default: /
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permissions_boundary(self) -> typing.Optional[IManagedPolicy]:
        '''AWS supports permissions boundaries for IAM entities (users or roles).

        A permissions boundary is an advanced feature for using a managed policy
        to set the maximum permissions that an identity-based policy can grant to
        an IAM entity. An entity's permissions boundary allows it to perform only
        the actions that are allowed by both its identity-based policies and its
        permissions boundaries.

        :default: - No permissions boundary.

        :link: https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html
        '''
        result = self._values.get("permissions_boundary")
        return typing.cast(typing.Optional[IManagedPolicy], result)

    @builtins.property
    def role_name(self) -> typing.Optional[builtins.str]:
        '''A name for the IAM role.

        For valid values, see the RoleName parameter for
        the CreateRole action in the IAM API Reference.

        IMPORTANT: If you specify a name, you cannot perform updates that require
        replacement of this resource. You can perform updates that require no or
        some interruption. If you must replace the resource, specify a new name.

        If you specify a name, you must specify the CAPABILITY_NAMED_IAM value to
        acknowledge your template's capabilities. For more information, see
        Acknowledging IAM Resources in AWS CloudFormation Templates.

        :default:

        - AWS CloudFormation generates a unique physical ID and uses that ID
        for the role name.
        '''
        result = self._values.get("role_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LazyRoleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IAssumeRolePrincipal, IComparablePrincipal)
class PrincipalBase(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_iam.PrincipalBase",
):
    '''Base class for policy principals.

    :exampleMetadata: infused

    Example::

        tag_param = CfnParameter(self, "TagName")
        
        string_equals = CfnJson(self, "ConditionJson",
            value={
                "f"aws:PrincipalTag/{tagParam.valueAsString}"": True
            }
        )
        
        principal = iam.AccountRootPrincipal().with_conditions({
            "StringEquals": string_equals
        })
        
        iam.Role(self, "MyRole", assumed_by=principal)
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="addToAssumeRolePolicy")
    def add_to_assume_role_policy(self, document: PolicyDocument) -> None:
        '''Add the principal to the AssumeRolePolicyDocument.

        Add the statements to the AssumeRolePolicyDocument necessary to give this principal
        permissions to assume the given role.

        :param document: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42ee81c5ba382087856f240a875085c5aed8781df1691cfb44f7e6acc7b30673)
            check_type(argname="argument document", value=document, expected_type=type_hints["document"])
        return typing.cast(None, jsii.invoke(self, "addToAssumeRolePolicy", [document]))

    @jsii.member(jsii_name="addToPolicy")
    def add_to_policy(self, statement: PolicyStatement) -> builtins.bool:
        '''Add to the policy of this principal.

        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45b95100f32cd1955075f2549ccdf50ea07eb9fac9da91437affa72fa70479f9)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(builtins.bool, jsii.invoke(self, "addToPolicy", [statement]))

    @jsii.member(jsii_name="addToPrincipalPolicy")
    def add_to_principal_policy(
        self,
        _statement: PolicyStatement,
    ) -> AddToPrincipalPolicyResult:
        '''Add to the policy of this principal.

        :param _statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__694de3cb2e0ed269c34a93287704999ec395e28838b40b3e517ecb1615ada2fa)
            check_type(argname="argument _statement", value=_statement, expected_type=type_hints["_statement"])
        return typing.cast(AddToPrincipalPolicyResult, jsii.invoke(self, "addToPrincipalPolicy", [_statement]))

    @jsii.member(jsii_name="dedupeString")
    @abc.abstractmethod
    def dedupe_string(self) -> typing.Optional[builtins.str]:
        '''Return whether or not this principal is equal to the given principal.'''
        ...

    @jsii.member(jsii_name="toJSON")
    def to_json(self) -> typing.Mapping[builtins.str, typing.List[builtins.str]]:
        '''JSON-ify the principal.

        Used when JSON.stringify() is called
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.List[builtins.str]], jsii.invoke(self, "toJSON", []))

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''Returns a string representation of an object.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @jsii.member(jsii_name="withConditions")
    def with_conditions(
        self,
        conditions: typing.Mapping[builtins.str, typing.Any],
    ) -> "PrincipalBase":
        '''Returns a new PrincipalWithConditions using this principal as the base, with the passed conditions added.

        When there is a value for the same operator and key in both the principal and the
        conditions parameter, the value from the conditions parameter will be used.

        :param conditions: -

        :return: a new PrincipalWithConditions object.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba3f398ed80c1e1a0dc5bdc18716f592ab5d21f2ccdd69f292d4579db4f8920e)
            check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
        return typing.cast("PrincipalBase", jsii.invoke(self, "withConditions", [conditions]))

    @jsii.member(jsii_name="withSessionTags")
    def with_session_tags(self) -> "PrincipalBase":
        '''Returns a new principal using this principal as the base, with session tags enabled.

        :return: a new SessionTagsPrincipal object.
        '''
        return typing.cast("PrincipalBase", jsii.invoke(self, "withSessionTags", []))

    @builtins.property
    @jsii.member(jsii_name="assumeRoleAction")
    def assume_role_action(self) -> builtins.str:
        '''When this Principal is used in an AssumeRole policy, the action to use.'''
        return typing.cast(builtins.str, jsii.get(self, "assumeRoleAction"))

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> IPrincipal:
        '''The principal to grant permissions to.'''
        return typing.cast(IPrincipal, jsii.get(self, "grantPrincipal"))

    @builtins.property
    @jsii.member(jsii_name="policyFragment")
    @abc.abstractmethod
    def policy_fragment(self) -> PrincipalPolicyFragment:
        '''Return the policy fragment that identifies this principal in a Policy.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="principalAccount")
    def principal_account(self) -> typing.Optional[builtins.str]:
        '''The AWS account ID of this principal.

        Can be undefined when the account is not known
        (for example, for service principals).
        Can be a Token - in that case,
        it's assumed to be AWS::AccountId.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "principalAccount"))


class _PrincipalBaseProxy(PrincipalBase):
    @jsii.member(jsii_name="dedupeString")
    def dedupe_string(self) -> typing.Optional[builtins.str]:
        '''Return whether or not this principal is equal to the given principal.'''
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "dedupeString", []))

    @builtins.property
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> PrincipalPolicyFragment:
        '''Return the policy fragment that identifies this principal in a Policy.'''
        return typing.cast(PrincipalPolicyFragment, jsii.get(self, "policyFragment"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, PrincipalBase).__jsii_proxy_class__ = lambda : _PrincipalBaseProxy


class PrincipalWithConditions(
    PrincipalBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.PrincipalWithConditions",
):
    '''An IAM principal with additional conditions specifying when the policy is in effect.

    For more information about conditions, see:
    https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iam as iam
        
        # conditions: Any
        # principal: iam.IPrincipal
        
        principal_with_conditions = iam.PrincipalWithConditions(principal, {
            "conditions_key": conditions
        })
    '''

    def __init__(
        self,
        principal: IPrincipal,
        conditions: typing.Mapping[builtins.str, typing.Any],
    ) -> None:
        '''
        :param principal: -
        :param conditions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80467c10f35d2de95737da2b6bd8a1e49b25ad1cbfddc90cf983335b0fdcb0e6)
            check_type(argname="argument principal", value=principal, expected_type=type_hints["principal"])
            check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
        jsii.create(self.__class__, self, [principal, conditions])

    @jsii.member(jsii_name="addCondition")
    def add_condition(self, key: builtins.str, value: typing.Any) -> None:
        '''Add a condition to the principal.

        :param key: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4453baead1238307d35f2c6280eb8ee8b9d8b2c69fd3bc1a186637187dfc8ebb)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "addCondition", [key, value]))

    @jsii.member(jsii_name="addConditions")
    def add_conditions(
        self,
        conditions: typing.Mapping[builtins.str, typing.Any],
    ) -> None:
        '''Adds multiple conditions to the principal.

        Values from the conditions parameter will overwrite existing values with the same operator
        and key.

        :param conditions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06f98d5139c999f6bf39f7d3b6b83cf4b629160f211cfac70b66df210aafd59c)
            check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
        return typing.cast(None, jsii.invoke(self, "addConditions", [conditions]))

    @jsii.member(jsii_name="addToAssumeRolePolicy")
    def add_to_assume_role_policy(self, doc: PolicyDocument) -> None:
        '''Add the principal to the AssumeRolePolicyDocument.

        Add the statements to the AssumeRolePolicyDocument necessary to give this principal
        permissions to assume the given role.

        :param doc: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f3b5797da3ed30fffb5a07fdbc780cf2bb80f8c955f12f28429742fe81076d9)
            check_type(argname="argument doc", value=doc, expected_type=type_hints["doc"])
        return typing.cast(None, jsii.invoke(self, "addToAssumeRolePolicy", [doc]))

    @jsii.member(jsii_name="addToPolicy")
    def add_to_policy(self, statement: PolicyStatement) -> builtins.bool:
        '''Add to the policy of this principal.

        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de4963000e34b16a5638f4c44067171e566faa24c22a4a7cc74d90b52ec2976a)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(builtins.bool, jsii.invoke(self, "addToPolicy", [statement]))

    @jsii.member(jsii_name="addToPrincipalPolicy")
    def add_to_principal_policy(
        self,
        statement: PolicyStatement,
    ) -> AddToPrincipalPolicyResult:
        '''Add to the policy of this principal.

        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc14ce5e667818ff09808b3d56342245457ad7af45baf54098e3554bdfbb9c5d)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(AddToPrincipalPolicyResult, jsii.invoke(self, "addToPrincipalPolicy", [statement]))

    @jsii.member(jsii_name="appendDedupe")
    def _append_dedupe(self, append: builtins.str) -> typing.Optional[builtins.str]:
        '''Append the given string to the wrapped principal's dedupe string (if available).

        :param append: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c48145b0627d702d4a653d7ea8b27af46eec5c5caee28fa1b477e7a6b7ee9b6)
            check_type(argname="argument append", value=append, expected_type=type_hints["append"])
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "appendDedupe", [append]))

    @jsii.member(jsii_name="dedupeString")
    def dedupe_string(self) -> typing.Optional[builtins.str]:
        '''Return whether or not this principal is equal to the given principal.'''
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "dedupeString", []))

    @jsii.member(jsii_name="toJSON")
    def to_json(self) -> typing.Mapping[builtins.str, typing.List[builtins.str]]:
        '''JSON-ify the principal.

        Used when JSON.stringify() is called
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.List[builtins.str]], jsii.invoke(self, "toJSON", []))

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''Returns a string representation of an object.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @builtins.property
    @jsii.member(jsii_name="assumeRoleAction")
    def assume_role_action(self) -> builtins.str:
        '''When this Principal is used in an AssumeRole policy, the action to use.'''
        return typing.cast(builtins.str, jsii.get(self, "assumeRoleAction"))

    @builtins.property
    @jsii.member(jsii_name="conditions")
    def conditions(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''The conditions under which the policy is in effect.

        See `the IAM documentation <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html>`_.
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "conditions"))

    @builtins.property
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> PrincipalPolicyFragment:
        '''Return the policy fragment that identifies this principal in a Policy.'''
        return typing.cast(PrincipalPolicyFragment, jsii.get(self, "policyFragment"))

    @builtins.property
    @jsii.member(jsii_name="principalAccount")
    def principal_account(self) -> typing.Optional[builtins.str]:
        '''The AWS account ID of this principal.

        Can be undefined when the account is not known
        (for example, for service principals).
        Can be a Token - in that case,
        it's assumed to be AWS::AccountId.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "principalAccount"))


@jsii.implements(IRole)
class Role(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.Role",
):
    '''IAM Role.

    Defines an IAM role. The role is created with an assume policy document associated with
    the specified AWS service principal defined in ``serviceAssumeRole``.

    :exampleMetadata: infused

    Example::

        # definition: sfn.IChainable
        role = iam.Role(self, "Role",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com")
        )
        state_machine = sfn.StateMachine(self, "StateMachine",
            definition_body=sfn.DefinitionBody.from_chainable(definition)
        )
        
        # Give role permission to get execution history of ALL executions for the state machine
        state_machine.grant_execution(role, "states:GetExecutionHistory")
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        assumed_by: IPrincipal,
        description: typing.Optional[builtins.str] = None,
        external_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        inline_policies: typing.Optional[typing.Mapping[builtins.str, PolicyDocument]] = None,
        managed_policies: typing.Optional[typing.Sequence[IManagedPolicy]] = None,
        max_session_duration: typing.Optional[_Duration_4839e8c3] = None,
        path: typing.Optional[builtins.str] = None,
        permissions_boundary: typing.Optional[IManagedPolicy] = None,
        role_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param assumed_by: The IAM principal (i.e. ``new ServicePrincipal('sns.amazonaws.com')``) which can assume this role. You can later modify the assume role policy document by accessing it via the ``assumeRolePolicy`` property.
        :param description: A description of the role. It can be up to 1000 characters long. Default: - No description.
        :param external_ids: List of IDs that the role assumer needs to provide one of when assuming this role. If the configured and provided external IDs do not match, the AssumeRole operation will fail. Default: No external ID required
        :param inline_policies: A list of named policies to inline into this role. These policies will be created with the role, whereas those added by ``addToPolicy`` are added using a separate CloudFormation resource (allowing a way around circular dependencies that could otherwise be introduced). Default: - No policy is inlined in the Role resource.
        :param managed_policies: A list of managed policies associated with this role. You can add managed policies later using ``addManagedPolicy(ManagedPolicy.fromAwsManagedPolicyName(policyName))``. Default: - No managed policies.
        :param max_session_duration: The maximum session duration that you want to set for the specified role. This setting can have a value from 1 hour (3600sec) to 12 (43200sec) hours. Anyone who assumes the role from the AWS CLI or API can use the DurationSeconds API parameter or the duration-seconds CLI parameter to request a longer session. The MaxSessionDuration setting determines the maximum duration that can be requested using the DurationSeconds parameter. If users don't specify a value for the DurationSeconds parameter, their security credentials are valid for one hour by default. This applies when you use the AssumeRole* API operations or the assume-role* CLI operations but does not apply when you use those operations to create a console URL. Default: Duration.hours(1)
        :param path: The path associated with this role. For information about IAM paths, see Friendly Names and Paths in IAM User Guide. Default: /
        :param permissions_boundary: AWS supports permissions boundaries for IAM entities (users or roles). A permissions boundary is an advanced feature for using a managed policy to set the maximum permissions that an identity-based policy can grant to an IAM entity. An entity's permissions boundary allows it to perform only the actions that are allowed by both its identity-based policies and its permissions boundaries. Default: - No permissions boundary.
        :param role_name: A name for the IAM role. For valid values, see the RoleName parameter for the CreateRole action in the IAM API Reference. IMPORTANT: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name. If you specify a name, you must specify the CAPABILITY_NAMED_IAM value to acknowledge your template's capabilities. For more information, see Acknowledging IAM Resources in AWS CloudFormation Templates. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the role name.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efe80cc42a362ee0de99d64f7cf860226cb252074012ad3a5ff62f47ec94abae)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = RoleProps(
            assumed_by=assumed_by,
            description=description,
            external_ids=external_ids,
            inline_policies=inline_policies,
            managed_policies=managed_policies,
            max_session_duration=max_session_duration,
            path=path,
            permissions_boundary=permissions_boundary,
            role_name=role_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="customizeRoles")
    @builtins.classmethod
    def customize_roles(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        *,
        prevent_synthesis: typing.Optional[builtins.bool] = None,
        use_precreated_roles: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Customize the creation of IAM roles within the given scope.

        It is recommended that you **do not** use this method and instead allow
        CDK to manage role creation. This should only be used
        in environments where CDK applications are not allowed to created IAM roles.

        This can be used to prevent the CDK application from creating roles
        within the given scope and instead replace the references to the roles with
        precreated role names. A report will be synthesized in the cloud assembly (i.e. cdk.out)
        that will contain the list of IAM roles that would have been created along with the
        IAM policy statements that the role should contain. This report can then be used
        to create the IAM roles outside of CDK and then the created role names can be provided
        in ``usePrecreatedRoles``.

        :param scope: construct scope to customize role creation.
        :param prevent_synthesis: Whether or not to synthesize the resource into the CFN template. Set this to ``false`` if you still want to create the resources *and* you also want to create the policy report. Default: true
        :param use_precreated_roles: A list of precreated IAM roles to substitute for roles that CDK is creating. The constructPath can be either a relative or absolute path from the scope that ``customizeRoles`` is used on to the role being created. Default: - there are no precreated roles. Synthesis will fail if ``preventSynthesis=true``

        Example::

            # app: App
            
            iam.Role.customize_roles(app,
                use_precreated_roles={
                    "ConstructPath/To/Role": "my-precreated-role-name"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3abda5df0b9e172ab6b6506372119fbc1518a3e56245c4130fbbbd57373a8cb5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        options = CustomizeRolesOptions(
            prevent_synthesis=prevent_synthesis,
            use_precreated_roles=use_precreated_roles,
        )

        return typing.cast(None, jsii.sinvoke(cls, "customizeRoles", [scope, options]))

    @jsii.member(jsii_name="fromRoleArn")
    @builtins.classmethod
    def from_role_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        role_arn: builtins.str,
        *,
        add_grants_to_resources: typing.Optional[builtins.bool] = None,
        default_policy_name: typing.Optional[builtins.str] = None,
        mutable: typing.Optional[builtins.bool] = None,
    ) -> IRole:
        '''Import an external role by ARN.

        If the imported Role ARN is a Token (such as a
        ``CfnParameter.valueAsString`` or a ``Fn.importValue()``) *and* the referenced
        role has a ``path`` (like ``arn:...:role/AdminRoles/Alice``), the
        ``roleName`` property will not resolve to the correct value. Instead it
        will resolve to the first path component. We unfortunately cannot express
        the correct calculation of the full path name as a CloudFormation
        expression. In this scenario the Role ARN should be supplied without the
        ``path`` in order to resolve the correct role resource.

        :param scope: construct scope.
        :param id: construct id.
        :param role_arn: the ARN of the role to import.
        :param add_grants_to_resources: For immutable roles: add grants to resources instead of dropping them. If this is ``false`` or not specified, grant permissions added to this role are ignored. It is your own responsibility to make sure the role has the required permissions. If this is ``true``, any grant permissions will be added to the resource instead. Default: false
        :param default_policy_name: Any policies created by this role will use this value as their ID, if specified. Specify this if importing the same role in multiple stacks, and granting it different permissions in at least two stacks. If this is not specified (or if the same name is specified in more than one stack), a CloudFormation issue will result in the policy created in whichever stack is deployed last overwriting the policies created by the others. Default: 'Policy'
        :param mutable: Whether the imported role can be modified by attaching policy resources to it. Default: true
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c43d6c30d91c1507a4d83080c4d03e80839da9ab22909456251bc529eb41a48)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        options = FromRoleArnOptions(
            add_grants_to_resources=add_grants_to_resources,
            default_policy_name=default_policy_name,
            mutable=mutable,
        )

        return typing.cast(IRole, jsii.sinvoke(cls, "fromRoleArn", [scope, id, role_arn, options]))

    @jsii.member(jsii_name="fromRoleName")
    @builtins.classmethod
    def from_role_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        role_name: builtins.str,
        *,
        add_grants_to_resources: typing.Optional[builtins.bool] = None,
        default_policy_name: typing.Optional[builtins.str] = None,
        mutable: typing.Optional[builtins.bool] = None,
    ) -> IRole:
        '''Import an external role by name.

        The imported role is assumed to exist in the same account as the account
        the scope's containing Stack is being deployed to.

        :param scope: construct scope.
        :param id: construct id.
        :param role_name: the name of the role to import.
        :param add_grants_to_resources: For immutable roles: add grants to resources instead of dropping them. If this is ``false`` or not specified, grant permissions added to this role are ignored. It is your own responsibility to make sure the role has the required permissions. If this is ``true``, any grant permissions will be added to the resource instead. Default: false
        :param default_policy_name: Any policies created by this role will use this value as their ID, if specified. Specify this if importing the same role in multiple stacks, and granting it different permissions in at least two stacks. If this is not specified (or if the same name is specified in more than one stack), a CloudFormation issue will result in the policy created in whichever stack is deployed last overwriting the policies created by the others. Default: 'Policy'
        :param mutable: Whether the imported role can be modified by attaching policy resources to it. Default: true
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ea076ee8cb2b2334bd316dea50996363cb2544fbad031a486b3c1d584e2a0aa)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument role_name", value=role_name, expected_type=type_hints["role_name"])
        options = FromRoleNameOptions(
            add_grants_to_resources=add_grants_to_resources,
            default_policy_name=default_policy_name,
            mutable=mutable,
        )

        return typing.cast(IRole, jsii.sinvoke(cls, "fromRoleName", [scope, id, role_name, options]))

    @jsii.member(jsii_name="isRole")
    @builtins.classmethod
    def is_role(cls, x: typing.Any) -> builtins.bool:
        '''Return whether the given object is a Role.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40a28d979d193e374e71b2cd587b8f95f7bbca459116e6d16c987738134119fe)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isRole", [x]))

    @jsii.member(jsii_name="addManagedPolicy")
    def add_managed_policy(self, policy: IManagedPolicy) -> None:
        '''Attaches a managed policy to this role.

        :param policy: The the managed policy to attach.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b3ebdee2cbdf8c694d4ae443ef5b2e0d8fa417a4913c0abb90a83eb91dc3733)
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
        return typing.cast(None, jsii.invoke(self, "addManagedPolicy", [policy]))

    @jsii.member(jsii_name="addToPolicy")
    def add_to_policy(self, statement: PolicyStatement) -> builtins.bool:
        '''Add to the policy of this principal.

        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__138765eba0bce05f18e74c04f9874eca5b353ef80b5afc6a733d36c809ed5a25)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(builtins.bool, jsii.invoke(self, "addToPolicy", [statement]))

    @jsii.member(jsii_name="addToPrincipalPolicy")
    def add_to_principal_policy(
        self,
        statement: PolicyStatement,
    ) -> AddToPrincipalPolicyResult:
        '''Adds a permission to the role's default policy document.

        If there is no default policy attached to this role, it will be created.

        :param statement: The permission statement to add to the policy document.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6168031f65ea6f5bbc6ae6d7207de3c8b2039038e0a8ddec4cc0db5ef919299d)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(AddToPrincipalPolicyResult, jsii.invoke(self, "addToPrincipalPolicy", [statement]))

    @jsii.member(jsii_name="attachInlinePolicy")
    def attach_inline_policy(self, policy: Policy) -> None:
        '''Attaches a policy to this role.

        :param policy: The policy to attach.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6daee5d0cd9791a7321d18f729dc2d93548a8a15705bd861a902bd0dbae73cf6)
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
        return typing.cast(None, jsii.invoke(self, "attachInlinePolicy", [policy]))

    @jsii.member(jsii_name="grant")
    def grant(self, grantee: IPrincipal, *actions: builtins.str) -> Grant:
        '''Grant the actions defined in actions to the identity Principal on this resource.

        :param grantee: -
        :param actions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14c932caa1eadf56fd976a12545a5f150425c6f5a3ea878d9bb6ff0b3e24cd46)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(Grant, jsii.invoke(self, "grant", [grantee, *actions]))

    @jsii.member(jsii_name="grantAssumeRole")
    def grant_assume_role(self, identity: IPrincipal) -> Grant:
        '''Grant permissions to the given principal to assume this role.

        :param identity: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e41637797f37e9e841bf058d39d0b910ed287ffbdcfeb24f7652a386a18b61e)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(Grant, jsii.invoke(self, "grantAssumeRole", [identity]))

    @jsii.member(jsii_name="grantPassRole")
    def grant_pass_role(self, identity: IPrincipal) -> Grant:
        '''Grant permissions to the given principal to pass this role.

        :param identity: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ac7870e7ae4f160829d1eaf7f6d20c937b9c938e96709e254eb1422b6989700)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(Grant, jsii.invoke(self, "grantPassRole", [identity]))

    @jsii.member(jsii_name="withoutPolicyUpdates")
    def without_policy_updates(
        self,
        *,
        add_grants_to_resources: typing.Optional[builtins.bool] = None,
    ) -> IRole:
        '''Return a copy of this Role object whose Policies will not be updated.

        Use the object returned by this method if you want this Role to be used by
        a construct without it automatically updating the Role's Policies.

        If you do, you are responsible for adding the correct statements to the
        Role's policies yourself.

        :param add_grants_to_resources: Add grants to resources instead of dropping them. If this is ``false`` or not specified, grant permissions added to this role are ignored. It is your own responsibility to make sure the role has the required permissions. If this is ``true``, any grant permissions will be added to the resource instead. Default: false
        '''
        options = WithoutPolicyUpdatesOptions(
            add_grants_to_resources=add_grants_to_resources
        )

        return typing.cast(IRole, jsii.invoke(self, "withoutPolicyUpdates", [options]))

    @builtins.property
    @jsii.member(jsii_name="assumeRoleAction")
    def assume_role_action(self) -> builtins.str:
        '''When this Principal is used in an AssumeRole policy, the action to use.'''
        return typing.cast(builtins.str, jsii.get(self, "assumeRoleAction"))

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> IPrincipal:
        '''The principal to grant permissions to.'''
        return typing.cast(IPrincipal, jsii.get(self, "grantPrincipal"))

    @builtins.property
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> PrincipalPolicyFragment:
        '''Returns the role.'''
        return typing.cast(PrincipalPolicyFragment, jsii.get(self, "policyFragment"))

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''Returns the ARN of this role.'''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @builtins.property
    @jsii.member(jsii_name="roleId")
    def role_id(self) -> builtins.str:
        '''Returns the stable and unique string identifying the role.

        For example,
        AIDAJQABLZS4A3QDU576Q.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleId"))

    @builtins.property
    @jsii.member(jsii_name="roleName")
    def role_name(self) -> builtins.str:
        '''Returns the name of the role.'''
        return typing.cast(builtins.str, jsii.get(self, "roleName"))

    @builtins.property
    @jsii.member(jsii_name="assumeRolePolicy")
    def assume_role_policy(self) -> typing.Optional[PolicyDocument]:
        '''The assume role policy document associated with this role.'''
        return typing.cast(typing.Optional[PolicyDocument], jsii.get(self, "assumeRolePolicy"))

    @builtins.property
    @jsii.member(jsii_name="permissionsBoundary")
    def permissions_boundary(self) -> typing.Optional[IManagedPolicy]:
        '''Returns the permissions boundary attached to this role.'''
        return typing.cast(typing.Optional[IManagedPolicy], jsii.get(self, "permissionsBoundary"))

    @builtins.property
    @jsii.member(jsii_name="principalAccount")
    def principal_account(self) -> typing.Optional[builtins.str]:
        '''The AWS account ID of this principal.

        Can be undefined when the account is not known
        (for example, for service principals).
        Can be a Token - in that case,
        it's assumed to be AWS::AccountId.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "principalAccount"))


class ServicePrincipal(
    PrincipalBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.ServicePrincipal",
):
    '''An IAM principal that represents an AWS service (i.e. ``sqs.amazonaws.com``).

    :exampleMetadata: infused

    Example::

        lambda_role = iam.Role(self, "Role",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            description="Example role..."
        )
        
        stream = kinesis.Stream(self, "MyEncryptedStream",
            encryption=kinesis.StreamEncryption.KMS
        )
        
        # give lambda permissions to read stream
        stream.grant_read(lambda_role)
    '''

    def __init__(
        self,
        service: builtins.str,
        *,
        conditions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Reference an AWS service, optionally in a given region.

        :param service: AWS service (i.e. sqs.amazonaws.com).
        :param conditions: Additional conditions to add to the Service Principal. Default: - No conditions
        :param region: The region in which you want to reference the service. This is only necessary for *cross-region* references to *opt-in* regions. In those cases, the region name needs to be included to reference the correct service principal. In all other cases, the global service principal name is sufficient. This field behaves differently depending on whether the ``@aws-cdk/aws-iam:standardizedServicePrincipals`` flag is set or not: - If the flag is set, the input service principal is assumed to be of the form ``SERVICE.amazonaws.com``. That value will always be returned, unless the given region is an opt-in region and the service principal is rendered in a stack in a different region, in which case ``SERVICE.REGION.amazonaws.com`` will be rendered. Under this regime, there is no downside to always specifying the region property: it will be rendered only if necessary. - If the flag is not set, the service principal will resolve to a single principal whose name comes from the ``@aws-cdk/region-info`` package, using the region to override the stack region. If there is no entry for this service principal in the database,, the input service name is returned literally. This is legacy behavior and is not recommended. Default: - the resolving Stack's region.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2745f75caaf5bf82ce9582f03d25e19c93145745996ad93d343457dd927d8007)
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
        opts = ServicePrincipalOpts(conditions=conditions, region=region)

        jsii.create(self.__class__, self, [service, opts])

    @jsii.member(jsii_name="servicePrincipalName")
    @builtins.classmethod
    def service_principal_name(cls, service: builtins.str) -> builtins.str:
        '''Return the service principal name based on the region it's used in.

        Some service principal names used to be different for different partitions,
        and some were not. This method would return the appropriate region-specific
        service principal name, getting that information from the ``region-info``
        module.

        These days all service principal names are standardized, and they are all
        of the form ``<servicename>.amazonaws.com``.

        If the feature flag ``@aws-cdk/aws-iam:standardizedServicePrincipals`` is set, this
        method will always return its input. If this feature flag is not set, this
        method will perform the legacy behavior, which appends the region-specific
        domain suffix for some select services (for example, it would append ``.cn``
        to some service principal names).

        :param service: -

        Example::

            principal_name = iam.ServicePrincipal.service_principal_name("ec2.amazonaws.com")
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb337dcddbd70acf0d25c8d6f2b9ec2e9bae9105c6aa6db67b9a3c2354bf684b)
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "servicePrincipalName", [service]))

    @jsii.member(jsii_name="dedupeString")
    def dedupe_string(self) -> typing.Optional[builtins.str]:
        '''Return whether or not this principal is equal to the given principal.'''
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "dedupeString", []))

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''Returns a string representation of an object.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @builtins.property
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> PrincipalPolicyFragment:
        '''Return the policy fragment that identifies this principal in a Policy.'''
        return typing.cast(PrincipalPolicyFragment, jsii.get(self, "policyFragment"))

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        '''AWS service (i.e. sqs.amazonaws.com).'''
        return typing.cast(builtins.str, jsii.get(self, "service"))


class SessionTagsPrincipal(
    PrincipalBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.SessionTagsPrincipal",
):
    '''Enables session tags on role assumptions from a principal.

    For more information on session tags, see:
    https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iam as iam
        
        # principal: iam.IPrincipal
        
        session_tags_principal = iam.SessionTagsPrincipal(principal)
    '''

    def __init__(self, principal: IPrincipal) -> None:
        '''
        :param principal: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__215a039cacc00cbccb40418a20fcc0e80fb7dd31e57c9d0c0d0356a9a790712d)
            check_type(argname="argument principal", value=principal, expected_type=type_hints["principal"])
        jsii.create(self.__class__, self, [principal])

    @jsii.member(jsii_name="addToAssumeRolePolicy")
    def add_to_assume_role_policy(self, doc: PolicyDocument) -> None:
        '''Add the principal to the AssumeRolePolicyDocument.

        Add the statements to the AssumeRolePolicyDocument necessary to give this principal
        permissions to assume the given role.

        :param doc: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25844b9c8aff78b5d8d0dcc4f9fc6ccfe89e32ec78de55d3ce8260e20bdaefbc)
            check_type(argname="argument doc", value=doc, expected_type=type_hints["doc"])
        return typing.cast(None, jsii.invoke(self, "addToAssumeRolePolicy", [doc]))

    @jsii.member(jsii_name="addToPolicy")
    def add_to_policy(self, statement: PolicyStatement) -> builtins.bool:
        '''Add to the policy of this principal.

        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ce41cc2346f2ebbd7c1e4b4722e1ee8d346119ac63045afc316c940631f9141)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(builtins.bool, jsii.invoke(self, "addToPolicy", [statement]))

    @jsii.member(jsii_name="addToPrincipalPolicy")
    def add_to_principal_policy(
        self,
        statement: PolicyStatement,
    ) -> AddToPrincipalPolicyResult:
        '''Add to the policy of this principal.

        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbc62d90b05edca6f8d13d813c28fe7dc43759fba6779d5577f60de0344b39f2)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(AddToPrincipalPolicyResult, jsii.invoke(self, "addToPrincipalPolicy", [statement]))

    @jsii.member(jsii_name="appendDedupe")
    def _append_dedupe(self, append: builtins.str) -> typing.Optional[builtins.str]:
        '''Append the given string to the wrapped principal's dedupe string (if available).

        :param append: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f6570adbc6df85f505162eefc0b9a41164dc55f58d0ed93c10d47d5a1ecd669)
            check_type(argname="argument append", value=append, expected_type=type_hints["append"])
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "appendDedupe", [append]))

    @jsii.member(jsii_name="dedupeString")
    def dedupe_string(self) -> typing.Optional[builtins.str]:
        '''Return whether or not this principal is equal to the given principal.'''
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "dedupeString", []))

    @builtins.property
    @jsii.member(jsii_name="assumeRoleAction")
    def assume_role_action(self) -> builtins.str:
        '''When this Principal is used in an AssumeRole policy, the action to use.'''
        return typing.cast(builtins.str, jsii.get(self, "assumeRoleAction"))

    @builtins.property
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> PrincipalPolicyFragment:
        '''Return the policy fragment that identifies this principal in a Policy.'''
        return typing.cast(PrincipalPolicyFragment, jsii.get(self, "policyFragment"))

    @builtins.property
    @jsii.member(jsii_name="principalAccount")
    def principal_account(self) -> typing.Optional[builtins.str]:
        '''The AWS account ID of this principal.

        Can be undefined when the account is not known
        (for example, for service principals).
        Can be a Token - in that case,
        it's assumed to be AWS::AccountId.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "principalAccount"))


class StarPrincipal(
    PrincipalBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.StarPrincipal",
):
    '''A principal that uses a literal '*' in the IAM JSON language.

    Some services behave differently when you specify ``Principal: "*"``
    or ``Principal: { AWS: "*" }`` in their resource policy.

    ``StarPrincipal`` renders to ``Principal: *``. Most of the time, you
    should use ``AnyPrincipal`` instead.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iam as iam
        
        star_principal = iam.StarPrincipal()
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="dedupeString")
    def dedupe_string(self) -> typing.Optional[builtins.str]:
        '''Return whether or not this principal is equal to the given principal.'''
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "dedupeString", []))

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''Returns a string representation of an object.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @builtins.property
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> PrincipalPolicyFragment:
        '''Return the policy fragment that identifies this principal in a Policy.'''
        return typing.cast(PrincipalPolicyFragment, jsii.get(self, "policyFragment"))


@jsii.implements(IIdentity, IUser)
class User(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.User",
):
    '''Define a new IAM user.

    :exampleMetadata: infused

    Example::

        # definition: sfn.IChainable
        user = iam.User(self, "MyUser")
        state_machine = sfn.StateMachine(self, "StateMachine",
            definition_body=sfn.DefinitionBody.from_chainable(definition)
        )
        
        # give user permission to send task success to the state machine
        state_machine.grant(user, "states:SendTaskSuccess")
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        groups: typing.Optional[typing.Sequence["IGroup"]] = None,
        managed_policies: typing.Optional[typing.Sequence[IManagedPolicy]] = None,
        password: typing.Optional[_SecretValue_3dd0ddae] = None,
        password_reset_required: typing.Optional[builtins.bool] = None,
        path: typing.Optional[builtins.str] = None,
        permissions_boundary: typing.Optional[IManagedPolicy] = None,
        user_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param groups: Groups to add this user to. You can also use ``addToGroup`` to add this user to a group. Default: - No groups.
        :param managed_policies: A list of managed policies associated with this role. You can add managed policies later using ``addManagedPolicy(ManagedPolicy.fromAwsManagedPolicyName(policyName))``. Default: - No managed policies.
        :param password: The password for the user. This is required so the user can access the AWS Management Console. You can use ``SecretValue.unsafePlainText`` to specify a password in plain text or use ``secretsmanager.Secret.fromSecretAttributes`` to reference a secret in Secrets Manager. Default: - User won't be able to access the management console without a password.
        :param password_reset_required: Specifies whether the user is required to set a new password the next time the user logs in to the AWS Management Console. If this is set to 'true', you must also specify "initialPassword". Default: false
        :param path: The path for the user name. For more information about paths, see IAM Identifiers in the IAM User Guide. Default: /
        :param permissions_boundary: AWS supports permissions boundaries for IAM entities (users or roles). A permissions boundary is an advanced feature for using a managed policy to set the maximum permissions that an identity-based policy can grant to an IAM entity. An entity's permissions boundary allows it to perform only the actions that are allowed by both its identity-based policies and its permissions boundaries. Default: - No permissions boundary.
        :param user_name: A name for the IAM user. For valid values, see the UserName parameter for the CreateUser action in the IAM API Reference. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the user name. If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name. If you specify a name, you must specify the CAPABILITY_NAMED_IAM value to acknowledge your template's capabilities. For more information, see Acknowledging IAM Resources in AWS CloudFormation Templates. Default: - Generated by CloudFormation (recommended)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef7259f99a29e3c7c58c43ee586670c112f44b42e5364d12a09a03f3e23e008f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = UserProps(
            groups=groups,
            managed_policies=managed_policies,
            password=password,
            password_reset_required=password_reset_required,
            path=path,
            permissions_boundary=permissions_boundary,
            user_name=user_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromUserArn")
    @builtins.classmethod
    def from_user_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        user_arn: builtins.str,
    ) -> IUser:
        '''Import an existing user given a user ARN.

        If the ARN comes from a Token, the User cannot have a path; if so, any attempt
        to reference its username will fail.

        :param scope: construct scope.
        :param id: construct id.
        :param user_arn: the ARN of an existing user to import.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f33e29e061af19beff293732951c7a6d99741716ad9f7bc86023959d5cdd535d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument user_arn", value=user_arn, expected_type=type_hints["user_arn"])
        return typing.cast(IUser, jsii.sinvoke(cls, "fromUserArn", [scope, id, user_arn]))

    @jsii.member(jsii_name="fromUserAttributes")
    @builtins.classmethod
    def from_user_attributes(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        user_arn: builtins.str,
    ) -> IUser:
        '''Import an existing user given user attributes.

        If the ARN comes from a Token, the User cannot have a path; if so, any attempt
        to reference its username will fail.

        :param scope: construct scope.
        :param id: construct id.
        :param user_arn: The ARN of the user. Format: arn::iam:::user/
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5958a1f11a99684a3e852867fdde9311b58b9cddac80d1d8960f16a03f113e2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = UserAttributes(user_arn=user_arn)

        return typing.cast(IUser, jsii.sinvoke(cls, "fromUserAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="fromUserName")
    @builtins.classmethod
    def from_user_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        user_name: builtins.str,
    ) -> IUser:
        '''Import an existing user given a username.

        :param scope: construct scope.
        :param id: construct id.
        :param user_name: the username of the existing user to import.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b8c426fc5ef927d751eda7ff78c09000e89b63da6804dc345c76e762568b602)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
        return typing.cast(IUser, jsii.sinvoke(cls, "fromUserName", [scope, id, user_name]))

    @jsii.member(jsii_name="addManagedPolicy")
    def add_managed_policy(self, policy: IManagedPolicy) -> None:
        '''Attaches a managed policy to the user.

        :param policy: The managed policy to attach.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7748f62b253a3a856fa72ad5ed5a163b0c9bc0cdf07e2c6fbb666420c4caf464)
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
        return typing.cast(None, jsii.invoke(self, "addManagedPolicy", [policy]))

    @jsii.member(jsii_name="addToGroup")
    def add_to_group(self, group: "IGroup") -> None:
        '''Adds this user to a group.

        :param group: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31a18f03acf086224c5283fb04241844d012d625b3226dc86059d3dbe23841a1)
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
        return typing.cast(None, jsii.invoke(self, "addToGroup", [group]))

    @jsii.member(jsii_name="addToPolicy")
    def add_to_policy(self, statement: PolicyStatement) -> builtins.bool:
        '''Add to the policy of this principal.

        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc9d48f42d89386c4c39fee9b294cf26d7165fba930b228997d4f866ec04a340)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(builtins.bool, jsii.invoke(self, "addToPolicy", [statement]))

    @jsii.member(jsii_name="addToPrincipalPolicy")
    def add_to_principal_policy(
        self,
        statement: PolicyStatement,
    ) -> AddToPrincipalPolicyResult:
        '''Adds an IAM statement to the default policy.

        :param statement: -

        :return: true
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__add40848d812b2b19e71bd4e186b890cfd72dfc35ae18ae5733132e665b366a6)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(AddToPrincipalPolicyResult, jsii.invoke(self, "addToPrincipalPolicy", [statement]))

    @jsii.member(jsii_name="attachInlinePolicy")
    def attach_inline_policy(self, policy: Policy) -> None:
        '''Attaches a policy to this user.

        :param policy: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ebb8924f05370c7968859fd9c4bc9b3ab97a7fcbee56ddd82313a0a6038f3d0)
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
        return typing.cast(None, jsii.invoke(self, "attachInlinePolicy", [policy]))

    @builtins.property
    @jsii.member(jsii_name="assumeRoleAction")
    def assume_role_action(self) -> builtins.str:
        '''When this Principal is used in an AssumeRole policy, the action to use.'''
        return typing.cast(builtins.str, jsii.get(self, "assumeRoleAction"))

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> IPrincipal:
        '''The principal to grant permissions to.'''
        return typing.cast(IPrincipal, jsii.get(self, "grantPrincipal"))

    @builtins.property
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> PrincipalPolicyFragment:
        '''Return the policy fragment that identifies this principal in a Policy.'''
        return typing.cast(PrincipalPolicyFragment, jsii.get(self, "policyFragment"))

    @builtins.property
    @jsii.member(jsii_name="userArn")
    def user_arn(self) -> builtins.str:
        '''An attribute that represents the user's ARN.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "userArn"))

    @builtins.property
    @jsii.member(jsii_name="userName")
    def user_name(self) -> builtins.str:
        '''An attribute that represents the user name.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "userName"))

    @builtins.property
    @jsii.member(jsii_name="permissionsBoundary")
    def permissions_boundary(self) -> typing.Optional[IManagedPolicy]:
        '''Returns the permissions boundary attached  to this user.'''
        return typing.cast(typing.Optional[IManagedPolicy], jsii.get(self, "permissionsBoundary"))

    @builtins.property
    @jsii.member(jsii_name="principalAccount")
    def principal_account(self) -> typing.Optional[builtins.str]:
        '''The AWS account ID of this principal.

        Can be undefined when the account is not known
        (for example, for service principals).
        Can be a Token - in that case,
        it's assumed to be AWS::AccountId.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "principalAccount"))


class ArnPrincipal(
    PrincipalBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.ArnPrincipal",
):
    '''Specify a principal by the Amazon Resource Name (ARN).

    You can specify AWS accounts, IAM users, Federated SAML users, IAM roles, and specific assumed-role sessions.
    You cannot specify IAM groups or instance profiles as principals

    :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html
    :exampleMetadata: infused

    Example::

        # Option 2: create your custom mastersRole with scoped assumeBy arn as the Cluster prop. Switch to this role from the AWS console.
        from aws_cdk.lambda_layer_kubectl_v29 import KubectlV29Layer
        # vpc: ec2.Vpc
        
        
        masters_role = iam.Role(self, "MastersRole",
            assumed_by=iam.ArnPrincipal("arn_for_trusted_principal")
        )
        
        cluster = eks.Cluster(self, "EksCluster",
            vpc=vpc,
            version=eks.KubernetesVersion.V1_29,
            kubectl_layer=KubectlV29Layer(self, "KubectlLayer"),
            masters_role=masters_role
        )
        
        masters_role.add_to_policy(iam.PolicyStatement(
            actions=["eks:AccessKubernetesApi", "eks:Describe*", "eks:List*"
            ],
            resources=[cluster.cluster_arn]
        ))
    '''

    def __init__(self, arn: builtins.str) -> None:
        '''
        :param arn: Amazon Resource Name (ARN) of the principal entity (i.e. arn:aws:iam::123456789012:user/user-name).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a6d6c32d3e183186382b39b6b11487d115ae752f5ad9109d40863d0f5d49536)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
        jsii.create(self.__class__, self, [arn])

    @jsii.member(jsii_name="dedupeString")
    def dedupe_string(self) -> typing.Optional[builtins.str]:
        '''Return whether or not this principal is equal to the given principal.'''
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "dedupeString", []))

    @jsii.member(jsii_name="inOrganization")
    def in_organization(self, organization_id: builtins.str) -> PrincipalBase:
        '''A convenience method for adding a condition that the principal is part of the specified AWS Organization.

        :param organization_id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4053cc6c8a246179292ae366feb44cbec456a8fe5d81ab3ded5bd52657116d7f)
            check_type(argname="argument organization_id", value=organization_id, expected_type=type_hints["organization_id"])
        return typing.cast(PrincipalBase, jsii.invoke(self, "inOrganization", [organization_id]))

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''Returns a string representation of an object.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        '''Amazon Resource Name (ARN) of the principal entity (i.e. arn:aws:iam::123456789012:user/user-name).'''
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> PrincipalPolicyFragment:
        '''Return the policy fragment that identifies this principal in a Policy.'''
        return typing.cast(PrincipalPolicyFragment, jsii.get(self, "policyFragment"))


class CanonicalUserPrincipal(
    PrincipalBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.CanonicalUserPrincipal",
):
    '''A policy principal for canonicalUserIds - useful for S3 bucket policies that use Origin Access identities.

    See https://docs.aws.amazon.com/general/latest/gr/acct-identifiers.html

    and

    https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html

    for more details.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iam as iam
        
        canonical_user_principal = iam.CanonicalUserPrincipal("canonicalUserId")
    '''

    def __init__(self, canonical_user_id: builtins.str) -> None:
        '''
        :param canonical_user_id: unique identifier assigned by AWS for every account. root user and IAM users for an account all see the same ID. (i.e. 79a59df900b949e55d96a1e698fbacedfd6e09d98eacf8f8d5218e7cd47ef2be)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22e250eb0875ea5bc04b33f170117ce4bdb9a3d40b2e26bdff85831b69831b6f)
            check_type(argname="argument canonical_user_id", value=canonical_user_id, expected_type=type_hints["canonical_user_id"])
        jsii.create(self.__class__, self, [canonical_user_id])

    @jsii.member(jsii_name="dedupeString")
    def dedupe_string(self) -> typing.Optional[builtins.str]:
        '''Return whether or not this principal is equal to the given principal.'''
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "dedupeString", []))

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''Returns a string representation of an object.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @builtins.property
    @jsii.member(jsii_name="canonicalUserId")
    def canonical_user_id(self) -> builtins.str:
        '''unique identifier assigned by AWS for every account.

        root user and IAM users for an account all see the same ID.
        (i.e. 79a59df900b949e55d96a1e698fbacedfd6e09d98eacf8f8d5218e7cd47ef2be)
        '''
        return typing.cast(builtins.str, jsii.get(self, "canonicalUserId"))

    @builtins.property
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> PrincipalPolicyFragment:
        '''Return the policy fragment that identifies this principal in a Policy.'''
        return typing.cast(PrincipalPolicyFragment, jsii.get(self, "policyFragment"))


class CompositePrincipal(
    PrincipalBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.CompositePrincipal",
):
    '''Represents a principal that has multiple types of principals.

    A composite principal cannot
    have conditions. i.e. multiple ServicePrincipals that form a composite principal

    :exampleMetadata: infused

    Example::

        # vpc: ec2.Vpc
        
        role = iam.Role(self, "RDSDirectoryServicesRole",
            assumed_by=iam.CompositePrincipal(
                iam.ServicePrincipal("rds.amazonaws.com"),
                iam.ServicePrincipal("directoryservice.rds.amazonaws.com")),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AmazonRDSDirectoryServiceAccess")
            ]
        )
        instance = rds.DatabaseInstance(self, "Instance",
            engine=rds.DatabaseInstanceEngine.mysql(version=rds.MysqlEngineVersion.VER_8_0_19),
            vpc=vpc,
            domain="d-????????",  # The ID of the domain for the instance to join.
            domain_role=role
        )
    '''

    def __init__(self, *principals: IPrincipal) -> None:
        '''
        :param principals: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab13bb781032f3d9d6e5e0937284451c23201075b7417c49ce544c4414bf41e3)
            check_type(argname="argument principals", value=principals, expected_type=typing.Tuple[type_hints["principals"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        jsii.create(self.__class__, self, [*principals])

    @jsii.member(jsii_name="addPrincipals")
    def add_principals(self, *principals: IPrincipal) -> "CompositePrincipal":
        '''Adds IAM principals to the composite principal.

        Composite principals cannot have
        conditions.

        :param principals: IAM principals that will be added to the composite principal.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d76c23cbda04481b176ab94cd5ee3b4fce9aef14001b0c32d2e77dead6e97197)
            check_type(argname="argument principals", value=principals, expected_type=typing.Tuple[type_hints["principals"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast("CompositePrincipal", jsii.invoke(self, "addPrincipals", [*principals]))

    @jsii.member(jsii_name="addToAssumeRolePolicy")
    def add_to_assume_role_policy(self, doc: PolicyDocument) -> None:
        '''Add the principal to the AssumeRolePolicyDocument.

        Add the statements to the AssumeRolePolicyDocument necessary to give this principal
        permissions to assume the given role.

        :param doc: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a3e58b43a166e7406b94ea031be5cae69807e96df4fcf4693d630bcd8b11551)
            check_type(argname="argument doc", value=doc, expected_type=type_hints["doc"])
        return typing.cast(None, jsii.invoke(self, "addToAssumeRolePolicy", [doc]))

    @jsii.member(jsii_name="dedupeString")
    def dedupe_string(self) -> typing.Optional[builtins.str]:
        '''Return whether or not this principal is equal to the given principal.'''
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "dedupeString", []))

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''Returns a string representation of an object.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @builtins.property
    @jsii.member(jsii_name="assumeRoleAction")
    def assume_role_action(self) -> builtins.str:
        '''When this Principal is used in an AssumeRole policy, the action to use.'''
        return typing.cast(builtins.str, jsii.get(self, "assumeRoleAction"))

    @builtins.property
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> PrincipalPolicyFragment:
        '''Return the policy fragment that identifies this principal in a Policy.'''
        return typing.cast(PrincipalPolicyFragment, jsii.get(self, "policyFragment"))

    @builtins.property
    @jsii.member(jsii_name="principals")
    def principals(self) -> typing.List[IPrincipal]:
        '''Returns the principals that make up the CompositePrincipal.'''
        return typing.cast(typing.List[IPrincipal], jsii.get(self, "principals"))


class FederatedPrincipal(
    PrincipalBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.FederatedPrincipal",
):
    '''Principal entity that represents a federated identity provider such as Amazon Cognito, that can be used to provide temporary security credentials to users who have been authenticated.

    Additional condition keys are available when the temporary security credentials are used to make a request.
    You can use these keys to write policies that limit the access of federated users.

    :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#condition-keys-wif
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iam as iam
        
        # conditions: Any
        
        federated_principal = iam.FederatedPrincipal("federated", {
            "conditions_key": conditions
        }, "assumeRoleAction")
    '''

    def __init__(
        self,
        federated: builtins.str,
        conditions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        assume_role_action: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param federated: federated identity provider (i.e. 'cognito-identity.amazonaws.com' for users authenticated through Cognito).
        :param conditions: -
        :param assume_role_action: When this Principal is used in an AssumeRole policy, the action to use.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c749f64109d7c36ddb9493478d4b0593ab5de546886b36477d9cbf39e486306)
            check_type(argname="argument federated", value=federated, expected_type=type_hints["federated"])
            check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
            check_type(argname="argument assume_role_action", value=assume_role_action, expected_type=type_hints["assume_role_action"])
        jsii.create(self.__class__, self, [federated, conditions, assume_role_action])

    @jsii.member(jsii_name="dedupeString")
    def dedupe_string(self) -> typing.Optional[builtins.str]:
        '''Return whether or not this principal is equal to the given principal.'''
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "dedupeString", []))

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''Returns a string representation of an object.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @builtins.property
    @jsii.member(jsii_name="assumeRoleAction")
    def assume_role_action(self) -> builtins.str:
        '''When this Principal is used in an AssumeRole policy, the action to use.'''
        return typing.cast(builtins.str, jsii.get(self, "assumeRoleAction"))

    @builtins.property
    @jsii.member(jsii_name="conditions")
    def conditions(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''The conditions under which the policy is in effect.

        :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "conditions"))

    @builtins.property
    @jsii.member(jsii_name="federated")
    def federated(self) -> builtins.str:
        '''federated identity provider (i.e. 'cognito-identity.amazonaws.com' for users authenticated through Cognito).'''
        return typing.cast(builtins.str, jsii.get(self, "federated"))

    @builtins.property
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> PrincipalPolicyFragment:
        '''Return the policy fragment that identifies this principal in a Policy.'''
        return typing.cast(PrincipalPolicyFragment, jsii.get(self, "policyFragment"))


@jsii.interface(jsii_type="aws-cdk-lib.aws_iam.IGroup")
class IGroup(IIdentity, typing_extensions.Protocol):
    '''Represents an IAM Group.

    :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html
    '''

    @builtins.property
    @jsii.member(jsii_name="groupArn")
    def group_arn(self) -> builtins.str:
        '''Returns the IAM Group ARN.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="groupName")
    def group_name(self) -> builtins.str:
        '''Returns the IAM Group Name.

        :attribute: true
        '''
        ...


class _IGroupProxy(
    jsii.proxy_for(IIdentity), # type: ignore[misc]
):
    '''Represents an IAM Group.

    :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_iam.IGroup"

    @builtins.property
    @jsii.member(jsii_name="groupArn")
    def group_arn(self) -> builtins.str:
        '''Returns the IAM Group ARN.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "groupArn"))

    @builtins.property
    @jsii.member(jsii_name="groupName")
    def group_name(self) -> builtins.str:
        '''Returns the IAM Group Name.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "groupName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGroup).__jsii_proxy_class__ = lambda : _IGroupProxy


class OrganizationPrincipal(
    PrincipalBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.OrganizationPrincipal",
):
    '''A principal that represents an AWS Organization.

    :exampleMetadata: infused

    Example::

        # Grant permissions to an entire AWS organization
        # fn: lambda.Function
        
        org = iam.OrganizationPrincipal("o-xxxxxxxxxx")
        
        fn.grant_invoke(org)
    '''

    def __init__(self, organization_id: builtins.str) -> None:
        '''
        :param organization_id: The unique identifier (ID) of an organization (i.e. o-12345abcde).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dc4375c7e3b272eef905d1d27c4bd67aa9d9f51ccb424f15955369df5f52edd)
            check_type(argname="argument organization_id", value=organization_id, expected_type=type_hints["organization_id"])
        jsii.create(self.__class__, self, [organization_id])

    @jsii.member(jsii_name="dedupeString")
    def dedupe_string(self) -> typing.Optional[builtins.str]:
        '''Return whether or not this principal is equal to the given principal.'''
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "dedupeString", []))

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''Returns a string representation of an object.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @builtins.property
    @jsii.member(jsii_name="organizationId")
    def organization_id(self) -> builtins.str:
        '''The unique identifier (ID) of an organization (i.e. o-12345abcde).'''
        return typing.cast(builtins.str, jsii.get(self, "organizationId"))

    @builtins.property
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> PrincipalPolicyFragment:
        '''Return the policy fragment that identifies this principal in a Policy.'''
        return typing.cast(PrincipalPolicyFragment, jsii.get(self, "policyFragment"))


class SamlPrincipal(
    FederatedPrincipal,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.SamlPrincipal",
):
    '''Principal entity that represents a SAML federated identity provider.

    :exampleMetadata: infused

    Example::

        provider = iam.SamlProvider(self, "Provider",
            metadata_document=iam.SamlMetadataDocument.from_file("/path/to/saml-metadata-document.xml")
        )
        principal = iam.SamlPrincipal(provider, {
            "StringEquals": {
                "SAML:iss": "issuer"
            }
        })
    '''

    def __init__(
        self,
        saml_provider: ISamlProvider,
        conditions: typing.Mapping[builtins.str, typing.Any],
    ) -> None:
        '''
        :param saml_provider: -
        :param conditions: The conditions under which the policy is in effect.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__703e9a9603562e94536f153d5ccc52492ff19cc38ed968f3b1f3e31592a8ae7f)
            check_type(argname="argument saml_provider", value=saml_provider, expected_type=type_hints["saml_provider"])
            check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
        jsii.create(self.__class__, self, [saml_provider, conditions])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''Returns a string representation of an object.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))


class WebIdentityPrincipal(
    FederatedPrincipal,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.WebIdentityPrincipal",
):
    '''A principal that represents a federated identity provider as Web Identity such as Cognito, Amazon, Facebook, Google, etc.

    :exampleMetadata: infused

    Example::

        principal = iam.WebIdentityPrincipal("cognito-identity.amazonaws.com", {
            "StringEquals": {"cognito-identity.amazonaws.com:aud": "us-east-2:12345678-abcd-abcd-abcd-123456"},
            "ForAnyValue:StringLike": {"cognito-identity.amazonaws.com:amr": "unauthenticated"}
        })
    '''

    def __init__(
        self,
        identity_provider: builtins.str,
        conditions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param identity_provider: identity provider (i.e. 'cognito-identity.amazonaws.com' for users authenticated through Cognito).
        :param conditions: The conditions under which the policy is in effect. See `the IAM documentation <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html>`_.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c81facd20ae242e2b4956594bdbb7a0322ce30953b66f3849bf4961e03e6f7ba)
            check_type(argname="argument identity_provider", value=identity_provider, expected_type=type_hints["identity_provider"])
            check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
        jsii.create(self.__class__, self, [identity_provider, conditions])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''Returns a string representation of an object.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @builtins.property
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> PrincipalPolicyFragment:
        '''Return the policy fragment that identifies this principal in a Policy.'''
        return typing.cast(PrincipalPolicyFragment, jsii.get(self, "policyFragment"))


class AccountPrincipal(
    ArnPrincipal,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.AccountPrincipal",
):
    '''Specify AWS account ID as the principal entity in a policy to delegate authority to the account.

    :exampleMetadata: infused

    Example::

        cluster = neptune.DatabaseCluster(self, "Cluster",
            vpc=vpc,
            instance_type=neptune.InstanceType.R5_LARGE,
            iam_authentication=True
        )
        role = iam.Role(self, "DBRole", assumed_by=iam.AccountPrincipal(self.account))
        # Use one of the following statements to grant the role the necessary permissions
        cluster.grant_connect(role) # Grant the role neptune-db:* access to the DB
        cluster.grant(role, "neptune-db:ReadDataViaQuery", "neptune-db:WriteDataViaQuery")
    '''

    def __init__(self, account_id: typing.Any) -> None:
        '''
        :param account_id: AWS account ID (i.e. '123456789012').
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39ac905e3b21cb76d85b13b658dee1bcf9822e6af870299fb037df092642ec81)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        jsii.create(self.__class__, self, [account_id])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''Returns a string representation of an object.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> typing.Any:
        '''AWS account ID (i.e. '123456789012').'''
        return typing.cast(typing.Any, jsii.get(self, "accountId"))

    @builtins.property
    @jsii.member(jsii_name="principalAccount")
    def principal_account(self) -> typing.Optional[builtins.str]:
        '''The AWS account ID of this principal.

        Can be undefined when the account is not known
        (for example, for service principals).
        Can be a Token - in that case,
        it's assumed to be AWS::AccountId.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "principalAccount"))


class AccountRootPrincipal(
    AccountPrincipal,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.AccountRootPrincipal",
):
    '''Use the AWS account into which a stack is deployed as the principal entity in a policy.

    :exampleMetadata: infused

    Example::

        bucket = s3.Bucket(self, "MyBucket")
        result = bucket.add_to_resource_policy(
            iam.PolicyStatement(
                actions=["s3:GetObject"],
                resources=[bucket.arn_for_objects("file.txt")],
                principals=[iam.AccountRootPrincipal()]
            ))
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''Returns a string representation of an object.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))


class AnyPrincipal(
    ArnPrincipal,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.AnyPrincipal",
):
    '''A principal representing all AWS identities in all accounts.

    Some services behave differently when you specify ``Principal: '*'``
    or ``Principal: { AWS: "*" }`` in their resource policy.

    ``AnyPrincipal`` renders to ``Principal: { AWS: "*" }``. This is correct
    most of the time, but in cases where you need the other principal,
    use ``StarPrincipal`` instead.

    :exampleMetadata: infused

    Example::

        topic = sns.Topic(self, "Topic")
        topic_policy = sns.TopicPolicy(self, "TopicPolicy",
            topics=[topic]
        )
        
        topic_policy.document.add_statements(iam.PolicyStatement(
            actions=["sns:Subscribe"],
            principals=[iam.AnyPrincipal()],
            resources=[topic.topic_arn]
        ))
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''Returns a string representation of an object.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))


@jsii.implements(IGroup)
class Group(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.Group",
):
    '''An IAM Group (collection of IAM users) lets you specify permissions for multiple users, which can make it easier to manage permissions for those users.

    :see: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html
    :exampleMetadata: infused

    Example::

        user = iam.User(self, "MyUser") # or User.fromUserName(this, 'User', 'johnsmith');
        group = iam.Group(self, "MyGroup") # or Group.fromGroupArn(this, 'Group', 'arn:aws:iam::account-id:group/group-name');
        
        user.add_to_group(group)
        # or
        group.add_user(user)
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        group_name: typing.Optional[builtins.str] = None,
        managed_policies: typing.Optional[typing.Sequence[IManagedPolicy]] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param group_name: A name for the IAM group. For valid values, see the GroupName parameter for the CreateGroup action in the IAM API Reference. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the group name. If you specify a name, you must specify the CAPABILITY_NAMED_IAM value to acknowledge your template's capabilities. For more information, see Acknowledging IAM Resources in AWS CloudFormation Templates. Default: Generated by CloudFormation (recommended)
        :param managed_policies: A list of managed policies associated with this role. You can add managed policies later using ``addManagedPolicy(ManagedPolicy.fromAwsManagedPolicyName(policyName))``. Default: - No managed policies.
        :param path: The path to the group. For more information about paths, see `IAM Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/index.html?Using_Identifiers.html>`_ in the IAM User Guide. Default: /
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b516a0686a548e570bd88d7c4c375e62f54baff3fc092d817ad9c2403b62715)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = GroupProps(
            group_name=group_name, managed_policies=managed_policies, path=path
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromGroupArn")
    @builtins.classmethod
    def from_group_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        group_arn: builtins.str,
    ) -> IGroup:
        '''Import an external group by ARN.

        If the imported Group ARN is a Token (such as a
        ``CfnParameter.valueAsString`` or a ``Fn.importValue()``) *and* the referenced
        group has a ``path`` (like ``arn:...:group/AdminGroup/NetworkAdmin``), the
        ``groupName`` property will not resolve to the correct value. Instead it
        will resolve to the first path component. We unfortunately cannot express
        the correct calculation of the full path name as a CloudFormation
        expression. In this scenario the Group ARN should be supplied without the
        ``path`` in order to resolve the correct group resource.

        :param scope: construct scope.
        :param id: construct id.
        :param group_arn: the ARN of the group to import (e.g. ``arn:aws:iam::account-id:group/group-name``).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16bb559f9cd4a61e31d9831c49f44aae4279f1bc47714c390ef63d433654c0dd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument group_arn", value=group_arn, expected_type=type_hints["group_arn"])
        return typing.cast(IGroup, jsii.sinvoke(cls, "fromGroupArn", [scope, id, group_arn]))

    @jsii.member(jsii_name="fromGroupName")
    @builtins.classmethod
    def from_group_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        group_name: builtins.str,
    ) -> IGroup:
        '''Import an existing group by given name (with path).

        This method has same caveats of ``fromGroupArn``

        :param scope: construct scope.
        :param id: construct id.
        :param group_name: the groupName (path included) of the existing group to import.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfa77f640d9bc653654c474376cfff254a2c4f7d0f6875a80eb44b243e1dc369)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument group_name", value=group_name, expected_type=type_hints["group_name"])
        return typing.cast(IGroup, jsii.sinvoke(cls, "fromGroupName", [scope, id, group_name]))

    @jsii.member(jsii_name="addManagedPolicy")
    def add_managed_policy(self, policy: IManagedPolicy) -> None:
        '''Attaches a managed policy to this group.

        See [IAM and AWS STS quotas, name requirements, and character limits]
        (https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html#reference_iam-quotas-entities)
        for quota of managed policies attached to an IAM group.

        :param policy: The managed policy to attach.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0073d4596a3cd9c2b07a428313a1c04604bd8df34c71816c90136ffa7c58ecb0)
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
        return typing.cast(None, jsii.invoke(self, "addManagedPolicy", [policy]))

    @jsii.member(jsii_name="addToPolicy")
    def add_to_policy(self, statement: PolicyStatement) -> builtins.bool:
        '''Add to the policy of this principal.

        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7efe2608ceefd191431a8adea13871fda6fe3193bf8171a4ead0318828be5264)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(builtins.bool, jsii.invoke(self, "addToPolicy", [statement]))

    @jsii.member(jsii_name="addToPrincipalPolicy")
    def add_to_principal_policy(
        self,
        statement: PolicyStatement,
    ) -> AddToPrincipalPolicyResult:
        '''Adds an IAM statement to the default policy.

        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f66e324527f4dca14250545b90ce229575ffc379f162d485eb2c630ba43e00b5)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(AddToPrincipalPolicyResult, jsii.invoke(self, "addToPrincipalPolicy", [statement]))

    @jsii.member(jsii_name="addUser")
    def add_user(self, user: IUser) -> None:
        '''Adds a user to this group.

        :param user: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d2ddce83ad48ecf3ade5fa694be3a205a6dce4cf4669aa568be1ffb0df38d34)
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
        return typing.cast(None, jsii.invoke(self, "addUser", [user]))

    @jsii.member(jsii_name="attachInlinePolicy")
    def attach_inline_policy(self, policy: Policy) -> None:
        '''Attaches a policy to this group.

        :param policy: The policy to attach.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8334d09c64ac01b56e25eccb0dd778a954e4f613c776ac3447cf3f1318a89d7)
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
        return typing.cast(None, jsii.invoke(self, "attachInlinePolicy", [policy]))

    @builtins.property
    @jsii.member(jsii_name="assumeRoleAction")
    def assume_role_action(self) -> builtins.str:
        '''When this Principal is used in an AssumeRole policy, the action to use.'''
        return typing.cast(builtins.str, jsii.get(self, "assumeRoleAction"))

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> IPrincipal:
        '''The principal to grant permissions to.'''
        return typing.cast(IPrincipal, jsii.get(self, "grantPrincipal"))

    @builtins.property
    @jsii.member(jsii_name="groupArn")
    def group_arn(self) -> builtins.str:
        '''Returns the IAM Group ARN.'''
        return typing.cast(builtins.str, jsii.get(self, "groupArn"))

    @builtins.property
    @jsii.member(jsii_name="groupName")
    def group_name(self) -> builtins.str:
        '''Returns the IAM Group Name.'''
        return typing.cast(builtins.str, jsii.get(self, "groupName"))

    @builtins.property
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> PrincipalPolicyFragment:
        '''Return the policy fragment that identifies this principal in a Policy.'''
        return typing.cast(PrincipalPolicyFragment, jsii.get(self, "policyFragment"))

    @builtins.property
    @jsii.member(jsii_name="principalAccount")
    def principal_account(self) -> typing.Optional[builtins.str]:
        '''The AWS account ID of this principal.

        Can be undefined when the account is not known
        (for example, for service principals).
        Can be a Token - in that case,
        it's assumed to be AWS::AccountId.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "principalAccount"))


class OpenIdConnectPrincipal(
    WebIdentityPrincipal,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.OpenIdConnectPrincipal",
):
    '''A principal that represents a federated identity provider as from a OpenID Connect provider.

    :exampleMetadata: infused

    Example::

        provider = iam.OpenIdConnectProvider(self, "MyProvider",
            url="https://openid/connect",
            client_ids=["myclient1", "myclient2"]
        )
        principal = iam.OpenIdConnectPrincipal(provider)
    '''

    def __init__(
        self,
        open_id_connect_provider: IOpenIdConnectProvider,
        conditions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param open_id_connect_provider: OpenID Connect provider.
        :param conditions: The conditions under which the policy is in effect. See `the IAM documentation <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html>`_.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11057e2b11d9138bde96aa84215de1b5dba16e8c36af672dbebea8a1c33f4310)
            check_type(argname="argument open_id_connect_provider", value=open_id_connect_provider, expected_type=type_hints["open_id_connect_provider"])
            check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
        jsii.create(self.__class__, self, [open_id_connect_provider, conditions])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''Returns a string representation of an object.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @builtins.property
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> PrincipalPolicyFragment:
        '''Return the policy fragment that identifies this principal in a Policy.'''
        return typing.cast(PrincipalPolicyFragment, jsii.get(self, "policyFragment"))


class SamlConsolePrincipal(
    SamlPrincipal,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iam.SamlConsolePrincipal",
):
    '''Principal entity that represents a SAML federated identity provider for programmatic and AWS Management Console access.

    :exampleMetadata: infused

    Example::

        provider = iam.SamlProvider(self, "Provider",
            metadata_document=iam.SamlMetadataDocument.from_file("/path/to/saml-metadata-document.xml")
        )
        iam.Role(self, "Role",
            assumed_by=iam.SamlConsolePrincipal(provider)
        )
    '''

    def __init__(
        self,
        saml_provider: ISamlProvider,
        conditions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param saml_provider: -
        :param conditions: The conditions under which the policy is in effect.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7271e79a3715a166397ac94ded3c4043db8b40c10213ffae6abbb3a17ce6768)
            check_type(argname="argument saml_provider", value=saml_provider, expected_type=type_hints["saml_provider"])
            check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
        jsii.create(self.__class__, self, [saml_provider, conditions])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''Returns a string representation of an object.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))


__all__ = [
    "AccessKey",
    "AccessKeyProps",
    "AccessKeyStatus",
    "AccountPrincipal",
    "AccountRootPrincipal",
    "AddToPrincipalPolicyResult",
    "AddToResourcePolicyResult",
    "AnyPrincipal",
    "ArnPrincipal",
    "CanonicalUserPrincipal",
    "CfnAccessKey",
    "CfnAccessKeyProps",
    "CfnGroup",
    "CfnGroupPolicy",
    "CfnGroupPolicyProps",
    "CfnGroupProps",
    "CfnInstanceProfile",
    "CfnInstanceProfileProps",
    "CfnManagedPolicy",
    "CfnManagedPolicyProps",
    "CfnOIDCProvider",
    "CfnOIDCProviderProps",
    "CfnPolicy",
    "CfnPolicyProps",
    "CfnRole",
    "CfnRolePolicy",
    "CfnRolePolicyProps",
    "CfnRoleProps",
    "CfnSAMLProvider",
    "CfnSAMLProviderProps",
    "CfnServerCertificate",
    "CfnServerCertificateProps",
    "CfnServiceLinkedRole",
    "CfnServiceLinkedRoleProps",
    "CfnUser",
    "CfnUserPolicy",
    "CfnUserPolicyProps",
    "CfnUserProps",
    "CfnUserToGroupAddition",
    "CfnUserToGroupAdditionProps",
    "CfnVirtualMFADevice",
    "CfnVirtualMFADeviceProps",
    "CommonGrantOptions",
    "ComparablePrincipal",
    "CompositeDependable",
    "CompositePrincipal",
    "CustomizeRolesOptions",
    "Effect",
    "FederatedPrincipal",
    "FromRoleArnOptions",
    "FromRoleNameOptions",
    "Grant",
    "GrantOnPrincipalAndResourceOptions",
    "GrantOnPrincipalOptions",
    "GrantWithResourceOptions",
    "Group",
    "GroupProps",
    "IAccessKey",
    "IAssumeRolePrincipal",
    "IComparablePrincipal",
    "IGrantable",
    "IGroup",
    "IIdentity",
    "IInstanceProfile",
    "IManagedPolicy",
    "IOpenIdConnectProvider",
    "IPolicy",
    "IPrincipal",
    "IResourceWithPolicy",
    "IRole",
    "ISamlProvider",
    "IUser",
    "InstanceProfile",
    "InstanceProfileAttributes",
    "InstanceProfileProps",
    "LazyRole",
    "LazyRoleProps",
    "ManagedPolicy",
    "ManagedPolicyProps",
    "OpenIdConnectPrincipal",
    "OpenIdConnectProvider",
    "OpenIdConnectProviderProps",
    "OrganizationPrincipal",
    "PermissionsBoundary",
    "Policy",
    "PolicyDocument",
    "PolicyDocumentProps",
    "PolicyProps",
    "PolicyStatement",
    "PolicyStatementProps",
    "PrincipalBase",
    "PrincipalPolicyFragment",
    "PrincipalWithConditions",
    "Role",
    "RoleProps",
    "SamlConsolePrincipal",
    "SamlMetadataDocument",
    "SamlPrincipal",
    "SamlProvider",
    "SamlProviderProps",
    "ServicePrincipal",
    "ServicePrincipalOpts",
    "SessionTagsPrincipal",
    "StarPrincipal",
    "UnknownPrincipal",
    "UnknownPrincipalProps",
    "User",
    "UserAttributes",
    "UserProps",
    "WebIdentityPrincipal",
    "WithoutPolicyUpdatesOptions",
]

publication.publish()

def _typecheckingstub__f7aec9396799d928b7043c068a165e3ad161cc590afe8defeb0ce4ae06ecd9ae(
    *,
    user: IUser,
    serial: typing.Optional[jsii.Number] = None,
    status: typing.Optional[AccessKeyStatus] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c4bef18bd7824d787c934ed761d1626296453e8109e28b61a0c4634f48435dd(
    *,
    statement_added: builtins.bool,
    policy_dependable: typing.Optional[_constructs_77d1e7e8.IDependable] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__828f1cacd29f05b4eed40f202f7b5da1fdf626701e78525463598fc447b5869a(
    *,
    statement_added: builtins.bool,
    policy_dependable: typing.Optional[_constructs_77d1e7e8.IDependable] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d6875d360f4b68d81822160010f3dcab4fad75219310207a67ebdbd76b5d610(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    user_name: builtins.str,
    serial: typing.Optional[jsii.Number] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__253c114f9b2f2b6b08dd9a5564956df556fd7f0ff623cf82d94801cb17f499b2(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab5857eebc55e10a0edcb4b0c6f013af1342700cb0a55e89483e6f8b6d574741(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3405535e039979434b63eda6cd780e7a68f3036e83c19773aa4cce38e62cfcc0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de65be3bea4fb6cb4947339490001a6cb74c0e6991d864cd5de95395f19d977b(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c8207c22274bc6fabc3862c3b573f9d71344e354dbd17a00318aa43fa18cb7d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8155aca561d14186aae77c5658124546588f321eecca8d6e53a5467862dbddc5(
    *,
    user_name: builtins.str,
    serial: typing.Optional[jsii.Number] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20b2c419e0a9df4f72befe689959dc5d68aff361365a09c398c4a5645df50b18(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    group_name: typing.Optional[builtins.str] = None,
    managed_policy_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    path: typing.Optional[builtins.str] = None,
    policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGroup.PolicyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cd8f3cc95c07c18415e709564850ea545ed675e3f0b6e3505e763a15b48e963(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89278b67425b9a0f94f61235c7282945d071b501bc7b15f85a485662ff826258(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01be7e8dfd9fda0df1899d3026531e8a38a22b7e1f2d6027c883cf4d505c3d51(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a267baaf187cde3f3930ebef9cdd1a754591f3f54b47d9729cc1d9bb3a93458(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b014a61027fdb2afb518b56e4a64ca65934df00a511ae153c21193094d07e4ca(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a23f252d3f662bbd9b85e3ee272df167b08d0ce70d4a20ac116d5b1cb15a44e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGroup.PolicyProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5381732fad8dcd5499b3b303273fdd9097ec896987b47080216d0c734f18d9a8(
    *,
    policy_document: typing.Any,
    policy_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f890caaa5f6b29722a17bf5c714640d202cb740a7f07aec5a5ced9b53eed348(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    group_name: builtins.str,
    policy_name: builtins.str,
    policy_document: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79a0026280df7e0717ed9e16473b60d33a900f8870446901848eb1af15bc48c1(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef5341af0b1e6f12f150e9d4694149341aec7aa000971cb5f25b0b9672a631cd(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__789fa1310fa5f0c8a58c7721ec65bb7fb38294aa983f688e92a477a4ecf7a44c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98fde951f7da16e6788d849111dc918395ada4b5134156e2bc4d29caf92e119f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__252a63b1958f4306e76e5da346149aa1087fd66fc85306f6c6c58ab5571644a4(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa640a2b964f19199ce54686b7fd65c710619c4f560d010f4b3ceaac824c022b(
    *,
    group_name: builtins.str,
    policy_name: builtins.str,
    policy_document: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83c00814903fe43cbe21eca7faddcd90dcea9ec971aac6d8d2daf6b50f845df0(
    *,
    group_name: typing.Optional[builtins.str] = None,
    managed_policy_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    path: typing.Optional[builtins.str] = None,
    policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGroup.PolicyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31ec5f0ea7f9ac49e8ad53cc5faa514c2ff04ae0962ad9e9fb0274b3c7f7b0b4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    roles: typing.Sequence[builtins.str],
    instance_profile_name: typing.Optional[builtins.str] = None,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__014a9e16c0ce84f545ddc2fd74080cc35e47d194639e0b8133383c054c81a206(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ea1d50531a33bafd660573c8a2e3a8e5e0215acf7462185f0959ea67f61bee5(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__785f95fb95c2bbe41d514dea64d18cfcbfa66bffbfa2d083ae501bdd37a0fe4f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94d5332482fea97767ec730f2c1930a5e4ec68efce72124dd1cfd7a7c5f40bba(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbfe487716a390ca26e092b03b19bce39babeaa672e667fad6be4aed43f11cf4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13af24b231dab76416337b37eed1fc0eb441fa93214942c4f328be745d78987f(
    *,
    roles: typing.Sequence[builtins.str],
    instance_profile_name: typing.Optional[builtins.str] = None,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a8c17449d46e088e632540cdf9eb1a587f03d90f16e24cec8b7c30c9962df64(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    policy_document: typing.Any,
    description: typing.Optional[builtins.str] = None,
    groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    managed_policy_name: typing.Optional[builtins.str] = None,
    path: typing.Optional[builtins.str] = None,
    roles: typing.Optional[typing.Sequence[builtins.str]] = None,
    users: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a722cb81ff9cd42fafa9ac5e408b6c1bfdb242f04cc4ae98a8ea3a1b79fdbfd2(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49691612ad6d051c64843fc36b88e2a32e132ab38af6120ecf52699776f24808(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57f5af0ac55173154c340115659691a27fc295c9250c8d5ca198109f64466ee8(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cc04fd5744afbd3cf5d35eec5e89c42dc47f150557ef85988e2e74ea873c422(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc185a3adf8688a003c343f2c7f2d2213871db292b02bf41ab584d89834d560d(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad4dd76c35346216139c78ee6af3ca0521328f8eeab6374f6ea5d0c3af2b9886(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55edad48d274800976c6721903c6c5c63dd8559011473654245716943a0e2895(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1de9b6a5aa5082e09fb07840ea3cdfca3eb8553aa46fd492dbb181b5362f13b9(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ad59cd00d0e0ac909d310dbcbbd6e052d1f131f984c456d7dec6c6d0f890843(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7363835eb798096a2561a7a8a91d2914cb5cb1e71dbda6de66efc5952296bc7f(
    *,
    policy_document: typing.Any,
    description: typing.Optional[builtins.str] = None,
    groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    managed_policy_name: typing.Optional[builtins.str] = None,
    path: typing.Optional[builtins.str] = None,
    roles: typing.Optional[typing.Sequence[builtins.str]] = None,
    users: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cc57bdb168ce990f6466a329942805a3eead54a8207df63d06106140ceabaf1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    thumbprint_list: typing.Sequence[builtins.str],
    client_id_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e414fee3e3f5f30b79be56e642403e70f811157ff8d43b791b5526b812061d8(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dae706f759e2af37c98017ae788d704bf61cf6db2c64c99cf832bc287eb6389(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa3ed6dd0ef0854d834aaa2a169f05db6443763c0d3f9c4bd58c44fcdac5c427(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65ff0b468eb305f1d15390d9c9c9f031b03af51fdd4c6edcd5f1c7b3fabe5e02(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4db8fa394e822c865ec6e624ef31a1dd1aaba19da7971d0044ad1d1d5a060d70(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__047a9e084da3802dd407fe84ef685690e55704bff14429720999a139e667481e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7712735ff8576b291ddb9c7e92ce8078bf6f1d87729109296c1be6414cb3532d(
    *,
    thumbprint_list: typing.Sequence[builtins.str],
    client_id_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb67178fe7e1b31e1be07438cbe12957995260af0ad90c58a3ab490fe6dfe65e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    policy_document: typing.Any,
    policy_name: builtins.str,
    groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    roles: typing.Optional[typing.Sequence[builtins.str]] = None,
    users: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b0b1b065d832052b886db644c3488c7bc10240091ef05927590351b7bc53eb1(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85f1de37bbcdfc836c215c1a1844169c37747c39945f4381b39bfd452963ff73(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06044458de4bf8f3f6bd0026d2e0c44680c55d70af59396fc7616d84dab9d26d(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecc19153b06dcc252bfb1ae6146652d56fcd1825369497489a00194a960696d5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cb77529b0bb4edf27e46d46d8fcaedafea19611a49ee1c83bfdd3a98234745e(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87a89a5b9d5419ceb30e8217d4489eae0857ac493147f2a7af32a527ec688a14(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c25ce8e0b5d932098589ac1c033a96eed27019fa02e7aea82f7eaacbdd509100(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__368d6e95de387252f469d8428e0a4cbe73ffdab170f90c7194b6f3e54f8b875c(
    *,
    policy_document: typing.Any,
    policy_name: builtins.str,
    groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    roles: typing.Optional[typing.Sequence[builtins.str]] = None,
    users: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b418623e6c6b819228e2a7c5d9c5341241e5b0e738f77eeabd6cacec7c6fab32(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    assume_role_policy_document: typing.Any,
    description: typing.Optional[builtins.str] = None,
    managed_policy_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    max_session_duration: typing.Optional[jsii.Number] = None,
    path: typing.Optional[builtins.str] = None,
    permissions_boundary: typing.Optional[builtins.str] = None,
    policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRole.PolicyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    role_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ab1ed2eb652f78c921a94468eea54161c2d72210612c21a2d7221190717d546(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c17ebfb69a2f5ed9dd9290d6026b842dd5e032f3f0f7aa29ccc996da3be8aa3(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f64edf2fd513d8eaa71e570374ea6368333dca94e9bcd75c06e0cd57bf703237(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c2a9dbc73d67aad806d2048aa4381abc22ed38266fbe7ad4d0f9363cfdac4a7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84c396c36f658a4080b46dfbbcb0f9163ca138b4afaf4da438a00378beffede7(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6431acc0b99ad558bc7b549bbfe3e581f937dce92da78253920c201c8cc22e0a(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d420d46f77d7cfcfcd09009a0f2eadf9ebada83d085948137f30c8ee4abdd4b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6141e4bbefd436f5eddad46690a81845abcebab51fabb169abf1431f02795db1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de13ceb9aac4a8cea0907c7e4ba81eeca369f4f35bfc0f1d48beddf9ab76811f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnRole.PolicyProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__435e72316ea55d9adabad0902ac623255b110529fcd748e3ac74055cff795bef(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c0657eba6af54757d6f74532e2ed61efbdc50fb773a54687878cfd7c7f8dda5(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e339dba71f34d8ac881f4a2583a5b3e824a8bb93f479517aebabc1977c8c2ba1(
    *,
    policy_document: typing.Any,
    policy_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1532590762c98b830f41db58b5d7333f7f995a90f128be89292c180ecefabf3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    policy_name: builtins.str,
    role_name: builtins.str,
    policy_document: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f878b18113dc1f16c459595683f03c065b56afd62d2918c65c6cde7539984412(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0db54a249a715ade4f26735343ca5a55eb1952e807ce57e2d7ec4b843c350641(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7042bd66e9ba283ac19987752cc24a822d1f227ca8217dbbae1ca253f583b373(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c89cdd638f3704d6ca88c2e6c9c5c301322b1ed12de337f2ec3c4bfdee661f0f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2153da01bebec26c385aa83a08c1b544e6c1e15dfda33c546698c885cbf1e9b9(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0668a03621626b1e6c6578349ef013dbc6d934f3d76b7973db1350fe9541efc(
    *,
    policy_name: builtins.str,
    role_name: builtins.str,
    policy_document: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5103775c44bc4d8c2381a2d9cd5bbb47d14617e4000af5af24e41da605c8820f(
    *,
    assume_role_policy_document: typing.Any,
    description: typing.Optional[builtins.str] = None,
    managed_policy_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    max_session_duration: typing.Optional[jsii.Number] = None,
    path: typing.Optional[builtins.str] = None,
    permissions_boundary: typing.Optional[builtins.str] = None,
    policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRole.PolicyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    role_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f64934981377388842130b01da042285d0dfa38ef82a7537c7ff86f5d1f3f009(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    saml_metadata_document: builtins.str,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__125ecb4c71203c76b16de524888c31f4d67c2ec1eb117d698f7d362c7d8fe450(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa493901e136133decf51345379fd4b5dd35432e35f354e5dd453eb7daa8245b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c9b70ef0e0ed94f53ecf2221518796deaf4c5a9353a14b0183e26bbe0e0d57c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf699aa7d755e072f3b60499335fb6469de4ed3bdb0605652b9c3269877e220a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b139c04642da2a9b428a58eb37077beb7f9b79971517b5fd95e8c7dbfa322e67(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__753bbb479e0c0a542a8456d357a3312bedbcc25e8753ca69dabd0ebf09aa6de7(
    *,
    saml_metadata_document: builtins.str,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6cf37b70ff9a27f22bc984fc19e96b2e42e00f83cc2e2efd66e3b46e76e4b5b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    certificate_body: typing.Optional[builtins.str] = None,
    certificate_chain: typing.Optional[builtins.str] = None,
    path: typing.Optional[builtins.str] = None,
    private_key: typing.Optional[builtins.str] = None,
    server_certificate_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__366b62f33040d7a5e531fab130ce2a8bbbba719ed080e892236f3127f59f0273(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a54a0dba3e2e40002701a3afd9e2e4bf8ce9a72d2137a4aaa4aa728c81f007a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87c7211629136fb42c02f367b9448da78ab4e5abfd4d9e04ab0caad5325bb2b2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4ff303b49caa7890566d08d6a2a60ec1a95e65e81edd71a7aa6f85f708e4fdd(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77ad8bd4800869c88771ef98910278fbbe26e1520e96f812fdbc0837580817e8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4203fd09b7317247f69586ca724e62c2ea809be65e02471885451dfe4324b20(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54cd160d96a28915ae295954600508a01387f155ef6c01892d38e609428f5648(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__579aa0e0cc52787dc34d6f715f95942533f29fc470256c2e7e0cd454c26ae2f4(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c0fa14d93aea4f905649a3dfa7bcd3ea31e86d8c6ac197efe6a3040eb6155f7(
    *,
    certificate_body: typing.Optional[builtins.str] = None,
    certificate_chain: typing.Optional[builtins.str] = None,
    path: typing.Optional[builtins.str] = None,
    private_key: typing.Optional[builtins.str] = None,
    server_certificate_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d428bb539fd6df78e6e28b0695f366af555fe1f958879857ee30c8067e2af789(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    aws_service_name: typing.Optional[builtins.str] = None,
    custom_suffix: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cc7c392a2b0731277a0218b6b90c103a720e9d973fe65098c66c9cbdbc1777d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f0f81638df3b5467a6f2750e681e60bb99239f2a978002ef69aae000229a742(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__894356a5067d4595c32429fb905a7c37dbca2ce428fa3c0743817d563a07b673(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73b7c9779d86988f0dcb8c2282ce3fb8bd23b1db482b7081dbf555457bc45bdc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__796fb2b9a69a72a7ee224d68a6ba88159e7107645a0f704a025f9b8bf7b3d6ce(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dafce478a4346996727c8ffa75ed8a924def97e273b5d6cc9f321b9c8eea85d7(
    *,
    aws_service_name: typing.Optional[builtins.str] = None,
    custom_suffix: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b453e8e55124e84a27aa60acd149280051b756df30318da37839b1e4ca523687(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    login_profile: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnUser.LoginProfileProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    managed_policy_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    path: typing.Optional[builtins.str] = None,
    permissions_boundary: typing.Optional[builtins.str] = None,
    policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnUser.PolicyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    user_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c540efa10e05810a6302626e0a6f54b2963bab597096fea4ee0e6023d72f25a8(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0ee3dc7778b587a3d4c4511b986f6fc1c9c865253acfb48b0df1fe42cd5f082(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a030f35db68335b8a550d10c248a4f289bc47052d3d3d7ad1feb6d43257f1398(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9ec71116c53dba6fcd83f943f62c54cf4a1829d2c1fbfb773b475eb2e580e43(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnUser.LoginProfileProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d9bc7aa1272c0c2d7eca931089eb5238a71667de1dd61a5e39d1bb0d80b06ac(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b45a0c327fbd95f77396687ff75f3c61c77223d854a371180accaa05cec25e6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__766b6286be304f39fa6308bbe3eb6a8a552712c6becdc31706c5312027885dc7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25df8a318c9f526fd31465b78f732e159102acc489b971d41ccdbe1b91ff426e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnUser.PolicyProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68bb5e640fe8f1d3df25a029bc80e69cb1904a783dae4c75d6eb193e37389a44(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__673a92f6f8c13a39a21d59717aefb8413279cd51db902ce34f4e3611efe7c1f3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b9798165bbdd5df9e80975dc2c6efce6bd25d4f2cb0e4afb86f5dd32cb51e5a(
    *,
    password: builtins.str,
    password_reset_required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e10d289e0033a52d00a2a3cfb4f5dd68a85b62b072e59b08358dbe810503669c(
    *,
    policy_document: typing.Any,
    policy_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b09938208fba24d256ecd68450b14a065d6488754943e666f9c0528cd0571773(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    policy_name: builtins.str,
    user_name: builtins.str,
    policy_document: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cde7256763c767d2775e466edc810c10426403d26df61b45c5e90e87328e04f1(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ce5c91a6c338867856c8d0c8e4fb1baca52b1340f6738e4b2d9310ae995e3d0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1863a06ff9856e56ddfef1835185f36375de9aab427703c632667bf53aed26d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c87f136af227b9d80b9c996ebad3cd0115cf869a0b881cdc44f69822e5d676a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__868920d1b0a57c789262fb64d7c1ce084d6f3da90f834b2da8cc620e6553bad8(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe6f239efe54addc57c69dc765719968f9ffeb9e19e348f502085249d1739fd5(
    *,
    policy_name: builtins.str,
    user_name: builtins.str,
    policy_document: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b4312dc8ff103705c67491ae6f470e2644acffd396e5635261bf47e9a8a945f(
    *,
    groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    login_profile: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnUser.LoginProfileProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    managed_policy_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    path: typing.Optional[builtins.str] = None,
    permissions_boundary: typing.Optional[builtins.str] = None,
    policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnUser.PolicyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    user_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cff069f9e69e3551ebb007914281abb14f05e8d822825ab91577ecf95414ffb(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    group_name: builtins.str,
    users: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__839f86071dc7f367d40ea9ba8b644702b8c3f40d83e2a8d6821a097013d1a603(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34d58a01767f256628192ca708cd20a48bd1b0ad6795595846565c2c84e235e8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80988c0737b217a15fbc51dd191617d213752314ac76d041cba72fa2fbca3c04(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9633608428e6d8df416ba93dfbf3f5248605fc8d2d8dc1be95067a291eb4223e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be028fcc46f0c07bb061d985679cb1824767d764103c011f6956ac7bb2f20043(
    *,
    group_name: builtins.str,
    users: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e13769e4d8767c55f844c7fd4df38f85edde39c6b8cf55033fe2d0cc49399a99(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    users: typing.Sequence[builtins.str],
    path: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    virtual_mfa_device_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50929ddeddd60b35f52c962b9e82522e8bb65a7b719ace39001073ce2996743c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95acd7cc3c337be75e6e1344aafe2900ca56480c92605d270e827237b04933d9(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62933eb2630cbda8cd521b55437211294e28433e9f2916bffa9f4987d4a9aa8c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ed4aacd2a4d70c96cd36de260e15008f2e50d943134027a7f4ea4a75e1d03c8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cf1f893827aab77cb8d7fec4a522878bd879b2f8a49198a93c51cf414124229(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5456135f25b9d08fb97dae8235054f6111c0d6ff6cb6ca028c6c552d38b10cd(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5ed743528ff356ce758fcb44914dce08240fea9458cd411d40223e93fcbbd55(
    *,
    users: typing.Sequence[builtins.str],
    path: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    virtual_mfa_device_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53036310adac5dd1bbf375726f6d4951d790e671d970614b44aa288195097a24(
    *,
    actions: typing.Sequence[builtins.str],
    grantee: IGrantable,
    resource_arns: typing.Sequence[builtins.str],
    conditions: typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e05d9e2d20ba422910a4ba52987ae06003b821061dcd5fb66ea08234a5add520(
    x: IPrincipal,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed18f5361eb860ae94547e85443180c995c1de1d28ef2ccda9f79c39983c1afb(
    x: IPrincipal,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11451a597e4f52017e14ede781ef9eadbc8d06d5380bf40a47e9667cf431ab84(
    *dependables: _constructs_77d1e7e8.IDependable,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1882c00172b4072d4822b976aed7e86da105b2fb611d32539f72c644071f16d4(
    *,
    prevent_synthesis: typing.Optional[builtins.bool] = None,
    use_precreated_roles: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f2caa0021d06fd2643ae1baf77362146ac3d8099ebadae2a932738c2a2a8792(
    *,
    add_grants_to_resources: typing.Optional[builtins.bool] = None,
    default_policy_name: typing.Optional[builtins.str] = None,
    mutable: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8d60e61efe2fd0be1638c155ae6ceb97e4047a546e091855a6300b0267cc06a(
    *,
    add_grants_to_resources: typing.Optional[builtins.bool] = None,
    default_policy_name: typing.Optional[builtins.str] = None,
    mutable: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ae645e99a39c5eb8dbdb0a66396e18ca51afd239a00e07d929768a9a716ccce(
    grantee: IGrantable,
    _intent: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6318dcb5bbc942b36daa3ec8cb25267c59a79903d43165acc5d48f60d4ef308(
    *constructs: _constructs_77d1e7e8.IConstruct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18a4ff4a989416437955a50d12b650943c445c1bd75cbc2f47d19390462e1842(
    rhs: Grant,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a60e5877e638d22c44d2e72be768df7f85caf47bec9ab2e6b2adcce826a6aae0(
    *,
    actions: typing.Sequence[builtins.str],
    grantee: IGrantable,
    resource_arns: typing.Sequence[builtins.str],
    conditions: typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]] = None,
    resource: IResourceWithPolicy,
    resource_policy_principal: typing.Optional[IPrincipal] = None,
    resource_self_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e1d68e4e0e483e95fcca600944e0e8047f1278ed2d44d2d239ae6584b491dcc(
    *,
    actions: typing.Sequence[builtins.str],
    grantee: IGrantable,
    resource_arns: typing.Sequence[builtins.str],
    conditions: typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]] = None,
    scope: typing.Optional[_constructs_77d1e7e8.IConstruct] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d76f68f1d67dcad526c87768d88423a4092a0ef3127be7cb53462044851e0ea2(
    *,
    actions: typing.Sequence[builtins.str],
    grantee: IGrantable,
    resource_arns: typing.Sequence[builtins.str],
    conditions: typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]] = None,
    resource: IResourceWithPolicy,
    resource_self_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7889ad6c97f3c96c3ead5d27bd1231fba11aadae1700a9dcd088123609e9b9a5(
    *,
    group_name: typing.Optional[builtins.str] = None,
    managed_policies: typing.Optional[typing.Sequence[IManagedPolicy]] = None,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c10aadcc3756f5f6d5486d7ecd5cabd7845be5964af1722a9d4962d586babd4(
    statement: PolicyStatement,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc0b619bfbc345bc9140fcc58d59f27472a211b09306f5c2e6b0147efcef6b18(
    statement: PolicyStatement,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47902e96d39fe1f772c15032b60b34efd5f4ebb64e4f7d08d924c04ab8393203(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instance_profile_name: typing.Optional[builtins.str] = None,
    path: typing.Optional[builtins.str] = None,
    role: typing.Optional[IRole] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c5f92c9eb36073e3604dae6b3449d6b3ce102597766d24026143d8edc87c0a1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    instance_profile_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4829ea04dde958ee082c71fd13dbdde279a49cce33d5b0cd09b7c5dc1a90e0a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instance_profile_arn: builtins.str,
    role: typing.Optional[IRole] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7870e30876638f54c4d41cd7645fabe3356a94b6ede305036ccf59d622f572e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    instance_profile_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb6dd6d0c3541471c82745ecbcf8e73c173fa6246fd7249b3a9e71e7c5b84388(
    *,
    instance_profile_arn: builtins.str,
    role: typing.Optional[IRole] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac5e12eff086b0ebec934d941ac660747a3807a1f2e371ed4b509707ab23e345(
    *,
    instance_profile_name: typing.Optional[builtins.str] = None,
    path: typing.Optional[builtins.str] = None,
    role: typing.Optional[IRole] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cd427eaa6d6959043bb705f947d652220f35431c484ef548899b9f81e573c2d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    description: typing.Optional[builtins.str] = None,
    document: typing.Optional[PolicyDocument] = None,
    groups: typing.Optional[typing.Sequence[IGroup]] = None,
    managed_policy_name: typing.Optional[builtins.str] = None,
    path: typing.Optional[builtins.str] = None,
    roles: typing.Optional[typing.Sequence[IRole]] = None,
    statements: typing.Optional[typing.Sequence[PolicyStatement]] = None,
    users: typing.Optional[typing.Sequence[IUser]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04dc3b9def232bf73e8992c95959e8ca96d18af4cafb5db34a590a221cb825ca(
    managed_policy_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b433b3584cc62234ee457168b3f3d2db5b0b227fe9dc2240edd9ce3eecb779a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    managed_policy_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__324e775a0f29673011a6cd38f79e52c1bb0c3c5c895f02fcfd38496e4fe98322(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    managed_policy_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc09c2f794b8d270cf58515acd36f16f22c50e8e485667751a6b6bf5441cdcef(
    *statement: PolicyStatement,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53947185e012309c9619b70da30bfebeef3a52fedd6d8eca19e9a8e96853c82e(
    group: IGroup,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3b5752936a78a06ee1095be0dc5362932d7db4aa0245a456f4cfea45bef91c9(
    role: IRole,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3b5f4b1c957b78ec0d5ae0e80dc7f2471a55d293c6a67e32ef5a2046d89543d(
    user: IUser,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ac402af2b963b15f12c561030bd732418fdef258857572111b9a81189e27e35(
    *,
    description: typing.Optional[builtins.str] = None,
    document: typing.Optional[PolicyDocument] = None,
    groups: typing.Optional[typing.Sequence[IGroup]] = None,
    managed_policy_name: typing.Optional[builtins.str] = None,
    path: typing.Optional[builtins.str] = None,
    roles: typing.Optional[typing.Sequence[IRole]] = None,
    statements: typing.Optional[typing.Sequence[PolicyStatement]] = None,
    users: typing.Optional[typing.Sequence[IUser]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__270fe9db45fea69c973ea36d667d5236d0463996999ebebabf67dbaafe739d10(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    url: builtins.str,
    client_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    thumbprints: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b937a1209414da4def854fd0c371550ec506b47f8d3f8c931bee67604e5589a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    open_id_connect_provider_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c07fc1633df440495e4513aa2acd1999d7e26f667e4c9d387ecfed34ba60aa34(
    *,
    url: builtins.str,
    client_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    thumbprints: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c60cfb31fa5f1464742fd5bd4c6874bbac2f64c851f5a2c9446ae181b34b208(
    scope: _constructs_77d1e7e8.IConstruct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d84d00226fae280f509c83e8e2fe992e095759345570998cb685b91b3428566(
    boundary_policy: IManagedPolicy,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf4aaba2f6acb5486adaf871c56e1317b1a2931936b56a78bf4633c14caba596(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    document: typing.Optional[PolicyDocument] = None,
    force: typing.Optional[builtins.bool] = None,
    groups: typing.Optional[typing.Sequence[IGroup]] = None,
    policy_name: typing.Optional[builtins.str] = None,
    roles: typing.Optional[typing.Sequence[IRole]] = None,
    statements: typing.Optional[typing.Sequence[PolicyStatement]] = None,
    users: typing.Optional[typing.Sequence[IUser]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11207539a0ef88ae02fb600ab0862501107d998ae3be0f5a08a9fc0466cc0948(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    policy_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__510252a6b115bef4c94f6ab3c402eb29a1b2012a86045ddad51b4825713e0799(
    *statement: PolicyStatement,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d09ae4b9f8a7c9ca0442c9a4b6f69bce78f42c194de9b535704dc9718516fea(
    group: IGroup,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__010ce98a5e97a30c0c893a505506c652f5ecdb76ee983e02c498a174717f3e82(
    role: IRole,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87f9ba31abd317367c4b853073e8d4e30843f460c3420b69165c6082b01547ae(
    user: IUser,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__570b193deac1ab27a70fd71df51891425bc3ec3540e0a5cf7f8f9e585b276f20(
    obj: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54360ff9757f011bcac10fedb199770d4d17ebf0453c3d234c0d5dc45d33e1c1(
    *statement: PolicyStatement,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2bffb5bcc0e0574448352039a95ee7ed66fbd29faff9f34b1c5e482d329f7e3(
    context: _IResolveContext_b2df1921,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__148d80305c19bb7e6f27161227f29ccdccd87c5529111c191eee0c97d735d661(
    *,
    assign_sids: typing.Optional[builtins.bool] = None,
    minimize: typing.Optional[builtins.bool] = None,
    statements: typing.Optional[typing.Sequence[PolicyStatement]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a119470d7c78e863a14a450dfe2d14dd9454487e93601f2675b2fafe09790c2(
    *,
    document: typing.Optional[PolicyDocument] = None,
    force: typing.Optional[builtins.bool] = None,
    groups: typing.Optional[typing.Sequence[IGroup]] = None,
    policy_name: typing.Optional[builtins.str] = None,
    roles: typing.Optional[typing.Sequence[IRole]] = None,
    statements: typing.Optional[typing.Sequence[PolicyStatement]] = None,
    users: typing.Optional[typing.Sequence[IUser]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3310dd221a31143a87ae81db4017dcad81b1a99d3d920f2184101ed8e7186455(
    obj: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__709bd112516bbfd3a8db442420a90bf80eae4cfd2a7d514a5612c6b3a447720c(
    account_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7570c3287006f9128c65d62789b1ef89599fe16f2b3a738f83cb5fa00aac1beb(
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__753e936d4d13cab9c5aa2f61d42cab848105cd421cf5e5027b920d5ad7ca0fdf(
    arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e93c2a641b144f46ca61b524c40ddbae1d4b77b9640fa4996e816f445d8f6edd(
    account_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__344be87a6a10a3974e50790a68d361cd386fe620caf5baa8dae7ef6f97881c28(
    canonical_user_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db59aa35431ad83b8fa7e1c45f11c92108f81ccef5b7baab7a37414280719862(
    key: builtins.str,
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f76cf4da6bbc6e1cb542b1c4034ab81599d83ce4800b0a288a241ba0d4ac6ee(
    conditions: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ee9dcc2ed7fe994d44a076dc07c103db4407fcda32a738035feb148a22879ba(
    federated: typing.Any,
    conditions: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b6b4424bff8556b7a98dfced6db44392158d11177b9f964fe1cb0cfb4532f85(
    *not_actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3b9cc21ab5c593c77deae20933faab5861db2f155f8bf91ced6fe1a382e51ba(
    *not_principals: IPrincipal,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b596ffa85ab5014633dac1d25489acd42c736f41cdba62b050ca048610a83ed2(
    *arns: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1783e9c91d9c307df264cec637ef147b4aa30b973ac302ab19a9f486211719bf(
    *principals: IPrincipal,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__feb2cb778edcb3c0b9cafd7458f0c6d0481e45f9d827da0b859be3f4f30d6393(
    *arns: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd372f80873e5e30ce5cf291cd80c7ce500c12643cde076cf4ddfbc1c05faea5(
    service: builtins.str,
    *,
    conditions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b4744c164be6f567bdcb8f9b4c6dd9ee9ed642a926a6200c6fcb6735c3499e4(
    account_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e49097a84ad9a7af8121131935195997223c04f9d2b394c9d8f88a9f6446dc9b(
    arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0938212412c89f00c92be30674976489815687ff4590eef7d1e3a8d2b3605ff1(
    value: Effect,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ad1bd9e071f1c20bcba127bf551d42076cff1e619eeeecfffabbcefe7b69818(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1307ab5f5dd84b7184f36603f7af026efb2798812c35c96dbe60552fff14c3b(
    *,
    actions: typing.Optional[typing.Sequence[builtins.str]] = None,
    conditions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    effect: typing.Optional[Effect] = None,
    not_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
    not_principals: typing.Optional[typing.Sequence[IPrincipal]] = None,
    not_resources: typing.Optional[typing.Sequence[builtins.str]] = None,
    principals: typing.Optional[typing.Sequence[IPrincipal]] = None,
    resources: typing.Optional[typing.Sequence[builtins.str]] = None,
    sid: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__278426b331a0d887bf9449f77f6f9c562033abef58a3d7279c5604a1e1c928ea(
    principal_json: typing.Mapping[builtins.str, typing.Sequence[builtins.str]],
    conditions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c9223cb9fa6dff45ee4fd7013629ab18542c2499a83f542c5405968fad2287c(
    *,
    assumed_by: IPrincipal,
    description: typing.Optional[builtins.str] = None,
    external_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    inline_policies: typing.Optional[typing.Mapping[builtins.str, PolicyDocument]] = None,
    managed_policies: typing.Optional[typing.Sequence[IManagedPolicy]] = None,
    max_session_duration: typing.Optional[_Duration_4839e8c3] = None,
    path: typing.Optional[builtins.str] = None,
    permissions_boundary: typing.Optional[IManagedPolicy] = None,
    role_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91316381005170938f0843dfc46ecd2dcd5bff5e8a02bd3f549257a6766268ec(
    path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__539954bae3260c99c71a9ce3ae7c5beabd619c72716348d783fb02a4392e8980(
    xml: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75c8a0ae91cf9a623b67a15b867de0473fa7870f3d3806ea585381a9a32222a2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    metadata_document: SamlMetadataDocument,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b78da91cf00435dc5bff92bbb2857fe752f6a28b7483a3790b9a5fc1a88be6ab(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    saml_provider_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f0838242f105f982b040b1e4abc268b7e6230b1f40a59916bdce34e26df4782(
    *,
    metadata_document: SamlMetadataDocument,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1a7b908a503ee76c237762d915d7a503778df01faaca4c8b3e6de46c413efea(
    *,
    conditions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0427f0b3c82f050501fde1f37f0708213ce2880cf76710cab2373a0fce6fbf0a(
    statement: PolicyStatement,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2eafec25f04d3417a92e78ef10e9bfbbdf9bad8c39e6cf6cafe9a65939952296(
    statement: PolicyStatement,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5de6fb03be5f0e87676deff413c87e5098f429f34e2caed17f1337c435ed431(
    *,
    resource: _constructs_77d1e7e8.IConstruct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5246085f2e2073ef1bcc0015f7ac242968b5a4a77257c315904c1bf3c1dabd4a(
    *,
    user_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b49c33f300471f45a248f56a068fb48f78451f10631fedcb3e5890d72ce3fe05(
    *,
    groups: typing.Optional[typing.Sequence[IGroup]] = None,
    managed_policies: typing.Optional[typing.Sequence[IManagedPolicy]] = None,
    password: typing.Optional[_SecretValue_3dd0ddae] = None,
    password_reset_required: typing.Optional[builtins.bool] = None,
    path: typing.Optional[builtins.str] = None,
    permissions_boundary: typing.Optional[IManagedPolicy] = None,
    user_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63c38b4a84c27c159038a7ab31110e5032bef8ddad181f04f0b754232fb1ed44(
    *,
    add_grants_to_resources: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__604f514db426465dbc092293e7b2e46f5358ddb17770a96f51ef7e6a5f6d15f4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    user: IUser,
    serial: typing.Optional[jsii.Number] = None,
    status: typing.Optional[AccessKeyStatus] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2773dd1c98b9bb45b356173892f3248a430e55c5ab0a22cb6e5df0bcdaa898a5(
    document: PolicyDocument,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c19fda9308c83b1b61fd496fa74f5eddc104dfaf811b56cfe18d29e27da6971(
    policy: IManagedPolicy,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a57592179e2cd5bb2a5698dd5de580c2c15bed0adf0f8f55b31f9abd9fd5846(
    policy: Policy,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67e856ddb493b4542dc716dcab0126ed6ac149cd365202cb608c313320eb7b58(
    grantee: IPrincipal,
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0b3c996a892c638167074eb637574936aa29a63e5e76ed7d460ff90993815e6(
    grantee: IPrincipal,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a259325b943101480d852a30d681aee828d57198b8501de84e4d9963505af62(
    grantee: IPrincipal,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17a32edfd359a804d50015e17cf8c5632c9a0e28c3542088534431b5ae1090e3(
    group: IGroup,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__771573f5504b0120c9b82d20864766023cef9d916834720ff78de68c51d14153(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    assumed_by: IPrincipal,
    description: typing.Optional[builtins.str] = None,
    external_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    inline_policies: typing.Optional[typing.Mapping[builtins.str, PolicyDocument]] = None,
    managed_policies: typing.Optional[typing.Sequence[IManagedPolicy]] = None,
    max_session_duration: typing.Optional[_Duration_4839e8c3] = None,
    path: typing.Optional[builtins.str] = None,
    permissions_boundary: typing.Optional[IManagedPolicy] = None,
    role_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43833b8b06cff5918ffc7655ee5b826bd75570f638200a98519f8c2ebf0372b5(
    policy: IManagedPolicy,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c166a85c28147c9f37dcd0918c774393f73316341430625933ab60ba8c826890(
    statement: PolicyStatement,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__360ff356db658c7d68d451f8da5ae3d55112b9a2f638786bc4cdaea9658802b8(
    statement: PolicyStatement,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22f70d75c15f0109cb998f8124e49401dae23a005cccc337014728056eeaa336(
    policy: Policy,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31e7156ac8208f98f3be102fb3156e3f6bcdf5fe871d6df26b60c2e9cf69336f(
    identity: IPrincipal,
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d09b1058d1d2350165fea6b922b2c0fe02ec3216af993738db1f47c4932c55f(
    identity: IPrincipal,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6367cadac69d2b22537737f04814197b71e654eb8d432cbd5b41e484577f1446(
    identity: IPrincipal,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__214cb969b47d061738027497a5718edc40a7ebc688fb6a11b0b38fef268c3b05(
    *,
    assumed_by: IPrincipal,
    description: typing.Optional[builtins.str] = None,
    external_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    inline_policies: typing.Optional[typing.Mapping[builtins.str, PolicyDocument]] = None,
    managed_policies: typing.Optional[typing.Sequence[IManagedPolicy]] = None,
    max_session_duration: typing.Optional[_Duration_4839e8c3] = None,
    path: typing.Optional[builtins.str] = None,
    permissions_boundary: typing.Optional[IManagedPolicy] = None,
    role_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42ee81c5ba382087856f240a875085c5aed8781df1691cfb44f7e6acc7b30673(
    document: PolicyDocument,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45b95100f32cd1955075f2549ccdf50ea07eb9fac9da91437affa72fa70479f9(
    statement: PolicyStatement,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__694de3cb2e0ed269c34a93287704999ec395e28838b40b3e517ecb1615ada2fa(
    _statement: PolicyStatement,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba3f398ed80c1e1a0dc5bdc18716f592ab5d21f2ccdd69f292d4579db4f8920e(
    conditions: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80467c10f35d2de95737da2b6bd8a1e49b25ad1cbfddc90cf983335b0fdcb0e6(
    principal: IPrincipal,
    conditions: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4453baead1238307d35f2c6280eb8ee8b9d8b2c69fd3bc1a186637187dfc8ebb(
    key: builtins.str,
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06f98d5139c999f6bf39f7d3b6b83cf4b629160f211cfac70b66df210aafd59c(
    conditions: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f3b5797da3ed30fffb5a07fdbc780cf2bb80f8c955f12f28429742fe81076d9(
    doc: PolicyDocument,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de4963000e34b16a5638f4c44067171e566faa24c22a4a7cc74d90b52ec2976a(
    statement: PolicyStatement,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc14ce5e667818ff09808b3d56342245457ad7af45baf54098e3554bdfbb9c5d(
    statement: PolicyStatement,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c48145b0627d702d4a653d7ea8b27af46eec5c5caee28fa1b477e7a6b7ee9b6(
    append: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efe80cc42a362ee0de99d64f7cf860226cb252074012ad3a5ff62f47ec94abae(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    assumed_by: IPrincipal,
    description: typing.Optional[builtins.str] = None,
    external_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    inline_policies: typing.Optional[typing.Mapping[builtins.str, PolicyDocument]] = None,
    managed_policies: typing.Optional[typing.Sequence[IManagedPolicy]] = None,
    max_session_duration: typing.Optional[_Duration_4839e8c3] = None,
    path: typing.Optional[builtins.str] = None,
    permissions_boundary: typing.Optional[IManagedPolicy] = None,
    role_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3abda5df0b9e172ab6b6506372119fbc1518a3e56245c4130fbbbd57373a8cb5(
    scope: _constructs_77d1e7e8.Construct,
    *,
    prevent_synthesis: typing.Optional[builtins.bool] = None,
    use_precreated_roles: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c43d6c30d91c1507a4d83080c4d03e80839da9ab22909456251bc529eb41a48(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    role_arn: builtins.str,
    *,
    add_grants_to_resources: typing.Optional[builtins.bool] = None,
    default_policy_name: typing.Optional[builtins.str] = None,
    mutable: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ea076ee8cb2b2334bd316dea50996363cb2544fbad031a486b3c1d584e2a0aa(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    role_name: builtins.str,
    *,
    add_grants_to_resources: typing.Optional[builtins.bool] = None,
    default_policy_name: typing.Optional[builtins.str] = None,
    mutable: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40a28d979d193e374e71b2cd587b8f95f7bbca459116e6d16c987738134119fe(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b3ebdee2cbdf8c694d4ae443ef5b2e0d8fa417a4913c0abb90a83eb91dc3733(
    policy: IManagedPolicy,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__138765eba0bce05f18e74c04f9874eca5b353ef80b5afc6a733d36c809ed5a25(
    statement: PolicyStatement,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6168031f65ea6f5bbc6ae6d7207de3c8b2039038e0a8ddec4cc0db5ef919299d(
    statement: PolicyStatement,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6daee5d0cd9791a7321d18f729dc2d93548a8a15705bd861a902bd0dbae73cf6(
    policy: Policy,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14c932caa1eadf56fd976a12545a5f150425c6f5a3ea878d9bb6ff0b3e24cd46(
    grantee: IPrincipal,
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e41637797f37e9e841bf058d39d0b910ed287ffbdcfeb24f7652a386a18b61e(
    identity: IPrincipal,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ac7870e7ae4f160829d1eaf7f6d20c937b9c938e96709e254eb1422b6989700(
    identity: IPrincipal,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2745f75caaf5bf82ce9582f03d25e19c93145745996ad93d343457dd927d8007(
    service: builtins.str,
    *,
    conditions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb337dcddbd70acf0d25c8d6f2b9ec2e9bae9105c6aa6db67b9a3c2354bf684b(
    service: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__215a039cacc00cbccb40418a20fcc0e80fb7dd31e57c9d0c0d0356a9a790712d(
    principal: IPrincipal,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25844b9c8aff78b5d8d0dcc4f9fc6ccfe89e32ec78de55d3ce8260e20bdaefbc(
    doc: PolicyDocument,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ce41cc2346f2ebbd7c1e4b4722e1ee8d346119ac63045afc316c940631f9141(
    statement: PolicyStatement,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbc62d90b05edca6f8d13d813c28fe7dc43759fba6779d5577f60de0344b39f2(
    statement: PolicyStatement,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f6570adbc6df85f505162eefc0b9a41164dc55f58d0ed93c10d47d5a1ecd669(
    append: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef7259f99a29e3c7c58c43ee586670c112f44b42e5364d12a09a03f3e23e008f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    groups: typing.Optional[typing.Sequence[IGroup]] = None,
    managed_policies: typing.Optional[typing.Sequence[IManagedPolicy]] = None,
    password: typing.Optional[_SecretValue_3dd0ddae] = None,
    password_reset_required: typing.Optional[builtins.bool] = None,
    path: typing.Optional[builtins.str] = None,
    permissions_boundary: typing.Optional[IManagedPolicy] = None,
    user_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f33e29e061af19beff293732951c7a6d99741716ad9f7bc86023959d5cdd535d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    user_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5958a1f11a99684a3e852867fdde9311b58b9cddac80d1d8960f16a03f113e2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    user_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b8c426fc5ef927d751eda7ff78c09000e89b63da6804dc345c76e762568b602(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    user_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7748f62b253a3a856fa72ad5ed5a163b0c9bc0cdf07e2c6fbb666420c4caf464(
    policy: IManagedPolicy,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31a18f03acf086224c5283fb04241844d012d625b3226dc86059d3dbe23841a1(
    group: IGroup,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc9d48f42d89386c4c39fee9b294cf26d7165fba930b228997d4f866ec04a340(
    statement: PolicyStatement,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__add40848d812b2b19e71bd4e186b890cfd72dfc35ae18ae5733132e665b366a6(
    statement: PolicyStatement,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ebb8924f05370c7968859fd9c4bc9b3ab97a7fcbee56ddd82313a0a6038f3d0(
    policy: Policy,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a6d6c32d3e183186382b39b6b11487d115ae752f5ad9109d40863d0f5d49536(
    arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4053cc6c8a246179292ae366feb44cbec456a8fe5d81ab3ded5bd52657116d7f(
    organization_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22e250eb0875ea5bc04b33f170117ce4bdb9a3d40b2e26bdff85831b69831b6f(
    canonical_user_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab13bb781032f3d9d6e5e0937284451c23201075b7417c49ce544c4414bf41e3(
    *principals: IPrincipal,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d76c23cbda04481b176ab94cd5ee3b4fce9aef14001b0c32d2e77dead6e97197(
    *principals: IPrincipal,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a3e58b43a166e7406b94ea031be5cae69807e96df4fcf4693d630bcd8b11551(
    doc: PolicyDocument,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c749f64109d7c36ddb9493478d4b0593ab5de546886b36477d9cbf39e486306(
    federated: builtins.str,
    conditions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    assume_role_action: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dc4375c7e3b272eef905d1d27c4bd67aa9d9f51ccb424f15955369df5f52edd(
    organization_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__703e9a9603562e94536f153d5ccc52492ff19cc38ed968f3b1f3e31592a8ae7f(
    saml_provider: ISamlProvider,
    conditions: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c81facd20ae242e2b4956594bdbb7a0322ce30953b66f3849bf4961e03e6f7ba(
    identity_provider: builtins.str,
    conditions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39ac905e3b21cb76d85b13b658dee1bcf9822e6af870299fb037df092642ec81(
    account_id: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b516a0686a548e570bd88d7c4c375e62f54baff3fc092d817ad9c2403b62715(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    group_name: typing.Optional[builtins.str] = None,
    managed_policies: typing.Optional[typing.Sequence[IManagedPolicy]] = None,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16bb559f9cd4a61e31d9831c49f44aae4279f1bc47714c390ef63d433654c0dd(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfa77f640d9bc653654c474376cfff254a2c4f7d0f6875a80eb44b243e1dc369(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0073d4596a3cd9c2b07a428313a1c04604bd8df34c71816c90136ffa7c58ecb0(
    policy: IManagedPolicy,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7efe2608ceefd191431a8adea13871fda6fe3193bf8171a4ead0318828be5264(
    statement: PolicyStatement,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f66e324527f4dca14250545b90ce229575ffc379f162d485eb2c630ba43e00b5(
    statement: PolicyStatement,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d2ddce83ad48ecf3ade5fa694be3a205a6dce4cf4669aa568be1ffb0df38d34(
    user: IUser,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8334d09c64ac01b56e25eccb0dd778a954e4f613c776ac3447cf3f1318a89d7(
    policy: Policy,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11057e2b11d9138bde96aa84215de1b5dba16e8c36af672dbebea8a1c33f4310(
    open_id_connect_provider: IOpenIdConnectProvider,
    conditions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7271e79a3715a166397ac94ded3c4043db8b40c10213ffae6abbb3a17ce6768(
    saml_provider: ISamlProvider,
    conditions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass
