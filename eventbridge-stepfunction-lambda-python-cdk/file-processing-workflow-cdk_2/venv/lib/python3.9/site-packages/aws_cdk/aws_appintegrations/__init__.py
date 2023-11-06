'''
# AWS::AppIntegrations Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_appintegrations as appintegrations
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for AppIntegrations construct libraries](https://constructs.dev/search?q=appintegrations)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::AppIntegrations resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AppIntegrations.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::AppIntegrations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AppIntegrations.html).

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
class CfnDataIntegration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appintegrations.CfnDataIntegration",
):
    '''Creates and persists a DataIntegration resource.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-dataintegration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appintegrations as appintegrations
        
        # filters: Any
        # object_configuration: Any
        
        cfn_data_integration = appintegrations.CfnDataIntegration(self, "MyCfnDataIntegration",
            kms_key="kmsKey",
            name="name",
            schedule_config=appintegrations.CfnDataIntegration.ScheduleConfigProperty(
                schedule_expression="scheduleExpression",
        
                # the properties below are optional
                first_execution_from="firstExecutionFrom",
                object="object"
            ),
            source_uri="sourceUri",
        
            # the properties below are optional
            description="description",
            file_configuration=appintegrations.CfnDataIntegration.FileConfigurationProperty(
                folders=["folders"],
        
                # the properties below are optional
                filters=filters
            ),
            object_configuration=object_configuration,
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
        kms_key: builtins.str,
        name: builtins.str,
        schedule_config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataIntegration.ScheduleConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        source_uri: builtins.str,
        description: typing.Optional[builtins.str] = None,
        file_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataIntegration.FileConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        object_configuration: typing.Any = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param kms_key: The KMS key for the DataIntegration.
        :param name: The name of the DataIntegration.
        :param schedule_config: The name of the data and how often it should be pulled from the source.
        :param source_uri: The URI of the data source.
        :param description: A description of the DataIntegration.
        :param file_configuration: The configuration for what files should be pulled from the source.
        :param object_configuration: The configuration for what data should be pulled from the source.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07830c24dc09b0662b03583ee4edbdbaeb4fabf95d85c4f4ed965ea9d0999f40)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDataIntegrationProps(
            kms_key=kms_key,
            name=name,
            schedule_config=schedule_config,
            source_uri=source_uri,
            description=description,
            file_configuration=file_configuration,
            object_configuration=object_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b6af7441719b460ee4641270770c612fb58e431a8fbcc3d0f99ddae2d585fb7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c538be594c10bcec9c53489ef9157700761163aaf6bc0272307d9a7f7d936952)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrDataIntegrationArn")
    def attr_data_integration_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the DataIntegration.

        :cloudformationAttribute: DataIntegrationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDataIntegrationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''A unique identifier.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

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
    @jsii.member(jsii_name="kmsKey")
    def kms_key(self) -> builtins.str:
        '''The KMS key for the DataIntegration.'''
        return typing.cast(builtins.str, jsii.get(self, "kmsKey"))

    @kms_key.setter
    def kms_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a3cad25e2a72d7ef20681bd49e23420f83d37ece3e2e6187f06b562941a0afc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKey", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the DataIntegration.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e51110622d3f4ff27df719656fd99fc526be5468469b3eea1ec762212e0d0d83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="scheduleConfig")
    def schedule_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnDataIntegration.ScheduleConfigProperty"]:
        '''The name of the data and how often it should be pulled from the source.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDataIntegration.ScheduleConfigProperty"], jsii.get(self, "scheduleConfig"))

    @schedule_config.setter
    def schedule_config(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnDataIntegration.ScheduleConfigProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5245bc847871e6f3d723769c28404578dc706f908a62836394d9ef2b6acc8a92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduleConfig", value)

    @builtins.property
    @jsii.member(jsii_name="sourceUri")
    def source_uri(self) -> builtins.str:
        '''The URI of the data source.'''
        return typing.cast(builtins.str, jsii.get(self, "sourceUri"))

    @source_uri.setter
    def source_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c40d38376f274efd003c192558a948691aa19100c92ffcb8b59fa6c6f3ab8dcc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceUri", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the DataIntegration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac6cbca81b19a3d28448d5b03b3556d234f451a65367c5aece805bf98e731c52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="fileConfiguration")
    def file_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataIntegration.FileConfigurationProperty"]]:
        '''The configuration for what files should be pulled from the source.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataIntegration.FileConfigurationProperty"]], jsii.get(self, "fileConfiguration"))

    @file_configuration.setter
    def file_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataIntegration.FileConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa142812d7a4300d1fdf79595aa40d4ec698ff46a0af150d168d97ee958e67e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="objectConfiguration")
    def object_configuration(self) -> typing.Any:
        '''The configuration for what data should be pulled from the source.'''
        return typing.cast(typing.Any, jsii.get(self, "objectConfiguration"))

    @object_configuration.setter
    def object_configuration(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09c4d150a6b38a21718340d0e7596e6fe23c488efff8579d0b26f44d2d887f87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d778105dbb9cf7d3e71800bafeafc79e0c6102ba3bccf8a3f96fd8b2c9aac3b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appintegrations.CfnDataIntegration.FileConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"folders": "folders", "filters": "filters"},
    )
    class FileConfigurationProperty:
        def __init__(
            self,
            *,
            folders: typing.Sequence[builtins.str],
            filters: typing.Any = None,
        ) -> None:
            '''The configuration for what files should be pulled from the source.

            :param folders: Identifiers for the source folders to pull all files from recursively.
            :param filters: Restrictions for what files should be pulled from the source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-dataintegration-fileconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appintegrations as appintegrations
                
                # filters: Any
                
                file_configuration_property = appintegrations.CfnDataIntegration.FileConfigurationProperty(
                    folders=["folders"],
                
                    # the properties below are optional
                    filters=filters
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e7240d0935d712dd0763236cffe39f34c0eb20f0e4285482cf5e89018d193000)
                check_type(argname="argument folders", value=folders, expected_type=type_hints["folders"])
                check_type(argname="argument filters", value=filters, expected_type=type_hints["filters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "folders": folders,
            }
            if filters is not None:
                self._values["filters"] = filters

        @builtins.property
        def folders(self) -> typing.List[builtins.str]:
            '''Identifiers for the source folders to pull all files from recursively.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-dataintegration-fileconfiguration.html#cfn-appintegrations-dataintegration-fileconfiguration-folders
            '''
            result = self._values.get("folders")
            assert result is not None, "Required property 'folders' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def filters(self) -> typing.Any:
            '''Restrictions for what files should be pulled from the source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-dataintegration-fileconfiguration.html#cfn-appintegrations-dataintegration-fileconfiguration-filters
            '''
            result = self._values.get("filters")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FileConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appintegrations.CfnDataIntegration.ScheduleConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "schedule_expression": "scheduleExpression",
            "first_execution_from": "firstExecutionFrom",
            "object": "object",
        },
    )
    class ScheduleConfigProperty:
        def __init__(
            self,
            *,
            schedule_expression: builtins.str,
            first_execution_from: typing.Optional[builtins.str] = None,
            object: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The name of the data and how often it should be pulled from the source.

            :param schedule_expression: How often the data should be pulled from data source.
            :param first_execution_from: The start date for objects to import in the first flow run as an Unix/epoch timestamp in milliseconds or in ISO-8601 format.
            :param object: The name of the object to pull from the data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-dataintegration-scheduleconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appintegrations as appintegrations
                
                schedule_config_property = appintegrations.CfnDataIntegration.ScheduleConfigProperty(
                    schedule_expression="scheduleExpression",
                
                    # the properties below are optional
                    first_execution_from="firstExecutionFrom",
                    object="object"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1fa0efcac2eeb739bb68a54b8c7816a32a28a265c96601fb14102a1f9a7db338)
                check_type(argname="argument schedule_expression", value=schedule_expression, expected_type=type_hints["schedule_expression"])
                check_type(argname="argument first_execution_from", value=first_execution_from, expected_type=type_hints["first_execution_from"])
                check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "schedule_expression": schedule_expression,
            }
            if first_execution_from is not None:
                self._values["first_execution_from"] = first_execution_from
            if object is not None:
                self._values["object"] = object

        @builtins.property
        def schedule_expression(self) -> builtins.str:
            '''How often the data should be pulled from data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-dataintegration-scheduleconfig.html#cfn-appintegrations-dataintegration-scheduleconfig-scheduleexpression
            '''
            result = self._values.get("schedule_expression")
            assert result is not None, "Required property 'schedule_expression' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def first_execution_from(self) -> typing.Optional[builtins.str]:
            '''The start date for objects to import in the first flow run as an Unix/epoch timestamp in milliseconds or in ISO-8601 format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-dataintegration-scheduleconfig.html#cfn-appintegrations-dataintegration-scheduleconfig-firstexecutionfrom
            '''
            result = self._values.get("first_execution_from")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def object(self) -> typing.Optional[builtins.str]:
            '''The name of the object to pull from the data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-dataintegration-scheduleconfig.html#cfn-appintegrations-dataintegration-scheduleconfig-object
            '''
            result = self._values.get("object")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScheduleConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appintegrations.CfnDataIntegrationProps",
    jsii_struct_bases=[],
    name_mapping={
        "kms_key": "kmsKey",
        "name": "name",
        "schedule_config": "scheduleConfig",
        "source_uri": "sourceUri",
        "description": "description",
        "file_configuration": "fileConfiguration",
        "object_configuration": "objectConfiguration",
        "tags": "tags",
    },
)
class CfnDataIntegrationProps:
    def __init__(
        self,
        *,
        kms_key: builtins.str,
        name: builtins.str,
        schedule_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataIntegration.ScheduleConfigProperty, typing.Dict[builtins.str, typing.Any]]],
        source_uri: builtins.str,
        description: typing.Optional[builtins.str] = None,
        file_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataIntegration.FileConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        object_configuration: typing.Any = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDataIntegration``.

        :param kms_key: The KMS key for the DataIntegration.
        :param name: The name of the DataIntegration.
        :param schedule_config: The name of the data and how often it should be pulled from the source.
        :param source_uri: The URI of the data source.
        :param description: A description of the DataIntegration.
        :param file_configuration: The configuration for what files should be pulled from the source.
        :param object_configuration: The configuration for what data should be pulled from the source.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-dataintegration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appintegrations as appintegrations
            
            # filters: Any
            # object_configuration: Any
            
            cfn_data_integration_props = appintegrations.CfnDataIntegrationProps(
                kms_key="kmsKey",
                name="name",
                schedule_config=appintegrations.CfnDataIntegration.ScheduleConfigProperty(
                    schedule_expression="scheduleExpression",
            
                    # the properties below are optional
                    first_execution_from="firstExecutionFrom",
                    object="object"
                ),
                source_uri="sourceUri",
            
                # the properties below are optional
                description="description",
                file_configuration=appintegrations.CfnDataIntegration.FileConfigurationProperty(
                    folders=["folders"],
            
                    # the properties below are optional
                    filters=filters
                ),
                object_configuration=object_configuration,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4e7b2c594c26fb87f1ee6d6a6b7787330233c7a73e8ce2cfe23ce1b18ffe290)
            check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument schedule_config", value=schedule_config, expected_type=type_hints["schedule_config"])
            check_type(argname="argument source_uri", value=source_uri, expected_type=type_hints["source_uri"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument file_configuration", value=file_configuration, expected_type=type_hints["file_configuration"])
            check_type(argname="argument object_configuration", value=object_configuration, expected_type=type_hints["object_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "kms_key": kms_key,
            "name": name,
            "schedule_config": schedule_config,
            "source_uri": source_uri,
        }
        if description is not None:
            self._values["description"] = description
        if file_configuration is not None:
            self._values["file_configuration"] = file_configuration
        if object_configuration is not None:
            self._values["object_configuration"] = object_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def kms_key(self) -> builtins.str:
        '''The KMS key for the DataIntegration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-dataintegration.html#cfn-appintegrations-dataintegration-kmskey
        '''
        result = self._values.get("kms_key")
        assert result is not None, "Required property 'kms_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the DataIntegration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-dataintegration.html#cfn-appintegrations-dataintegration-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schedule_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnDataIntegration.ScheduleConfigProperty]:
        '''The name of the data and how often it should be pulled from the source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-dataintegration.html#cfn-appintegrations-dataintegration-scheduleconfig
        '''
        result = self._values.get("schedule_config")
        assert result is not None, "Required property 'schedule_config' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnDataIntegration.ScheduleConfigProperty], result)

    @builtins.property
    def source_uri(self) -> builtins.str:
        '''The URI of the data source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-dataintegration.html#cfn-appintegrations-dataintegration-sourceuri
        '''
        result = self._values.get("source_uri")
        assert result is not None, "Required property 'source_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the DataIntegration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-dataintegration.html#cfn-appintegrations-dataintegration-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataIntegration.FileConfigurationProperty]]:
        '''The configuration for what files should be pulled from the source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-dataintegration.html#cfn-appintegrations-dataintegration-fileconfiguration
        '''
        result = self._values.get("file_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataIntegration.FileConfigurationProperty]], result)

    @builtins.property
    def object_configuration(self) -> typing.Any:
        '''The configuration for what data should be pulled from the source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-dataintegration.html#cfn-appintegrations-dataintegration-objectconfiguration
        '''
        result = self._values.get("object_configuration")
        return typing.cast(typing.Any, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-dataintegration.html#cfn-appintegrations-dataintegration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataIntegrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnEventIntegration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appintegrations.CfnEventIntegration",
):
    '''Creates an event integration.

    You provide a name, description, and a reference to an Amazon EventBridge bus in your account and a partner event source that will push events to that bus. No objects are created in your account, only metadata that is persisted on the EventIntegration control plane.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appintegrations as appintegrations
        
        cfn_event_integration = appintegrations.CfnEventIntegration(self, "MyCfnEventIntegration",
            event_bridge_bus="eventBridgeBus",
            event_filter=appintegrations.CfnEventIntegration.EventFilterProperty(
                source="source"
            ),
            name="name",
        
            # the properties below are optional
            description="description",
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
        event_bridge_bus: builtins.str,
        event_filter: typing.Union[_IResolvable_da3f097b, typing.Union["CfnEventIntegration.EventFilterProperty", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param event_bridge_bus: The Amazon EventBridge bus for the event integration.
        :param event_filter: The event integration filter.
        :param name: The name of the event integration.
        :param description: The event integration description.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f4a16fc332806342706d2878c9a173a25d599659c9ec58d0c31e1ae7a621e4f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEventIntegrationProps(
            event_bridge_bus=event_bridge_bus,
            event_filter=event_filter,
            name=name,
            description=description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73b155f65b8c626e094fd78079276b84b0fcfa577110b2ffa5fd975593086533)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d2dd2ffc1f659143f7a6cb15c06dae8c737a11c4d5a56af0a3337f921ebd81e1)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrEventIntegrationArn")
    def attr_event_integration_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the event integration.

        :cloudformationAttribute: EventIntegrationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEventIntegrationArn"))

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
    @jsii.member(jsii_name="eventBridgeBus")
    def event_bridge_bus(self) -> builtins.str:
        '''The Amazon EventBridge bus for the event integration.'''
        return typing.cast(builtins.str, jsii.get(self, "eventBridgeBus"))

    @event_bridge_bus.setter
    def event_bridge_bus(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__454b16c02d23ad7183df72a0517049ca680971186fd144d912c66c66f41479b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventBridgeBus", value)

    @builtins.property
    @jsii.member(jsii_name="eventFilter")
    def event_filter(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnEventIntegration.EventFilterProperty"]:
        '''The event integration filter.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnEventIntegration.EventFilterProperty"], jsii.get(self, "eventFilter"))

    @event_filter.setter
    def event_filter(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnEventIntegration.EventFilterProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26c1d519a62cc46ab080cc71141eaf4a08280d9dfa5cc2110dd627f095a67241)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventFilter", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the event integration.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e44ab4713818a147dca8ac5a9022090f6d871398c1671b532e61470fc234e20f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The event integration description.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16fd4e12e97916052e3996eda8c3774583ca79f8ceda9b5fca42d81c38c9ad1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1545291bb728d092049a68fe1f3f167513ab081a64c955a81627589c9ef4bfa1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appintegrations.CfnEventIntegration.EventFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"source": "source"},
    )
    class EventFilterProperty:
        def __init__(self, *, source: builtins.str) -> None:
            '''The event integration filter.

            :param source: The source of the events.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-eventintegration-eventfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appintegrations as appintegrations
                
                event_filter_property = appintegrations.CfnEventIntegration.EventFilterProperty(
                    source="source"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fe2caaefe76d9510e6ff29f9afdf7706ad87988fce20dbb68ad8862bcbb22154)
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "source": source,
            }

        @builtins.property
        def source(self) -> builtins.str:
            '''The source of the events.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-eventintegration-eventfilter.html#cfn-appintegrations-eventintegration-eventfilter-source
            '''
            result = self._values.get("source")
            assert result is not None, "Required property 'source' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appintegrations.CfnEventIntegrationProps",
    jsii_struct_bases=[],
    name_mapping={
        "event_bridge_bus": "eventBridgeBus",
        "event_filter": "eventFilter",
        "name": "name",
        "description": "description",
        "tags": "tags",
    },
)
class CfnEventIntegrationProps:
    def __init__(
        self,
        *,
        event_bridge_bus: builtins.str,
        event_filter: typing.Union[_IResolvable_da3f097b, typing.Union[CfnEventIntegration.EventFilterProperty, typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEventIntegration``.

        :param event_bridge_bus: The Amazon EventBridge bus for the event integration.
        :param event_filter: The event integration filter.
        :param name: The name of the event integration.
        :param description: The event integration description.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appintegrations as appintegrations
            
            cfn_event_integration_props = appintegrations.CfnEventIntegrationProps(
                event_bridge_bus="eventBridgeBus",
                event_filter=appintegrations.CfnEventIntegration.EventFilterProperty(
                    source="source"
                ),
                name="name",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9153bde28b2e9d1843c748f4d513f8ac68ef7ba9754ea2cdad14193f14742d6)
            check_type(argname="argument event_bridge_bus", value=event_bridge_bus, expected_type=type_hints["event_bridge_bus"])
            check_type(argname="argument event_filter", value=event_filter, expected_type=type_hints["event_filter"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "event_bridge_bus": event_bridge_bus,
            "event_filter": event_filter,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def event_bridge_bus(self) -> builtins.str:
        '''The Amazon EventBridge bus for the event integration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html#cfn-appintegrations-eventintegration-eventbridgebus
        '''
        result = self._values.get("event_bridge_bus")
        assert result is not None, "Required property 'event_bridge_bus' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_filter(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnEventIntegration.EventFilterProperty]:
        '''The event integration filter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html#cfn-appintegrations-eventintegration-eventfilter
        '''
        result = self._values.get("event_filter")
        assert result is not None, "Required property 'event_filter' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnEventIntegration.EventFilterProperty], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the event integration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html#cfn-appintegrations-eventintegration-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The event integration description.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html#cfn-appintegrations-eventintegration-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html#cfn-appintegrations-eventintegration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEventIntegrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDataIntegration",
    "CfnDataIntegrationProps",
    "CfnEventIntegration",
    "CfnEventIntegrationProps",
]

publication.publish()

def _typecheckingstub__07830c24dc09b0662b03583ee4edbdbaeb4fabf95d85c4f4ed965ea9d0999f40(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    kms_key: builtins.str,
    name: builtins.str,
    schedule_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataIntegration.ScheduleConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    source_uri: builtins.str,
    description: typing.Optional[builtins.str] = None,
    file_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataIntegration.FileConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    object_configuration: typing.Any = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b6af7441719b460ee4641270770c612fb58e431a8fbcc3d0f99ddae2d585fb7(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c538be594c10bcec9c53489ef9157700761163aaf6bc0272307d9a7f7d936952(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a3cad25e2a72d7ef20681bd49e23420f83d37ece3e2e6187f06b562941a0afc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e51110622d3f4ff27df719656fd99fc526be5468469b3eea1ec762212e0d0d83(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5245bc847871e6f3d723769c28404578dc706f908a62836394d9ef2b6acc8a92(
    value: typing.Union[_IResolvable_da3f097b, CfnDataIntegration.ScheduleConfigProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c40d38376f274efd003c192558a948691aa19100c92ffcb8b59fa6c6f3ab8dcc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac6cbca81b19a3d28448d5b03b3556d234f451a65367c5aece805bf98e731c52(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa142812d7a4300d1fdf79595aa40d4ec698ff46a0af150d168d97ee958e67e1(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataIntegration.FileConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09c4d150a6b38a21718340d0e7596e6fe23c488efff8579d0b26f44d2d887f87(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d778105dbb9cf7d3e71800bafeafc79e0c6102ba3bccf8a3f96fd8b2c9aac3b2(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7240d0935d712dd0763236cffe39f34c0eb20f0e4285482cf5e89018d193000(
    *,
    folders: typing.Sequence[builtins.str],
    filters: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fa0efcac2eeb739bb68a54b8c7816a32a28a265c96601fb14102a1f9a7db338(
    *,
    schedule_expression: builtins.str,
    first_execution_from: typing.Optional[builtins.str] = None,
    object: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4e7b2c594c26fb87f1ee6d6a6b7787330233c7a73e8ce2cfe23ce1b18ffe290(
    *,
    kms_key: builtins.str,
    name: builtins.str,
    schedule_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataIntegration.ScheduleConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    source_uri: builtins.str,
    description: typing.Optional[builtins.str] = None,
    file_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataIntegration.FileConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    object_configuration: typing.Any = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f4a16fc332806342706d2878c9a173a25d599659c9ec58d0c31e1ae7a621e4f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    event_bridge_bus: builtins.str,
    event_filter: typing.Union[_IResolvable_da3f097b, typing.Union[CfnEventIntegration.EventFilterProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73b155f65b8c626e094fd78079276b84b0fcfa577110b2ffa5fd975593086533(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2dd2ffc1f659143f7a6cb15c06dae8c737a11c4d5a56af0a3337f921ebd81e1(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__454b16c02d23ad7183df72a0517049ca680971186fd144d912c66c66f41479b7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26c1d519a62cc46ab080cc71141eaf4a08280d9dfa5cc2110dd627f095a67241(
    value: typing.Union[_IResolvable_da3f097b, CfnEventIntegration.EventFilterProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e44ab4713818a147dca8ac5a9022090f6d871398c1671b532e61470fc234e20f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16fd4e12e97916052e3996eda8c3774583ca79f8ceda9b5fca42d81c38c9ad1d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1545291bb728d092049a68fe1f3f167513ab081a64c955a81627589c9ef4bfa1(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe2caaefe76d9510e6ff29f9afdf7706ad87988fce20dbb68ad8862bcbb22154(
    *,
    source: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9153bde28b2e9d1843c748f4d513f8ac68ef7ba9754ea2cdad14193f14742d6(
    *,
    event_bridge_bus: builtins.str,
    event_filter: typing.Union[_IResolvable_da3f097b, typing.Union[CfnEventIntegration.EventFilterProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
