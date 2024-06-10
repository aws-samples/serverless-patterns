'''
# AWS::CleanRoomsML Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_cleanroomsml as cleanroomsml
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for CleanRoomsML construct libraries](https://constructs.dev/search?q=cleanroomsml)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::CleanRoomsML resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CleanRoomsML.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::CleanRoomsML](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CleanRoomsML.html).

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
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnTrainingDataset(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cleanroomsml.CfnTrainingDataset",
):
    '''Defines the information necessary to create a training dataset.

    In Clean Rooms ML, the ``TrainingDataset`` is metadata that points to a Glue table, which is read only during ``AudienceModel`` creation.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanroomsml-trainingdataset.html
    :cloudformationResource: AWS::CleanRoomsML::TrainingDataset
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cleanroomsml as cleanroomsml
        
        cfn_training_dataset = cleanroomsml.CfnTrainingDataset(self, "MyCfnTrainingDataset",
            name="name",
            role_arn="roleArn",
            training_data=[cleanroomsml.CfnTrainingDataset.DatasetProperty(
                input_config=cleanroomsml.CfnTrainingDataset.DatasetInputConfigProperty(
                    data_source=cleanroomsml.CfnTrainingDataset.DataSourceProperty(
                        glue_data_source=cleanroomsml.CfnTrainingDataset.GlueDataSourceProperty(
                            database_name="databaseName",
                            table_name="tableName",
        
                            # the properties below are optional
                            catalog_id="catalogId"
                        )
                    ),
                    schema=[cleanroomsml.CfnTrainingDataset.ColumnSchemaProperty(
                        column_name="columnName",
                        column_types=["columnTypes"]
                    )]
                ),
                type="type"
            )],
        
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
        name: builtins.str,
        role_arn: builtins.str,
        training_data: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTrainingDataset.DatasetProperty", typing.Dict[builtins.str, typing.Any]]]]],
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the training dataset.
        :param role_arn: The ARN of the IAM role that Clean Rooms ML can assume to read the data referred to in the ``dataSource`` field of each dataset. Passing a role across accounts is not allowed. If you pass a role that isn't in your account, you get an ``AccessDeniedException`` error.
        :param training_data: An array of information that lists the Dataset objects, which specifies the dataset type and details on its location and schema. You must provide a role that has read access to these tables.
        :param description: The description of the training dataset.
        :param tags: The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. The following basic restrictions apply to tags: - Maximum number of tags per resource - 50. - For each resource, each tag key must be unique, and each tag key can have only one value. - Maximum key length - 128 Unicode characters in UTF-8. - Maximum value length - 256 Unicode characters in UTF-8. - If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : /
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__038c489df01bd94323363a194424fbe900aac226689cefa852a1f05e78d3bf55)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTrainingDatasetProps(
            name=name,
            role_arn=role_arn,
            training_data=training_data,
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
            type_hints = typing.get_type_hints(_typecheckingstub__9028b0a86b67eeece54985e3b32f00cd36517f094fd9d81836504af70a287532)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9a85a48fae07d74ac7e0c59e9b85c0b8f0441d9c407bfe3085fc7206894045b9)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the training dataset.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrTrainingDatasetArn")
    def attr_training_dataset_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the training dataset.

        :cloudformationAttribute: TrainingDatasetArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTrainingDatasetArn"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the training dataset.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__494f55ff0a6978c4165f5d363cd591484cf83133d7818ceede53e907d0c936c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The ARN of the IAM role that Clean Rooms ML can assume to read the data referred to in the ``dataSource`` field of each dataset.'''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dd3ad8ea8435bdf184f933dfcef7f130800d9b2a40eae3e2318bb9c9a09e4e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="trainingData")
    def training_data(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTrainingDataset.DatasetProperty"]]]:
        '''An array of information that lists the Dataset objects, which specifies the dataset type and details on its location and schema.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTrainingDataset.DatasetProperty"]]], jsii.get(self, "trainingData"))

    @training_data.setter
    def training_data(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTrainingDataset.DatasetProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc1942d638c495e8ce078a6ab83bfe20a886d72c3fb786c501cd684c593146ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trainingData", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the training dataset.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1072b383b65b621f0fc0b4b9426fe6c12552a36489cacafc4d1d23d46a07fc1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The optional metadata that you apply to the resource to help you categorize and organize them.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3b6f50dc896f0f57ebfe75a224d400087cca80791cfac1f7d4afe9d1151d747)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanroomsml.CfnTrainingDataset.ColumnSchemaProperty",
        jsii_struct_bases=[],
        name_mapping={"column_name": "columnName", "column_types": "columnTypes"},
    )
    class ColumnSchemaProperty:
        def __init__(
            self,
            *,
            column_name: builtins.str,
            column_types: typing.Sequence[builtins.str],
        ) -> None:
            '''Metadata for a column.

            :param column_name: The name of a column.
            :param column_types: The data type of column.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-trainingdataset-columnschema.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanroomsml as cleanroomsml
                
                column_schema_property = cleanroomsml.CfnTrainingDataset.ColumnSchemaProperty(
                    column_name="columnName",
                    column_types=["columnTypes"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__15de5d6643671de2a88fad9d9afaad1a33eaa500023772c59a4b9d5f2c0e5ca5)
                check_type(argname="argument column_name", value=column_name, expected_type=type_hints["column_name"])
                check_type(argname="argument column_types", value=column_types, expected_type=type_hints["column_types"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "column_name": column_name,
                "column_types": column_types,
            }

        @builtins.property
        def column_name(self) -> builtins.str:
            '''The name of a column.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-trainingdataset-columnschema.html#cfn-cleanroomsml-trainingdataset-columnschema-columnname
            '''
            result = self._values.get("column_name")
            assert result is not None, "Required property 'column_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def column_types(self) -> typing.List[builtins.str]:
            '''The data type of column.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-trainingdataset-columnschema.html#cfn-cleanroomsml-trainingdataset-columnschema-columntypes
            '''
            result = self._values.get("column_types")
            assert result is not None, "Required property 'column_types' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ColumnSchemaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanroomsml.CfnTrainingDataset.DataSourceProperty",
        jsii_struct_bases=[],
        name_mapping={"glue_data_source": "glueDataSource"},
    )
    class DataSourceProperty:
        def __init__(
            self,
            *,
            glue_data_source: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTrainingDataset.GlueDataSourceProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Defines information about the Glue data source that contains the training data.

            :param glue_data_source: A GlueDataSource object that defines the catalog ID, database name, and table name for the training data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-trainingdataset-datasource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanroomsml as cleanroomsml
                
                data_source_property = cleanroomsml.CfnTrainingDataset.DataSourceProperty(
                    glue_data_source=cleanroomsml.CfnTrainingDataset.GlueDataSourceProperty(
                        database_name="databaseName",
                        table_name="tableName",
                
                        # the properties below are optional
                        catalog_id="catalogId"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d605167b33212652a5badb6d4db40ca8e474bafedbd9c8b5354317bb8e696966)
                check_type(argname="argument glue_data_source", value=glue_data_source, expected_type=type_hints["glue_data_source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "glue_data_source": glue_data_source,
            }

        @builtins.property
        def glue_data_source(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTrainingDataset.GlueDataSourceProperty"]:
            '''A GlueDataSource object that defines the catalog ID, database name, and table name for the training data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-trainingdataset-datasource.html#cfn-cleanroomsml-trainingdataset-datasource-gluedatasource
            '''
            result = self._values.get("glue_data_source")
            assert result is not None, "Required property 'glue_data_source' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTrainingDataset.GlueDataSourceProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanroomsml.CfnTrainingDataset.DatasetInputConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"data_source": "dataSource", "schema": "schema"},
    )
    class DatasetInputConfigProperty:
        def __init__(
            self,
            *,
            data_source: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTrainingDataset.DataSourceProperty", typing.Dict[builtins.str, typing.Any]]],
            schema: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTrainingDataset.ColumnSchemaProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''Defines the Glue data source and schema mapping information.

            :param data_source: A DataSource object that specifies the Glue data source for the training data.
            :param schema: The schema information for the training data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-trainingdataset-datasetinputconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanroomsml as cleanroomsml
                
                dataset_input_config_property = cleanroomsml.CfnTrainingDataset.DatasetInputConfigProperty(
                    data_source=cleanroomsml.CfnTrainingDataset.DataSourceProperty(
                        glue_data_source=cleanroomsml.CfnTrainingDataset.GlueDataSourceProperty(
                            database_name="databaseName",
                            table_name="tableName",
                
                            # the properties below are optional
                            catalog_id="catalogId"
                        )
                    ),
                    schema=[cleanroomsml.CfnTrainingDataset.ColumnSchemaProperty(
                        column_name="columnName",
                        column_types=["columnTypes"]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ab93d97f5b26accc73a8c37bd47a1cbf272dd2d33e0ff1a267931c622072b676)
                check_type(argname="argument data_source", value=data_source, expected_type=type_hints["data_source"])
                check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "data_source": data_source,
                "schema": schema,
            }

        @builtins.property
        def data_source(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTrainingDataset.DataSourceProperty"]:
            '''A DataSource object that specifies the Glue data source for the training data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-trainingdataset-datasetinputconfig.html#cfn-cleanroomsml-trainingdataset-datasetinputconfig-datasource
            '''
            result = self._values.get("data_source")
            assert result is not None, "Required property 'data_source' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTrainingDataset.DataSourceProperty"], result)

        @builtins.property
        def schema(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTrainingDataset.ColumnSchemaProperty"]]]:
            '''The schema information for the training data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-trainingdataset-datasetinputconfig.html#cfn-cleanroomsml-trainingdataset-datasetinputconfig-schema
            '''
            result = self._values.get("schema")
            assert result is not None, "Required property 'schema' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTrainingDataset.ColumnSchemaProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatasetInputConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanroomsml.CfnTrainingDataset.DatasetProperty",
        jsii_struct_bases=[],
        name_mapping={"input_config": "inputConfig", "type": "type"},
    )
    class DatasetProperty:
        def __init__(
            self,
            *,
            input_config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTrainingDataset.DatasetInputConfigProperty", typing.Dict[builtins.str, typing.Any]]],
            type: builtins.str,
        ) -> None:
            '''Defines where the training dataset is located, what type of data it contains, and how to access the data.

            :param input_config: A DatasetInputConfig object that defines the data source and schema mapping.
            :param type: What type of information is found in the dataset.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-trainingdataset-dataset.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanroomsml as cleanroomsml
                
                dataset_property = cleanroomsml.CfnTrainingDataset.DatasetProperty(
                    input_config=cleanroomsml.CfnTrainingDataset.DatasetInputConfigProperty(
                        data_source=cleanroomsml.CfnTrainingDataset.DataSourceProperty(
                            glue_data_source=cleanroomsml.CfnTrainingDataset.GlueDataSourceProperty(
                                database_name="databaseName",
                                table_name="tableName",
                
                                # the properties below are optional
                                catalog_id="catalogId"
                            )
                        ),
                        schema=[cleanroomsml.CfnTrainingDataset.ColumnSchemaProperty(
                            column_name="columnName",
                            column_types=["columnTypes"]
                        )]
                    ),
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__38a3a37ec245bf1288fe1fb7ea7c3d9b1d3b4642f41f30639da52a4dca9bd86c)
                check_type(argname="argument input_config", value=input_config, expected_type=type_hints["input_config"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "input_config": input_config,
                "type": type,
            }

        @builtins.property
        def input_config(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTrainingDataset.DatasetInputConfigProperty"]:
            '''A DatasetInputConfig object that defines the data source and schema mapping.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-trainingdataset-dataset.html#cfn-cleanroomsml-trainingdataset-dataset-inputconfig
            '''
            result = self._values.get("input_config")
            assert result is not None, "Required property 'input_config' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTrainingDataset.DatasetInputConfigProperty"], result)

        @builtins.property
        def type(self) -> builtins.str:
            '''What type of information is found in the dataset.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-trainingdataset-dataset.html#cfn-cleanroomsml-trainingdataset-dataset-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatasetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanroomsml.CfnTrainingDataset.GlueDataSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "database_name": "databaseName",
            "table_name": "tableName",
            "catalog_id": "catalogId",
        },
    )
    class GlueDataSourceProperty:
        def __init__(
            self,
            *,
            database_name: builtins.str,
            table_name: builtins.str,
            catalog_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines the Glue data source that contains the training data.

            :param database_name: The Glue database that contains the training data.
            :param table_name: The Glue table that contains the training data.
            :param catalog_id: The Glue catalog that contains the training data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-trainingdataset-gluedatasource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanroomsml as cleanroomsml
                
                glue_data_source_property = cleanroomsml.CfnTrainingDataset.GlueDataSourceProperty(
                    database_name="databaseName",
                    table_name="tableName",
                
                    # the properties below are optional
                    catalog_id="catalogId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__960bc53c7c406ea248f393051fd58abbf5074d22e0eb6439f849d7558cb02ffd)
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "database_name": database_name,
                "table_name": table_name,
            }
            if catalog_id is not None:
                self._values["catalog_id"] = catalog_id

        @builtins.property
        def database_name(self) -> builtins.str:
            '''The Glue database that contains the training data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-trainingdataset-gluedatasource.html#cfn-cleanroomsml-trainingdataset-gluedatasource-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_name(self) -> builtins.str:
            '''The Glue table that contains the training data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-trainingdataset-gluedatasource.html#cfn-cleanroomsml-trainingdataset-gluedatasource-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def catalog_id(self) -> typing.Optional[builtins.str]:
            '''The Glue catalog that contains the training data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-trainingdataset-gluedatasource.html#cfn-cleanroomsml-trainingdataset-gluedatasource-catalogid
            '''
            result = self._values.get("catalog_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GlueDataSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cleanroomsml.CfnTrainingDatasetProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "role_arn": "roleArn",
        "training_data": "trainingData",
        "description": "description",
        "tags": "tags",
    },
)
class CfnTrainingDatasetProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        role_arn: builtins.str,
        training_data: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrainingDataset.DatasetProperty, typing.Dict[builtins.str, typing.Any]]]]],
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTrainingDataset``.

        :param name: The name of the training dataset.
        :param role_arn: The ARN of the IAM role that Clean Rooms ML can assume to read the data referred to in the ``dataSource`` field of each dataset. Passing a role across accounts is not allowed. If you pass a role that isn't in your account, you get an ``AccessDeniedException`` error.
        :param training_data: An array of information that lists the Dataset objects, which specifies the dataset type and details on its location and schema. You must provide a role that has read access to these tables.
        :param description: The description of the training dataset.
        :param tags: The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. The following basic restrictions apply to tags: - Maximum number of tags per resource - 50. - For each resource, each tag key must be unique, and each tag key can have only one value. - Maximum key length - 128 Unicode characters in UTF-8. - Maximum value length - 256 Unicode characters in UTF-8. - If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : /

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanroomsml-trainingdataset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cleanroomsml as cleanroomsml
            
            cfn_training_dataset_props = cleanroomsml.CfnTrainingDatasetProps(
                name="name",
                role_arn="roleArn",
                training_data=[cleanroomsml.CfnTrainingDataset.DatasetProperty(
                    input_config=cleanroomsml.CfnTrainingDataset.DatasetInputConfigProperty(
                        data_source=cleanroomsml.CfnTrainingDataset.DataSourceProperty(
                            glue_data_source=cleanroomsml.CfnTrainingDataset.GlueDataSourceProperty(
                                database_name="databaseName",
                                table_name="tableName",
            
                                # the properties below are optional
                                catalog_id="catalogId"
                            )
                        ),
                        schema=[cleanroomsml.CfnTrainingDataset.ColumnSchemaProperty(
                            column_name="columnName",
                            column_types=["columnTypes"]
                        )]
                    ),
                    type="type"
                )],
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a83ce04ef3c373a0c189c16bb2a7e23aea1fda52268a69a4e97e560d76564547)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument training_data", value=training_data, expected_type=type_hints["training_data"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "role_arn": role_arn,
            "training_data": training_data,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the training dataset.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanroomsml-trainingdataset.html#cfn-cleanroomsml-trainingdataset-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The ARN of the IAM role that Clean Rooms ML can assume to read the data referred to in the ``dataSource`` field of each dataset.

        Passing a role across accounts is not allowed. If you pass a role that isn't in your account, you get an ``AccessDeniedException`` error.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanroomsml-trainingdataset.html#cfn-cleanroomsml-trainingdataset-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def training_data(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTrainingDataset.DatasetProperty]]]:
        '''An array of information that lists the Dataset objects, which specifies the dataset type and details on its location and schema.

        You must provide a role that has read access to these tables.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanroomsml-trainingdataset.html#cfn-cleanroomsml-trainingdataset-trainingdata
        '''
        result = self._values.get("training_data")
        assert result is not None, "Required property 'training_data' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTrainingDataset.DatasetProperty]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the training dataset.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanroomsml-trainingdataset.html#cfn-cleanroomsml-trainingdataset-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The optional metadata that you apply to the resource to help you categorize and organize them.

        Each tag consists of a key and an optional value, both of which you define.

        The following basic restrictions apply to tags:

        - Maximum number of tags per resource - 50.
        - For each resource, each tag key must be unique, and each tag key can have only one value.
        - Maximum key length - 128 Unicode characters in UTF-8.
        - Maximum value length - 256 Unicode characters in UTF-8.
        - If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : /

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanroomsml-trainingdataset.html#cfn-cleanroomsml-trainingdataset-tags
        ::

        .

        - Tag keys and values are case sensitive.
        - Do not use ``aws:`` , ``AWS:`` , or any upper or lowercase combination of such as a prefix for keys as it is reserved. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has ``aws`` as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of ``aws`` do not count against your tags per resource limit.
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTrainingDatasetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnTrainingDataset",
    "CfnTrainingDatasetProps",
]

