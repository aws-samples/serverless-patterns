'''
# Amazon ECR Construct Library

This package contains constructs for working with Amazon Elastic Container Registry.

## Repositories

Define a repository by creating a new instance of `Repository`. A repository
holds multiple versions of a single container image.

```python
repository = ecr.Repository(self, "Repository")
```

## Image scanning

Amazon ECR image scanning helps in identifying software vulnerabilities in your container images.
You can manually scan container images stored in Amazon ECR, or you can configure your repositories
to scan images when you push them to a repository. To create a new repository to scan on push, simply
enable `imageScanOnPush` in the properties.

```python
repository = ecr.Repository(self, "Repo",
    image_scan_on_push=True
)
```

To create an `onImageScanCompleted` event rule and trigger the event target

```python
# repository: ecr.Repository
# target: SomeTarget


repository.on_image_scan_completed("ImageScanComplete").add_target(target)
```

### Authorization Token

Besides the Amazon ECR APIs, ECR also allows the Docker CLI or a language-specific Docker library to push and pull
images from an ECR repository. However, the Docker CLI does not support native IAM authentication methods and
additional steps must be taken so that Amazon ECR can authenticate and authorize Docker push and pull requests.
More information can be found at at [Registry Authentication](https://docs.aws.amazon.com/AmazonECR/latest/userguide/Registries.html#registry_auth).

A Docker authorization token can be obtained using the `GetAuthorizationToken` ECR API. The following code snippets
grants an IAM user access to call this API.

```python
user = iam.User(self, "User")
ecr.AuthorizationToken.grant_read(user)
```

If you access images in the [Public ECR Gallery](https://gallery.ecr.aws/) as well, it is recommended you authenticate to the registry to benefit from
higher rate and bandwidth limits.

> See `Pricing` in https://aws.amazon.com/blogs/aws/amazon-ecr-public-a-new-public-container-registry/ and [Service quotas](https://docs.aws.amazon.com/AmazonECR/latest/public/public-service-quotas.html).

The following code snippet grants an IAM user access to retrieve an authorization token for the public gallery.

```python
user = iam.User(self, "User")
ecr.PublicGalleryAuthorizationToken.grant_read(user)
```

This user can then proceed to login to the registry using one of the [authentication methods](https://docs.aws.amazon.com/AmazonECR/latest/public/public-registries.html#public-registry-auth).

### Other Grantee

#### grantPush

The grantPush method grants the specified IAM entity (the grantee) permission to push images to the ECR repository. Specifically, it grants permissions for the following actions:

* 'ecr:CompleteLayerUpload'
* 'ecr:UploadLayerPart'
* 'ecr:InitiateLayerUpload'
* 'ecr:BatchCheckLayerAvailability'
* 'ecr:PutImage'
* 'ecr:GetAuthorizationToken'

Here is an example of granting a user push permissions:

```python
# repository: ecr.Repository


role = iam.Role(self, "Role",
    assumed_by=iam.ServicePrincipal("codebuild.amazonaws.com")
)
repository.grant_push(role)
```

#### grantPull

The grantPull method grants the specified IAM entity (the grantee) permission to pull images from the ECR repository. Specifically, it grants permissions for the following actions:

* 'ecr:BatchCheckLayerAvailability'
* 'ecr:GetDownloadUrlForLayer'
* 'ecr:BatchGetImage'
* 'ecr:GetAuthorizationToken'

```python
# repository: ecr.Repository


role = iam.Role(self, "Role",
    assumed_by=iam.ServicePrincipal("codebuild.amazonaws.com")
)
repository.grant_pull(role)
```

#### grantPullPush

The grantPullPush method grants the specified IAM entity (the grantee) permission to both pull and push images from/to the ECR repository. Specifically, it grants permissions for all the actions required for pull and push permissions.

Here is an example of granting a user both pull and push permissions:

```python
# repository: ecr.Repository


role = iam.Role(self, "Role",
    assumed_by=iam.ServicePrincipal("codebuild.amazonaws.com")
)
repository.grant_pull_push(role)
```

By using these methods, you can grant specific operational permissions on the ECR repository to IAM entities. This allows for proper management of access to the repository and ensures security.

### Image tag immutability

You can set tag immutability on images in our repository using the `imageTagMutability` construct prop.

```python
ecr.Repository(self, "Repo", image_tag_mutability=ecr.TagMutability.IMMUTABLE)
```

### Encryption

By default, Amazon ECR uses server-side encryption with Amazon S3-managed encryption keys which encrypts your data at rest using an AES-256 encryption algorithm. For more control over the encryption for your Amazon ECR repositories, you can use server-side encryption with KMS keys stored in AWS Key Management Service (AWS KMS). Read more about this feature in the [ECR Developer Guide](https://docs.aws.amazon.com/AmazonECR/latest/userguide/encryption-at-rest.html).

When you use AWS KMS to encrypt your data, you can either use the default AWS managed key, which is managed by Amazon ECR, by specifying `RepositoryEncryption.KMS` in the `encryption` property. Or specify your own customer managed KMS key, by specifying the `encryptionKey` property.

When `encryptionKey` is set, the `encryption` property must be `KMS` or empty.

In the case `encryption` is set to `KMS` but no `encryptionKey` is set, an AWS managed KMS key is used.

```python
ecr.Repository(self, "Repo",
    encryption=ecr.RepositoryEncryption.KMS
)
```

Otherwise, a customer-managed KMS key is used if `encryptionKey` was set and `encryption` was optionally set to `KMS`.

```python
import aws_cdk.aws_kms as kms


ecr.Repository(self, "Repo",
    encryption_key=kms.Key(self, "Key")
)
```

## Automatically clean up repositories

You can set life cycle rules to automatically clean up old images from your
repository. The first life cycle rule that matches an image will be applied
against that image. For example, the following deletes images older than
30 days, while keeping all images tagged with prod (note that the order
is important here):

```python
# repository: ecr.Repository

repository.add_lifecycle_rule(tag_prefix_list=["prod"], max_image_count=9999)
repository.add_lifecycle_rule(max_image_age=Duration.days(30))
```

When using `tagPatternList`, an image is successfully matched if it matches
the wildcard filter.

```python
# repository: ecr.Repository

repository.add_lifecycle_rule(tag_pattern_list=["prod*"], max_image_count=9999)
```

### Repository deletion

When a repository is removed from a stack (or the stack is deleted), the ECR
repository will be removed according to its removal policy (which by default will
simply orphan the repository and leave it in your AWS account). If the removal
policy is set to `RemovalPolicy.DESTROY`, the repository will be deleted as long
as it does not contain any images.

To override this and force all images to get deleted during repository deletion,
enable the `emptyOnDelete` option as well as setting the removal policy to
`RemovalPolicy.DESTROY`.

```python
repository = ecr.Repository(self, "MyTempRepo",
    removal_policy=RemovalPolicy.DESTROY,
    empty_on_delete=True
)
```

## Managing the Resource Policy

You can add statements to the resource policy of the repository using the
`addToResourcePolicy` method. However, be advised that you must not include
a `resources` section in the `PolicyStatement`.

```python
# repository: ecr.Repository

repository.add_to_resource_policy(iam.PolicyStatement(
    actions=["ecr:GetDownloadUrlForLayer"],
    # resources: ['*'], // not currently allowed!
    principals=[iam.AnyPrincipal()]
))
```

## CloudWatch event rules

You can publish repository events to a CloudWatch event rule with `onEvent`:

```python
import aws_cdk.aws_lambda as lambda_
from aws_cdk.aws_events_targets import LambdaFunction


repo = ecr.Repository(self, "Repo")
lambda_handler = lambda_.Function(self, "LambdaFunction",
    runtime=lambda_.Runtime.PYTHON_3_12,
    code=lambda_.Code.from_inline("# dummy func"),
    handler="index.handler"
)

repo.on_event("OnEventTargetLambda",
    target=LambdaFunction(lambda_handler)
)
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
    ResourceProps as _ResourceProps_15a65b4e,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..aws_events import (
    EventPattern as _EventPattern_fe557901,
    IRuleTarget as _IRuleTarget_7a91f454,
    OnEventOptions as _OnEventOptions_8711b8b3,
    Rule as _Rule_334ed2b5,
)
from ..aws_iam import (
    AddToResourcePolicyResult as _AddToResourcePolicyResult_1d0a53ad,
    Grant as _Grant_a7ae64f8,
    IGrantable as _IGrantable_71c4f5de,
    PolicyStatement as _PolicyStatement_0fe33853,
)
from ..aws_kms import IKey as _IKey_5f11635f


class AuthorizationToken(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ecr.AuthorizationToken",
):
    '''Authorization token to access private ECR repositories in the current environment via Docker CLI.

    :see: https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry_auth.html
    :exampleMetadata: infused

    Example::

        user = iam.User(self, "User")
        ecr.AuthorizationToken.grant_read(user)
    '''

    @jsii.member(jsii_name="grantRead")
    @builtins.classmethod
    def grant_read(cls, grantee: _IGrantable_71c4f5de) -> None:
        '''Grant access to retrieve an authorization token.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b189c1467d2bda9405aa4cabd8bab18d9bb346d049339366389c70f4216e7822)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(None, jsii.sinvoke(cls, "grantRead", [grantee]))


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnPublicRepository(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ecr.CfnPublicRepository",
):
    '''The ``AWS::ECR::PublicRepository`` resource specifies an Amazon Elastic Container Registry Public (Amazon ECR Public) repository, where users can push and pull Docker images, Open Container Initiative (OCI) images, and OCI compatible artifacts.

    For more information, see `Amazon ECR public repositories <https://docs.aws.amazon.com/AmazonECR/latest/public/public-repositories.html>`_ in the *Amazon ECR Public User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-publicrepository.html
    :cloudformationResource: AWS::ECR::PublicRepository
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ecr as ecr
        
        # repository_catalog_data: Any
        # repository_policy_text: Any
        
        cfn_public_repository = ecr.CfnPublicRepository(self, "MyCfnPublicRepository",
            repository_catalog_data=repository_catalog_data,
            repository_name="repositoryName",
            repository_policy_text=repository_policy_text,
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
        repository_catalog_data: typing.Any = None,
        repository_name: typing.Optional[builtins.str] = None,
        repository_policy_text: typing.Any = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param repository_catalog_data: The details about the repository that are publicly visible in the Amazon ECR Public Gallery. For more information, see `Amazon ECR Public repository catalog data <https://docs.aws.amazon.com/AmazonECR/latest/public/public-repository-catalog-data.html>`_ in the *Amazon ECR Public User Guide* .
        :param repository_name: The name to use for the public repository. The repository name may be specified on its own (such as ``nginx-web-app`` ) or it can be prepended with a namespace to group the repository into a category (such as ``project-a/nginx-web-app`` ). If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the repository name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ . .. epigraph:: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.
        :param repository_policy_text: The JSON repository policy text to apply to the public repository. For more information, see `Amazon ECR Public repository policies <https://docs.aws.amazon.com/AmazonECR/latest/public/public-repository-policies.html>`_ in the *Amazon ECR Public User Guide* .
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5b1b0a44f7b903d10d3e873896cf1709943b67e3503cc3918e4e98f04ed2c17)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPublicRepositoryProps(
            repository_catalog_data=repository_catalog_data,
            repository_name=repository_name,
            repository_policy_text=repository_policy_text,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__317b166576f7593305ca27885da5cd7a621d59c15390c40d8de8d3e3c28eb94b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e3890a4bb017b2e52f74cb2ffb17f575b120d2d4a4d312e0c59290c8145be664)
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
        '''Returns the Amazon Resource Name (ARN) for the specified ``AWS::ECR::PublicRepository`` resource.

        For example, ``arn:aws:ecr-public:: *123456789012* :repository/ *test-repository*`` .

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
    @jsii.member(jsii_name="repositoryCatalogData")
    def repository_catalog_data(self) -> typing.Any:
        '''The details about the repository that are publicly visible in the Amazon ECR Public Gallery.'''
        return typing.cast(typing.Any, jsii.get(self, "repositoryCatalogData"))

    @repository_catalog_data.setter
    def repository_catalog_data(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff52c4c89f76461de2458e82c2bfd20f4de3951ad8eab58aec1b52004c07cea7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repositoryCatalogData", value)

    @builtins.property
    @jsii.member(jsii_name="repositoryName")
    def repository_name(self) -> typing.Optional[builtins.str]:
        '''The name to use for the public repository.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repositoryName"))

    @repository_name.setter
    def repository_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c540342cfab06c3e938dc25340d0df062558f4ba1bb13c342e9740ee0e1e909a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repositoryName", value)

    @builtins.property
    @jsii.member(jsii_name="repositoryPolicyText")
    def repository_policy_text(self) -> typing.Any:
        '''The JSON repository policy text to apply to the public repository.'''
        return typing.cast(typing.Any, jsii.get(self, "repositoryPolicyText"))

    @repository_policy_text.setter
    def repository_policy_text(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a5d0a391359eb22e8e450fd43d68011135dcfa6d843724b27da64f19e19aad7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repositoryPolicyText", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e01e3d955755b76bef4d0ce1b9a558313454d69c44cb97d65b4fcb564602a54d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ecr.CfnPublicRepository.RepositoryCatalogDataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "about_text": "aboutText",
            "architectures": "architectures",
            "operating_systems": "operatingSystems",
            "repository_description": "repositoryDescription",
            "usage_text": "usageText",
        },
    )
    class RepositoryCatalogDataProperty:
        def __init__(
            self,
            *,
            about_text: typing.Optional[builtins.str] = None,
            architectures: typing.Optional[typing.Sequence[builtins.str]] = None,
            operating_systems: typing.Optional[typing.Sequence[builtins.str]] = None,
            repository_description: typing.Optional[builtins.str] = None,
            usage_text: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The details about the repository that are publicly visible in the Amazon ECR Public Gallery.

            For more information, see `Amazon ECR Public repository catalog data <https://docs.aws.amazon.com/AmazonECR/latest/public/public-repository-catalog-data.html>`_ in the *Amazon ECR Public User Guide* .

            :param about_text: The longform description of the contents of the repository. This text appears in the repository details on the Amazon ECR Public Gallery.
            :param architectures: The architecture tags that are associated with the repository.
            :param operating_systems: The operating system tags that are associated with the repository.
            :param repository_description: The short description of the repository.
            :param usage_text: The longform usage details of the contents of the repository. The usage text provides context for users of the repository.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-publicrepository-repositorycatalogdata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ecr as ecr
                
                repository_catalog_data_property = ecr.CfnPublicRepository.RepositoryCatalogDataProperty(
                    about_text="aboutText",
                    architectures=["architectures"],
                    operating_systems=["operatingSystems"],
                    repository_description="repositoryDescription",
                    usage_text="usageText"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fc5ac22c59e9479a770d5c069f616e21f7babce6447100492c58de88f31b34d6)
                check_type(argname="argument about_text", value=about_text, expected_type=type_hints["about_text"])
                check_type(argname="argument architectures", value=architectures, expected_type=type_hints["architectures"])
                check_type(argname="argument operating_systems", value=operating_systems, expected_type=type_hints["operating_systems"])
                check_type(argname="argument repository_description", value=repository_description, expected_type=type_hints["repository_description"])
                check_type(argname="argument usage_text", value=usage_text, expected_type=type_hints["usage_text"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if about_text is not None:
                self._values["about_text"] = about_text
            if architectures is not None:
                self._values["architectures"] = architectures
            if operating_systems is not None:
                self._values["operating_systems"] = operating_systems
            if repository_description is not None:
                self._values["repository_description"] = repository_description
            if usage_text is not None:
                self._values["usage_text"] = usage_text

        @builtins.property
        def about_text(self) -> typing.Optional[builtins.str]:
            '''The longform description of the contents of the repository.

            This text appears in the repository details on the Amazon ECR Public Gallery.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-publicrepository-repositorycatalogdata.html#cfn-ecr-publicrepository-repositorycatalogdata-abouttext
            '''
            result = self._values.get("about_text")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def architectures(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The architecture tags that are associated with the repository.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-publicrepository-repositorycatalogdata.html#cfn-ecr-publicrepository-repositorycatalogdata-architectures
            '''
            result = self._values.get("architectures")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def operating_systems(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The operating system tags that are associated with the repository.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-publicrepository-repositorycatalogdata.html#cfn-ecr-publicrepository-repositorycatalogdata-operatingsystems
            '''
            result = self._values.get("operating_systems")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def repository_description(self) -> typing.Optional[builtins.str]:
            '''The short description of the repository.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-publicrepository-repositorycatalogdata.html#cfn-ecr-publicrepository-repositorycatalogdata-repositorydescription
            '''
            result = self._values.get("repository_description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def usage_text(self) -> typing.Optional[builtins.str]:
            '''The longform usage details of the contents of the repository.

            The usage text provides context for users of the repository.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-publicrepository-repositorycatalogdata.html#cfn-ecr-publicrepository-repositorycatalogdata-usagetext
            '''
            result = self._values.get("usage_text")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RepositoryCatalogDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ecr.CfnPublicRepositoryProps",
    jsii_struct_bases=[],
    name_mapping={
        "repository_catalog_data": "repositoryCatalogData",
        "repository_name": "repositoryName",
        "repository_policy_text": "repositoryPolicyText",
        "tags": "tags",
    },
)
class CfnPublicRepositoryProps:
    def __init__(
        self,
        *,
        repository_catalog_data: typing.Any = None,
        repository_name: typing.Optional[builtins.str] = None,
        repository_policy_text: typing.Any = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPublicRepository``.

        :param repository_catalog_data: The details about the repository that are publicly visible in the Amazon ECR Public Gallery. For more information, see `Amazon ECR Public repository catalog data <https://docs.aws.amazon.com/AmazonECR/latest/public/public-repository-catalog-data.html>`_ in the *Amazon ECR Public User Guide* .
        :param repository_name: The name to use for the public repository. The repository name may be specified on its own (such as ``nginx-web-app`` ) or it can be prepended with a namespace to group the repository into a category (such as ``project-a/nginx-web-app`` ). If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the repository name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ . .. epigraph:: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.
        :param repository_policy_text: The JSON repository policy text to apply to the public repository. For more information, see `Amazon ECR Public repository policies <https://docs.aws.amazon.com/AmazonECR/latest/public/public-repository-policies.html>`_ in the *Amazon ECR Public User Guide* .
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-publicrepository.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ecr as ecr
            
            # repository_catalog_data: Any
            # repository_policy_text: Any
            
            cfn_public_repository_props = ecr.CfnPublicRepositoryProps(
                repository_catalog_data=repository_catalog_data,
                repository_name="repositoryName",
                repository_policy_text=repository_policy_text,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92fbf4d1252b7ea335bc4ed7360447e55242ed532586420ec9671bdac83ae8d8)
            check_type(argname="argument repository_catalog_data", value=repository_catalog_data, expected_type=type_hints["repository_catalog_data"])
            check_type(argname="argument repository_name", value=repository_name, expected_type=type_hints["repository_name"])
            check_type(argname="argument repository_policy_text", value=repository_policy_text, expected_type=type_hints["repository_policy_text"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if repository_catalog_data is not None:
            self._values["repository_catalog_data"] = repository_catalog_data
        if repository_name is not None:
            self._values["repository_name"] = repository_name
        if repository_policy_text is not None:
            self._values["repository_policy_text"] = repository_policy_text
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def repository_catalog_data(self) -> typing.Any:
        '''The details about the repository that are publicly visible in the Amazon ECR Public Gallery.

        For more information, see `Amazon ECR Public repository catalog data <https://docs.aws.amazon.com/AmazonECR/latest/public/public-repository-catalog-data.html>`_ in the *Amazon ECR Public User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-publicrepository.html#cfn-ecr-publicrepository-repositorycatalogdata
        '''
        result = self._values.get("repository_catalog_data")
        return typing.cast(typing.Any, result)

    @builtins.property
    def repository_name(self) -> typing.Optional[builtins.str]:
        '''The name to use for the public repository.

        The repository name may be specified on its own (such as ``nginx-web-app`` ) or it can be prepended with a namespace to group the repository into a category (such as ``project-a/nginx-web-app`` ). If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the repository name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ .
        .. epigraph::

           If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-publicrepository.html#cfn-ecr-publicrepository-repositoryname
        '''
        result = self._values.get("repository_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def repository_policy_text(self) -> typing.Any:
        '''The JSON repository policy text to apply to the public repository.

        For more information, see `Amazon ECR Public repository policies <https://docs.aws.amazon.com/AmazonECR/latest/public/public-repository-policies.html>`_ in the *Amazon ECR Public User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-publicrepository.html#cfn-ecr-publicrepository-repositorypolicytext
        '''
        result = self._values.get("repository_policy_text")
        return typing.cast(typing.Any, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-publicrepository.html#cfn-ecr-publicrepository-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPublicRepositoryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnPullThroughCacheRule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ecr.CfnPullThroughCacheRule",
):
    '''The ``AWS::ECR::PullThroughCacheRule`` resource creates or updates a pull through cache rule.

    A pull through cache rule provides a way to cache images from an upstream registry in your Amazon ECR private registry.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-pullthroughcacherule.html
    :cloudformationResource: AWS::ECR::PullThroughCacheRule
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ecr as ecr
        
        cfn_pull_through_cache_rule = ecr.CfnPullThroughCacheRule(self, "MyCfnPullThroughCacheRule",
            credential_arn="credentialArn",
            ecr_repository_prefix="ecrRepositoryPrefix",
            upstream_registry="upstreamRegistry",
            upstream_registry_url="upstreamRegistryUrl"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        credential_arn: typing.Optional[builtins.str] = None,
        ecr_repository_prefix: typing.Optional[builtins.str] = None,
        upstream_registry: typing.Optional[builtins.str] = None,
        upstream_registry_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param credential_arn: The ARN of the Secrets Manager secret associated with the pull through cache rule.
        :param ecr_repository_prefix: The Amazon ECR repository prefix associated with the pull through cache rule.
        :param upstream_registry: The name of the upstream source registry associated with the pull through cache rule.
        :param upstream_registry_url: The upstream registry URL associated with the pull through cache rule.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d43871e7810dc89346a08c3c9c24a04a2b82bf02da0d8fa05ef0df564aea4986)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPullThroughCacheRuleProps(
            credential_arn=credential_arn,
            ecr_repository_prefix=ecr_repository_prefix,
            upstream_registry=upstream_registry,
            upstream_registry_url=upstream_registry_url,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d8119fd2e97a8168e1c38fa9f34bcdb5556aadec2158866fb3fdc43828f6206)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c4a9a8ae5483bccddfb96a4fda4c50b5e880bc70af4044cf5bd93d1432c10c1d)
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
    @jsii.member(jsii_name="credentialArn")
    def credential_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the Secrets Manager secret associated with the pull through cache rule.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "credentialArn"))

    @credential_arn.setter
    def credential_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a379fdfcc316f1fba45c0243614513599bd6a9e9b599a9e279a8cc606e4bf382)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "credentialArn", value)

    @builtins.property
    @jsii.member(jsii_name="ecrRepositoryPrefix")
    def ecr_repository_prefix(self) -> typing.Optional[builtins.str]:
        '''The Amazon ECR repository prefix associated with the pull through cache rule.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ecrRepositoryPrefix"))

    @ecr_repository_prefix.setter
    def ecr_repository_prefix(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97e7364a9d8ce3c9c0a95d7d650a21956fb29a984bd55c4450ace32814a23728)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ecrRepositoryPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="upstreamRegistry")
    def upstream_registry(self) -> typing.Optional[builtins.str]:
        '''The name of the upstream source registry associated with the pull through cache rule.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "upstreamRegistry"))

    @upstream_registry.setter
    def upstream_registry(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e6176654c03645cd104e31d54362eb32d0b3856b8d7015586ea920e9ef9cc77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "upstreamRegistry", value)

    @builtins.property
    @jsii.member(jsii_name="upstreamRegistryUrl")
    def upstream_registry_url(self) -> typing.Optional[builtins.str]:
        '''The upstream registry URL associated with the pull through cache rule.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "upstreamRegistryUrl"))

    @upstream_registry_url.setter
    def upstream_registry_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7eb1d214154bb7e817af1779f0f5bf9f4b1c880ec0a8357fa98987f1063b451f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "upstreamRegistryUrl", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ecr.CfnPullThroughCacheRuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "credential_arn": "credentialArn",
        "ecr_repository_prefix": "ecrRepositoryPrefix",
        "upstream_registry": "upstreamRegistry",
        "upstream_registry_url": "upstreamRegistryUrl",
    },
)
class CfnPullThroughCacheRuleProps:
    def __init__(
        self,
        *,
        credential_arn: typing.Optional[builtins.str] = None,
        ecr_repository_prefix: typing.Optional[builtins.str] = None,
        upstream_registry: typing.Optional[builtins.str] = None,
        upstream_registry_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnPullThroughCacheRule``.

        :param credential_arn: The ARN of the Secrets Manager secret associated with the pull through cache rule.
        :param ecr_repository_prefix: The Amazon ECR repository prefix associated with the pull through cache rule.
        :param upstream_registry: The name of the upstream source registry associated with the pull through cache rule.
        :param upstream_registry_url: The upstream registry URL associated with the pull through cache rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-pullthroughcacherule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ecr as ecr
            
            cfn_pull_through_cache_rule_props = ecr.CfnPullThroughCacheRuleProps(
                credential_arn="credentialArn",
                ecr_repository_prefix="ecrRepositoryPrefix",
                upstream_registry="upstreamRegistry",
                upstream_registry_url="upstreamRegistryUrl"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e53d5495feeae3bec08dd309eceed79d390d73c31e234c306abd812ec670db16)
            check_type(argname="argument credential_arn", value=credential_arn, expected_type=type_hints["credential_arn"])
            check_type(argname="argument ecr_repository_prefix", value=ecr_repository_prefix, expected_type=type_hints["ecr_repository_prefix"])
            check_type(argname="argument upstream_registry", value=upstream_registry, expected_type=type_hints["upstream_registry"])
            check_type(argname="argument upstream_registry_url", value=upstream_registry_url, expected_type=type_hints["upstream_registry_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if credential_arn is not None:
            self._values["credential_arn"] = credential_arn
        if ecr_repository_prefix is not None:
            self._values["ecr_repository_prefix"] = ecr_repository_prefix
        if upstream_registry is not None:
            self._values["upstream_registry"] = upstream_registry
        if upstream_registry_url is not None:
            self._values["upstream_registry_url"] = upstream_registry_url

    @builtins.property
    def credential_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the Secrets Manager secret associated with the pull through cache rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-pullthroughcacherule.html#cfn-ecr-pullthroughcacherule-credentialarn
        '''
        result = self._values.get("credential_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ecr_repository_prefix(self) -> typing.Optional[builtins.str]:
        '''The Amazon ECR repository prefix associated with the pull through cache rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-pullthroughcacherule.html#cfn-ecr-pullthroughcacherule-ecrrepositoryprefix
        '''
        result = self._values.get("ecr_repository_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def upstream_registry(self) -> typing.Optional[builtins.str]:
        '''The name of the upstream source registry associated with the pull through cache rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-pullthroughcacherule.html#cfn-ecr-pullthroughcacherule-upstreamregistry
        '''
        result = self._values.get("upstream_registry")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def upstream_registry_url(self) -> typing.Optional[builtins.str]:
        '''The upstream registry URL associated with the pull through cache rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-pullthroughcacherule.html#cfn-ecr-pullthroughcacherule-upstreamregistryurl
        '''
        result = self._values.get("upstream_registry_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPullThroughCacheRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnRegistryPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ecr.CfnRegistryPolicy",
):
    '''The ``AWS::ECR::RegistryPolicy`` resource creates or updates the permissions policy for a private registry.

    A private registry policy is used to specify permissions for another AWS account and is used when configuring cross-account replication. For more information, see `Registry permissions <https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry-permissions.html>`_ in the *Amazon Elastic Container Registry User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-registrypolicy.html
    :cloudformationResource: AWS::ECR::RegistryPolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ecr as ecr
        
        # policy_text: Any
        
        cfn_registry_policy = ecr.CfnRegistryPolicy(self, "MyCfnRegistryPolicy",
            policy_text=policy_text
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        policy_text: typing.Any,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param policy_text: The JSON policy text for your registry.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46ab6d6ee08d8397c3ef5738c56a6b991e46657e46e9bb7db4c65859782e8b95)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRegistryPolicyProps(policy_text=policy_text)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__518326f401673fc075bc36aad49fa8c732bf800dcb0a35c514296a4680b8b006)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b830f40efb29b77f187b8cdd48dd5f42b9758bdfaa5f26f17a5410aaba10f2a2)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrRegistryId")
    def attr_registry_id(self) -> builtins.str:
        '''The account ID of the private registry the policy is associated with.

        :cloudformationAttribute: RegistryId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRegistryId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="policyText")
    def policy_text(self) -> typing.Any:
        '''The JSON policy text for your registry.'''
        return typing.cast(typing.Any, jsii.get(self, "policyText"))

    @policy_text.setter
    def policy_text(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22f296a7fd25dcbd0e6d71e5f19c5a64bea31bc39494f50b1a2fdceb3a96d82b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyText", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ecr.CfnRegistryPolicyProps",
    jsii_struct_bases=[],
    name_mapping={"policy_text": "policyText"},
)
class CfnRegistryPolicyProps:
    def __init__(self, *, policy_text: typing.Any) -> None:
        '''Properties for defining a ``CfnRegistryPolicy``.

        :param policy_text: The JSON policy text for your registry.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-registrypolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ecr as ecr
            
            # policy_text: Any
            
            cfn_registry_policy_props = ecr.CfnRegistryPolicyProps(
                policy_text=policy_text
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61caec2d35981c77552d8e7762d2c96379773ad1cbd183c24427fd9006273d94)
            check_type(argname="argument policy_text", value=policy_text, expected_type=type_hints["policy_text"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_text": policy_text,
        }

    @builtins.property
    def policy_text(self) -> typing.Any:
        '''The JSON policy text for your registry.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-registrypolicy.html#cfn-ecr-registrypolicy-policytext
        '''
        result = self._values.get("policy_text")
        assert result is not None, "Required property 'policy_text' is missing"
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRegistryPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnReplicationConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ecr.CfnReplicationConfiguration",
):
    '''The ``AWS::ECR::ReplicationConfiguration`` resource creates or updates the replication configuration for a private registry.

    The first time a replication configuration is applied to a private registry, a service-linked IAM role is created in your account for the replication process. For more information, see `Using Service-Linked Roles for Amazon ECR <https://docs.aws.amazon.com/AmazonECR/latest/userguide/using-service-linked-roles.html>`_ in the *Amazon Elastic Container Registry User Guide* .
    .. epigraph::

       When configuring cross-account replication, the destination account must grant the source account permission to replicate. This permission is controlled using a private registry permissions policy. For more information, see ``AWS::ECR::RegistryPolicy`` .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-replicationconfiguration.html
    :cloudformationResource: AWS::ECR::ReplicationConfiguration
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ecr as ecr
        
        cfn_replication_configuration = ecr.CfnReplicationConfiguration(self, "MyCfnReplicationConfiguration",
            replication_configuration=ecr.CfnReplicationConfiguration.ReplicationConfigurationProperty(
                rules=[ecr.CfnReplicationConfiguration.ReplicationRuleProperty(
                    destinations=[ecr.CfnReplicationConfiguration.ReplicationDestinationProperty(
                        region="region",
                        registry_id="registryId"
                    )],
        
                    # the properties below are optional
                    repository_filters=[ecr.CfnReplicationConfiguration.RepositoryFilterProperty(
                        filter="filter",
                        filter_type="filterType"
                    )]
                )]
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        replication_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnReplicationConfiguration.ReplicationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param replication_configuration: The replication configuration for a registry.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ec8853622a7046906439da72fd8cf7dc34848650d739a637e7ae30cf30d26db)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnReplicationConfigurationProps(
            replication_configuration=replication_configuration
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf6794ecc113ab8e22e20dce72c6d4af221f57c5e7b6d95be1fa395b94eb50bb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fcdbbdadfe76a214299f1bf1546cbf834942546e6a1a187654f56c7a28e6ee9c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrRegistryId")
    def attr_registry_id(self) -> builtins.str:
        '''The account ID of the destination registry.

        :cloudformationAttribute: RegistryId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRegistryId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="replicationConfiguration")
    def replication_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnReplicationConfiguration.ReplicationConfigurationProperty"]:
        '''The replication configuration for a registry.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnReplicationConfiguration.ReplicationConfigurationProperty"], jsii.get(self, "replicationConfiguration"))

    @replication_configuration.setter
    def replication_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnReplicationConfiguration.ReplicationConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99f4c1062f6a81bbbbbb1ec51556be75ca089974820458f2cf7c2b6ef30a1f4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationConfiguration", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ecr.CfnReplicationConfiguration.ReplicationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"rules": "rules"},
    )
    class ReplicationConfigurationProperty:
        def __init__(
            self,
            *,
            rules: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnReplicationConfiguration.ReplicationRuleProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''The replication configuration for a registry.

            :param rules: An array of objects representing the replication destinations and repository filters for a replication configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-replicationconfiguration-replicationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ecr as ecr
                
                replication_configuration_property = ecr.CfnReplicationConfiguration.ReplicationConfigurationProperty(
                    rules=[ecr.CfnReplicationConfiguration.ReplicationRuleProperty(
                        destinations=[ecr.CfnReplicationConfiguration.ReplicationDestinationProperty(
                            region="region",
                            registry_id="registryId"
                        )],
                
                        # the properties below are optional
                        repository_filters=[ecr.CfnReplicationConfiguration.RepositoryFilterProperty(
                            filter="filter",
                            filter_type="filterType"
                        )]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4f1a61ec35ac6455ef5be103b0ad56cd75e35b592381509aff016aeca6fc509b)
                check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "rules": rules,
            }

        @builtins.property
        def rules(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnReplicationConfiguration.ReplicationRuleProperty"]]]:
            '''An array of objects representing the replication destinations and repository filters for a replication configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-replicationconfiguration-replicationconfiguration.html#cfn-ecr-replicationconfiguration-replicationconfiguration-rules
            '''
            result = self._values.get("rules")
            assert result is not None, "Required property 'rules' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnReplicationConfiguration.ReplicationRuleProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReplicationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ecr.CfnReplicationConfiguration.ReplicationDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"region": "region", "registry_id": "registryId"},
    )
    class ReplicationDestinationProperty:
        def __init__(self, *, region: builtins.str, registry_id: builtins.str) -> None:
            '''An array of objects representing the destination for a replication rule.

            :param region: The Region to replicate to.
            :param registry_id: The AWS account ID of the Amazon ECR private registry to replicate to. When configuring cross-Region replication within your own registry, specify your own account ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-replicationconfiguration-replicationdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ecr as ecr
                
                replication_destination_property = ecr.CfnReplicationConfiguration.ReplicationDestinationProperty(
                    region="region",
                    registry_id="registryId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__be71124f033e3826f4c32205bda1d3adb39ad2e783cc193fc52ee22d7f1e2eab)
                check_type(argname="argument region", value=region, expected_type=type_hints["region"])
                check_type(argname="argument registry_id", value=registry_id, expected_type=type_hints["registry_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "region": region,
                "registry_id": registry_id,
            }

        @builtins.property
        def region(self) -> builtins.str:
            '''The Region to replicate to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-replicationconfiguration-replicationdestination.html#cfn-ecr-replicationconfiguration-replicationdestination-region
            '''
            result = self._values.get("region")
            assert result is not None, "Required property 'region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def registry_id(self) -> builtins.str:
            '''The AWS account ID of the Amazon ECR private registry to replicate to.

            When configuring cross-Region replication within your own registry, specify your own account ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-replicationconfiguration-replicationdestination.html#cfn-ecr-replicationconfiguration-replicationdestination-registryid
            '''
            result = self._values.get("registry_id")
            assert result is not None, "Required property 'registry_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReplicationDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ecr.CfnReplicationConfiguration.ReplicationRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destinations": "destinations",
            "repository_filters": "repositoryFilters",
        },
    )
    class ReplicationRuleProperty:
        def __init__(
            self,
            *,
            destinations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnReplicationConfiguration.ReplicationDestinationProperty", typing.Dict[builtins.str, typing.Any]]]]],
            repository_filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnReplicationConfiguration.RepositoryFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''An array of objects representing the replication destinations and repository filters for a replication configuration.

            :param destinations: An array of objects representing the destination for a replication rule.
            :param repository_filters: An array of objects representing the filters for a replication rule. Specifying a repository filter for a replication rule provides a method for controlling which repositories in a private registry are replicated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-replicationconfiguration-replicationrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ecr as ecr
                
                replication_rule_property = ecr.CfnReplicationConfiguration.ReplicationRuleProperty(
                    destinations=[ecr.CfnReplicationConfiguration.ReplicationDestinationProperty(
                        region="region",
                        registry_id="registryId"
                    )],
                
                    # the properties below are optional
                    repository_filters=[ecr.CfnReplicationConfiguration.RepositoryFilterProperty(
                        filter="filter",
                        filter_type="filterType"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__db6d7133bf506488b87a4ed998e2db1455e219e9bfa903d0880e4240a48da3c6)
                check_type(argname="argument destinations", value=destinations, expected_type=type_hints["destinations"])
                check_type(argname="argument repository_filters", value=repository_filters, expected_type=type_hints["repository_filters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destinations": destinations,
            }
            if repository_filters is not None:
                self._values["repository_filters"] = repository_filters

        @builtins.property
        def destinations(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnReplicationConfiguration.ReplicationDestinationProperty"]]]:
            '''An array of objects representing the destination for a replication rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-replicationconfiguration-replicationrule.html#cfn-ecr-replicationconfiguration-replicationrule-destinations
            '''
            result = self._values.get("destinations")
            assert result is not None, "Required property 'destinations' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnReplicationConfiguration.ReplicationDestinationProperty"]]], result)

        @builtins.property
        def repository_filters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnReplicationConfiguration.RepositoryFilterProperty"]]]]:
            '''An array of objects representing the filters for a replication rule.

            Specifying a repository filter for a replication rule provides a method for controlling which repositories in a private registry are replicated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-replicationconfiguration-replicationrule.html#cfn-ecr-replicationconfiguration-replicationrule-repositoryfilters
            '''
            result = self._values.get("repository_filters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnReplicationConfiguration.RepositoryFilterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReplicationRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ecr.CfnReplicationConfiguration.RepositoryFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"filter": "filter", "filter_type": "filterType"},
    )
    class RepositoryFilterProperty:
        def __init__(self, *, filter: builtins.str, filter_type: builtins.str) -> None:
            '''The filter settings used with image replication.

            Specifying a repository filter to a replication rule provides a method for controlling which repositories in a private registry are replicated. If no filters are added, the contents of all repositories are replicated.

            :param filter: The repository filter details. When the ``PREFIX_MATCH`` filter type is specified, this value is required and should be the repository name prefix to configure replication for.
            :param filter_type: The repository filter type. The only supported value is ``PREFIX_MATCH`` , which is a repository name prefix specified with the ``filter`` parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-replicationconfiguration-repositoryfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ecr as ecr
                
                repository_filter_property = ecr.CfnReplicationConfiguration.RepositoryFilterProperty(
                    filter="filter",
                    filter_type="filterType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__81091e3ace4bd61ec67e8544391ccaefe639b2950197c427c9804e66f026b577)
                check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
                check_type(argname="argument filter_type", value=filter_type, expected_type=type_hints["filter_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "filter": filter,
                "filter_type": filter_type,
            }

        @builtins.property
        def filter(self) -> builtins.str:
            '''The repository filter details.

            When the ``PREFIX_MATCH`` filter type is specified, this value is required and should be the repository name prefix to configure replication for.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-replicationconfiguration-repositoryfilter.html#cfn-ecr-replicationconfiguration-repositoryfilter-filter
            '''
            result = self._values.get("filter")
            assert result is not None, "Required property 'filter' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def filter_type(self) -> builtins.str:
            '''The repository filter type.

            The only supported value is ``PREFIX_MATCH`` , which is a repository name prefix specified with the ``filter`` parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-replicationconfiguration-repositoryfilter.html#cfn-ecr-replicationconfiguration-repositoryfilter-filtertype
            '''
            result = self._values.get("filter_type")
            assert result is not None, "Required property 'filter_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RepositoryFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ecr.CfnReplicationConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={"replication_configuration": "replicationConfiguration"},
)
class CfnReplicationConfigurationProps:
    def __init__(
        self,
        *,
        replication_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnReplicationConfiguration.ReplicationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Properties for defining a ``CfnReplicationConfiguration``.

        :param replication_configuration: The replication configuration for a registry.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-replicationconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ecr as ecr
            
            cfn_replication_configuration_props = ecr.CfnReplicationConfigurationProps(
                replication_configuration=ecr.CfnReplicationConfiguration.ReplicationConfigurationProperty(
                    rules=[ecr.CfnReplicationConfiguration.ReplicationRuleProperty(
                        destinations=[ecr.CfnReplicationConfiguration.ReplicationDestinationProperty(
                            region="region",
                            registry_id="registryId"
                        )],
            
                        # the properties below are optional
                        repository_filters=[ecr.CfnReplicationConfiguration.RepositoryFilterProperty(
                            filter="filter",
                            filter_type="filterType"
                        )]
                    )]
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d245b9cf8a9f1459a5c0b6311093064a71adab6058193aba296fc0fff15d6a8)
            check_type(argname="argument replication_configuration", value=replication_configuration, expected_type=type_hints["replication_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "replication_configuration": replication_configuration,
        }

    @builtins.property
    def replication_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnReplicationConfiguration.ReplicationConfigurationProperty]:
        '''The replication configuration for a registry.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-replicationconfiguration.html#cfn-ecr-replicationconfiguration-replicationconfiguration
        '''
        result = self._values.get("replication_configuration")
        assert result is not None, "Required property 'replication_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnReplicationConfiguration.ReplicationConfigurationProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnReplicationConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnRepository(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ecr.CfnRepository",
):
    '''The ``AWS::ECR::Repository`` resource specifies an Amazon Elastic Container Registry (Amazon ECR) repository, where users can push and pull Docker images, Open Container Initiative (OCI) images, and OCI compatible artifacts.

    For more information, see `Amazon ECR private repositories <https://docs.aws.amazon.com/AmazonECR/latest/userguide/Repositories.html>`_ in the *Amazon ECR User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html
    :cloudformationResource: AWS::ECR::Repository
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ecr as ecr
        
        # repository_policy_text: Any
        
        cfn_repository = ecr.CfnRepository(self, "MyCfnRepository",
            empty_on_delete=False,
            encryption_configuration=ecr.CfnRepository.EncryptionConfigurationProperty(
                encryption_type="encryptionType",
        
                # the properties below are optional
                kms_key="kmsKey"
            ),
            image_scanning_configuration=ecr.CfnRepository.ImageScanningConfigurationProperty(
                scan_on_push=False
            ),
            image_tag_mutability="imageTagMutability",
            lifecycle_policy=ecr.CfnRepository.LifecyclePolicyProperty(
                lifecycle_policy_text="lifecyclePolicyText",
                registry_id="registryId"
            ),
            repository_name="repositoryName",
            repository_policy_text=repository_policy_text,
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
        empty_on_delete: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRepository.EncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        image_scanning_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRepository.ImageScanningConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        image_tag_mutability: typing.Optional[builtins.str] = None,
        lifecycle_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRepository.LifecyclePolicyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        repository_name: typing.Optional[builtins.str] = None,
        repository_policy_text: typing.Any = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param empty_on_delete: If true, deleting the repository force deletes the contents of the repository. If false, the repository must be empty before attempting to delete it.
        :param encryption_configuration: The encryption configuration for the repository. This determines how the contents of your repository are encrypted at rest.
        :param image_scanning_configuration: The image scanning configuration for the repository. This determines whether images are scanned for known vulnerabilities after being pushed to the repository.
        :param image_tag_mutability: The tag mutability setting for the repository. If this parameter is omitted, the default setting of ``MUTABLE`` will be used which will allow image tags to be overwritten. If ``IMMUTABLE`` is specified, all image tags within the repository will be immutable which will prevent them from being overwritten.
        :param lifecycle_policy: Creates or updates a lifecycle policy. For information about lifecycle policy syntax, see `Lifecycle policy template <https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html>`_ .
        :param repository_name: The name to use for the repository. The repository name may be specified on its own (such as ``nginx-web-app`` ) or it can be prepended with a namespace to group the repository into a category (such as ``project-a/nginx-web-app`` ). If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the repository name. For more information, see `Name type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ . The repository name must start with a letter and can only contain lowercase letters, numbers, hyphens, underscores, and forward slashes. .. epigraph:: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.
        :param repository_policy_text: The JSON repository policy text to apply to the repository. For more information, see `Amazon ECR repository policies <https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-policy-examples.html>`_ in the *Amazon Elastic Container Registry User Guide* .
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c4027f87eb46bfdc341ea831d36476b6bcb3d7c3adf8e4193a6f82d2e5e98f4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRepositoryProps(
            empty_on_delete=empty_on_delete,
            encryption_configuration=encryption_configuration,
            image_scanning_configuration=image_scanning_configuration,
            image_tag_mutability=image_tag_mutability,
            lifecycle_policy=lifecycle_policy,
            repository_name=repository_name,
            repository_policy_text=repository_policy_text,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2248718d73b3c7bcee12085148b85f05a4c458576be92459e450678dd33ba17a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6ddcf78870d9e7c9d8fc7a3b39e380fe70edfa62cae47c7ae43d73f1d4e5f7c7)
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
        '''Returns the Amazon Resource Name (ARN) for the specified ``AWS::ECR::Repository`` resource.

        For example, ``arn:aws:ecr: *eu-west-1* : *123456789012* :repository/ *test-repository*`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrRepositoryUri")
    def attr_repository_uri(self) -> builtins.str:
        '''Returns the URI for the specified ``AWS::ECR::Repository`` resource.

        For example, ``*123456789012* .dkr.ecr. *us-west-2* .amazonaws.com/repository`` .

        :cloudformationAttribute: RepositoryUri
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRepositoryUri"))

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
    @jsii.member(jsii_name="emptyOnDelete")
    def empty_on_delete(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''If true, deleting the repository force deletes the contents of the repository.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "emptyOnDelete"))

    @empty_on_delete.setter
    def empty_on_delete(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cdf31a68d1403243dabdc584938d9cf5b1769c665a1d405daaaa8438f7d0367)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emptyOnDelete", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRepository.EncryptionConfigurationProperty"]]:
        '''The encryption configuration for the repository.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRepository.EncryptionConfigurationProperty"]], jsii.get(self, "encryptionConfiguration"))

    @encryption_configuration.setter
    def encryption_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRepository.EncryptionConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf78a5a76e0710f9d352977f8ee877ef0fc7f3c43b6cd9839d2fbeaff522caa1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="imageScanningConfiguration")
    def image_scanning_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRepository.ImageScanningConfigurationProperty"]]:
        '''The image scanning configuration for the repository.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRepository.ImageScanningConfigurationProperty"]], jsii.get(self, "imageScanningConfiguration"))

    @image_scanning_configuration.setter
    def image_scanning_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRepository.ImageScanningConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ae9439aabd4d324bf1d5bdb5b430c995fa4f0fdc0cb44daa41909d48e778564)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageScanningConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="imageTagMutability")
    def image_tag_mutability(self) -> typing.Optional[builtins.str]:
        '''The tag mutability setting for the repository.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageTagMutability"))

    @image_tag_mutability.setter
    def image_tag_mutability(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d75698f85ccefe489f53d4f155b619c9c3df1026fe201828f3f0ccc7b5fda28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageTagMutability", value)

    @builtins.property
    @jsii.member(jsii_name="lifecyclePolicy")
    def lifecycle_policy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRepository.LifecyclePolicyProperty"]]:
        '''Creates or updates a lifecycle policy.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRepository.LifecyclePolicyProperty"]], jsii.get(self, "lifecyclePolicy"))

    @lifecycle_policy.setter
    def lifecycle_policy(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRepository.LifecyclePolicyProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47418c52de9eb82b5a96dfa3524d84345309cf3a2f06fbbc30eaa7da852a33fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecyclePolicy", value)

    @builtins.property
    @jsii.member(jsii_name="repositoryName")
    def repository_name(self) -> typing.Optional[builtins.str]:
        '''The name to use for the repository.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repositoryName"))

    @repository_name.setter
    def repository_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__320e28aebae3ff1053b4006047e990e27e37c3a2753340ee0372d4f8e354bc2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repositoryName", value)

    @builtins.property
    @jsii.member(jsii_name="repositoryPolicyText")
    def repository_policy_text(self) -> typing.Any:
        '''The JSON repository policy text to apply to the repository.'''
        return typing.cast(typing.Any, jsii.get(self, "repositoryPolicyText"))

    @repository_policy_text.setter
    def repository_policy_text(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab6f8914cd6d9319d4c072a32100fe3532bf6bfdfe1b069100045f46efd7f432)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repositoryPolicyText", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a187140649b7378ce5c825b26017544130f832c6f44250242ffcc01b801ada76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ecr.CfnRepository.EncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"encryption_type": "encryptionType", "kms_key": "kmsKey"},
    )
    class EncryptionConfigurationProperty:
        def __init__(
            self,
            *,
            encryption_type: builtins.str,
            kms_key: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The encryption configuration for the repository. This determines how the contents of your repository are encrypted at rest.

            By default, when no encryption configuration is set or the ``AES256`` encryption type is used, Amazon ECR uses server-side encryption with Amazon S3-managed encryption keys which encrypts your data at rest using an AES-256 encryption algorithm. This does not require any action on your part.

            For more control over the encryption of the contents of your repository, you can use server-side encryption with AWS Key Management Service key stored in AWS Key Management Service ( AWS KMS ) to encrypt your images. For more information, see `Amazon ECR encryption at rest <https://docs.aws.amazon.com/AmazonECR/latest/userguide/encryption-at-rest.html>`_ in the *Amazon Elastic Container Registry User Guide* .

            :param encryption_type: The encryption type to use. If you use the ``KMS`` encryption type, the contents of the repository will be encrypted using server-side encryption with AWS Key Management Service key stored in AWS KMS . When you use AWS KMS to encrypt your data, you can either use the default AWS managed AWS KMS key for Amazon ECR, or specify your own AWS KMS key, which you already created. For more information, see `Protecting data using server-side encryption with an AWS KMS key stored in AWS Key Management Service (SSE-KMS) <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html>`_ in the *Amazon Simple Storage Service Console Developer Guide* . If you use the ``AES256`` encryption type, Amazon ECR uses server-side encryption with Amazon S3-managed encryption keys which encrypts the images in the repository using an AES-256 encryption algorithm. For more information, see `Protecting data using server-side encryption with Amazon S3-managed encryption keys (SSE-S3) <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html>`_ in the *Amazon Simple Storage Service Console Developer Guide* .
            :param kms_key: If you use the ``KMS`` encryption type, specify the AWS KMS key to use for encryption. The alias, key ID, or full ARN of the AWS KMS key can be specified. The key must exist in the same Region as the repository. If no key is specified, the default AWS managed AWS KMS key for Amazon ECR will be used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-encryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ecr as ecr
                
                encryption_configuration_property = ecr.CfnRepository.EncryptionConfigurationProperty(
                    encryption_type="encryptionType",
                
                    # the properties below are optional
                    kms_key="kmsKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3784a36a4911b348cdf5fe0a9dc355e52973bde3ecafee9df5e1242b07da7d08)
                check_type(argname="argument encryption_type", value=encryption_type, expected_type=type_hints["encryption_type"])
                check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "encryption_type": encryption_type,
            }
            if kms_key is not None:
                self._values["kms_key"] = kms_key

        @builtins.property
        def encryption_type(self) -> builtins.str:
            '''The encryption type to use.

            If you use the ``KMS`` encryption type, the contents of the repository will be encrypted using server-side encryption with AWS Key Management Service key stored in AWS KMS . When you use AWS KMS to encrypt your data, you can either use the default AWS managed AWS KMS key for Amazon ECR, or specify your own AWS KMS key, which you already created. For more information, see `Protecting data using server-side encryption with an AWS KMS key stored in AWS Key Management Service (SSE-KMS) <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html>`_ in the *Amazon Simple Storage Service Console Developer Guide* .

            If you use the ``AES256`` encryption type, Amazon ECR uses server-side encryption with Amazon S3-managed encryption keys which encrypts the images in the repository using an AES-256 encryption algorithm. For more information, see `Protecting data using server-side encryption with Amazon S3-managed encryption keys (SSE-S3) <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html>`_ in the *Amazon Simple Storage Service Console Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-encryptionconfiguration.html#cfn-ecr-repository-encryptionconfiguration-encryptiontype
            '''
            result = self._values.get("encryption_type")
            assert result is not None, "Required property 'encryption_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def kms_key(self) -> typing.Optional[builtins.str]:
            '''If you use the ``KMS`` encryption type, specify the AWS KMS key to use for encryption.

            The alias, key ID, or full ARN of the AWS KMS key can be specified. The key must exist in the same Region as the repository. If no key is specified, the default AWS managed AWS KMS key for Amazon ECR will be used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-encryptionconfiguration.html#cfn-ecr-repository-encryptionconfiguration-kmskey
            '''
            result = self._values.get("kms_key")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ecr.CfnRepository.ImageScanningConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"scan_on_push": "scanOnPush"},
    )
    class ImageScanningConfigurationProperty:
        def __init__(
            self,
            *,
            scan_on_push: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The image scanning configuration for a repository.

            :param scan_on_push: The setting that determines whether images are scanned after being pushed to a repository. If set to ``true`` , images will be scanned after being pushed. If this parameter is not specified, it will default to ``false`` and images will not be scanned unless a scan is manually started.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-imagescanningconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ecr as ecr
                
                image_scanning_configuration_property = ecr.CfnRepository.ImageScanningConfigurationProperty(
                    scan_on_push=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c75cd2b6ec01cb2a5879c051b4088257f2aa69c2f3db3f6435eba0c0b6fd191d)
                check_type(argname="argument scan_on_push", value=scan_on_push, expected_type=type_hints["scan_on_push"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if scan_on_push is not None:
                self._values["scan_on_push"] = scan_on_push

        @builtins.property
        def scan_on_push(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The setting that determines whether images are scanned after being pushed to a repository.

            If set to ``true`` , images will be scanned after being pushed. If this parameter is not specified, it will default to ``false`` and images will not be scanned unless a scan is manually started.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-imagescanningconfiguration.html#cfn-ecr-repository-imagescanningconfiguration-scanonpush
            '''
            result = self._values.get("scan_on_push")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ImageScanningConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ecr.CfnRepository.LifecyclePolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "lifecycle_policy_text": "lifecyclePolicyText",
            "registry_id": "registryId",
        },
    )
    class LifecyclePolicyProperty:
        def __init__(
            self,
            *,
            lifecycle_policy_text: typing.Optional[builtins.str] = None,
            registry_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``LifecyclePolicy`` property type specifies a lifecycle policy.

            For information about lifecycle policy syntax, see `Lifecycle policy template <https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html>`_ in the *Amazon ECR User Guide* .

            :param lifecycle_policy_text: The JSON repository policy text to apply to the repository.
            :param registry_id: The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-lifecyclepolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ecr as ecr
                
                lifecycle_policy_property = ecr.CfnRepository.LifecyclePolicyProperty(
                    lifecycle_policy_text="lifecyclePolicyText",
                    registry_id="registryId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e19a186a43de423097984e8a515b442413c2fa31fe895650e26f9f349987264e)
                check_type(argname="argument lifecycle_policy_text", value=lifecycle_policy_text, expected_type=type_hints["lifecycle_policy_text"])
                check_type(argname="argument registry_id", value=registry_id, expected_type=type_hints["registry_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if lifecycle_policy_text is not None:
                self._values["lifecycle_policy_text"] = lifecycle_policy_text
            if registry_id is not None:
                self._values["registry_id"] = registry_id

        @builtins.property
        def lifecycle_policy_text(self) -> typing.Optional[builtins.str]:
            '''The JSON repository policy text to apply to the repository.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-lifecyclepolicy.html#cfn-ecr-repository-lifecyclepolicy-lifecyclepolicytext
            '''
            result = self._values.get("lifecycle_policy_text")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def registry_id(self) -> typing.Optional[builtins.str]:
            '''The AWS account ID associated with the registry that contains the repository.

            If you do not specify a registry, the default registry is assumed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-lifecyclepolicy.html#cfn-ecr-repository-lifecyclepolicy-registryid
            '''
            result = self._values.get("registry_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LifecyclePolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnRepositoryCreationTemplate(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ecr.CfnRepositoryCreationTemplate",
):
    '''AWS::ECR::RepositoryCreationTemplate is used to create repository with configuration from a pre-defined template.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repositorycreationtemplate.html
    :cloudformationResource: AWS::ECR::RepositoryCreationTemplate
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ecr as ecr
        
        cfn_repository_creation_template = ecr.CfnRepositoryCreationTemplate(self, "MyCfnRepositoryCreationTemplate",
            applied_for=["appliedFor"],
            prefix="prefix",
        
            # the properties below are optional
            description="description",
            encryption_configuration=ecr.CfnRepositoryCreationTemplate.EncryptionConfigurationProperty(
                encryption_type="encryptionType",
        
                # the properties below are optional
                kms_key="kmsKey"
            ),
            image_tag_mutability="imageTagMutability",
            lifecycle_policy="lifecyclePolicy",
            repository_policy="repositoryPolicy",
            resource_tags=[CfnTag(
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
        applied_for: typing.Sequence[builtins.str],
        prefix: builtins.str,
        description: typing.Optional[builtins.str] = None,
        encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRepositoryCreationTemplate.EncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        image_tag_mutability: typing.Optional[builtins.str] = None,
        lifecycle_policy: typing.Optional[builtins.str] = None,
        repository_policy: typing.Optional[builtins.str] = None,
        resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param applied_for: A list of enumerable Strings representing the repository creation scenarios that the template will apply towards.
        :param prefix: The prefix use to match the repository name and apply the template.
        :param description: The description of the template.
        :param encryption_configuration: The encryption configuration for the repository. This determines how the contents of your repository are encrypted at rest. By default, when no encryption configuration is set or the ``AES256`` encryption type is used, Amazon ECR uses server-side encryption with Amazon S3-managed encryption keys which encrypts your data at rest using an AES-256 encryption algorithm. This does not require any action on your part. For more control over the encryption of the contents of your repository, you can use server-side encryption with AWS Key Management Service key stored in AWS Key Management Service ( AWS KMS ) to encrypt your images. For more information, see `Amazon ECR encryption at rest <https://docs.aws.amazon.com/AmazonECR/latest/userguide/encryption-at-rest.html>`_ in the *Amazon Elastic Container Registry User Guide* .
        :param image_tag_mutability: The image tag mutability setting for the repository.
        :param lifecycle_policy: The JSON lifecycle policy text to apply to the repository. For information about lifecycle policy syntax, see https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html
        :param repository_policy: The JSON repository policy text to apply to the repository. For more information, see https://docs.aws.amazon.com/AmazonECR/latest/userguide/RepositoryPolicyExamples.html
        :param resource_tags: The tags attached to the resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__494445c3594e6c48becf87b896b56289e6923275ed1be048e55a955aad19112e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRepositoryCreationTemplateProps(
            applied_for=applied_for,
            prefix=prefix,
            description=description,
            encryption_configuration=encryption_configuration,
            image_tag_mutability=image_tag_mutability,
            lifecycle_policy=lifecycle_policy,
            repository_policy=repository_policy,
            resource_tags=resource_tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de25621df06cd38b2a7712beec393825dd8540c7ddd5884bcdd2f43c88cc6a9f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d7346b42c53608f40e97cb9640d25fec5f2bfffc755ff8390a4f399e8fec8c41)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''Create timestamp of the template.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''Update timestamp of the template.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="appliedFor")
    def applied_for(self) -> typing.List[builtins.str]:
        '''A list of enumerable Strings representing the repository creation scenarios that the template will apply towards.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "appliedFor"))

    @applied_for.setter
    def applied_for(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d70128c5c73464a6960bdf3e12180f730d72102eeb954991a5ee91b6ced476e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appliedFor", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        '''The prefix use to match the repository name and apply the template.'''
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7421fb0840fe7d5bdb7ebafbc563d2498adfea23d49797835c3b7262cf06acbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the template.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5438699040b3663de96ef1aac64ac4344fe755ea3bb114b36fdb20c66eeb12e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRepositoryCreationTemplate.EncryptionConfigurationProperty"]]:
        '''The encryption configuration for the repository.

        This determines how the contents of your repository are encrypted at rest.
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRepositoryCreationTemplate.EncryptionConfigurationProperty"]], jsii.get(self, "encryptionConfiguration"))

    @encryption_configuration.setter
    def encryption_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRepositoryCreationTemplate.EncryptionConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc9a1c0060c4bcb98843249551561d40d0d01c6137b55d2fc6b20909c4d50df4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="imageTagMutability")
    def image_tag_mutability(self) -> typing.Optional[builtins.str]:
        '''The image tag mutability setting for the repository.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageTagMutability"))

    @image_tag_mutability.setter
    def image_tag_mutability(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d03ac6e7b2975934cbd1c8b2470015fc671509b1b82834732e60abe440bad58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageTagMutability", value)

    @builtins.property
    @jsii.member(jsii_name="lifecyclePolicy")
    def lifecycle_policy(self) -> typing.Optional[builtins.str]:
        '''The JSON lifecycle policy text to apply to the repository.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lifecyclePolicy"))

    @lifecycle_policy.setter
    def lifecycle_policy(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2e08b01e66ab87aacff8f76d06c2abf47c27bd4366b69a73969d43a0b0b636a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecyclePolicy", value)

    @builtins.property
    @jsii.member(jsii_name="repositoryPolicy")
    def repository_policy(self) -> typing.Optional[builtins.str]:
        '''The JSON repository policy text to apply to the repository.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repositoryPolicy"))

    @repository_policy.setter
    def repository_policy(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6133d22d20cb78fbb430ebd26935743e57cfc66d8da0d8b426c625527396018f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repositoryPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="resourceTags")
    def resource_tags(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]]:
        '''The tags attached to the resource.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]], jsii.get(self, "resourceTags"))

    @resource_tags.setter
    def resource_tags(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2fb99e1f96881ee2eeb1081388dcf7c16b80d047a366d3bbc0d4a883ac0e52b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceTags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ecr.CfnRepositoryCreationTemplate.EncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"encryption_type": "encryptionType", "kms_key": "kmsKey"},
    )
    class EncryptionConfigurationProperty:
        def __init__(
            self,
            *,
            encryption_type: builtins.str,
            kms_key: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The encryption configuration for the repository. This determines how the contents of your repository are encrypted at rest.

            By default, when no encryption configuration is set or the ``AES256`` encryption type is used, Amazon ECR uses server-side encryption with Amazon S3-managed encryption keys which encrypts your data at rest using an AES-256 encryption algorithm. This does not require any action on your part.

            For more control over the encryption of the contents of your repository, you can use server-side encryption with AWS Key Management Service key stored in AWS Key Management Service ( AWS KMS ) to encrypt your images. For more information, see `Amazon ECR encryption at rest <https://docs.aws.amazon.com/AmazonECR/latest/userguide/encryption-at-rest.html>`_ in the *Amazon Elastic Container Registry User Guide* .

            :param encryption_type: The encryption type to use. If you use the ``KMS`` encryption type, the contents of the repository will be encrypted using server-side encryption with AWS Key Management Service key stored in AWS KMS . When you use AWS KMS to encrypt your data, you can either use the default AWS managed AWS KMS key for Amazon ECR, or specify your own AWS KMS key, which you already created. For more information, see `Protecting data using server-side encryption with an AWS KMS key stored in AWS Key Management Service (SSE-KMS) <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html>`_ in the *Amazon Simple Storage Service Console Developer Guide* . If you use the ``AES256`` encryption type, Amazon ECR uses server-side encryption with Amazon S3-managed encryption keys which encrypts the images in the repository using an AES-256 encryption algorithm. For more information, see `Protecting data using server-side encryption with Amazon S3-managed encryption keys (SSE-S3) <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html>`_ in the *Amazon Simple Storage Service Console Developer Guide* .
            :param kms_key: If you use the ``KMS`` encryption type, specify the AWS KMS key to use for encryption. The alias, key ID, or full ARN of the AWS KMS key can be specified. The key must exist in the same Region as the repository. If no key is specified, the default AWS managed AWS KMS key for Amazon ECR will be used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repositorycreationtemplate-encryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ecr as ecr
                
                encryption_configuration_property = ecr.CfnRepositoryCreationTemplate.EncryptionConfigurationProperty(
                    encryption_type="encryptionType",
                
                    # the properties below are optional
                    kms_key="kmsKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0f48a77de88f0d76d55768806e65efb655f325c51435a78fe46978432e8610ec)
                check_type(argname="argument encryption_type", value=encryption_type, expected_type=type_hints["encryption_type"])
                check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "encryption_type": encryption_type,
            }
            if kms_key is not None:
                self._values["kms_key"] = kms_key

        @builtins.property
        def encryption_type(self) -> builtins.str:
            '''The encryption type to use.

            If you use the ``KMS`` encryption type, the contents of the repository will be encrypted using server-side encryption with AWS Key Management Service key stored in AWS KMS . When you use AWS KMS to encrypt your data, you can either use the default AWS managed AWS KMS key for Amazon ECR, or specify your own AWS KMS key, which you already created. For more information, see `Protecting data using server-side encryption with an AWS KMS key stored in AWS Key Management Service (SSE-KMS) <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html>`_ in the *Amazon Simple Storage Service Console Developer Guide* .

            If you use the ``AES256`` encryption type, Amazon ECR uses server-side encryption with Amazon S3-managed encryption keys which encrypts the images in the repository using an AES-256 encryption algorithm. For more information, see `Protecting data using server-side encryption with Amazon S3-managed encryption keys (SSE-S3) <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html>`_ in the *Amazon Simple Storage Service Console Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repositorycreationtemplate-encryptionconfiguration.html#cfn-ecr-repositorycreationtemplate-encryptionconfiguration-encryptiontype
            '''
            result = self._values.get("encryption_type")
            assert result is not None, "Required property 'encryption_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def kms_key(self) -> typing.Optional[builtins.str]:
            '''If you use the ``KMS`` encryption type, specify the AWS KMS key to use for encryption.

            The alias, key ID, or full ARN of the AWS KMS key can be specified. The key must exist in the same Region as the repository. If no key is specified, the default AWS managed AWS KMS key for Amazon ECR will be used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repositorycreationtemplate-encryptionconfiguration.html#cfn-ecr-repositorycreationtemplate-encryptionconfiguration-kmskey
            '''
            result = self._values.get("kms_key")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ecr.CfnRepositoryCreationTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "applied_for": "appliedFor",
        "prefix": "prefix",
        "description": "description",
        "encryption_configuration": "encryptionConfiguration",
        "image_tag_mutability": "imageTagMutability",
        "lifecycle_policy": "lifecyclePolicy",
        "repository_policy": "repositoryPolicy",
        "resource_tags": "resourceTags",
    },
)
class CfnRepositoryCreationTemplateProps:
    def __init__(
        self,
        *,
        applied_for: typing.Sequence[builtins.str],
        prefix: builtins.str,
        description: typing.Optional[builtins.str] = None,
        encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRepositoryCreationTemplate.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        image_tag_mutability: typing.Optional[builtins.str] = None,
        lifecycle_policy: typing.Optional[builtins.str] = None,
        repository_policy: typing.Optional[builtins.str] = None,
        resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRepositoryCreationTemplate``.

        :param applied_for: A list of enumerable Strings representing the repository creation scenarios that the template will apply towards.
        :param prefix: The prefix use to match the repository name and apply the template.
        :param description: The description of the template.
        :param encryption_configuration: The encryption configuration for the repository. This determines how the contents of your repository are encrypted at rest. By default, when no encryption configuration is set or the ``AES256`` encryption type is used, Amazon ECR uses server-side encryption with Amazon S3-managed encryption keys which encrypts your data at rest using an AES-256 encryption algorithm. This does not require any action on your part. For more control over the encryption of the contents of your repository, you can use server-side encryption with AWS Key Management Service key stored in AWS Key Management Service ( AWS KMS ) to encrypt your images. For more information, see `Amazon ECR encryption at rest <https://docs.aws.amazon.com/AmazonECR/latest/userguide/encryption-at-rest.html>`_ in the *Amazon Elastic Container Registry User Guide* .
        :param image_tag_mutability: The image tag mutability setting for the repository.
        :param lifecycle_policy: The JSON lifecycle policy text to apply to the repository. For information about lifecycle policy syntax, see https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html
        :param repository_policy: The JSON repository policy text to apply to the repository. For more information, see https://docs.aws.amazon.com/AmazonECR/latest/userguide/RepositoryPolicyExamples.html
        :param resource_tags: The tags attached to the resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repositorycreationtemplate.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ecr as ecr
            
            cfn_repository_creation_template_props = ecr.CfnRepositoryCreationTemplateProps(
                applied_for=["appliedFor"],
                prefix="prefix",
            
                # the properties below are optional
                description="description",
                encryption_configuration=ecr.CfnRepositoryCreationTemplate.EncryptionConfigurationProperty(
                    encryption_type="encryptionType",
            
                    # the properties below are optional
                    kms_key="kmsKey"
                ),
                image_tag_mutability="imageTagMutability",
                lifecycle_policy="lifecyclePolicy",
                repository_policy="repositoryPolicy",
                resource_tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__623a27e5bf9e58dfa2c0c25d5b312731cce32386963e30de33e3bd636fb982d3)
            check_type(argname="argument applied_for", value=applied_for, expected_type=type_hints["applied_for"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument encryption_configuration", value=encryption_configuration, expected_type=type_hints["encryption_configuration"])
            check_type(argname="argument image_tag_mutability", value=image_tag_mutability, expected_type=type_hints["image_tag_mutability"])
            check_type(argname="argument lifecycle_policy", value=lifecycle_policy, expected_type=type_hints["lifecycle_policy"])
            check_type(argname="argument repository_policy", value=repository_policy, expected_type=type_hints["repository_policy"])
            check_type(argname="argument resource_tags", value=resource_tags, expected_type=type_hints["resource_tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "applied_for": applied_for,
            "prefix": prefix,
        }
        if description is not None:
            self._values["description"] = description
        if encryption_configuration is not None:
            self._values["encryption_configuration"] = encryption_configuration
        if image_tag_mutability is not None:
            self._values["image_tag_mutability"] = image_tag_mutability
        if lifecycle_policy is not None:
            self._values["lifecycle_policy"] = lifecycle_policy
        if repository_policy is not None:
            self._values["repository_policy"] = repository_policy
        if resource_tags is not None:
            self._values["resource_tags"] = resource_tags

    @builtins.property
    def applied_for(self) -> typing.List[builtins.str]:
        '''A list of enumerable Strings representing the repository creation scenarios that the template will apply towards.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repositorycreationtemplate.html#cfn-ecr-repositorycreationtemplate-appliedfor
        '''
        result = self._values.get("applied_for")
        assert result is not None, "Required property 'applied_for' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def prefix(self) -> builtins.str:
        '''The prefix use to match the repository name and apply the template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repositorycreationtemplate.html#cfn-ecr-repositorycreationtemplate-prefix
        '''
        result = self._values.get("prefix")
        assert result is not None, "Required property 'prefix' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repositorycreationtemplate.html#cfn-ecr-repositorycreationtemplate-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRepositoryCreationTemplate.EncryptionConfigurationProperty]]:
        '''The encryption configuration for the repository. This determines how the contents of your repository are encrypted at rest.

        By default, when no encryption configuration is set or the ``AES256`` encryption type is used, Amazon ECR uses server-side encryption with Amazon S3-managed encryption keys which encrypts your data at rest using an AES-256 encryption algorithm. This does not require any action on your part.

        For more control over the encryption of the contents of your repository, you can use server-side encryption with AWS Key Management Service key stored in AWS Key Management Service ( AWS KMS ) to encrypt your images. For more information, see `Amazon ECR encryption at rest <https://docs.aws.amazon.com/AmazonECR/latest/userguide/encryption-at-rest.html>`_ in the *Amazon Elastic Container Registry User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repositorycreationtemplate.html#cfn-ecr-repositorycreationtemplate-encryptionconfiguration
        '''
        result = self._values.get("encryption_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRepositoryCreationTemplate.EncryptionConfigurationProperty]], result)

    @builtins.property
    def image_tag_mutability(self) -> typing.Optional[builtins.str]:
        '''The image tag mutability setting for the repository.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repositorycreationtemplate.html#cfn-ecr-repositorycreationtemplate-imagetagmutability
        '''
        result = self._values.get("image_tag_mutability")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lifecycle_policy(self) -> typing.Optional[builtins.str]:
        '''The JSON lifecycle policy text to apply to the repository.

        For information about lifecycle policy syntax, see https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repositorycreationtemplate.html#cfn-ecr-repositorycreationtemplate-lifecyclepolicy
        '''
        result = self._values.get("lifecycle_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def repository_policy(self) -> typing.Optional[builtins.str]:
        '''The JSON repository policy text to apply to the repository.

        For more information, see https://docs.aws.amazon.com/AmazonECR/latest/userguide/RepositoryPolicyExamples.html

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repositorycreationtemplate.html#cfn-ecr-repositorycreationtemplate-repositorypolicy
        '''
        result = self._values.get("repository_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_tags(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]]:
        '''The tags attached to the resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repositorycreationtemplate.html#cfn-ecr-repositorycreationtemplate-resourcetags
        '''
        result = self._values.get("resource_tags")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRepositoryCreationTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ecr.CfnRepositoryProps",
    jsii_struct_bases=[],
    name_mapping={
        "empty_on_delete": "emptyOnDelete",
        "encryption_configuration": "encryptionConfiguration",
        "image_scanning_configuration": "imageScanningConfiguration",
        "image_tag_mutability": "imageTagMutability",
        "lifecycle_policy": "lifecyclePolicy",
        "repository_name": "repositoryName",
        "repository_policy_text": "repositoryPolicyText",
        "tags": "tags",
    },
)
class CfnRepositoryProps:
    def __init__(
        self,
        *,
        empty_on_delete: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRepository.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        image_scanning_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRepository.ImageScanningConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        image_tag_mutability: typing.Optional[builtins.str] = None,
        lifecycle_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRepository.LifecyclePolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        repository_name: typing.Optional[builtins.str] = None,
        repository_policy_text: typing.Any = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRepository``.

        :param empty_on_delete: If true, deleting the repository force deletes the contents of the repository. If false, the repository must be empty before attempting to delete it.
        :param encryption_configuration: The encryption configuration for the repository. This determines how the contents of your repository are encrypted at rest.
        :param image_scanning_configuration: The image scanning configuration for the repository. This determines whether images are scanned for known vulnerabilities after being pushed to the repository.
        :param image_tag_mutability: The tag mutability setting for the repository. If this parameter is omitted, the default setting of ``MUTABLE`` will be used which will allow image tags to be overwritten. If ``IMMUTABLE`` is specified, all image tags within the repository will be immutable which will prevent them from being overwritten.
        :param lifecycle_policy: Creates or updates a lifecycle policy. For information about lifecycle policy syntax, see `Lifecycle policy template <https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html>`_ .
        :param repository_name: The name to use for the repository. The repository name may be specified on its own (such as ``nginx-web-app`` ) or it can be prepended with a namespace to group the repository into a category (such as ``project-a/nginx-web-app`` ). If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the repository name. For more information, see `Name type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ . The repository name must start with a letter and can only contain lowercase letters, numbers, hyphens, underscores, and forward slashes. .. epigraph:: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.
        :param repository_policy_text: The JSON repository policy text to apply to the repository. For more information, see `Amazon ECR repository policies <https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-policy-examples.html>`_ in the *Amazon Elastic Container Registry User Guide* .
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ecr as ecr
            
            # repository_policy_text: Any
            
            cfn_repository_props = ecr.CfnRepositoryProps(
                empty_on_delete=False,
                encryption_configuration=ecr.CfnRepository.EncryptionConfigurationProperty(
                    encryption_type="encryptionType",
            
                    # the properties below are optional
                    kms_key="kmsKey"
                ),
                image_scanning_configuration=ecr.CfnRepository.ImageScanningConfigurationProperty(
                    scan_on_push=False
                ),
                image_tag_mutability="imageTagMutability",
                lifecycle_policy=ecr.CfnRepository.LifecyclePolicyProperty(
                    lifecycle_policy_text="lifecyclePolicyText",
                    registry_id="registryId"
                ),
                repository_name="repositoryName",
                repository_policy_text=repository_policy_text,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6887f05f59c4e061f761607002ffdf5b7ad09f76abbf4b7be49513c3ea20ebad)
            check_type(argname="argument empty_on_delete", value=empty_on_delete, expected_type=type_hints["empty_on_delete"])
            check_type(argname="argument encryption_configuration", value=encryption_configuration, expected_type=type_hints["encryption_configuration"])
            check_type(argname="argument image_scanning_configuration", value=image_scanning_configuration, expected_type=type_hints["image_scanning_configuration"])
            check_type(argname="argument image_tag_mutability", value=image_tag_mutability, expected_type=type_hints["image_tag_mutability"])
            check_type(argname="argument lifecycle_policy", value=lifecycle_policy, expected_type=type_hints["lifecycle_policy"])
            check_type(argname="argument repository_name", value=repository_name, expected_type=type_hints["repository_name"])
            check_type(argname="argument repository_policy_text", value=repository_policy_text, expected_type=type_hints["repository_policy_text"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if empty_on_delete is not None:
            self._values["empty_on_delete"] = empty_on_delete
        if encryption_configuration is not None:
            self._values["encryption_configuration"] = encryption_configuration
        if image_scanning_configuration is not None:
            self._values["image_scanning_configuration"] = image_scanning_configuration
        if image_tag_mutability is not None:
            self._values["image_tag_mutability"] = image_tag_mutability
        if lifecycle_policy is not None:
            self._values["lifecycle_policy"] = lifecycle_policy
        if repository_name is not None:
            self._values["repository_name"] = repository_name
        if repository_policy_text is not None:
            self._values["repository_policy_text"] = repository_policy_text
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def empty_on_delete(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''If true, deleting the repository force deletes the contents of the repository.

        If false, the repository must be empty before attempting to delete it.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html#cfn-ecr-repository-emptyondelete
        '''
        result = self._values.get("empty_on_delete")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRepository.EncryptionConfigurationProperty]]:
        '''The encryption configuration for the repository.

        This determines how the contents of your repository are encrypted at rest.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html#cfn-ecr-repository-encryptionconfiguration
        '''
        result = self._values.get("encryption_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRepository.EncryptionConfigurationProperty]], result)

    @builtins.property
    def image_scanning_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRepository.ImageScanningConfigurationProperty]]:
        '''The image scanning configuration for the repository.

        This determines whether images are scanned for known vulnerabilities after being pushed to the repository.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html#cfn-ecr-repository-imagescanningconfiguration
        '''
        result = self._values.get("image_scanning_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRepository.ImageScanningConfigurationProperty]], result)

    @builtins.property
    def image_tag_mutability(self) -> typing.Optional[builtins.str]:
        '''The tag mutability setting for the repository.

        If this parameter is omitted, the default setting of ``MUTABLE`` will be used which will allow image tags to be overwritten. If ``IMMUTABLE`` is specified, all image tags within the repository will be immutable which will prevent them from being overwritten.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html#cfn-ecr-repository-imagetagmutability
        '''
        result = self._values.get("image_tag_mutability")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lifecycle_policy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRepository.LifecyclePolicyProperty]]:
        '''Creates or updates a lifecycle policy.

        For information about lifecycle policy syntax, see `Lifecycle policy template <https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html#cfn-ecr-repository-lifecyclepolicy
        '''
        result = self._values.get("lifecycle_policy")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRepository.LifecyclePolicyProperty]], result)

    @builtins.property
    def repository_name(self) -> typing.Optional[builtins.str]:
        '''The name to use for the repository.

        The repository name may be specified on its own (such as ``nginx-web-app`` ) or it can be prepended with a namespace to group the repository into a category (such as ``project-a/nginx-web-app`` ). If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the repository name. For more information, see `Name type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ .

        The repository name must start with a letter and can only contain lowercase letters, numbers, hyphens, underscores, and forward slashes.
        .. epigraph::

           If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html#cfn-ecr-repository-repositoryname
        '''
        result = self._values.get("repository_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def repository_policy_text(self) -> typing.Any:
        '''The JSON repository policy text to apply to the repository.

        For more information, see `Amazon ECR repository policies <https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-policy-examples.html>`_ in the *Amazon Elastic Container Registry User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html#cfn-ecr-repository-repositorypolicytext
        '''
        result = self._values.get("repository_policy_text")
        return typing.cast(typing.Any, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html#cfn-ecr-repository-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRepositoryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.aws_ecr.IRepository")
class IRepository(_IResource_c80c4260, typing_extensions.Protocol):
    '''Represents an ECR repository.'''

    @builtins.property
    @jsii.member(jsii_name="repositoryArn")
    def repository_arn(self) -> builtins.str:
        '''The ARN of the repository.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="repositoryName")
    def repository_name(self) -> builtins.str:
        '''The name of the repository.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="repositoryUri")
    def repository_uri(self) -> builtins.str:
        '''The URI of this repository (represents the latest image):.

        ACCOUNT.dkr.ecr.REGION.amazonaws.com/REPOSITORY

        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="addToResourcePolicy")
    def add_to_resource_policy(
        self,
        statement: _PolicyStatement_0fe33853,
    ) -> _AddToResourcePolicyResult_1d0a53ad:
        '''Add a policy statement to the repository's resource policy.

        :param statement: -
        '''
        ...

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Grant the given principal identity permissions to perform the actions on this repository.

        :param grantee: -
        :param actions: -
        '''
        ...

    @jsii.member(jsii_name="grantPull")
    def grant_pull(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the given identity permissions to pull images in this repository.

        :param grantee: -
        '''
        ...

    @jsii.member(jsii_name="grantPullPush")
    def grant_pull_push(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the given identity permissions to pull and push images to this repository.

        :param grantee: -
        '''
        ...

    @jsii.member(jsii_name="grantPush")
    def grant_push(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the given identity permissions to push images in this repository.

        :param grantee: -
        '''
        ...

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the given identity permissions to read images in this repository.

        :param grantee: -
        '''
        ...

    @jsii.member(jsii_name="onCloudTrailEvent")
    def on_cloud_trail_event(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Define a CloudWatch event that triggers when something happens to this repository.

        Requires that there exists at least one CloudTrail Trail in your account
        that captures the event. This method will not create the Trail.

        :param id: The id of the rule.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        ...

    @jsii.member(jsii_name="onCloudTrailImagePushed")
    def on_cloud_trail_image_pushed(
        self,
        id: builtins.str,
        *,
        image_tag: typing.Optional[builtins.str] = None,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines an AWS CloudWatch event rule that can trigger a target when an image is pushed to this repository.

        Requires that there exists at least one CloudTrail Trail in your account
        that captures the event. This method will not create the Trail.

        :param id: The id of the rule.
        :param image_tag: Only watch changes to this image tag. Default: - Watch changes to all tags
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        ...

    @jsii.member(jsii_name="onEvent")
    def on_event(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines a CloudWatch event rule which triggers for repository events.

        Use
        ``rule.addEventPattern(pattern)`` to specify a filter.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        ...

    @jsii.member(jsii_name="onImageScanCompleted")
    def on_image_scan_completed(
        self,
        id: builtins.str,
        *,
        image_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines an AWS CloudWatch event rule that can trigger a target when the image scan is completed.

        :param id: The id of the rule.
        :param image_tags: Only watch changes to the image tags specified. Leave it undefined to watch the full repository. Default: - Watch the changes to the repository with all image tags
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        ...

    @jsii.member(jsii_name="repositoryUriForDigest")
    def repository_uri_for_digest(
        self,
        digest: typing.Optional[builtins.str] = None,
    ) -> builtins.str:
        '''Returns the URI of the repository for a certain digest. Can be used in ``docker push/pull``.

        ACCOUNT.dkr.ecr.REGION.amazonaws.com/REPOSITORY[@DIGEST]

        :param digest: Image digest to use (tools usually default to the image with the "latest" tag if omitted).
        '''
        ...

    @jsii.member(jsii_name="repositoryUriForTag")
    def repository_uri_for_tag(
        self,
        tag: typing.Optional[builtins.str] = None,
    ) -> builtins.str:
        '''Returns the URI of the repository for a certain tag. Can be used in ``docker push/pull``.

        ACCOUNT.dkr.ecr.REGION.amazonaws.com/REPOSITORY[:TAG]

        :param tag: Image tag to use (tools usually default to "latest" if omitted).
        '''
        ...

    @jsii.member(jsii_name="repositoryUriForTagOrDigest")
    def repository_uri_for_tag_or_digest(
        self,
        tag_or_digest: typing.Optional[builtins.str] = None,
    ) -> builtins.str:
        '''Returns the URI of the repository for a certain tag or digest, inferring based on the syntax of the tag.

        Can be used in ``docker push/pull``.

        ACCOUNT.dkr.ecr.REGION.amazonaws.com/REPOSITORY[:TAG]
        ACCOUNT.dkr.ecr.REGION.amazonaws.com/REPOSITORY[@DIGEST]

        :param tag_or_digest: Image tag or digest to use (tools usually default to the image with the "latest" tag if omitted).
        '''
        ...


class _IRepositoryProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''Represents an ECR repository.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_ecr.IRepository"

    @builtins.property
    @jsii.member(jsii_name="repositoryArn")
    def repository_arn(self) -> builtins.str:
        '''The ARN of the repository.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "repositoryArn"))

    @builtins.property
    @jsii.member(jsii_name="repositoryName")
    def repository_name(self) -> builtins.str:
        '''The name of the repository.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "repositoryName"))

    @builtins.property
    @jsii.member(jsii_name="repositoryUri")
    def repository_uri(self) -> builtins.str:
        '''The URI of this repository (represents the latest image):.

        ACCOUNT.dkr.ecr.REGION.amazonaws.com/REPOSITORY

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "repositoryUri"))

    @jsii.member(jsii_name="addToResourcePolicy")
    def add_to_resource_policy(
        self,
        statement: _PolicyStatement_0fe33853,
    ) -> _AddToResourcePolicyResult_1d0a53ad:
        '''Add a policy statement to the repository's resource policy.

        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b93b76e3ed83c647651e88dbe69b68aa31811ba690fb413bbf493b24ddae92f)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(_AddToResourcePolicyResult_1d0a53ad, jsii.invoke(self, "addToResourcePolicy", [statement]))

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Grant the given principal identity permissions to perform the actions on this repository.

        :param grantee: -
        :param actions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18f0b3f711a06661adb3c2b503f084f1e6774a4c435313ce60aeb9b9c0862a78)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grant", [grantee, *actions]))

    @jsii.member(jsii_name="grantPull")
    def grant_pull(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the given identity permissions to pull images in this repository.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14c48998ec9021e98f12464e9359edb24e2b0f539ca596d1d12fb187b8364316)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantPull", [grantee]))

    @jsii.member(jsii_name="grantPullPush")
    def grant_pull_push(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the given identity permissions to pull and push images to this repository.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73c31def1a2c005caef141293abd28f7d52bc6b3cd34b9aab72ad4461456bf52)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantPullPush", [grantee]))

    @jsii.member(jsii_name="grantPush")
    def grant_push(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the given identity permissions to push images in this repository.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40780df047155d20f169a5f7d2e3cec9d737795fbd2fd65bfbfbff880a95f552)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantPush", [grantee]))

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the given identity permissions to read images in this repository.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03f9678bf6d1275cad4a69c4327c5ec4e50a698bcb71b91bc565ec5c00d17ebd)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantRead", [grantee]))

    @jsii.member(jsii_name="onCloudTrailEvent")
    def on_cloud_trail_event(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Define a CloudWatch event that triggers when something happens to this repository.

        Requires that there exists at least one CloudTrail Trail in your account
        that captures the event. This method will not create the Trail.

        :param id: The id of the rule.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__581481b04818144d35c370c8364691c22c75abf889fbbde93425ef00df6eb66a)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _OnEventOptions_8711b8b3(
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onCloudTrailEvent", [id, options]))

    @jsii.member(jsii_name="onCloudTrailImagePushed")
    def on_cloud_trail_image_pushed(
        self,
        id: builtins.str,
        *,
        image_tag: typing.Optional[builtins.str] = None,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines an AWS CloudWatch event rule that can trigger a target when an image is pushed to this repository.

        Requires that there exists at least one CloudTrail Trail in your account
        that captures the event. This method will not create the Trail.

        :param id: The id of the rule.
        :param image_tag: Only watch changes to this image tag. Default: - Watch changes to all tags
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6682a5de5f017cf245f225ab2ffa20f3d976bd0d01ff908575d68289ea5cb92e)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = OnCloudTrailImagePushedOptions(
            image_tag=image_tag,
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onCloudTrailImagePushed", [id, options]))

    @jsii.member(jsii_name="onEvent")
    def on_event(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines a CloudWatch event rule which triggers for repository events.

        Use
        ``rule.addEventPattern(pattern)`` to specify a filter.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05e48b88e3cb8ff8071e5137a10ebf822f9a67fee50365cc9ad50d0e5ef048be)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _OnEventOptions_8711b8b3(
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onEvent", [id, options]))

    @jsii.member(jsii_name="onImageScanCompleted")
    def on_image_scan_completed(
        self,
        id: builtins.str,
        *,
        image_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines an AWS CloudWatch event rule that can trigger a target when the image scan is completed.

        :param id: The id of the rule.
        :param image_tags: Only watch changes to the image tags specified. Leave it undefined to watch the full repository. Default: - Watch the changes to the repository with all image tags
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e891aed9e9c072461bf707e41c6a0f85f0bf27b1d49dd72a2380d2f74650b37)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = OnImageScanCompletedOptions(
            image_tags=image_tags,
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onImageScanCompleted", [id, options]))

    @jsii.member(jsii_name="repositoryUriForDigest")
    def repository_uri_for_digest(
        self,
        digest: typing.Optional[builtins.str] = None,
    ) -> builtins.str:
        '''Returns the URI of the repository for a certain digest. Can be used in ``docker push/pull``.

        ACCOUNT.dkr.ecr.REGION.amazonaws.com/REPOSITORY[@DIGEST]

        :param digest: Image digest to use (tools usually default to the image with the "latest" tag if omitted).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6efec5eaaaff5e5a00be5c12bb1466927bb81353f89902e1dd5c4af405620db8)
            check_type(argname="argument digest", value=digest, expected_type=type_hints["digest"])
        return typing.cast(builtins.str, jsii.invoke(self, "repositoryUriForDigest", [digest]))

    @jsii.member(jsii_name="repositoryUriForTag")
    def repository_uri_for_tag(
        self,
        tag: typing.Optional[builtins.str] = None,
    ) -> builtins.str:
        '''Returns the URI of the repository for a certain tag. Can be used in ``docker push/pull``.

        ACCOUNT.dkr.ecr.REGION.amazonaws.com/REPOSITORY[:TAG]

        :param tag: Image tag to use (tools usually default to "latest" if omitted).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43ac1e08a24281d72c0ed626aa4a3d8becdaeb21dc0117029ed9cb5e93568fb5)
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
        return typing.cast(builtins.str, jsii.invoke(self, "repositoryUriForTag", [tag]))

    @jsii.member(jsii_name="repositoryUriForTagOrDigest")
    def repository_uri_for_tag_or_digest(
        self,
        tag_or_digest: typing.Optional[builtins.str] = None,
    ) -> builtins.str:
        '''Returns the URI of the repository for a certain tag or digest, inferring based on the syntax of the tag.

        Can be used in ``docker push/pull``.

        ACCOUNT.dkr.ecr.REGION.amazonaws.com/REPOSITORY[:TAG]
        ACCOUNT.dkr.ecr.REGION.amazonaws.com/REPOSITORY[@DIGEST]

        :param tag_or_digest: Image tag or digest to use (tools usually default to the image with the "latest" tag if omitted).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__894e1dc0284d8788d4bcf980d7755525e14fbcec8b305670af1a388f39980974)
            check_type(argname="argument tag_or_digest", value=tag_or_digest, expected_type=type_hints["tag_or_digest"])
        return typing.cast(builtins.str, jsii.invoke(self, "repositoryUriForTagOrDigest", [tag_or_digest]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRepository).__jsii_proxy_class__ = lambda : _IRepositoryProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ecr.LifecycleRule",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "max_image_age": "maxImageAge",
        "max_image_count": "maxImageCount",
        "rule_priority": "rulePriority",
        "tag_pattern_list": "tagPatternList",
        "tag_prefix_list": "tagPrefixList",
        "tag_status": "tagStatus",
    },
)
class LifecycleRule:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        max_image_age: typing.Optional[_Duration_4839e8c3] = None,
        max_image_count: typing.Optional[jsii.Number] = None,
        rule_priority: typing.Optional[jsii.Number] = None,
        tag_pattern_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        tag_prefix_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        tag_status: typing.Optional["TagStatus"] = None,
    ) -> None:
        '''An ECR life cycle rule.

        :param description: Describes the purpose of the rule. Default: No description
        :param max_image_age: The maximum age of images to retain. The value must represent a number of days. Specify exactly one of maxImageCount and maxImageAge.
        :param max_image_count: The maximum number of images to retain. Specify exactly one of maxImageCount and maxImageAge.
        :param rule_priority: Controls the order in which rules are evaluated (low to high). All rules must have a unique priority, where lower numbers have higher precedence. The first rule that matches is applied to an image. There can only be one rule with a tagStatus of Any, and it must have the highest rulePriority. All rules without a specified priority will have incrementing priorities automatically assigned to them, higher than any rules that DO have priorities. Default: Automatically assigned
        :param tag_pattern_list: Select images that have ALL the given patterns in their tag. There is a maximum limit of four wildcards (*) per string. For example, ["*test*1*2*3", "test*1*2*3*"] is valid but ["test*1*2*3*4*5*6"] is invalid. Both tagPrefixList and tagPatternList cannot be specified together in a rule. Only if tagStatus == TagStatus.Tagged
        :param tag_prefix_list: Select images that have ALL the given prefixes in their tag. Both tagPrefixList and tagPatternList cannot be specified together in a rule. Only if tagStatus == TagStatus.Tagged
        :param tag_status: Select images based on tags. Only one rule is allowed to select untagged images, and it must have the highest rulePriority. Default: TagStatus.Tagged if tagPrefixList or tagPatternList is given, TagStatus.Any otherwise

        :exampleMetadata: infused

        Example::

            # repository: ecr.Repository
            
            repository.add_lifecycle_rule(tag_prefix_list=["prod"], max_image_count=9999)
            repository.add_lifecycle_rule(max_image_age=Duration.days(30))
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__daefc01ac58c056180e96357fa989faf5de713c6f5bd46bb023e2579bcaf8de0)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument max_image_age", value=max_image_age, expected_type=type_hints["max_image_age"])
            check_type(argname="argument max_image_count", value=max_image_count, expected_type=type_hints["max_image_count"])
            check_type(argname="argument rule_priority", value=rule_priority, expected_type=type_hints["rule_priority"])
            check_type(argname="argument tag_pattern_list", value=tag_pattern_list, expected_type=type_hints["tag_pattern_list"])
            check_type(argname="argument tag_prefix_list", value=tag_prefix_list, expected_type=type_hints["tag_prefix_list"])
            check_type(argname="argument tag_status", value=tag_status, expected_type=type_hints["tag_status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if max_image_age is not None:
            self._values["max_image_age"] = max_image_age
        if max_image_count is not None:
            self._values["max_image_count"] = max_image_count
        if rule_priority is not None:
            self._values["rule_priority"] = rule_priority
        if tag_pattern_list is not None:
            self._values["tag_pattern_list"] = tag_pattern_list
        if tag_prefix_list is not None:
            self._values["tag_prefix_list"] = tag_prefix_list
        if tag_status is not None:
            self._values["tag_status"] = tag_status

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Describes the purpose of the rule.

        :default: No description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_image_age(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The maximum age of images to retain. The value must represent a number of days.

        Specify exactly one of maxImageCount and maxImageAge.
        '''
        result = self._values.get("max_image_age")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def max_image_count(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of images to retain.

        Specify exactly one of maxImageCount and maxImageAge.
        '''
        result = self._values.get("max_image_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def rule_priority(self) -> typing.Optional[jsii.Number]:
        '''Controls the order in which rules are evaluated (low to high).

        All rules must have a unique priority, where lower numbers have
        higher precedence. The first rule that matches is applied to an image.

        There can only be one rule with a tagStatus of Any, and it must have
        the highest rulePriority.

        All rules without a specified priority will have incrementing priorities
        automatically assigned to them, higher than any rules that DO have priorities.

        :default: Automatically assigned
        '''
        result = self._values.get("rule_priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tag_pattern_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Select images that have ALL the given patterns in their tag.

        There is a maximum limit of four wildcards (*) per string.
        For example, ["*test*1*2*3", "test*1*2*3*"] is valid but
        ["test*1*2*3*4*5*6"] is invalid.

        Both tagPrefixList and tagPatternList cannot be specified
        together in a rule.

        Only if tagStatus == TagStatus.Tagged
        '''
        result = self._values.get("tag_pattern_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tag_prefix_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Select images that have ALL the given prefixes in their tag.

        Both tagPrefixList and tagPatternList cannot be specified
        together in a rule.

        Only if tagStatus == TagStatus.Tagged
        '''
        result = self._values.get("tag_prefix_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tag_status(self) -> typing.Optional["TagStatus"]:
        '''Select images based on tags.

        Only one rule is allowed to select untagged images, and it must
        have the highest rulePriority.

        :default:

        TagStatus.Tagged if tagPrefixList or tagPatternList is
        given, TagStatus.Any otherwise
        '''
        result = self._values.get("tag_status")
        return typing.cast(typing.Optional["TagStatus"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LifecycleRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ecr.OnCloudTrailImagePushedOptions",
    jsii_struct_bases=[_OnEventOptions_8711b8b3],
    name_mapping={
        "cross_stack_scope": "crossStackScope",
        "description": "description",
        "event_pattern": "eventPattern",
        "rule_name": "ruleName",
        "target": "target",
        "image_tag": "imageTag",
    },
)
class OnCloudTrailImagePushedOptions(_OnEventOptions_8711b8b3):
    def __init__(
        self,
        *,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        image_tag: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Options for the onCloudTrailImagePushed method.

        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param image_tag: Only watch changes to this image tag. Default: - Watch changes to all tags

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ecr as ecr
            from aws_cdk import aws_events as events
            import constructs as constructs
            
            # construct: constructs.Construct
            # detail: Any
            # rule_target: events.IRuleTarget
            
            on_cloud_trail_image_pushed_options = ecr.OnCloudTrailImagePushedOptions(
                cross_stack_scope=construct,
                description="description",
                event_pattern=events.EventPattern(
                    account=["account"],
                    detail={
                        "detail_key": detail
                    },
                    detail_type=["detailType"],
                    id=["id"],
                    region=["region"],
                    resources=["resources"],
                    source=["source"],
                    time=["time"],
                    version=["version"]
                ),
                image_tag="imageTag",
                rule_name="ruleName",
                target=rule_target
            )
        '''
        if isinstance(event_pattern, dict):
            event_pattern = _EventPattern_fe557901(**event_pattern)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29ce751d750234300d3a95f38312d7cd333a8c93f40235199d6b35a3379922d7)
            check_type(argname="argument cross_stack_scope", value=cross_stack_scope, expected_type=type_hints["cross_stack_scope"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument event_pattern", value=event_pattern, expected_type=type_hints["event_pattern"])
            check_type(argname="argument rule_name", value=rule_name, expected_type=type_hints["rule_name"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument image_tag", value=image_tag, expected_type=type_hints["image_tag"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cross_stack_scope is not None:
            self._values["cross_stack_scope"] = cross_stack_scope
        if description is not None:
            self._values["description"] = description
        if event_pattern is not None:
            self._values["event_pattern"] = event_pattern
        if rule_name is not None:
            self._values["rule_name"] = rule_name
        if target is not None:
            self._values["target"] = target
        if image_tag is not None:
            self._values["image_tag"] = image_tag

    @builtins.property
    def cross_stack_scope(self) -> typing.Optional[_constructs_77d1e7e8.Construct]:
        '''The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region).

        This helps dealing with cycles that often arise in these situations.

        :default: - none (the main scope will be used, even for cross-stack Events)
        '''
        result = self._values.get("cross_stack_scope")
        return typing.cast(typing.Optional[_constructs_77d1e7e8.Construct], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the rule's purpose.

        :default: - No description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def event_pattern(self) -> typing.Optional[_EventPattern_fe557901]:
        '''Additional restrictions for the event to route to the specified target.

        The method that generates the rule probably imposes some type of event
        filtering. The filtering implied by what you pass here is added
        on top of that filtering.

        :default: - No additional filtering based on an event pattern.

        :see: https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html
        '''
        result = self._values.get("event_pattern")
        return typing.cast(typing.Optional[_EventPattern_fe557901], result)

    @builtins.property
    def rule_name(self) -> typing.Optional[builtins.str]:
        '''A name for the rule.

        :default: AWS CloudFormation generates a unique physical ID.
        '''
        result = self._values.get("rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target(self) -> typing.Optional[_IRuleTarget_7a91f454]:
        '''The target to register for the event.

        :default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional[_IRuleTarget_7a91f454], result)

    @builtins.property
    def image_tag(self) -> typing.Optional[builtins.str]:
        '''Only watch changes to this image tag.

        :default: - Watch changes to all tags
        '''
        result = self._values.get("image_tag")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OnCloudTrailImagePushedOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ecr.OnImageScanCompletedOptions",
    jsii_struct_bases=[_OnEventOptions_8711b8b3],
    name_mapping={
        "cross_stack_scope": "crossStackScope",
        "description": "description",
        "event_pattern": "eventPattern",
        "rule_name": "ruleName",
        "target": "target",
        "image_tags": "imageTags",
    },
)
class OnImageScanCompletedOptions(_OnEventOptions_8711b8b3):
    def __init__(
        self,
        *,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        image_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Options for the OnImageScanCompleted method.

        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param image_tags: Only watch changes to the image tags specified. Leave it undefined to watch the full repository. Default: - Watch the changes to the repository with all image tags

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ecr as ecr
            from aws_cdk import aws_events as events
            import constructs as constructs
            
            # construct: constructs.Construct
            # detail: Any
            # rule_target: events.IRuleTarget
            
            on_image_scan_completed_options = ecr.OnImageScanCompletedOptions(
                cross_stack_scope=construct,
                description="description",
                event_pattern=events.EventPattern(
                    account=["account"],
                    detail={
                        "detail_key": detail
                    },
                    detail_type=["detailType"],
                    id=["id"],
                    region=["region"],
                    resources=["resources"],
                    source=["source"],
                    time=["time"],
                    version=["version"]
                ),
                image_tags=["imageTags"],
                rule_name="ruleName",
                target=rule_target
            )
        '''
        if isinstance(event_pattern, dict):
            event_pattern = _EventPattern_fe557901(**event_pattern)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7008a301b5d27c21d26fff448212766f7f8c0067ab03fc3eb8bb5bd100c32277)
            check_type(argname="argument cross_stack_scope", value=cross_stack_scope, expected_type=type_hints["cross_stack_scope"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument event_pattern", value=event_pattern, expected_type=type_hints["event_pattern"])
            check_type(argname="argument rule_name", value=rule_name, expected_type=type_hints["rule_name"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument image_tags", value=image_tags, expected_type=type_hints["image_tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cross_stack_scope is not None:
            self._values["cross_stack_scope"] = cross_stack_scope
        if description is not None:
            self._values["description"] = description
        if event_pattern is not None:
            self._values["event_pattern"] = event_pattern
        if rule_name is not None:
            self._values["rule_name"] = rule_name
        if target is not None:
            self._values["target"] = target
        if image_tags is not None:
            self._values["image_tags"] = image_tags

    @builtins.property
    def cross_stack_scope(self) -> typing.Optional[_constructs_77d1e7e8.Construct]:
        '''The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region).

        This helps dealing with cycles that often arise in these situations.

        :default: - none (the main scope will be used, even for cross-stack Events)
        '''
        result = self._values.get("cross_stack_scope")
        return typing.cast(typing.Optional[_constructs_77d1e7e8.Construct], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the rule's purpose.

        :default: - No description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def event_pattern(self) -> typing.Optional[_EventPattern_fe557901]:
        '''Additional restrictions for the event to route to the specified target.

        The method that generates the rule probably imposes some type of event
        filtering. The filtering implied by what you pass here is added
        on top of that filtering.

        :default: - No additional filtering based on an event pattern.

        :see: https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html
        '''
        result = self._values.get("event_pattern")
        return typing.cast(typing.Optional[_EventPattern_fe557901], result)

    @builtins.property
    def rule_name(self) -> typing.Optional[builtins.str]:
        '''A name for the rule.

        :default: AWS CloudFormation generates a unique physical ID.
        '''
        result = self._values.get("rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target(self) -> typing.Optional[_IRuleTarget_7a91f454]:
        '''The target to register for the event.

        :default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional[_IRuleTarget_7a91f454], result)

    @builtins.property
    def image_tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Only watch changes to the image tags specified.

        Leave it undefined to watch the full repository.

        :default: - Watch the changes to the repository with all image tags
        '''
        result = self._values.get("image_tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OnImageScanCompletedOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PublicGalleryAuthorizationToken(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ecr.PublicGalleryAuthorizationToken",
):
    '''Authorization token to access the global public ECR Gallery via Docker CLI.

    :see: https://docs.aws.amazon.com/AmazonECR/latest/public/public-registries.html#public-registry-auth
    :exampleMetadata: infused

    Example::

        user = iam.User(self, "User")
        ecr.PublicGalleryAuthorizationToken.grant_read(user)
    '''

    @jsii.member(jsii_name="grantRead")
    @builtins.classmethod
    def grant_read(cls, grantee: _IGrantable_71c4f5de) -> None:
        '''Grant access to retrieve an authorization token.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fd77e7b53fca07660d5412cd9d20f56fac4fdb4d2e19b7941335059053bf70c)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(None, jsii.sinvoke(cls, "grantRead", [grantee]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ecr.RepositoryAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "repository_arn": "repositoryArn",
        "repository_name": "repositoryName",
    },
)
class RepositoryAttributes:
    def __init__(
        self,
        *,
        repository_arn: builtins.str,
        repository_name: builtins.str,
    ) -> None:
        '''
        :param repository_arn: 
        :param repository_name: 

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ecr as ecr
            
            repository_attributes = ecr.RepositoryAttributes(
                repository_arn="repositoryArn",
                repository_name="repositoryName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e7e79b01d862fd1beb9d23e3ac604e86944e354ddaa5cefb7cead2845a54dc6)
            check_type(argname="argument repository_arn", value=repository_arn, expected_type=type_hints["repository_arn"])
            check_type(argname="argument repository_name", value=repository_name, expected_type=type_hints["repository_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "repository_arn": repository_arn,
            "repository_name": repository_name,
        }

    @builtins.property
    def repository_arn(self) -> builtins.str:
        result = self._values.get("repository_arn")
        assert result is not None, "Required property 'repository_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repository_name(self) -> builtins.str:
        result = self._values.get("repository_name")
        assert result is not None, "Required property 'repository_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RepositoryAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IRepository)
class RepositoryBase(
    _Resource_45bc6135,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_ecr.RepositoryBase",
):
    '''Base class for ECR repository.

    Reused between imported repositories and owned repositories.
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        environment_from_arn: typing.Optional[builtins.str] = None,
        physical_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param account: The AWS account ID this resource belongs to. Default: - the resource is in the same account as the stack it belongs to
        :param environment_from_arn: ARN to deduce region and account from. The ARN is parsed and the account and region are taken from the ARN. This should be used for imported resources. Cannot be supplied together with either ``account`` or ``region``. Default: - take environment from ``account``, ``region`` parameters, or use Stack environment.
        :param physical_name: The value passed in by users to the physical name prop of the resource. - ``undefined`` implies that a physical name will be allocated by CloudFormation during deployment. - a concrete value implies a specific physical name - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation. Default: - The physical name will be allocated by CloudFormation at deployment time
        :param region: The AWS region this resource belongs to. Default: - the resource is in the same region as the stack it belongs to
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a38c5ca8c70073b00eab7631b4fe1e84b9d8307578ae544e69bb8e01e082e536)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = _ResourceProps_15a65b4e(
            account=account,
            environment_from_arn=environment_from_arn,
            physical_name=physical_name,
            region=region,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addToResourcePolicy")
    @abc.abstractmethod
    def add_to_resource_policy(
        self,
        statement: _PolicyStatement_0fe33853,
    ) -> _AddToResourcePolicyResult_1d0a53ad:
        '''Add a policy statement to the repository's resource policy.

        :param statement: -
        '''
        ...

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Grant the given principal identity permissions to perform the actions on this repository.

        :param grantee: -
        :param actions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0332d345aba5679afe9fb0b7ab696008671005f2f0d37df9b84a4e6c8e76114a)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grant", [grantee, *actions]))

    @jsii.member(jsii_name="grantPull")
    def grant_pull(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the given identity permissions to use the images in this repository.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a73c5a3d57036dda31cb310868d740db73df050bd928d1f98a2aa6dc7f8f8195)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantPull", [grantee]))

    @jsii.member(jsii_name="grantPullPush")
    def grant_pull_push(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the given identity permissions to pull and push images to this repository.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee46b08a597ed3ce199cf26924cf11ab5fabd9d17bedcc7efc476d1d1c700e2c)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantPullPush", [grantee]))

    @jsii.member(jsii_name="grantPush")
    def grant_push(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the given identity permissions to use the images in this repository.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b0273082d293ef1f0dde5de95fd611df83c06e41660b7409f297f562363e104)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantPush", [grantee]))

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the given identity permissions to read the images in this repository.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31a099ab10f2924b872f9278330820dffe9b52373bfaa3e8885d4ff563eac580)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantRead", [grantee]))

    @jsii.member(jsii_name="onCloudTrailEvent")
    def on_cloud_trail_event(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Define a CloudWatch event that triggers when something happens to this repository.

        Requires that there exists at least one CloudTrail Trail in your account
        that captures the event. This method will not create the Trail.

        :param id: The id of the rule.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c139a9b31fe3e7f708003b6e9681fb4646f332fdded0d9490a28ed070894122)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _OnEventOptions_8711b8b3(
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onCloudTrailEvent", [id, options]))

    @jsii.member(jsii_name="onCloudTrailImagePushed")
    def on_cloud_trail_image_pushed(
        self,
        id: builtins.str,
        *,
        image_tag: typing.Optional[builtins.str] = None,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines an AWS CloudWatch event rule that can trigger a target when an image is pushed to this repository.

        Requires that there exists at least one CloudTrail Trail in your account
        that captures the event. This method will not create the Trail.

        :param id: The id of the rule.
        :param image_tag: Only watch changes to this image tag. Default: - Watch changes to all tags
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0d2ebb124849d81a392bd26c0bce7b3b3cf10151d71b5907fb7bd4fafbff603)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = OnCloudTrailImagePushedOptions(
            image_tag=image_tag,
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onCloudTrailImagePushed", [id, options]))

    @jsii.member(jsii_name="onEvent")
    def on_event(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines a CloudWatch event rule which triggers for repository events.

        Use
        ``rule.addEventPattern(pattern)`` to specify a filter.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51f97041baa3939cfb2ce34fc3fa53b516f3c6e0c4aa588c04f69ec9c7f5c4c2)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _OnEventOptions_8711b8b3(
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onEvent", [id, options]))

    @jsii.member(jsii_name="onImageScanCompleted")
    def on_image_scan_completed(
        self,
        id: builtins.str,
        *,
        image_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines an AWS CloudWatch event rule that can trigger a target when an image scan is completed.

        :param id: The id of the rule.
        :param image_tags: Only watch changes to the image tags specified. Leave it undefined to watch the full repository. Default: - Watch the changes to the repository with all image tags
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60f3c389878e84cfc27eacd079e1260fe1c75a68121b98730f3af9e704635af9)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = OnImageScanCompletedOptions(
            image_tags=image_tags,
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onImageScanCompleted", [id, options]))

    @jsii.member(jsii_name="repositoryUriForDigest")
    def repository_uri_for_digest(
        self,
        digest: typing.Optional[builtins.str] = None,
    ) -> builtins.str:
        '''Returns the URL of the repository. Can be used in ``docker push/pull``.

        ACCOUNT.dkr.ecr.REGION.amazonaws.com/REPOSITORY[@DIGEST]

        :param digest: Optional image digest.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1cd01de98d564bf59abc17d6fde8add4f2d946d00d87164b7209d02c893dfee)
            check_type(argname="argument digest", value=digest, expected_type=type_hints["digest"])
        return typing.cast(builtins.str, jsii.invoke(self, "repositoryUriForDigest", [digest]))

    @jsii.member(jsii_name="repositoryUriForTag")
    def repository_uri_for_tag(
        self,
        tag: typing.Optional[builtins.str] = None,
    ) -> builtins.str:
        '''Returns the URL of the repository. Can be used in ``docker push/pull``.

        ACCOUNT.dkr.ecr.REGION.amazonaws.com/REPOSITORY[:TAG]

        :param tag: Optional image tag.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9de3aee1b153dc478086c6f0e5f5e48cb31aaaa05063a0617ec682978677806)
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
        return typing.cast(builtins.str, jsii.invoke(self, "repositoryUriForTag", [tag]))

    @jsii.member(jsii_name="repositoryUriForTagOrDigest")
    def repository_uri_for_tag_or_digest(
        self,
        tag_or_digest: typing.Optional[builtins.str] = None,
    ) -> builtins.str:
        '''Returns the URL of the repository. Can be used in ``docker push/pull``.

        ACCOUNT.dkr.ecr.REGION.amazonaws.com/REPOSITORY[:TAG]
        ACCOUNT.dkr.ecr.REGION.amazonaws.com/REPOSITORY[@DIGEST]

        :param tag_or_digest: Optional image tag or digest (digests must start with ``sha256:``).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__737ee8e7775488279e9f1051f87dc9b1d6c752b8154e3381c9b62a3cc696f8d2)
            check_type(argname="argument tag_or_digest", value=tag_or_digest, expected_type=type_hints["tag_or_digest"])
        return typing.cast(builtins.str, jsii.invoke(self, "repositoryUriForTagOrDigest", [tag_or_digest]))

    @builtins.property
    @jsii.member(jsii_name="repositoryArn")
    @abc.abstractmethod
    def repository_arn(self) -> builtins.str:
        '''The ARN of the repository.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="repositoryName")
    @abc.abstractmethod
    def repository_name(self) -> builtins.str:
        '''The name of the repository.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="repositoryUri")
    def repository_uri(self) -> builtins.str:
        '''The URI of this repository (represents the latest image):.

        ACCOUNT.dkr.ecr.REGION.amazonaws.com/REPOSITORY
        '''
        return typing.cast(builtins.str, jsii.get(self, "repositoryUri"))


class _RepositoryBaseProxy(
    RepositoryBase,
    jsii.proxy_for(_Resource_45bc6135), # type: ignore[misc]
):
    @jsii.member(jsii_name="addToResourcePolicy")
    def add_to_resource_policy(
        self,
        statement: _PolicyStatement_0fe33853,
    ) -> _AddToResourcePolicyResult_1d0a53ad:
        '''Add a policy statement to the repository's resource policy.

        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6698dcafdf5c8416d9634135d68ec261fb74e16ec8e5fa780d78a8a8fa822ee6)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(_AddToResourcePolicyResult_1d0a53ad, jsii.invoke(self, "addToResourcePolicy", [statement]))

    @builtins.property
    @jsii.member(jsii_name="repositoryArn")
    def repository_arn(self) -> builtins.str:
        '''The ARN of the repository.'''
        return typing.cast(builtins.str, jsii.get(self, "repositoryArn"))

    @builtins.property
    @jsii.member(jsii_name="repositoryName")
    def repository_name(self) -> builtins.str:
        '''The name of the repository.'''
        return typing.cast(builtins.str, jsii.get(self, "repositoryName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, RepositoryBase).__jsii_proxy_class__ = lambda : _RepositoryBaseProxy


class RepositoryEncryption(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ecr.RepositoryEncryption",
):
    '''Indicates whether server-side encryption is enabled for the object, and whether that encryption is from the AWS Key Management Service (AWS KMS) or from Amazon S3 managed encryption (SSE-S3).

    :see: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#SysMetadata
    :exampleMetadata: infused

    Example::

        ecr.Repository(self, "Repo",
            encryption=ecr.RepositoryEncryption.KMS
        )
    '''

    def __init__(self, value: builtins.str) -> None:
        '''
        :param value: the string value of the encryption.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__144b557444508fc0a954f4a654cd03105778da2972bab34f799be4e543750902)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.create(self.__class__, self, [value])

    @jsii.python.classproperty
    @jsii.member(jsii_name="AES_256")
    def AES_256(cls) -> "RepositoryEncryption":
        ''''AES256'.'''
        return typing.cast("RepositoryEncryption", jsii.sget(cls, "AES_256"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="KMS")
    def KMS(cls) -> "RepositoryEncryption":
        ''''KMS'.'''
        return typing.cast("RepositoryEncryption", jsii.sget(cls, "KMS"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        '''the string value of the encryption.'''
        return typing.cast(builtins.str, jsii.get(self, "value"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ecr.RepositoryProps",
    jsii_struct_bases=[],
    name_mapping={
        "auto_delete_images": "autoDeleteImages",
        "empty_on_delete": "emptyOnDelete",
        "encryption": "encryption",
        "encryption_key": "encryptionKey",
        "image_scan_on_push": "imageScanOnPush",
        "image_tag_mutability": "imageTagMutability",
        "lifecycle_registry_id": "lifecycleRegistryId",
        "lifecycle_rules": "lifecycleRules",
        "removal_policy": "removalPolicy",
        "repository_name": "repositoryName",
    },
)
class RepositoryProps:
    def __init__(
        self,
        *,
        auto_delete_images: typing.Optional[builtins.bool] = None,
        empty_on_delete: typing.Optional[builtins.bool] = None,
        encryption: typing.Optional[RepositoryEncryption] = None,
        encryption_key: typing.Optional[_IKey_5f11635f] = None,
        image_scan_on_push: typing.Optional[builtins.bool] = None,
        image_tag_mutability: typing.Optional["TagMutability"] = None,
        lifecycle_registry_id: typing.Optional[builtins.str] = None,
        lifecycle_rules: typing.Optional[typing.Sequence[typing.Union[LifecycleRule, typing.Dict[builtins.str, typing.Any]]]] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
        repository_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auto_delete_images: (deprecated) Whether all images should be automatically deleted when the repository is removed from the stack or when the stack is deleted. Requires the ``removalPolicy`` to be set to ``RemovalPolicy.DESTROY``. Default: false
        :param empty_on_delete: If true, deleting the repository force deletes the contents of the repository. If false, the repository must be empty before attempting to delete it. Default: false
        :param encryption: The kind of server-side encryption to apply to this repository. If you choose KMS, you can specify a KMS key via ``encryptionKey``. If encryptionKey is not specified, an AWS managed KMS key is used. Default: - ``KMS`` if ``encryptionKey`` is specified, or ``AES256`` otherwise.
        :param encryption_key: External KMS key to use for repository encryption. The 'encryption' property must be either not specified or set to "KMS". An error will be emitted if encryption is set to "AES256". Default: - If encryption is set to ``KMS`` and this property is undefined, an AWS managed KMS key is used.
        :param image_scan_on_push: Enable the scan on push when creating the repository. Default: false
        :param image_tag_mutability: The tag mutability setting for the repository. If this parameter is omitted, the default setting of MUTABLE will be used which will allow image tags to be overwritten. Default: TagMutability.MUTABLE
        :param lifecycle_registry_id: The AWS account ID associated with the registry that contains the repository. Default: The default registry is assumed.
        :param lifecycle_rules: Life cycle rules to apply to this registry. Default: No life cycle rules
        :param removal_policy: Determine what happens to the repository when the resource/stack is deleted. Default: RemovalPolicy.Retain
        :param repository_name: Name for this repository. The repository name must start with a letter and can only contain lowercase letters, numbers, hyphens, underscores, and forward slashes. .. epigraph:: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name. Default: Automatically generated name.

        :exampleMetadata: infused

        Example::

            ecr.Repository(self, "Repo", image_tag_mutability=ecr.TagMutability.IMMUTABLE)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__638b63dd5eb589e01019ee47c63d6335810d02b0d769f767f2bf2fddc285af28)
            check_type(argname="argument auto_delete_images", value=auto_delete_images, expected_type=type_hints["auto_delete_images"])
            check_type(argname="argument empty_on_delete", value=empty_on_delete, expected_type=type_hints["empty_on_delete"])
            check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
            check_type(argname="argument encryption_key", value=encryption_key, expected_type=type_hints["encryption_key"])
            check_type(argname="argument image_scan_on_push", value=image_scan_on_push, expected_type=type_hints["image_scan_on_push"])
            check_type(argname="argument image_tag_mutability", value=image_tag_mutability, expected_type=type_hints["image_tag_mutability"])
            check_type(argname="argument lifecycle_registry_id", value=lifecycle_registry_id, expected_type=type_hints["lifecycle_registry_id"])
            check_type(argname="argument lifecycle_rules", value=lifecycle_rules, expected_type=type_hints["lifecycle_rules"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument repository_name", value=repository_name, expected_type=type_hints["repository_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if auto_delete_images is not None:
            self._values["auto_delete_images"] = auto_delete_images
        if empty_on_delete is not None:
            self._values["empty_on_delete"] = empty_on_delete
        if encryption is not None:
            self._values["encryption"] = encryption
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if image_scan_on_push is not None:
            self._values["image_scan_on_push"] = image_scan_on_push
        if image_tag_mutability is not None:
            self._values["image_tag_mutability"] = image_tag_mutability
        if lifecycle_registry_id is not None:
            self._values["lifecycle_registry_id"] = lifecycle_registry_id
        if lifecycle_rules is not None:
            self._values["lifecycle_rules"] = lifecycle_rules
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if repository_name is not None:
            self._values["repository_name"] = repository_name

    @builtins.property
    def auto_delete_images(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) Whether all images should be automatically deleted when the repository is removed from the stack or when the stack is deleted.

        Requires the ``removalPolicy`` to be set to ``RemovalPolicy.DESTROY``.

        :default: false

        :deprecated: Use ``emptyOnDelete`` instead.

        :stability: deprecated
        '''
        result = self._values.get("auto_delete_images")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def empty_on_delete(self) -> typing.Optional[builtins.bool]:
        '''If true, deleting the repository force deletes the contents of the repository.

        If false, the repository must be empty before attempting to delete it.

        :default: false
        '''
        result = self._values.get("empty_on_delete")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def encryption(self) -> typing.Optional[RepositoryEncryption]:
        '''The kind of server-side encryption to apply to this repository.

        If you choose KMS, you can specify a KMS key via ``encryptionKey``. If
        encryptionKey is not specified, an AWS managed KMS key is used.

        :default: - ``KMS`` if ``encryptionKey`` is specified, or ``AES256`` otherwise.
        '''
        result = self._values.get("encryption")
        return typing.cast(typing.Optional[RepositoryEncryption], result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''External KMS key to use for repository encryption.

        The 'encryption' property must be either not specified or set to "KMS".
        An error will be emitted if encryption is set to "AES256".

        :default:

        - If encryption is set to ``KMS`` and this property is undefined,
        an AWS managed KMS key is used.
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[_IKey_5f11635f], result)

    @builtins.property
    def image_scan_on_push(self) -> typing.Optional[builtins.bool]:
        '''Enable the scan on push when creating the repository.

        :default: false
        '''
        result = self._values.get("image_scan_on_push")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def image_tag_mutability(self) -> typing.Optional["TagMutability"]:
        '''The tag mutability setting for the repository.

        If this parameter is omitted, the default setting of MUTABLE will be used which will allow image tags to be overwritten.

        :default: TagMutability.MUTABLE
        '''
        result = self._values.get("image_tag_mutability")
        return typing.cast(typing.Optional["TagMutability"], result)

    @builtins.property
    def lifecycle_registry_id(self) -> typing.Optional[builtins.str]:
        '''The AWS account ID associated with the registry that contains the repository.

        :default: The default registry is assumed.

        :see: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_PutLifecyclePolicy.html
        '''
        result = self._values.get("lifecycle_registry_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lifecycle_rules(self) -> typing.Optional[typing.List[LifecycleRule]]:
        '''Life cycle rules to apply to this registry.

        :default: No life cycle rules
        '''
        result = self._values.get("lifecycle_rules")
        return typing.cast(typing.Optional[typing.List[LifecycleRule]], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[_RemovalPolicy_9f93c814]:
        '''Determine what happens to the repository when the resource/stack is deleted.

        :default: RemovalPolicy.Retain
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_RemovalPolicy_9f93c814], result)

    @builtins.property
    def repository_name(self) -> typing.Optional[builtins.str]:
        '''Name for this repository.

        The repository name must start with a letter and can only contain lowercase letters, numbers, hyphens, underscores, and forward slashes.
        .. epigraph::

           If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.

        :default: Automatically generated name.
        '''
        result = self._values.get("repository_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RepositoryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_ecr.TagMutability")
class TagMutability(enum.Enum):
    '''The tag mutability setting for your repository.

    :exampleMetadata: infused

    Example::

        ecr.Repository(self, "Repo", image_tag_mutability=ecr.TagMutability.IMMUTABLE)
    '''

    MUTABLE = "MUTABLE"
    '''allow image tags to be overwritten.'''
    IMMUTABLE = "IMMUTABLE"
    '''all image tags within the repository will be immutable which will prevent them from being overwritten.'''


@jsii.enum(jsii_type="aws-cdk-lib.aws_ecr.TagStatus")
class TagStatus(enum.Enum):
    '''Select images based on tags.'''

    ANY = "ANY"
    '''Rule applies to all images.'''
    TAGGED = "TAGGED"
    '''Rule applies to tagged images.'''
    UNTAGGED = "UNTAGGED"
    '''Rule applies to untagged images.'''


class Repository(
    RepositoryBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ecr.Repository",
):
    '''Define an ECR repository.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_lambda as lambda_
        from aws_cdk.aws_events_targets import LambdaFunction
        
        
        repo = ecr.Repository(self, "Repo")
        lambda_handler = lambda_.Function(self, "LambdaFunction",
            runtime=lambda_.Runtime.PYTHON_3_12,
            code=lambda_.Code.from_inline("# dummy func"),
            handler="index.handler"
        )
        
        repo.on_event("OnEventTargetLambda",
            target=LambdaFunction(lambda_handler)
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        auto_delete_images: typing.Optional[builtins.bool] = None,
        empty_on_delete: typing.Optional[builtins.bool] = None,
        encryption: typing.Optional[RepositoryEncryption] = None,
        encryption_key: typing.Optional[_IKey_5f11635f] = None,
        image_scan_on_push: typing.Optional[builtins.bool] = None,
        image_tag_mutability: typing.Optional[TagMutability] = None,
        lifecycle_registry_id: typing.Optional[builtins.str] = None,
        lifecycle_rules: typing.Optional[typing.Sequence[typing.Union[LifecycleRule, typing.Dict[builtins.str, typing.Any]]]] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
        repository_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param auto_delete_images: (deprecated) Whether all images should be automatically deleted when the repository is removed from the stack or when the stack is deleted. Requires the ``removalPolicy`` to be set to ``RemovalPolicy.DESTROY``. Default: false
        :param empty_on_delete: If true, deleting the repository force deletes the contents of the repository. If false, the repository must be empty before attempting to delete it. Default: false
        :param encryption: The kind of server-side encryption to apply to this repository. If you choose KMS, you can specify a KMS key via ``encryptionKey``. If encryptionKey is not specified, an AWS managed KMS key is used. Default: - ``KMS`` if ``encryptionKey`` is specified, or ``AES256`` otherwise.
        :param encryption_key: External KMS key to use for repository encryption. The 'encryption' property must be either not specified or set to "KMS". An error will be emitted if encryption is set to "AES256". Default: - If encryption is set to ``KMS`` and this property is undefined, an AWS managed KMS key is used.
        :param image_scan_on_push: Enable the scan on push when creating the repository. Default: false
        :param image_tag_mutability: The tag mutability setting for the repository. If this parameter is omitted, the default setting of MUTABLE will be used which will allow image tags to be overwritten. Default: TagMutability.MUTABLE
        :param lifecycle_registry_id: The AWS account ID associated with the registry that contains the repository. Default: The default registry is assumed.
        :param lifecycle_rules: Life cycle rules to apply to this registry. Default: No life cycle rules
        :param removal_policy: Determine what happens to the repository when the resource/stack is deleted. Default: RemovalPolicy.Retain
        :param repository_name: Name for this repository. The repository name must start with a letter and can only contain lowercase letters, numbers, hyphens, underscores, and forward slashes. .. epigraph:: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name. Default: Automatically generated name.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fcb489ea7ac91914ff0429ef13d64f8bd29978872d9ce4754ee9d39730a8048)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = RepositoryProps(
            auto_delete_images=auto_delete_images,
            empty_on_delete=empty_on_delete,
            encryption=encryption,
            encryption_key=encryption_key,
            image_scan_on_push=image_scan_on_push,
            image_tag_mutability=image_tag_mutability,
            lifecycle_registry_id=lifecycle_registry_id,
            lifecycle_rules=lifecycle_rules,
            removal_policy=removal_policy,
            repository_name=repository_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForLocalRepository")
    @builtins.classmethod
    def arn_for_local_repository(
        cls,
        repository_name: builtins.str,
        scope: _constructs_77d1e7e8.IConstruct,
        account: typing.Optional[builtins.str] = None,
    ) -> builtins.str:
        '''Returns an ECR ARN for a repository that resides in the same account/region as the current stack.

        :param repository_name: -
        :param scope: -
        :param account: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50aa60495dfd0ac59e7bbbb1d22e4d7dd496bad018fa9790d09cb317dc57b0e5)
            check_type(argname="argument repository_name", value=repository_name, expected_type=type_hints["repository_name"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForLocalRepository", [repository_name, scope, account]))

    @jsii.member(jsii_name="fromRepositoryArn")
    @builtins.classmethod
    def from_repository_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        repository_arn: builtins.str,
    ) -> IRepository:
        '''
        :param scope: -
        :param id: -
        :param repository_arn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb580f927f8776b0abfc35ebe773b5e9b7f5332fd46fd5a456e0b23e497c660e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument repository_arn", value=repository_arn, expected_type=type_hints["repository_arn"])
        return typing.cast(IRepository, jsii.sinvoke(cls, "fromRepositoryArn", [scope, id, repository_arn]))

    @jsii.member(jsii_name="fromRepositoryAttributes")
    @builtins.classmethod
    def from_repository_attributes(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        repository_arn: builtins.str,
        repository_name: builtins.str,
    ) -> IRepository:
        '''Import a repository.

        :param scope: -
        :param id: -
        :param repository_arn: 
        :param repository_name: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84e95ff8ffc142b6c58fd88e86bd423928c5064f45adb93cb53f66970f9f3391)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = RepositoryAttributes(
            repository_arn=repository_arn, repository_name=repository_name
        )

        return typing.cast(IRepository, jsii.sinvoke(cls, "fromRepositoryAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="fromRepositoryName")
    @builtins.classmethod
    def from_repository_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        repository_name: builtins.str,
    ) -> IRepository:
        '''
        :param scope: -
        :param id: -
        :param repository_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5ca0477b2fd49bba346d8aca88c7718dd03d03afcf74fa24cc6e13d86937685)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument repository_name", value=repository_name, expected_type=type_hints["repository_name"])
        return typing.cast(IRepository, jsii.sinvoke(cls, "fromRepositoryName", [scope, id, repository_name]))

    @jsii.member(jsii_name="addLifecycleRule")
    def add_lifecycle_rule(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        max_image_age: typing.Optional[_Duration_4839e8c3] = None,
        max_image_count: typing.Optional[jsii.Number] = None,
        rule_priority: typing.Optional[jsii.Number] = None,
        tag_pattern_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        tag_prefix_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        tag_status: typing.Optional[TagStatus] = None,
    ) -> None:
        '''Add a life cycle rule to the repository.

        Life cycle rules automatically expire images from the repository that match
        certain conditions.

        :param description: Describes the purpose of the rule. Default: No description
        :param max_image_age: The maximum age of images to retain. The value must represent a number of days. Specify exactly one of maxImageCount and maxImageAge.
        :param max_image_count: The maximum number of images to retain. Specify exactly one of maxImageCount and maxImageAge.
        :param rule_priority: Controls the order in which rules are evaluated (low to high). All rules must have a unique priority, where lower numbers have higher precedence. The first rule that matches is applied to an image. There can only be one rule with a tagStatus of Any, and it must have the highest rulePriority. All rules without a specified priority will have incrementing priorities automatically assigned to them, higher than any rules that DO have priorities. Default: Automatically assigned
        :param tag_pattern_list: Select images that have ALL the given patterns in their tag. There is a maximum limit of four wildcards (*) per string. For example, ["*test*1*2*3", "test*1*2*3*"] is valid but ["test*1*2*3*4*5*6"] is invalid. Both tagPrefixList and tagPatternList cannot be specified together in a rule. Only if tagStatus == TagStatus.Tagged
        :param tag_prefix_list: Select images that have ALL the given prefixes in their tag. Both tagPrefixList and tagPatternList cannot be specified together in a rule. Only if tagStatus == TagStatus.Tagged
        :param tag_status: Select images based on tags. Only one rule is allowed to select untagged images, and it must have the highest rulePriority. Default: TagStatus.Tagged if tagPrefixList or tagPatternList is given, TagStatus.Any otherwise
        '''
        rule = LifecycleRule(
            description=description,
            max_image_age=max_image_age,
            max_image_count=max_image_count,
            rule_priority=rule_priority,
            tag_pattern_list=tag_pattern_list,
            tag_prefix_list=tag_prefix_list,
            tag_status=tag_status,
        )

        return typing.cast(None, jsii.invoke(self, "addLifecycleRule", [rule]))

    @jsii.member(jsii_name="addToResourcePolicy")
    def add_to_resource_policy(
        self,
        statement: _PolicyStatement_0fe33853,
    ) -> _AddToResourcePolicyResult_1d0a53ad:
        '''Add a policy statement to the repository's resource policy.

        While other resources policies in AWS either require or accept a resource section,
        Cfn for ECR does not allow us to specify a resource policy.
        It will fail if a resource section is present at all.

        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4c2e425a71ed909d2a0bfefe861aad7c34b251f3ef1f93f5dd7f2be5afffd6b)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(_AddToResourcePolicyResult_1d0a53ad, jsii.invoke(self, "addToResourcePolicy", [statement]))

    @builtins.property
    @jsii.member(jsii_name="repositoryArn")
    def repository_arn(self) -> builtins.str:
        '''The ARN of the repository.'''
        return typing.cast(builtins.str, jsii.get(self, "repositoryArn"))

    @builtins.property
    @jsii.member(jsii_name="repositoryName")
    def repository_name(self) -> builtins.str:
        '''The name of the repository.'''
        return typing.cast(builtins.str, jsii.get(self, "repositoryName"))


__all__ = [
    "AuthorizationToken",
    "CfnPublicRepository",
    "CfnPublicRepositoryProps",
    "CfnPullThroughCacheRule",
    "CfnPullThroughCacheRuleProps",
    "CfnRegistryPolicy",
    "CfnRegistryPolicyProps",
    "CfnReplicationConfiguration",
    "CfnReplicationConfigurationProps",
    "CfnRepository",
    "CfnRepositoryCreationTemplate",
    "CfnRepositoryCreationTemplateProps",
    "CfnRepositoryProps",
    "IRepository",
    "LifecycleRule",
    "OnCloudTrailImagePushedOptions",
    "OnImageScanCompletedOptions",
    "PublicGalleryAuthorizationToken",
    "Repository",
    "RepositoryAttributes",
    "RepositoryBase",
    "RepositoryEncryption",
    "RepositoryProps",
    "TagMutability",
    "TagStatus",
]

publication.publish()

def _typecheckingstub__b189c1467d2bda9405aa4cabd8bab18d9bb346d049339366389c70f4216e7822(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5b1b0a44f7b903d10d3e873896cf1709943b67e3503cc3918e4e98f04ed2c17(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    repository_catalog_data: typing.Any = None,
    repository_name: typing.Optional[builtins.str] = None,
    repository_policy_text: typing.Any = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__317b166576f7593305ca27885da5cd7a621d59c15390c40d8de8d3e3c28eb94b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3890a4bb017b2e52f74cb2ffb17f575b120d2d4a4d312e0c59290c8145be664(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff52c4c89f76461de2458e82c2bfd20f4de3951ad8eab58aec1b52004c07cea7(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c540342cfab06c3e938dc25340d0df062558f4ba1bb13c342e9740ee0e1e909a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a5d0a391359eb22e8e450fd43d68011135dcfa6d843724b27da64f19e19aad7(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e01e3d955755b76bef4d0ce1b9a558313454d69c44cb97d65b4fcb564602a54d(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc5ac22c59e9479a770d5c069f616e21f7babce6447100492c58de88f31b34d6(
    *,
    about_text: typing.Optional[builtins.str] = None,
    architectures: typing.Optional[typing.Sequence[builtins.str]] = None,
    operating_systems: typing.Optional[typing.Sequence[builtins.str]] = None,
    repository_description: typing.Optional[builtins.str] = None,
    usage_text: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92fbf4d1252b7ea335bc4ed7360447e55242ed532586420ec9671bdac83ae8d8(
    *,
    repository_catalog_data: typing.Any = None,
    repository_name: typing.Optional[builtins.str] = None,
    repository_policy_text: typing.Any = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d43871e7810dc89346a08c3c9c24a04a2b82bf02da0d8fa05ef0df564aea4986(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    credential_arn: typing.Optional[builtins.str] = None,
    ecr_repository_prefix: typing.Optional[builtins.str] = None,
    upstream_registry: typing.Optional[builtins.str] = None,
    upstream_registry_url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d8119fd2e97a8168e1c38fa9f34bcdb5556aadec2158866fb3fdc43828f6206(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4a9a8ae5483bccddfb96a4fda4c50b5e880bc70af4044cf5bd93d1432c10c1d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a379fdfcc316f1fba45c0243614513599bd6a9e9b599a9e279a8cc606e4bf382(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97e7364a9d8ce3c9c0a95d7d650a21956fb29a984bd55c4450ace32814a23728(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e6176654c03645cd104e31d54362eb32d0b3856b8d7015586ea920e9ef9cc77(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7eb1d214154bb7e817af1779f0f5bf9f4b1c880ec0a8357fa98987f1063b451f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e53d5495feeae3bec08dd309eceed79d390d73c31e234c306abd812ec670db16(
    *,
    credential_arn: typing.Optional[builtins.str] = None,
    ecr_repository_prefix: typing.Optional[builtins.str] = None,
    upstream_registry: typing.Optional[builtins.str] = None,
    upstream_registry_url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46ab6d6ee08d8397c3ef5738c56a6b991e46657e46e9bb7db4c65859782e8b95(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    policy_text: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__518326f401673fc075bc36aad49fa8c732bf800dcb0a35c514296a4680b8b006(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b830f40efb29b77f187b8cdd48dd5f42b9758bdfaa5f26f17a5410aaba10f2a2(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22f296a7fd25dcbd0e6d71e5f19c5a64bea31bc39494f50b1a2fdceb3a96d82b(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61caec2d35981c77552d8e7762d2c96379773ad1cbd183c24427fd9006273d94(
    *,
    policy_text: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ec8853622a7046906439da72fd8cf7dc34848650d739a637e7ae30cf30d26db(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    replication_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnReplicationConfiguration.ReplicationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf6794ecc113ab8e22e20dce72c6d4af221f57c5e7b6d95be1fa395b94eb50bb(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcdbbdadfe76a214299f1bf1546cbf834942546e6a1a187654f56c7a28e6ee9c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99f4c1062f6a81bbbbbb1ec51556be75ca089974820458f2cf7c2b6ef30a1f4b(
    value: typing.Union[_IResolvable_da3f097b, CfnReplicationConfiguration.ReplicationConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f1a61ec35ac6455ef5be103b0ad56cd75e35b592381509aff016aeca6fc509b(
    *,
    rules: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnReplicationConfiguration.ReplicationRuleProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be71124f033e3826f4c32205bda1d3adb39ad2e783cc193fc52ee22d7f1e2eab(
    *,
    region: builtins.str,
    registry_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db6d7133bf506488b87a4ed998e2db1455e219e9bfa903d0880e4240a48da3c6(
    *,
    destinations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnReplicationConfiguration.ReplicationDestinationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    repository_filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnReplicationConfiguration.RepositoryFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81091e3ace4bd61ec67e8544391ccaefe639b2950197c427c9804e66f026b577(
    *,
    filter: builtins.str,
    filter_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d245b9cf8a9f1459a5c0b6311093064a71adab6058193aba296fc0fff15d6a8(
    *,
    replication_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnReplicationConfiguration.ReplicationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c4027f87eb46bfdc341ea831d36476b6bcb3d7c3adf8e4193a6f82d2e5e98f4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    empty_on_delete: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRepository.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    image_scanning_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRepository.ImageScanningConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    image_tag_mutability: typing.Optional[builtins.str] = None,
    lifecycle_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRepository.LifecyclePolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    repository_name: typing.Optional[builtins.str] = None,
    repository_policy_text: typing.Any = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2248718d73b3c7bcee12085148b85f05a4c458576be92459e450678dd33ba17a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ddcf78870d9e7c9d8fc7a3b39e380fe70edfa62cae47c7ae43d73f1d4e5f7c7(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cdf31a68d1403243dabdc584938d9cf5b1769c665a1d405daaaa8438f7d0367(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf78a5a76e0710f9d352977f8ee877ef0fc7f3c43b6cd9839d2fbeaff522caa1(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRepository.EncryptionConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ae9439aabd4d324bf1d5bdb5b430c995fa4f0fdc0cb44daa41909d48e778564(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRepository.ImageScanningConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d75698f85ccefe489f53d4f155b619c9c3df1026fe201828f3f0ccc7b5fda28(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47418c52de9eb82b5a96dfa3524d84345309cf3a2f06fbbc30eaa7da852a33fa(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRepository.LifecyclePolicyProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__320e28aebae3ff1053b4006047e990e27e37c3a2753340ee0372d4f8e354bc2b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab6f8914cd6d9319d4c072a32100fe3532bf6bfdfe1b069100045f46efd7f432(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a187140649b7378ce5c825b26017544130f832c6f44250242ffcc01b801ada76(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3784a36a4911b348cdf5fe0a9dc355e52973bde3ecafee9df5e1242b07da7d08(
    *,
    encryption_type: builtins.str,
    kms_key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c75cd2b6ec01cb2a5879c051b4088257f2aa69c2f3db3f6435eba0c0b6fd191d(
    *,
    scan_on_push: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e19a186a43de423097984e8a515b442413c2fa31fe895650e26f9f349987264e(
    *,
    lifecycle_policy_text: typing.Optional[builtins.str] = None,
    registry_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__494445c3594e6c48becf87b896b56289e6923275ed1be048e55a955aad19112e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    applied_for: typing.Sequence[builtins.str],
    prefix: builtins.str,
    description: typing.Optional[builtins.str] = None,
    encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRepositoryCreationTemplate.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    image_tag_mutability: typing.Optional[builtins.str] = None,
    lifecycle_policy: typing.Optional[builtins.str] = None,
    repository_policy: typing.Optional[builtins.str] = None,
    resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de25621df06cd38b2a7712beec393825dd8540c7ddd5884bcdd2f43c88cc6a9f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7346b42c53608f40e97cb9640d25fec5f2bfffc755ff8390a4f399e8fec8c41(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d70128c5c73464a6960bdf3e12180f730d72102eeb954991a5ee91b6ced476e1(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7421fb0840fe7d5bdb7ebafbc563d2498adfea23d49797835c3b7262cf06acbe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5438699040b3663de96ef1aac64ac4344fe755ea3bb114b36fdb20c66eeb12e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc9a1c0060c4bcb98843249551561d40d0d01c6137b55d2fc6b20909c4d50df4(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRepositoryCreationTemplate.EncryptionConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d03ac6e7b2975934cbd1c8b2470015fc671509b1b82834732e60abe440bad58(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2e08b01e66ab87aacff8f76d06c2abf47c27bd4366b69a73969d43a0b0b636a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6133d22d20cb78fbb430ebd26935743e57cfc66d8da0d8b426c625527396018f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2fb99e1f96881ee2eeb1081388dcf7c16b80d047a366d3bbc0d4a883ac0e52b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f48a77de88f0d76d55768806e65efb655f325c51435a78fe46978432e8610ec(
    *,
    encryption_type: builtins.str,
    kms_key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__623a27e5bf9e58dfa2c0c25d5b312731cce32386963e30de33e3bd636fb982d3(
    *,
    applied_for: typing.Sequence[builtins.str],
    prefix: builtins.str,
    description: typing.Optional[builtins.str] = None,
    encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRepositoryCreationTemplate.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    image_tag_mutability: typing.Optional[builtins.str] = None,
    lifecycle_policy: typing.Optional[builtins.str] = None,
    repository_policy: typing.Optional[builtins.str] = None,
    resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6887f05f59c4e061f761607002ffdf5b7ad09f76abbf4b7be49513c3ea20ebad(
    *,
    empty_on_delete: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRepository.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    image_scanning_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRepository.ImageScanningConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    image_tag_mutability: typing.Optional[builtins.str] = None,
    lifecycle_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRepository.LifecyclePolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    repository_name: typing.Optional[builtins.str] = None,
    repository_policy_text: typing.Any = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b93b76e3ed83c647651e88dbe69b68aa31811ba690fb413bbf493b24ddae92f(
    statement: _PolicyStatement_0fe33853,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18f0b3f711a06661adb3c2b503f084f1e6774a4c435313ce60aeb9b9c0862a78(
    grantee: _IGrantable_71c4f5de,
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14c48998ec9021e98f12464e9359edb24e2b0f539ca596d1d12fb187b8364316(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73c31def1a2c005caef141293abd28f7d52bc6b3cd34b9aab72ad4461456bf52(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40780df047155d20f169a5f7d2e3cec9d737795fbd2fd65bfbfbff880a95f552(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03f9678bf6d1275cad4a69c4327c5ec4e50a698bcb71b91bc565ec5c00d17ebd(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__581481b04818144d35c370c8364691c22c75abf889fbbde93425ef00df6eb66a(
    id: builtins.str,
    *,
    target: typing.Optional[_IRuleTarget_7a91f454] = None,
    cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6682a5de5f017cf245f225ab2ffa20f3d976bd0d01ff908575d68289ea5cb92e(
    id: builtins.str,
    *,
    image_tag: typing.Optional[builtins.str] = None,
    target: typing.Optional[_IRuleTarget_7a91f454] = None,
    cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05e48b88e3cb8ff8071e5137a10ebf822f9a67fee50365cc9ad50d0e5ef048be(
    id: builtins.str,
    *,
    target: typing.Optional[_IRuleTarget_7a91f454] = None,
    cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e891aed9e9c072461bf707e41c6a0f85f0bf27b1d49dd72a2380d2f74650b37(
    id: builtins.str,
    *,
    image_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    target: typing.Optional[_IRuleTarget_7a91f454] = None,
    cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6efec5eaaaff5e5a00be5c12bb1466927bb81353f89902e1dd5c4af405620db8(
    digest: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43ac1e08a24281d72c0ed626aa4a3d8becdaeb21dc0117029ed9cb5e93568fb5(
    tag: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__894e1dc0284d8788d4bcf980d7755525e14fbcec8b305670af1a388f39980974(
    tag_or_digest: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daefc01ac58c056180e96357fa989faf5de713c6f5bd46bb023e2579bcaf8de0(
    *,
    description: typing.Optional[builtins.str] = None,
    max_image_age: typing.Optional[_Duration_4839e8c3] = None,
    max_image_count: typing.Optional[jsii.Number] = None,
    rule_priority: typing.Optional[jsii.Number] = None,
    tag_pattern_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    tag_prefix_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    tag_status: typing.Optional[TagStatus] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29ce751d750234300d3a95f38312d7cd333a8c93f40235199d6b35a3379922d7(
    *,
    cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
    target: typing.Optional[_IRuleTarget_7a91f454] = None,
    image_tag: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7008a301b5d27c21d26fff448212766f7f8c0067ab03fc3eb8bb5bd100c32277(
    *,
    cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
    target: typing.Optional[_IRuleTarget_7a91f454] = None,
    image_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fd77e7b53fca07660d5412cd9d20f56fac4fdb4d2e19b7941335059053bf70c(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e7e79b01d862fd1beb9d23e3ac604e86944e354ddaa5cefb7cead2845a54dc6(
    *,
    repository_arn: builtins.str,
    repository_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a38c5ca8c70073b00eab7631b4fe1e84b9d8307578ae544e69bb8e01e082e536(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    account: typing.Optional[builtins.str] = None,
    environment_from_arn: typing.Optional[builtins.str] = None,
    physical_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0332d345aba5679afe9fb0b7ab696008671005f2f0d37df9b84a4e6c8e76114a(
    grantee: _IGrantable_71c4f5de,
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a73c5a3d57036dda31cb310868d740db73df050bd928d1f98a2aa6dc7f8f8195(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee46b08a597ed3ce199cf26924cf11ab5fabd9d17bedcc7efc476d1d1c700e2c(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b0273082d293ef1f0dde5de95fd611df83c06e41660b7409f297f562363e104(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31a099ab10f2924b872f9278330820dffe9b52373bfaa3e8885d4ff563eac580(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c139a9b31fe3e7f708003b6e9681fb4646f332fdded0d9490a28ed070894122(
    id: builtins.str,
    *,
    target: typing.Optional[_IRuleTarget_7a91f454] = None,
    cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0d2ebb124849d81a392bd26c0bce7b3b3cf10151d71b5907fb7bd4fafbff603(
    id: builtins.str,
    *,
    image_tag: typing.Optional[builtins.str] = None,
    target: typing.Optional[_IRuleTarget_7a91f454] = None,
    cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51f97041baa3939cfb2ce34fc3fa53b516f3c6e0c4aa588c04f69ec9c7f5c4c2(
    id: builtins.str,
    *,
    target: typing.Optional[_IRuleTarget_7a91f454] = None,
    cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60f3c389878e84cfc27eacd079e1260fe1c75a68121b98730f3af9e704635af9(
    id: builtins.str,
    *,
    image_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    target: typing.Optional[_IRuleTarget_7a91f454] = None,
    cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1cd01de98d564bf59abc17d6fde8add4f2d946d00d87164b7209d02c893dfee(
    digest: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9de3aee1b153dc478086c6f0e5f5e48cb31aaaa05063a0617ec682978677806(
    tag: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__737ee8e7775488279e9f1051f87dc9b1d6c752b8154e3381c9b62a3cc696f8d2(
    tag_or_digest: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6698dcafdf5c8416d9634135d68ec261fb74e16ec8e5fa780d78a8a8fa822ee6(
    statement: _PolicyStatement_0fe33853,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__144b557444508fc0a954f4a654cd03105778da2972bab34f799be4e543750902(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__638b63dd5eb589e01019ee47c63d6335810d02b0d769f767f2bf2fddc285af28(
    *,
    auto_delete_images: typing.Optional[builtins.bool] = None,
    empty_on_delete: typing.Optional[builtins.bool] = None,
    encryption: typing.Optional[RepositoryEncryption] = None,
    encryption_key: typing.Optional[_IKey_5f11635f] = None,
    image_scan_on_push: typing.Optional[builtins.bool] = None,
    image_tag_mutability: typing.Optional[TagMutability] = None,
    lifecycle_registry_id: typing.Optional[builtins.str] = None,
    lifecycle_rules: typing.Optional[typing.Sequence[typing.Union[LifecycleRule, typing.Dict[builtins.str, typing.Any]]]] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    repository_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fcb489ea7ac91914ff0429ef13d64f8bd29978872d9ce4754ee9d39730a8048(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    auto_delete_images: typing.Optional[builtins.bool] = None,
    empty_on_delete: typing.Optional[builtins.bool] = None,
    encryption: typing.Optional[RepositoryEncryption] = None,
    encryption_key: typing.Optional[_IKey_5f11635f] = None,
    image_scan_on_push: typing.Optional[builtins.bool] = None,
    image_tag_mutability: typing.Optional[TagMutability] = None,
    lifecycle_registry_id: typing.Optional[builtins.str] = None,
    lifecycle_rules: typing.Optional[typing.Sequence[typing.Union[LifecycleRule, typing.Dict[builtins.str, typing.Any]]]] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    repository_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50aa60495dfd0ac59e7bbbb1d22e4d7dd496bad018fa9790d09cb317dc57b0e5(
    repository_name: builtins.str,
    scope: _constructs_77d1e7e8.IConstruct,
    account: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb580f927f8776b0abfc35ebe773b5e9b7f5332fd46fd5a456e0b23e497c660e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    repository_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84e95ff8ffc142b6c58fd88e86bd423928c5064f45adb93cb53f66970f9f3391(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    repository_arn: builtins.str,
    repository_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5ca0477b2fd49bba346d8aca88c7718dd03d03afcf74fa24cc6e13d86937685(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    repository_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4c2e425a71ed909d2a0bfefe861aad7c34b251f3ef1f93f5dd7f2be5afffd6b(
    statement: _PolicyStatement_0fe33853,
) -> None:
    """Type checking stubs"""
    pass
