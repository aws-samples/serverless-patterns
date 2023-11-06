'''
# AWS::CodeGuruReviewer Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_codegurureviewer as codegurureviewer
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for CodeGuruReviewer construct libraries](https://constructs.dev/search?q=codegurureviewer)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::CodeGuruReviewer resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CodeGuruReviewer.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::CodeGuruReviewer](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CodeGuruReviewer.html).

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
    ITaggable as _ITaggable_36806126,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnRepositoryAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codegurureviewer.CfnRepositoryAssociation",
):
    '''This resource configures how Amazon CodeGuru Reviewer retrieves the source code to be reviewed.

    You can use an AWS CloudFormation template to create an association with the following repository types:

    - AWS CodeCommit - For more information, see `Create an AWS CodeCommit repository association <https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/create-codecommit-association.html>`_ in the *Amazon CodeGuru Reviewer User Guide* .
    - Bitbucket - For more information, see `Create a Bitbucket repository association <https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/create-bitbucket-association.html>`_ in the *Amazon CodeGuru Reviewer User Guide* .
    - GitHub Enterprise Server - For more information, see `Create a GitHub Enterprise Server repository association <https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/create-github-enterprise-association.html>`_ in the *Amazon CodeGuru Reviewer User Guide* .
    - S3Bucket - For more information, see `Create code reviews with GitHub Actions <https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/working-with-cicd.html>`_ in the *Amazon CodeGuru Reviewer User Guide* .

    .. epigraph::

       You cannot use a CloudFormation template to create an association with a GitHub repository.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codegurureviewer-repositoryassociation.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_codegurureviewer as codegurureviewer
        
        cfn_repository_association = codegurureviewer.CfnRepositoryAssociation(self, "MyCfnRepositoryAssociation",
            name="name",
            type="type",
        
            # the properties below are optional
            bucket_name="bucketName",
            connection_arn="connectionArn",
            owner="owner",
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
        name: builtins.str,
        type: builtins.str,
        bucket_name: typing.Optional[builtins.str] = None,
        connection_arn: typing.Optional[builtins.str] = None,
        owner: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the repository.
        :param type: The type of repository that contains the source code to be reviewed. The valid values are:. - ``CodeCommit`` - ``Bitbucket`` - ``GitHubEnterpriseServer`` - ``S3Bucket``
        :param bucket_name: The name of the bucket. This is required for your S3Bucket repository. The name must start with the prefix ``codeguru-reviewer-*`` .
        :param connection_arn: The Amazon Resource Name (ARN) of an AWS CodeStar Connections connection. Its format is ``arn:aws:codestar-connections:region-id:aws-account_id:connection/connection-id`` . For more information, see `Connection <https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_Connection.html>`_ in the *AWS CodeStar Connections API Reference* . ``ConnectionArn`` must be specified for Bitbucket and GitHub Enterprise Server repositories. It has no effect if it is specified for an AWS CodeCommit repository.
        :param owner: The owner of the repository. For a GitHub Enterprise Server or Bitbucket repository, this is the username for the account that owns the repository. ``Owner`` must be specified for Bitbucket and GitHub Enterprise Server repositories. It has no effect if it is specified for an AWS CodeCommit repository.
        :param tags: An array of key-value pairs used to tag an associated repository. A tag is a custom attribute label with two parts: - A *tag key* (for example, ``CostCenter`` , ``Environment`` , ``Project`` , or ``Secret`` ). Tag keys are case sensitive. - An optional field known as a *tag value* (for example, ``111122223333`` , ``Production`` , or a team name). Omitting the tag value is the same as using an empty string. Like tag keys, tag values are case sensitive.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9945ca32970980617005509f9022b62752f888a7e9cebee0660710304b008fb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRepositoryAssociationProps(
            name=name,
            type=type,
            bucket_name=bucket_name,
            connection_arn=connection_arn,
            owner=owner,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9494290d2bf8ec960d9c30bd0fe39a9b9ee507a6c5bea27b1f005c7b575cfb99)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d533cc1f848d9ccf4055a8d205fc69df3d4943d562961039d5a9771ff2e1f9c0)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAssociationArn")
    def attr_association_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the ```RepositoryAssociation`` <https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html>`_ object. You can retrieve this ARN by calling ``ListRepositories`` .

        :cloudformationAttribute: AssociationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssociationArn"))

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the repository.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec9e75171bbdbb6cad03874dfbe83db6de3d62b761d498097d3ecba4cf7d16b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of repository that contains the source code to be reviewed.

        The valid values are:.
        '''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d3e86008a39bc645731a533974f985601bc350a2cc19b6f00d11eb1edc1df86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''The name of the bucket.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c8ec6150a86eca081534ff87cce4f72151744870d3d3bc09559dc63a710868e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="connectionArn")
    def connection_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of an AWS CodeStar Connections connection.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionArn"))

    @connection_arn.setter
    def connection_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__340c4719835b7311aad6b121af2a3ba1aef22151834543162668050d35f09271)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionArn", value)

    @builtins.property
    @jsii.member(jsii_name="owner")
    def owner(self) -> typing.Optional[builtins.str]:
        '''The owner of the repository.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "owner"))

    @owner.setter
    def owner(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__427305c50fc8bc62fd3ad14efd4738acd5830917e16d2861604ace45033d2b4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "owner", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs used to tag an associated repository.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8a7019de50716e632f620fdc25a9002b3dd655fc191589f4a7e2eb2a4dd50d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codegurureviewer.CfnRepositoryAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "type": "type",
        "bucket_name": "bucketName",
        "connection_arn": "connectionArn",
        "owner": "owner",
        "tags": "tags",
    },
)
class CfnRepositoryAssociationProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        type: builtins.str,
        bucket_name: typing.Optional[builtins.str] = None,
        connection_arn: typing.Optional[builtins.str] = None,
        owner: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRepositoryAssociation``.

        :param name: The name of the repository.
        :param type: The type of repository that contains the source code to be reviewed. The valid values are:. - ``CodeCommit`` - ``Bitbucket`` - ``GitHubEnterpriseServer`` - ``S3Bucket``
        :param bucket_name: The name of the bucket. This is required for your S3Bucket repository. The name must start with the prefix ``codeguru-reviewer-*`` .
        :param connection_arn: The Amazon Resource Name (ARN) of an AWS CodeStar Connections connection. Its format is ``arn:aws:codestar-connections:region-id:aws-account_id:connection/connection-id`` . For more information, see `Connection <https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_Connection.html>`_ in the *AWS CodeStar Connections API Reference* . ``ConnectionArn`` must be specified for Bitbucket and GitHub Enterprise Server repositories. It has no effect if it is specified for an AWS CodeCommit repository.
        :param owner: The owner of the repository. For a GitHub Enterprise Server or Bitbucket repository, this is the username for the account that owns the repository. ``Owner`` must be specified for Bitbucket and GitHub Enterprise Server repositories. It has no effect if it is specified for an AWS CodeCommit repository.
        :param tags: An array of key-value pairs used to tag an associated repository. A tag is a custom attribute label with two parts: - A *tag key* (for example, ``CostCenter`` , ``Environment`` , ``Project`` , or ``Secret`` ). Tag keys are case sensitive. - An optional field known as a *tag value* (for example, ``111122223333`` , ``Production`` , or a team name). Omitting the tag value is the same as using an empty string. Like tag keys, tag values are case sensitive.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codegurureviewer-repositoryassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codegurureviewer as codegurureviewer
            
            cfn_repository_association_props = codegurureviewer.CfnRepositoryAssociationProps(
                name="name",
                type="type",
            
                # the properties below are optional
                bucket_name="bucketName",
                connection_arn="connectionArn",
                owner="owner",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d939dd7ccb51c4eab47616544e6b07081d3a443d23fe246d4d8c6605b292a2f3)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument connection_arn", value=connection_arn, expected_type=type_hints["connection_arn"])
            check_type(argname="argument owner", value=owner, expected_type=type_hints["owner"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "type": type,
        }
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if connection_arn is not None:
            self._values["connection_arn"] = connection_arn
        if owner is not None:
            self._values["owner"] = owner
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the repository.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codegurureviewer-repositoryassociation.html#cfn-codegurureviewer-repositoryassociation-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of repository that contains the source code to be reviewed. The valid values are:.

        - ``CodeCommit``
        - ``Bitbucket``
        - ``GitHubEnterpriseServer``
        - ``S3Bucket``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codegurureviewer-repositoryassociation.html#cfn-codegurureviewer-repositoryassociation-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''The name of the bucket.

        This is required for your S3Bucket repository. The name must start with the prefix ``codeguru-reviewer-*`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codegurureviewer-repositoryassociation.html#cfn-codegurureviewer-repositoryassociation-bucketname
        '''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connection_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of an AWS CodeStar Connections connection.

        Its format is ``arn:aws:codestar-connections:region-id:aws-account_id:connection/connection-id`` . For more information, see `Connection <https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_Connection.html>`_ in the *AWS CodeStar Connections API Reference* .

        ``ConnectionArn`` must be specified for Bitbucket and GitHub Enterprise Server repositories. It has no effect if it is specified for an AWS CodeCommit repository.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codegurureviewer-repositoryassociation.html#cfn-codegurureviewer-repositoryassociation-connectionarn
        '''
        result = self._values.get("connection_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def owner(self) -> typing.Optional[builtins.str]:
        '''The owner of the repository.

        For a GitHub Enterprise Server or Bitbucket repository, this is the username for the account that owns the repository.

        ``Owner`` must be specified for Bitbucket and GitHub Enterprise Server repositories. It has no effect if it is specified for an AWS CodeCommit repository.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codegurureviewer-repositoryassociation.html#cfn-codegurureviewer-repositoryassociation-owner
        '''
        result = self._values.get("owner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs used to tag an associated repository.

        A tag is a custom attribute label with two parts:

        - A *tag key* (for example, ``CostCenter`` , ``Environment`` , ``Project`` , or ``Secret`` ). Tag keys are case sensitive.
        - An optional field known as a *tag value* (for example, ``111122223333`` , ``Production`` , or a team name). Omitting the tag value is the same as using an empty string. Like tag keys, tag values are case sensitive.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codegurureviewer-repositoryassociation.html#cfn-codegurureviewer-repositoryassociation-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRepositoryAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnRepositoryAssociation",
    "CfnRepositoryAssociationProps",
]

publication.publish()

def _typecheckingstub__a9945ca32970980617005509f9022b62752f888a7e9cebee0660710304b008fb(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    type: builtins.str,
    bucket_name: typing.Optional[builtins.str] = None,
    connection_arn: typing.Optional[builtins.str] = None,
    owner: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9494290d2bf8ec960d9c30bd0fe39a9b9ee507a6c5bea27b1f005c7b575cfb99(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d533cc1f848d9ccf4055a8d205fc69df3d4943d562961039d5a9771ff2e1f9c0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec9e75171bbdbb6cad03874dfbe83db6de3d62b761d498097d3ecba4cf7d16b0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d3e86008a39bc645731a533974f985601bc350a2cc19b6f00d11eb1edc1df86(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c8ec6150a86eca081534ff87cce4f72151744870d3d3bc09559dc63a710868e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__340c4719835b7311aad6b121af2a3ba1aef22151834543162668050d35f09271(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__427305c50fc8bc62fd3ad14efd4738acd5830917e16d2861604ace45033d2b4d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8a7019de50716e632f620fdc25a9002b3dd655fc191589f4a7e2eb2a4dd50d0(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d939dd7ccb51c4eab47616544e6b07081d3a443d23fe246d4d8c6605b292a2f3(
    *,
    name: builtins.str,
    type: builtins.str,
    bucket_name: typing.Optional[builtins.str] = None,
    connection_arn: typing.Optional[builtins.str] = None,
    owner: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
