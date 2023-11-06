'''
# AWS CodeCommit Construct Library

AWS CodeCommit is a version control service that enables you to privately store and manage Git repositories in the AWS cloud.

For further information on CodeCommit,
see the [AWS CodeCommit documentation](https://docs.aws.amazon.com/codecommit).

To add a CodeCommit Repository to your stack:

```python
repo = codecommit.Repository(self, "Repository",
    repository_name="MyRepositoryName",
    description="Some description."
)
```

Use the `repositoryCloneUrlHttp`, `repositoryCloneUrlSsh` or `repositoryCloneUrlGrc`
property to clone your repository.

To add an Amazon SNS trigger to your repository:

```python
# repo: codecommit.Repository


# trigger is established for all repository actions on all branches by default.
repo.notify("arn:aws:sns:*:123456789012:my_topic")
```

## Add initial commit

It is possible to initialize the Repository via the `Code` class.
It provides methods for loading code from a directory, `.zip` file and from a pre-created CDK Asset.

Example:

```python
repo = codecommit.Repository(self, "Repository",
    repository_name="MyRepositoryName",
    code=codecommit.Code.from_directory(path.join(__dirname, "directory/"), "develop")
)
```

## Events

CodeCommit repositories emit Amazon CloudWatch events for certain activities.
Use the `repo.onXxx` methods to define rules that trigger on these events
and invoke targets as a result:

```python
import aws_cdk.aws_sns as sns
import aws_cdk.aws_events_targets as targets

# repo: codecommit.Repository
# project: codebuild.PipelineProject
# my_topic: sns.Topic


# starts a CodeBuild project when a commit is pushed to the "main" branch of the repo
repo.on_commit("CommitToMain",
    target=targets.CodeBuildProject(project),
    branches=["main"]
)

# publishes a message to an Amazon SNS topic when a comment is made on a pull request
rule = repo.on_comment_on_pull_request("CommentOnPullRequest",
    target=targets.SnsTopic(my_topic)
)
```

## CodeStar Notifications

To define CodeStar Notification rules for Repositories, use one of the `notifyOnXxx()` methods.
They are very similar to `onXxx()` methods for CloudWatch events:

```python
import aws_cdk.aws_chatbot as chatbot

# repository: codecommit.Repository

target = chatbot.SlackChannelConfiguration(self, "MySlackChannel",
    slack_channel_configuration_name="YOUR_CHANNEL_NAME",
    slack_workspace_id="YOUR_SLACK_WORKSPACE_ID",
    slack_channel_id="YOUR_SLACK_CHANNEL_ID"
)
rule = repository.notify_on_pull_request_created("NotifyOnPullRequestCreated", target)
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
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    IResource as _IResource_c80c4260,
    ITaggable as _ITaggable_36806126,
    Resource as _Resource_45bc6135,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..aws_codestarnotifications import (
    DetailType as _DetailType_cf8135e7,
    INotificationRule as _INotificationRule_71939426,
    INotificationRuleSource as _INotificationRuleSource_10482823,
    INotificationRuleTarget as _INotificationRuleTarget_faa3b79b,
    NotificationRuleOptions as _NotificationRuleOptions_dff73281,
    NotificationRuleSourceConfig as _NotificationRuleSourceConfig_20189a3e,
)
from ..aws_events import (
    EventPattern as _EventPattern_fe557901,
    IRuleTarget as _IRuleTarget_7a91f454,
    OnEventOptions as _OnEventOptions_8711b8b3,
    Rule as _Rule_334ed2b5,
)
from ..aws_iam import Grant as _Grant_a7ae64f8, IGrantable as _IGrantable_71c4f5de
from ..aws_s3_assets import Asset as _Asset_ac2a7e61


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnRepository(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codecommit.CfnRepository",
):
    '''Creates a new, empty repository.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_codecommit as codecommit
        
        cfn_repository = codecommit.CfnRepository(self, "MyCfnRepository",
            repository_name="repositoryName",
        
            # the properties below are optional
            code=codecommit.CfnRepository.CodeProperty(
                s3=codecommit.CfnRepository.S3Property(
                    bucket="bucket",
                    key="key",
        
                    # the properties below are optional
                    object_version="objectVersion"
                ),
        
                # the properties below are optional
                branch_name="branchName"
            ),
            repository_description="repositoryDescription",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            triggers=[codecommit.CfnRepository.RepositoryTriggerProperty(
                destination_arn="destinationArn",
                events=["events"],
                name="name",
        
                # the properties below are optional
                branches=["branches"],
                custom_data="customData"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        repository_name: builtins.str,
        code: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRepository.CodeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        repository_description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        triggers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRepository.RepositoryTriggerProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param repository_name: The name of the new repository to be created. .. epigraph:: The repository name must be unique across the calling AWS account . Repository names are limited to 100 alphanumeric, dash, and underscore characters, and cannot include certain characters. For more information about the limits on repository names, see `Quotas <https://docs.aws.amazon.com/codecommit/latest/userguide/limits.html>`_ in the *AWS CodeCommit User Guide* . The suffix .git is prohibited.
        :param code: Information about code to be committed to a repository after it is created in an AWS CloudFormation stack. Information about code is only used in resource creation. Updates to a stack will not reflect changes made to code properties after initial resource creation. .. epigraph:: You can only use this property to add code when creating a repository with a AWS CloudFormation template at creation time. This property cannot be used for updating code to an existing repository.
        :param repository_description: A comment or description about the new repository. .. epigraph:: The description field for a repository accepts all HTML characters and all valid Unicode characters. Applications that do not HTML-encode the description and display it in a webpage can expose users to potentially malicious code. Make sure that you HTML-encode the description field in any application that uses this API to display the repository description on a webpage.
        :param tags: One or more tag key-value pairs to use when tagging this repository.
        :param triggers: The JSON block of configuration information for each trigger.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64c8b70ff11de55544c0f9980a825007e7719d10a7e5b40f2acf7a97e1903316)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRepositoryProps(
            repository_name=repository_name,
            code=code,
            repository_description=repository_description,
            tags=tags,
            triggers=triggers,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14e7c387467f372d552f803c722a33900eeead6044c503cdbb6a483f2bffeb20)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3f41b60d01c2fa702da78ec1be5d872be8498ed5eda9f32e839d8336fab0bd5b)
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
        '''When you pass the logical ID of this resource, the function returns the Amazon Resource Name (ARN) of the repository.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCloneUrlHttp")
    def attr_clone_url_http(self) -> builtins.str:
        '''When you pass the logical ID of this resource, the function returns the URL to use for cloning the repository over HTTPS.

        :cloudformationAttribute: CloneUrlHttp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCloneUrlHttp"))

    @builtins.property
    @jsii.member(jsii_name="attrCloneUrlSsh")
    def attr_clone_url_ssh(self) -> builtins.str:
        '''When you pass the logical ID of this resource, the function returns the URL to use for cloning the repository over SSH.

        :cloudformationAttribute: CloneUrlSsh
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCloneUrlSsh"))

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
        '''When you pass the logical ID of this resource, the function returns the repository's name.

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
    @jsii.member(jsii_name="repositoryName")
    def repository_name(self) -> builtins.str:
        '''The name of the new repository to be created.'''
        return typing.cast(builtins.str, jsii.get(self, "repositoryName"))

    @repository_name.setter
    def repository_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6859c317a69708aff80ba1f8fecce3dd4d7f3d6fb86832e6cff0b5dbd8fab108)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repositoryName", value)

    @builtins.property
    @jsii.member(jsii_name="code")
    def code(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRepository.CodeProperty"]]:
        '''Information about code to be committed to a repository after it is created in an AWS CloudFormation stack.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRepository.CodeProperty"]], jsii.get(self, "code"))

    @code.setter
    def code(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRepository.CodeProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2d9aa151db0306c7144ac1b558b3e0c05b6ba724aad48d7d1cc2dd97531376f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "code", value)

    @builtins.property
    @jsii.member(jsii_name="repositoryDescription")
    def repository_description(self) -> typing.Optional[builtins.str]:
        '''A comment or description about the new repository.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repositoryDescription"))

    @repository_description.setter
    def repository_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f9325bc159d21706aa8257fe0bbabdab9cae89a56ab234752d2dca8f1e7f144)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repositoryDescription", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''One or more tag key-value pairs to use when tagging this repository.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d0a6e36f693d4cc2a11babc985e1e5d85042ffad99b950a29a50f501027166d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="triggers")
    def triggers(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRepository.RepositoryTriggerProperty"]]]]:
        '''The JSON block of configuration information for each trigger.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRepository.RepositoryTriggerProperty"]]]], jsii.get(self, "triggers"))

    @triggers.setter
    def triggers(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRepository.RepositoryTriggerProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aefad5f1e3f33a8892a077db431acd9bec95241245fd5d972238256b13e99377)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "triggers", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codecommit.CfnRepository.CodeProperty",
        jsii_struct_bases=[],
        name_mapping={"s3": "s3", "branch_name": "branchName"},
    )
    class CodeProperty:
        def __init__(
            self,
            *,
            s3: typing.Union[_IResolvable_da3f097b, typing.Union["CfnRepository.S3Property", typing.Dict[builtins.str, typing.Any]]],
            branch_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about code to be committed.

            :param s3: Information about the Amazon S3 bucket that contains a ZIP file of code to be committed to the repository. Changes to this property are ignored after initial resource creation.
            :param branch_name: Optional. Specifies a branch name to be used as the default branch when importing code into a repository on initial creation. If this property is not set, the name *main* will be used for the default branch for the repository. Changes to this property are ignored after initial resource creation. We recommend using this parameter to set the name to *main* to align with the default behavior of CodeCommit unless another name is needed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-code.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codecommit as codecommit
                
                code_property = codecommit.CfnRepository.CodeProperty(
                    s3=codecommit.CfnRepository.S3Property(
                        bucket="bucket",
                        key="key",
                
                        # the properties below are optional
                        object_version="objectVersion"
                    ),
                
                    # the properties below are optional
                    branch_name="branchName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5d1bb9150aed730dac085187c6940e2ac51e7864e609b47673a17723ea173121)
                check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
                check_type(argname="argument branch_name", value=branch_name, expected_type=type_hints["branch_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "s3": s3,
            }
            if branch_name is not None:
                self._values["branch_name"] = branch_name

        @builtins.property
        def s3(self) -> typing.Union[_IResolvable_da3f097b, "CfnRepository.S3Property"]:
            '''Information about the Amazon S3 bucket that contains a ZIP file of code to be committed to the repository.

            Changes to this property are ignored after initial resource creation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-code.html#cfn-codecommit-repository-code-s3
            '''
            result = self._values.get("s3")
            assert result is not None, "Required property 's3' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnRepository.S3Property"], result)

        @builtins.property
        def branch_name(self) -> typing.Optional[builtins.str]:
            '''Optional.

            Specifies a branch name to be used as the default branch when importing code into a repository on initial creation. If this property is not set, the name *main* will be used for the default branch for the repository. Changes to this property are ignored after initial resource creation. We recommend using this parameter to set the name to *main* to align with the default behavior of CodeCommit unless another name is needed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-code.html#cfn-codecommit-repository-code-branchname
            '''
            result = self._values.get("branch_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CodeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codecommit.CfnRepository.RepositoryTriggerProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_arn": "destinationArn",
            "events": "events",
            "name": "name",
            "branches": "branches",
            "custom_data": "customData",
        },
    )
    class RepositoryTriggerProperty:
        def __init__(
            self,
            *,
            destination_arn: builtins.str,
            events: typing.Sequence[builtins.str],
            name: builtins.str,
            branches: typing.Optional[typing.Sequence[builtins.str]] = None,
            custom_data: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about a trigger for a repository.

            .. epigraph::

               If you want to receive notifications about repository events, consider using notifications instead of triggers. For more information, see `Configuring notifications for repository events <https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-repository-email.html>`_ .

            :param destination_arn: The ARN of the resource that is the target for a trigger (for example, the ARN of a topic in Amazon SNS).
            :param events: The repository events that cause the trigger to run actions in another service, such as sending a notification through Amazon SNS. .. epigraph:: The valid value "all" cannot be used with any other values.
            :param name: The name of the trigger.
            :param branches: The branches to be included in the trigger configuration. If you specify an empty array, the trigger applies to all branches. .. epigraph:: Although no content is required in the array, you must include the array itself.
            :param custom_data: Any custom data associated with the trigger to be included in the information sent to the target of the trigger.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-repositorytrigger.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codecommit as codecommit
                
                repository_trigger_property = codecommit.CfnRepository.RepositoryTriggerProperty(
                    destination_arn="destinationArn",
                    events=["events"],
                    name="name",
                
                    # the properties below are optional
                    branches=["branches"],
                    custom_data="customData"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__791b1a38389ed344ae527a7de85d3f177e7ceb35234c227008cb04af7a291ecd)
                check_type(argname="argument destination_arn", value=destination_arn, expected_type=type_hints["destination_arn"])
                check_type(argname="argument events", value=events, expected_type=type_hints["events"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument branches", value=branches, expected_type=type_hints["branches"])
                check_type(argname="argument custom_data", value=custom_data, expected_type=type_hints["custom_data"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination_arn": destination_arn,
                "events": events,
                "name": name,
            }
            if branches is not None:
                self._values["branches"] = branches
            if custom_data is not None:
                self._values["custom_data"] = custom_data

        @builtins.property
        def destination_arn(self) -> builtins.str:
            '''The ARN of the resource that is the target for a trigger (for example, the ARN of a topic in Amazon SNS).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-repositorytrigger.html#cfn-codecommit-repository-repositorytrigger-destinationarn
            '''
            result = self._values.get("destination_arn")
            assert result is not None, "Required property 'destination_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def events(self) -> typing.List[builtins.str]:
            '''The repository events that cause the trigger to run actions in another service, such as sending a notification through Amazon SNS.

            .. epigraph::

               The valid value "all" cannot be used with any other values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-repositorytrigger.html#cfn-codecommit-repository-repositorytrigger-events
            '''
            result = self._values.get("events")
            assert result is not None, "Required property 'events' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the trigger.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-repositorytrigger.html#cfn-codecommit-repository-repositorytrigger-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def branches(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The branches to be included in the trigger configuration.

            If you specify an empty array, the trigger applies to all branches.
            .. epigraph::

               Although no content is required in the array, you must include the array itself.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-repositorytrigger.html#cfn-codecommit-repository-repositorytrigger-branches
            '''
            result = self._values.get("branches")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def custom_data(self) -> typing.Optional[builtins.str]:
            '''Any custom data associated with the trigger to be included in the information sent to the target of the trigger.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-repositorytrigger.html#cfn-codecommit-repository-repositorytrigger-customdata
            '''
            result = self._values.get("custom_data")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RepositoryTriggerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codecommit.CfnRepository.S3Property",
        jsii_struct_bases=[],
        name_mapping={
            "bucket": "bucket",
            "key": "key",
            "object_version": "objectVersion",
        },
    )
    class S3Property:
        def __init__(
            self,
            *,
            bucket: builtins.str,
            key: builtins.str,
            object_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about the Amazon S3 bucket that contains the code that will be committed to the new repository.

            Changes to this property are ignored after initial resource creation.

            :param bucket: The name of the Amazon S3 bucket that contains the ZIP file with the content that will be committed to the new repository. This can be specified using the name of the bucket in the AWS account . Changes to this property are ignored after initial resource creation.
            :param key: The key to use for accessing the Amazon S3 bucket. Changes to this property are ignored after initial resource creation. For more information, see `Creating object key names <https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html>`_ and `Uploading objects <https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html>`_ in the Amazon S3 User Guide.
            :param object_version: The object version of the ZIP file, if versioning is enabled for the Amazon S3 bucket. Changes to this property are ignored after initial resource creation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-s3.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codecommit as codecommit
                
                s3_property = codecommit.CfnRepository.S3Property(
                    bucket="bucket",
                    key="key",
                
                    # the properties below are optional
                    object_version="objectVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ccc0f96fde3de9f745dd3bd29e280e1ca949e70419a8c39fca92cfec1f02e227)
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument object_version", value=object_version, expected_type=type_hints["object_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket": bucket,
                "key": key,
            }
            if object_version is not None:
                self._values["object_version"] = object_version

        @builtins.property
        def bucket(self) -> builtins.str:
            '''The name of the Amazon S3 bucket that contains the ZIP file with the content that will be committed to the new repository.

            This can be specified using the name of the bucket in the AWS account . Changes to this property are ignored after initial resource creation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-s3.html#cfn-codecommit-repository-s3-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key(self) -> builtins.str:
            '''The key to use for accessing the Amazon S3 bucket.

            Changes to this property are ignored after initial resource creation. For more information, see `Creating object key names <https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html>`_ and `Uploading objects <https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html>`_ in the Amazon S3 User Guide.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-s3.html#cfn-codecommit-repository-s3-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def object_version(self) -> typing.Optional[builtins.str]:
            '''The object version of the ZIP file, if versioning is enabled for the Amazon S3 bucket.

            Changes to this property are ignored after initial resource creation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-s3.html#cfn-codecommit-repository-s3-objectversion
            '''
            result = self._values.get("object_version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codecommit.CfnRepositoryProps",
    jsii_struct_bases=[],
    name_mapping={
        "repository_name": "repositoryName",
        "code": "code",
        "repository_description": "repositoryDescription",
        "tags": "tags",
        "triggers": "triggers",
    },
)
class CfnRepositoryProps:
    def __init__(
        self,
        *,
        repository_name: builtins.str,
        code: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRepository.CodeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        repository_description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        triggers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRepository.RepositoryTriggerProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRepository``.

        :param repository_name: The name of the new repository to be created. .. epigraph:: The repository name must be unique across the calling AWS account . Repository names are limited to 100 alphanumeric, dash, and underscore characters, and cannot include certain characters. For more information about the limits on repository names, see `Quotas <https://docs.aws.amazon.com/codecommit/latest/userguide/limits.html>`_ in the *AWS CodeCommit User Guide* . The suffix .git is prohibited.
        :param code: Information about code to be committed to a repository after it is created in an AWS CloudFormation stack. Information about code is only used in resource creation. Updates to a stack will not reflect changes made to code properties after initial resource creation. .. epigraph:: You can only use this property to add code when creating a repository with a AWS CloudFormation template at creation time. This property cannot be used for updating code to an existing repository.
        :param repository_description: A comment or description about the new repository. .. epigraph:: The description field for a repository accepts all HTML characters and all valid Unicode characters. Applications that do not HTML-encode the description and display it in a webpage can expose users to potentially malicious code. Make sure that you HTML-encode the description field in any application that uses this API to display the repository description on a webpage.
        :param tags: One or more tag key-value pairs to use when tagging this repository.
        :param triggers: The JSON block of configuration information for each trigger.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codecommit as codecommit
            
            cfn_repository_props = codecommit.CfnRepositoryProps(
                repository_name="repositoryName",
            
                # the properties below are optional
                code=codecommit.CfnRepository.CodeProperty(
                    s3=codecommit.CfnRepository.S3Property(
                        bucket="bucket",
                        key="key",
            
                        # the properties below are optional
                        object_version="objectVersion"
                    ),
            
                    # the properties below are optional
                    branch_name="branchName"
                ),
                repository_description="repositoryDescription",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                triggers=[codecommit.CfnRepository.RepositoryTriggerProperty(
                    destination_arn="destinationArn",
                    events=["events"],
                    name="name",
            
                    # the properties below are optional
                    branches=["branches"],
                    custom_data="customData"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40c04585281a174d6c45f3d0ebb0cbf1dd9d263edfd133ff98f6e08e9e052bb1)
            check_type(argname="argument repository_name", value=repository_name, expected_type=type_hints["repository_name"])
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
            check_type(argname="argument repository_description", value=repository_description, expected_type=type_hints["repository_description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument triggers", value=triggers, expected_type=type_hints["triggers"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "repository_name": repository_name,
        }
        if code is not None:
            self._values["code"] = code
        if repository_description is not None:
            self._values["repository_description"] = repository_description
        if tags is not None:
            self._values["tags"] = tags
        if triggers is not None:
            self._values["triggers"] = triggers

    @builtins.property
    def repository_name(self) -> builtins.str:
        '''The name of the new repository to be created.

        .. epigraph::

           The repository name must be unique across the calling AWS account . Repository names are limited to 100 alphanumeric, dash, and underscore characters, and cannot include certain characters. For more information about the limits on repository names, see `Quotas <https://docs.aws.amazon.com/codecommit/latest/userguide/limits.html>`_ in the *AWS CodeCommit User Guide* . The suffix .git is prohibited.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.html#cfn-codecommit-repository-repositoryname
        '''
        result = self._values.get("repository_name")
        assert result is not None, "Required property 'repository_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def code(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRepository.CodeProperty]]:
        '''Information about code to be committed to a repository after it is created in an AWS CloudFormation stack.

        Information about code is only used in resource creation. Updates to a stack will not reflect changes made to code properties after initial resource creation.
        .. epigraph::

           You can only use this property to add code when creating a repository with a AWS CloudFormation template at creation time. This property cannot be used for updating code to an existing repository.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.html#cfn-codecommit-repository-code
        '''
        result = self._values.get("code")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRepository.CodeProperty]], result)

    @builtins.property
    def repository_description(self) -> typing.Optional[builtins.str]:
        '''A comment or description about the new repository.

        .. epigraph::

           The description field for a repository accepts all HTML characters and all valid Unicode characters. Applications that do not HTML-encode the description and display it in a webpage can expose users to potentially malicious code. Make sure that you HTML-encode the description field in any application that uses this API to display the repository description on a webpage.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.html#cfn-codecommit-repository-repositorydescription
        '''
        result = self._values.get("repository_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''One or more tag key-value pairs to use when tagging this repository.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.html#cfn-codecommit-repository-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def triggers(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnRepository.RepositoryTriggerProperty]]]]:
        '''The JSON block of configuration information for each trigger.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.html#cfn-codecommit-repository-triggers
        '''
        result = self._values.get("triggers")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnRepository.RepositoryTriggerProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRepositoryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Code(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_codecommit.Code",
):
    '''Represents the contents to initialize the repository with.

    :exampleMetadata: infused

    Example::

        repo = codecommit.Repository(self, "Repository",
            repository_name="MyRepositoryName",
            code=codecommit.Code.from_directory(path.join(__dirname, "directory/"), "develop")
        )
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="fromAsset")
    @builtins.classmethod
    def from_asset(
        cls,
        asset: _Asset_ac2a7e61,
        branch: typing.Optional[builtins.str] = None,
    ) -> "Code":
        '''Code from user-supplied asset.

        :param asset: pre-existing asset.
        :param branch: the name of the branch to create in the repository. Default is "main"
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36447c37e024f3735b5478be259e58f349ae7d9ccb44ee4e4a18a2784b9ba16e)
            check_type(argname="argument asset", value=asset, expected_type=type_hints["asset"])
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
        return typing.cast("Code", jsii.sinvoke(cls, "fromAsset", [asset, branch]))

    @jsii.member(jsii_name="fromDirectory")
    @builtins.classmethod
    def from_directory(
        cls,
        directory_path: builtins.str,
        branch: typing.Optional[builtins.str] = None,
    ) -> "Code":
        '''Code from directory.

        :param directory_path: the path to the local directory containing the contents to initialize the repository with.
        :param branch: the name of the branch to create in the repository. Default is "main"
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__598e43d07069e8231016c09115aeb8aa3804300933d3217d83823def2ca6a4f1)
            check_type(argname="argument directory_path", value=directory_path, expected_type=type_hints["directory_path"])
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
        return typing.cast("Code", jsii.sinvoke(cls, "fromDirectory", [directory_path, branch]))

    @jsii.member(jsii_name="fromZipFile")
    @builtins.classmethod
    def from_zip_file(
        cls,
        file_path: builtins.str,
        branch: typing.Optional[builtins.str] = None,
    ) -> "Code":
        '''Code from preexisting ZIP file.

        :param file_path: the path to the local ZIP file containing the contents to initialize the repository with.
        :param branch: the name of the branch to create in the repository. Default is "main"
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a3f82bd9873943fb876dee699b9267856598db5c500f20e56f140afc46128f4)
            check_type(argname="argument file_path", value=file_path, expected_type=type_hints["file_path"])
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
        return typing.cast("Code", jsii.sinvoke(cls, "fromZipFile", [file_path, branch]))

    @jsii.member(jsii_name="bind")
    @abc.abstractmethod
    def bind(self, scope: _constructs_77d1e7e8.Construct) -> "CodeConfig":
        '''This method is called after a repository is passed this instance of Code in its 'code' property.

        :param scope: the binding scope.
        '''
        ...


class _CodeProxy(Code):
    @jsii.member(jsii_name="bind")
    def bind(self, scope: _constructs_77d1e7e8.Construct) -> "CodeConfig":
        '''This method is called after a repository is passed this instance of Code in its 'code' property.

        :param scope: the binding scope.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4003c87938666d148b25d601f7a14a5a2d2aae2bf4ef6a22a3d035647810652)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast("CodeConfig", jsii.invoke(self, "bind", [scope]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Code).__jsii_proxy_class__ = lambda : _CodeProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codecommit.CodeConfig",
    jsii_struct_bases=[],
    name_mapping={"code": "code"},
)
class CodeConfig:
    def __init__(
        self,
        *,
        code: typing.Union[CfnRepository.CodeProperty, typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''Represents the structure to pass into the underlying CfnRepository class.

        :param code: represents the underlying code structure.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codecommit as codecommit
            
            code_config = codecommit.CodeConfig(
                code=codecommit.CfnRepository.CodeProperty(
                    s3=codecommit.CfnRepository.S3Property(
                        bucket="bucket",
                        key="key",
            
                        # the properties below are optional
                        object_version="objectVersion"
                    ),
            
                    # the properties below are optional
                    branch_name="branchName"
                )
            )
        '''
        if isinstance(code, dict):
            code = CfnRepository.CodeProperty(**code)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea4ac2a79dbabc1d15f21b47d006d6df72efdb31ab914edd8a994b41022afbc8)
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "code": code,
        }

    @builtins.property
    def code(self) -> CfnRepository.CodeProperty:
        '''represents the underlying code structure.'''
        result = self._values.get("code")
        assert result is not None, "Required property 'code' is missing"
        return typing.cast(CfnRepository.CodeProperty, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.aws_codecommit.IRepository")
class IRepository(
    _IResource_c80c4260,
    _INotificationRuleSource_10482823,
    typing_extensions.Protocol,
):
    @builtins.property
    @jsii.member(jsii_name="repositoryArn")
    def repository_arn(self) -> builtins.str:
        '''The ARN of this Repository.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="repositoryCloneUrlGrc")
    def repository_clone_url_grc(self) -> builtins.str:
        '''The HTTPS (GRC) clone URL.

        HTTPS (GRC) is the protocol to use with git-remote-codecommit (GRC).

        It is the recommended method for supporting connections made with federated
        access, identity providers, and temporary credentials.

        :see: https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-git-remote-codecommit.html
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="repositoryCloneUrlHttp")
    def repository_clone_url_http(self) -> builtins.str:
        '''The HTTP clone URL.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="repositoryCloneUrlSsh")
    def repository_clone_url_ssh(self) -> builtins.str:
        '''The SSH clone URL.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="repositoryName")
    def repository_name(self) -> builtins.str:
        '''The human-visible name of this Repository.

        :attribute: true
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
        '''Grant the given identity permissions to pull this repository.

        :param grantee: -
        '''
        ...

    @jsii.member(jsii_name="grantPullPush")
    def grant_pull_push(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the given identity permissions to pull and push this repository.

        :param grantee: -
        '''
        ...

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the given identity permissions to read this repository.

        :param grantee: -
        '''
        ...

    @jsii.member(jsii_name="notifyOn")
    def notify_on(
        self,
        id: builtins.str,
        target: _INotificationRuleTarget_faa3b79b,
        *,
        events: typing.Sequence["RepositoryNotificationEvents"],
        detail_type: typing.Optional[_DetailType_cf8135e7] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> _INotificationRule_71939426:
        '''Defines a CodeStar Notification rule triggered when the project events specified by you are emitted. Similar to ``onEvent`` API.

        You can also use the methods to define rules for the specific event emitted.
        eg: ``notifyOnPullRequstCreated``.

        :param id: -
        :param target: -
        :param events: A list of event types associated with this notification rule for CodeCommit repositories. For a complete list of event types and IDs, see Notification concepts in the Developer Tools Console User Guide.
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``

        :return: CodeStar Notifications rule associated with this repository.
        '''
        ...

    @jsii.member(jsii_name="notifyOnApprovalRuleOverridden")
    def notify_on_approval_rule_overridden(
        self,
        id: builtins.str,
        target: _INotificationRuleTarget_faa3b79b,
        *,
        detail_type: typing.Optional[_DetailType_cf8135e7] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> _INotificationRule_71939426:
        '''Defines a CodeStar Notification rule which triggers when an approval rule is overridden.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        ...

    @jsii.member(jsii_name="notifyOnApprovalStatusChanged")
    def notify_on_approval_status_changed(
        self,
        id: builtins.str,
        target: _INotificationRuleTarget_faa3b79b,
        *,
        detail_type: typing.Optional[_DetailType_cf8135e7] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> _INotificationRule_71939426:
        '''Defines a CodeStar Notification rule which triggers when an approval status is changed.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        ...

    @jsii.member(jsii_name="notifyOnBranchOrTagCreated")
    def notify_on_branch_or_tag_created(
        self,
        id: builtins.str,
        target: _INotificationRuleTarget_faa3b79b,
        *,
        detail_type: typing.Optional[_DetailType_cf8135e7] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> _INotificationRule_71939426:
        '''Defines a CodeStar Notification rule which triggers when a new branch or tag is created.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        ...

    @jsii.member(jsii_name="notifyOnBranchOrTagDeleted")
    def notify_on_branch_or_tag_deleted(
        self,
        id: builtins.str,
        target: _INotificationRuleTarget_faa3b79b,
        *,
        detail_type: typing.Optional[_DetailType_cf8135e7] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> _INotificationRule_71939426:
        '''Defines a CodeStar Notification rule which triggers when a branch or tag is deleted.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        ...

    @jsii.member(jsii_name="notifyOnPullRequestComment")
    def notify_on_pull_request_comment(
        self,
        id: builtins.str,
        target: _INotificationRuleTarget_faa3b79b,
        *,
        detail_type: typing.Optional[_DetailType_cf8135e7] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> _INotificationRule_71939426:
        '''Defines a CodeStar Notification rule which triggers when a comment is made on a pull request.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        ...

    @jsii.member(jsii_name="notifyOnPullRequestCreated")
    def notify_on_pull_request_created(
        self,
        id: builtins.str,
        target: _INotificationRuleTarget_faa3b79b,
        *,
        detail_type: typing.Optional[_DetailType_cf8135e7] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> _INotificationRule_71939426:
        '''Defines a CodeStar Notification rule which triggers when a pull request is created.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        ...

    @jsii.member(jsii_name="notifyOnPullRequestMerged")
    def notify_on_pull_request_merged(
        self,
        id: builtins.str,
        target: _INotificationRuleTarget_faa3b79b,
        *,
        detail_type: typing.Optional[_DetailType_cf8135e7] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> _INotificationRule_71939426:
        '''Defines a CodeStar Notification rule which triggers when a pull request is merged.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        ...

    @jsii.member(jsii_name="onCommentOnCommit")
    def on_comment_on_commit(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines a CloudWatch event rule which triggers when a comment is made on a commit.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        ...

    @jsii.member(jsii_name="onCommentOnPullRequest")
    def on_comment_on_pull_request(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines a CloudWatch event rule which triggers when a comment is made on a pull request.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        ...

    @jsii.member(jsii_name="onCommit")
    def on_commit(
        self,
        id: builtins.str,
        *,
        branches: typing.Optional[typing.Sequence[builtins.str]] = None,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines a CloudWatch event rule which triggers when a commit is pushed to a branch.

        :param id: -
        :param branches: The branch to monitor. Default: - All branches
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

    @jsii.member(jsii_name="onPullRequestStateChange")
    def on_pull_request_state_change(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines a CloudWatch event rule which triggers when a pull request state is changed.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        ...

    @jsii.member(jsii_name="onReferenceCreated")
    def on_reference_created(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines a CloudWatch event rule which triggers when a reference is created (i.e. a new branch/tag is created) to the repository.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        ...

    @jsii.member(jsii_name="onReferenceDeleted")
    def on_reference_deleted(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines a CloudWatch event rule which triggers when a reference is delete (i.e. a branch/tag is deleted) from the repository.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        ...

    @jsii.member(jsii_name="onReferenceUpdated")
    def on_reference_updated(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines a CloudWatch event rule which triggers when a reference is updated (i.e. a commit is pushed to an existing or new branch) from the repository.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        ...

    @jsii.member(jsii_name="onStateChange")
    def on_state_change(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines a CloudWatch event rule which triggers when a "CodeCommit Repository State Change" event occurs.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        ...


class _IRepositoryProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
    jsii.proxy_for(_INotificationRuleSource_10482823), # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_codecommit.IRepository"

    @builtins.property
    @jsii.member(jsii_name="repositoryArn")
    def repository_arn(self) -> builtins.str:
        '''The ARN of this Repository.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "repositoryArn"))

    @builtins.property
    @jsii.member(jsii_name="repositoryCloneUrlGrc")
    def repository_clone_url_grc(self) -> builtins.str:
        '''The HTTPS (GRC) clone URL.

        HTTPS (GRC) is the protocol to use with git-remote-codecommit (GRC).

        It is the recommended method for supporting connections made with federated
        access, identity providers, and temporary credentials.

        :see: https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-git-remote-codecommit.html
        '''
        return typing.cast(builtins.str, jsii.get(self, "repositoryCloneUrlGrc"))

    @builtins.property
    @jsii.member(jsii_name="repositoryCloneUrlHttp")
    def repository_clone_url_http(self) -> builtins.str:
        '''The HTTP clone URL.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "repositoryCloneUrlHttp"))

    @builtins.property
    @jsii.member(jsii_name="repositoryCloneUrlSsh")
    def repository_clone_url_ssh(self) -> builtins.str:
        '''The SSH clone URL.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "repositoryCloneUrlSsh"))

    @builtins.property
    @jsii.member(jsii_name="repositoryName")
    def repository_name(self) -> builtins.str:
        '''The human-visible name of this Repository.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "repositoryName"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__365c5593ff83cf972d077b7c5a84fbc1b5a0265992dc07d9c11fc0b29a29216a)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grant", [grantee, *actions]))

    @jsii.member(jsii_name="grantPull")
    def grant_pull(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the given identity permissions to pull this repository.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d9e6b243e05b7c6eba91182b9bd7adabc3f071225b4e3a50df8e001d1f4fa37)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantPull", [grantee]))

    @jsii.member(jsii_name="grantPullPush")
    def grant_pull_push(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the given identity permissions to pull and push this repository.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a6febdc5d7cf9c0ad4956ce1b01c3943a10e93da55708f00ece4f2eb5e3afb7)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantPullPush", [grantee]))

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the given identity permissions to read this repository.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a3b246d79233ee846d1ea5d76eae3faed1da036177a20d699700bc19f4718f7)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantRead", [grantee]))

    @jsii.member(jsii_name="notifyOn")
    def notify_on(
        self,
        id: builtins.str,
        target: _INotificationRuleTarget_faa3b79b,
        *,
        events: typing.Sequence["RepositoryNotificationEvents"],
        detail_type: typing.Optional[_DetailType_cf8135e7] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> _INotificationRule_71939426:
        '''Defines a CodeStar Notification rule triggered when the project events specified by you are emitted. Similar to ``onEvent`` API.

        You can also use the methods to define rules for the specific event emitted.
        eg: ``notifyOnPullRequstCreated``.

        :param id: -
        :param target: -
        :param events: A list of event types associated with this notification rule for CodeCommit repositories. For a complete list of event types and IDs, see Notification concepts in the Developer Tools Console User Guide.
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``

        :return: CodeStar Notifications rule associated with this repository.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c7942184f6ef1171bc9e0c3554be4e156be2d930de75af76e6c7194dba6915d)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        options = RepositoryNotifyOnOptions(
            events=events,
            detail_type=detail_type,
            enabled=enabled,
            notification_rule_name=notification_rule_name,
        )

        return typing.cast(_INotificationRule_71939426, jsii.invoke(self, "notifyOn", [id, target, options]))

    @jsii.member(jsii_name="notifyOnApprovalRuleOverridden")
    def notify_on_approval_rule_overridden(
        self,
        id: builtins.str,
        target: _INotificationRuleTarget_faa3b79b,
        *,
        detail_type: typing.Optional[_DetailType_cf8135e7] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> _INotificationRule_71939426:
        '''Defines a CodeStar Notification rule which triggers when an approval rule is overridden.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1eaa0e8d10ed3253a51fe07f30f2e5ccd87923daac9fa5cac304d64e8cd2bc73)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        options = _NotificationRuleOptions_dff73281(
            detail_type=detail_type,
            enabled=enabled,
            notification_rule_name=notification_rule_name,
        )

        return typing.cast(_INotificationRule_71939426, jsii.invoke(self, "notifyOnApprovalRuleOverridden", [id, target, options]))

    @jsii.member(jsii_name="notifyOnApprovalStatusChanged")
    def notify_on_approval_status_changed(
        self,
        id: builtins.str,
        target: _INotificationRuleTarget_faa3b79b,
        *,
        detail_type: typing.Optional[_DetailType_cf8135e7] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> _INotificationRule_71939426:
        '''Defines a CodeStar Notification rule which triggers when an approval status is changed.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7bf91f05b1a4f3ae616bd9f41791280fc198c1c0da943398dda62249bb2c93d)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        options = _NotificationRuleOptions_dff73281(
            detail_type=detail_type,
            enabled=enabled,
            notification_rule_name=notification_rule_name,
        )

        return typing.cast(_INotificationRule_71939426, jsii.invoke(self, "notifyOnApprovalStatusChanged", [id, target, options]))

    @jsii.member(jsii_name="notifyOnBranchOrTagCreated")
    def notify_on_branch_or_tag_created(
        self,
        id: builtins.str,
        target: _INotificationRuleTarget_faa3b79b,
        *,
        detail_type: typing.Optional[_DetailType_cf8135e7] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> _INotificationRule_71939426:
        '''Defines a CodeStar Notification rule which triggers when a new branch or tag is created.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cafbc61c624b37c5ad3d4b8a63e817009d77858ce7b25f3e44bba75d8b2c826c)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        options = _NotificationRuleOptions_dff73281(
            detail_type=detail_type,
            enabled=enabled,
            notification_rule_name=notification_rule_name,
        )

        return typing.cast(_INotificationRule_71939426, jsii.invoke(self, "notifyOnBranchOrTagCreated", [id, target, options]))

    @jsii.member(jsii_name="notifyOnBranchOrTagDeleted")
    def notify_on_branch_or_tag_deleted(
        self,
        id: builtins.str,
        target: _INotificationRuleTarget_faa3b79b,
        *,
        detail_type: typing.Optional[_DetailType_cf8135e7] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> _INotificationRule_71939426:
        '''Defines a CodeStar Notification rule which triggers when a branch or tag is deleted.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0275a2e8104bae4bd7ac1bba2e30688464d013a5007f7602a9ea90f4408842fc)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        options = _NotificationRuleOptions_dff73281(
            detail_type=detail_type,
            enabled=enabled,
            notification_rule_name=notification_rule_name,
        )

        return typing.cast(_INotificationRule_71939426, jsii.invoke(self, "notifyOnBranchOrTagDeleted", [id, target, options]))

    @jsii.member(jsii_name="notifyOnPullRequestComment")
    def notify_on_pull_request_comment(
        self,
        id: builtins.str,
        target: _INotificationRuleTarget_faa3b79b,
        *,
        detail_type: typing.Optional[_DetailType_cf8135e7] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> _INotificationRule_71939426:
        '''Defines a CodeStar Notification rule which triggers when a comment is made on a pull request.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6248afe48e2fb868c294f63ac413c00382e7856dc1949f9226aad20932c7e7e5)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        options = _NotificationRuleOptions_dff73281(
            detail_type=detail_type,
            enabled=enabled,
            notification_rule_name=notification_rule_name,
        )

        return typing.cast(_INotificationRule_71939426, jsii.invoke(self, "notifyOnPullRequestComment", [id, target, options]))

    @jsii.member(jsii_name="notifyOnPullRequestCreated")
    def notify_on_pull_request_created(
        self,
        id: builtins.str,
        target: _INotificationRuleTarget_faa3b79b,
        *,
        detail_type: typing.Optional[_DetailType_cf8135e7] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> _INotificationRule_71939426:
        '''Defines a CodeStar Notification rule which triggers when a pull request is created.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f02ad2ac0201a88eb92c38b6798b71bcc5a0c60f935ccccfd798c221251e41df)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        options = _NotificationRuleOptions_dff73281(
            detail_type=detail_type,
            enabled=enabled,
            notification_rule_name=notification_rule_name,
        )

        return typing.cast(_INotificationRule_71939426, jsii.invoke(self, "notifyOnPullRequestCreated", [id, target, options]))

    @jsii.member(jsii_name="notifyOnPullRequestMerged")
    def notify_on_pull_request_merged(
        self,
        id: builtins.str,
        target: _INotificationRuleTarget_faa3b79b,
        *,
        detail_type: typing.Optional[_DetailType_cf8135e7] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> _INotificationRule_71939426:
        '''Defines a CodeStar Notification rule which triggers when a pull request is merged.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a979cb7a485f86b22849a4dd125f67228ce5778a7cf334f786600ef50b4bcb80)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        options = _NotificationRuleOptions_dff73281(
            detail_type=detail_type,
            enabled=enabled,
            notification_rule_name=notification_rule_name,
        )

        return typing.cast(_INotificationRule_71939426, jsii.invoke(self, "notifyOnPullRequestMerged", [id, target, options]))

    @jsii.member(jsii_name="onCommentOnCommit")
    def on_comment_on_commit(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines a CloudWatch event rule which triggers when a comment is made on a commit.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b13dbc0afad5a8310c818d81730321b5d30c626697d8b2da78f99e2fd1bc7a2)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _OnEventOptions_8711b8b3(
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onCommentOnCommit", [id, options]))

    @jsii.member(jsii_name="onCommentOnPullRequest")
    def on_comment_on_pull_request(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines a CloudWatch event rule which triggers when a comment is made on a pull request.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__022a2d7879b191ea4d30f968e4c0507a65f74cb5655b3e01025c411d5a87d764)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _OnEventOptions_8711b8b3(
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onCommentOnPullRequest", [id, options]))

    @jsii.member(jsii_name="onCommit")
    def on_commit(
        self,
        id: builtins.str,
        *,
        branches: typing.Optional[typing.Sequence[builtins.str]] = None,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines a CloudWatch event rule which triggers when a commit is pushed to a branch.

        :param id: -
        :param branches: The branch to monitor. Default: - All branches
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0d481bc7c4182a1ac18ea2989bcaa2496cb87321e12fc1d4c1199f6c9725fa9)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = OnCommitOptions(
            branches=branches,
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onCommit", [id, options]))

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
            type_hints = typing.get_type_hints(_typecheckingstub__d6f54ec4ba5273f31ec8895010478e4112d943903cb729374b88ff19d8d2cbbb)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _OnEventOptions_8711b8b3(
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onEvent", [id, options]))

    @jsii.member(jsii_name="onPullRequestStateChange")
    def on_pull_request_state_change(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines a CloudWatch event rule which triggers when a pull request state is changed.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd475d88fc4c78b023fb9486283e5b3c70aa9e5bc8198d12f2d6258e07211c05)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _OnEventOptions_8711b8b3(
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onPullRequestStateChange", [id, options]))

    @jsii.member(jsii_name="onReferenceCreated")
    def on_reference_created(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines a CloudWatch event rule which triggers when a reference is created (i.e. a new branch/tag is created) to the repository.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0910d5c390fbbee842a81d3014cb2cbc92f66be0788ad6afdbd8d33537f5fff6)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _OnEventOptions_8711b8b3(
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onReferenceCreated", [id, options]))

    @jsii.member(jsii_name="onReferenceDeleted")
    def on_reference_deleted(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines a CloudWatch event rule which triggers when a reference is delete (i.e. a branch/tag is deleted) from the repository.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcd3a4ba200e7a391250089adbbdae2d47ddef364737384821b9f31b6264315c)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _OnEventOptions_8711b8b3(
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onReferenceDeleted", [id, options]))

    @jsii.member(jsii_name="onReferenceUpdated")
    def on_reference_updated(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines a CloudWatch event rule which triggers when a reference is updated (i.e. a commit is pushed to an existing or new branch) from the repository.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0aee5dce826833691e86aae6c2a6d46fb6d2653dcf57d20baee5422625ba26e3)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _OnEventOptions_8711b8b3(
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onReferenceUpdated", [id, options]))

    @jsii.member(jsii_name="onStateChange")
    def on_state_change(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines a CloudWatch event rule which triggers when a "CodeCommit Repository State Change" event occurs.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec4a2730813e663960c4c8d8a730817b32d936daf8c8ac9bd2ccfedb72150e2c)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _OnEventOptions_8711b8b3(
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onStateChange", [id, options]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRepository).__jsii_proxy_class__ = lambda : _IRepositoryProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codecommit.OnCommitOptions",
    jsii_struct_bases=[_OnEventOptions_8711b8b3],
    name_mapping={
        "cross_stack_scope": "crossStackScope",
        "description": "description",
        "event_pattern": "eventPattern",
        "rule_name": "ruleName",
        "target": "target",
        "branches": "branches",
    },
)
class OnCommitOptions(_OnEventOptions_8711b8b3):
    def __init__(
        self,
        *,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        branches: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Options for the onCommit() method.

        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param branches: The branch to monitor. Default: - All branches

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_codecommit as codecommit
            import aws_cdk.aws_events_targets as targets
            
            # repo: codecommit.Repository
            
            my_topic = sns.Topic(self, "Topic")
            
            repo.on_commit("OnCommit",
                target=targets.SnsTopic(my_topic)
            )
        '''
        if isinstance(event_pattern, dict):
            event_pattern = _EventPattern_fe557901(**event_pattern)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c53b1f18ce4d88514601fab8586927ad977e89525fe4ce21ca79eee655396c1d)
            check_type(argname="argument cross_stack_scope", value=cross_stack_scope, expected_type=type_hints["cross_stack_scope"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument event_pattern", value=event_pattern, expected_type=type_hints["event_pattern"])
            check_type(argname="argument rule_name", value=rule_name, expected_type=type_hints["rule_name"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument branches", value=branches, expected_type=type_hints["branches"])
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
        if branches is not None:
            self._values["branches"] = branches

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
    def branches(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The branch to monitor.

        :default: - All branches
        '''
        result = self._values.get("branches")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OnCommitOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ReferenceEvent(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codecommit.ReferenceEvent",
):
    '''Fields of CloudWatch Events that change references.

    :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/EventTypes.html#codebuild_event_type
    '''

    @jsii.python.classproperty
    @jsii.member(jsii_name="commitId")
    def commit_id(cls) -> builtins.str:
        '''Commit id this reference now points to.'''
        return typing.cast(builtins.str, jsii.sget(cls, "commitId"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="eventType")
    def event_type(cls) -> builtins.str:
        '''The type of reference event.

        'referenceCreated', 'referenceUpdated' or 'referenceDeleted'
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "eventType"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="referenceFullName")
    def reference_full_name(cls) -> builtins.str:
        '''Full reference name.

        For example, 'refs/tags/myTag'
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "referenceFullName"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="referenceName")
    def reference_name(cls) -> builtins.str:
        '''Name of reference changed (branch or tag name).'''
        return typing.cast(builtins.str, jsii.sget(cls, "referenceName"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="referenceType")
    def reference_type(cls) -> builtins.str:
        '''Type of reference changed.

        'branch' or 'tag'
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "referenceType"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="repositoryId")
    def repository_id(cls) -> builtins.str:
        '''Id of the CodeCommit repository.'''
        return typing.cast(builtins.str, jsii.sget(cls, "repositoryId"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="repositoryName")
    def repository_name(cls) -> builtins.str:
        '''Name of the CodeCommit repository.'''
        return typing.cast(builtins.str, jsii.sget(cls, "repositoryName"))


@jsii.implements(IRepository)
class Repository(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codecommit.Repository",
):
    '''Provides a CodeCommit Repository.

    :exampleMetadata: infused

    Example::

        # project: codebuild.PipelineProject
        
        repository = codecommit.Repository(self, "MyRepository",
            repository_name="MyRepository"
        )
        project = codebuild.PipelineProject(self, "MyProject")
        
        source_output = codepipeline.Artifact()
        source_action = codepipeline_actions.CodeCommitSourceAction(
            action_name="CodeCommit",
            repository=repository,
            output=source_output
        )
        build_action = codepipeline_actions.CodeBuildAction(
            action_name="CodeBuild",
            project=project,
            input=source_output,
            outputs=[codepipeline.Artifact()],  # optional
            execute_batch_build=True,  # optional, defaults to false
            combine_batch_build_artifacts=True
        )
        
        codepipeline.Pipeline(self, "MyPipeline",
            stages=[codepipeline.StageProps(
                stage_name="Source",
                actions=[source_action]
            ), codepipeline.StageProps(
                stage_name="Build",
                actions=[build_action]
            )
            ]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        repository_name: builtins.str,
        code: typing.Optional[Code] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param repository_name: Name of the repository. This property is required for all CodeCommit repositories.
        :param code: The contents with which to initialize the repository after it has been created. Default: - No initialization (create empty repo)
        :param description: A description of the repository. Use the description to identify the purpose of the repository. Default: - No description.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc18226d2621b909e0802baaec299567def39762c6bf07510ef197899ff96a91)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = RepositoryProps(
            repository_name=repository_name, code=code, description=description
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromRepositoryArn")
    @builtins.classmethod
    def from_repository_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        repository_arn: builtins.str,
    ) -> IRepository:
        '''Imports a codecommit repository.

        :param scope: -
        :param id: -
        :param repository_arn: (e.g. ``arn:aws:codecommit:us-east-1:123456789012:MyDemoRepo``).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3981dcb255b9a3266cc0fc6d2890e5a7fef96f5894a4ef967ff666e58f72833)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument repository_arn", value=repository_arn, expected_type=type_hints["repository_arn"])
        return typing.cast(IRepository, jsii.sinvoke(cls, "fromRepositoryArn", [scope, id, repository_arn]))

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
            type_hints = typing.get_type_hints(_typecheckingstub__81bca08f72268202d3b364831715be5587852151603627292a8e61129e37c3c0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument repository_name", value=repository_name, expected_type=type_hints["repository_name"])
        return typing.cast(IRepository, jsii.sinvoke(cls, "fromRepositoryName", [scope, id, repository_name]))

    @jsii.member(jsii_name="bindAsNotificationRuleSource")
    def bind_as_notification_rule_source(
        self,
        _scope: _constructs_77d1e7e8.Construct,
    ) -> _NotificationRuleSourceConfig_20189a3e:
        '''Returns a source configuration for notification rule.

        :param _scope: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bce1acfc9824ad93658ba014d62079e398555716fd9c87708b05022831b1b038)
            check_type(argname="argument _scope", value=_scope, expected_type=type_hints["_scope"])
        return typing.cast(_NotificationRuleSourceConfig_20189a3e, jsii.invoke(self, "bindAsNotificationRuleSource", [_scope]))

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
            type_hints = typing.get_type_hints(_typecheckingstub__f7402788e4dbfde5dc7ec7b32089dea4a8dc1cb74bc501e6fa6508c70c4d8ded)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grant", [grantee, *actions]))

    @jsii.member(jsii_name="grantPull")
    def grant_pull(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the given identity permissions to pull this repository.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbbcecbc7faeddbda99d49cffd055e8154005631aa698172977c6e4db28ac599)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantPull", [grantee]))

    @jsii.member(jsii_name="grantPullPush")
    def grant_pull_push(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the given identity permissions to pull and push this repository.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79efe60503b55cc3a5f2df365dc0093da149f058148cc261dc626ddfc9d2f4df)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantPullPush", [grantee]))

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the given identity permissions to read this repository.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3458cc082e7e4e18874ae54159c1143c8d40951328feef885af0a725811c1938)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantRead", [grantee]))

    @jsii.member(jsii_name="notifiyOnPullRequestMerged")
    def notifiy_on_pull_request_merged(
        self,
        id: builtins.str,
        target: _INotificationRuleTarget_faa3b79b,
        *,
        detail_type: typing.Optional[_DetailType_cf8135e7] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> _INotificationRule_71939426:
        '''Defines a CodeStar Notification rule which triggers when a pull request is merged.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e51541fedf5c8bb4467983a2551ed5f9efa788750c8ebec9fbcf9aaeeb197dca)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        options = _NotificationRuleOptions_dff73281(
            detail_type=detail_type,
            enabled=enabled,
            notification_rule_name=notification_rule_name,
        )

        return typing.cast(_INotificationRule_71939426, jsii.invoke(self, "notifiyOnPullRequestMerged", [id, target, options]))

    @jsii.member(jsii_name="notify")
    def notify(
        self,
        arn: builtins.str,
        *,
        branches: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_data: typing.Optional[builtins.str] = None,
        events: typing.Optional[typing.Sequence["RepositoryEventTrigger"]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "Repository":
        '''Create a trigger to notify another service to run actions on repository events.

        :param arn: Arn of the resource that repository events will notify.
        :param branches: The names of the branches in the AWS CodeCommit repository that contain events that you want to include in the trigger. If you don't specify at least one branch, the trigger applies to all branches.
        :param custom_data: When an event is triggered, additional information that AWS CodeCommit includes when it sends information to the target.
        :param events: The repository events for which AWS CodeCommit sends information to the target, which you specified in the DestinationArn property.If you don't specify events, the trigger runs for all repository events.
        :param name: A name for the trigger.Triggers on a repository must have unique names.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dbf9817defa3c5754b555f652afc4ba61c38e30a594dad01abc68b7850d81ee)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
        options = RepositoryTriggerOptions(
            branches=branches, custom_data=custom_data, events=events, name=name
        )

        return typing.cast("Repository", jsii.invoke(self, "notify", [arn, options]))

    @jsii.member(jsii_name="notifyOn")
    def notify_on(
        self,
        id: builtins.str,
        target: _INotificationRuleTarget_faa3b79b,
        *,
        events: typing.Sequence["RepositoryNotificationEvents"],
        detail_type: typing.Optional[_DetailType_cf8135e7] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> _INotificationRule_71939426:
        '''Defines a CodeStar Notification rule triggered when the project events specified by you are emitted. Similar to ``onEvent`` API.

        You can also use the methods to define rules for the specific event emitted.
        eg: ``notifyOnPullRequstCreated``.

        :param id: -
        :param target: -
        :param events: A list of event types associated with this notification rule for CodeCommit repositories. For a complete list of event types and IDs, see Notification concepts in the Developer Tools Console User Guide.
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2749a2587821387b871505c0408414b596d663e34cdcf4cf4680c6ea428ab696)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        options = RepositoryNotifyOnOptions(
            events=events,
            detail_type=detail_type,
            enabled=enabled,
            notification_rule_name=notification_rule_name,
        )

        return typing.cast(_INotificationRule_71939426, jsii.invoke(self, "notifyOn", [id, target, options]))

    @jsii.member(jsii_name="notifyOnApprovalRuleOverridden")
    def notify_on_approval_rule_overridden(
        self,
        id: builtins.str,
        target: _INotificationRuleTarget_faa3b79b,
        *,
        detail_type: typing.Optional[_DetailType_cf8135e7] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> _INotificationRule_71939426:
        '''Defines a CodeStar Notification rule which triggers when an approval rule is overridden.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e63d1ce633a4f4266a796f6cdb67b39a645cc34554e1565e442106e47410e044)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        options = _NotificationRuleOptions_dff73281(
            detail_type=detail_type,
            enabled=enabled,
            notification_rule_name=notification_rule_name,
        )

        return typing.cast(_INotificationRule_71939426, jsii.invoke(self, "notifyOnApprovalRuleOverridden", [id, target, options]))

    @jsii.member(jsii_name="notifyOnApprovalStatusChanged")
    def notify_on_approval_status_changed(
        self,
        id: builtins.str,
        target: _INotificationRuleTarget_faa3b79b,
        *,
        detail_type: typing.Optional[_DetailType_cf8135e7] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> _INotificationRule_71939426:
        '''Defines a CodeStar Notification rule which triggers when an approval status is changed.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc8c6b048a43947387c3a5e34fc554543aa2e3e1d20768589eed5d96e44164a3)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        options = _NotificationRuleOptions_dff73281(
            detail_type=detail_type,
            enabled=enabled,
            notification_rule_name=notification_rule_name,
        )

        return typing.cast(_INotificationRule_71939426, jsii.invoke(self, "notifyOnApprovalStatusChanged", [id, target, options]))

    @jsii.member(jsii_name="notifyOnBranchOrTagCreated")
    def notify_on_branch_or_tag_created(
        self,
        id: builtins.str,
        target: _INotificationRuleTarget_faa3b79b,
        *,
        detail_type: typing.Optional[_DetailType_cf8135e7] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> _INotificationRule_71939426:
        '''Defines a CodeStar Notification rule which triggers when a new branch or tag is created.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb870921bbb9ab4ed9e1a62ba8ef6bf25612d59da0df03c9c1baa71010433baf)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        options = _NotificationRuleOptions_dff73281(
            detail_type=detail_type,
            enabled=enabled,
            notification_rule_name=notification_rule_name,
        )

        return typing.cast(_INotificationRule_71939426, jsii.invoke(self, "notifyOnBranchOrTagCreated", [id, target, options]))

    @jsii.member(jsii_name="notifyOnBranchOrTagDeleted")
    def notify_on_branch_or_tag_deleted(
        self,
        id: builtins.str,
        target: _INotificationRuleTarget_faa3b79b,
        *,
        detail_type: typing.Optional[_DetailType_cf8135e7] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> _INotificationRule_71939426:
        '''Defines a CodeStar Notification rule which triggers when a branch or tag is deleted.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__590bcfde747b37888d42f2e95418df6766d69b978c2275b81a2d68c189377d31)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        options = _NotificationRuleOptions_dff73281(
            detail_type=detail_type,
            enabled=enabled,
            notification_rule_name=notification_rule_name,
        )

        return typing.cast(_INotificationRule_71939426, jsii.invoke(self, "notifyOnBranchOrTagDeleted", [id, target, options]))

    @jsii.member(jsii_name="notifyOnPullRequestComment")
    def notify_on_pull_request_comment(
        self,
        id: builtins.str,
        target: _INotificationRuleTarget_faa3b79b,
        *,
        detail_type: typing.Optional[_DetailType_cf8135e7] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> _INotificationRule_71939426:
        '''Defines a CodeStar Notification rule which triggers when a comment is made on a pull request.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8945454cd0688bf69a49ca491edd2ce985eab8c28b695a4392ae84fbba40b96f)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        options = _NotificationRuleOptions_dff73281(
            detail_type=detail_type,
            enabled=enabled,
            notification_rule_name=notification_rule_name,
        )

        return typing.cast(_INotificationRule_71939426, jsii.invoke(self, "notifyOnPullRequestComment", [id, target, options]))

    @jsii.member(jsii_name="notifyOnPullRequestCreated")
    def notify_on_pull_request_created(
        self,
        id: builtins.str,
        target: _INotificationRuleTarget_faa3b79b,
        *,
        detail_type: typing.Optional[_DetailType_cf8135e7] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> _INotificationRule_71939426:
        '''Defines a CodeStar Notification rule which triggers when a pull request is created.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9584aecb592a6d74f000818947c6960318c665568cef4b2803439fb35a634f69)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        options = _NotificationRuleOptions_dff73281(
            detail_type=detail_type,
            enabled=enabled,
            notification_rule_name=notification_rule_name,
        )

        return typing.cast(_INotificationRule_71939426, jsii.invoke(self, "notifyOnPullRequestCreated", [id, target, options]))

    @jsii.member(jsii_name="notifyOnPullRequestMerged")
    def notify_on_pull_request_merged(
        self,
        id: builtins.str,
        target: _INotificationRuleTarget_faa3b79b,
        *,
        detail_type: typing.Optional[_DetailType_cf8135e7] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> _INotificationRule_71939426:
        '''Defines a CodeStar Notification rule which triggers when a pull request is merged.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a56da01a2bfa53759d6ea1d05f82f37dbb5b0d0a992404afbafaabc9ee32c0a4)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        options = _NotificationRuleOptions_dff73281(
            detail_type=detail_type,
            enabled=enabled,
            notification_rule_name=notification_rule_name,
        )

        return typing.cast(_INotificationRule_71939426, jsii.invoke(self, "notifyOnPullRequestMerged", [id, target, options]))

    @jsii.member(jsii_name="onCommentOnCommit")
    def on_comment_on_commit(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines a CloudWatch event rule which triggers when a comment is made on a commit.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f176079faedd3ddd4ac31d2d0b9c018b9c32310f84d7c41ed39d586518dcb0d)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _OnEventOptions_8711b8b3(
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onCommentOnCommit", [id, options]))

    @jsii.member(jsii_name="onCommentOnPullRequest")
    def on_comment_on_pull_request(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines a CloudWatch event rule which triggers when a comment is made on a pull request.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de35095a4c36c49554ecc892ce7931ac9d6185c79597e7132048ce2c061d3497)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _OnEventOptions_8711b8b3(
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onCommentOnPullRequest", [id, options]))

    @jsii.member(jsii_name="onCommit")
    def on_commit(
        self,
        id: builtins.str,
        *,
        branches: typing.Optional[typing.Sequence[builtins.str]] = None,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines a CloudWatch event rule which triggers when a commit is pushed to a branch.

        :param id: -
        :param branches: The branch to monitor. Default: - All branches
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2ebe7cddf755b7bc82b4405e31c110bd2e3f0b1b6f641983b4d3c1b3dc0b31c)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = OnCommitOptions(
            branches=branches,
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onCommit", [id, options]))

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
            type_hints = typing.get_type_hints(_typecheckingstub__b0b93a9d5701b0dca5e904fc6edbea6970f576a0e8bc4db36b43b0aa38b81f25)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _OnEventOptions_8711b8b3(
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onEvent", [id, options]))

    @jsii.member(jsii_name="onPullRequestStateChange")
    def on_pull_request_state_change(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines a CloudWatch event rule which triggers when a pull request state is changed.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5488a133f0d0938542fe1ce849050c9127cb97f23fe22494080993548f5bf14)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _OnEventOptions_8711b8b3(
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onPullRequestStateChange", [id, options]))

    @jsii.member(jsii_name="onReferenceCreated")
    def on_reference_created(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines a CloudWatch event rule which triggers when a reference is created (i.e. a new branch/tag is created) to the repository.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7df2da21049928efb9ab3242676cc304cd8fa677f87dd8602a4ea27dfa2f402a)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _OnEventOptions_8711b8b3(
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onReferenceCreated", [id, options]))

    @jsii.member(jsii_name="onReferenceDeleted")
    def on_reference_deleted(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines a CloudWatch event rule which triggers when a reference is delete (i.e. a branch/tag is deleted) from the repository.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0446cdca88991cfa784b5f0f912638fdba89c78521b26c393af077ecefa25e05)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _OnEventOptions_8711b8b3(
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onReferenceDeleted", [id, options]))

    @jsii.member(jsii_name="onReferenceUpdated")
    def on_reference_updated(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines a CloudWatch event rule which triggers when a reference is updated (i.e. a commit is pushed to an existing or new branch) from the repository.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83d473666784cac4ba5b8e4d3cf2e3bb787317bb9cbd1801363bbf43035b300d)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _OnEventOptions_8711b8b3(
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onReferenceUpdated", [id, options]))

    @jsii.member(jsii_name="onStateChange")
    def on_state_change(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines a CloudWatch event rule which triggers when a "CodeCommit Repository State Change" event occurs.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a5f61873c1de6801c610dc52c1b0aead08c4373e86647a8107cc8b1b17daa74)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _OnEventOptions_8711b8b3(
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onStateChange", [id, options]))

    @builtins.property
    @jsii.member(jsii_name="repositoryArn")
    def repository_arn(self) -> builtins.str:
        '''The ARN of this Repository.'''
        return typing.cast(builtins.str, jsii.get(self, "repositoryArn"))

    @builtins.property
    @jsii.member(jsii_name="repositoryCloneUrlGrc")
    def repository_clone_url_grc(self) -> builtins.str:
        '''The HTTPS (GRC) clone URL.

        HTTPS (GRC) is the protocol to use with git-remote-codecommit (GRC).

        It is the recommended method for supporting connections made with federated
        access, identity providers, and temporary credentials.
        '''
        return typing.cast(builtins.str, jsii.get(self, "repositoryCloneUrlGrc"))

    @builtins.property
    @jsii.member(jsii_name="repositoryCloneUrlHttp")
    def repository_clone_url_http(self) -> builtins.str:
        '''The HTTP clone URL.'''
        return typing.cast(builtins.str, jsii.get(self, "repositoryCloneUrlHttp"))

    @builtins.property
    @jsii.member(jsii_name="repositoryCloneUrlSsh")
    def repository_clone_url_ssh(self) -> builtins.str:
        '''The SSH clone URL.'''
        return typing.cast(builtins.str, jsii.get(self, "repositoryCloneUrlSsh"))

    @builtins.property
    @jsii.member(jsii_name="repositoryName")
    def repository_name(self) -> builtins.str:
        '''The human-visible name of this Repository.'''
        return typing.cast(builtins.str, jsii.get(self, "repositoryName"))


@jsii.enum(jsii_type="aws-cdk-lib.aws_codecommit.RepositoryEventTrigger")
class RepositoryEventTrigger(enum.Enum):
    '''Repository events that will cause the trigger to run actions in another service.'''

    ALL = "ALL"
    UPDATE_REF = "UPDATE_REF"
    CREATE_REF = "CREATE_REF"
    DELETE_REF = "DELETE_REF"


@jsii.enum(jsii_type="aws-cdk-lib.aws_codecommit.RepositoryNotificationEvents")
class RepositoryNotificationEvents(enum.Enum):
    '''List of event types for AWS CodeCommit.

    :see: https://docs.aws.amazon.com/dtconsole/latest/userguide/concepts.html#events-ref-repositories
    '''

    COMMIT_COMMENT = "COMMIT_COMMENT"
    '''Trigger notication when comment made on commit.'''
    PULL_REQUEST_COMMENT = "PULL_REQUEST_COMMENT"
    '''Trigger notification when comment made on pull request.'''
    APPROVAL_STATUS_CHANGED = "APPROVAL_STATUS_CHANGED"
    '''Trigger notification when approval status changed.'''
    APPROVAL_RULE_OVERRIDDEN = "APPROVAL_RULE_OVERRIDDEN"
    '''Trigger notifications when approval rule is overridden.'''
    PULL_REQUEST_CREATED = "PULL_REQUEST_CREATED"
    '''Trigger notification when pull request created.'''
    PULL_REQUEST_SOURCE_UPDATED = "PULL_REQUEST_SOURCE_UPDATED"
    '''Trigger notification when pull request source updated.'''
    PULL_REQUEST_STATUS_CHANGED = "PULL_REQUEST_STATUS_CHANGED"
    '''Trigger notification when pull request status is changed.'''
    PULL_REQUEST_MERGED = "PULL_REQUEST_MERGED"
    '''Trigger notification when pull requset is merged.'''
    BRANCH_OR_TAG_CREATED = "BRANCH_OR_TAG_CREATED"
    '''Trigger notification when a branch or tag is created.'''
    BRANCH_OR_TAG_DELETED = "BRANCH_OR_TAG_DELETED"
    '''Trigger notification when a branch or tag is deleted.'''
    BRANCH_OR_TAG_UPDATED = "BRANCH_OR_TAG_UPDATED"
    '''Trigger notification when a branch or tag is updated.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codecommit.RepositoryNotifyOnOptions",
    jsii_struct_bases=[_NotificationRuleOptions_dff73281],
    name_mapping={
        "detail_type": "detailType",
        "enabled": "enabled",
        "notification_rule_name": "notificationRuleName",
        "events": "events",
    },
)
class RepositoryNotifyOnOptions(_NotificationRuleOptions_dff73281):
    def __init__(
        self,
        *,
        detail_type: typing.Optional[_DetailType_cf8135e7] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
        events: typing.Sequence[RepositoryNotificationEvents],
    ) -> None:
        '''Additional options to pass to the notification rule.

        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        :param events: A list of event types associated with this notification rule for CodeCommit repositories. For a complete list of event types and IDs, see Notification concepts in the Developer Tools Console User Guide.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codecommit as codecommit
            from aws_cdk import aws_codestarnotifications as codestarnotifications
            
            repository_notify_on_options = codecommit.RepositoryNotifyOnOptions(
                events=[codecommit.RepositoryNotificationEvents.COMMIT_COMMENT],
            
                # the properties below are optional
                detail_type=codestarnotifications.DetailType.BASIC,
                enabled=False,
                notification_rule_name="notificationRuleName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16fd76e74f0043c5c5c8d74817ce13ba7cb586b9bf523ff287c1613ecca5ac20)
            check_type(argname="argument detail_type", value=detail_type, expected_type=type_hints["detail_type"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument notification_rule_name", value=notification_rule_name, expected_type=type_hints["notification_rule_name"])
            check_type(argname="argument events", value=events, expected_type=type_hints["events"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "events": events,
        }
        if detail_type is not None:
            self._values["detail_type"] = detail_type
        if enabled is not None:
            self._values["enabled"] = enabled
        if notification_rule_name is not None:
            self._values["notification_rule_name"] = notification_rule_name

    @builtins.property
    def detail_type(self) -> typing.Optional[_DetailType_cf8135e7]:
        '''The level of detail to include in the notifications for this resource.

        BASIC will include only the contents of the event as it would appear in AWS CloudWatch.
        FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created.

        :default: DetailType.FULL
        '''
        result = self._values.get("detail_type")
        return typing.cast(typing.Optional[_DetailType_cf8135e7], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''The status of the notification rule.

        If the enabled is set to DISABLED, notifications aren't sent for the notification rule.

        :default: true
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def notification_rule_name(self) -> typing.Optional[builtins.str]:
        '''The name for the notification rule.

        Notification rule names must be unique in your AWS account.

        :default: - generated from the ``id``
        '''
        result = self._values.get("notification_rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def events(self) -> typing.List[RepositoryNotificationEvents]:
        '''A list of event types associated with this notification rule for CodeCommit repositories.

        For a complete list of event types and IDs, see Notification concepts in the Developer Tools Console User Guide.

        :see: https://docs.aws.amazon.com/dtconsole/latest/userguide/concepts.html#concepts-api
        '''
        result = self._values.get("events")
        assert result is not None, "Required property 'events' is missing"
        return typing.cast(typing.List[RepositoryNotificationEvents], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RepositoryNotifyOnOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codecommit.RepositoryProps",
    jsii_struct_bases=[],
    name_mapping={
        "repository_name": "repositoryName",
        "code": "code",
        "description": "description",
    },
)
class RepositoryProps:
    def __init__(
        self,
        *,
        repository_name: builtins.str,
        code: typing.Optional[Code] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param repository_name: Name of the repository. This property is required for all CodeCommit repositories.
        :param code: The contents with which to initialize the repository after it has been created. Default: - No initialization (create empty repo)
        :param description: A description of the repository. Use the description to identify the purpose of the repository. Default: - No description.

        :exampleMetadata: lit=aws-codepipeline-actions/test/integ.cfn-template-from-repo.lit.ts infused

        Example::

            # Source stage: read from repository
            repo = codecommit.Repository(stack, "TemplateRepo",
                repository_name="template-repo"
            )
            source_output = codepipeline.Artifact("SourceArtifact")
            source = cpactions.CodeCommitSourceAction(
                action_name="Source",
                repository=repo,
                output=source_output,
                trigger=cpactions.CodeCommitTrigger.POLL
            )
            source_stage = {
                "stage_name": "Source",
                "actions": [source]
            }
            
            # Deployment stage: create and deploy changeset with manual approval
            stack_name = "OurStack"
            change_set_name = "StagedChangeSet"
            
            prod_stage = {
                "stage_name": "Deploy",
                "actions": [
                    cpactions.CloudFormationCreateReplaceChangeSetAction(
                        action_name="PrepareChanges",
                        stack_name=stack_name,
                        change_set_name=change_set_name,
                        admin_permissions=True,
                        template_path=source_output.at_path("template.yaml"),
                        run_order=1
                    ),
                    cpactions.ManualApprovalAction(
                        action_name="ApproveChanges",
                        run_order=2
                    ),
                    cpactions.CloudFormationExecuteChangeSetAction(
                        action_name="ExecuteChanges",
                        stack_name=stack_name,
                        change_set_name=change_set_name,
                        run_order=3
                    )
                ]
            }
            
            codepipeline.Pipeline(stack, "Pipeline",
                stages=[source_stage, prod_stage
                ]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f5b7aba6edb1a65dfbcce23930da17cf0e6a0d64372346382ade8dd17d1ceec)
            check_type(argname="argument repository_name", value=repository_name, expected_type=type_hints["repository_name"])
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "repository_name": repository_name,
        }
        if code is not None:
            self._values["code"] = code
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def repository_name(self) -> builtins.str:
        '''Name of the repository.

        This property is required for all CodeCommit repositories.
        '''
        result = self._values.get("repository_name")
        assert result is not None, "Required property 'repository_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def code(self) -> typing.Optional[Code]:
        '''The contents with which to initialize the repository after it has been created.

        :default: - No initialization (create empty repo)
        '''
        result = self._values.get("code")
        return typing.cast(typing.Optional[Code], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the repository.

        Use the description to identify the
        purpose of the repository.

        :default: - No description.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RepositoryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codecommit.RepositoryTriggerOptions",
    jsii_struct_bases=[],
    name_mapping={
        "branches": "branches",
        "custom_data": "customData",
        "events": "events",
        "name": "name",
    },
)
class RepositoryTriggerOptions:
    def __init__(
        self,
        *,
        branches: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_data: typing.Optional[builtins.str] = None,
        events: typing.Optional[typing.Sequence[RepositoryEventTrigger]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Creates for a repository trigger to an SNS topic or Lambda function.

        :param branches: The names of the branches in the AWS CodeCommit repository that contain events that you want to include in the trigger. If you don't specify at least one branch, the trigger applies to all branches.
        :param custom_data: When an event is triggered, additional information that AWS CodeCommit includes when it sends information to the target.
        :param events: The repository events for which AWS CodeCommit sends information to the target, which you specified in the DestinationArn property.If you don't specify events, the trigger runs for all repository events.
        :param name: A name for the trigger.Triggers on a repository must have unique names.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codecommit as codecommit
            
            repository_trigger_options = codecommit.RepositoryTriggerOptions(
                branches=["branches"],
                custom_data="customData",
                events=[codecommit.RepositoryEventTrigger.ALL],
                name="name"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0dba412560c45b87b40cb60b3a994966135dd4343e862cd7d83789ad0058a928)
            check_type(argname="argument branches", value=branches, expected_type=type_hints["branches"])
            check_type(argname="argument custom_data", value=custom_data, expected_type=type_hints["custom_data"])
            check_type(argname="argument events", value=events, expected_type=type_hints["events"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if branches is not None:
            self._values["branches"] = branches
        if custom_data is not None:
            self._values["custom_data"] = custom_data
        if events is not None:
            self._values["events"] = events
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def branches(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The names of the branches in the AWS CodeCommit repository that contain events that you want to include in the trigger.

        If you don't specify at
        least one branch, the trigger applies to all branches.
        '''
        result = self._values.get("branches")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def custom_data(self) -> typing.Optional[builtins.str]:
        '''When an event is triggered, additional information that AWS CodeCommit includes when it sends information to the target.'''
        result = self._values.get("custom_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def events(self) -> typing.Optional[typing.List[RepositoryEventTrigger]]:
        '''The repository events for which AWS CodeCommit sends information to the target, which you specified in the DestinationArn property.If you don't specify events, the trigger runs for all repository events.'''
        result = self._values.get("events")
        return typing.cast(typing.Optional[typing.List[RepositoryEventTrigger]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''A name for the trigger.Triggers on a repository must have unique names.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RepositoryTriggerOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnRepository",
    "CfnRepositoryProps",
    "Code",
    "CodeConfig",
    "IRepository",
    "OnCommitOptions",
    "ReferenceEvent",
    "Repository",
    "RepositoryEventTrigger",
    "RepositoryNotificationEvents",
    "RepositoryNotifyOnOptions",
    "RepositoryProps",
    "RepositoryTriggerOptions",
]

publication.publish()

def _typecheckingstub__64c8b70ff11de55544c0f9980a825007e7719d10a7e5b40f2acf7a97e1903316(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    repository_name: builtins.str,
    code: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRepository.CodeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    repository_description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    triggers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRepository.RepositoryTriggerProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14e7c387467f372d552f803c722a33900eeead6044c503cdbb6a483f2bffeb20(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f41b60d01c2fa702da78ec1be5d872be8498ed5eda9f32e839d8336fab0bd5b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6859c317a69708aff80ba1f8fecce3dd4d7f3d6fb86832e6cff0b5dbd8fab108(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2d9aa151db0306c7144ac1b558b3e0c05b6ba724aad48d7d1cc2dd97531376f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRepository.CodeProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f9325bc159d21706aa8257fe0bbabdab9cae89a56ab234752d2dca8f1e7f144(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d0a6e36f693d4cc2a11babc985e1e5d85042ffad99b950a29a50f501027166d(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aefad5f1e3f33a8892a077db431acd9bec95241245fd5d972238256b13e99377(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnRepository.RepositoryTriggerProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d1bb9150aed730dac085187c6940e2ac51e7864e609b47673a17723ea173121(
    *,
    s3: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRepository.S3Property, typing.Dict[builtins.str, typing.Any]]],
    branch_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__791b1a38389ed344ae527a7de85d3f177e7ceb35234c227008cb04af7a291ecd(
    *,
    destination_arn: builtins.str,
    events: typing.Sequence[builtins.str],
    name: builtins.str,
    branches: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_data: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccc0f96fde3de9f745dd3bd29e280e1ca949e70419a8c39fca92cfec1f02e227(
    *,
    bucket: builtins.str,
    key: builtins.str,
    object_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40c04585281a174d6c45f3d0ebb0cbf1dd9d263edfd133ff98f6e08e9e052bb1(
    *,
    repository_name: builtins.str,
    code: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRepository.CodeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    repository_description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    triggers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRepository.RepositoryTriggerProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36447c37e024f3735b5478be259e58f349ae7d9ccb44ee4e4a18a2784b9ba16e(
    asset: _Asset_ac2a7e61,
    branch: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__598e43d07069e8231016c09115aeb8aa3804300933d3217d83823def2ca6a4f1(
    directory_path: builtins.str,
    branch: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a3f82bd9873943fb876dee699b9267856598db5c500f20e56f140afc46128f4(
    file_path: builtins.str,
    branch: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4003c87938666d148b25d601f7a14a5a2d2aae2bf4ef6a22a3d035647810652(
    scope: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea4ac2a79dbabc1d15f21b47d006d6df72efdb31ab914edd8a994b41022afbc8(
    *,
    code: typing.Union[CfnRepository.CodeProperty, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__365c5593ff83cf972d077b7c5a84fbc1b5a0265992dc07d9c11fc0b29a29216a(
    grantee: _IGrantable_71c4f5de,
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d9e6b243e05b7c6eba91182b9bd7adabc3f071225b4e3a50df8e001d1f4fa37(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a6febdc5d7cf9c0ad4956ce1b01c3943a10e93da55708f00ece4f2eb5e3afb7(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a3b246d79233ee846d1ea5d76eae3faed1da036177a20d699700bc19f4718f7(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c7942184f6ef1171bc9e0c3554be4e156be2d930de75af76e6c7194dba6915d(
    id: builtins.str,
    target: _INotificationRuleTarget_faa3b79b,
    *,
    events: typing.Sequence[RepositoryNotificationEvents],
    detail_type: typing.Optional[_DetailType_cf8135e7] = None,
    enabled: typing.Optional[builtins.bool] = None,
    notification_rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1eaa0e8d10ed3253a51fe07f30f2e5ccd87923daac9fa5cac304d64e8cd2bc73(
    id: builtins.str,
    target: _INotificationRuleTarget_faa3b79b,
    *,
    detail_type: typing.Optional[_DetailType_cf8135e7] = None,
    enabled: typing.Optional[builtins.bool] = None,
    notification_rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7bf91f05b1a4f3ae616bd9f41791280fc198c1c0da943398dda62249bb2c93d(
    id: builtins.str,
    target: _INotificationRuleTarget_faa3b79b,
    *,
    detail_type: typing.Optional[_DetailType_cf8135e7] = None,
    enabled: typing.Optional[builtins.bool] = None,
    notification_rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cafbc61c624b37c5ad3d4b8a63e817009d77858ce7b25f3e44bba75d8b2c826c(
    id: builtins.str,
    target: _INotificationRuleTarget_faa3b79b,
    *,
    detail_type: typing.Optional[_DetailType_cf8135e7] = None,
    enabled: typing.Optional[builtins.bool] = None,
    notification_rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0275a2e8104bae4bd7ac1bba2e30688464d013a5007f7602a9ea90f4408842fc(
    id: builtins.str,
    target: _INotificationRuleTarget_faa3b79b,
    *,
    detail_type: typing.Optional[_DetailType_cf8135e7] = None,
    enabled: typing.Optional[builtins.bool] = None,
    notification_rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6248afe48e2fb868c294f63ac413c00382e7856dc1949f9226aad20932c7e7e5(
    id: builtins.str,
    target: _INotificationRuleTarget_faa3b79b,
    *,
    detail_type: typing.Optional[_DetailType_cf8135e7] = None,
    enabled: typing.Optional[builtins.bool] = None,
    notification_rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f02ad2ac0201a88eb92c38b6798b71bcc5a0c60f935ccccfd798c221251e41df(
    id: builtins.str,
    target: _INotificationRuleTarget_faa3b79b,
    *,
    detail_type: typing.Optional[_DetailType_cf8135e7] = None,
    enabled: typing.Optional[builtins.bool] = None,
    notification_rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a979cb7a485f86b22849a4dd125f67228ce5778a7cf334f786600ef50b4bcb80(
    id: builtins.str,
    target: _INotificationRuleTarget_faa3b79b,
    *,
    detail_type: typing.Optional[_DetailType_cf8135e7] = None,
    enabled: typing.Optional[builtins.bool] = None,
    notification_rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b13dbc0afad5a8310c818d81730321b5d30c626697d8b2da78f99e2fd1bc7a2(
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

def _typecheckingstub__022a2d7879b191ea4d30f968e4c0507a65f74cb5655b3e01025c411d5a87d764(
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

def _typecheckingstub__c0d481bc7c4182a1ac18ea2989bcaa2496cb87321e12fc1d4c1199f6c9725fa9(
    id: builtins.str,
    *,
    branches: typing.Optional[typing.Sequence[builtins.str]] = None,
    target: typing.Optional[_IRuleTarget_7a91f454] = None,
    cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6f54ec4ba5273f31ec8895010478e4112d943903cb729374b88ff19d8d2cbbb(
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

def _typecheckingstub__cd475d88fc4c78b023fb9486283e5b3c70aa9e5bc8198d12f2d6258e07211c05(
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

def _typecheckingstub__0910d5c390fbbee842a81d3014cb2cbc92f66be0788ad6afdbd8d33537f5fff6(
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

def _typecheckingstub__dcd3a4ba200e7a391250089adbbdae2d47ddef364737384821b9f31b6264315c(
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

def _typecheckingstub__0aee5dce826833691e86aae6c2a6d46fb6d2653dcf57d20baee5422625ba26e3(
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

def _typecheckingstub__ec4a2730813e663960c4c8d8a730817b32d936daf8c8ac9bd2ccfedb72150e2c(
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

def _typecheckingstub__c53b1f18ce4d88514601fab8586927ad977e89525fe4ce21ca79eee655396c1d(
    *,
    cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
    target: typing.Optional[_IRuleTarget_7a91f454] = None,
    branches: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc18226d2621b909e0802baaec299567def39762c6bf07510ef197899ff96a91(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    repository_name: builtins.str,
    code: typing.Optional[Code] = None,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3981dcb255b9a3266cc0fc6d2890e5a7fef96f5894a4ef967ff666e58f72833(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    repository_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81bca08f72268202d3b364831715be5587852151603627292a8e61129e37c3c0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    repository_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bce1acfc9824ad93658ba014d62079e398555716fd9c87708b05022831b1b038(
    _scope: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7402788e4dbfde5dc7ec7b32089dea4a8dc1cb74bc501e6fa6508c70c4d8ded(
    grantee: _IGrantable_71c4f5de,
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbbcecbc7faeddbda99d49cffd055e8154005631aa698172977c6e4db28ac599(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79efe60503b55cc3a5f2df365dc0093da149f058148cc261dc626ddfc9d2f4df(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3458cc082e7e4e18874ae54159c1143c8d40951328feef885af0a725811c1938(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e51541fedf5c8bb4467983a2551ed5f9efa788750c8ebec9fbcf9aaeeb197dca(
    id: builtins.str,
    target: _INotificationRuleTarget_faa3b79b,
    *,
    detail_type: typing.Optional[_DetailType_cf8135e7] = None,
    enabled: typing.Optional[builtins.bool] = None,
    notification_rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dbf9817defa3c5754b555f652afc4ba61c38e30a594dad01abc68b7850d81ee(
    arn: builtins.str,
    *,
    branches: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_data: typing.Optional[builtins.str] = None,
    events: typing.Optional[typing.Sequence[RepositoryEventTrigger]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2749a2587821387b871505c0408414b596d663e34cdcf4cf4680c6ea428ab696(
    id: builtins.str,
    target: _INotificationRuleTarget_faa3b79b,
    *,
    events: typing.Sequence[RepositoryNotificationEvents],
    detail_type: typing.Optional[_DetailType_cf8135e7] = None,
    enabled: typing.Optional[builtins.bool] = None,
    notification_rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e63d1ce633a4f4266a796f6cdb67b39a645cc34554e1565e442106e47410e044(
    id: builtins.str,
    target: _INotificationRuleTarget_faa3b79b,
    *,
    detail_type: typing.Optional[_DetailType_cf8135e7] = None,
    enabled: typing.Optional[builtins.bool] = None,
    notification_rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc8c6b048a43947387c3a5e34fc554543aa2e3e1d20768589eed5d96e44164a3(
    id: builtins.str,
    target: _INotificationRuleTarget_faa3b79b,
    *,
    detail_type: typing.Optional[_DetailType_cf8135e7] = None,
    enabled: typing.Optional[builtins.bool] = None,
    notification_rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb870921bbb9ab4ed9e1a62ba8ef6bf25612d59da0df03c9c1baa71010433baf(
    id: builtins.str,
    target: _INotificationRuleTarget_faa3b79b,
    *,
    detail_type: typing.Optional[_DetailType_cf8135e7] = None,
    enabled: typing.Optional[builtins.bool] = None,
    notification_rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__590bcfde747b37888d42f2e95418df6766d69b978c2275b81a2d68c189377d31(
    id: builtins.str,
    target: _INotificationRuleTarget_faa3b79b,
    *,
    detail_type: typing.Optional[_DetailType_cf8135e7] = None,
    enabled: typing.Optional[builtins.bool] = None,
    notification_rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8945454cd0688bf69a49ca491edd2ce985eab8c28b695a4392ae84fbba40b96f(
    id: builtins.str,
    target: _INotificationRuleTarget_faa3b79b,
    *,
    detail_type: typing.Optional[_DetailType_cf8135e7] = None,
    enabled: typing.Optional[builtins.bool] = None,
    notification_rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9584aecb592a6d74f000818947c6960318c665568cef4b2803439fb35a634f69(
    id: builtins.str,
    target: _INotificationRuleTarget_faa3b79b,
    *,
    detail_type: typing.Optional[_DetailType_cf8135e7] = None,
    enabled: typing.Optional[builtins.bool] = None,
    notification_rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a56da01a2bfa53759d6ea1d05f82f37dbb5b0d0a992404afbafaabc9ee32c0a4(
    id: builtins.str,
    target: _INotificationRuleTarget_faa3b79b,
    *,
    detail_type: typing.Optional[_DetailType_cf8135e7] = None,
    enabled: typing.Optional[builtins.bool] = None,
    notification_rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f176079faedd3ddd4ac31d2d0b9c018b9c32310f84d7c41ed39d586518dcb0d(
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

def _typecheckingstub__de35095a4c36c49554ecc892ce7931ac9d6185c79597e7132048ce2c061d3497(
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

def _typecheckingstub__d2ebe7cddf755b7bc82b4405e31c110bd2e3f0b1b6f641983b4d3c1b3dc0b31c(
    id: builtins.str,
    *,
    branches: typing.Optional[typing.Sequence[builtins.str]] = None,
    target: typing.Optional[_IRuleTarget_7a91f454] = None,
    cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0b93a9d5701b0dca5e904fc6edbea6970f576a0e8bc4db36b43b0aa38b81f25(
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

def _typecheckingstub__a5488a133f0d0938542fe1ce849050c9127cb97f23fe22494080993548f5bf14(
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

def _typecheckingstub__7df2da21049928efb9ab3242676cc304cd8fa677f87dd8602a4ea27dfa2f402a(
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

def _typecheckingstub__0446cdca88991cfa784b5f0f912638fdba89c78521b26c393af077ecefa25e05(
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

def _typecheckingstub__83d473666784cac4ba5b8e4d3cf2e3bb787317bb9cbd1801363bbf43035b300d(
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

def _typecheckingstub__1a5f61873c1de6801c610dc52c1b0aead08c4373e86647a8107cc8b1b17daa74(
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

def _typecheckingstub__16fd76e74f0043c5c5c8d74817ce13ba7cb586b9bf523ff287c1613ecca5ac20(
    *,
    detail_type: typing.Optional[_DetailType_cf8135e7] = None,
    enabled: typing.Optional[builtins.bool] = None,
    notification_rule_name: typing.Optional[builtins.str] = None,
    events: typing.Sequence[RepositoryNotificationEvents],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f5b7aba6edb1a65dfbcce23930da17cf0e6a0d64372346382ade8dd17d1ceec(
    *,
    repository_name: builtins.str,
    code: typing.Optional[Code] = None,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dba412560c45b87b40cb60b3a994966135dd4343e862cd7d83789ad0058a928(
    *,
    branches: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_data: typing.Optional[builtins.str] = None,
    events: typing.Optional[typing.Sequence[RepositoryEventTrigger]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
