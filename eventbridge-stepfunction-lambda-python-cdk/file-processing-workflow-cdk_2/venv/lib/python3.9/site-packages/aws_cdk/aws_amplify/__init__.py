'''
# AWS Amplify Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_amplify as amplify
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Amplify construct libraries](https://constructs.dev/search?q=amplify)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Amplify resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Amplify.html) directly.

> An experimental construct library for this service is available in preview. Since it is not stable yet, it is distributed
> as a separate package so that you can pin its version independently of the rest of the CDK. See the package:
>
> <span class="package-reference">@aws-cdk/aws-amplify-alpha</span>

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Amplify](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Amplify.html).

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
class CfnApp(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_amplify.CfnApp",
):
    '''The AWS::Amplify::App resource specifies Apps in Amplify Hosting.

    An App is a collection of branches.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_amplify as amplify
        
        cfn_app = amplify.CfnApp(self, "MyCfnApp",
            name="name",
        
            # the properties below are optional
            access_token="accessToken",
            auto_branch_creation_config=amplify.CfnApp.AutoBranchCreationConfigProperty(
                auto_branch_creation_patterns=["autoBranchCreationPatterns"],
                basic_auth_config=amplify.CfnApp.BasicAuthConfigProperty(
                    enable_basic_auth=False,
                    password="password",
                    username="username"
                ),
                build_spec="buildSpec",
                enable_auto_branch_creation=False,
                enable_auto_build=False,
                enable_performance_mode=False,
                enable_pull_request_preview=False,
                environment_variables=[amplify.CfnApp.EnvironmentVariableProperty(
                    name="name",
                    value="value"
                )],
                framework="framework",
                pull_request_environment_name="pullRequestEnvironmentName",
                stage="stage"
            ),
            basic_auth_config=amplify.CfnApp.BasicAuthConfigProperty(
                enable_basic_auth=False,
                password="password",
                username="username"
            ),
            build_spec="buildSpec",
            custom_headers="customHeaders",
            custom_rules=[amplify.CfnApp.CustomRuleProperty(
                source="source",
                target="target",
        
                # the properties below are optional
                condition="condition",
                status="status"
            )],
            description="description",
            enable_branch_auto_deletion=False,
            environment_variables=[amplify.CfnApp.EnvironmentVariableProperty(
                name="name",
                value="value"
            )],
            iam_service_role="iamServiceRole",
            oauth_token="oauthToken",
            platform="platform",
            repository="repository",
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
        access_token: typing.Optional[builtins.str] = None,
        auto_branch_creation_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApp.AutoBranchCreationConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        basic_auth_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApp.BasicAuthConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        build_spec: typing.Optional[builtins.str] = None,
        custom_headers: typing.Optional[builtins.str] = None,
        custom_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApp.CustomRuleProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        enable_branch_auto_deletion: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        environment_variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApp.EnvironmentVariableProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        iam_service_role: typing.Optional[builtins.str] = None,
        oauth_token: typing.Optional[builtins.str] = None,
        platform: typing.Optional[builtins.str] = None,
        repository: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name for an Amplify app. *Length Constraints:* Minimum length of 1. Maximum length of 255. *Pattern:* (?s).+
        :param access_token: The personal access token for a GitHub repository for an Amplify app. The personal access token is used to authorize access to a GitHub repository using the Amplify GitHub App. The token is not stored. Use ``AccessToken`` for GitHub repositories only. To authorize access to a repository provider such as Bitbucket or CodeCommit, use ``OauthToken`` . You must specify either ``AccessToken`` or ``OauthToken`` when you create a new app. Existing Amplify apps deployed from a GitHub repository using OAuth continue to work with CI/CD. However, we strongly recommend that you migrate these apps to use the GitHub App. For more information, see `Migrating an existing OAuth app to the Amplify GitHub App <https://docs.aws.amazon.com/amplify/latest/userguide/setting-up-GitHub-access.html#migrating-to-github-app-auth>`_ in the *Amplify User Guide* . *Length Constraints:* Minimum length of 1. Maximum length of 255.
        :param auto_branch_creation_config: Sets the configuration for your automatic branch creation.
        :param basic_auth_config: The credentials for basic authorization for an Amplify app. You must base64-encode the authorization credentials and provide them in the format ``user:password`` .
        :param build_spec: The build specification (build spec) for an Amplify app. *Length Constraints:* Minimum length of 1. Maximum length of 25000. *Pattern:* (?s).+
        :param custom_headers: The custom HTTP headers for an Amplify app. *Length Constraints:* Minimum length of 0. Maximum length of 25000. *Pattern:* (?s).*
        :param custom_rules: The custom rewrite and redirect rules for an Amplify app.
        :param description: The description for an Amplify app. *Length Constraints:* Maximum length of 1000. *Pattern:* (?s).*
        :param enable_branch_auto_deletion: Automatically disconnect a branch in Amplify Hosting when you delete a branch from your Git repository.
        :param environment_variables: The environment variables map for an Amplify app. For a list of the environment variables that are accessible to Amplify by default, see `Amplify Environment variables <https://docs.aws.amazon.com/amplify/latest/userguide/amplify-console-environment-variables.html>`_ in the *Amplify Hosting User Guide* .
        :param iam_service_role: The AWS Identity and Access Management (IAM) service role for the Amazon Resource Name (ARN) of the Amplify app. *Length Constraints:* Minimum length of 0. Maximum length of 1000. *Pattern:* (?s).*
        :param oauth_token: The OAuth token for a third-party source control system for an Amplify app. The OAuth token is used to create a webhook and a read-only deploy key using SSH cloning. The OAuth token is not stored. Use ``OauthToken`` for repository providers other than GitHub, such as Bitbucket or CodeCommit. To authorize access to GitHub as your repository provider, use ``AccessToken`` . You must specify either ``OauthToken`` or ``AccessToken`` when you create a new app. Existing Amplify apps deployed from a GitHub repository using OAuth continue to work with CI/CD. However, we strongly recommend that you migrate these apps to use the GitHub App. For more information, see `Migrating an existing OAuth app to the Amplify GitHub App <https://docs.aws.amazon.com/amplify/latest/userguide/setting-up-GitHub-access.html#migrating-to-github-app-auth>`_ in the *Amplify User Guide* . *Length Constraints:* Maximum length of 1000. *Pattern:* (?s).*
        :param platform: The platform for the Amplify app. For a static app, set the platform type to ``WEB`` . For a dynamic server-side rendered (SSR) app, set the platform type to ``WEB_COMPUTE`` . For an app requiring Amplify Hosting's original SSR support only, set the platform type to ``WEB_DYNAMIC`` .
        :param repository: The repository for an Amplify app. *Pattern:* (?s).*
        :param tags: The tag for an Amplify app.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dc8d772047a068d22a76d907b344356448c6a26d23e419ed69cc622d02781ee)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAppProps(
            name=name,
            access_token=access_token,
            auto_branch_creation_config=auto_branch_creation_config,
            basic_auth_config=basic_auth_config,
            build_spec=build_spec,
            custom_headers=custom_headers,
            custom_rules=custom_rules,
            description=description,
            enable_branch_auto_deletion=enable_branch_auto_deletion,
            environment_variables=environment_variables,
            iam_service_role=iam_service_role,
            oauth_token=oauth_token,
            platform=platform,
            repository=repository,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86430113f75e093324439a08235b05caf66a071c9480bffb7d367fe6c3214308)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0a907b90c3eb27e674a931172d848655ba40852fd440d8525c2a6819779ce4b4)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAppId")
    def attr_app_id(self) -> builtins.str:
        '''Unique Id for the Amplify App.

        :cloudformationAttribute: AppId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAppId"))

    @builtins.property
    @jsii.member(jsii_name="attrAppName")
    def attr_app_name(self) -> builtins.str:
        '''Name for the Amplify App.

        :cloudformationAttribute: AppName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAppName"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''ARN for the Amplify App.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrDefaultDomain")
    def attr_default_domain(self) -> builtins.str:
        '''Default domain for the Amplify App.

        :cloudformationAttribute: DefaultDomain
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDefaultDomain"))

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
        '''The name for an Amplify app.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdfa7791969585e493dc40e8ceb68db0f3860ba941690b779c4d50f75aebbbd7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="accessToken")
    def access_token(self) -> typing.Optional[builtins.str]:
        '''The personal access token for a GitHub repository for an Amplify app.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessToken"))

    @access_token.setter
    def access_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a34b8e83d25c0c26838033ec8d45694e410c5c28d0bf83263b9f9d0942496b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessToken", value)

    @builtins.property
    @jsii.member(jsii_name="autoBranchCreationConfig")
    def auto_branch_creation_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApp.AutoBranchCreationConfigProperty"]]:
        '''Sets the configuration for your automatic branch creation.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApp.AutoBranchCreationConfigProperty"]], jsii.get(self, "autoBranchCreationConfig"))

    @auto_branch_creation_config.setter
    def auto_branch_creation_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApp.AutoBranchCreationConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f38a76185a264f75d2add648c8308477d491dddde9804ac7dfbe3bb22d6ea352)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoBranchCreationConfig", value)

    @builtins.property
    @jsii.member(jsii_name="basicAuthConfig")
    def basic_auth_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApp.BasicAuthConfigProperty"]]:
        '''The credentials for basic authorization for an Amplify app.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApp.BasicAuthConfigProperty"]], jsii.get(self, "basicAuthConfig"))

    @basic_auth_config.setter
    def basic_auth_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApp.BasicAuthConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c88becb37a9dd8239d9ff6aff490658ca182aff7fcab83a21ab6054c309a8432)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "basicAuthConfig", value)

    @builtins.property
    @jsii.member(jsii_name="buildSpec")
    def build_spec(self) -> typing.Optional[builtins.str]:
        '''The build specification (build spec) for an Amplify app.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "buildSpec"))

    @build_spec.setter
    def build_spec(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8d9c326dc2b610757cecc45608945b716d8ea6af4111bd656fb2927aa80d26c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buildSpec", value)

    @builtins.property
    @jsii.member(jsii_name="customHeaders")
    def custom_headers(self) -> typing.Optional[builtins.str]:
        '''The custom HTTP headers for an Amplify app.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customHeaders"))

    @custom_headers.setter
    def custom_headers(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__623b6d97b6b1967c76a0782c9ba61b276ee5ff570dad9ab0003baf0626317805)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="customRules")
    def custom_rules(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApp.CustomRuleProperty"]]]]:
        '''The custom rewrite and redirect rules for an Amplify app.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApp.CustomRuleProperty"]]]], jsii.get(self, "customRules"))

    @custom_rules.setter
    def custom_rules(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApp.CustomRuleProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24f88ebda938286ba2d8ff036b7dcf3cb20a38f782c34c0484b66a2b916ac21f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customRules", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description for an Amplify app.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f271970963b091aefd84c3ab3d2b252d3dca5e4789a892ae905ec8fbf52784e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="enableBranchAutoDeletion")
    def enable_branch_auto_deletion(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Automatically disconnect a branch in Amplify Hosting when you delete a branch from your Git repository.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enableBranchAutoDeletion"))

    @enable_branch_auto_deletion.setter
    def enable_branch_auto_deletion(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2dc6d20be8c1648863255ae7968af724a5e56aadb1ddf86b4126b4d6fc096bb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableBranchAutoDeletion", value)

    @builtins.property
    @jsii.member(jsii_name="environmentVariables")
    def environment_variables(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApp.EnvironmentVariableProperty"]]]]:
        '''The environment variables map for an Amplify app.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApp.EnvironmentVariableProperty"]]]], jsii.get(self, "environmentVariables"))

    @environment_variables.setter
    def environment_variables(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApp.EnvironmentVariableProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ffb3244739d356fab1ba7899722798d4558303d9d3e2a3caaa138b21a86181b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentVariables", value)

    @builtins.property
    @jsii.member(jsii_name="iamServiceRole")
    def iam_service_role(self) -> typing.Optional[builtins.str]:
        '''The AWS Identity and Access Management (IAM) service role for the Amazon Resource Name (ARN) of the Amplify app.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamServiceRole"))

    @iam_service_role.setter
    def iam_service_role(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__378909021f9642b2e612e1ecd4b62069a17df2eef9f3461fa46cd5337a44dae9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamServiceRole", value)

    @builtins.property
    @jsii.member(jsii_name="oauthToken")
    def oauth_token(self) -> typing.Optional[builtins.str]:
        '''The OAuth token for a third-party source control system for an Amplify app.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauthToken"))

    @oauth_token.setter
    def oauth_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4f1a9875121cc669c475a05f9524db58d7e32e0b0134143bf750ceca8d2d6ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthToken", value)

    @builtins.property
    @jsii.member(jsii_name="platform")
    def platform(self) -> typing.Optional[builtins.str]:
        '''The platform for the Amplify app.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "platform"))

    @platform.setter
    def platform(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67a5adcc133fbd9a8b5cd704d8959ba2006e08994f5a37195cf965503b97fa28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "platform", value)

    @builtins.property
    @jsii.member(jsii_name="repository")
    def repository(self) -> typing.Optional[builtins.str]:
        '''The repository for an Amplify app.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repository"))

    @repository.setter
    def repository(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77810a604b4d1c18de17ffbf1fde3969ab827d2e901598428f49ecc37a16b28d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repository", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tag for an Amplify app.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8df0df5db275f36f972fd610984f160f89f4bdc11545dfef3ffa8b0e4dda0842)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplify.CfnApp.AutoBranchCreationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "auto_branch_creation_patterns": "autoBranchCreationPatterns",
            "basic_auth_config": "basicAuthConfig",
            "build_spec": "buildSpec",
            "enable_auto_branch_creation": "enableAutoBranchCreation",
            "enable_auto_build": "enableAutoBuild",
            "enable_performance_mode": "enablePerformanceMode",
            "enable_pull_request_preview": "enablePullRequestPreview",
            "environment_variables": "environmentVariables",
            "framework": "framework",
            "pull_request_environment_name": "pullRequestEnvironmentName",
            "stage": "stage",
        },
    )
    class AutoBranchCreationConfigProperty:
        def __init__(
            self,
            *,
            auto_branch_creation_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            basic_auth_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApp.BasicAuthConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            build_spec: typing.Optional[builtins.str] = None,
            enable_auto_branch_creation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            enable_auto_build: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            enable_performance_mode: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            enable_pull_request_preview: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            environment_variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApp.EnvironmentVariableProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            framework: typing.Optional[builtins.str] = None,
            pull_request_environment_name: typing.Optional[builtins.str] = None,
            stage: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Use the AutoBranchCreationConfig property type to automatically create branches that match a certain pattern.

            :param auto_branch_creation_patterns: Automated branch creation glob patterns for the Amplify app.
            :param basic_auth_config: Sets password protection for your auto created branch.
            :param build_spec: The build specification (build spec) for the autocreated branch. *Length Constraints:* Minimum length of 1. Maximum length of 25000.
            :param enable_auto_branch_creation: Enables automated branch creation for the Amplify app.
            :param enable_auto_build: Enables auto building for the auto created branch.
            :param enable_performance_mode: Enables performance mode for the branch. Performance mode optimizes for faster hosting performance by keeping content cached at the edge for a longer interval. When performance mode is enabled, hosting configuration or code changes can take up to 10 minutes to roll out.
            :param enable_pull_request_preview: Sets whether pull request previews are enabled for each branch that Amplify Hosting automatically creates for your app. Amplify creates previews by deploying your app to a unique URL whenever a pull request is opened for the branch. Development and QA teams can use this preview to test the pull request before it's merged into a production or integration branch. To provide backend support for your preview, Amplify Hosting automatically provisions a temporary backend environment that it deletes when the pull request is closed. If you want to specify a dedicated backend environment for your previews, use the ``PullRequestEnvironmentName`` property. For more information, see `Web Previews <https://docs.aws.amazon.com/amplify/latest/userguide/pr-previews.html>`_ in the *AWS Amplify Hosting User Guide* .
            :param environment_variables: Environment variables for the auto created branch.
            :param framework: The framework for the autocreated branch.
            :param pull_request_environment_name: If pull request previews are enabled, you can use this property to specify a dedicated backend environment for your previews. For example, you could specify an environment named ``prod`` , ``test`` , or ``dev`` that you initialized with the Amplify CLI. To enable pull request previews, set the ``EnablePullRequestPreview`` property to ``true`` . If you don't specify an environment, Amplify Hosting provides backend support for each preview by automatically provisioning a temporary backend environment. Amplify deletes this environment when the pull request is closed. For more information about creating backend environments, see `Feature Branch Deployments and Team Workflows <https://docs.aws.amazon.com/amplify/latest/userguide/multi-environments.html>`_ in the *AWS Amplify Hosting User Guide* . *Length Constraints:* Maximum length of 20. *Pattern:* (?s).*
            :param stage: Stage for the auto created branch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplify as amplify
                
                auto_branch_creation_config_property = amplify.CfnApp.AutoBranchCreationConfigProperty(
                    auto_branch_creation_patterns=["autoBranchCreationPatterns"],
                    basic_auth_config=amplify.CfnApp.BasicAuthConfigProperty(
                        enable_basic_auth=False,
                        password="password",
                        username="username"
                    ),
                    build_spec="buildSpec",
                    enable_auto_branch_creation=False,
                    enable_auto_build=False,
                    enable_performance_mode=False,
                    enable_pull_request_preview=False,
                    environment_variables=[amplify.CfnApp.EnvironmentVariableProperty(
                        name="name",
                        value="value"
                    )],
                    framework="framework",
                    pull_request_environment_name="pullRequestEnvironmentName",
                    stage="stage"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9f2d37f548867fe52cc8c3c461e27ca7411af070358e14a397f593a46ce69d2f)
                check_type(argname="argument auto_branch_creation_patterns", value=auto_branch_creation_patterns, expected_type=type_hints["auto_branch_creation_patterns"])
                check_type(argname="argument basic_auth_config", value=basic_auth_config, expected_type=type_hints["basic_auth_config"])
                check_type(argname="argument build_spec", value=build_spec, expected_type=type_hints["build_spec"])
                check_type(argname="argument enable_auto_branch_creation", value=enable_auto_branch_creation, expected_type=type_hints["enable_auto_branch_creation"])
                check_type(argname="argument enable_auto_build", value=enable_auto_build, expected_type=type_hints["enable_auto_build"])
                check_type(argname="argument enable_performance_mode", value=enable_performance_mode, expected_type=type_hints["enable_performance_mode"])
                check_type(argname="argument enable_pull_request_preview", value=enable_pull_request_preview, expected_type=type_hints["enable_pull_request_preview"])
                check_type(argname="argument environment_variables", value=environment_variables, expected_type=type_hints["environment_variables"])
                check_type(argname="argument framework", value=framework, expected_type=type_hints["framework"])
                check_type(argname="argument pull_request_environment_name", value=pull_request_environment_name, expected_type=type_hints["pull_request_environment_name"])
                check_type(argname="argument stage", value=stage, expected_type=type_hints["stage"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if auto_branch_creation_patterns is not None:
                self._values["auto_branch_creation_patterns"] = auto_branch_creation_patterns
            if basic_auth_config is not None:
                self._values["basic_auth_config"] = basic_auth_config
            if build_spec is not None:
                self._values["build_spec"] = build_spec
            if enable_auto_branch_creation is not None:
                self._values["enable_auto_branch_creation"] = enable_auto_branch_creation
            if enable_auto_build is not None:
                self._values["enable_auto_build"] = enable_auto_build
            if enable_performance_mode is not None:
                self._values["enable_performance_mode"] = enable_performance_mode
            if enable_pull_request_preview is not None:
                self._values["enable_pull_request_preview"] = enable_pull_request_preview
            if environment_variables is not None:
                self._values["environment_variables"] = environment_variables
            if framework is not None:
                self._values["framework"] = framework
            if pull_request_environment_name is not None:
                self._values["pull_request_environment_name"] = pull_request_environment_name
            if stage is not None:
                self._values["stage"] = stage

        @builtins.property
        def auto_branch_creation_patterns(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''Automated branch creation glob patterns for the Amplify app.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-autobranchcreationpatterns
            '''
            result = self._values.get("auto_branch_creation_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def basic_auth_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApp.BasicAuthConfigProperty"]]:
            '''Sets password protection for your auto created branch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-basicauthconfig
            '''
            result = self._values.get("basic_auth_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApp.BasicAuthConfigProperty"]], result)

        @builtins.property
        def build_spec(self) -> typing.Optional[builtins.str]:
            '''The build specification (build spec) for the autocreated branch.

            *Length Constraints:* Minimum length of 1. Maximum length of 25000.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-buildspec
            '''
            result = self._values.get("build_spec")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def enable_auto_branch_creation(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Enables automated branch creation for the Amplify app.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-enableautobranchcreation
            '''
            result = self._values.get("enable_auto_branch_creation")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def enable_auto_build(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Enables auto building for the auto created branch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-enableautobuild
            '''
            result = self._values.get("enable_auto_build")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def enable_performance_mode(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Enables performance mode for the branch.

            Performance mode optimizes for faster hosting performance by keeping content cached at the edge for a longer interval. When performance mode is enabled, hosting configuration or code changes can take up to 10 minutes to roll out.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-enableperformancemode
            '''
            result = self._values.get("enable_performance_mode")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def enable_pull_request_preview(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Sets whether pull request previews are enabled for each branch that Amplify Hosting automatically creates for your app.

            Amplify creates previews by deploying your app to a unique URL whenever a pull request is opened for the branch. Development and QA teams can use this preview to test the pull request before it's merged into a production or integration branch.

            To provide backend support for your preview, Amplify Hosting automatically provisions a temporary backend environment that it deletes when the pull request is closed. If you want to specify a dedicated backend environment for your previews, use the ``PullRequestEnvironmentName`` property.

            For more information, see `Web Previews <https://docs.aws.amazon.com/amplify/latest/userguide/pr-previews.html>`_ in the *AWS Amplify Hosting User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-enablepullrequestpreview
            '''
            result = self._values.get("enable_pull_request_preview")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def environment_variables(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApp.EnvironmentVariableProperty"]]]]:
            '''Environment variables for the auto created branch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-environmentvariables
            '''
            result = self._values.get("environment_variables")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApp.EnvironmentVariableProperty"]]]], result)

        @builtins.property
        def framework(self) -> typing.Optional[builtins.str]:
            '''The framework for the autocreated branch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-framework
            '''
            result = self._values.get("framework")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def pull_request_environment_name(self) -> typing.Optional[builtins.str]:
            '''If pull request previews are enabled, you can use this property to specify a dedicated backend environment for your previews.

            For example, you could specify an environment named ``prod`` , ``test`` , or ``dev`` that you initialized with the Amplify CLI.

            To enable pull request previews, set the ``EnablePullRequestPreview`` property to ``true`` .

            If you don't specify an environment, Amplify Hosting provides backend support for each preview by automatically provisioning a temporary backend environment. Amplify deletes this environment when the pull request is closed.

            For more information about creating backend environments, see `Feature Branch Deployments and Team Workflows <https://docs.aws.amazon.com/amplify/latest/userguide/multi-environments.html>`_ in the *AWS Amplify Hosting User Guide* .

            *Length Constraints:* Maximum length of 20.

            *Pattern:* (?s).*

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-pullrequestenvironmentname
            '''
            result = self._values.get("pull_request_environment_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def stage(self) -> typing.Optional[builtins.str]:
            '''Stage for the auto created branch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html#cfn-amplify-app-autobranchcreationconfig-stage
            '''
            result = self._values.get("stage")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoBranchCreationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplify.CfnApp.BasicAuthConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enable_basic_auth": "enableBasicAuth",
            "password": "password",
            "username": "username",
        },
    )
    class BasicAuthConfigProperty:
        def __init__(
            self,
            *,
            enable_basic_auth: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            password: typing.Optional[builtins.str] = None,
            username: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Use the BasicAuthConfig property type to set password protection at an app level to all your branches.

            :param enable_basic_auth: Enables basic authorization for the Amplify app's branches.
            :param password: The password for basic authorization. *Length Constraints:* Minimum length of 1. Maximum length of 255.
            :param username: The user name for basic authorization. *Length Constraints:* Minimum length of 1. Maximum length of 255.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-basicauthconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplify as amplify
                
                basic_auth_config_property = amplify.CfnApp.BasicAuthConfigProperty(
                    enable_basic_auth=False,
                    password="password",
                    username="username"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__44bbd6c7457829d13279657590a4d74f5306d440e4549b9168c72df5cff67af9)
                check_type(argname="argument enable_basic_auth", value=enable_basic_auth, expected_type=type_hints["enable_basic_auth"])
                check_type(argname="argument password", value=password, expected_type=type_hints["password"])
                check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enable_basic_auth is not None:
                self._values["enable_basic_auth"] = enable_basic_auth
            if password is not None:
                self._values["password"] = password
            if username is not None:
                self._values["username"] = username

        @builtins.property
        def enable_basic_auth(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Enables basic authorization for the Amplify app's branches.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-basicauthconfig.html#cfn-amplify-app-basicauthconfig-enablebasicauth
            '''
            result = self._values.get("enable_basic_auth")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def password(self) -> typing.Optional[builtins.str]:
            '''The password for basic authorization.

            *Length Constraints:* Minimum length of 1. Maximum length of 255.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-basicauthconfig.html#cfn-amplify-app-basicauthconfig-password
            '''
            result = self._values.get("password")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def username(self) -> typing.Optional[builtins.str]:
            '''The user name for basic authorization.

            *Length Constraints:* Minimum length of 1. Maximum length of 255.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-basicauthconfig.html#cfn-amplify-app-basicauthconfig-username
            '''
            result = self._values.get("username")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BasicAuthConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplify.CfnApp.CustomRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "source": "source",
            "target": "target",
            "condition": "condition",
            "status": "status",
        },
    )
    class CustomRuleProperty:
        def __init__(
            self,
            *,
            source: builtins.str,
            target: builtins.str,
            condition: typing.Optional[builtins.str] = None,
            status: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The CustomRule property type allows you to specify redirects, rewrites, and reverse proxies.

            Redirects enable a web app to reroute navigation from one URL to another.

            :param source: The source pattern for a URL rewrite or redirect rule. *Length Constraints:* Minimum length of 1. Maximum length of 2048. *Pattern:* (?s).+
            :param target: The target pattern for a URL rewrite or redirect rule. *Length Constraints:* Minimum length of 1. Maximum length of 2048. *Pattern:* (?s).+
            :param condition: The condition for a URL rewrite or redirect rule, such as a country code. *Length Constraints:* Minimum length of 0. Maximum length of 2048. *Pattern:* (?s).*
            :param status: The status code for a URL rewrite or redirect rule. - **200** - Represents a 200 rewrite rule. - **301** - Represents a 301 (moved pemanently) redirect rule. This and all future requests should be directed to the target URL. - **302** - Represents a 302 temporary redirect rule. - **404** - Represents a 404 redirect rule. - **404-200** - Represents a 404 rewrite rule. *Length Constraints:* Minimum length of 3. Maximum length of 7. *Pattern:* .{3,7}

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-customrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplify as amplify
                
                custom_rule_property = amplify.CfnApp.CustomRuleProperty(
                    source="source",
                    target="target",
                
                    # the properties below are optional
                    condition="condition",
                    status="status"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ca2210b3c179b77af8d9da860b10e6e93aafae9d4e268f8999f6ce252c3f2363)
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
                check_type(argname="argument target", value=target, expected_type=type_hints["target"])
                check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "source": source,
                "target": target,
            }
            if condition is not None:
                self._values["condition"] = condition
            if status is not None:
                self._values["status"] = status

        @builtins.property
        def source(self) -> builtins.str:
            '''The source pattern for a URL rewrite or redirect rule.

            *Length Constraints:* Minimum length of 1. Maximum length of 2048.

            *Pattern:* (?s).+

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-customrule.html#cfn-amplify-app-customrule-source
            '''
            result = self._values.get("source")
            assert result is not None, "Required property 'source' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def target(self) -> builtins.str:
            '''The target pattern for a URL rewrite or redirect rule.

            *Length Constraints:* Minimum length of 1. Maximum length of 2048.

            *Pattern:* (?s).+

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-customrule.html#cfn-amplify-app-customrule-target
            '''
            result = self._values.get("target")
            assert result is not None, "Required property 'target' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def condition(self) -> typing.Optional[builtins.str]:
            '''The condition for a URL rewrite or redirect rule, such as a country code.

            *Length Constraints:* Minimum length of 0. Maximum length of 2048.

            *Pattern:* (?s).*

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-customrule.html#cfn-amplify-app-customrule-condition
            '''
            result = self._values.get("condition")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''The status code for a URL rewrite or redirect rule.

            - **200** - Represents a 200 rewrite rule.
            - **301** - Represents a 301 (moved pemanently) redirect rule. This and all future requests should be directed to the target URL.
            - **302** - Represents a 302 temporary redirect rule.
            - **404** - Represents a 404 redirect rule.
            - **404-200** - Represents a 404 rewrite rule.

            *Length Constraints:* Minimum length of 3. Maximum length of 7.

            *Pattern:* .{3,7}

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-customrule.html#cfn-amplify-app-customrule-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplify.CfnApp.EnvironmentVariableProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class EnvironmentVariableProperty:
        def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
            '''Environment variables are key-value pairs that are available at build time.

            Set environment variables for all branches in your app.

            :param name: The environment variable name. *Length Constraints:* Maximum length of 255. *Pattern:* (?s).*
            :param value: The environment variable value. *Length Constraints:* Maximum length of 5500. *Pattern:* (?s).*

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-environmentvariable.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplify as amplify
                
                environment_variable_property = amplify.CfnApp.EnvironmentVariableProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f76edc62ddffd84b573400931e580feb099c3a238dc1b312f88a08a681bc79a2)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "value": value,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The environment variable name.

            *Length Constraints:* Maximum length of 255.

            *Pattern:* (?s).*

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-environmentvariable.html#cfn-amplify-app-environmentvariable-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The environment variable value.

            *Length Constraints:* Maximum length of 5500.

            *Pattern:* (?s).*

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-environmentvariable.html#cfn-amplify-app-environmentvariable-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnvironmentVariableProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_amplify.CfnAppProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "access_token": "accessToken",
        "auto_branch_creation_config": "autoBranchCreationConfig",
        "basic_auth_config": "basicAuthConfig",
        "build_spec": "buildSpec",
        "custom_headers": "customHeaders",
        "custom_rules": "customRules",
        "description": "description",
        "enable_branch_auto_deletion": "enableBranchAutoDeletion",
        "environment_variables": "environmentVariables",
        "iam_service_role": "iamServiceRole",
        "oauth_token": "oauthToken",
        "platform": "platform",
        "repository": "repository",
        "tags": "tags",
    },
)
class CfnAppProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        access_token: typing.Optional[builtins.str] = None,
        auto_branch_creation_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.AutoBranchCreationConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        basic_auth_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.BasicAuthConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        build_spec: typing.Optional[builtins.str] = None,
        custom_headers: typing.Optional[builtins.str] = None,
        custom_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.CustomRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        enable_branch_auto_deletion: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        environment_variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.EnvironmentVariableProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        iam_service_role: typing.Optional[builtins.str] = None,
        oauth_token: typing.Optional[builtins.str] = None,
        platform: typing.Optional[builtins.str] = None,
        repository: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnApp``.

        :param name: The name for an Amplify app. *Length Constraints:* Minimum length of 1. Maximum length of 255. *Pattern:* (?s).+
        :param access_token: The personal access token for a GitHub repository for an Amplify app. The personal access token is used to authorize access to a GitHub repository using the Amplify GitHub App. The token is not stored. Use ``AccessToken`` for GitHub repositories only. To authorize access to a repository provider such as Bitbucket or CodeCommit, use ``OauthToken`` . You must specify either ``AccessToken`` or ``OauthToken`` when you create a new app. Existing Amplify apps deployed from a GitHub repository using OAuth continue to work with CI/CD. However, we strongly recommend that you migrate these apps to use the GitHub App. For more information, see `Migrating an existing OAuth app to the Amplify GitHub App <https://docs.aws.amazon.com/amplify/latest/userguide/setting-up-GitHub-access.html#migrating-to-github-app-auth>`_ in the *Amplify User Guide* . *Length Constraints:* Minimum length of 1. Maximum length of 255.
        :param auto_branch_creation_config: Sets the configuration for your automatic branch creation.
        :param basic_auth_config: The credentials for basic authorization for an Amplify app. You must base64-encode the authorization credentials and provide them in the format ``user:password`` .
        :param build_spec: The build specification (build spec) for an Amplify app. *Length Constraints:* Minimum length of 1. Maximum length of 25000. *Pattern:* (?s).+
        :param custom_headers: The custom HTTP headers for an Amplify app. *Length Constraints:* Minimum length of 0. Maximum length of 25000. *Pattern:* (?s).*
        :param custom_rules: The custom rewrite and redirect rules for an Amplify app.
        :param description: The description for an Amplify app. *Length Constraints:* Maximum length of 1000. *Pattern:* (?s).*
        :param enable_branch_auto_deletion: Automatically disconnect a branch in Amplify Hosting when you delete a branch from your Git repository.
        :param environment_variables: The environment variables map for an Amplify app. For a list of the environment variables that are accessible to Amplify by default, see `Amplify Environment variables <https://docs.aws.amazon.com/amplify/latest/userguide/amplify-console-environment-variables.html>`_ in the *Amplify Hosting User Guide* .
        :param iam_service_role: The AWS Identity and Access Management (IAM) service role for the Amazon Resource Name (ARN) of the Amplify app. *Length Constraints:* Minimum length of 0. Maximum length of 1000. *Pattern:* (?s).*
        :param oauth_token: The OAuth token for a third-party source control system for an Amplify app. The OAuth token is used to create a webhook and a read-only deploy key using SSH cloning. The OAuth token is not stored. Use ``OauthToken`` for repository providers other than GitHub, such as Bitbucket or CodeCommit. To authorize access to GitHub as your repository provider, use ``AccessToken`` . You must specify either ``OauthToken`` or ``AccessToken`` when you create a new app. Existing Amplify apps deployed from a GitHub repository using OAuth continue to work with CI/CD. However, we strongly recommend that you migrate these apps to use the GitHub App. For more information, see `Migrating an existing OAuth app to the Amplify GitHub App <https://docs.aws.amazon.com/amplify/latest/userguide/setting-up-GitHub-access.html#migrating-to-github-app-auth>`_ in the *Amplify User Guide* . *Length Constraints:* Maximum length of 1000. *Pattern:* (?s).*
        :param platform: The platform for the Amplify app. For a static app, set the platform type to ``WEB`` . For a dynamic server-side rendered (SSR) app, set the platform type to ``WEB_COMPUTE`` . For an app requiring Amplify Hosting's original SSR support only, set the platform type to ``WEB_DYNAMIC`` .
        :param repository: The repository for an Amplify app. *Pattern:* (?s).*
        :param tags: The tag for an Amplify app.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_amplify as amplify
            
            cfn_app_props = amplify.CfnAppProps(
                name="name",
            
                # the properties below are optional
                access_token="accessToken",
                auto_branch_creation_config=amplify.CfnApp.AutoBranchCreationConfigProperty(
                    auto_branch_creation_patterns=["autoBranchCreationPatterns"],
                    basic_auth_config=amplify.CfnApp.BasicAuthConfigProperty(
                        enable_basic_auth=False,
                        password="password",
                        username="username"
                    ),
                    build_spec="buildSpec",
                    enable_auto_branch_creation=False,
                    enable_auto_build=False,
                    enable_performance_mode=False,
                    enable_pull_request_preview=False,
                    environment_variables=[amplify.CfnApp.EnvironmentVariableProperty(
                        name="name",
                        value="value"
                    )],
                    framework="framework",
                    pull_request_environment_name="pullRequestEnvironmentName",
                    stage="stage"
                ),
                basic_auth_config=amplify.CfnApp.BasicAuthConfigProperty(
                    enable_basic_auth=False,
                    password="password",
                    username="username"
                ),
                build_spec="buildSpec",
                custom_headers="customHeaders",
                custom_rules=[amplify.CfnApp.CustomRuleProperty(
                    source="source",
                    target="target",
            
                    # the properties below are optional
                    condition="condition",
                    status="status"
                )],
                description="description",
                enable_branch_auto_deletion=False,
                environment_variables=[amplify.CfnApp.EnvironmentVariableProperty(
                    name="name",
                    value="value"
                )],
                iam_service_role="iamServiceRole",
                oauth_token="oauthToken",
                platform="platform",
                repository="repository",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfa8f09e6d42b5d6d1122d3e9214ec780302e9c3fda48d7ca044dd07613d11db)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
            check_type(argname="argument auto_branch_creation_config", value=auto_branch_creation_config, expected_type=type_hints["auto_branch_creation_config"])
            check_type(argname="argument basic_auth_config", value=basic_auth_config, expected_type=type_hints["basic_auth_config"])
            check_type(argname="argument build_spec", value=build_spec, expected_type=type_hints["build_spec"])
            check_type(argname="argument custom_headers", value=custom_headers, expected_type=type_hints["custom_headers"])
            check_type(argname="argument custom_rules", value=custom_rules, expected_type=type_hints["custom_rules"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enable_branch_auto_deletion", value=enable_branch_auto_deletion, expected_type=type_hints["enable_branch_auto_deletion"])
            check_type(argname="argument environment_variables", value=environment_variables, expected_type=type_hints["environment_variables"])
            check_type(argname="argument iam_service_role", value=iam_service_role, expected_type=type_hints["iam_service_role"])
            check_type(argname="argument oauth_token", value=oauth_token, expected_type=type_hints["oauth_token"])
            check_type(argname="argument platform", value=platform, expected_type=type_hints["platform"])
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if access_token is not None:
            self._values["access_token"] = access_token
        if auto_branch_creation_config is not None:
            self._values["auto_branch_creation_config"] = auto_branch_creation_config
        if basic_auth_config is not None:
            self._values["basic_auth_config"] = basic_auth_config
        if build_spec is not None:
            self._values["build_spec"] = build_spec
        if custom_headers is not None:
            self._values["custom_headers"] = custom_headers
        if custom_rules is not None:
            self._values["custom_rules"] = custom_rules
        if description is not None:
            self._values["description"] = description
        if enable_branch_auto_deletion is not None:
            self._values["enable_branch_auto_deletion"] = enable_branch_auto_deletion
        if environment_variables is not None:
            self._values["environment_variables"] = environment_variables
        if iam_service_role is not None:
            self._values["iam_service_role"] = iam_service_role
        if oauth_token is not None:
            self._values["oauth_token"] = oauth_token
        if platform is not None:
            self._values["platform"] = platform
        if repository is not None:
            self._values["repository"] = repository
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name for an Amplify app.

        *Length Constraints:* Minimum length of 1. Maximum length of 255.

        *Pattern:* (?s).+

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_token(self) -> typing.Optional[builtins.str]:
        '''The personal access token for a GitHub repository for an Amplify app.

        The personal access token is used to authorize access to a GitHub repository using the Amplify GitHub App. The token is not stored.

        Use ``AccessToken`` for GitHub repositories only. To authorize access to a repository provider such as Bitbucket or CodeCommit, use ``OauthToken`` .

        You must specify either ``AccessToken`` or ``OauthToken`` when you create a new app.

        Existing Amplify apps deployed from a GitHub repository using OAuth continue to work with CI/CD. However, we strongly recommend that you migrate these apps to use the GitHub App. For more information, see `Migrating an existing OAuth app to the Amplify GitHub App <https://docs.aws.amazon.com/amplify/latest/userguide/setting-up-GitHub-access.html#migrating-to-github-app-auth>`_ in the *Amplify User Guide* .

        *Length Constraints:* Minimum length of 1. Maximum length of 255.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-accesstoken
        '''
        result = self._values.get("access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auto_branch_creation_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApp.AutoBranchCreationConfigProperty]]:
        '''Sets the configuration for your automatic branch creation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-autobranchcreationconfig
        '''
        result = self._values.get("auto_branch_creation_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApp.AutoBranchCreationConfigProperty]], result)

    @builtins.property
    def basic_auth_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApp.BasicAuthConfigProperty]]:
        '''The credentials for basic authorization for an Amplify app.

        You must base64-encode the authorization credentials and provide them in the format ``user:password`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-basicauthconfig
        '''
        result = self._values.get("basic_auth_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApp.BasicAuthConfigProperty]], result)

    @builtins.property
    def build_spec(self) -> typing.Optional[builtins.str]:
        '''The build specification (build spec) for an Amplify app.

        *Length Constraints:* Minimum length of 1. Maximum length of 25000.

        *Pattern:* (?s).+

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-buildspec
        '''
        result = self._values.get("build_spec")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_headers(self) -> typing.Optional[builtins.str]:
        '''The custom HTTP headers for an Amplify app.

        *Length Constraints:* Minimum length of 0. Maximum length of 25000.

        *Pattern:* (?s).*

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-customheaders
        '''
        result = self._values.get("custom_headers")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_rules(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnApp.CustomRuleProperty]]]]:
        '''The custom rewrite and redirect rules for an Amplify app.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-customrules
        '''
        result = self._values.get("custom_rules")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnApp.CustomRuleProperty]]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description for an Amplify app.

        *Length Constraints:* Maximum length of 1000.

        *Pattern:* (?s).*

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_branch_auto_deletion(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Automatically disconnect a branch in Amplify Hosting when you delete a branch from your Git repository.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-enablebranchautodeletion
        '''
        result = self._values.get("enable_branch_auto_deletion")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def environment_variables(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnApp.EnvironmentVariableProperty]]]]:
        '''The environment variables map for an Amplify app.

        For a list of the environment variables that are accessible to Amplify by default, see `Amplify Environment variables <https://docs.aws.amazon.com/amplify/latest/userguide/amplify-console-environment-variables.html>`_ in the *Amplify Hosting User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-environmentvariables
        '''
        result = self._values.get("environment_variables")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnApp.EnvironmentVariableProperty]]]], result)

    @builtins.property
    def iam_service_role(self) -> typing.Optional[builtins.str]:
        '''The AWS Identity and Access Management (IAM) service role for the Amazon Resource Name (ARN) of the Amplify app.

        *Length Constraints:* Minimum length of 0. Maximum length of 1000.

        *Pattern:* (?s).*

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-iamservicerole
        '''
        result = self._values.get("iam_service_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_token(self) -> typing.Optional[builtins.str]:
        '''The OAuth token for a third-party source control system for an Amplify app.

        The OAuth token is used to create a webhook and a read-only deploy key using SSH cloning. The OAuth token is not stored.

        Use ``OauthToken`` for repository providers other than GitHub, such as Bitbucket or CodeCommit. To authorize access to GitHub as your repository provider, use ``AccessToken`` .

        You must specify either ``OauthToken`` or ``AccessToken`` when you create a new app.

        Existing Amplify apps deployed from a GitHub repository using OAuth continue to work with CI/CD. However, we strongly recommend that you migrate these apps to use the GitHub App. For more information, see `Migrating an existing OAuth app to the Amplify GitHub App <https://docs.aws.amazon.com/amplify/latest/userguide/setting-up-GitHub-access.html#migrating-to-github-app-auth>`_ in the *Amplify User Guide* .

        *Length Constraints:* Maximum length of 1000.

        *Pattern:* (?s).*

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-oauthtoken
        '''
        result = self._values.get("oauth_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def platform(self) -> typing.Optional[builtins.str]:
        '''The platform for the Amplify app.

        For a static app, set the platform type to ``WEB`` . For a dynamic server-side rendered (SSR) app, set the platform type to ``WEB_COMPUTE`` . For an app requiring Amplify Hosting's original SSR support only, set the platform type to ``WEB_DYNAMIC`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-platform
        '''
        result = self._values.get("platform")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def repository(self) -> typing.Optional[builtins.str]:
        '''The repository for an Amplify app.

        *Pattern:* (?s).*

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-repository
        '''
        result = self._values.get("repository")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tag for an Amplify app.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html#cfn-amplify-app-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAppProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnBranch(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_amplify.CfnBranch",
):
    '''The AWS::Amplify::Branch resource specifies a new branch within an app.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_amplify as amplify
        
        cfn_branch = amplify.CfnBranch(self, "MyCfnBranch",
            app_id="appId",
            branch_name="branchName",
        
            # the properties below are optional
            basic_auth_config=amplify.CfnBranch.BasicAuthConfigProperty(
                password="password",
                username="username",
        
                # the properties below are optional
                enable_basic_auth=False
            ),
            build_spec="buildSpec",
            description="description",
            enable_auto_build=False,
            enable_performance_mode=False,
            enable_pull_request_preview=False,
            environment_variables=[amplify.CfnBranch.EnvironmentVariableProperty(
                name="name",
                value="value"
            )],
            framework="framework",
            pull_request_environment_name="pullRequestEnvironmentName",
            stage="stage",
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
        app_id: builtins.str,
        branch_name: builtins.str,
        basic_auth_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBranch.BasicAuthConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        build_spec: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        enable_auto_build: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        enable_performance_mode: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        enable_pull_request_preview: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        environment_variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBranch.EnvironmentVariableProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        framework: typing.Optional[builtins.str] = None,
        pull_request_environment_name: typing.Optional[builtins.str] = None,
        stage: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param app_id: The unique ID for an Amplify app. *Length Constraints:* Minimum length of 1. Maximum length of 20. *Pattern:* d[a-z0-9]+
        :param branch_name: The name for the branch. *Length Constraints:* Minimum length of 1. Maximum length of 255. *Pattern:* (?s).+
        :param basic_auth_config: The basic authorization credentials for a branch of an Amplify app. You must base64-encode the authorization credentials and provide them in the format ``user:password`` .
        :param build_spec: The build specification (build spec) for the branch. *Length Constraints:* Minimum length of 1. Maximum length of 25000. *Pattern:* (?s).+
        :param description: The description for the branch that is part of an Amplify app. *Length Constraints:* Maximum length of 1000. *Pattern:* (?s).*
        :param enable_auto_build: Enables auto building for the branch.
        :param enable_performance_mode: Enables performance mode for the branch. Performance mode optimizes for faster hosting performance by keeping content cached at the edge for a longer interval. When performance mode is enabled, hosting configuration or code changes can take up to 10 minutes to roll out.
        :param enable_pull_request_preview: Specifies whether Amplify Hosting creates a preview for each pull request that is made for this branch. If this property is enabled, Amplify deploys your app to a unique preview URL after each pull request is opened. Development and QA teams can use this preview to test the pull request before it's merged into a production or integration branch. To provide backend support for your preview, Amplify automatically provisions a temporary backend environment that it deletes when the pull request is closed. If you want to specify a dedicated backend environment for your previews, use the ``PullRequestEnvironmentName`` property. For more information, see `Web Previews <https://docs.aws.amazon.com/amplify/latest/userguide/pr-previews.html>`_ in the *AWS Amplify Hosting User Guide* .
        :param environment_variables: The environment variables for the branch.
        :param framework: The framework for the branch.
        :param pull_request_environment_name: If pull request previews are enabled for this branch, you can use this property to specify a dedicated backend environment for your previews. For example, you could specify an environment named ``prod`` , ``test`` , or ``dev`` that you initialized with the Amplify CLI and mapped to this branch. To enable pull request previews, set the ``EnablePullRequestPreview`` property to ``true`` . If you don't specify an environment, Amplify Hosting provides backend support for each preview by automatically provisioning a temporary backend environment. Amplify Hosting deletes this environment when the pull request is closed. For more information about creating backend environments, see `Feature Branch Deployments and Team Workflows <https://docs.aws.amazon.com/amplify/latest/userguide/multi-environments.html>`_ in the *AWS Amplify Hosting User Guide* . *Length Constraints:* Maximum length of 20. *Pattern:* (?s).*
        :param stage: Describes the current stage for the branch. *Valid Values:* PRODUCTION | BETA | DEVELOPMENT | EXPERIMENTAL | PULL_REQUEST
        :param tags: The tag for the branch.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__859cd0a15aef1449f80ffe32589fdb895b13f3510c6905791c3eea0336ef1a99)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBranchProps(
            app_id=app_id,
            branch_name=branch_name,
            basic_auth_config=basic_auth_config,
            build_spec=build_spec,
            description=description,
            enable_auto_build=enable_auto_build,
            enable_performance_mode=enable_performance_mode,
            enable_pull_request_preview=enable_pull_request_preview,
            environment_variables=environment_variables,
            framework=framework,
            pull_request_environment_name=pull_request_environment_name,
            stage=stage,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc71828b32564e7bfee35f76a534a0b840914bd4c468396d6b8980cc50ec7e4e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__543fb1814e6e6dc2b2a566111532e52b3b918ec4a69887eb2bc5b8e84805596a)
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
        '''ARN for a branch, part of an Amplify App.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrBranchName")
    def attr_branch_name(self) -> builtins.str:
        '''Name for a branch, part of an Amplify App.

        :cloudformationAttribute: BranchName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBranchName"))

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
    @jsii.member(jsii_name="appId")
    def app_id(self) -> builtins.str:
        '''The unique ID for an Amplify app.'''
        return typing.cast(builtins.str, jsii.get(self, "appId"))

    @app_id.setter
    def app_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__972692afd9ab7e7b991e01833237c55c73059ffac2b6a78fea9664f5f74e725a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appId", value)

    @builtins.property
    @jsii.member(jsii_name="branchName")
    def branch_name(self) -> builtins.str:
        '''The name for the branch.'''
        return typing.cast(builtins.str, jsii.get(self, "branchName"))

    @branch_name.setter
    def branch_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c4cf98b8fee11d8015201a67af685d75d6635cd6b821c934cbf30ef8b3f1c6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "branchName", value)

    @builtins.property
    @jsii.member(jsii_name="basicAuthConfig")
    def basic_auth_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBranch.BasicAuthConfigProperty"]]:
        '''The basic authorization credentials for a branch of an Amplify app.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBranch.BasicAuthConfigProperty"]], jsii.get(self, "basicAuthConfig"))

    @basic_auth_config.setter
    def basic_auth_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBranch.BasicAuthConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c37375d7a595236b497b553716f1bf9273bb14c35be13e872b3614e8223292ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "basicAuthConfig", value)

    @builtins.property
    @jsii.member(jsii_name="buildSpec")
    def build_spec(self) -> typing.Optional[builtins.str]:
        '''The build specification (build spec) for the branch.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "buildSpec"))

    @build_spec.setter
    def build_spec(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae472a508b2b0e4a122ae35d93c8733d00df3680d8823bd2ad857acc210e1c1e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buildSpec", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description for the branch that is part of an Amplify app.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a71cabeaa4605532f47314006f7075821b92f53c6bdb0be7bbb3c0f09ff70ea2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="enableAutoBuild")
    def enable_auto_build(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Enables auto building for the branch.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enableAutoBuild"))

    @enable_auto_build.setter
    def enable_auto_build(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__445b2b1767b882d1a1d22a895384690c61096ef43e57ace707417bc73d08195a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableAutoBuild", value)

    @builtins.property
    @jsii.member(jsii_name="enablePerformanceMode")
    def enable_performance_mode(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Enables performance mode for the branch.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enablePerformanceMode"))

    @enable_performance_mode.setter
    def enable_performance_mode(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a674b2cc76c13d0c0fde7397bd241e62f175181642487615840d580e9e27dcca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enablePerformanceMode", value)

    @builtins.property
    @jsii.member(jsii_name="enablePullRequestPreview")
    def enable_pull_request_preview(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether Amplify Hosting creates a preview for each pull request that is made for this branch.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enablePullRequestPreview"))

    @enable_pull_request_preview.setter
    def enable_pull_request_preview(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c8216d12e1375a7227a3e83088f390c0e7d3575f804bea24c90bc6e4c251ace)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enablePullRequestPreview", value)

    @builtins.property
    @jsii.member(jsii_name="environmentVariables")
    def environment_variables(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBranch.EnvironmentVariableProperty"]]]]:
        '''The environment variables for the branch.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBranch.EnvironmentVariableProperty"]]]], jsii.get(self, "environmentVariables"))

    @environment_variables.setter
    def environment_variables(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBranch.EnvironmentVariableProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ff5456e47cd7b5d2fb38bcf736c28804423dcef024c2d036243fc28345dd532)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentVariables", value)

    @builtins.property
    @jsii.member(jsii_name="framework")
    def framework(self) -> typing.Optional[builtins.str]:
        '''The framework for the branch.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "framework"))

    @framework.setter
    def framework(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b5b9fc9467a46609e53d8cdb56a6811e7e3f85181762874f2a6e91d5dd70f44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "framework", value)

    @builtins.property
    @jsii.member(jsii_name="pullRequestEnvironmentName")
    def pull_request_environment_name(self) -> typing.Optional[builtins.str]:
        '''If pull request previews are enabled for this branch, you can use this property to specify a dedicated backend environment for your previews.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pullRequestEnvironmentName"))

    @pull_request_environment_name.setter
    def pull_request_environment_name(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c0297c438693d937abee43985b9e9c331f79c1c85d337116afc192bca865a77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pullRequestEnvironmentName", value)

    @builtins.property
    @jsii.member(jsii_name="stage")
    def stage(self) -> typing.Optional[builtins.str]:
        '''Describes the current stage for the branch.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stage"))

    @stage.setter
    def stage(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0471f45903b00e5627732fe1b72dc860e5306e479204cad266ccfb5fb50fec5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stage", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tag for the branch.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c012f8c2468f905d2733bdec6a2da61d5e329c6b93e5605a72648a60145eb2d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplify.CfnBranch.BasicAuthConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "password": "password",
            "username": "username",
            "enable_basic_auth": "enableBasicAuth",
        },
    )
    class BasicAuthConfigProperty:
        def __init__(
            self,
            *,
            password: builtins.str,
            username: builtins.str,
            enable_basic_auth: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Use the BasicAuthConfig property type to set password protection for a specific branch.

            :param password: The password for basic authorization. *Length Constraints:* Minimum length of 1. Maximum length of 255.
            :param username: The user name for basic authorization. *Length Constraints:* Minimum length of 1. Maximum length of 255.
            :param enable_basic_auth: Enables basic authorization for the branch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-basicauthconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplify as amplify
                
                basic_auth_config_property = amplify.CfnBranch.BasicAuthConfigProperty(
                    password="password",
                    username="username",
                
                    # the properties below are optional
                    enable_basic_auth=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cc69fa6a46b4e9f374d5854184021c668cb732b42f9661bb62550bea5b4db498)
                check_type(argname="argument password", value=password, expected_type=type_hints["password"])
                check_type(argname="argument username", value=username, expected_type=type_hints["username"])
                check_type(argname="argument enable_basic_auth", value=enable_basic_auth, expected_type=type_hints["enable_basic_auth"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "password": password,
                "username": username,
            }
            if enable_basic_auth is not None:
                self._values["enable_basic_auth"] = enable_basic_auth

        @builtins.property
        def password(self) -> builtins.str:
            '''The password for basic authorization.

            *Length Constraints:* Minimum length of 1. Maximum length of 255.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-basicauthconfig.html#cfn-amplify-branch-basicauthconfig-password
            '''
            result = self._values.get("password")
            assert result is not None, "Required property 'password' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def username(self) -> builtins.str:
            '''The user name for basic authorization.

            *Length Constraints:* Minimum length of 1. Maximum length of 255.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-basicauthconfig.html#cfn-amplify-branch-basicauthconfig-username
            '''
            result = self._values.get("username")
            assert result is not None, "Required property 'username' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def enable_basic_auth(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Enables basic authorization for the branch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-basicauthconfig.html#cfn-amplify-branch-basicauthconfig-enablebasicauth
            '''
            result = self._values.get("enable_basic_auth")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BasicAuthConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplify.CfnBranch.EnvironmentVariableProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class EnvironmentVariableProperty:
        def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
            '''The EnvironmentVariable property type sets environment variables for a specific branch.

            Environment variables are key-value pairs that are available at build time.

            :param name: The environment variable name. *Length Constraints:* Maximum length of 255. *Pattern:* (?s).*
            :param value: The environment variable value. *Length Constraints:* Maximum length of 5500. *Pattern:* (?s).*

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-environmentvariable.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplify as amplify
                
                environment_variable_property = amplify.CfnBranch.EnvironmentVariableProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5692be601b7d7aa14d2fdd9d64f48f458db4470a9da3bcd9c9e8bdbe7562e757)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "value": value,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The environment variable name.

            *Length Constraints:* Maximum length of 255.

            *Pattern:* (?s).*

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-environmentvariable.html#cfn-amplify-branch-environmentvariable-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The environment variable value.

            *Length Constraints:* Maximum length of 5500.

            *Pattern:* (?s).*

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-environmentvariable.html#cfn-amplify-branch-environmentvariable-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnvironmentVariableProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_amplify.CfnBranchProps",
    jsii_struct_bases=[],
    name_mapping={
        "app_id": "appId",
        "branch_name": "branchName",
        "basic_auth_config": "basicAuthConfig",
        "build_spec": "buildSpec",
        "description": "description",
        "enable_auto_build": "enableAutoBuild",
        "enable_performance_mode": "enablePerformanceMode",
        "enable_pull_request_preview": "enablePullRequestPreview",
        "environment_variables": "environmentVariables",
        "framework": "framework",
        "pull_request_environment_name": "pullRequestEnvironmentName",
        "stage": "stage",
        "tags": "tags",
    },
)
class CfnBranchProps:
    def __init__(
        self,
        *,
        app_id: builtins.str,
        branch_name: builtins.str,
        basic_auth_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBranch.BasicAuthConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        build_spec: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        enable_auto_build: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        enable_performance_mode: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        enable_pull_request_preview: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        environment_variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBranch.EnvironmentVariableProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        framework: typing.Optional[builtins.str] = None,
        pull_request_environment_name: typing.Optional[builtins.str] = None,
        stage: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnBranch``.

        :param app_id: The unique ID for an Amplify app. *Length Constraints:* Minimum length of 1. Maximum length of 20. *Pattern:* d[a-z0-9]+
        :param branch_name: The name for the branch. *Length Constraints:* Minimum length of 1. Maximum length of 255. *Pattern:* (?s).+
        :param basic_auth_config: The basic authorization credentials for a branch of an Amplify app. You must base64-encode the authorization credentials and provide them in the format ``user:password`` .
        :param build_spec: The build specification (build spec) for the branch. *Length Constraints:* Minimum length of 1. Maximum length of 25000. *Pattern:* (?s).+
        :param description: The description for the branch that is part of an Amplify app. *Length Constraints:* Maximum length of 1000. *Pattern:* (?s).*
        :param enable_auto_build: Enables auto building for the branch.
        :param enable_performance_mode: Enables performance mode for the branch. Performance mode optimizes for faster hosting performance by keeping content cached at the edge for a longer interval. When performance mode is enabled, hosting configuration or code changes can take up to 10 minutes to roll out.
        :param enable_pull_request_preview: Specifies whether Amplify Hosting creates a preview for each pull request that is made for this branch. If this property is enabled, Amplify deploys your app to a unique preview URL after each pull request is opened. Development and QA teams can use this preview to test the pull request before it's merged into a production or integration branch. To provide backend support for your preview, Amplify automatically provisions a temporary backend environment that it deletes when the pull request is closed. If you want to specify a dedicated backend environment for your previews, use the ``PullRequestEnvironmentName`` property. For more information, see `Web Previews <https://docs.aws.amazon.com/amplify/latest/userguide/pr-previews.html>`_ in the *AWS Amplify Hosting User Guide* .
        :param environment_variables: The environment variables for the branch.
        :param framework: The framework for the branch.
        :param pull_request_environment_name: If pull request previews are enabled for this branch, you can use this property to specify a dedicated backend environment for your previews. For example, you could specify an environment named ``prod`` , ``test`` , or ``dev`` that you initialized with the Amplify CLI and mapped to this branch. To enable pull request previews, set the ``EnablePullRequestPreview`` property to ``true`` . If you don't specify an environment, Amplify Hosting provides backend support for each preview by automatically provisioning a temporary backend environment. Amplify Hosting deletes this environment when the pull request is closed. For more information about creating backend environments, see `Feature Branch Deployments and Team Workflows <https://docs.aws.amazon.com/amplify/latest/userguide/multi-environments.html>`_ in the *AWS Amplify Hosting User Guide* . *Length Constraints:* Maximum length of 20. *Pattern:* (?s).*
        :param stage: Describes the current stage for the branch. *Valid Values:* PRODUCTION | BETA | DEVELOPMENT | EXPERIMENTAL | PULL_REQUEST
        :param tags: The tag for the branch.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_amplify as amplify
            
            cfn_branch_props = amplify.CfnBranchProps(
                app_id="appId",
                branch_name="branchName",
            
                # the properties below are optional
                basic_auth_config=amplify.CfnBranch.BasicAuthConfigProperty(
                    password="password",
                    username="username",
            
                    # the properties below are optional
                    enable_basic_auth=False
                ),
                build_spec="buildSpec",
                description="description",
                enable_auto_build=False,
                enable_performance_mode=False,
                enable_pull_request_preview=False,
                environment_variables=[amplify.CfnBranch.EnvironmentVariableProperty(
                    name="name",
                    value="value"
                )],
                framework="framework",
                pull_request_environment_name="pullRequestEnvironmentName",
                stage="stage",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57c0d80a85d344dca51e3abe3e5e1ee9fff906ef48fa3809bec9a68a37b6d22f)
            check_type(argname="argument app_id", value=app_id, expected_type=type_hints["app_id"])
            check_type(argname="argument branch_name", value=branch_name, expected_type=type_hints["branch_name"])
            check_type(argname="argument basic_auth_config", value=basic_auth_config, expected_type=type_hints["basic_auth_config"])
            check_type(argname="argument build_spec", value=build_spec, expected_type=type_hints["build_spec"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enable_auto_build", value=enable_auto_build, expected_type=type_hints["enable_auto_build"])
            check_type(argname="argument enable_performance_mode", value=enable_performance_mode, expected_type=type_hints["enable_performance_mode"])
            check_type(argname="argument enable_pull_request_preview", value=enable_pull_request_preview, expected_type=type_hints["enable_pull_request_preview"])
            check_type(argname="argument environment_variables", value=environment_variables, expected_type=type_hints["environment_variables"])
            check_type(argname="argument framework", value=framework, expected_type=type_hints["framework"])
            check_type(argname="argument pull_request_environment_name", value=pull_request_environment_name, expected_type=type_hints["pull_request_environment_name"])
            check_type(argname="argument stage", value=stage, expected_type=type_hints["stage"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_id": app_id,
            "branch_name": branch_name,
        }
        if basic_auth_config is not None:
            self._values["basic_auth_config"] = basic_auth_config
        if build_spec is not None:
            self._values["build_spec"] = build_spec
        if description is not None:
            self._values["description"] = description
        if enable_auto_build is not None:
            self._values["enable_auto_build"] = enable_auto_build
        if enable_performance_mode is not None:
            self._values["enable_performance_mode"] = enable_performance_mode
        if enable_pull_request_preview is not None:
            self._values["enable_pull_request_preview"] = enable_pull_request_preview
        if environment_variables is not None:
            self._values["environment_variables"] = environment_variables
        if framework is not None:
            self._values["framework"] = framework
        if pull_request_environment_name is not None:
            self._values["pull_request_environment_name"] = pull_request_environment_name
        if stage is not None:
            self._values["stage"] = stage
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def app_id(self) -> builtins.str:
        '''The unique ID for an Amplify app.

        *Length Constraints:* Minimum length of 1. Maximum length of 20.

        *Pattern:* d[a-z0-9]+

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-appid
        '''
        result = self._values.get("app_id")
        assert result is not None, "Required property 'app_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def branch_name(self) -> builtins.str:
        '''The name for the branch.

        *Length Constraints:* Minimum length of 1. Maximum length of 255.

        *Pattern:* (?s).+

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-branchname
        '''
        result = self._values.get("branch_name")
        assert result is not None, "Required property 'branch_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def basic_auth_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBranch.BasicAuthConfigProperty]]:
        '''The basic authorization credentials for a branch of an Amplify app.

        You must base64-encode the authorization credentials and provide them in the format ``user:password`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-basicauthconfig
        '''
        result = self._values.get("basic_auth_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBranch.BasicAuthConfigProperty]], result)

    @builtins.property
    def build_spec(self) -> typing.Optional[builtins.str]:
        '''The build specification (build spec) for the branch.

        *Length Constraints:* Minimum length of 1. Maximum length of 25000.

        *Pattern:* (?s).+

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-buildspec
        '''
        result = self._values.get("build_spec")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description for the branch that is part of an Amplify app.

        *Length Constraints:* Maximum length of 1000.

        *Pattern:* (?s).*

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_auto_build(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Enables auto building for the branch.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-enableautobuild
        '''
        result = self._values.get("enable_auto_build")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def enable_performance_mode(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Enables performance mode for the branch.

        Performance mode optimizes for faster hosting performance by keeping content cached at the edge for a longer interval. When performance mode is enabled, hosting configuration or code changes can take up to 10 minutes to roll out.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-enableperformancemode
        '''
        result = self._values.get("enable_performance_mode")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def enable_pull_request_preview(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether Amplify Hosting creates a preview for each pull request that is made for this branch.

        If this property is enabled, Amplify deploys your app to a unique preview URL after each pull request is opened. Development and QA teams can use this preview to test the pull request before it's merged into a production or integration branch.

        To provide backend support for your preview, Amplify automatically provisions a temporary backend environment that it deletes when the pull request is closed. If you want to specify a dedicated backend environment for your previews, use the ``PullRequestEnvironmentName`` property.

        For more information, see `Web Previews <https://docs.aws.amazon.com/amplify/latest/userguide/pr-previews.html>`_ in the *AWS Amplify Hosting User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-enablepullrequestpreview
        '''
        result = self._values.get("enable_pull_request_preview")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def environment_variables(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnBranch.EnvironmentVariableProperty]]]]:
        '''The environment variables for the branch.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-environmentvariables
        '''
        result = self._values.get("environment_variables")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnBranch.EnvironmentVariableProperty]]]], result)

    @builtins.property
    def framework(self) -> typing.Optional[builtins.str]:
        '''The framework for the branch.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-framework
        '''
        result = self._values.get("framework")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pull_request_environment_name(self) -> typing.Optional[builtins.str]:
        '''If pull request previews are enabled for this branch, you can use this property to specify a dedicated backend environment for your previews.

        For example, you could specify an environment named ``prod`` , ``test`` , or ``dev`` that you initialized with the Amplify CLI and mapped to this branch.

        To enable pull request previews, set the ``EnablePullRequestPreview`` property to ``true`` .

        If you don't specify an environment, Amplify Hosting provides backend support for each preview by automatically provisioning a temporary backend environment. Amplify Hosting deletes this environment when the pull request is closed.

        For more information about creating backend environments, see `Feature Branch Deployments and Team Workflows <https://docs.aws.amazon.com/amplify/latest/userguide/multi-environments.html>`_ in the *AWS Amplify Hosting User Guide* .

        *Length Constraints:* Maximum length of 20.

        *Pattern:* (?s).*

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-pullrequestenvironmentname
        '''
        result = self._values.get("pull_request_environment_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stage(self) -> typing.Optional[builtins.str]:
        '''Describes the current stage for the branch.

        *Valid Values:* PRODUCTION | BETA | DEVELOPMENT | EXPERIMENTAL | PULL_REQUEST

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-stage
        '''
        result = self._values.get("stage")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tag for the branch.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html#cfn-amplify-branch-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBranchProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnDomain(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_amplify.CfnDomain",
):
    '''The AWS::Amplify::Domain resource allows you to connect a custom domain to your app.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_amplify as amplify
        
        cfn_domain = amplify.CfnDomain(self, "MyCfnDomain",
            app_id="appId",
            domain_name="domainName",
            sub_domain_settings=[amplify.CfnDomain.SubDomainSettingProperty(
                branch_name="branchName",
                prefix="prefix"
            )],
        
            # the properties below are optional
            auto_sub_domain_creation_patterns=["autoSubDomainCreationPatterns"],
            auto_sub_domain_iam_role="autoSubDomainIamRole",
            enable_auto_sub_domain=False
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        app_id: builtins.str,
        domain_name: builtins.str,
        sub_domain_settings: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.SubDomainSettingProperty", typing.Dict[builtins.str, typing.Any]]]]],
        auto_sub_domain_creation_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        auto_sub_domain_iam_role: typing.Optional[builtins.str] = None,
        enable_auto_sub_domain: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param app_id: The unique ID for an Amplify app. *Length Constraints:* Minimum length of 1. Maximum length of 20. *Pattern:* d[a-z0-9]+
        :param domain_name: The domain name for the domain association. *Length Constraints:* Maximum length of 255. *Pattern:* ^(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9]).)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])(.)?$
        :param sub_domain_settings: The setting for the subdomain.
        :param auto_sub_domain_creation_patterns: Sets the branch patterns for automatic subdomain creation.
        :param auto_sub_domain_iam_role: The required AWS Identity and Access Management (IAM) service role for the Amazon Resource Name (ARN) for automatically creating subdomains. *Length Constraints:* Maximum length of 1000. *Pattern:* ^$|^arn:aws:iam::\\d{12}:role.+
        :param enable_auto_sub_domain: Enables the automated creation of subdomains for branches.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a92a80249ff3da7389619f6d46781e48a0d6d9fe2d6d8bc5754daa9ff3c2f0e6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDomainProps(
            app_id=app_id,
            domain_name=domain_name,
            sub_domain_settings=sub_domain_settings,
            auto_sub_domain_creation_patterns=auto_sub_domain_creation_patterns,
            auto_sub_domain_iam_role=auto_sub_domain_iam_role,
            enable_auto_sub_domain=enable_auto_sub_domain,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1c7cb6bd1538d5b0adfbdfb98e3ba556f861cea42161c99c22f9113c1d13e10)
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
            type_hints = typing.get_type_hints(_typecheckingstub__31a4cf442d812fd827ea5057369fefdbaf5cdbe474a7bfab62edd257cdb67165)
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
        '''ARN for the Domain Association.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAutoSubDomainCreationPatterns")
    def attr_auto_sub_domain_creation_patterns(self) -> typing.List[builtins.str]:
        '''Branch patterns for the automatically created subdomain.

        :cloudformationAttribute: AutoSubDomainCreationPatterns
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrAutoSubDomainCreationPatterns"))

    @builtins.property
    @jsii.member(jsii_name="attrAutoSubDomainIamRole")
    def attr_auto_sub_domain_iam_role(self) -> builtins.str:
        '''The IAM service role for the subdomain.

        :cloudformationAttribute: AutoSubDomainIAMRole
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAutoSubDomainIamRole"))

    @builtins.property
    @jsii.member(jsii_name="attrCertificateRecord")
    def attr_certificate_record(self) -> builtins.str:
        '''DNS Record for certificate verification.

        :cloudformationAttribute: CertificateRecord
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCertificateRecord"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainName")
    def attr_domain_name(self) -> builtins.str:
        '''Name of the domain.

        :cloudformationAttribute: DomainName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainName"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainStatus")
    def attr_domain_status(self) -> builtins.str:
        '''Status for the Domain Association.

        :cloudformationAttribute: DomainStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrEnableAutoSubDomain")
    def attr_enable_auto_sub_domain(self) -> _IResolvable_da3f097b:
        '''Specifies whether the automated creation of subdomains for branches is enabled.

        :cloudformationAttribute: EnableAutoSubDomain
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrEnableAutoSubDomain"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusReason")
    def attr_status_reason(self) -> builtins.str:
        '''Reason for the current status of the domain.

        :cloudformationAttribute: StatusReason
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatusReason"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="appId")
    def app_id(self) -> builtins.str:
        '''The unique ID for an Amplify app.'''
        return typing.cast(builtins.str, jsii.get(self, "appId"))

    @app_id.setter
    def app_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad111c06ba39fd5ef23adb9b1caa5909da5ba2a2c2ae73108f5acdef9a233014)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appId", value)

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''The domain name for the domain association.'''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9159fc91129216a6edcebb97e058dd40f8c10e8c8ac3ee82f3e30fd3fd838fc1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="subDomainSettings")
    def sub_domain_settings(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDomain.SubDomainSettingProperty"]]]:
        '''The setting for the subdomain.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDomain.SubDomainSettingProperty"]]], jsii.get(self, "subDomainSettings"))

    @sub_domain_settings.setter
    def sub_domain_settings(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDomain.SubDomainSettingProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b936f87f557fe7bf52c60594221c93cd691bbd17bb4817dd3641ee604e257fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subDomainSettings", value)

    @builtins.property
    @jsii.member(jsii_name="autoSubDomainCreationPatterns")
    def auto_sub_domain_creation_patterns(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Sets the branch patterns for automatic subdomain creation.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "autoSubDomainCreationPatterns"))

    @auto_sub_domain_creation_patterns.setter
    def auto_sub_domain_creation_patterns(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61912070511222bed82564464c04f422d8826ae099f93887a8b1ec1d812d0115)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoSubDomainCreationPatterns", value)

    @builtins.property
    @jsii.member(jsii_name="autoSubDomainIamRole")
    def auto_sub_domain_iam_role(self) -> typing.Optional[builtins.str]:
        '''The required AWS Identity and Access Management (IAM) service role for the Amazon Resource Name (ARN) for automatically creating subdomains.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoSubDomainIamRole"))

    @auto_sub_domain_iam_role.setter
    def auto_sub_domain_iam_role(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e5c09e14aff92aaea4fa282a2b672905afabe76a4faa8624943dade22291ebf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoSubDomainIamRole", value)

    @builtins.property
    @jsii.member(jsii_name="enableAutoSubDomain")
    def enable_auto_sub_domain(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Enables the automated creation of subdomains for branches.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enableAutoSubDomain"))

    @enable_auto_sub_domain.setter
    def enable_auto_sub_domain(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5c15a94c5b8643d55b20a0fd990557b9f18fdec4e783bb03e0143f6e102d7a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableAutoSubDomain", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_amplify.CfnDomain.SubDomainSettingProperty",
        jsii_struct_bases=[],
        name_mapping={"branch_name": "branchName", "prefix": "prefix"},
    )
    class SubDomainSettingProperty:
        def __init__(self, *, branch_name: builtins.str, prefix: builtins.str) -> None:
            '''The SubDomainSetting property type enables you to connect a subdomain (for example, example.exampledomain.com) to a specific branch.

            :param branch_name: The branch name setting for the subdomain. *Length Constraints:* Minimum length of 1. Maximum length of 255. *Pattern:* (?s).+
            :param prefix: The prefix setting for the subdomain. *Length Constraints:* Maximum length of 255. *Pattern:* (?s).*

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-domain-subdomainsetting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_amplify as amplify
                
                sub_domain_setting_property = amplify.CfnDomain.SubDomainSettingProperty(
                    branch_name="branchName",
                    prefix="prefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dd38d5241efdfbfd6fe4d24eb582e27c45fd585058138e3d4ffa9e0774a76cd8)
                check_type(argname="argument branch_name", value=branch_name, expected_type=type_hints["branch_name"])
                check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "branch_name": branch_name,
                "prefix": prefix,
            }

        @builtins.property
        def branch_name(self) -> builtins.str:
            '''The branch name setting for the subdomain.

            *Length Constraints:* Minimum length of 1. Maximum length of 255.

            *Pattern:* (?s).+

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-domain-subdomainsetting.html#cfn-amplify-domain-subdomainsetting-branchname
            '''
            result = self._values.get("branch_name")
            assert result is not None, "Required property 'branch_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def prefix(self) -> builtins.str:
            '''The prefix setting for the subdomain.

            *Length Constraints:* Maximum length of 255.

            *Pattern:* (?s).*

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-domain-subdomainsetting.html#cfn-amplify-domain-subdomainsetting-prefix
            '''
            result = self._values.get("prefix")
            assert result is not None, "Required property 'prefix' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubDomainSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_amplify.CfnDomainProps",
    jsii_struct_bases=[],
    name_mapping={
        "app_id": "appId",
        "domain_name": "domainName",
        "sub_domain_settings": "subDomainSettings",
        "auto_sub_domain_creation_patterns": "autoSubDomainCreationPatterns",
        "auto_sub_domain_iam_role": "autoSubDomainIamRole",
        "enable_auto_sub_domain": "enableAutoSubDomain",
    },
)
class CfnDomainProps:
    def __init__(
        self,
        *,
        app_id: builtins.str,
        domain_name: builtins.str,
        sub_domain_settings: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.SubDomainSettingProperty, typing.Dict[builtins.str, typing.Any]]]]],
        auto_sub_domain_creation_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        auto_sub_domain_iam_role: typing.Optional[builtins.str] = None,
        enable_auto_sub_domain: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDomain``.

        :param app_id: The unique ID for an Amplify app. *Length Constraints:* Minimum length of 1. Maximum length of 20. *Pattern:* d[a-z0-9]+
        :param domain_name: The domain name for the domain association. *Length Constraints:* Maximum length of 255. *Pattern:* ^(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9]).)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])(.)?$
        :param sub_domain_settings: The setting for the subdomain.
        :param auto_sub_domain_creation_patterns: Sets the branch patterns for automatic subdomain creation.
        :param auto_sub_domain_iam_role: The required AWS Identity and Access Management (IAM) service role for the Amazon Resource Name (ARN) for automatically creating subdomains. *Length Constraints:* Maximum length of 1000. *Pattern:* ^$|^arn:aws:iam::\\d{12}:role.+
        :param enable_auto_sub_domain: Enables the automated creation of subdomains for branches.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_amplify as amplify
            
            cfn_domain_props = amplify.CfnDomainProps(
                app_id="appId",
                domain_name="domainName",
                sub_domain_settings=[amplify.CfnDomain.SubDomainSettingProperty(
                    branch_name="branchName",
                    prefix="prefix"
                )],
            
                # the properties below are optional
                auto_sub_domain_creation_patterns=["autoSubDomainCreationPatterns"],
                auto_sub_domain_iam_role="autoSubDomainIamRole",
                enable_auto_sub_domain=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88c16eb1917ed2b27dcef2eed98ca7097349329b83222123ac70b435f951d776)
            check_type(argname="argument app_id", value=app_id, expected_type=type_hints["app_id"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument sub_domain_settings", value=sub_domain_settings, expected_type=type_hints["sub_domain_settings"])
            check_type(argname="argument auto_sub_domain_creation_patterns", value=auto_sub_domain_creation_patterns, expected_type=type_hints["auto_sub_domain_creation_patterns"])
            check_type(argname="argument auto_sub_domain_iam_role", value=auto_sub_domain_iam_role, expected_type=type_hints["auto_sub_domain_iam_role"])
            check_type(argname="argument enable_auto_sub_domain", value=enable_auto_sub_domain, expected_type=type_hints["enable_auto_sub_domain"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_id": app_id,
            "domain_name": domain_name,
            "sub_domain_settings": sub_domain_settings,
        }
        if auto_sub_domain_creation_patterns is not None:
            self._values["auto_sub_domain_creation_patterns"] = auto_sub_domain_creation_patterns
        if auto_sub_domain_iam_role is not None:
            self._values["auto_sub_domain_iam_role"] = auto_sub_domain_iam_role
        if enable_auto_sub_domain is not None:
            self._values["enable_auto_sub_domain"] = enable_auto_sub_domain

    @builtins.property
    def app_id(self) -> builtins.str:
        '''The unique ID for an Amplify app.

        *Length Constraints:* Minimum length of 1. Maximum length of 20.

        *Pattern:* d[a-z0-9]+

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#cfn-amplify-domain-appid
        '''
        result = self._values.get("app_id")
        assert result is not None, "Required property 'app_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The domain name for the domain association.

        *Length Constraints:* Maximum length of 255.

        *Pattern:* ^(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9]).)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])(.)?$

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#cfn-amplify-domain-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sub_domain_settings(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDomain.SubDomainSettingProperty]]]:
        '''The setting for the subdomain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#cfn-amplify-domain-subdomainsettings
        '''
        result = self._values.get("sub_domain_settings")
        assert result is not None, "Required property 'sub_domain_settings' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDomain.SubDomainSettingProperty]]], result)

    @builtins.property
    def auto_sub_domain_creation_patterns(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Sets the branch patterns for automatic subdomain creation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#cfn-amplify-domain-autosubdomaincreationpatterns
        '''
        result = self._values.get("auto_sub_domain_creation_patterns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def auto_sub_domain_iam_role(self) -> typing.Optional[builtins.str]:
        '''The required AWS Identity and Access Management (IAM) service role for the Amazon Resource Name (ARN) for automatically creating subdomains.

        *Length Constraints:* Maximum length of 1000.

        *Pattern:* ^$|^arn:aws:iam::\\d{12}:role.+

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#cfn-amplify-domain-autosubdomainiamrole
        '''
        result = self._values.get("auto_sub_domain_iam_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_auto_sub_domain(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Enables the automated creation of subdomains for branches.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html#cfn-amplify-domain-enableautosubdomain
        '''
        result = self._values.get("enable_auto_sub_domain")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDomainProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApp",
    "CfnAppProps",
    "CfnBranch",
    "CfnBranchProps",
    "CfnDomain",
    "CfnDomainProps",
]

