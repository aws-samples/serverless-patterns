'''
# AWS::BCMDataExports Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_bcmdataexports as bcmdataexports
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for BCMDataExports construct libraries](https://constructs.dev/search?q=bcmdataexports)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::BCMDataExports resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_BCMDataExports.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::BCMDataExports](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_BCMDataExports.html).

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
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnExport(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_bcmdataexports.CfnExport",
):
    '''Creates a data export and specifies the data query, the delivery preference, and any optional resource tags.

    A ``DataQuery`` consists of both a ``QueryStatement`` and ``TableConfigurations`` .

    The ``QueryStatement`` is an SQL statement. Data Exports only supports a limited subset of the SQL syntax. For more information on the SQL syntax that is supported, see `Data query <https://docs.aws.amazon.com/cur/latest/userguide/de-data-query.html>`_ . To view the available tables and columns, see the `Data Exports table dictionary <https://docs.aws.amazon.com/cur/latest/userguide/de-table-dictionary.html>`_ .

    The ``TableConfigurations`` is a collection of specified ``TableProperties`` for the table being queried in the ``QueryStatement`` . TableProperties are additional configurations you can provide to change the data and schema of a table. Each table can have different TableProperties. However, tables are not required to have any TableProperties. Each table property has a default value that it assumes if not specified. For more information on table configurations, see `Data query <https://docs.aws.amazon.com/cur/latest/userguide/de-data-query.html>`_ . To view the table properties available for each table, see the `Data Exports table dictionary <https://docs.aws.amazon.com/cur/latest/userguide/de-table-dictionary.html>`_ or use the ``ListTables`` API to get a response of all tables and their available properties.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bcmdataexports-export.html
    :cloudformationResource: AWS::BCMDataExports::Export
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_bcmdataexports as bcmdataexports
        
        cfn_export = bcmdataexports.CfnExport(self, "MyCfnExport",
            export=bcmdataexports.CfnExport.ExportProperty(
                data_query=bcmdataexports.CfnExport.DataQueryProperty(
                    query_statement="queryStatement",
        
                    # the properties below are optional
                    table_configurations={
                        "table_configurations_key": {
                            "table_configurations_key": "tableConfigurations"
                        }
                    }
                ),
                destination_configurations=bcmdataexports.CfnExport.DestinationConfigurationsProperty(
                    s3_destination=bcmdataexports.CfnExport.S3DestinationProperty(
                        s3_bucket="s3Bucket",
                        s3_output_configurations=bcmdataexports.CfnExport.S3OutputConfigurationsProperty(
                            compression="compression",
                            format="format",
                            output_type="outputType",
                            overwrite="overwrite"
                        ),
                        s3_prefix="s3Prefix",
                        s3_region="s3Region"
                    )
                ),
                name="name",
                refresh_cadence=bcmdataexports.CfnExport.RefreshCadenceProperty(
                    frequency="frequency"
                ),
        
                # the properties below are optional
                description="description",
                export_arn="exportArn"
            ),
        
            # the properties below are optional
            tags=[bcmdataexports.CfnExport.ResourceTagProperty(
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
        export: typing.Union[_IResolvable_da3f097b, typing.Union["CfnExport.ExportProperty", typing.Dict[builtins.str, typing.Any]]],
        tags: typing.Optional[typing.Sequence[typing.Union["CfnExport.ResourceTagProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param export: The details that are available for an export.
        :param tags: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2bcca1af59fac907ca8714563d055c566e701daae8450fde60df7c0e3d3db64)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnExportProps(export=export, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1dac39dc3be3191a8c16e738400531fa018e236e77c82fbfaa9dc5f869f22217)
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
            type_hints = typing.get_type_hints(_typecheckingstub__eb93537976d222e41558fc4b0c82267089734f222dad1d93d6bf9ac01baf7235)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrExportArn")
    def attr_export_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for this export.

        :cloudformationAttribute: ExportArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrExportArn"))

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
    @jsii.member(jsii_name="export")
    def export(self) -> typing.Union[_IResolvable_da3f097b, "CfnExport.ExportProperty"]:
        '''The details that are available for an export.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnExport.ExportProperty"], jsii.get(self, "export"))

    @export.setter
    def export(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnExport.ExportProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8ce26f4856f4fbb56e9f2fa30a5520af71bb0fab07aab599f3d350bcd7af208)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "export", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["CfnExport.ResourceTagProperty"]]:
        return typing.cast(typing.Optional[typing.List["CfnExport.ResourceTagProperty"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["CfnExport.ResourceTagProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ad623342e4c1e6ad8d0a1e800f480ca841fcc2866deb4be0a499fc18bffc658)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bcmdataexports.CfnExport.DataQueryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "query_statement": "queryStatement",
            "table_configurations": "tableConfigurations",
        },
    )
    class DataQueryProperty:
        def __init__(
            self,
            *,
            query_statement: builtins.str,
            table_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]]] = None,
        ) -> None:
            '''The SQL query of column selections and row filters from the data table you want.

            :param query_statement: The query statement.
            :param table_configurations: The table configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bcmdataexports-export-dataquery.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bcmdataexports as bcmdataexports
                
                data_query_property = bcmdataexports.CfnExport.DataQueryProperty(
                    query_statement="queryStatement",
                
                    # the properties below are optional
                    table_configurations={
                        "table_configurations_key": {
                            "table_configurations_key": "tableConfigurations"
                        }
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e1a095753612659582b4b6117f8c7de657221f82c66d4926cce19af238d91343)
                check_type(argname="argument query_statement", value=query_statement, expected_type=type_hints["query_statement"])
                check_type(argname="argument table_configurations", value=table_configurations, expected_type=type_hints["table_configurations"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "query_statement": query_statement,
            }
            if table_configurations is not None:
                self._values["table_configurations"] = table_configurations

        @builtins.property
        def query_statement(self) -> builtins.str:
            '''The query statement.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bcmdataexports-export-dataquery.html#cfn-bcmdataexports-export-dataquery-querystatement
            '''
            result = self._values.get("query_statement")
            assert result is not None, "Required property 'query_statement' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_configurations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]]]:
            '''The table configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bcmdataexports-export-dataquery.html#cfn-bcmdataexports-export-dataquery-tableconfigurations
            '''
            result = self._values.get("table_configurations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataQueryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bcmdataexports.CfnExport.DestinationConfigurationsProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_destination": "s3Destination"},
    )
    class DestinationConfigurationsProperty:
        def __init__(
            self,
            *,
            s3_destination: typing.Union[_IResolvable_da3f097b, typing.Union["CfnExport.S3DestinationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The destinations used for data exports.

            :param s3_destination: An object that describes the destination of the data exports file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bcmdataexports-export-destinationconfigurations.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bcmdataexports as bcmdataexports
                
                destination_configurations_property = bcmdataexports.CfnExport.DestinationConfigurationsProperty(
                    s3_destination=bcmdataexports.CfnExport.S3DestinationProperty(
                        s3_bucket="s3Bucket",
                        s3_output_configurations=bcmdataexports.CfnExport.S3OutputConfigurationsProperty(
                            compression="compression",
                            format="format",
                            output_type="outputType",
                            overwrite="overwrite"
                        ),
                        s3_prefix="s3Prefix",
                        s3_region="s3Region"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__816060235493801ab48e2f3ab492e0786d6ff854a29cb93dcb295018d334cec5)
                check_type(argname="argument s3_destination", value=s3_destination, expected_type=type_hints["s3_destination"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "s3_destination": s3_destination,
            }

        @builtins.property
        def s3_destination(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnExport.S3DestinationProperty"]:
            '''An object that describes the destination of the data exports file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bcmdataexports-export-destinationconfigurations.html#cfn-bcmdataexports-export-destinationconfigurations-s3destination
            '''
            result = self._values.get("s3_destination")
            assert result is not None, "Required property 's3_destination' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnExport.S3DestinationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DestinationConfigurationsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bcmdataexports.CfnExport.ExportProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_query": "dataQuery",
            "destination_configurations": "destinationConfigurations",
            "name": "name",
            "refresh_cadence": "refreshCadence",
            "description": "description",
            "export_arn": "exportArn",
        },
    )
    class ExportProperty:
        def __init__(
            self,
            *,
            data_query: typing.Union[_IResolvable_da3f097b, typing.Union["CfnExport.DataQueryProperty", typing.Dict[builtins.str, typing.Any]]],
            destination_configurations: typing.Union[_IResolvable_da3f097b, typing.Union["CfnExport.DestinationConfigurationsProperty", typing.Dict[builtins.str, typing.Any]]],
            name: builtins.str,
            refresh_cadence: typing.Union[_IResolvable_da3f097b, typing.Union["CfnExport.RefreshCadenceProperty", typing.Dict[builtins.str, typing.Any]]],
            description: typing.Optional[builtins.str] = None,
            export_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The details that are available for an export.

            :param data_query: The data query for this specific data export.
            :param destination_configurations: The destination configuration for this specific data export.
            :param name: The name of this specific data export.
            :param refresh_cadence: The cadence for AWS to update the export in your S3 bucket.
            :param description: The description for this specific data export.
            :param export_arn: The Amazon Resource Name (ARN) for this export.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bcmdataexports-export-export.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bcmdataexports as bcmdataexports
                
                export_property = bcmdataexports.CfnExport.ExportProperty(
                    data_query=bcmdataexports.CfnExport.DataQueryProperty(
                        query_statement="queryStatement",
                
                        # the properties below are optional
                        table_configurations={
                            "table_configurations_key": {
                                "table_configurations_key": "tableConfigurations"
                            }
                        }
                    ),
                    destination_configurations=bcmdataexports.CfnExport.DestinationConfigurationsProperty(
                        s3_destination=bcmdataexports.CfnExport.S3DestinationProperty(
                            s3_bucket="s3Bucket",
                            s3_output_configurations=bcmdataexports.CfnExport.S3OutputConfigurationsProperty(
                                compression="compression",
                                format="format",
                                output_type="outputType",
                                overwrite="overwrite"
                            ),
                            s3_prefix="s3Prefix",
                            s3_region="s3Region"
                        )
                    ),
                    name="name",
                    refresh_cadence=bcmdataexports.CfnExport.RefreshCadenceProperty(
                        frequency="frequency"
                    ),
                
                    # the properties below are optional
                    description="description",
                    export_arn="exportArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5ed33f32923574fd9894f86effec26df25a5ff6f04eb0b09765445083fe0aeb8)
                check_type(argname="argument data_query", value=data_query, expected_type=type_hints["data_query"])
                check_type(argname="argument destination_configurations", value=destination_configurations, expected_type=type_hints["destination_configurations"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument refresh_cadence", value=refresh_cadence, expected_type=type_hints["refresh_cadence"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument export_arn", value=export_arn, expected_type=type_hints["export_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "data_query": data_query,
                "destination_configurations": destination_configurations,
                "name": name,
                "refresh_cadence": refresh_cadence,
            }
            if description is not None:
                self._values["description"] = description
            if export_arn is not None:
                self._values["export_arn"] = export_arn

        @builtins.property
        def data_query(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnExport.DataQueryProperty"]:
            '''The data query for this specific data export.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bcmdataexports-export-export.html#cfn-bcmdataexports-export-export-dataquery
            '''
            result = self._values.get("data_query")
            assert result is not None, "Required property 'data_query' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnExport.DataQueryProperty"], result)

        @builtins.property
        def destination_configurations(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnExport.DestinationConfigurationsProperty"]:
            '''The destination configuration for this specific data export.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bcmdataexports-export-export.html#cfn-bcmdataexports-export-export-destinationconfigurations
            '''
            result = self._values.get("destination_configurations")
            assert result is not None, "Required property 'destination_configurations' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnExport.DestinationConfigurationsProperty"], result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of this specific data export.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bcmdataexports-export-export.html#cfn-bcmdataexports-export-export-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def refresh_cadence(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnExport.RefreshCadenceProperty"]:
            '''The cadence for AWS to update the export in your S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bcmdataexports-export-export.html#cfn-bcmdataexports-export-export-refreshcadence
            '''
            result = self._values.get("refresh_cadence")
            assert result is not None, "Required property 'refresh_cadence' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnExport.RefreshCadenceProperty"], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The description for this specific data export.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bcmdataexports-export-export.html#cfn-bcmdataexports-export-export-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def export_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) for this export.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bcmdataexports-export-export.html#cfn-bcmdataexports-export-export-exportarn
            '''
            result = self._values.get("export_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExportProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bcmdataexports.CfnExport.RefreshCadenceProperty",
        jsii_struct_bases=[],
        name_mapping={"frequency": "frequency"},
    )
    class RefreshCadenceProperty:
        def __init__(self, *, frequency: builtins.str) -> None:
            '''The cadence for AWS to update the data export in your S3 bucket.

            :param frequency: The frequency that data exports are updated. The export refreshes each time the source data updates, up to three times daily.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bcmdataexports-export-refreshcadence.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bcmdataexports as bcmdataexports
                
                refresh_cadence_property = bcmdataexports.CfnExport.RefreshCadenceProperty(
                    frequency="frequency"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__51077f124ab3cd094da6dc910a65ab487514933f628cb750035c7e99cb5124a5)
                check_type(argname="argument frequency", value=frequency, expected_type=type_hints["frequency"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "frequency": frequency,
            }

        @builtins.property
        def frequency(self) -> builtins.str:
            '''The frequency that data exports are updated.

            The export refreshes each time the source data updates, up to three times daily.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bcmdataexports-export-refreshcadence.html#cfn-bcmdataexports-export-refreshcadence-frequency
            '''
            result = self._values.get("frequency")
            assert result is not None, "Required property 'frequency' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RefreshCadenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bcmdataexports.CfnExport.ResourceTagProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class ResourceTagProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''The tag structure that contains a tag key and value.

            :param key: The key that's associated with the tag.
            :param value: The value that's associated with the tag.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bcmdataexports-export-resourcetag.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bcmdataexports as bcmdataexports
                
                resource_tag_property = bcmdataexports.CfnExport.ResourceTagProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a77a31fde973f8e19f271b0c7493a0a5358853ae60f917aa6cc52d91aef79534)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The key that's associated with the tag.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bcmdataexports-export-resourcetag.html#cfn-bcmdataexports-export-resourcetag-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value that's associated with the tag.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bcmdataexports-export-resourcetag.html#cfn-bcmdataexports-export-resourcetag-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceTagProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bcmdataexports.CfnExport.S3DestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "s3_bucket": "s3Bucket",
            "s3_output_configurations": "s3OutputConfigurations",
            "s3_prefix": "s3Prefix",
            "s3_region": "s3Region",
        },
    )
    class S3DestinationProperty:
        def __init__(
            self,
            *,
            s3_bucket: builtins.str,
            s3_output_configurations: typing.Union[_IResolvable_da3f097b, typing.Union["CfnExport.S3OutputConfigurationsProperty", typing.Dict[builtins.str, typing.Any]]],
            s3_prefix: builtins.str,
            s3_region: builtins.str,
        ) -> None:
            '''Describes the destination Amazon Simple Storage Service (Amazon S3) bucket name and object keys of a data exports file.

            :param s3_bucket: The name of the Amazon S3 bucket used as the destination of a data export file.
            :param s3_output_configurations: The output configuration for the data export.
            :param s3_prefix: The S3 path prefix you want prepended to the name of your data export.
            :param s3_region: The S3 bucket Region.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bcmdataexports-export-s3destination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bcmdataexports as bcmdataexports
                
                s3_destination_property = bcmdataexports.CfnExport.S3DestinationProperty(
                    s3_bucket="s3Bucket",
                    s3_output_configurations=bcmdataexports.CfnExport.S3OutputConfigurationsProperty(
                        compression="compression",
                        format="format",
                        output_type="outputType",
                        overwrite="overwrite"
                    ),
                    s3_prefix="s3Prefix",
                    s3_region="s3Region"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f0e9ff7de57059ed083f4105af6db04a1e6eed259177bb46ecb6f3d066089e70)
                check_type(argname="argument s3_bucket", value=s3_bucket, expected_type=type_hints["s3_bucket"])
                check_type(argname="argument s3_output_configurations", value=s3_output_configurations, expected_type=type_hints["s3_output_configurations"])
                check_type(argname="argument s3_prefix", value=s3_prefix, expected_type=type_hints["s3_prefix"])
                check_type(argname="argument s3_region", value=s3_region, expected_type=type_hints["s3_region"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "s3_bucket": s3_bucket,
                "s3_output_configurations": s3_output_configurations,
                "s3_prefix": s3_prefix,
                "s3_region": s3_region,
            }

        @builtins.property
        def s3_bucket(self) -> builtins.str:
            '''The name of the Amazon S3 bucket used as the destination of a data export file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bcmdataexports-export-s3destination.html#cfn-bcmdataexports-export-s3destination-s3bucket
            '''
            result = self._values.get("s3_bucket")
            assert result is not None, "Required property 's3_bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_output_configurations(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnExport.S3OutputConfigurationsProperty"]:
            '''The output configuration for the data export.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bcmdataexports-export-s3destination.html#cfn-bcmdataexports-export-s3destination-s3outputconfigurations
            '''
            result = self._values.get("s3_output_configurations")
            assert result is not None, "Required property 's3_output_configurations' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnExport.S3OutputConfigurationsProperty"], result)

        @builtins.property
        def s3_prefix(self) -> builtins.str:
            '''The S3 path prefix you want prepended to the name of your data export.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bcmdataexports-export-s3destination.html#cfn-bcmdataexports-export-s3destination-s3prefix
            '''
            result = self._values.get("s3_prefix")
            assert result is not None, "Required property 's3_prefix' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_region(self) -> builtins.str:
            '''The S3 bucket Region.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bcmdataexports-export-s3destination.html#cfn-bcmdataexports-export-s3destination-s3region
            '''
            result = self._values.get("s3_region")
            assert result is not None, "Required property 's3_region' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3DestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bcmdataexports.CfnExport.S3OutputConfigurationsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "compression": "compression",
            "format": "format",
            "output_type": "outputType",
            "overwrite": "overwrite",
        },
    )
    class S3OutputConfigurationsProperty:
        def __init__(
            self,
            *,
            compression: builtins.str,
            format: builtins.str,
            output_type: builtins.str,
            overwrite: builtins.str,
        ) -> None:
            '''The compression type, file format, and overwrite preference for the data export.

            :param compression: The compression type for the data export.
            :param format: The file format for the data export.
            :param output_type: The output type for the data export.
            :param overwrite: The rule to follow when generating a version of the data export file. You have the choice to overwrite the previous version or to be delivered in addition to the previous versions. Overwriting exports can save on Amazon S3 storage costs. Creating new export versions allows you to track the changes in cost and usage data over time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bcmdataexports-export-s3outputconfigurations.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bcmdataexports as bcmdataexports
                
                s3_output_configurations_property = bcmdataexports.CfnExport.S3OutputConfigurationsProperty(
                    compression="compression",
                    format="format",
                    output_type="outputType",
                    overwrite="overwrite"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__921d4e97c7f0398e33206f9dc2808c5bbe6f9ab0df93b16ab6e4b33159e538e0)
                check_type(argname="argument compression", value=compression, expected_type=type_hints["compression"])
                check_type(argname="argument format", value=format, expected_type=type_hints["format"])
                check_type(argname="argument output_type", value=output_type, expected_type=type_hints["output_type"])
                check_type(argname="argument overwrite", value=overwrite, expected_type=type_hints["overwrite"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "compression": compression,
                "format": format,
                "output_type": output_type,
                "overwrite": overwrite,
            }

        @builtins.property
        def compression(self) -> builtins.str:
            '''The compression type for the data export.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bcmdataexports-export-s3outputconfigurations.html#cfn-bcmdataexports-export-s3outputconfigurations-compression
            '''
            result = self._values.get("compression")
            assert result is not None, "Required property 'compression' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def format(self) -> builtins.str:
            '''The file format for the data export.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bcmdataexports-export-s3outputconfigurations.html#cfn-bcmdataexports-export-s3outputconfigurations-format
            '''
            result = self._values.get("format")
            assert result is not None, "Required property 'format' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def output_type(self) -> builtins.str:
            '''The output type for the data export.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bcmdataexports-export-s3outputconfigurations.html#cfn-bcmdataexports-export-s3outputconfigurations-outputtype
            '''
            result = self._values.get("output_type")
            assert result is not None, "Required property 'output_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def overwrite(self) -> builtins.str:
            '''The rule to follow when generating a version of the data export file.

            You have the choice to overwrite the previous version or to be delivered in addition to the previous versions. Overwriting exports can save on Amazon S3 storage costs. Creating new export versions allows you to track the changes in cost and usage data over time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bcmdataexports-export-s3outputconfigurations.html#cfn-bcmdataexports-export-s3outputconfigurations-overwrite
            '''
            result = self._values.get("overwrite")
            assert result is not None, "Required property 'overwrite' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3OutputConfigurationsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bcmdataexports.CfnExportProps",
    jsii_struct_bases=[],
    name_mapping={"export": "export", "tags": "tags"},
)
class CfnExportProps:
    def __init__(
        self,
        *,
        export: typing.Union[_IResolvable_da3f097b, typing.Union[CfnExport.ExportProperty, typing.Dict[builtins.str, typing.Any]]],
        tags: typing.Optional[typing.Sequence[typing.Union[CfnExport.ResourceTagProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnExport``.

        :param export: The details that are available for an export.
        :param tags: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bcmdataexports-export.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bcmdataexports as bcmdataexports
            
            cfn_export_props = bcmdataexports.CfnExportProps(
                export=bcmdataexports.CfnExport.ExportProperty(
                    data_query=bcmdataexports.CfnExport.DataQueryProperty(
                        query_statement="queryStatement",
            
                        # the properties below are optional
                        table_configurations={
                            "table_configurations_key": {
                                "table_configurations_key": "tableConfigurations"
                            }
                        }
                    ),
                    destination_configurations=bcmdataexports.CfnExport.DestinationConfigurationsProperty(
                        s3_destination=bcmdataexports.CfnExport.S3DestinationProperty(
                            s3_bucket="s3Bucket",
                            s3_output_configurations=bcmdataexports.CfnExport.S3OutputConfigurationsProperty(
                                compression="compression",
                                format="format",
                                output_type="outputType",
                                overwrite="overwrite"
                            ),
                            s3_prefix="s3Prefix",
                            s3_region="s3Region"
                        )
                    ),
                    name="name",
                    refresh_cadence=bcmdataexports.CfnExport.RefreshCadenceProperty(
                        frequency="frequency"
                    ),
            
                    # the properties below are optional
                    description="description",
                    export_arn="exportArn"
                ),
            
                # the properties below are optional
                tags=[bcmdataexports.CfnExport.ResourceTagProperty(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f07a9b27578e3470b9f0c00c3d616068c70c252cc5f2b23f3ae0e27d9b81b31)
            check_type(argname="argument export", value=export, expected_type=type_hints["export"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "export": export,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def export(self) -> typing.Union[_IResolvable_da3f097b, CfnExport.ExportProperty]:
        '''The details that are available for an export.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bcmdataexports-export.html#cfn-bcmdataexports-export-export
        '''
        result = self._values.get("export")
        assert result is not None, "Required property 'export' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnExport.ExportProperty], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[CfnExport.ResourceTagProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bcmdataexports-export.html#cfn-bcmdataexports-export-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[CfnExport.ResourceTagProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExportProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnExport",
    "CfnExportProps",
]

publication.publish()

def _typecheckingstub__b2bcca1af59fac907ca8714563d055c566e701daae8450fde60df7c0e3d3db64(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    export: typing.Union[_IResolvable_da3f097b, typing.Union[CfnExport.ExportProperty, typing.Dict[builtins.str, typing.Any]]],
    tags: typing.Optional[typing.Sequence[typing.Union[CfnExport.ResourceTagProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dac39dc3be3191a8c16e738400531fa018e236e77c82fbfaa9dc5f869f22217(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb93537976d222e41558fc4b0c82267089734f222dad1d93d6bf9ac01baf7235(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8ce26f4856f4fbb56e9f2fa30a5520af71bb0fab07aab599f3d350bcd7af208(
    value: typing.Union[_IResolvable_da3f097b, CfnExport.ExportProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ad623342e4c1e6ad8d0a1e800f480ca841fcc2866deb4be0a499fc18bffc658(
    value: typing.Optional[typing.List[CfnExport.ResourceTagProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1a095753612659582b4b6117f8c7de657221f82c66d4926cce19af238d91343(
    *,
    query_statement: builtins.str,
    table_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__816060235493801ab48e2f3ab492e0786d6ff854a29cb93dcb295018d334cec5(
    *,
    s3_destination: typing.Union[_IResolvable_da3f097b, typing.Union[CfnExport.S3DestinationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ed33f32923574fd9894f86effec26df25a5ff6f04eb0b09765445083fe0aeb8(
    *,
    data_query: typing.Union[_IResolvable_da3f097b, typing.Union[CfnExport.DataQueryProperty, typing.Dict[builtins.str, typing.Any]]],
    destination_configurations: typing.Union[_IResolvable_da3f097b, typing.Union[CfnExport.DestinationConfigurationsProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    refresh_cadence: typing.Union[_IResolvable_da3f097b, typing.Union[CfnExport.RefreshCadenceProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    export_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51077f124ab3cd094da6dc910a65ab487514933f628cb750035c7e99cb5124a5(
    *,
    frequency: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a77a31fde973f8e19f271b0c7493a0a5358853ae60f917aa6cc52d91aef79534(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0e9ff7de57059ed083f4105af6db04a1e6eed259177bb46ecb6f3d066089e70(
    *,
    s3_bucket: builtins.str,
    s3_output_configurations: typing.Union[_IResolvable_da3f097b, typing.Union[CfnExport.S3OutputConfigurationsProperty, typing.Dict[builtins.str, typing.Any]]],
    s3_prefix: builtins.str,
    s3_region: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__921d4e97c7f0398e33206f9dc2808c5bbe6f9ab0df93b16ab6e4b33159e538e0(
    *,
    compression: builtins.str,
    format: builtins.str,
    output_type: builtins.str,
    overwrite: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f07a9b27578e3470b9f0c00c3d616068c70c252cc5f2b23f3ae0e27d9b81b31(
    *,
    export: typing.Union[_IResolvable_da3f097b, typing.Union[CfnExport.ExportProperty, typing.Dict[builtins.str, typing.Any]]],
    tags: typing.Optional[typing.Sequence[typing.Union[CfnExport.ResourceTagProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
