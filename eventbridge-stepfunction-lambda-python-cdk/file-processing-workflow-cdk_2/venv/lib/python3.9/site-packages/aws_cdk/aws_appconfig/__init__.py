'''
# AWS::AppConfig Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_appconfig as appconfig
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for AppConfig construct libraries](https://constructs.dev/search?q=appconfig)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::AppConfig resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AppConfig.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::AppConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AppConfig.html).

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


@jsii.implements(_IInspectable_c2943556)
class CfnApplication(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appconfig.CfnApplication",
):
    '''The ``AWS::AppConfig::Application`` resource creates an application.

    In AWS AppConfig , an application is simply an organizational construct like a folder. This organizational construct has a relationship with some unit of executable code. For example, you could create an application called MyMobileApp to organize and manage configuration data for a mobile application installed by your users.

    AWS AppConfig requires that you create resources and deploy a configuration in the following order:

    - Create an application
    - Create an environment
    - Create a configuration profile
    - Create a deployment strategy
    - Deploy the configuration

    For more information, see `AWS AppConfig <https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html>`_ in the *AWS AppConfig User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-application.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appconfig as appconfig
        
        cfn_application = appconfig.CfnApplication(self, "MyCfnApplication",
            name="name",
        
            # the properties below are optional
            description="description",
            tags=[appconfig.CfnApplication.TagsProperty(
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
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["CfnApplication.TagsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: A name for the application.
        :param description: A description of the application.
        :param tags: Metadata to assign to the application. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5cb8c402a0d1a836162f596142de6ed2a1f2a0635a355ae334b92eb1175e956)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationProps(name=name, description=description, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ea7b1a84049868bc175511a7cff8896cbe830377b519f6e81ca6912165c12a6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f6ba5479a5d56f629f8d2769fdc6bc86ac3ecfb94f4a9b20a0a26e228f899e8a)
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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A name for the application.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd439efd20029913dc2dc3442824daa5698101df926aeab59ca95e5e5b8bbd51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the application.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a824db2a54c11ce0a54133772196bc9c7049c60fe6169de15459866f72df2438)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["CfnApplication.TagsProperty"]]:
        '''Metadata to assign to the application.'''
        return typing.cast(typing.Optional[typing.List["CfnApplication.TagsProperty"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["CfnApplication.TagsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1c6b2136fb3c6e3eba293e5878e147b18261e888036e9d04f50ade7f12363e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appconfig.CfnApplication.TagsProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class TagsProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Metadata to assign to the application.

            Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.

            :param key: The key-value string map. The valid character set is ``[a-zA-Z+-=._:/]`` . The tag key can be up to 128 characters and must not start with ``aws:`` .
            :param value: The tag value can be up to 256 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-application-tags.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appconfig as appconfig
                
                tags_property = appconfig.CfnApplication.TagsProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e23a692b191ad17b59ca3b168ad9b22a1a2f3166cfe85a66eeb03dff73e0e4fd)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''The key-value string map.

            The valid character set is ``[a-zA-Z+-=._:/]`` . The tag key can be up to 128 characters and must not start with ``aws:`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-application-tags.html#cfn-appconfig-application-tags-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The tag value can be up to 256 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-application-tags.html#cfn-appconfig-application-tags-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appconfig.CfnApplicationProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "description": "description", "tags": "tags"},
)
class CfnApplicationProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[CfnApplication.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnApplication``.

        :param name: A name for the application.
        :param description: A description of the application.
        :param tags: Metadata to assign to the application. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-application.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appconfig as appconfig
            
            cfn_application_props = appconfig.CfnApplicationProps(
                name="name",
            
                # the properties below are optional
                description="description",
                tags=[appconfig.CfnApplication.TagsProperty(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32e1eda1678f32e80ec88e7c377d932bfe40dcff82d39b0dd0edf98a68d3e9d9)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''A name for the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-application.html#cfn-appconfig-application-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-application.html#cfn-appconfig-application-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[CfnApplication.TagsProperty]]:
        '''Metadata to assign to the application.

        Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-application.html#cfn-appconfig-application-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[CfnApplication.TagsProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnConfigurationProfile(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appconfig.CfnConfigurationProfile",
):
    '''The ``AWS::AppConfig::ConfigurationProfile`` resource creates a configuration profile that enables AWS AppConfig to access the configuration source.

    Valid configuration sources include AWS Systems Manager (SSM) documents, SSM Parameter Store parameters, and Amazon S3 . A configuration profile includes the following information.

    - The Uri location of the configuration data.
    - The AWS Identity and Access Management ( IAM ) role that provides access to the configuration data.
    - A validator for the configuration data. Available validators include either a JSON Schema or the Amazon Resource Name (ARN) of an AWS Lambda function.

    AWS AppConfig requires that you create resources and deploy a configuration in the following order:

    - Create an application
    - Create an environment
    - Create a configuration profile
    - Create a deployment strategy
    - Deploy the configuration

    For more information, see `AWS AppConfig <https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html>`_ in the *AWS AppConfig User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appconfig as appconfig
        
        cfn_configuration_profile = appconfig.CfnConfigurationProfile(self, "MyCfnConfigurationProfile",
            application_id="applicationId",
            location_uri="locationUri",
            name="name",
        
            # the properties below are optional
            description="description",
            retrieval_role_arn="retrievalRoleArn",
            tags=[appconfig.CfnConfigurationProfile.TagsProperty(
                key="key",
                value="value"
            )],
            type="type",
            validators=[appconfig.CfnConfigurationProfile.ValidatorsProperty(
                content="content",
                type="type"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        location_uri: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        retrieval_role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["CfnConfigurationProfile.TagsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        type: typing.Optional[builtins.str] = None,
        validators: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationProfile.ValidatorsProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_id: The application ID.
        :param location_uri: A URI to locate the configuration. You can specify the following:. - For the AWS AppConfig hosted configuration store and for feature flags, specify ``hosted`` . - For an AWS Systems Manager Parameter Store parameter, specify either the parameter name in the format ``ssm-parameter://<parameter name>`` or the ARN. - For an AWS CodePipeline pipeline, specify the URI in the following format: ``codepipeline`` ://. - For an AWS Secrets Manager secret, specify the URI in the following format: ``secretsmanager`` ://. - For an Amazon S3 object, specify the URI in the following format: ``s3://<bucket>/<objectKey>`` . Here is an example: ``s3://my-bucket/my-app/us-east-1/my-config.json`` - For an SSM document, specify either the document name in the format ``ssm-document://<document name>`` or the Amazon Resource Name (ARN).
        :param name: A name for the configuration profile.
        :param description: A description of the configuration profile.
        :param retrieval_role_arn: The ARN of an IAM role with permission to access the configuration at the specified ``LocationUri`` . .. epigraph:: A retrieval role ARN is not required for configurations stored in the AWS AppConfig hosted configuration store. It is required for all other sources that store your configuration.
        :param tags: Metadata to assign to the configuration profile. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.
        :param type: The type of configurations contained in the profile. AWS AppConfig supports ``feature flags`` and ``freeform`` configurations. We recommend you create feature flag configurations to enable or disable new features and freeform configurations to distribute configurations to an application. When calling this API, enter one of the following values for ``Type`` : ``AWS.AppConfig.FeatureFlags`` ``AWS.Freeform``
        :param validators: A list of methods for validating the configuration.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__332c05b5fb120e53a9fcdde311f2bc23aaec927aa0e70b013e72cc2cebe88708)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConfigurationProfileProps(
            application_id=application_id,
            location_uri=location_uri,
            name=name,
            description=description,
            retrieval_role_arn=retrieval_role_arn,
            tags=tags,
            type=type,
            validators=validators,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e772e24251baa448c01bcc3e6670ade5ceed90c38ae4803dc614bd5e09316acd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e32e704ce25e06be45d32d6a2f4cb3655c378ec2a6662baf1f650e54d58d3148)
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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The application ID.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a90d416aa5727f39ec3c71cf2276506643a5cf358d97a872994efb5efc0c6a23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="locationUri")
    def location_uri(self) -> builtins.str:
        '''A URI to locate the configuration.

        You can specify the following:.
        '''
        return typing.cast(builtins.str, jsii.get(self, "locationUri"))

    @location_uri.setter
    def location_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b354f0f45617e66d27b62ebf9a76fdbe168c6f5b6731023e6a366547233a4cb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locationUri", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A name for the configuration profile.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92d26c2b0d5b0b13ed55ca82e2b92075cdb99d8bd6d4a9122e33104a12cf9d5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the configuration profile.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5884bd7f8fdc28919378604807977665ba3e82a47697c023e5982eb7257f557c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="retrievalRoleArn")
    def retrieval_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of an IAM role with permission to access the configuration at the specified ``LocationUri`` .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "retrievalRoleArn"))

    @retrieval_role_arn.setter
    def retrieval_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d3f2e474a52e1c1e45abe4e24cd6c758600c20023f3697e0c69533c0e771bc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retrievalRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(
        self,
    ) -> typing.Optional[typing.List["CfnConfigurationProfile.TagsProperty"]]:
        '''Metadata to assign to the configuration profile.'''
        return typing.cast(typing.Optional[typing.List["CfnConfigurationProfile.TagsProperty"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["CfnConfigurationProfile.TagsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebd94616157773a4ab3988775ff92592f3cda9938c8625e395d1dbbf8406354b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of configurations contained in the profile.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "type"))

    @type.setter
    def type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c45113a4405009713d71c8289b038f5cff241d53b81b243f0372147d29440ad9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="validators")
    def validators(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfigurationProfile.ValidatorsProperty"]]]]:
        '''A list of methods for validating the configuration.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfigurationProfile.ValidatorsProperty"]]]], jsii.get(self, "validators"))

    @validators.setter
    def validators(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfigurationProfile.ValidatorsProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11ba2acd464e5613cd96989e3516592dcd5684d8452b3028698e0549f5d5fafb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validators", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appconfig.CfnConfigurationProfile.TagsProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class TagsProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Metadata to assign to the configuration profile.

            Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.

            :param key: The key-value string map. The valid character set is ``[a-zA-Z+-=._:/]`` . The tag key can be up to 128 characters and must not start with ``aws:`` .
            :param value: The tag value can be up to 256 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-configurationprofile-tags.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appconfig as appconfig
                
                tags_property = appconfig.CfnConfigurationProfile.TagsProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e56fd1db0eac83273c71919752012ed7424296a5db1629b01fefd16fbf70d613)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''The key-value string map.

            The valid character set is ``[a-zA-Z+-=._:/]`` . The tag key can be up to 128 characters and must not start with ``aws:`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-configurationprofile-tags.html#cfn-appconfig-configurationprofile-tags-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The tag value can be up to 256 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-configurationprofile-tags.html#cfn-appconfig-configurationprofile-tags-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appconfig.CfnConfigurationProfile.ValidatorsProperty",
        jsii_struct_bases=[],
        name_mapping={"content": "content", "type": "type"},
    )
    class ValidatorsProperty:
        def __init__(
            self,
            *,
            content: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A validator provides a syntactic or semantic check to ensure the configuration that you want to deploy functions as intended.

            To validate your application configuration data, you provide a schema or an AWS Lambda function that runs against the configuration. The configuration deployment or update can only proceed when the configuration data is valid.

            :param content: Either the JSON Schema content or the Amazon Resource Name (ARN) of an Lambda function.
            :param type: AWS AppConfig supports validators of type ``JSON_SCHEMA`` and ``LAMBDA``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-configurationprofile-validators.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appconfig as appconfig
                
                validators_property = appconfig.CfnConfigurationProfile.ValidatorsProperty(
                    content="content",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e3e2223bb16cf91626b0a44db9aa8ec9190717961f143668d3ff6961eec9abdd)
                check_type(argname="argument content", value=content, expected_type=type_hints["content"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if content is not None:
                self._values["content"] = content
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def content(self) -> typing.Optional[builtins.str]:
            '''Either the JSON Schema content or the Amazon Resource Name (ARN) of an Lambda function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-configurationprofile-validators.html#cfn-appconfig-configurationprofile-validators-content
            '''
            result = self._values.get("content")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''AWS AppConfig supports validators of type ``JSON_SCHEMA`` and ``LAMBDA``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-configurationprofile-validators.html#cfn-appconfig-configurationprofile-validators-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ValidatorsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appconfig.CfnConfigurationProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "location_uri": "locationUri",
        "name": "name",
        "description": "description",
        "retrieval_role_arn": "retrievalRoleArn",
        "tags": "tags",
        "type": "type",
        "validators": "validators",
    },
)
class CfnConfigurationProfileProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        location_uri: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        retrieval_role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[CfnConfigurationProfile.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        type: typing.Optional[builtins.str] = None,
        validators: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationProfile.ValidatorsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConfigurationProfile``.

        :param application_id: The application ID.
        :param location_uri: A URI to locate the configuration. You can specify the following:. - For the AWS AppConfig hosted configuration store and for feature flags, specify ``hosted`` . - For an AWS Systems Manager Parameter Store parameter, specify either the parameter name in the format ``ssm-parameter://<parameter name>`` or the ARN. - For an AWS CodePipeline pipeline, specify the URI in the following format: ``codepipeline`` ://. - For an AWS Secrets Manager secret, specify the URI in the following format: ``secretsmanager`` ://. - For an Amazon S3 object, specify the URI in the following format: ``s3://<bucket>/<objectKey>`` . Here is an example: ``s3://my-bucket/my-app/us-east-1/my-config.json`` - For an SSM document, specify either the document name in the format ``ssm-document://<document name>`` or the Amazon Resource Name (ARN).
        :param name: A name for the configuration profile.
        :param description: A description of the configuration profile.
        :param retrieval_role_arn: The ARN of an IAM role with permission to access the configuration at the specified ``LocationUri`` . .. epigraph:: A retrieval role ARN is not required for configurations stored in the AWS AppConfig hosted configuration store. It is required for all other sources that store your configuration.
        :param tags: Metadata to assign to the configuration profile. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.
        :param type: The type of configurations contained in the profile. AWS AppConfig supports ``feature flags`` and ``freeform`` configurations. We recommend you create feature flag configurations to enable or disable new features and freeform configurations to distribute configurations to an application. When calling this API, enter one of the following values for ``Type`` : ``AWS.AppConfig.FeatureFlags`` ``AWS.Freeform``
        :param validators: A list of methods for validating the configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appconfig as appconfig
            
            cfn_configuration_profile_props = appconfig.CfnConfigurationProfileProps(
                application_id="applicationId",
                location_uri="locationUri",
                name="name",
            
                # the properties below are optional
                description="description",
                retrieval_role_arn="retrievalRoleArn",
                tags=[appconfig.CfnConfigurationProfile.TagsProperty(
                    key="key",
                    value="value"
                )],
                type="type",
                validators=[appconfig.CfnConfigurationProfile.ValidatorsProperty(
                    content="content",
                    type="type"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37522e89a156f185f3387aea77d01f8010adde3d2bcfeb76862a70fd9b7e08bc)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument location_uri", value=location_uri, expected_type=type_hints["location_uri"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument retrieval_role_arn", value=retrieval_role_arn, expected_type=type_hints["retrieval_role_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument validators", value=validators, expected_type=type_hints["validators"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
            "location_uri": location_uri,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if retrieval_role_arn is not None:
            self._values["retrieval_role_arn"] = retrieval_role_arn
        if tags is not None:
            self._values["tags"] = tags
        if type is not None:
            self._values["type"] = type
        if validators is not None:
            self._values["validators"] = validators

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The application ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location_uri(self) -> builtins.str:
        '''A URI to locate the configuration. You can specify the following:.

        - For the AWS AppConfig hosted configuration store and for feature flags, specify ``hosted`` .
        - For an AWS Systems Manager Parameter Store parameter, specify either the parameter name in the format ``ssm-parameter://<parameter name>`` or the ARN.
        - For an AWS CodePipeline pipeline, specify the URI in the following format: ``codepipeline`` ://.
        - For an AWS Secrets Manager secret, specify the URI in the following format: ``secretsmanager`` ://.
        - For an Amazon S3 object, specify the URI in the following format: ``s3://<bucket>/<objectKey>`` . Here is an example: ``s3://my-bucket/my-app/us-east-1/my-config.json``
        - For an SSM document, specify either the document name in the format ``ssm-document://<document name>`` or the Amazon Resource Name (ARN).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-locationuri
        '''
        result = self._values.get("location_uri")
        assert result is not None, "Required property 'location_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A name for the configuration profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the configuration profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retrieval_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of an IAM role with permission to access the configuration at the specified ``LocationUri`` .

        .. epigraph::

           A retrieval role ARN is not required for configurations stored in the AWS AppConfig hosted configuration store. It is required for all other sources that store your configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-retrievalrolearn
        '''
        result = self._values.get("retrieval_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(
        self,
    ) -> typing.Optional[typing.List[CfnConfigurationProfile.TagsProperty]]:
        '''Metadata to assign to the configuration profile.

        Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[CfnConfigurationProfile.TagsProperty]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of configurations contained in the profile.

        AWS AppConfig supports ``feature flags`` and ``freeform`` configurations. We recommend you create feature flag configurations to enable or disable new features and freeform configurations to distribute configurations to an application. When calling this API, enter one of the following values for ``Type`` :

        ``AWS.AppConfig.FeatureFlags``

        ``AWS.Freeform``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def validators(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConfigurationProfile.ValidatorsProperty]]]]:
        '''A list of methods for validating the configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-validators
        '''
        result = self._values.get("validators")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConfigurationProfile.ValidatorsProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfigurationProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnDeployment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appconfig.CfnDeployment",
):
    '''The ``AWS::AppConfig::Deployment`` resource starts a deployment.

    Starting a deployment in AWS AppConfig calls the ``StartDeployment`` API action. This call includes the IDs of the AWS AppConfig application, the environment, the configuration profile, and (optionally) the configuration data version to deploy. The call also includes the ID of the deployment strategy to use, which determines how the configuration data is deployed.

    AWS AppConfig monitors the distribution to all hosts and reports status. If a distribution fails, then AWS AppConfig rolls back the configuration.

    AWS AppConfig requires that you create resources and deploy a configuration in the following order:

    - Create an application
    - Create an environment
    - Create a configuration profile
    - Create a deployment strategy
    - Deploy the configuration

    For more information, see `AWS AppConfig <https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html>`_ in the *AWS AppConfig User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appconfig as appconfig
        
        cfn_deployment = appconfig.CfnDeployment(self, "MyCfnDeployment",
            application_id="applicationId",
            configuration_profile_id="configurationProfileId",
            configuration_version="configurationVersion",
            deployment_strategy_id="deploymentStrategyId",
            environment_id="environmentId",
        
            # the properties below are optional
            description="description",
            kms_key_identifier="kmsKeyIdentifier",
            tags=[appconfig.CfnDeployment.TagsProperty(
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
        application_id: builtins.str,
        configuration_profile_id: builtins.str,
        configuration_version: builtins.str,
        deployment_strategy_id: builtins.str,
        environment_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        kms_key_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["CfnDeployment.TagsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_id: The application ID.
        :param configuration_profile_id: The configuration profile ID.
        :param configuration_version: The configuration version to deploy. If deploying an AWS AppConfig hosted configuration version, you can specify either the version number or version label. For all other configurations, you must specify the version number.
        :param deployment_strategy_id: The deployment strategy ID.
        :param environment_id: The environment ID.
        :param description: A description of the deployment.
        :param kms_key_identifier: The AWS KMS key identifier (key ID, key alias, or key ARN). AWS AppConfig uses this ID to encrypt the configuration data using a customer managed key.
        :param tags: Metadata to assign to the deployment. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1b3c15ba63fb6169371007d7bae981d061f49c21042389030326b9ae1271344)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDeploymentProps(
            application_id=application_id,
            configuration_profile_id=configuration_profile_id,
            configuration_version=configuration_version,
            deployment_strategy_id=deployment_strategy_id,
            environment_id=environment_id,
            description=description,
            kms_key_identifier=kms_key_identifier,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aaa2637a497fc43f28ee8b6e77e0f1878471c7f5bc0a736d0303ca69cb2d082c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6d3096cada1facd4de77c79fe8d588aa3d9567d81b3f913d2c2e6cf8fac54d0e)
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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The application ID.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95aaa1f67bb9531251e5f9c62292c84df7727307a58c223aaa637f0a36a3d65d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="configurationProfileId")
    def configuration_profile_id(self) -> builtins.str:
        '''The configuration profile ID.'''
        return typing.cast(builtins.str, jsii.get(self, "configurationProfileId"))

    @configuration_profile_id.setter
    def configuration_profile_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca3182ab453e0412fad7ba8649da4e0cfebf187bd90f38a026444982eb8bf50e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationProfileId", value)

    @builtins.property
    @jsii.member(jsii_name="configurationVersion")
    def configuration_version(self) -> builtins.str:
        '''The configuration version to deploy.'''
        return typing.cast(builtins.str, jsii.get(self, "configurationVersion"))

    @configuration_version.setter
    def configuration_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5abde1954bdb5d84cfce775808f90c961127e86db5ff5164bb90a98e3b0f9f20)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationVersion", value)

    @builtins.property
    @jsii.member(jsii_name="deploymentStrategyId")
    def deployment_strategy_id(self) -> builtins.str:
        '''The deployment strategy ID.'''
        return typing.cast(builtins.str, jsii.get(self, "deploymentStrategyId"))

    @deployment_strategy_id.setter
    def deployment_strategy_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0527964ec5c65ed1bca366f0674e5cda5d23fe019ae479f3ee3fb550fbdb0c23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentStrategyId", value)

    @builtins.property
    @jsii.member(jsii_name="environmentId")
    def environment_id(self) -> builtins.str:
        '''The environment ID.'''
        return typing.cast(builtins.str, jsii.get(self, "environmentId"))

    @environment_id.setter
    def environment_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f949624a9b6e222d754ab636966342dbb9eb207d34230837c882091a20f9abac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the deployment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96f77dd19f2c1b41d04318bc8aa9cc8f75808190471ba4922eb58652c55c5e38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdentifier")
    def kms_key_identifier(self) -> typing.Optional[builtins.str]:
        '''The AWS KMS key identifier (key ID, key alias, or key ARN).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdentifier"))

    @kms_key_identifier.setter
    def kms_key_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98b30f15af8144546829026dccf1aaf4fedd94b59dabeb6c8e8d7bc2b71e2efb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["CfnDeployment.TagsProperty"]]:
        '''Metadata to assign to the deployment.'''
        return typing.cast(typing.Optional[typing.List["CfnDeployment.TagsProperty"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["CfnDeployment.TagsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12211b05040a4e1a62df97a0128f266db1c0380eba8db0726824e99ad7241551)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appconfig.CfnDeployment.TagsProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class TagsProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Metadata to assign to the deployment strategy.

            Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.

            :param key: The key-value string map. The valid character set is ``[a-zA-Z+-=._:/]`` . The tag key can be up to 128 characters and must not start with ``aws:`` .
            :param value: The tag value can be up to 256 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-deployment-tags.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appconfig as appconfig
                
                tags_property = appconfig.CfnDeployment.TagsProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f2cbb4f58a4f6b9050d66f9a1afb3573fcfbb1445ae7d29b90ec9f65ac1f836f)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''The key-value string map.

            The valid character set is ``[a-zA-Z+-=._:/]`` . The tag key can be up to 128 characters and must not start with ``aws:`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-deployment-tags.html#cfn-appconfig-deployment-tags-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The tag value can be up to 256 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-deployment-tags.html#cfn-appconfig-deployment-tags-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appconfig.CfnDeploymentProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "configuration_profile_id": "configurationProfileId",
        "configuration_version": "configurationVersion",
        "deployment_strategy_id": "deploymentStrategyId",
        "environment_id": "environmentId",
        "description": "description",
        "kms_key_identifier": "kmsKeyIdentifier",
        "tags": "tags",
    },
)
class CfnDeploymentProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        configuration_profile_id: builtins.str,
        configuration_version: builtins.str,
        deployment_strategy_id: builtins.str,
        environment_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        kms_key_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[CfnDeployment.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDeployment``.

        :param application_id: The application ID.
        :param configuration_profile_id: The configuration profile ID.
        :param configuration_version: The configuration version to deploy. If deploying an AWS AppConfig hosted configuration version, you can specify either the version number or version label. For all other configurations, you must specify the version number.
        :param deployment_strategy_id: The deployment strategy ID.
        :param environment_id: The environment ID.
        :param description: A description of the deployment.
        :param kms_key_identifier: The AWS KMS key identifier (key ID, key alias, or key ARN). AWS AppConfig uses this ID to encrypt the configuration data using a customer managed key.
        :param tags: Metadata to assign to the deployment. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appconfig as appconfig
            
            cfn_deployment_props = appconfig.CfnDeploymentProps(
                application_id="applicationId",
                configuration_profile_id="configurationProfileId",
                configuration_version="configurationVersion",
                deployment_strategy_id="deploymentStrategyId",
                environment_id="environmentId",
            
                # the properties below are optional
                description="description",
                kms_key_identifier="kmsKeyIdentifier",
                tags=[appconfig.CfnDeployment.TagsProperty(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8289d78d65be12b91a60529d6c53d8a4385f73c87b2a23cfef86efebc1e00914)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument configuration_profile_id", value=configuration_profile_id, expected_type=type_hints["configuration_profile_id"])
            check_type(argname="argument configuration_version", value=configuration_version, expected_type=type_hints["configuration_version"])
            check_type(argname="argument deployment_strategy_id", value=deployment_strategy_id, expected_type=type_hints["deployment_strategy_id"])
            check_type(argname="argument environment_id", value=environment_id, expected_type=type_hints["environment_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument kms_key_identifier", value=kms_key_identifier, expected_type=type_hints["kms_key_identifier"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
            "configuration_profile_id": configuration_profile_id,
            "configuration_version": configuration_version,
            "deployment_strategy_id": deployment_strategy_id,
            "environment_id": environment_id,
        }
        if description is not None:
            self._values["description"] = description
        if kms_key_identifier is not None:
            self._values["kms_key_identifier"] = kms_key_identifier
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The application ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration_profile_id(self) -> builtins.str:
        '''The configuration profile ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-configurationprofileid
        '''
        result = self._values.get("configuration_profile_id")
        assert result is not None, "Required property 'configuration_profile_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration_version(self) -> builtins.str:
        '''The configuration version to deploy.

        If deploying an AWS AppConfig hosted configuration version, you can specify either the version number or version label. For all other configurations, you must specify the version number.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-configurationversion
        '''
        result = self._values.get("configuration_version")
        assert result is not None, "Required property 'configuration_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def deployment_strategy_id(self) -> builtins.str:
        '''The deployment strategy ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-deploymentstrategyid
        '''
        result = self._values.get("deployment_strategy_id")
        assert result is not None, "Required property 'deployment_strategy_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_id(self) -> builtins.str:
        '''The environment ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-environmentid
        '''
        result = self._values.get("environment_id")
        assert result is not None, "Required property 'environment_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the deployment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_identifier(self) -> typing.Optional[builtins.str]:
        '''The AWS KMS key identifier (key ID, key alias, or key ARN).

        AWS AppConfig uses this ID to encrypt the configuration data using a customer managed key.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-kmskeyidentifier
        '''
        result = self._values.get("kms_key_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[CfnDeployment.TagsProperty]]:
        '''Metadata to assign to the deployment.

        Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[CfnDeployment.TagsProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeploymentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnDeploymentStrategy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appconfig.CfnDeploymentStrategy",
):
    '''The ``AWS::AppConfig::DeploymentStrategy`` resource creates an AWS AppConfig deployment strategy.

    A deployment strategy defines important criteria for rolling out your configuration to the designated targets. A deployment strategy includes: the overall duration required, a percentage of targets to receive the deployment during each interval, an algorithm that defines how percentage grows, and bake time.

    AWS AppConfig requires that you create resources and deploy a configuration in the following order:

    - Create an application
    - Create an environment
    - Create a configuration profile
    - Create a deployment strategy
    - Deploy the configuration

    For more information, see `AWS AppConfig <https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html>`_ in the *AWS AppConfig User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appconfig as appconfig
        
        cfn_deployment_strategy = appconfig.CfnDeploymentStrategy(self, "MyCfnDeploymentStrategy",
            deployment_duration_in_minutes=123,
            growth_factor=123,
            name="name",
            replicate_to="replicateTo",
        
            # the properties below are optional
            description="description",
            final_bake_time_in_minutes=123,
            growth_type="growthType",
            tags=[appconfig.CfnDeploymentStrategy.TagsProperty(
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
        deployment_duration_in_minutes: jsii.Number,
        growth_factor: jsii.Number,
        name: builtins.str,
        replicate_to: builtins.str,
        description: typing.Optional[builtins.str] = None,
        final_bake_time_in_minutes: typing.Optional[jsii.Number] = None,
        growth_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["CfnDeploymentStrategy.TagsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param deployment_duration_in_minutes: Total amount of time for a deployment to last.
        :param growth_factor: The percentage of targets to receive a deployed configuration during each interval.
        :param name: A name for the deployment strategy.
        :param replicate_to: Save the deployment strategy to a Systems Manager (SSM) document.
        :param description: A description of the deployment strategy.
        :param final_bake_time_in_minutes: Specifies the amount of time AWS AppConfig monitors for Amazon CloudWatch alarms after the configuration has been deployed to 100% of its targets, before considering the deployment to be complete. If an alarm is triggered during this time, AWS AppConfig rolls back the deployment. You must configure permissions for AWS AppConfig to roll back based on CloudWatch alarms. For more information, see `Configuring permissions for rollback based on Amazon CloudWatch alarms <https://docs.aws.amazon.com/appconfig/latest/userguide/getting-started-with-appconfig-cloudwatch-alarms-permissions.html>`_ in the *AWS AppConfig User Guide* .
        :param growth_type: The algorithm used to define how percentage grows over time. AWS AppConfig supports the following growth types:. *Linear* : For this type, AWS AppConfig processes the deployment by dividing the total number of targets by the value specified for ``Step percentage`` . For example, a linear deployment that uses a ``Step percentage`` of 10 deploys the configuration to 10 percent of the hosts. After those deployments are complete, the system deploys the configuration to the next 10 percent. This continues until 100% of the targets have successfully received the configuration. *Exponential* : For this type, AWS AppConfig processes the deployment exponentially using the following formula: ``G*(2^N)`` . In this formula, ``G`` is the growth factor specified by the user and ``N`` is the number of steps until the configuration is deployed to all targets. For example, if you specify a growth factor of 2, then the system rolls out the configuration as follows: ``2*(2^0)`` ``2*(2^1)`` ``2*(2^2)`` Expressed numerically, the deployment rolls out as follows: 2% of the targets, 4% of the targets, 8% of the targets, and continues until the configuration has been deployed to all targets.
        :param tags: Assigns metadata to an AWS AppConfig resource. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define. You can specify a maximum of 50 tags for a resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb88c221f102c1b57ba4f19db7656eb36ff011a70e3643e39d048c313eda22fd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDeploymentStrategyProps(
            deployment_duration_in_minutes=deployment_duration_in_minutes,
            growth_factor=growth_factor,
            name=name,
            replicate_to=replicate_to,
            description=description,
            final_bake_time_in_minutes=final_bake_time_in_minutes,
            growth_type=growth_type,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c07282bd387e2aab09e9241f96ded37ff336d3f231f996e048ef207d3a38bc3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__750f81fb9177952991767d28a4a55a4de59c55177b25056fdd45e8aff0c293c2)
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
    @jsii.member(jsii_name="deploymentDurationInMinutes")
    def deployment_duration_in_minutes(self) -> jsii.Number:
        '''Total amount of time for a deployment to last.'''
        return typing.cast(jsii.Number, jsii.get(self, "deploymentDurationInMinutes"))

    @deployment_duration_in_minutes.setter
    def deployment_duration_in_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2b9cfcca9dae7bf599adef5f2b44e7662994e8143e1b3ccfa6f12c4d8ad5a19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentDurationInMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="growthFactor")
    def growth_factor(self) -> jsii.Number:
        '''The percentage of targets to receive a deployed configuration during each interval.'''
        return typing.cast(jsii.Number, jsii.get(self, "growthFactor"))

    @growth_factor.setter
    def growth_factor(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ac4cbcedcf27ec80d55a98d836dbb9ac52523d6ff7838145b4d527fadaf652d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "growthFactor", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A name for the deployment strategy.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43a46b42e0607ca1c01aa58dff3034f44511b63f99f559fe0fd370080f52f2c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="replicateTo")
    def replicate_to(self) -> builtins.str:
        '''Save the deployment strategy to a Systems Manager (SSM) document.'''
        return typing.cast(builtins.str, jsii.get(self, "replicateTo"))

    @replicate_to.setter
    def replicate_to(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb6ef1a3102939b024e6e99b451674a1ad1f6879f5355a20a6d365cfeab4ad4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicateTo", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the deployment strategy.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f47275a573fd911ba6db69f152dd00eab69b450d732941105375d198524fd2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="finalBakeTimeInMinutes")
    def final_bake_time_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''Specifies the amount of time AWS AppConfig monitors for Amazon CloudWatch alarms after the configuration has been deployed to 100% of its targets, before considering the deployment to be complete.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "finalBakeTimeInMinutes"))

    @final_bake_time_in_minutes.setter
    def final_bake_time_in_minutes(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad18c900d6d84d1f1dba268d6d666b830e5e5276badda4b775deb06725f3c4ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "finalBakeTimeInMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="growthType")
    def growth_type(self) -> typing.Optional[builtins.str]:
        '''The algorithm used to define how percentage grows over time.

        AWS AppConfig supports the following growth types:.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "growthType"))

    @growth_type.setter
    def growth_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38dbe338fc520a7ce3134f048d86265b2db4966fa73c38281b48ff6124acbc16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "growthType", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(
        self,
    ) -> typing.Optional[typing.List["CfnDeploymentStrategy.TagsProperty"]]:
        '''Assigns metadata to an AWS AppConfig resource.'''
        return typing.cast(typing.Optional[typing.List["CfnDeploymentStrategy.TagsProperty"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["CfnDeploymentStrategy.TagsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b0c7e44af284b89d6923411489d05fa28350784f8d88a837a0d019a1d575e65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appconfig.CfnDeploymentStrategy.TagsProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class TagsProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Metadata to assign to the deployment strategy.

            Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.

            :param key: The key-value string map. The valid character set is ``[a-zA-Z+-=._:/]`` . The tag key can be up to 128 characters and must not start with ``aws:`` .
            :param value: The tag value can be up to 256 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-deploymentstrategy-tags.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appconfig as appconfig
                
                tags_property = appconfig.CfnDeploymentStrategy.TagsProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__788f9166b700f88792d30ba7d0b953bc14938d30ade630f5fe723e23a497207d)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''The key-value string map.

            The valid character set is ``[a-zA-Z+-=._:/]`` . The tag key can be up to 128 characters and must not start with ``aws:`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-deploymentstrategy-tags.html#cfn-appconfig-deploymentstrategy-tags-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The tag value can be up to 256 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-deploymentstrategy-tags.html#cfn-appconfig-deploymentstrategy-tags-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appconfig.CfnDeploymentStrategyProps",
    jsii_struct_bases=[],
    name_mapping={
        "deployment_duration_in_minutes": "deploymentDurationInMinutes",
        "growth_factor": "growthFactor",
        "name": "name",
        "replicate_to": "replicateTo",
        "description": "description",
        "final_bake_time_in_minutes": "finalBakeTimeInMinutes",
        "growth_type": "growthType",
        "tags": "tags",
    },
)
class CfnDeploymentStrategyProps:
    def __init__(
        self,
        *,
        deployment_duration_in_minutes: jsii.Number,
        growth_factor: jsii.Number,
        name: builtins.str,
        replicate_to: builtins.str,
        description: typing.Optional[builtins.str] = None,
        final_bake_time_in_minutes: typing.Optional[jsii.Number] = None,
        growth_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[CfnDeploymentStrategy.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDeploymentStrategy``.

        :param deployment_duration_in_minutes: Total amount of time for a deployment to last.
        :param growth_factor: The percentage of targets to receive a deployed configuration during each interval.
        :param name: A name for the deployment strategy.
        :param replicate_to: Save the deployment strategy to a Systems Manager (SSM) document.
        :param description: A description of the deployment strategy.
        :param final_bake_time_in_minutes: Specifies the amount of time AWS AppConfig monitors for Amazon CloudWatch alarms after the configuration has been deployed to 100% of its targets, before considering the deployment to be complete. If an alarm is triggered during this time, AWS AppConfig rolls back the deployment. You must configure permissions for AWS AppConfig to roll back based on CloudWatch alarms. For more information, see `Configuring permissions for rollback based on Amazon CloudWatch alarms <https://docs.aws.amazon.com/appconfig/latest/userguide/getting-started-with-appconfig-cloudwatch-alarms-permissions.html>`_ in the *AWS AppConfig User Guide* .
        :param growth_type: The algorithm used to define how percentage grows over time. AWS AppConfig supports the following growth types:. *Linear* : For this type, AWS AppConfig processes the deployment by dividing the total number of targets by the value specified for ``Step percentage`` . For example, a linear deployment that uses a ``Step percentage`` of 10 deploys the configuration to 10 percent of the hosts. After those deployments are complete, the system deploys the configuration to the next 10 percent. This continues until 100% of the targets have successfully received the configuration. *Exponential* : For this type, AWS AppConfig processes the deployment exponentially using the following formula: ``G*(2^N)`` . In this formula, ``G`` is the growth factor specified by the user and ``N`` is the number of steps until the configuration is deployed to all targets. For example, if you specify a growth factor of 2, then the system rolls out the configuration as follows: ``2*(2^0)`` ``2*(2^1)`` ``2*(2^2)`` Expressed numerically, the deployment rolls out as follows: 2% of the targets, 4% of the targets, 8% of the targets, and continues until the configuration has been deployed to all targets.
        :param tags: Assigns metadata to an AWS AppConfig resource. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define. You can specify a maximum of 50 tags for a resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appconfig as appconfig
            
            cfn_deployment_strategy_props = appconfig.CfnDeploymentStrategyProps(
                deployment_duration_in_minutes=123,
                growth_factor=123,
                name="name",
                replicate_to="replicateTo",
            
                # the properties below are optional
                description="description",
                final_bake_time_in_minutes=123,
                growth_type="growthType",
                tags=[appconfig.CfnDeploymentStrategy.TagsProperty(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__199999cc14040404b938fa601301d483ec681a01c3bd23495d2d90dde59820b5)
            check_type(argname="argument deployment_duration_in_minutes", value=deployment_duration_in_minutes, expected_type=type_hints["deployment_duration_in_minutes"])
            check_type(argname="argument growth_factor", value=growth_factor, expected_type=type_hints["growth_factor"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument replicate_to", value=replicate_to, expected_type=type_hints["replicate_to"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument final_bake_time_in_minutes", value=final_bake_time_in_minutes, expected_type=type_hints["final_bake_time_in_minutes"])
            check_type(argname="argument growth_type", value=growth_type, expected_type=type_hints["growth_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "deployment_duration_in_minutes": deployment_duration_in_minutes,
            "growth_factor": growth_factor,
            "name": name,
            "replicate_to": replicate_to,
        }
        if description is not None:
            self._values["description"] = description
        if final_bake_time_in_minutes is not None:
            self._values["final_bake_time_in_minutes"] = final_bake_time_in_minutes
        if growth_type is not None:
            self._values["growth_type"] = growth_type
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def deployment_duration_in_minutes(self) -> jsii.Number:
        '''Total amount of time for a deployment to last.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-deploymentdurationinminutes
        '''
        result = self._values.get("deployment_duration_in_minutes")
        assert result is not None, "Required property 'deployment_duration_in_minutes' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def growth_factor(self) -> jsii.Number:
        '''The percentage of targets to receive a deployed configuration during each interval.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-growthfactor
        '''
        result = self._values.get("growth_factor")
        assert result is not None, "Required property 'growth_factor' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A name for the deployment strategy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def replicate_to(self) -> builtins.str:
        '''Save the deployment strategy to a Systems Manager (SSM) document.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-replicateto
        '''
        result = self._values.get("replicate_to")
        assert result is not None, "Required property 'replicate_to' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the deployment strategy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def final_bake_time_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''Specifies the amount of time AWS AppConfig monitors for Amazon CloudWatch alarms after the configuration has been deployed to 100% of its targets, before considering the deployment to be complete.

        If an alarm is triggered during this time, AWS AppConfig rolls back the deployment. You must configure permissions for AWS AppConfig to roll back based on CloudWatch alarms. For more information, see `Configuring permissions for rollback based on Amazon CloudWatch alarms <https://docs.aws.amazon.com/appconfig/latest/userguide/getting-started-with-appconfig-cloudwatch-alarms-permissions.html>`_ in the *AWS AppConfig User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-finalbaketimeinminutes
        '''
        result = self._values.get("final_bake_time_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def growth_type(self) -> typing.Optional[builtins.str]:
        '''The algorithm used to define how percentage grows over time. AWS AppConfig supports the following growth types:.

        *Linear* : For this type, AWS AppConfig processes the deployment by dividing the total number of targets by the value specified for ``Step percentage`` . For example, a linear deployment that uses a ``Step percentage`` of 10 deploys the configuration to 10 percent of the hosts. After those deployments are complete, the system deploys the configuration to the next 10 percent. This continues until 100% of the targets have successfully received the configuration.

        *Exponential* : For this type, AWS AppConfig processes the deployment exponentially using the following formula: ``G*(2^N)`` . In this formula, ``G`` is the growth factor specified by the user and ``N`` is the number of steps until the configuration is deployed to all targets. For example, if you specify a growth factor of 2, then the system rolls out the configuration as follows:

        ``2*(2^0)``

        ``2*(2^1)``

        ``2*(2^2)``

        Expressed numerically, the deployment rolls out as follows: 2% of the targets, 4% of the targets, 8% of the targets, and continues until the configuration has been deployed to all targets.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-growthtype
        '''
        result = self._values.get("growth_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[CfnDeploymentStrategy.TagsProperty]]:
        '''Assigns metadata to an AWS AppConfig resource.

        Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define. You can specify a maximum of 50 tags for a resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[CfnDeploymentStrategy.TagsProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeploymentStrategyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnEnvironment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appconfig.CfnEnvironment",
):
    '''The ``AWS::AppConfig::Environment`` resource creates an environment, which is a logical deployment group of AWS AppConfig targets, such as applications in a ``Beta`` or ``Production`` environment.

    You define one or more environments for each AWS AppConfig application. You can also define environments for application subcomponents such as the ``Web`` , ``Mobile`` and ``Back-end`` components for your application. You can configure Amazon CloudWatch alarms for each environment. The system monitors alarms during a configuration deployment. If an alarm is triggered, the system rolls back the configuration.

    AWS AppConfig requires that you create resources and deploy a configuration in the following order:

    - Create an application
    - Create an environment
    - Create a configuration profile
    - Create a deployment strategy
    - Deploy the configuration

    For more information, see `AWS AppConfig <https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html>`_ in the *AWS AppConfig User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appconfig as appconfig
        
        cfn_environment = appconfig.CfnEnvironment(self, "MyCfnEnvironment",
            application_id="applicationId",
            name="name",
        
            # the properties below are optional
            description="description",
            monitors=[appconfig.CfnEnvironment.MonitorsProperty(
                alarm_arn="alarmArn",
                alarm_role_arn="alarmRoleArn"
            )],
            tags=[appconfig.CfnEnvironment.TagsProperty(
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
        application_id: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        monitors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.MonitorsProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["CfnEnvironment.TagsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_id: The application ID.
        :param name: A name for the environment.
        :param description: A description of the environment.
        :param monitors: Amazon CloudWatch alarms to monitor during the deployment process.
        :param tags: Metadata to assign to the environment. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f357d5cab83004926812cf34c99a144f4f5d23ca26e4a818590a950622a06fc3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEnvironmentProps(
            application_id=application_id,
            name=name,
            description=description,
            monitors=monitors,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3842dacad1a08e5d9103a4c646c8fa2385f77b6f5495fbd4dab597c037c8f09b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2dbe73a2ef533ed22edd7fd274c6cca5a979759478da06114e8699f7b2409820)
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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The application ID.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d35c6a50b39401e18b97d5d78f1d4d92aaf846c18aa4ec32bce024a53e54c4be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A name for the environment.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__569391bda37ae2bcb096c8b3ab953d25c7ff488899b2557c773cc8f72ee8a4cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the environment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__154bd59aabeed21e27800d9d45bcdbb412639a65e9aaaf72ef6dae673fa26a43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="monitors")
    def monitors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.MonitorsProperty"]]]]:
        '''Amazon CloudWatch alarms to monitor during the deployment process.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.MonitorsProperty"]]]], jsii.get(self, "monitors"))

    @monitors.setter
    def monitors(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.MonitorsProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8d099ead34dfe7be9eb945722b31207889d993d21d927e1eeba6592c7f8fd44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitors", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["CfnEnvironment.TagsProperty"]]:
        '''Metadata to assign to the environment.'''
        return typing.cast(typing.Optional[typing.List["CfnEnvironment.TagsProperty"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["CfnEnvironment.TagsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60701727c0b2b8f0404d231ccc24899f35678bacc781ed4c6443de1b14432f68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appconfig.CfnEnvironment.MonitorsProperty",
        jsii_struct_bases=[],
        name_mapping={"alarm_arn": "alarmArn", "alarm_role_arn": "alarmRoleArn"},
    )
    class MonitorsProperty:
        def __init__(
            self,
            *,
            alarm_arn: typing.Optional[builtins.str] = None,
            alarm_role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Amazon CloudWatch alarms to monitor during the deployment process.

            :param alarm_arn: Amazon Resource Name (ARN) of the Amazon CloudWatch alarm.
            :param alarm_role_arn: ARN of an AWS Identity and Access Management (IAM) role for AWS AppConfig to monitor ``AlarmArn`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-monitors.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appconfig as appconfig
                
                monitors_property = appconfig.CfnEnvironment.MonitorsProperty(
                    alarm_arn="alarmArn",
                    alarm_role_arn="alarmRoleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__43d91f41d1c9d1acd545d0999d47687e0e5b7be03ec08728e3c5aa73ff76549f)
                check_type(argname="argument alarm_arn", value=alarm_arn, expected_type=type_hints["alarm_arn"])
                check_type(argname="argument alarm_role_arn", value=alarm_role_arn, expected_type=type_hints["alarm_role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if alarm_arn is not None:
                self._values["alarm_arn"] = alarm_arn
            if alarm_role_arn is not None:
                self._values["alarm_role_arn"] = alarm_role_arn

        @builtins.property
        def alarm_arn(self) -> typing.Optional[builtins.str]:
            '''Amazon Resource Name (ARN) of the Amazon CloudWatch alarm.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-monitors.html#cfn-appconfig-environment-monitors-alarmarn
            '''
            result = self._values.get("alarm_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def alarm_role_arn(self) -> typing.Optional[builtins.str]:
            '''ARN of an AWS Identity and Access Management (IAM) role for AWS AppConfig to monitor ``AlarmArn`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-monitors.html#cfn-appconfig-environment-monitors-alarmrolearn
            '''
            result = self._values.get("alarm_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitorsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appconfig.CfnEnvironment.TagsProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class TagsProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Metadata to assign to the environment.

            Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.

            :param key: The key-value string map. The valid character set is ``[a-zA-Z+-=._:/]`` . The tag key can be up to 128 characters and must not start with ``aws:`` .
            :param value: The tag value can be up to 256 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-tags.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appconfig as appconfig
                
                tags_property = appconfig.CfnEnvironment.TagsProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8f58f801045a8e3c147c3d78dc98e6b7aa29fb1f248587805b6f76a3486e6436)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''The key-value string map.

            The valid character set is ``[a-zA-Z+-=._:/]`` . The tag key can be up to 128 characters and must not start with ``aws:`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-tags.html#cfn-appconfig-environment-tags-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The tag value can be up to 256 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-tags.html#cfn-appconfig-environment-tags-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appconfig.CfnEnvironmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "name": "name",
        "description": "description",
        "monitors": "monitors",
        "tags": "tags",
    },
)
class CfnEnvironmentProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        monitors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.MonitorsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[CfnEnvironment.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEnvironment``.

        :param application_id: The application ID.
        :param name: A name for the environment.
        :param description: A description of the environment.
        :param monitors: Amazon CloudWatch alarms to monitor during the deployment process.
        :param tags: Metadata to assign to the environment. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appconfig as appconfig
            
            cfn_environment_props = appconfig.CfnEnvironmentProps(
                application_id="applicationId",
                name="name",
            
                # the properties below are optional
                description="description",
                monitors=[appconfig.CfnEnvironment.MonitorsProperty(
                    alarm_arn="alarmArn",
                    alarm_role_arn="alarmRoleArn"
                )],
                tags=[appconfig.CfnEnvironment.TagsProperty(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6c9856f1a5a9dfaed9be42ec835bb6eac4d4882999b993cbd02b3b11bbfe1ca)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument monitors", value=monitors, expected_type=type_hints["monitors"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if monitors is not None:
            self._values["monitors"] = monitors
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The application ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A name for the environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def monitors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironment.MonitorsProperty]]]]:
        '''Amazon CloudWatch alarms to monitor during the deployment process.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-monitors
        '''
        result = self._values.get("monitors")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironment.MonitorsProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[CfnEnvironment.TagsProperty]]:
        '''Metadata to assign to the environment.

        Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[CfnEnvironment.TagsProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEnvironmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnExtension(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appconfig.CfnExtension",
):
    '''Creates an AWS AppConfig extension.

    An extension augments your ability to inject logic or behavior at different points during the AWS AppConfig workflow of creating or deploying a configuration.

    You can create your own extensions or use the AWS authored extensions provided by AWS AppConfig . For an AWS AppConfig extension that uses AWS Lambda , you must create a Lambda function to perform any computation and processing defined in the extension. If you plan to create custom versions of the AWS authored notification extensions, you only need to specify an Amazon Resource Name (ARN) in the ``Uri`` field for the new extension version.

    - For a custom EventBridge notification extension, enter the ARN of the EventBridge default events in the ``Uri`` field.
    - For a custom Amazon SNS notification extension, enter the ARN of an Amazon SNS topic in the ``Uri`` field.
    - For a custom Amazon SQS notification extension, enter the ARN of an Amazon SQS message queue in the ``Uri`` field.

    For more information about extensions, see `Working with AWS AppConfig extensions <https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html>`_ in the *AWS AppConfig User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extension.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appconfig as appconfig
        
        # actions: Any
        
        cfn_extension = appconfig.CfnExtension(self, "MyCfnExtension",
            actions=actions,
            name="name",
        
            # the properties below are optional
            description="description",
            latest_version_number=123,
            parameters={
                "parameters_key": appconfig.CfnExtension.ParameterProperty(
                    required=False,
        
                    # the properties below are optional
                    description="description"
                )
            },
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
        actions: typing.Any,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union["CfnExtension.ParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param actions: The actions defined in the extension.
        :param name: A name for the extension. Each extension name in your account must be unique. Extension versions use the same name.
        :param description: Information about the extension.
        :param latest_version_number: You can omit this field when you create an extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field.
        :param parameters: The parameters accepted by the extension. You specify parameter values when you associate the extension to an AWS AppConfig resource by using the ``CreateExtensionAssociation`` API action. For AWS Lambda extension actions, these parameters are included in the Lambda request object.
        :param tags: Adds one or more tags for the specified extension. Tags are metadata that help you categorize resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3442a7f4d7a9c3256544c6b0526d285ef0cf3970ec1f140b344aed1abc4eef5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnExtensionProps(
            actions=actions,
            name=name,
            description=description,
            latest_version_number=latest_version_number,
            parameters=parameters,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6930a24c04bd5aebe54f7a225f7ec08743e520b61a781973e88a4b6678524a5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__57070195544dc008ade09c677ffa495cf4120e6b1dc834d6ffa101c3cf189599)
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
        '''The system-generated Amazon Resource Name (ARN) for the extension.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The system-generated ID of the extension.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrVersionNumber")
    def attr_version_number(self) -> jsii.Number:
        '''The extension version number.

        :cloudformationAttribute: VersionNumber
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrVersionNumber"))

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
    @jsii.member(jsii_name="actions")
    def actions(self) -> typing.Any:
        '''The actions defined in the extension.'''
        return typing.cast(typing.Any, jsii.get(self, "actions"))

    @actions.setter
    def actions(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f734d5e14d1ac32f7ec277282f23b1f2f7c0b8ce8e48d8df2b080f67d200577f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actions", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A name for the extension.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__081c55af29bf24c3599cf24134be4ce60656f052c575f59ff68c2084fa523481)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''Information about the extension.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__334508667f33fe5d26ff2e39e3bcbaaea618391e439f25094004fab0d75eb718)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="latestVersionNumber")
    def latest_version_number(self) -> typing.Optional[jsii.Number]:
        '''You can omit this field when you create an extension.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "latestVersionNumber"))

    @latest_version_number.setter
    def latest_version_number(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b38bdb75b51870401d0b83754078af02e3e6886d97a64481c3733b63a5a4c814)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "latestVersionNumber", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnExtension.ParameterProperty"]]]]:
        '''The parameters accepted by the extension.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnExtension.ParameterProperty"]]]], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnExtension.ParameterProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ad5fbf78cb34accb172520e561c08795fbca80280af2dcc78243ceb84841d07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Adds one or more tags for the specified extension.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e6cc683bfd791a6ddfdc2295e58057279b3a19bc4adc7a11fbff993fe64fe37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appconfig.CfnExtension.ActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "uri": "uri",
            "description": "description",
            "role_arn": "roleArn",
        },
    )
    class ActionProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            uri: builtins.str,
            description: typing.Optional[builtins.str] = None,
            role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An action for an extension to take at a specific action point.

            :param name: The name of the extension action.
            :param uri: The URI of the extension action.
            :param description: The description of the extension Action.
            :param role_arn: The ARN of the role for invoking the extension action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-extension-action.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appconfig as appconfig
                
                action_property = appconfig.CfnExtension.ActionProperty(
                    name="name",
                    uri="uri",
                
                    # the properties below are optional
                    description="description",
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__58317247cdf8a690d14849381527f22c6a038c04470bb6ed420b3ade323b7e43)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "uri": uri,
            }
            if description is not None:
                self._values["description"] = description
            if role_arn is not None:
                self._values["role_arn"] = role_arn

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the extension action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-extension-action.html#cfn-appconfig-extension-action-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def uri(self) -> builtins.str:
            '''The URI of the extension action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-extension-action.html#cfn-appconfig-extension-action-uri
            '''
            result = self._values.get("uri")
            assert result is not None, "Required property 'uri' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The description of the extension Action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-extension-action.html#cfn-appconfig-extension-action-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the role for invoking the extension action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-extension-action.html#cfn-appconfig-extension-action-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appconfig.CfnExtension.ParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"required": "required", "description": "description"},
    )
    class ParameterProperty:
        def __init__(
            self,
            *,
            required: typing.Union[builtins.bool, _IResolvable_da3f097b],
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A value such as an Amazon Resource Name (ARN) or an Amazon Simple Notification Service topic entered in an extension when invoked.

            Parameter values are specified in an extension association. For more information about extensions, see `Working with AWS AppConfig extensions <https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html>`_ in the *AWS AppConfig User Guide* .

            :param required: A parameter value must be specified in the extension association.
            :param description: Information about the parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-extension-parameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appconfig as appconfig
                
                parameter_property = appconfig.CfnExtension.ParameterProperty(
                    required=False,
                
                    # the properties below are optional
                    description="description"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__683bc731900456f8d594ddc90d3c7fc1fcdc884942410401537639fad3d02ed1)
                check_type(argname="argument required", value=required, expected_type=type_hints["required"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "required": required,
            }
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def required(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''A parameter value must be specified in the extension association.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-extension-parameter.html#cfn-appconfig-extension-parameter-required
            '''
            result = self._values.get("required")
            assert result is not None, "Required property 'required' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''Information about the parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-extension-parameter.html#cfn-appconfig-extension-parameter-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnExtensionAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appconfig.CfnExtensionAssociation",
):
    '''When you create an extension or configure an AWS authored extension, you associate the extension with an AWS AppConfig application, environment, or configuration profile.

    For example, you can choose to run the ``AWS AppConfig deployment events to Amazon SNS`` AWS authored extension and receive notifications on an Amazon SNS topic anytime a configuration deployment is started for a specific application. Defining which extension to associate with an AWS AppConfig resource is called an *extension association* . An extension association is a specified relationship between an extension and an AWS AppConfig resource, such as an application or a configuration profile. For more information about extensions and associations, see `Working with AWS AppConfig extensions <https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html>`_ in the *AWS AppConfig User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extensionassociation.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appconfig as appconfig
        
        cfn_extension_association = appconfig.CfnExtensionAssociation(self, "MyCfnExtensionAssociation",
            extension_identifier="extensionIdentifier",
            extension_version_number=123,
            parameters={
                "parameters_key": "parameters"
            },
            resource_identifier="resourceIdentifier",
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
        extension_identifier: typing.Optional[builtins.str] = None,
        extension_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
        resource_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param extension_identifier: The name, the ID, or the Amazon Resource Name (ARN) of the extension.
        :param extension_version_number: The version number of the extension. If not specified, AWS AppConfig uses the maximum version of the extension.
        :param parameters: The parameter names and values defined in the extensions. Extension parameters marked ``Required`` must be entered for this field.
        :param resource_identifier: The ARN of an application, configuration profile, or environment.
        :param tags: Adds one or more tags for the specified extension association. Tags are metadata that help you categorize resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2e5a069dff64a93330fdfc39cee819956ed46cafa89dc1aee558b0c288de8af)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnExtensionAssociationProps(
            extension_identifier=extension_identifier,
            extension_version_number=extension_version_number,
            parameters=parameters,
            resource_identifier=resource_identifier,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__209622600665bfa16663cc19d0b91c8caf5c5d29f4cc7cb09fd6fba67bcb1739)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d0a9f34459bdf3e807e0362d7767352a597304250be35f36b98afb6b8d6ca733)
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
        '''The ARN of the extension defined in the association.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrExtensionArn")
    def attr_extension_arn(self) -> builtins.str:
        '''The ARN of the extension defined in the association.

        :cloudformationAttribute: ExtensionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrExtensionArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The system-generated ID for the association.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrResourceArn")
    def attr_resource_arn(self) -> builtins.str:
        '''The ARNs of applications, configuration profiles, or environments defined in the association.

        :cloudformationAttribute: ResourceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceArn"))

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
    @jsii.member(jsii_name="extensionIdentifier")
    def extension_identifier(self) -> typing.Optional[builtins.str]:
        '''The name, the ID, or the Amazon Resource Name (ARN) of the extension.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "extensionIdentifier"))

    @extension_identifier.setter
    def extension_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd635cb248fd501f641536d553e5645fb6dd03b8db84e4059ddc6af591a307e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extensionIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="extensionVersionNumber")
    def extension_version_number(self) -> typing.Optional[jsii.Number]:
        '''The version number of the extension.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "extensionVersionNumber"))

    @extension_version_number.setter
    def extension_version_number(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4aa600ead50aeb1f2d5f5f5fe334e3e11a16eccfa413e5de0742f763f7938a43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extensionVersionNumber", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
        '''The parameter names and values defined in the extensions.'''
        return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(
        self,
        value: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc72677d37ba0fe5b56dcbee5b8705c9e4e30a75b5d3b051bc792305dfd3deda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="resourceIdentifier")
    def resource_identifier(self) -> typing.Optional[builtins.str]:
        '''The ARN of an application, configuration profile, or environment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceIdentifier"))

    @resource_identifier.setter
    def resource_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ff48a7c10c5007769564f0b18da5363288efbb9ca805f7bb5a7fd93e791ec3d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Adds one or more tags for the specified extension association.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d31c336e3843162aab44371392cbb25a2b62fcd270c6fc472b3f2819a21b9ea1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appconfig.CfnExtensionAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "extension_identifier": "extensionIdentifier",
        "extension_version_number": "extensionVersionNumber",
        "parameters": "parameters",
        "resource_identifier": "resourceIdentifier",
        "tags": "tags",
    },
)
class CfnExtensionAssociationProps:
    def __init__(
        self,
        *,
        extension_identifier: typing.Optional[builtins.str] = None,
        extension_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
        resource_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnExtensionAssociation``.

        :param extension_identifier: The name, the ID, or the Amazon Resource Name (ARN) of the extension.
        :param extension_version_number: The version number of the extension. If not specified, AWS AppConfig uses the maximum version of the extension.
        :param parameters: The parameter names and values defined in the extensions. Extension parameters marked ``Required`` must be entered for this field.
        :param resource_identifier: The ARN of an application, configuration profile, or environment.
        :param tags: Adds one or more tags for the specified extension association. Tags are metadata that help you categorize resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extensionassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appconfig as appconfig
            
            cfn_extension_association_props = appconfig.CfnExtensionAssociationProps(
                extension_identifier="extensionIdentifier",
                extension_version_number=123,
                parameters={
                    "parameters_key": "parameters"
                },
                resource_identifier="resourceIdentifier",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__658f796ad2928720e80bab1455b7c28527f38d13b4efe7780e0a592469829ce9)
            check_type(argname="argument extension_identifier", value=extension_identifier, expected_type=type_hints["extension_identifier"])
            check_type(argname="argument extension_version_number", value=extension_version_number, expected_type=type_hints["extension_version_number"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument resource_identifier", value=resource_identifier, expected_type=type_hints["resource_identifier"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if extension_identifier is not None:
            self._values["extension_identifier"] = extension_identifier
        if extension_version_number is not None:
            self._values["extension_version_number"] = extension_version_number
        if parameters is not None:
            self._values["parameters"] = parameters
        if resource_identifier is not None:
            self._values["resource_identifier"] = resource_identifier
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def extension_identifier(self) -> typing.Optional[builtins.str]:
        '''The name, the ID, or the Amazon Resource Name (ARN) of the extension.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extensionassociation.html#cfn-appconfig-extensionassociation-extensionidentifier
        '''
        result = self._values.get("extension_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extension_version_number(self) -> typing.Optional[jsii.Number]:
        '''The version number of the extension.

        If not specified, AWS AppConfig uses the maximum version of the extension.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extensionassociation.html#cfn-appconfig-extensionassociation-extensionversionnumber
        '''
        result = self._values.get("extension_version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
        '''The parameter names and values defined in the extensions.

        Extension parameters marked ``Required`` must be entered for this field.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extensionassociation.html#cfn-appconfig-extensionassociation-parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], result)

    @builtins.property
    def resource_identifier(self) -> typing.Optional[builtins.str]:
        '''The ARN of an application, configuration profile, or environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extensionassociation.html#cfn-appconfig-extensionassociation-resourceidentifier
        '''
        result = self._values.get("resource_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Adds one or more tags for the specified extension association.

        Tags are metadata that help you categorize resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extensionassociation.html#cfn-appconfig-extensionassociation-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExtensionAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appconfig.CfnExtensionProps",
    jsii_struct_bases=[],
    name_mapping={
        "actions": "actions",
        "name": "name",
        "description": "description",
        "latest_version_number": "latestVersionNumber",
        "parameters": "parameters",
        "tags": "tags",
    },
)
class CfnExtensionProps:
    def __init__(
        self,
        *,
        actions: typing.Any,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnExtension.ParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnExtension``.

        :param actions: The actions defined in the extension.
        :param name: A name for the extension. Each extension name in your account must be unique. Extension versions use the same name.
        :param description: Information about the extension.
        :param latest_version_number: You can omit this field when you create an extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field.
        :param parameters: The parameters accepted by the extension. You specify parameter values when you associate the extension to an AWS AppConfig resource by using the ``CreateExtensionAssociation`` API action. For AWS Lambda extension actions, these parameters are included in the Lambda request object.
        :param tags: Adds one or more tags for the specified extension. Tags are metadata that help you categorize resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extension.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appconfig as appconfig
            
            # actions: Any
            
            cfn_extension_props = appconfig.CfnExtensionProps(
                actions=actions,
                name="name",
            
                # the properties below are optional
                description="description",
                latest_version_number=123,
                parameters={
                    "parameters_key": appconfig.CfnExtension.ParameterProperty(
                        required=False,
            
                        # the properties below are optional
                        description="description"
                    )
                },
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a81148d01bee60e4140891afd5b9da3eab7a3dd5f81524eaa37f895ff781df1f)
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument latest_version_number", value=latest_version_number, expected_type=type_hints["latest_version_number"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "actions": actions,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if latest_version_number is not None:
            self._values["latest_version_number"] = latest_version_number
        if parameters is not None:
            self._values["parameters"] = parameters
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def actions(self) -> typing.Any:
        '''The actions defined in the extension.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extension.html#cfn-appconfig-extension-actions
        '''
        result = self._values.get("actions")
        assert result is not None, "Required property 'actions' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A name for the extension.

        Each extension name in your account must be unique. Extension versions use the same name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extension.html#cfn-appconfig-extension-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Information about the extension.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extension.html#cfn-appconfig-extension-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def latest_version_number(self) -> typing.Optional[jsii.Number]:
        '''You can omit this field when you create an extension.

        When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extension.html#cfn-appconfig-extension-latestversionnumber
        '''
        result = self._values.get("latest_version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnExtension.ParameterProperty]]]]:
        '''The parameters accepted by the extension.

        You specify parameter values when you associate the extension to an AWS AppConfig resource by using the ``CreateExtensionAssociation`` API action. For AWS Lambda extension actions, these parameters are included in the Lambda request object.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extension.html#cfn-appconfig-extension-parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnExtension.ParameterProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Adds one or more tags for the specified extension.

        Tags are metadata that help you categorize resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extension.html#cfn-appconfig-extension-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExtensionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnHostedConfigurationVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appconfig.CfnHostedConfigurationVersion",
):
    '''Create a new configuration in the AWS AppConfig hosted configuration store.

    Configurations must be 1 MB or smaller. The AWS AppConfig hosted configuration store provides the following benefits over other configuration store options.

    - You don't need to set up and configure other services such as Amazon Simple Storage Service ( Amazon S3 ) or Parameter Store.
    - You don't need to configure AWS Identity and Access Management ( IAM ) permissions to use the configuration store.
    - You can store configurations in any content type.
    - There is no cost to use the store.
    - You can create a configuration and add it to the store when you create a configuration profile.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appconfig as appconfig
        
        cfn_hosted_configuration_version = appconfig.CfnHostedConfigurationVersion(self, "MyCfnHostedConfigurationVersion",
            application_id="applicationId",
            configuration_profile_id="configurationProfileId",
            content="content",
            content_type="contentType",
        
            # the properties below are optional
            description="description",
            latest_version_number=123,
            version_label="versionLabel"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        configuration_profile_id: builtins.str,
        content: builtins.str,
        content_type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        version_label: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_id: The application ID.
        :param configuration_profile_id: The configuration profile ID.
        :param content: The content of the configuration or the configuration data.
        :param content_type: A standard MIME type describing the format of the configuration content. For more information, see `Content-Type <https://docs.aws.amazon.com/https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.17>`_ .
        :param description: A description of the configuration.
        :param latest_version_number: An optional locking token used to prevent race conditions from overwriting configuration updates when creating a new version. To ensure your data is not overwritten when creating multiple hosted configuration versions in rapid succession, specify the version number of the latest hosted configuration version.
        :param version_label: A user-defined label for an AWS AppConfig hosted configuration version.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f2dc9ae7157f5223a79cf8ea4a7355ec285dbe0fda348428c6e0e6cdabbb60b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnHostedConfigurationVersionProps(
            application_id=application_id,
            configuration_profile_id=configuration_profile_id,
            content=content,
            content_type=content_type,
            description=description,
            latest_version_number=latest_version_number,
            version_label=version_label,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__287f244644cef79eb3704756fc9fd6f98e693a42df76727f726091d3190ab82c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__694959938824dc357bd7ac9b60be653c213df7cdcc44905d59d6e7d7e1182171)
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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The application ID.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97e3d21e204bcf08a8dceb763729bfb70936f6d97ed550af3dfe101fac0f4331)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="configurationProfileId")
    def configuration_profile_id(self) -> builtins.str:
        '''The configuration profile ID.'''
        return typing.cast(builtins.str, jsii.get(self, "configurationProfileId"))

    @configuration_profile_id.setter
    def configuration_profile_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4193469efc98930e2e72ffffb47c40bb1631526d907d8eaab051ac721dce3631)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationProfileId", value)

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        '''The content of the configuration or the configuration data.'''
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac0de9d6bf3585fb47f9ad3fbb1d23a9a11447de5c02a24b6971d67ab3a7fa70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        '''A standard MIME type describing the format of the configuration content.'''
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb880ec8c47eca7663501403482ddb505ffe759b4792fa0a7236d31e1313d7fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d43da3f82c30824ce1a2d29683403d6e68cb792341046055e7df42a980951259)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="latestVersionNumber")
    def latest_version_number(self) -> typing.Optional[jsii.Number]:
        '''An optional locking token used to prevent race conditions from overwriting configuration updates when creating a new version.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "latestVersionNumber"))

    @latest_version_number.setter
    def latest_version_number(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14797876de335768bb8254a37ba88bf3300df4a568a8174a333380741acaa4b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "latestVersionNumber", value)

    @builtins.property
    @jsii.member(jsii_name="versionLabel")
    def version_label(self) -> typing.Optional[builtins.str]:
        '''A user-defined label for an AWS AppConfig hosted configuration version.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionLabel"))

    @version_label.setter
    def version_label(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__384487882c55b43a28f4a742590e489e653df19c023a94fbfacb65cdf0cf00e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versionLabel", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appconfig.CfnHostedConfigurationVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "configuration_profile_id": "configurationProfileId",
        "content": "content",
        "content_type": "contentType",
        "description": "description",
        "latest_version_number": "latestVersionNumber",
        "version_label": "versionLabel",
    },
)
class CfnHostedConfigurationVersionProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        configuration_profile_id: builtins.str,
        content: builtins.str,
        content_type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        version_label: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnHostedConfigurationVersion``.

        :param application_id: The application ID.
        :param configuration_profile_id: The configuration profile ID.
        :param content: The content of the configuration or the configuration data.
        :param content_type: A standard MIME type describing the format of the configuration content. For more information, see `Content-Type <https://docs.aws.amazon.com/https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.17>`_ .
        :param description: A description of the configuration.
        :param latest_version_number: An optional locking token used to prevent race conditions from overwriting configuration updates when creating a new version. To ensure your data is not overwritten when creating multiple hosted configuration versions in rapid succession, specify the version number of the latest hosted configuration version.
        :param version_label: A user-defined label for an AWS AppConfig hosted configuration version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appconfig as appconfig
            
            cfn_hosted_configuration_version_props = appconfig.CfnHostedConfigurationVersionProps(
                application_id="applicationId",
                configuration_profile_id="configurationProfileId",
                content="content",
                content_type="contentType",
            
                # the properties below are optional
                description="description",
                latest_version_number=123,
                version_label="versionLabel"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2e12025d283b0b516fc7a346d00f20eff94d8259ba3fc82c8cb240aeb05264e)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument configuration_profile_id", value=configuration_profile_id, expected_type=type_hints["configuration_profile_id"])
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument latest_version_number", value=latest_version_number, expected_type=type_hints["latest_version_number"])
            check_type(argname="argument version_label", value=version_label, expected_type=type_hints["version_label"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
            "configuration_profile_id": configuration_profile_id,
            "content": content,
            "content_type": content_type,
        }
        if description is not None:
            self._values["description"] = description
        if latest_version_number is not None:
            self._values["latest_version_number"] = latest_version_number
        if version_label is not None:
            self._values["version_label"] = version_label

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The application ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration_profile_id(self) -> builtins.str:
        '''The configuration profile ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-configurationprofileid
        '''
        result = self._values.get("configuration_profile_id")
        assert result is not None, "Required property 'configuration_profile_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content(self) -> builtins.str:
        '''The content of the configuration or the configuration data.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-content
        '''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_type(self) -> builtins.str:
        '''A standard MIME type describing the format of the configuration content.

        For more information, see `Content-Type <https://docs.aws.amazon.com/https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.17>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-contenttype
        '''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def latest_version_number(self) -> typing.Optional[jsii.Number]:
        '''An optional locking token used to prevent race conditions from overwriting configuration updates when creating a new version.

        To ensure your data is not overwritten when creating multiple hosted configuration versions in rapid succession, specify the version number of the latest hosted configuration version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-latestversionnumber
        '''
        result = self._values.get("latest_version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def version_label(self) -> typing.Optional[builtins.str]:
        '''A user-defined label for an AWS AppConfig hosted configuration version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-versionlabel
        '''
        result = self._values.get("version_label")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnHostedConfigurationVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApplication",
    "CfnApplicationProps",
    "CfnConfigurationProfile",
    "CfnConfigurationProfileProps",
    "CfnDeployment",
    "CfnDeploymentProps",
    "CfnDeploymentStrategy",
    "CfnDeploymentStrategyProps",
    "CfnEnvironment",
    "CfnEnvironmentProps",
    "CfnExtension",
    "CfnExtensionAssociation",
    "CfnExtensionAssociationProps",
    "CfnExtensionProps",
    "CfnHostedConfigurationVersion",
    "CfnHostedConfigurationVersionProps",
]

publication.publish()

def _typecheckingstub__c5cb8c402a0d1a836162f596142de6ed2a1f2a0635a355ae334b92eb1175e956(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnApplication.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ea7b1a84049868bc175511a7cff8896cbe830377b519f6e81ca6912165c12a6(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6ba5479a5d56f629f8d2769fdc6bc86ac3ecfb94f4a9b20a0a26e228f899e8a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd439efd20029913dc2dc3442824daa5698101df926aeab59ca95e5e5b8bbd51(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a824db2a54c11ce0a54133772196bc9c7049c60fe6169de15459866f72df2438(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1c6b2136fb3c6e3eba293e5878e147b18261e888036e9d04f50ade7f12363e3(
    value: typing.Optional[typing.List[CfnApplication.TagsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e23a692b191ad17b59ca3b168ad9b22a1a2f3166cfe85a66eeb03dff73e0e4fd(
    *,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32e1eda1678f32e80ec88e7c377d932bfe40dcff82d39b0dd0edf98a68d3e9d9(
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnApplication.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__332c05b5fb120e53a9fcdde311f2bc23aaec927aa0e70b013e72cc2cebe88708(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_id: builtins.str,
    location_uri: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    retrieval_role_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnConfigurationProfile.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    type: typing.Optional[builtins.str] = None,
    validators: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationProfile.ValidatorsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e772e24251baa448c01bcc3e6670ade5ceed90c38ae4803dc614bd5e09316acd(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e32e704ce25e06be45d32d6a2f4cb3655c378ec2a6662baf1f650e54d58d3148(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a90d416aa5727f39ec3c71cf2276506643a5cf358d97a872994efb5efc0c6a23(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b354f0f45617e66d27b62ebf9a76fdbe168c6f5b6731023e6a366547233a4cb5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92d26c2b0d5b0b13ed55ca82e2b92075cdb99d8bd6d4a9122e33104a12cf9d5d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5884bd7f8fdc28919378604807977665ba3e82a47697c023e5982eb7257f557c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d3f2e474a52e1c1e45abe4e24cd6c758600c20023f3697e0c69533c0e771bc2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebd94616157773a4ab3988775ff92592f3cda9938c8625e395d1dbbf8406354b(
    value: typing.Optional[typing.List[CfnConfigurationProfile.TagsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c45113a4405009713d71c8289b038f5cff241d53b81b243f0372147d29440ad9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11ba2acd464e5613cd96989e3516592dcd5684d8452b3028698e0549f5d5fafb(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConfigurationProfile.ValidatorsProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e56fd1db0eac83273c71919752012ed7424296a5db1629b01fefd16fbf70d613(
    *,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3e2223bb16cf91626b0a44db9aa8ec9190717961f143668d3ff6961eec9abdd(
    *,
    content: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37522e89a156f185f3387aea77d01f8010adde3d2bcfeb76862a70fd9b7e08bc(
    *,
    application_id: builtins.str,
    location_uri: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    retrieval_role_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnConfigurationProfile.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    type: typing.Optional[builtins.str] = None,
    validators: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationProfile.ValidatorsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1b3c15ba63fb6169371007d7bae981d061f49c21042389030326b9ae1271344(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_id: builtins.str,
    configuration_profile_id: builtins.str,
    configuration_version: builtins.str,
    deployment_strategy_id: builtins.str,
    environment_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    kms_key_identifier: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnDeployment.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aaa2637a497fc43f28ee8b6e77e0f1878471c7f5bc0a736d0303ca69cb2d082c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d3096cada1facd4de77c79fe8d588aa3d9567d81b3f913d2c2e6cf8fac54d0e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95aaa1f67bb9531251e5f9c62292c84df7727307a58c223aaa637f0a36a3d65d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca3182ab453e0412fad7ba8649da4e0cfebf187bd90f38a026444982eb8bf50e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5abde1954bdb5d84cfce775808f90c961127e86db5ff5164bb90a98e3b0f9f20(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0527964ec5c65ed1bca366f0674e5cda5d23fe019ae479f3ee3fb550fbdb0c23(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f949624a9b6e222d754ab636966342dbb9eb207d34230837c882091a20f9abac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96f77dd19f2c1b41d04318bc8aa9cc8f75808190471ba4922eb58652c55c5e38(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98b30f15af8144546829026dccf1aaf4fedd94b59dabeb6c8e8d7bc2b71e2efb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12211b05040a4e1a62df97a0128f266db1c0380eba8db0726824e99ad7241551(
    value: typing.Optional[typing.List[CfnDeployment.TagsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2cbb4f58a4f6b9050d66f9a1afb3573fcfbb1445ae7d29b90ec9f65ac1f836f(
    *,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8289d78d65be12b91a60529d6c53d8a4385f73c87b2a23cfef86efebc1e00914(
    *,
    application_id: builtins.str,
    configuration_profile_id: builtins.str,
    configuration_version: builtins.str,
    deployment_strategy_id: builtins.str,
    environment_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    kms_key_identifier: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnDeployment.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb88c221f102c1b57ba4f19db7656eb36ff011a70e3643e39d048c313eda22fd(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    deployment_duration_in_minutes: jsii.Number,
    growth_factor: jsii.Number,
    name: builtins.str,
    replicate_to: builtins.str,
    description: typing.Optional[builtins.str] = None,
    final_bake_time_in_minutes: typing.Optional[jsii.Number] = None,
    growth_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnDeploymentStrategy.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c07282bd387e2aab09e9241f96ded37ff336d3f231f996e048ef207d3a38bc3(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__750f81fb9177952991767d28a4a55a4de59c55177b25056fdd45e8aff0c293c2(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2b9cfcca9dae7bf599adef5f2b44e7662994e8143e1b3ccfa6f12c4d8ad5a19(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ac4cbcedcf27ec80d55a98d836dbb9ac52523d6ff7838145b4d527fadaf652d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43a46b42e0607ca1c01aa58dff3034f44511b63f99f559fe0fd370080f52f2c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb6ef1a3102939b024e6e99b451674a1ad1f6879f5355a20a6d365cfeab4ad4e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f47275a573fd911ba6db69f152dd00eab69b450d732941105375d198524fd2b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad18c900d6d84d1f1dba268d6d666b830e5e5276badda4b775deb06725f3c4ea(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38dbe338fc520a7ce3134f048d86265b2db4966fa73c38281b48ff6124acbc16(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b0c7e44af284b89d6923411489d05fa28350784f8d88a837a0d019a1d575e65(
    value: typing.Optional[typing.List[CfnDeploymentStrategy.TagsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__788f9166b700f88792d30ba7d0b953bc14938d30ade630f5fe723e23a497207d(
    *,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__199999cc14040404b938fa601301d483ec681a01c3bd23495d2d90dde59820b5(
    *,
    deployment_duration_in_minutes: jsii.Number,
    growth_factor: jsii.Number,
    name: builtins.str,
    replicate_to: builtins.str,
    description: typing.Optional[builtins.str] = None,
    final_bake_time_in_minutes: typing.Optional[jsii.Number] = None,
    growth_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnDeploymentStrategy.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f357d5cab83004926812cf34c99a144f4f5d23ca26e4a818590a950622a06fc3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_id: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    monitors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.MonitorsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnEnvironment.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3842dacad1a08e5d9103a4c646c8fa2385f77b6f5495fbd4dab597c037c8f09b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dbe73a2ef533ed22edd7fd274c6cca5a979759478da06114e8699f7b2409820(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d35c6a50b39401e18b97d5d78f1d4d92aaf846c18aa4ec32bce024a53e54c4be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__569391bda37ae2bcb096c8b3ab953d25c7ff488899b2557c773cc8f72ee8a4cb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__154bd59aabeed21e27800d9d45bcdbb412639a65e9aaaf72ef6dae673fa26a43(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8d099ead34dfe7be9eb945722b31207889d993d21d927e1eeba6592c7f8fd44(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironment.MonitorsProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60701727c0b2b8f0404d231ccc24899f35678bacc781ed4c6443de1b14432f68(
    value: typing.Optional[typing.List[CfnEnvironment.TagsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43d91f41d1c9d1acd545d0999d47687e0e5b7be03ec08728e3c5aa73ff76549f(
    *,
    alarm_arn: typing.Optional[builtins.str] = None,
    alarm_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f58f801045a8e3c147c3d78dc98e6b7aa29fb1f248587805b6f76a3486e6436(
    *,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6c9856f1a5a9dfaed9be42ec835bb6eac4d4882999b993cbd02b3b11bbfe1ca(
    *,
    application_id: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    monitors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.MonitorsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnEnvironment.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3442a7f4d7a9c3256544c6b0526d285ef0cf3970ec1f140b344aed1abc4eef5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    actions: typing.Any,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnExtension.ParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6930a24c04bd5aebe54f7a225f7ec08743e520b61a781973e88a4b6678524a5(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57070195544dc008ade09c677ffa495cf4120e6b1dc834d6ffa101c3cf189599(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f734d5e14d1ac32f7ec277282f23b1f2f7c0b8ce8e48d8df2b080f67d200577f(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__081c55af29bf24c3599cf24134be4ce60656f052c575f59ff68c2084fa523481(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__334508667f33fe5d26ff2e39e3bcbaaea618391e439f25094004fab0d75eb718(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b38bdb75b51870401d0b83754078af02e3e6886d97a64481c3733b63a5a4c814(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ad5fbf78cb34accb172520e561c08795fbca80280af2dcc78243ceb84841d07(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnExtension.ParameterProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e6cc683bfd791a6ddfdc2295e58057279b3a19bc4adc7a11fbff993fe64fe37(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58317247cdf8a690d14849381527f22c6a038c04470bb6ed420b3ade323b7e43(
    *,
    name: builtins.str,
    uri: builtins.str,
    description: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__683bc731900456f8d594ddc90d3c7fc1fcdc884942410401537639fad3d02ed1(
    *,
    required: typing.Union[builtins.bool, _IResolvable_da3f097b],
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2e5a069dff64a93330fdfc39cee819956ed46cafa89dc1aee558b0c288de8af(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    extension_identifier: typing.Optional[builtins.str] = None,
    extension_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    resource_identifier: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__209622600665bfa16663cc19d0b91c8caf5c5d29f4cc7cb09fd6fba67bcb1739(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0a9f34459bdf3e807e0362d7767352a597304250be35f36b98afb6b8d6ca733(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd635cb248fd501f641536d553e5645fb6dd03b8db84e4059ddc6af591a307e8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4aa600ead50aeb1f2d5f5f5fe334e3e11a16eccfa413e5de0742f763f7938a43(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc72677d37ba0fe5b56dcbee5b8705c9e4e30a75b5d3b051bc792305dfd3deda(
    value: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ff48a7c10c5007769564f0b18da5363288efbb9ca805f7bb5a7fd93e791ec3d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d31c336e3843162aab44371392cbb25a2b62fcd270c6fc472b3f2819a21b9ea1(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__658f796ad2928720e80bab1455b7c28527f38d13b4efe7780e0a592469829ce9(
    *,
    extension_identifier: typing.Optional[builtins.str] = None,
    extension_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    resource_identifier: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a81148d01bee60e4140891afd5b9da3eab7a3dd5f81524eaa37f895ff781df1f(
    *,
    actions: typing.Any,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnExtension.ParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f2dc9ae7157f5223a79cf8ea4a7355ec285dbe0fda348428c6e0e6cdabbb60b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_id: builtins.str,
    configuration_profile_id: builtins.str,
    content: builtins.str,
    content_type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    version_label: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__287f244644cef79eb3704756fc9fd6f98e693a42df76727f726091d3190ab82c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__694959938824dc357bd7ac9b60be653c213df7cdcc44905d59d6e7d7e1182171(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97e3d21e204bcf08a8dceb763729bfb70936f6d97ed550af3dfe101fac0f4331(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4193469efc98930e2e72ffffb47c40bb1631526d907d8eaab051ac721dce3631(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac0de9d6bf3585fb47f9ad3fbb1d23a9a11447de5c02a24b6971d67ab3a7fa70(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb880ec8c47eca7663501403482ddb505ffe759b4792fa0a7236d31e1313d7fe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d43da3f82c30824ce1a2d29683403d6e68cb792341046055e7df42a980951259(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14797876de335768bb8254a37ba88bf3300df4a568a8174a333380741acaa4b8(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__384487882c55b43a28f4a742590e489e653df19c023a94fbfacb65cdf0cf00e2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2e12025d283b0b516fc7a346d00f20eff94d8259ba3fc82c8cb240aeb05264e(
    *,
    application_id: builtins.str,
    configuration_profile_id: builtins.str,
    content: builtins.str,
    content_type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    version_label: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
