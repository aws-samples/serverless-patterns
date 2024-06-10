'''
# AWS Cloud9 Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_cloud9 as cloud9
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Cloud9 construct libraries](https://constructs.dev/search?q=cloud9)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Cloud9 resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Cloud9.html) directly.

> An experimental construct library for this service is available in preview. Since it is not stable yet, it is distributed
> as a separate package so that you can pin its version independently of the rest of the CDK. See the package:
>
> <span class="package-reference">@aws-cdk/aws-cloud9-alpha</span>

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Cloud9](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Cloud9.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
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
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    ITaggable as _ITaggable_36806126,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnEnvironmentEC2(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloud9.CfnEnvironmentEC2",
):
    '''The ``AWS::Cloud9::EnvironmentEC2`` resource creates an Amazon EC2 development environment in AWS Cloud9 .

    For more information, see `Creating an Environment <https://docs.aws.amazon.com/cloud9/latest/user-guide/create-environment.html>`_ in the *AWS Cloud9 User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html
    :cloudformationResource: AWS::Cloud9::EnvironmentEC2
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloud9 as cloud9
        
        cfn_environment_eC2 = cloud9.CfnEnvironmentEC2(self, "MyCfnEnvironmentEC2",
            image_id="imageId",
            instance_type="instanceType",
        
            # the properties below are optional
            automatic_stop_time_minutes=123,
            connection_type="connectionType",
            description="description",
            name="name",
            owner_arn="ownerArn",
            repositories=[cloud9.CfnEnvironmentEC2.RepositoryProperty(
                path_component="pathComponent",
                repository_url="repositoryUrl"
            )],
            subnet_id="subnetId",
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
        image_id: builtins.str,
        instance_type: builtins.str,
        automatic_stop_time_minutes: typing.Optional[jsii.Number] = None,
        connection_type: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        owner_arn: typing.Optional[builtins.str] = None,
        repositories: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironmentEC2.RepositoryProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param image_id: The identifier for the Amazon Machine Image (AMI) that's used to create the EC2 instance. To choose an AMI for the instance, you must specify a valid AMI alias or a valid AWS Systems Manager path. From December 04, 2023, you will be required to include the ``ImageId`` parameter for the ``CreateEnvironmentEC2`` action. This change will be reflected across all direct methods of communicating with the API, such as AWS SDK, AWS CLI and AWS CloudFormation. This change will only affect direct API consumers, and not AWS Cloud9 console users. Since Ubuntu 18.04 has ended standard support as of May 31, 2023, we recommend you choose Ubuntu 22.04. *AMI aliases* - Amazon Linux 2: ``amazonlinux-2-x86_64`` - Amazon Linux 2023 (recommended): ``amazonlinux-2023-x86_64`` - Ubuntu 18.04: ``ubuntu-18.04-x86_64`` - Ubuntu 22.04: ``ubuntu-22.04-x86_64`` *SSM paths* - Amazon Linux 2: ``resolve:ssm:/aws/service/cloud9/amis/amazonlinux-2-x86_64`` - Amazon Linux 2023 (recommended): ``resolve:ssm:/aws/service/cloud9/amis/amazonlinux-2023-x86_64`` - Ubuntu 18.04: ``resolve:ssm:/aws/service/cloud9/amis/ubuntu-18.04-x86_64`` - Ubuntu 22.04: ``resolve:ssm:/aws/service/cloud9/amis/ubuntu-22.04-x86_64``
        :param instance_type: The type of instance to connect to the environment (for example, ``t2.micro`` ).
        :param automatic_stop_time_minutes: The number of minutes until the running instance is shut down after the environment was last used.
        :param connection_type: The connection type used for connecting to an Amazon EC2 environment. Valid values are ``CONNECT_SSH`` (default) and ``CONNECT_SSM`` (connected through AWS Systems Manager ).
        :param description: The description of the environment to create.
        :param name: The name of the environment.
        :param owner_arn: The Amazon Resource Name (ARN) of the environment owner. This ARN can be the ARN of any AWS Identity and Access Management principal. If this value is not specified, the ARN defaults to this environment's creator.
        :param repositories: Any AWS CodeCommit source code repositories to be cloned into the development environment.
        :param subnet_id: The ID of the subnet in Amazon Virtual Private Cloud (Amazon VPC) that AWS Cloud9 will use to communicate with the Amazon Elastic Compute Cloud (Amazon EC2) instance.
        :param tags: An array of key-value pairs that will be associated with the new AWS Cloud9 development environment.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f20e60d53a3580dabcd8f88a1195a515fcbefe92a9ea846ab6ed1b1bce8546b4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEnvironmentEC2Props(
            image_id=image_id,
            instance_type=instance_type,
            automatic_stop_time_minutes=automatic_stop_time_minutes,
            connection_type=connection_type,
            description=description,
            name=name,
            owner_arn=owner_arn,
            repositories=repositories,
            subnet_id=subnet_id,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01c351d373b56f412cb07a01f554414870b3008fa4e878bdefe92eb62620b54a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__63d75ed9eee88e5c262f2f922913144295062e6e1adb8a8b0bfbf3a9138cb6f8)
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
        '''The Amazon Resource Name (ARN) of the development environment, such as ``arn:aws:cloud9:us-east-2:123456789012:environment:2bc3642873c342e485f7e0c561234567`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''The name of the environment.

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

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
    @jsii.member(jsii_name="imageId")
    def image_id(self) -> builtins.str:
        '''The identifier for the Amazon Machine Image (AMI) that's used to create the EC2 instance.'''
        return typing.cast(builtins.str, jsii.get(self, "imageId"))

    @image_id.setter
    def image_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adbcdde537aa596dafe80b35956e811f7c14d4ec15e787a1f841bf8b0759fd7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageId", value)

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        '''The type of instance to connect to the environment (for example, ``t2.micro`` ).'''
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__295c6c669e47da477e140f2fa3b417bf9d56edb0457b5c81c67e548bac5e583b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="automaticStopTimeMinutes")
    def automatic_stop_time_minutes(self) -> typing.Optional[jsii.Number]:
        '''The number of minutes until the running instance is shut down after the environment was last used.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "automaticStopTimeMinutes"))

    @automatic_stop_time_minutes.setter
    def automatic_stop_time_minutes(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__870f873862daac21573a9c7df2ce1ef3a0b18ce6b1f57830f1fd4ff7bd49aed8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "automaticStopTimeMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="connectionType")
    def connection_type(self) -> typing.Optional[builtins.str]:
        '''The connection type used for connecting to an Amazon EC2 environment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionType"))

    @connection_type.setter
    def connection_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__471cb7549dde284de51de47ad092b1e1639f724188faf55e1c31bcfa8f53fcc7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionType", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the environment to create.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccf8f26efd4e6d0e3ba3ed8bbaa9a66f737394e715521e96209b513a2501b43f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the environment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76adb15f6285c07cc9dbfcdd9c2db131f58b9629fa95eb0dfba0864178a1e3a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="ownerArn")
    def owner_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the environment owner.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ownerArn"))

    @owner_arn.setter
    def owner_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3ed6f600bbd525a5d366e8411b6f2c26e9945c1e1dd78ea3125c82b3ca3a85e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ownerArn", value)

    @builtins.property
    @jsii.member(jsii_name="repositories")
    def repositories(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironmentEC2.RepositoryProperty"]]]]:
        '''Any AWS CodeCommit source code repositories to be cloned into the development environment.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironmentEC2.RepositoryProperty"]]]], jsii.get(self, "repositories"))

    @repositories.setter
    def repositories(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironmentEC2.RepositoryProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33cc7cfcf14da7cc801212fb0f6bde87f66f7a89bbb8b1431ff0da977a8adfbb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repositories", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the subnet in Amazon Virtual Private Cloud (Amazon VPC) that AWS Cloud9 will use to communicate with the Amazon Elastic Compute Cloud (Amazon EC2) instance.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba7d365716a0cf05b85a3c0a55e7302dbb4657fd3bf42b5f280ee69f29e2eda0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs that will be associated with the new AWS Cloud9 development environment.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6e91291aa91d4092e5d643c1959f01ebac2b9c2b63e175fe396fc6fa242c91e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloud9.CfnEnvironmentEC2.RepositoryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "path_component": "pathComponent",
            "repository_url": "repositoryUrl",
        },
    )
    class RepositoryProperty:
        def __init__(
            self,
            *,
            path_component: builtins.str,
            repository_url: builtins.str,
        ) -> None:
            '''The ``Repository`` property type specifies an AWS CodeCommit source code repository to be cloned into an AWS Cloud9 development environment.

            :param path_component: The path within the development environment's default file system location to clone the AWS CodeCommit repository into. For example, ``/REPOSITORY_NAME`` would clone the repository into the ``/home/USER_NAME/environment/REPOSITORY_NAME`` directory in the environment.
            :param repository_url: The clone URL of the AWS CodeCommit repository to be cloned. For example, for an AWS CodeCommit repository this might be ``https://git-codecommit.us-east-2.amazonaws.com/v1/repos/REPOSITORY_NAME`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloud9-environmentec2-repository.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloud9 as cloud9
                
                repository_property = cloud9.CfnEnvironmentEC2.RepositoryProperty(
                    path_component="pathComponent",
                    repository_url="repositoryUrl"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1f170b124bae07e704d39551c1b3c66810f3a968e777ec40f4c806bb7805fc7b)
                check_type(argname="argument path_component", value=path_component, expected_type=type_hints["path_component"])
                check_type(argname="argument repository_url", value=repository_url, expected_type=type_hints["repository_url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "path_component": path_component,
                "repository_url": repository_url,
            }

        @builtins.property
        def path_component(self) -> builtins.str:
            '''The path within the development environment's default file system location to clone the AWS CodeCommit repository into.

            For example, ``/REPOSITORY_NAME`` would clone the repository into the ``/home/USER_NAME/environment/REPOSITORY_NAME`` directory in the environment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloud9-environmentec2-repository.html#cfn-cloud9-environmentec2-repository-pathcomponent
            '''
            result = self._values.get("path_component")
            assert result is not None, "Required property 'path_component' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def repository_url(self) -> builtins.str:
            '''The clone URL of the AWS CodeCommit repository to be cloned.

            For example, for an AWS CodeCommit repository this might be ``https://git-codecommit.us-east-2.amazonaws.com/v1/repos/REPOSITORY_NAME`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloud9-environmentec2-repository.html#cfn-cloud9-environmentec2-repository-repositoryurl
            '''
            result = self._values.get("repository_url")
            assert result is not None, "Required property 'repository_url' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RepositoryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloud9.CfnEnvironmentEC2Props",
    jsii_struct_bases=[],
    name_mapping={
        "image_id": "imageId",
        "instance_type": "instanceType",
        "automatic_stop_time_minutes": "automaticStopTimeMinutes",
        "connection_type": "connectionType",
        "description": "description",
        "name": "name",
        "owner_arn": "ownerArn",
        "repositories": "repositories",
        "subnet_id": "subnetId",
        "tags": "tags",
    },
)
class CfnEnvironmentEC2Props:
    def __init__(
        self,
        *,
        image_id: builtins.str,
        instance_type: builtins.str,
        automatic_stop_time_minutes: typing.Optional[jsii.Number] = None,
        connection_type: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        owner_arn: typing.Optional[builtins.str] = None,
        repositories: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironmentEC2.RepositoryProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEnvironmentEC2``.

        :param image_id: The identifier for the Amazon Machine Image (AMI) that's used to create the EC2 instance. To choose an AMI for the instance, you must specify a valid AMI alias or a valid AWS Systems Manager path. From December 04, 2023, you will be required to include the ``ImageId`` parameter for the ``CreateEnvironmentEC2`` action. This change will be reflected across all direct methods of communicating with the API, such as AWS SDK, AWS CLI and AWS CloudFormation. This change will only affect direct API consumers, and not AWS Cloud9 console users. Since Ubuntu 18.04 has ended standard support as of May 31, 2023, we recommend you choose Ubuntu 22.04. *AMI aliases* - Amazon Linux 2: ``amazonlinux-2-x86_64`` - Amazon Linux 2023 (recommended): ``amazonlinux-2023-x86_64`` - Ubuntu 18.04: ``ubuntu-18.04-x86_64`` - Ubuntu 22.04: ``ubuntu-22.04-x86_64`` *SSM paths* - Amazon Linux 2: ``resolve:ssm:/aws/service/cloud9/amis/amazonlinux-2-x86_64`` - Amazon Linux 2023 (recommended): ``resolve:ssm:/aws/service/cloud9/amis/amazonlinux-2023-x86_64`` - Ubuntu 18.04: ``resolve:ssm:/aws/service/cloud9/amis/ubuntu-18.04-x86_64`` - Ubuntu 22.04: ``resolve:ssm:/aws/service/cloud9/amis/ubuntu-22.04-x86_64``
        :param instance_type: The type of instance to connect to the environment (for example, ``t2.micro`` ).
        :param automatic_stop_time_minutes: The number of minutes until the running instance is shut down after the environment was last used.
        :param connection_type: The connection type used for connecting to an Amazon EC2 environment. Valid values are ``CONNECT_SSH`` (default) and ``CONNECT_SSM`` (connected through AWS Systems Manager ).
        :param description: The description of the environment to create.
        :param name: The name of the environment.
        :param owner_arn: The Amazon Resource Name (ARN) of the environment owner. This ARN can be the ARN of any AWS Identity and Access Management principal. If this value is not specified, the ARN defaults to this environment's creator.
        :param repositories: Any AWS CodeCommit source code repositories to be cloned into the development environment.
        :param subnet_id: The ID of the subnet in Amazon Virtual Private Cloud (Amazon VPC) that AWS Cloud9 will use to communicate with the Amazon Elastic Compute Cloud (Amazon EC2) instance.
        :param tags: An array of key-value pairs that will be associated with the new AWS Cloud9 development environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloud9 as cloud9
            
            cfn_environment_eC2_props = cloud9.CfnEnvironmentEC2Props(
                image_id="imageId",
                instance_type="instanceType",
            
                # the properties below are optional
                automatic_stop_time_minutes=123,
                connection_type="connectionType",
                description="description",
                name="name",
                owner_arn="ownerArn",
                repositories=[cloud9.CfnEnvironmentEC2.RepositoryProperty(
                    path_component="pathComponent",
                    repository_url="repositoryUrl"
                )],
                subnet_id="subnetId",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__403dfb9cb8cd675259c0bc90a981409f45ae842c0991cd0ff175e88f5bd60fca)
            check_type(argname="argument image_id", value=image_id, expected_type=type_hints["image_id"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument automatic_stop_time_minutes", value=automatic_stop_time_minutes, expected_type=type_hints["automatic_stop_time_minutes"])
            check_type(argname="argument connection_type", value=connection_type, expected_type=type_hints["connection_type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument owner_arn", value=owner_arn, expected_type=type_hints["owner_arn"])
            check_type(argname="argument repositories", value=repositories, expected_type=type_hints["repositories"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "image_id": image_id,
            "instance_type": instance_type,
        }
        if automatic_stop_time_minutes is not None:
            self._values["automatic_stop_time_minutes"] = automatic_stop_time_minutes
        if connection_type is not None:
            self._values["connection_type"] = connection_type
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if owner_arn is not None:
            self._values["owner_arn"] = owner_arn
        if repositories is not None:
            self._values["repositories"] = repositories
        if subnet_id is not None:
            self._values["subnet_id"] = subnet_id
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def image_id(self) -> builtins.str:
        '''The identifier for the Amazon Machine Image (AMI) that's used to create the EC2 instance.

        To choose an AMI for the instance, you must specify a valid AMI alias or a valid AWS Systems Manager path.

        From December 04, 2023, you will be required to include the ``ImageId`` parameter for the ``CreateEnvironmentEC2`` action. This change will be reflected across all direct methods of communicating with the API, such as AWS SDK, AWS CLI and AWS CloudFormation. This change will only affect direct API consumers, and not AWS Cloud9 console users.

        Since Ubuntu 18.04 has ended standard support as of May 31, 2023, we recommend you choose Ubuntu 22.04.

        *AMI aliases*

        - Amazon Linux 2: ``amazonlinux-2-x86_64``
        - Amazon Linux 2023 (recommended): ``amazonlinux-2023-x86_64``
        - Ubuntu 18.04: ``ubuntu-18.04-x86_64``
        - Ubuntu 22.04: ``ubuntu-22.04-x86_64``

        *SSM paths*

        - Amazon Linux 2: ``resolve:ssm:/aws/service/cloud9/amis/amazonlinux-2-x86_64``
        - Amazon Linux 2023 (recommended): ``resolve:ssm:/aws/service/cloud9/amis/amazonlinux-2023-x86_64``
        - Ubuntu 18.04: ``resolve:ssm:/aws/service/cloud9/amis/ubuntu-18.04-x86_64``
        - Ubuntu 22.04: ``resolve:ssm:/aws/service/cloud9/amis/ubuntu-22.04-x86_64``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-imageid
        '''
        result = self._values.get("image_id")
        assert result is not None, "Required property 'image_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_type(self) -> builtins.str:
        '''The type of instance to connect to the environment (for example, ``t2.micro`` ).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-instancetype
        '''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def automatic_stop_time_minutes(self) -> typing.Optional[jsii.Number]:
        '''The number of minutes until the running instance is shut down after the environment was last used.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-automaticstoptimeminutes
        '''
        result = self._values.get("automatic_stop_time_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def connection_type(self) -> typing.Optional[builtins.str]:
        '''The connection type used for connecting to an Amazon EC2 environment.

        Valid values are ``CONNECT_SSH`` (default) and ``CONNECT_SSM`` (connected through AWS Systems Manager ).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-connectiontype
        '''
        result = self._values.get("connection_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the environment to create.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def owner_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the environment owner.

        This ARN can be the ARN of any AWS Identity and Access Management principal. If this value is not specified, the ARN defaults to this environment's creator.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-ownerarn
        '''
        result = self._values.get("owner_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def repositories(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironmentEC2.RepositoryProperty]]]]:
        '''Any AWS CodeCommit source code repositories to be cloned into the development environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-repositories
        '''
        result = self._values.get("repositories")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironmentEC2.RepositoryProperty]]]], result)

    @builtins.property
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the subnet in Amazon Virtual Private Cloud (Amazon VPC) that AWS Cloud9 will use to communicate with the Amazon Elastic Compute Cloud (Amazon EC2) instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-subnetid
        '''
        result = self._values.get("subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs that will be associated with the new AWS Cloud9 development environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEnvironmentEC2Props(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnEnvironmentEC2",
    "CfnEnvironmentEC2Props",
]

publication.publish()

def _typecheckingstub__f20e60d53a3580dabcd8f88a1195a515fcbefe92a9ea846ab6ed1b1bce8546b4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    image_id: builtins.str,
    instance_type: builtins.str,
    automatic_stop_time_minutes: typing.Optional[jsii.Number] = None,
    connection_type: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    owner_arn: typing.Optional[builtins.str] = None,
    repositories: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironmentEC2.RepositoryProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    subnet_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01c351d373b56f412cb07a01f554414870b3008fa4e878bdefe92eb62620b54a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63d75ed9eee88e5c262f2f922913144295062e6e1adb8a8b0bfbf3a9138cb6f8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adbcdde537aa596dafe80b35956e811f7c14d4ec15e787a1f841bf8b0759fd7b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__295c6c669e47da477e140f2fa3b417bf9d56edb0457b5c81c67e548bac5e583b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__870f873862daac21573a9c7df2ce1ef3a0b18ce6b1f57830f1fd4ff7bd49aed8(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__471cb7549dde284de51de47ad092b1e1639f724188faf55e1c31bcfa8f53fcc7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccf8f26efd4e6d0e3ba3ed8bbaa9a66f737394e715521e96209b513a2501b43f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76adb15f6285c07cc9dbfcdd9c2db131f58b9629fa95eb0dfba0864178a1e3a0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3ed6f600bbd525a5d366e8411b6f2c26e9945c1e1dd78ea3125c82b3ca3a85e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33cc7cfcf14da7cc801212fb0f6bde87f66f7a89bbb8b1431ff0da977a8adfbb(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironmentEC2.RepositoryProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba7d365716a0cf05b85a3c0a55e7302dbb4657fd3bf42b5f280ee69f29e2eda0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6e91291aa91d4092e5d643c1959f01ebac2b9c2b63e175fe396fc6fa242c91e(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f170b124bae07e704d39551c1b3c66810f3a968e777ec40f4c806bb7805fc7b(
    *,
    path_component: builtins.str,
    repository_url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__403dfb9cb8cd675259c0bc90a981409f45ae842c0991cd0ff175e88f5bd60fca(
    *,
    image_id: builtins.str,
    instance_type: builtins.str,
    automatic_stop_time_minutes: typing.Optional[jsii.Number] = None,
    connection_type: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    owner_arn: typing.Optional[builtins.str] = None,
    repositories: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironmentEC2.RepositoryProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    subnet_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
