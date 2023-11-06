'''
# AWS::M2 Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_m2 as m2
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for M2 construct libraries](https://constructs.dev/search?q=m2)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::M2 resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_M2.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::M2](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_M2.html).

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
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    ITaggable as _ITaggable_36806126,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnApplication(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_m2.CfnApplication",
):
    '''Specifies a new application with given parameters. Requires an existing runtime environment and application definition file.

    For information about application definitions, see the `AWS Mainframe Modernization User Guide <https://docs.aws.amazon.com/m2/latest/userguide/applications-m2-definition.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-application.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_m2 as m2
        
        cfn_application = m2.CfnApplication(self, "MyCfnApplication",
            definition=m2.CfnApplication.DefinitionProperty(
                content="content",
                s3_location="s3Location"
            ),
            engine_type="engineType",
            name="name",
        
            # the properties below are optional
            description="description",
            kms_key_id="kmsKeyId",
            role_arn="roleArn",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        definition: typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplication.DefinitionProperty", typing.Dict[builtins.str, typing.Any]]],
        engine_type: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param definition: The application definition for a particular application. You can specify either inline JSON or an Amazon S3 bucket location. For information about application definitions, see the `AWS Mainframe Modernization User Guide <https://docs.aws.amazon.com/m2/latest/userguide/applications-m2-definition.html>`_ .
        :param engine_type: The type of the target platform for this application.
        :param name: The name of the application.
        :param description: The description of the application.
        :param kms_key_id: The identifier of a customer managed key.
        :param role_arn: 
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d9f18e4c35f8dd6932a89aab0c7c8325ca5f0e480e78df5838e1e64d1ba0f80)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationProps(
            definition=definition,
            engine_type=engine_type,
            name=name,
            description=description,
            kms_key_id=kms_key_id,
            role_arn=role_arn,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__930fa019de61c28a83bc70684b2fec3054c6540e78cef82bbebd5e15c7888337)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c0533659aa42d859aee8bd4e01b62d0756e88da8f0e83be9c1f372431f25ce04)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrApplicationArn")
    def attr_application_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the application.

        :cloudformationAttribute: ApplicationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApplicationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrApplicationId")
    def attr_application_id(self) -> builtins.str:
        '''The identifier of the application.

        :cloudformationAttribute: ApplicationId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApplicationId"))

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
    @jsii.member(jsii_name="definition")
    def definition(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnApplication.DefinitionProperty"]:
        '''The application definition for a particular application.

        You can specify either inline JSON or an Amazon S3 bucket location.
        '''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnApplication.DefinitionProperty"], jsii.get(self, "definition"))

    @definition.setter
    def definition(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnApplication.DefinitionProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a8ea13658af5ef1a7d26f032b47b28d17ab527b4ede05c82ee7c653b2de040f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "definition", value)

    @builtins.property
    @jsii.member(jsii_name="engineType")
    def engine_type(self) -> builtins.str:
        '''The type of the target platform for this application.'''
        return typing.cast(builtins.str, jsii.get(self, "engineType"))

    @engine_type.setter
    def engine_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ba4f8f93c55dbcb042b32b8823b3acaab4fde77a6bdcad9a5ee86fb35a2686c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engineType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the application.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ffbf95da1d1e51725779fb8b533d4d030b427cf5adffd8b2fc9a4f81ffacff7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the application.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05a9747db0681d6113a5020c40da3c44e751ec1244812a5a2d722be19aeffe18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of a customer managed key.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2505906ed4b14ef890ab5ee84486183008470a96e5a0f7fadacc1bad20316e1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b52acf25288a670285300bc407fc4150f9b0505813e2b8351c2d4d1215ead9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__293deb70e531b45518966264fd86e02d133b64b34373c541f5c050cd77567d2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_m2.CfnApplication.DefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={"content": "content", "s3_location": "s3Location"},
    )
    class DefinitionProperty:
        def __init__(
            self,
            *,
            content: typing.Optional[builtins.str] = None,
            s3_location: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The application definition for a particular application.

            You can specify either inline JSON or an Amazon S3 bucket location.

            :param content: The content of the application definition. This is a JSON object that contains the resource configuration/definitions that identify an application.
            :param s3_location: The S3 bucket that contains the application definition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-application-definition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_m2 as m2
                
                definition_property = m2.CfnApplication.DefinitionProperty(
                    content="content",
                    s3_location="s3Location"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e6a2c5ede257cc8f9ff5fc917afe31b9bf6e82d475e3a8dedebfee5db21e5553)
                check_type(argname="argument content", value=content, expected_type=type_hints["content"])
                check_type(argname="argument s3_location", value=s3_location, expected_type=type_hints["s3_location"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if content is not None:
                self._values["content"] = content
            if s3_location is not None:
                self._values["s3_location"] = s3_location

        @builtins.property
        def content(self) -> typing.Optional[builtins.str]:
            '''The content of the application definition.

            This is a JSON object that contains the resource configuration/definitions that identify an application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-application-definition.html#cfn-m2-application-definition-content
            '''
            result = self._values.get("content")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_location(self) -> typing.Optional[builtins.str]:
            '''The S3 bucket that contains the application definition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-application-definition.html#cfn-m2-application-definition-s3location
            '''
            result = self._values.get("s3_location")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_m2.CfnApplicationProps",
    jsii_struct_bases=[],
    name_mapping={
        "definition": "definition",
        "engine_type": "engineType",
        "name": "name",
        "description": "description",
        "kms_key_id": "kmsKeyId",
        "role_arn": "roleArn",
        "tags": "tags",
    },
)
class CfnApplicationProps:
    def __init__(
        self,
        *,
        definition: typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.DefinitionProperty, typing.Dict[builtins.str, typing.Any]]],
        engine_type: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnApplication``.

        :param definition: The application definition for a particular application. You can specify either inline JSON or an Amazon S3 bucket location. For information about application definitions, see the `AWS Mainframe Modernization User Guide <https://docs.aws.amazon.com/m2/latest/userguide/applications-m2-definition.html>`_ .
        :param engine_type: The type of the target platform for this application.
        :param name: The name of the application.
        :param description: The description of the application.
        :param kms_key_id: The identifier of a customer managed key.
        :param role_arn: 
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-application.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_m2 as m2
            
            cfn_application_props = m2.CfnApplicationProps(
                definition=m2.CfnApplication.DefinitionProperty(
                    content="content",
                    s3_location="s3Location"
                ),
                engine_type="engineType",
                name="name",
            
                # the properties below are optional
                description="description",
                kms_key_id="kmsKeyId",
                role_arn="roleArn",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ed1db61d31dff8aa8e94733976425175ee39f97b9a27b2b69f86017aa34d4b5)
            check_type(argname="argument definition", value=definition, expected_type=type_hints["definition"])
            check_type(argname="argument engine_type", value=engine_type, expected_type=type_hints["engine_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "definition": definition,
            "engine_type": engine_type,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def definition(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnApplication.DefinitionProperty]:
        '''The application definition for a particular application. You can specify either inline JSON or an Amazon S3 bucket location.

        For information about application definitions, see the `AWS Mainframe Modernization User Guide <https://docs.aws.amazon.com/m2/latest/userguide/applications-m2-definition.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-application.html#cfn-m2-application-definition
        '''
        result = self._values.get("definition")
        assert result is not None, "Required property 'definition' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnApplication.DefinitionProperty], result)

    @builtins.property
    def engine_type(self) -> builtins.str:
        '''The type of the target platform for this application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-application.html#cfn-m2-application-enginetype
        '''
        result = self._values.get("engine_type")
        assert result is not None, "Required property 'engine_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-application.html#cfn-m2-application-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-application.html#cfn-m2-application-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of a customer managed key.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-application.html#cfn-m2-application-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-application.html#cfn-m2-application-rolearn
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-application.html#cfn-m2-application-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnEnvironment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_m2.CfnEnvironment",
):
    '''Specifies a runtime environment for a given runtime engine.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-environment.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_m2 as m2
        
        cfn_environment = m2.CfnEnvironment(self, "MyCfnEnvironment",
            engine_type="engineType",
            instance_type="instanceType",
            name="name",
        
            # the properties below are optional
            description="description",
            engine_version="engineVersion",
            high_availability_config=m2.CfnEnvironment.HighAvailabilityConfigProperty(
                desired_capacity=123
            ),
            kms_key_id="kmsKeyId",
            preferred_maintenance_window="preferredMaintenanceWindow",
            publicly_accessible=False,
            security_group_ids=["securityGroupIds"],
            storage_configurations=[m2.CfnEnvironment.StorageConfigurationProperty(
                efs=m2.CfnEnvironment.EfsStorageConfigurationProperty(
                    file_system_id="fileSystemId",
                    mount_point="mountPoint"
                ),
                fsx=m2.CfnEnvironment.FsxStorageConfigurationProperty(
                    file_system_id="fileSystemId",
                    mount_point="mountPoint"
                )
            )],
            subnet_ids=["subnetIds"],
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        engine_type: builtins.str,
        instance_type: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        high_availability_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.HighAvailabilityConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        storage_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.StorageConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param engine_type: The target platform for the runtime environment.
        :param instance_type: The instance type of the runtime environment.
        :param name: The name of the runtime environment.
        :param description: The description of the runtime environment.
        :param engine_version: The version of the runtime engine.
        :param high_availability_config: Defines the details of a high availability configuration.
        :param kms_key_id: The identifier of a customer managed key.
        :param preferred_maintenance_window: Configures the maintenance window that you want for the runtime environment. The maintenance window must have the format ``ddd:hh24:mi-ddd:hh24:mi`` and must be less than 24 hours. The following two examples are valid maintenance windows: ``sun:23:45-mon:00:15`` or ``sat:01:00-sat:03:00`` . If you do not provide a value, a random system-generated value will be assigned.
        :param publicly_accessible: Specifies whether the runtime environment is publicly accessible.
        :param security_group_ids: The list of security groups for the VPC associated with this runtime environment.
        :param storage_configurations: Defines the storage configuration for a runtime environment.
        :param subnet_ids: The list of subnets associated with the VPC for this runtime environment.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b13501bd562f397b7070738470ee5bd51ff8aa50c0a2fb6c33998acdd3e0ac0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEnvironmentProps(
            engine_type=engine_type,
            instance_type=instance_type,
            name=name,
            description=description,
            engine_version=engine_version,
            high_availability_config=high_availability_config,
            kms_key_id=kms_key_id,
            preferred_maintenance_window=preferred_maintenance_window,
            publicly_accessible=publicly_accessible,
            security_group_ids=security_group_ids,
            storage_configurations=storage_configurations,
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
            type_hints = typing.get_type_hints(_typecheckingstub__7d048d4292e86fa84d87ff475412cc0702cb9e132a6a77d37b03ce65f5decc2b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__15b27312e8939adf4539c09dae85d7caa28cefe74bc4b8665ac1112cf51b36dc)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrEnvironmentArn")
    def attr_environment_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the runtime environment.

        :cloudformationAttribute: EnvironmentArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEnvironmentArn"))

    @builtins.property
    @jsii.member(jsii_name="attrEnvironmentId")
    def attr_environment_id(self) -> builtins.str:
        '''The unique identifier of the runtime environment.

        :cloudformationAttribute: EnvironmentId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEnvironmentId"))

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
    @jsii.member(jsii_name="engineType")
    def engine_type(self) -> builtins.str:
        '''The target platform for the runtime environment.'''
        return typing.cast(builtins.str, jsii.get(self, "engineType"))

    @engine_type.setter
    def engine_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__784433f8815f51a4ecb5d24bcbbeea0aab1bda1482e3b171aa08f85e8cd69e89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engineType", value)

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        '''The instance type of the runtime environment.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a33e21e8e5ffd1792561121d437dd4bd3dbbb02fdbf972e85c60b122a76f0df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the runtime environment.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b19d9065041ecedcf47470d85fa105b70f6302a6353a6dccf2ac2a5f8ad59089)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the runtime environment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4161a9157728187bc69374d773118ff198e8a63fbfdc86af20b7410ec0450977)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="engineVersion")
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''The version of the runtime engine.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engineVersion"))

    @engine_version.setter
    def engine_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cffb7289576fe3b2be64680240da9bb558f0118faa6c3fad464af5497e349630)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engineVersion", value)

    @builtins.property
    @jsii.member(jsii_name="highAvailabilityConfig")
    def high_availability_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.HighAvailabilityConfigProperty"]]:
        '''Defines the details of a high availability configuration.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.HighAvailabilityConfigProperty"]], jsii.get(self, "highAvailabilityConfig"))

    @high_availability_config.setter
    def high_availability_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.HighAvailabilityConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ae32ee44c20ee3d62c04275975bd36b0c4b52f1a4e530da019c34c5a304d354)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "highAvailabilityConfig", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of a customer managed key.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0011b59017b38aa278dd84a2dd688ba62f95b50bfcab1e26f0b42157dee12848)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''Configures the maintenance window that you want for the runtime environment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredMaintenanceWindow"))

    @preferred_maintenance_window.setter
    def preferred_maintenance_window(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__935b559bc9b04464e444f79017f7e13d5455cbffe9f8f3e646c3890255b99bf6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredMaintenanceWindow", value)

    @builtins.property
    @jsii.member(jsii_name="publiclyAccessible")
    def publicly_accessible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the runtime environment is publicly accessible.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "publiclyAccessible"))

    @publicly_accessible.setter
    def publicly_accessible(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aafc9453ef0e6f29c2ca5627640e99238639f68f55fcd53863b14a7773934a0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publiclyAccessible", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of security groups for the VPC associated with this runtime environment.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7e3951a053d9f19df8749e136c23fe663c499ce22be6a098e609f71c9a1f32a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="storageConfigurations")
    def storage_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.StorageConfigurationProperty"]]]]:
        '''Defines the storage configuration for a runtime environment.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.StorageConfigurationProperty"]]]], jsii.get(self, "storageConfigurations"))

    @storage_configurations.setter
    def storage_configurations(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.StorageConfigurationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0469c70e4a0b0e01a5d619854f0773c467db7e6e0849f3c4da28fc65e5a14f5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageConfigurations", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of subnets associated with the VPC for this runtime environment.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__437876d91ad9d53d1e283b7f005938a4a61d2ee60e417ce69ea85a2d39a391e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1da39fd1787883dfdef23ec69543cb36b29e712c9d56ca2a70d0c8bcc84e7adc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_m2.CfnEnvironment.EfsStorageConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"file_system_id": "fileSystemId", "mount_point": "mountPoint"},
    )
    class EfsStorageConfigurationProperty:
        def __init__(
            self,
            *,
            file_system_id: builtins.str,
            mount_point: builtins.str,
        ) -> None:
            '''Defines the storage configuration for an Amazon EFS file system.

            :param file_system_id: The file system identifier.
            :param mount_point: The mount point for the file system.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-environment-efsstorageconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_m2 as m2
                
                efs_storage_configuration_property = m2.CfnEnvironment.EfsStorageConfigurationProperty(
                    file_system_id="fileSystemId",
                    mount_point="mountPoint"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__aa585c36e9b2320b141d44e8ed71eb0bfa714c8575925ecd62f0e5106d7a74b5)
                check_type(argname="argument file_system_id", value=file_system_id, expected_type=type_hints["file_system_id"])
                check_type(argname="argument mount_point", value=mount_point, expected_type=type_hints["mount_point"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "file_system_id": file_system_id,
                "mount_point": mount_point,
            }

        @builtins.property
        def file_system_id(self) -> builtins.str:
            '''The file system identifier.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-environment-efsstorageconfiguration.html#cfn-m2-environment-efsstorageconfiguration-filesystemid
            '''
            result = self._values.get("file_system_id")
            assert result is not None, "Required property 'file_system_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def mount_point(self) -> builtins.str:
            '''The mount point for the file system.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-environment-efsstorageconfiguration.html#cfn-m2-environment-efsstorageconfiguration-mountpoint
            '''
            result = self._values.get("mount_point")
            assert result is not None, "Required property 'mount_point' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EfsStorageConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_m2.CfnEnvironment.FsxStorageConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"file_system_id": "fileSystemId", "mount_point": "mountPoint"},
    )
    class FsxStorageConfigurationProperty:
        def __init__(
            self,
            *,
            file_system_id: builtins.str,
            mount_point: builtins.str,
        ) -> None:
            '''Defines the storage configuration for an Amazon FSx file system.

            :param file_system_id: The file system identifier.
            :param mount_point: The mount point for the file system.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-environment-fsxstorageconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_m2 as m2
                
                fsx_storage_configuration_property = m2.CfnEnvironment.FsxStorageConfigurationProperty(
                    file_system_id="fileSystemId",
                    mount_point="mountPoint"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cab33bb1cb9e6880655f2cc59cdae8878841b12cef1c8f4f339a65bae6fd8a80)
                check_type(argname="argument file_system_id", value=file_system_id, expected_type=type_hints["file_system_id"])
                check_type(argname="argument mount_point", value=mount_point, expected_type=type_hints["mount_point"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "file_system_id": file_system_id,
                "mount_point": mount_point,
            }

        @builtins.property
        def file_system_id(self) -> builtins.str:
            '''The file system identifier.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-environment-fsxstorageconfiguration.html#cfn-m2-environment-fsxstorageconfiguration-filesystemid
            '''
            result = self._values.get("file_system_id")
            assert result is not None, "Required property 'file_system_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def mount_point(self) -> builtins.str:
            '''The mount point for the file system.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-environment-fsxstorageconfiguration.html#cfn-m2-environment-fsxstorageconfiguration-mountpoint
            '''
            result = self._values.get("mount_point")
            assert result is not None, "Required property 'mount_point' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FsxStorageConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_m2.CfnEnvironment.HighAvailabilityConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"desired_capacity": "desiredCapacity"},
    )
    class HighAvailabilityConfigProperty:
        def __init__(self, *, desired_capacity: jsii.Number) -> None:
            '''Defines the details of a high availability configuration.

            :param desired_capacity: The number of instances in a high availability configuration. The minimum possible value is 1 and the maximum is 100.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-environment-highavailabilityconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_m2 as m2
                
                high_availability_config_property = m2.CfnEnvironment.HighAvailabilityConfigProperty(
                    desired_capacity=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3db2944148ec0403161716eadf183182b4b11684f200f43b6fae27b14abd06ab)
                check_type(argname="argument desired_capacity", value=desired_capacity, expected_type=type_hints["desired_capacity"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "desired_capacity": desired_capacity,
            }

        @builtins.property
        def desired_capacity(self) -> jsii.Number:
            '''The number of instances in a high availability configuration.

            The minimum possible value is 1 and the maximum is 100.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-environment-highavailabilityconfig.html#cfn-m2-environment-highavailabilityconfig-desiredcapacity
            '''
            result = self._values.get("desired_capacity")
            assert result is not None, "Required property 'desired_capacity' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HighAvailabilityConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_m2.CfnEnvironment.StorageConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"efs": "efs", "fsx": "fsx"},
    )
    class StorageConfigurationProperty:
        def __init__(
            self,
            *,
            efs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.EfsStorageConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            fsx: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.FsxStorageConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Defines the storage configuration for a runtime environment.

            :param efs: Defines the storage configuration for an Amazon EFS file system.
            :param fsx: Defines the storage configuration for an Amazon FSx file system.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-environment-storageconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_m2 as m2
                
                storage_configuration_property = m2.CfnEnvironment.StorageConfigurationProperty(
                    efs=m2.CfnEnvironment.EfsStorageConfigurationProperty(
                        file_system_id="fileSystemId",
                        mount_point="mountPoint"
                    ),
                    fsx=m2.CfnEnvironment.FsxStorageConfigurationProperty(
                        file_system_id="fileSystemId",
                        mount_point="mountPoint"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__be54682f3b71055b15a50a83ac3cb959dac840823bb036ddd8f40b08613c23f3)
                check_type(argname="argument efs", value=efs, expected_type=type_hints["efs"])
                check_type(argname="argument fsx", value=fsx, expected_type=type_hints["fsx"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if efs is not None:
                self._values["efs"] = efs
            if fsx is not None:
                self._values["fsx"] = fsx

        @builtins.property
        def efs(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.EfsStorageConfigurationProperty"]]:
            '''Defines the storage configuration for an Amazon EFS file system.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-environment-storageconfiguration.html#cfn-m2-environment-storageconfiguration-efs
            '''
            result = self._values.get("efs")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.EfsStorageConfigurationProperty"]], result)

        @builtins.property
        def fsx(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.FsxStorageConfigurationProperty"]]:
            '''Defines the storage configuration for an Amazon FSx file system.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-environment-storageconfiguration.html#cfn-m2-environment-storageconfiguration-fsx
            '''
            result = self._values.get("fsx")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.FsxStorageConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StorageConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_m2.CfnEnvironmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "engine_type": "engineType",
        "instance_type": "instanceType",
        "name": "name",
        "description": "description",
        "engine_version": "engineVersion",
        "high_availability_config": "highAvailabilityConfig",
        "kms_key_id": "kmsKeyId",
        "preferred_maintenance_window": "preferredMaintenanceWindow",
        "publicly_accessible": "publiclyAccessible",
        "security_group_ids": "securityGroupIds",
        "storage_configurations": "storageConfigurations",
        "subnet_ids": "subnetIds",
        "tags": "tags",
    },
)
class CfnEnvironmentProps:
    def __init__(
        self,
        *,
        engine_type: builtins.str,
        instance_type: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        high_availability_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.HighAvailabilityConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        storage_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.StorageConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEnvironment``.

        :param engine_type: The target platform for the runtime environment.
        :param instance_type: The instance type of the runtime environment.
        :param name: The name of the runtime environment.
        :param description: The description of the runtime environment.
        :param engine_version: The version of the runtime engine.
        :param high_availability_config: Defines the details of a high availability configuration.
        :param kms_key_id: The identifier of a customer managed key.
        :param preferred_maintenance_window: Configures the maintenance window that you want for the runtime environment. The maintenance window must have the format ``ddd:hh24:mi-ddd:hh24:mi`` and must be less than 24 hours. The following two examples are valid maintenance windows: ``sun:23:45-mon:00:15`` or ``sat:01:00-sat:03:00`` . If you do not provide a value, a random system-generated value will be assigned.
        :param publicly_accessible: Specifies whether the runtime environment is publicly accessible.
        :param security_group_ids: The list of security groups for the VPC associated with this runtime environment.
        :param storage_configurations: Defines the storage configuration for a runtime environment.
        :param subnet_ids: The list of subnets associated with the VPC for this runtime environment.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-environment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_m2 as m2
            
            cfn_environment_props = m2.CfnEnvironmentProps(
                engine_type="engineType",
                instance_type="instanceType",
                name="name",
            
                # the properties below are optional
                description="description",
                engine_version="engineVersion",
                high_availability_config=m2.CfnEnvironment.HighAvailabilityConfigProperty(
                    desired_capacity=123
                ),
                kms_key_id="kmsKeyId",
                preferred_maintenance_window="preferredMaintenanceWindow",
                publicly_accessible=False,
                security_group_ids=["securityGroupIds"],
                storage_configurations=[m2.CfnEnvironment.StorageConfigurationProperty(
                    efs=m2.CfnEnvironment.EfsStorageConfigurationProperty(
                        file_system_id="fileSystemId",
                        mount_point="mountPoint"
                    ),
                    fsx=m2.CfnEnvironment.FsxStorageConfigurationProperty(
                        file_system_id="fileSystemId",
                        mount_point="mountPoint"
                    )
                )],
                subnet_ids=["subnetIds"],
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a01760c10dc72a17faa5c350ba316c41979d4b9c411e040a52c7924e69c40e90)
            check_type(argname="argument engine_type", value=engine_type, expected_type=type_hints["engine_type"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument engine_version", value=engine_version, expected_type=type_hints["engine_version"])
            check_type(argname="argument high_availability_config", value=high_availability_config, expected_type=type_hints["high_availability_config"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument preferred_maintenance_window", value=preferred_maintenance_window, expected_type=type_hints["preferred_maintenance_window"])
            check_type(argname="argument publicly_accessible", value=publicly_accessible, expected_type=type_hints["publicly_accessible"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument storage_configurations", value=storage_configurations, expected_type=type_hints["storage_configurations"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "engine_type": engine_type,
            "instance_type": instance_type,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if engine_version is not None:
            self._values["engine_version"] = engine_version
        if high_availability_config is not None:
            self._values["high_availability_config"] = high_availability_config
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if preferred_maintenance_window is not None:
            self._values["preferred_maintenance_window"] = preferred_maintenance_window
        if publicly_accessible is not None:
            self._values["publicly_accessible"] = publicly_accessible
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if storage_configurations is not None:
            self._values["storage_configurations"] = storage_configurations
        if subnet_ids is not None:
            self._values["subnet_ids"] = subnet_ids
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def engine_type(self) -> builtins.str:
        '''The target platform for the runtime environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-environment.html#cfn-m2-environment-enginetype
        '''
        result = self._values.get("engine_type")
        assert result is not None, "Required property 'engine_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_type(self) -> builtins.str:
        '''The instance type of the runtime environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-environment.html#cfn-m2-environment-instancetype
        '''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the runtime environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-environment.html#cfn-m2-environment-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the runtime environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-environment.html#cfn-m2-environment-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''The version of the runtime engine.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-environment.html#cfn-m2-environment-engineversion
        '''
        result = self._values.get("engine_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def high_availability_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEnvironment.HighAvailabilityConfigProperty]]:
        '''Defines the details of a high availability configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-environment.html#cfn-m2-environment-highavailabilityconfig
        '''
        result = self._values.get("high_availability_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEnvironment.HighAvailabilityConfigProperty]], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of a customer managed key.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-environment.html#cfn-m2-environment-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''Configures the maintenance window that you want for the runtime environment.

        The maintenance window must have the format ``ddd:hh24:mi-ddd:hh24:mi`` and must be less than 24 hours. The following two examples are valid maintenance windows: ``sun:23:45-mon:00:15`` or ``sat:01:00-sat:03:00`` .

        If you do not provide a value, a random system-generated value will be assigned.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-environment.html#cfn-m2-environment-preferredmaintenancewindow
        '''
        result = self._values.get("preferred_maintenance_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def publicly_accessible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the runtime environment is publicly accessible.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-environment.html#cfn-m2-environment-publiclyaccessible
        '''
        result = self._values.get("publicly_accessible")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of security groups for the VPC associated with this runtime environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-environment.html#cfn-m2-environment-securitygroupids
        '''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def storage_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironment.StorageConfigurationProperty]]]]:
        '''Defines the storage configuration for a runtime environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-environment.html#cfn-m2-environment-storageconfigurations
        '''
        result = self._values.get("storage_configurations")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironment.StorageConfigurationProperty]]]], result)

    @builtins.property
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of subnets associated with the VPC for this runtime environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-environment.html#cfn-m2-environment-subnetids
        '''
        result = self._values.get("subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-environment.html#cfn-m2-environment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEnvironmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApplication",
    "CfnApplicationProps",
    "CfnEnvironment",
    "CfnEnvironmentProps",
]

publication.publish()

def _typecheckingstub__4d9f18e4c35f8dd6932a89aab0c7c8325ca5f0e480e78df5838e1e64d1ba0f80(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    definition: typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.DefinitionProperty, typing.Dict[builtins.str, typing.Any]]],
    engine_type: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__930fa019de61c28a83bc70684b2fec3054c6540e78cef82bbebd5e15c7888337(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0533659aa42d859aee8bd4e01b62d0756e88da8f0e83be9c1f372431f25ce04(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a8ea13658af5ef1a7d26f032b47b28d17ab527b4ede05c82ee7c653b2de040f(
    value: typing.Union[_IResolvable_da3f097b, CfnApplication.DefinitionProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ba4f8f93c55dbcb042b32b8823b3acaab4fde77a6bdcad9a5ee86fb35a2686c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ffbf95da1d1e51725779fb8b533d4d030b427cf5adffd8b2fc9a4f81ffacff7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05a9747db0681d6113a5020c40da3c44e751ec1244812a5a2d722be19aeffe18(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2505906ed4b14ef890ab5ee84486183008470a96e5a0f7fadacc1bad20316e1d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b52acf25288a670285300bc407fc4150f9b0505813e2b8351c2d4d1215ead9c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__293deb70e531b45518966264fd86e02d133b64b34373c541f5c050cd77567d2a(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6a2c5ede257cc8f9ff5fc917afe31b9bf6e82d475e3a8dedebfee5db21e5553(
    *,
    content: typing.Optional[builtins.str] = None,
    s3_location: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ed1db61d31dff8aa8e94733976425175ee39f97b9a27b2b69f86017aa34d4b5(
    *,
    definition: typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.DefinitionProperty, typing.Dict[builtins.str, typing.Any]]],
    engine_type: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b13501bd562f397b7070738470ee5bd51ff8aa50c0a2fb6c33998acdd3e0ac0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    engine_type: builtins.str,
    instance_type: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    engine_version: typing.Optional[builtins.str] = None,
    high_availability_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.HighAvailabilityConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    storage_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.StorageConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d048d4292e86fa84d87ff475412cc0702cb9e132a6a77d37b03ce65f5decc2b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15b27312e8939adf4539c09dae85d7caa28cefe74bc4b8665ac1112cf51b36dc(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__784433f8815f51a4ecb5d24bcbbeea0aab1bda1482e3b171aa08f85e8cd69e89(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a33e21e8e5ffd1792561121d437dd4bd3dbbb02fdbf972e85c60b122a76f0df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b19d9065041ecedcf47470d85fa105b70f6302a6353a6dccf2ac2a5f8ad59089(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4161a9157728187bc69374d773118ff198e8a63fbfdc86af20b7410ec0450977(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cffb7289576fe3b2be64680240da9bb558f0118faa6c3fad464af5497e349630(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ae32ee44c20ee3d62c04275975bd36b0c4b52f1a4e530da019c34c5a304d354(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEnvironment.HighAvailabilityConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0011b59017b38aa278dd84a2dd688ba62f95b50bfcab1e26f0b42157dee12848(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__935b559bc9b04464e444f79017f7e13d5455cbffe9f8f3e646c3890255b99bf6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aafc9453ef0e6f29c2ca5627640e99238639f68f55fcd53863b14a7773934a0d(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7e3951a053d9f19df8749e136c23fe663c499ce22be6a098e609f71c9a1f32a(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0469c70e4a0b0e01a5d619854f0773c467db7e6e0849f3c4da28fc65e5a14f5f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironment.StorageConfigurationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__437876d91ad9d53d1e283b7f005938a4a61d2ee60e417ce69ea85a2d39a391e3(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1da39fd1787883dfdef23ec69543cb36b29e712c9d56ca2a70d0c8bcc84e7adc(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa585c36e9b2320b141d44e8ed71eb0bfa714c8575925ecd62f0e5106d7a74b5(
    *,
    file_system_id: builtins.str,
    mount_point: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cab33bb1cb9e6880655f2cc59cdae8878841b12cef1c8f4f339a65bae6fd8a80(
    *,
    file_system_id: builtins.str,
    mount_point: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3db2944148ec0403161716eadf183182b4b11684f200f43b6fae27b14abd06ab(
    *,
    desired_capacity: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be54682f3b71055b15a50a83ac3cb959dac840823bb036ddd8f40b08613c23f3(
    *,
    efs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.EfsStorageConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    fsx: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.FsxStorageConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a01760c10dc72a17faa5c350ba316c41979d4b9c411e040a52c7924e69c40e90(
    *,
    engine_type: builtins.str,
    instance_type: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    engine_version: typing.Optional[builtins.str] = None,
    high_availability_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.HighAvailabilityConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    storage_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.StorageConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