publication.publish()

def _typecheckingstub__038c489df01bd94323363a194424fbe900aac226689cefa852a1f05e78d3bf55(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    role_arn: builtins.str,
    training_data: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrainingDataset.DatasetProperty, typing.Dict[builtins.str, typing.Any]]]]],
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9028b0a86b67eeece54985e3b32f00cd36517f094fd9d81836504af70a287532(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a85a48fae07d74ac7e0c59e9b85c0b8f0441d9c407bfe3085fc7206894045b9(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__494f55ff0a6978c4165f5d363cd591484cf83133d7818ceede53e907d0c936c8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dd3ad8ea8435bdf184f933dfcef7f130800d9b2a40eae3e2318bb9c9a09e4e6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc1942d638c495e8ce078a6ab83bfe20a886d72c3fb786c501cd684c593146ac(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTrainingDataset.DatasetProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1072b383b65b621f0fc0b4b9426fe6c12552a36489cacafc4d1d23d46a07fc1f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3b6f50dc896f0f57ebfe75a224d400087cca80791cfac1f7d4afe9d1151d747(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15de5d6643671de2a88fad9d9afaad1a33eaa500023772c59a4b9d5f2c0e5ca5(
    *,
    column_name: builtins.str,
    column_types: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d605167b33212652a5badb6d4db40ca8e474bafedbd9c8b5354317bb8e696966(
    *,
    glue_data_source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrainingDataset.GlueDataSourceProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab93d97f5b26accc73a8c37bd47a1cbf272dd2d33e0ff1a267931c622072b676(
    *,
    data_source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrainingDataset.DataSourceProperty, typing.Dict[builtins.str, typing.Any]]],
    schema: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrainingDataset.ColumnSchemaProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38a3a37ec245bf1288fe1fb7ea7c3d9b1d3b4642f41f30639da52a4dca9bd86c(
    *,
    input_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrainingDataset.DatasetInputConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__960bc53c7c406ea248f393051fd58abbf5074d22e0eb6439f849d7558cb02ffd(
    *,
    database_name: builtins.str,
    table_name: builtins.str,
    catalog_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a83ce04ef3c373a0c189c16bb2a7e23aea1fda52268a69a4e97e560d76564547(
    *,
    name: builtins.str,
    role_arn: builtins.str,
    training_data: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrainingDataset.DatasetProperty, typing.Dict[builtins.str, typing.Any]]]]],
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