publication.publish()

def _typecheckingstub__8dc8d772047a068d22a76d907b344356448c6a26d23e419ed69cc622d02781ee(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    access_token: typing.Optional[builtins.str] = None,
    auto_branch_creation_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.AutoBranchCreationConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    basic_auth_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.BasicAuthConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    build_spec: typing.Optional[builtins.str] = None,
    custom_headers: typing.Optional[builtins.str] = None,
    custom_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.CustomRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    enable_branch_auto_deletion: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    environment_variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.EnvironmentVariableProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    iam_service_role: typing.Optional[builtins.str] = None,
    oauth_token: typing.Optional[builtins.str] = None,
    platform: typing.Optional[builtins.str] = None,
    repository: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86430113f75e093324439a08235b05caf66a071c9480bffb7d367fe6c3214308(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a907b90c3eb27e674a931172d848655ba40852fd440d8525c2a6819779ce4b4(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdfa7791969585e493dc40e8ceb68db0f3860ba941690b779c4d50f75aebbbd7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a34b8e83d25c0c26838033ec8d45694e410c5c28d0bf83263b9f9d0942496b2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f38a76185a264f75d2add648c8308477d491dddde9804ac7dfbe3bb22d6ea352(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApp.AutoBranchCreationConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c88becb37a9dd8239d9ff6aff490658ca182aff7fcab83a21ab6054c309a8432(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApp.BasicAuthConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8d9c326dc2b610757cecc45608945b716d8ea6af4111bd656fb2927aa80d26c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__623b6d97b6b1967c76a0782c9ba61b276ee5ff570dad9ab0003baf0626317805(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24f88ebda938286ba2d8ff036b7dcf3cb20a38f782c34c0484b66a2b916ac21f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnApp.CustomRuleProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f271970963b091aefd84c3ab3d2b252d3dca5e4789a892ae905ec8fbf52784e5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dc6d20be8c1648863255ae7968af724a5e56aadb1ddf86b4126b4d6fc096bb6(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ffb3244739d356fab1ba7899722798d4558303d9d3e2a3caaa138b21a86181b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnApp.EnvironmentVariableProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__378909021f9642b2e612e1ecd4b62069a17df2eef9f3461fa46cd5337a44dae9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4f1a9875121cc669c475a05f9524db58d7e32e0b0134143bf750ceca8d2d6ec(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67a5adcc133fbd9a8b5cd704d8959ba2006e08994f5a37195cf965503b97fa28(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77810a604b4d1c18de17ffbf1fde3969ab827d2e901598428f49ecc37a16b28d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8df0df5db275f36f972fd610984f160f89f4bdc11545dfef3ffa8b0e4dda0842(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f2d37f548867fe52cc8c3c461e27ca7411af070358e14a397f593a46ce69d2f(
    *,
    auto_branch_creation_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    basic_auth_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.BasicAuthConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    build_spec: typing.Optional[builtins.str] = None,
    enable_auto_branch_creation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    enable_auto_build: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    enable_performance_mode: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    enable_pull_request_preview: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    environment_variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.EnvironmentVariableProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    framework: typing.Optional[builtins.str] = None,
    pull_request_environment_name: typing.Optional[builtins.str] = None,
    stage: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44bbd6c7457829d13279657590a4d74f5306d440e4549b9168c72df5cff67af9(
    *,
    enable_basic_auth: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    password: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca2210b3c179b77af8d9da860b10e6e93aafae9d4e268f8999f6ce252c3f2363(
    *,
    source: builtins.str,
    target: builtins.str,
    condition: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f76edc62ddffd84b573400931e580feb099c3a238dc1b312f88a08a681bc79a2(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfa8f09e6d42b5d6d1122d3e9214ec780302e9c3fda48d7ca044dd07613d11db(
    *,
    name: builtins.str,
    access_token: typing.Optional[builtins.str] = None,
    auto_branch_creation_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.AutoBranchCreationConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    basic_auth_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.BasicAuthConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    build_spec: typing.Optional[builtins.str] = None,
    custom_headers: typing.Optional[builtins.str] = None,
    custom_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.CustomRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    enable_branch_auto_deletion: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    environment_variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApp.EnvironmentVariableProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    iam_service_role: typing.Optional[builtins.str] = None,
    oauth_token: typing.Optional[builtins.str] = None,
    platform: typing.Optional[builtins.str] = None,
    repository: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__859cd0a15aef1449f80ffe32589fdb895b13f3510c6905791c3eea0336ef1a99(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    app_id: builtins.str,
    branch_name: builtins.str,
    basic_auth_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBranch.BasicAuthConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    build_spec: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    enable_auto_build: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    enable_performance_mode: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    enable_pull_request_preview: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    environment_variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBranch.EnvironmentVariableProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    framework: typing.Optional[builtins.str] = None,
    pull_request_environment_name: typing.Optional[builtins.str] = None,
    stage: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc71828b32564e7bfee35f76a534a0b840914bd4c468396d6b8980cc50ec7e4e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__543fb1814e6e6dc2b2a566111532e52b3b918ec4a69887eb2bc5b8e84805596a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__972692afd9ab7e7b991e01833237c55c73059ffac2b6a78fea9664f5f74e725a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c4cf98b8fee11d8015201a67af685d75d6635cd6b821c934cbf30ef8b3f1c6b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c37375d7a595236b497b553716f1bf9273bb14c35be13e872b3614e8223292ad(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBranch.BasicAuthConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae472a508b2b0e4a122ae35d93c8733d00df3680d8823bd2ad857acc210e1c1e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a71cabeaa4605532f47314006f7075821b92f53c6bdb0be7bbb3c0f09ff70ea2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__445b2b1767b882d1a1d22a895384690c61096ef43e57ace707417bc73d08195a(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a674b2cc76c13d0c0fde7397bd241e62f175181642487615840d580e9e27dcca(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c8216d12e1375a7227a3e83088f390c0e7d3575f804bea24c90bc6e4c251ace(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ff5456e47cd7b5d2fb38bcf736c28804423dcef024c2d036243fc28345dd532(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnBranch.EnvironmentVariableProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b5b9fc9467a46609e53d8cdb56a6811e7e3f85181762874f2a6e91d5dd70f44(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c0297c438693d937abee43985b9e9c331f79c1c85d337116afc192bca865a77(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0471f45903b00e5627732fe1b72dc860e5306e479204cad266ccfb5fb50fec5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c012f8c2468f905d2733bdec6a2da61d5e329c6b93e5605a72648a60145eb2d4(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc69fa6a46b4e9f374d5854184021c668cb732b42f9661bb62550bea5b4db498(
    *,
    password: builtins.str,
    username: builtins.str,
    enable_basic_auth: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5692be601b7d7aa14d2fdd9d64f48f458db4470a9da3bcd9c9e8bdbe7562e757(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57c0d80a85d344dca51e3abe3e5e1ee9fff906ef48fa3809bec9a68a37b6d22f(
    *,
    app_id: builtins.str,
    branch_name: builtins.str,
    basic_auth_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBranch.BasicAuthConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    build_spec: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    enable_auto_build: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    enable_performance_mode: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    enable_pull_request_preview: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    environment_variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBranch.EnvironmentVariableProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    framework: typing.Optional[builtins.str] = None,
    pull_request_environment_name: typing.Optional[builtins.str] = None,
    stage: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a92a80249ff3da7389619f6d46781e48a0d6d9fe2d6d8bc5754daa9ff3c2f0e6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    app_id: builtins.str,
    domain_name: builtins.str,
    sub_domain_settings: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.SubDomainSettingProperty, typing.Dict[builtins.str, typing.Any]]]]],
    auto_sub_domain_creation_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    auto_sub_domain_iam_role: typing.Optional[builtins.str] = None,
    enable_auto_sub_domain: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1c7cb6bd1538d5b0adfbdfb98e3ba556f861cea42161c99c22f9113c1d13e10(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31a4cf442d812fd827ea5057369fefdbaf5cdbe474a7bfab62edd257cdb67165(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad111c06ba39fd5ef23adb9b1caa5909da5ba2a2c2ae73108f5acdef9a233014(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9159fc91129216a6edcebb97e058dd40f8c10e8c8ac3ee82f3e30fd3fd838fc1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b936f87f557fe7bf52c60594221c93cd691bbd17bb4817dd3641ee604e257fb(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDomain.SubDomainSettingProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61912070511222bed82564464c04f422d8826ae099f93887a8b1ec1d812d0115(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e5c09e14aff92aaea4fa282a2b672905afabe76a4faa8624943dade22291ebf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5c15a94c5b8643d55b20a0fd990557b9f18fdec4e783bb03e0143f6e102d7a4(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd38d5241efdfbfd6fe4d24eb582e27c45fd585058138e3d4ffa9e0774a76cd8(
    *,
    branch_name: builtins.str,
    prefix: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88c16eb1917ed2b27dcef2eed98ca7097349329b83222123ac70b435f951d776(
    *,
    app_id: builtins.str,
    domain_name: builtins.str,
    sub_domain_settings: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.SubDomainSettingProperty, typing.Dict[builtins.str, typing.Any]]]]],
    auto_sub_domain_creation_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    auto_sub_domain_iam_role: typing.Optional[builtins.str] = None,
    enable_auto_sub_domain: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass
