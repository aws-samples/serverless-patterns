'''
# AWS::LakeFormation Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_lakeformation as lakeformation
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for LakeFormation construct libraries](https://constructs.dev/search?q=lakeformation)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::LakeFormation resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_LakeFormation.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::LakeFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_LakeFormation.html).

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
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnDataCellsFilter(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lakeformation.CfnDataCellsFilter",
):
    '''A structure that represents a data cell filter with column-level, row-level, and/or cell-level security.

    Data cell filters belong to a specific table in a Data Catalog . During a stack operation, AWS CloudFormation calls the AWS Lake Formation ``CreateDataCellsFilter`` API operation to create a ``DataCellsFilter`` resource, and calls the ``DeleteDataCellsFilter`` API operation to delete it.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lakeformation as lakeformation
        
        # all_rows_wildcard: Any
        
        cfn_data_cells_filter = lakeformation.CfnDataCellsFilter(self, "MyCfnDataCellsFilter",
            database_name="databaseName",
            name="name",
            table_catalog_id="tableCatalogId",
            table_name="tableName",
        
            # the properties below are optional
            column_names=["columnNames"],
            column_wildcard=lakeformation.CfnDataCellsFilter.ColumnWildcardProperty(
                excluded_column_names=["excludedColumnNames"]
            ),
            row_filter=lakeformation.CfnDataCellsFilter.RowFilterProperty(
                all_rows_wildcard=all_rows_wildcard,
                filter_expression="filterExpression"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        database_name: builtins.str,
        name: builtins.str,
        table_catalog_id: builtins.str,
        table_name: builtins.str,
        column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        column_wildcard: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataCellsFilter.ColumnWildcardProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        row_filter: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataCellsFilter.RowFilterProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param database_name: UTF-8 string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html>`_ . A database in the Data Catalog .
        :param name: UTF-8 string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html>`_ . The name given by the user to the data filter cell.
        :param table_catalog_id: Catalog id string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html>`_ . The ID of the catalog to which the table belongs.
        :param table_name: UTF-8 string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html>`_ . A table in the database.
        :param column_names: An array of UTF-8 strings. A list of column names.
        :param column_wildcard: A wildcard with exclusions. You must specify either a ``ColumnNames`` list or the ``ColumnWildCard`` .
        :param row_filter: A PartiQL predicate.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a9e0f2e2c8572da6300632b42930370bb203310961a1d82af3036a8c04fd788)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDataCellsFilterProps(
            database_name=database_name,
            name=name,
            table_catalog_id=table_catalog_id,
            table_name=table_name,
            column_names=column_names,
            column_wildcard=column_wildcard,
            row_filter=row_filter,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ec2c4ae3e05879746cc41d6b7ec6a03ba20902ffc48bd129aa397d1d5a70e7e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a7550823f808ffe201e6847b495d6892ddb995ec5519cee9493e2f6a540da733)
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
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        '''UTF-8 string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html>`_ .'''
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc93dcc91058f9885e949d095cb9cbd4ebbf83657aef2c98bdbd7642aa2b641f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''UTF-8 string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html>`_ .'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48e194f3f5e117b948f5fd8f39a3c23624f934ba178488c21dcbeb47739eb3d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tableCatalogId")
    def table_catalog_id(self) -> builtins.str:
        '''Catalog id string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html>`_ .'''
        return typing.cast(builtins.str, jsii.get(self, "tableCatalogId"))

    @table_catalog_id.setter
    def table_catalog_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a2c891466da3cee74414ca67472fd45c6fe92a42dbf54f91e90276b9db4a09d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableCatalogId", value)

    @builtins.property
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> builtins.str:
        '''UTF-8 string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html>`_ .'''
        return typing.cast(builtins.str, jsii.get(self, "tableName"))

    @table_name.setter
    def table_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b9edb03eab58adb69826ccb4eeac83e17f956f28af214b840626176e3b23986)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableName", value)

    @builtins.property
    @jsii.member(jsii_name="columnNames")
    def column_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of UTF-8 strings.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "columnNames"))

    @column_names.setter
    def column_names(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e63b539b5926a43d01e515712efb604ac6b3d1ede325bc1b9c5dffd65f6b333c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "columnNames", value)

    @builtins.property
    @jsii.member(jsii_name="columnWildcard")
    def column_wildcard(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataCellsFilter.ColumnWildcardProperty"]]:
        '''A wildcard with exclusions.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataCellsFilter.ColumnWildcardProperty"]], jsii.get(self, "columnWildcard"))

    @column_wildcard.setter
    def column_wildcard(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataCellsFilter.ColumnWildcardProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24e7504a12b1b5d7e26809268009dbec0ff8e5b821de877742f07891ecfccf10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "columnWildcard", value)

    @builtins.property
    @jsii.member(jsii_name="rowFilter")
    def row_filter(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataCellsFilter.RowFilterProperty"]]:
        '''A PartiQL predicate.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataCellsFilter.RowFilterProperty"]], jsii.get(self, "rowFilter"))

    @row_filter.setter
    def row_filter(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataCellsFilter.RowFilterProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9f504934d13512b5f3bc876387b568ad7594bcf89c9905c5e36a7ab25137e38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rowFilter", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnDataCellsFilter.ColumnWildcardProperty",
        jsii_struct_bases=[],
        name_mapping={"excluded_column_names": "excludedColumnNames"},
    )
    class ColumnWildcardProperty:
        def __init__(
            self,
            *,
            excluded_column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''A wildcard object, consisting of an optional list of excluded column names or indexes.

            :param excluded_column_names: Excludes column names. Any column with this name will be excluded.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datacellsfilter-columnwildcard.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                column_wildcard_property = lakeformation.CfnDataCellsFilter.ColumnWildcardProperty(
                    excluded_column_names=["excludedColumnNames"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d84dab12def7ab74d756b3488b56485fbe9e3c5d2293a55ee2317a32e970e93a)
                check_type(argname="argument excluded_column_names", value=excluded_column_names, expected_type=type_hints["excluded_column_names"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if excluded_column_names is not None:
                self._values["excluded_column_names"] = excluded_column_names

        @builtins.property
        def excluded_column_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Excludes column names.

            Any column with this name will be excluded.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datacellsfilter-columnwildcard.html#cfn-lakeformation-datacellsfilter-columnwildcard-excludedcolumnnames
            '''
            result = self._values.get("excluded_column_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ColumnWildcardProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnDataCellsFilter.RowFilterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "all_rows_wildcard": "allRowsWildcard",
            "filter_expression": "filterExpression",
        },
    )
    class RowFilterProperty:
        def __init__(
            self,
            *,
            all_rows_wildcard: typing.Any = None,
            filter_expression: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A PartiQL predicate.

            :param all_rows_wildcard: A wildcard for all rows.
            :param filter_expression: A filter expression.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datacellsfilter-rowfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                # all_rows_wildcard: Any
                
                row_filter_property = lakeformation.CfnDataCellsFilter.RowFilterProperty(
                    all_rows_wildcard=all_rows_wildcard,
                    filter_expression="filterExpression"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e7b949fde25ae1b3b377b26570479963a5dec16b47fe2674ce47b5ea088af049)
                check_type(argname="argument all_rows_wildcard", value=all_rows_wildcard, expected_type=type_hints["all_rows_wildcard"])
                check_type(argname="argument filter_expression", value=filter_expression, expected_type=type_hints["filter_expression"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if all_rows_wildcard is not None:
                self._values["all_rows_wildcard"] = all_rows_wildcard
            if filter_expression is not None:
                self._values["filter_expression"] = filter_expression

        @builtins.property
        def all_rows_wildcard(self) -> typing.Any:
            '''A wildcard for all rows.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datacellsfilter-rowfilter.html#cfn-lakeformation-datacellsfilter-rowfilter-allrowswildcard
            '''
            result = self._values.get("all_rows_wildcard")
            return typing.cast(typing.Any, result)

        @builtins.property
        def filter_expression(self) -> typing.Optional[builtins.str]:
            '''A filter expression.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datacellsfilter-rowfilter.html#cfn-lakeformation-datacellsfilter-rowfilter-filterexpression
            '''
            result = self._values.get("filter_expression")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RowFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lakeformation.CfnDataCellsFilterProps",
    jsii_struct_bases=[],
    name_mapping={
        "database_name": "databaseName",
        "name": "name",
        "table_catalog_id": "tableCatalogId",
        "table_name": "tableName",
        "column_names": "columnNames",
        "column_wildcard": "columnWildcard",
        "row_filter": "rowFilter",
    },
)
class CfnDataCellsFilterProps:
    def __init__(
        self,
        *,
        database_name: builtins.str,
        name: builtins.str,
        table_catalog_id: builtins.str,
        table_name: builtins.str,
        column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        column_wildcard: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataCellsFilter.ColumnWildcardProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        row_filter: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataCellsFilter.RowFilterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDataCellsFilter``.

        :param database_name: UTF-8 string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html>`_ . A database in the Data Catalog .
        :param name: UTF-8 string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html>`_ . The name given by the user to the data filter cell.
        :param table_catalog_id: Catalog id string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html>`_ . The ID of the catalog to which the table belongs.
        :param table_name: UTF-8 string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html>`_ . A table in the database.
        :param column_names: An array of UTF-8 strings. A list of column names.
        :param column_wildcard: A wildcard with exclusions. You must specify either a ``ColumnNames`` list or the ``ColumnWildCard`` .
        :param row_filter: A PartiQL predicate.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lakeformation as lakeformation
            
            # all_rows_wildcard: Any
            
            cfn_data_cells_filter_props = lakeformation.CfnDataCellsFilterProps(
                database_name="databaseName",
                name="name",
                table_catalog_id="tableCatalogId",
                table_name="tableName",
            
                # the properties below are optional
                column_names=["columnNames"],
                column_wildcard=lakeformation.CfnDataCellsFilter.ColumnWildcardProperty(
                    excluded_column_names=["excludedColumnNames"]
                ),
                row_filter=lakeformation.CfnDataCellsFilter.RowFilterProperty(
                    all_rows_wildcard=all_rows_wildcard,
                    filter_expression="filterExpression"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a431cb2c88a63c9acd6913435bb5a3f7e689fea9c26e811a77582b6774fc6a8)
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument table_catalog_id", value=table_catalog_id, expected_type=type_hints["table_catalog_id"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            check_type(argname="argument column_names", value=column_names, expected_type=type_hints["column_names"])
            check_type(argname="argument column_wildcard", value=column_wildcard, expected_type=type_hints["column_wildcard"])
            check_type(argname="argument row_filter", value=row_filter, expected_type=type_hints["row_filter"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database_name": database_name,
            "name": name,
            "table_catalog_id": table_catalog_id,
            "table_name": table_name,
        }
        if column_names is not None:
            self._values["column_names"] = column_names
        if column_wildcard is not None:
            self._values["column_wildcard"] = column_wildcard
        if row_filter is not None:
            self._values["row_filter"] = row_filter

    @builtins.property
    def database_name(self) -> builtins.str:
        '''UTF-8 string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html>`_ .

        A database in the Data Catalog .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-databasename
        '''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''UTF-8 string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html>`_ .

        The name given by the user to the data filter cell.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_catalog_id(self) -> builtins.str:
        '''Catalog id string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html>`_ .

        The ID of the catalog to which the table belongs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-tablecatalogid
        '''
        result = self._values.get("table_catalog_id")
        assert result is not None, "Required property 'table_catalog_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_name(self) -> builtins.str:
        '''UTF-8 string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html>`_ .

        A table in the database.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-tablename
        '''
        result = self._values.get("table_name")
        assert result is not None, "Required property 'table_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def column_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of UTF-8 strings.

        A list of column names.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-columnnames
        '''
        result = self._values.get("column_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def column_wildcard(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataCellsFilter.ColumnWildcardProperty]]:
        '''A wildcard with exclusions.

        You must specify either a ``ColumnNames`` list or the ``ColumnWildCard`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-columnwildcard
        '''
        result = self._values.get("column_wildcard")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataCellsFilter.ColumnWildcardProperty]], result)

    @builtins.property
    def row_filter(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataCellsFilter.RowFilterProperty]]:
        '''A PartiQL predicate.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html#cfn-lakeformation-datacellsfilter-rowfilter
        '''
        result = self._values.get("row_filter")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataCellsFilter.RowFilterProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataCellsFilterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnDataLakeSettings(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lakeformation.CfnDataLakeSettings",
):
    '''The ``AWS::LakeFormation::DataLakeSettings`` resource is an AWS Lake Formation resource type that manages the data lake settings for your account.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lakeformation as lakeformation
        
        # parameters: Any
        
        cfn_data_lake_settings = lakeformation.CfnDataLakeSettings(self, "MyCfnDataLakeSettings",
            admins=[lakeformation.CfnDataLakeSettings.DataLakePrincipalProperty(
                data_lake_principal_identifier="dataLakePrincipalIdentifier"
            )],
            allow_external_data_filtering=False,
            authorized_session_tag_value_list=["authorizedSessionTagValueList"],
            create_database_default_permissions=[lakeformation.CfnDataLakeSettings.PrincipalPermissionsProperty(
                permissions=["permissions"],
                principal=lakeformation.CfnDataLakeSettings.DataLakePrincipalProperty(
                    data_lake_principal_identifier="dataLakePrincipalIdentifier"
                )
            )],
            create_table_default_permissions=[lakeformation.CfnDataLakeSettings.PrincipalPermissionsProperty(
                permissions=["permissions"],
                principal=lakeformation.CfnDataLakeSettings.DataLakePrincipalProperty(
                    data_lake_principal_identifier="dataLakePrincipalIdentifier"
                )
            )],
            external_data_filtering_allow_list=[lakeformation.CfnDataLakeSettings.DataLakePrincipalProperty(
                data_lake_principal_identifier="dataLakePrincipalIdentifier"
            )],
            parameters=parameters,
            trusted_resource_owners=["trustedResourceOwners"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        admins: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataLakeSettings.DataLakePrincipalProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        allow_external_data_filtering: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        authorized_session_tag_value_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        create_database_default_permissions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataLakeSettings.PrincipalPermissionsProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        create_table_default_permissions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataLakeSettings.PrincipalPermissionsProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        external_data_filtering_allow_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataLakeSettings.DataLakePrincipalProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        parameters: typing.Any = None,
        trusted_resource_owners: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param admins: A list of AWS Lake Formation principals.
        :param allow_external_data_filtering: Whether to allow Amazon EMR clusters or other third-party query engines to access data managed by Lake Formation . If set to true, you allow Amazon EMR clusters or other third-party engines to access data in Amazon S3 locations that are registered with Lake Formation . If false or null, no third-party query engines will be able to access data in Amazon S3 locations that are registered with Lake Formation. For more information, see `External data filtering setting <https://docs.aws.amazon.com/lake-formation/latest/dg/initial-LF-setup.html#external-data-filter>`_ .
        :param authorized_session_tag_value_list: Lake Formation relies on a privileged process secured by Amazon EMR or the third party integrator to tag the user's role while assuming it. Lake Formation will publish the acceptable key-value pair, for example key = "LakeFormationTrustedCaller" and value = "TRUE" and the third party integrator must properly tag the temporary security credentials that will be used to call Lake Formation 's administrative API operations.
        :param create_database_default_permissions: Specifies whether access control on a newly created database is managed by Lake Formation permissions or exclusively by IAM permissions. A null value indicates that the access is controlled by Lake Formation permissions. ``ALL`` permissions assigned to ``IAM_ALLOWED_PRINCIPALS`` group indicates that the user's IAM permissions determine the access to the database. This is referred to as the setting "Use only IAM access control," and is to support backward compatibility with the AWS Glue permission model implemented by IAM permissions. The only permitted values are an empty array or an array that contains a single JSON object that grants ``ALL`` to ``IAM_ALLOWED_PRINCIPALS`` . For more information, see `Changing the default security settings for your data lake <https://docs.aws.amazon.com/lake-formation/latest/dg/change-settings.html>`_ .
        :param create_table_default_permissions: Specifies whether access control on a newly created table is managed by Lake Formation permissions or exclusively by IAM permissions. A null value indicates that the access is controlled by Lake Formation permissions. ``ALL`` permissions assigned to ``IAM_ALLOWED_PRINCIPALS`` group indicate that the user's IAM permissions determine the access to the table. This is referred to as the setting "Use only IAM access control," and is to support the backward compatibility with the AWS Glue permission model implemented by IAM permissions. The only permitted values are an empty array or an array that contains a single JSON object that grants ``ALL`` permissions to ``IAM_ALLOWED_PRINCIPALS`` . For more information, see `Changing the default security settings for your data lake <https://docs.aws.amazon.com/lake-formation/latest/dg/change-settings.html>`_ .
        :param external_data_filtering_allow_list: A list of the account IDs of AWS accounts with Amazon EMR clusters or third-party engines that are allwed to perform data filtering.
        :param parameters: A key-value map that provides an additional configuration on your data lake. ``CrossAccountVersion`` is the key you can configure in the ``Parameters`` field. Accepted values for the ``CrossAccountVersion`` key are 1, 2, and 3.
        :param trusted_resource_owners: An array of UTF-8 strings. A list of the resource-owning account IDs that the caller's account can use to share their user access details (user ARNs). The user ARNs can be logged in the resource owner's CloudTrail log. You may want to specify this property when you are in a high-trust boundary, such as the same team or company.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f70f29826d8a7fc5611588cb6eeb3680ada51f8de62dc227827dff9f54d92319)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDataLakeSettingsProps(
            admins=admins,
            allow_external_data_filtering=allow_external_data_filtering,
            authorized_session_tag_value_list=authorized_session_tag_value_list,
            create_database_default_permissions=create_database_default_permissions,
            create_table_default_permissions=create_table_default_permissions,
            external_data_filtering_allow_list=external_data_filtering_allow_list,
            parameters=parameters,
            trusted_resource_owners=trusted_resource_owners,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45022e2f75497dc5031de0534471b774f37d3e0163dd1cf0944a879956918611)
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
            type_hints = typing.get_type_hints(_typecheckingstub__638c6babf62b74da5a2cf7141e8d1f010dd75138406d16700684bff77834fdb5)
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
    @jsii.member(jsii_name="admins")
    def admins(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataLakeSettings.DataLakePrincipalProperty"]]]]:
        '''A list of AWS Lake Formation principals.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataLakeSettings.DataLakePrincipalProperty"]]]], jsii.get(self, "admins"))

    @admins.setter
    def admins(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataLakeSettings.DataLakePrincipalProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df68ab1ab5b6831a2e0f48c47e111909fcae53ceb431cf9876b2a6b3ee4895a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "admins", value)

    @builtins.property
    @jsii.member(jsii_name="allowExternalDataFiltering")
    def allow_external_data_filtering(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to allow Amazon EMR clusters or other third-party query engines to access data managed by Lake Formation .'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "allowExternalDataFiltering"))

    @allow_external_data_filtering.setter
    def allow_external_data_filtering(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad4d063925881a74c4f1073af94f569441bb4b8f7c58ee42383196bbb4e64aad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowExternalDataFiltering", value)

    @builtins.property
    @jsii.member(jsii_name="authorizedSessionTagValueList")
    def authorized_session_tag_value_list(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Lake Formation relies on a privileged process secured by Amazon EMR or the third party integrator to tag the user's role while assuming it.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "authorizedSessionTagValueList"))

    @authorized_session_tag_value_list.setter
    def authorized_session_tag_value_list(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd0547c17046b539f4cc757ea06d70b24e27b41611578b3219bd0ca23fe6ecd0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizedSessionTagValueList", value)

    @builtins.property
    @jsii.member(jsii_name="createDatabaseDefaultPermissions")
    def create_database_default_permissions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataLakeSettings.PrincipalPermissionsProperty"]]]]:
        '''Specifies whether access control on a newly created database is managed by Lake Formation permissions or exclusively by IAM permissions.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataLakeSettings.PrincipalPermissionsProperty"]]]], jsii.get(self, "createDatabaseDefaultPermissions"))

    @create_database_default_permissions.setter
    def create_database_default_permissions(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataLakeSettings.PrincipalPermissionsProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__436b96d2708f96f391be82ba6eaa6481bbecd3b17c06354069035866187d1b45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createDatabaseDefaultPermissions", value)

    @builtins.property
    @jsii.member(jsii_name="createTableDefaultPermissions")
    def create_table_default_permissions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataLakeSettings.PrincipalPermissionsProperty"]]]]:
        '''Specifies whether access control on a newly created table is managed by Lake Formation permissions or exclusively by IAM permissions.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataLakeSettings.PrincipalPermissionsProperty"]]]], jsii.get(self, "createTableDefaultPermissions"))

    @create_table_default_permissions.setter
    def create_table_default_permissions(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataLakeSettings.PrincipalPermissionsProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60f9c70a917c1c3ef84f9fe5f53041f2cdd59022a7255ab1c017bbfc4891f92f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createTableDefaultPermissions", value)

    @builtins.property
    @jsii.member(jsii_name="externalDataFilteringAllowList")
    def external_data_filtering_allow_list(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataLakeSettings.DataLakePrincipalProperty"]]]]:
        '''A list of the account IDs of AWS accounts with Amazon EMR clusters or third-party engines that are allwed to perform data filtering.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataLakeSettings.DataLakePrincipalProperty"]]]], jsii.get(self, "externalDataFilteringAllowList"))

    @external_data_filtering_allow_list.setter
    def external_data_filtering_allow_list(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataLakeSettings.DataLakePrincipalProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eeb2f0e282d2dada4492c1a03ccdd85cb8e0865b8f5fc9d4efeee92270845ca4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalDataFilteringAllowList", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Any:
        '''A key-value map that provides an additional configuration on your data lake.'''
        return typing.cast(typing.Any, jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52aab4b55f0c39756a432c91d3eeabd5eb70c011e8f466df712c0d1151418341)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="trustedResourceOwners")
    def trusted_resource_owners(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of UTF-8 strings.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "trustedResourceOwners"))

    @trusted_resource_owners.setter
    def trusted_resource_owners(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__674387b8d4744b1214561eb77053527136809ff4a2e9cd1a69f2ab7af63d2bce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trustedResourceOwners", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnDataLakeSettings.AdminsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class AdminsProperty:
        def __init__(self) -> None:
            '''A list of AWS Lake Formation principals.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datalakesettings-admins.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                admins_property = lakeformation.CfnDataLakeSettings.AdminsProperty()
            '''
            self._values: typing.Dict[builtins.str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AdminsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnDataLakeSettings.CreateDatabaseDefaultPermissionsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class CreateDatabaseDefaultPermissionsProperty:
        def __init__(self) -> None:
            '''Specifies whether access control on a newly created database is managed by Lake Formation permissions or exclusively by IAM permissions.

            A null value indicates that the access is controlled by Lake Formation permissions. A value that assigns ``ALL`` to ``IAM_ALLOWED_PRINCIPALS`` indicates access control by IAM permissions. This is referred to as the setting "Use only IAM access control," and is for backward compatibility with the AWS Glue permission model implemented by IAM permissions.

            The only permitted values are an empty array or an array that contains a single JSON object that grants ``ALL`` to ``IAM_ALLOWED_PRINCIPALS`` .

            For more information, see `Changing the default security settings for your data lake <https://docs.aws.amazon.com/lake-formation/latest/dg/change-settings.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datalakesettings-createdatabasedefaultpermissions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                create_database_default_permissions_property = lakeformation.CfnDataLakeSettings.CreateDatabaseDefaultPermissionsProperty()
            '''
            self._values: typing.Dict[builtins.str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CreateDatabaseDefaultPermissionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnDataLakeSettings.CreateTableDefaultPermissionsProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class CreateTableDefaultPermissionsProperty:
        def __init__(self) -> None:
            '''Specifies whether access control on a newly created table is managed by Lake Formation permissions or exclusively by IAM permissions.

            A null value indicates that the access is controlled by Lake Formation permissions. A value that assigns ``ALL`` to ``IAM_ALLOWED_PRINCIPALS`` indicates access control by IAM permissions. This is referred to as the setting "Use only IAM access control," and is for backward compatibility with the AWS Glue permission model implemented by IAM permissions.

            The only permitted values are an empty array or an array that contains a single JSON object that grants ``ALL`` to ``IAM_ALLOWED_PRINCIPALS`` .

            For more information, see `Changing the Default Security Settings for Your Data Lake <https://docs.aws.amazon.com/lake-formation/latest/dg/change-settings.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datalakesettings-createtabledefaultpermissions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                create_table_default_permissions_property = lakeformation.CfnDataLakeSettings.CreateTableDefaultPermissionsProperty()
            '''
            self._values: typing.Dict[builtins.str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CreateTableDefaultPermissionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnDataLakeSettings.DataLakePrincipalProperty",
        jsii_struct_bases=[],
        name_mapping={"data_lake_principal_identifier": "dataLakePrincipalIdentifier"},
    )
    class DataLakePrincipalProperty:
        def __init__(self, *, data_lake_principal_identifier: builtins.str) -> None:
            '''The Lake Formation principal.

            :param data_lake_principal_identifier: An identifier for the Lake Formation principal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datalakesettings-datalakeprincipal.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                data_lake_principal_property = lakeformation.CfnDataLakeSettings.DataLakePrincipalProperty(
                    data_lake_principal_identifier="dataLakePrincipalIdentifier"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2170e5a67ab80501cee1e7b138e885605f96762aa99d98fe439758c186de8147)
                check_type(argname="argument data_lake_principal_identifier", value=data_lake_principal_identifier, expected_type=type_hints["data_lake_principal_identifier"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "data_lake_principal_identifier": data_lake_principal_identifier,
            }

        @builtins.property
        def data_lake_principal_identifier(self) -> builtins.str:
            '''An identifier for the Lake Formation principal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datalakesettings-datalakeprincipal.html#cfn-lakeformation-datalakesettings-datalakeprincipal-datalakeprincipalidentifier
            '''
            result = self._values.get("data_lake_principal_identifier")
            assert result is not None, "Required property 'data_lake_principal_identifier' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataLakePrincipalProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnDataLakeSettings.ExternalDataFilteringAllowListProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class ExternalDataFilteringAllowListProperty:
        def __init__(self) -> None:
            '''A list of the account IDs of AWS accounts with Amazon EMR clusters that are allowed to perform data filtering.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datalakesettings-externaldatafilteringallowlist.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                external_data_filtering_allow_list_property = lakeformation.CfnDataLakeSettings.ExternalDataFilteringAllowListProperty()
            '''
            self._values: typing.Dict[builtins.str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExternalDataFilteringAllowListProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnDataLakeSettings.PrincipalPermissionsProperty",
        jsii_struct_bases=[],
        name_mapping={"permissions": "permissions", "principal": "principal"},
    )
    class PrincipalPermissionsProperty:
        def __init__(
            self,
            *,
            permissions: typing.Sequence[builtins.str],
            principal: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataLakeSettings.DataLakePrincipalProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Permissions granted to a principal.

            :param permissions: The permissions that are granted to the principal.
            :param principal: The principal who is granted permissions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datalakesettings-principalpermissions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                principal_permissions_property = lakeformation.CfnDataLakeSettings.PrincipalPermissionsProperty(
                    permissions=["permissions"],
                    principal=lakeformation.CfnDataLakeSettings.DataLakePrincipalProperty(
                        data_lake_principal_identifier="dataLakePrincipalIdentifier"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__71d0279f7a0c8de462002223da529999b8cfab83d83a4f5d4c771f0df4712e5f)
                check_type(argname="argument permissions", value=permissions, expected_type=type_hints["permissions"])
                check_type(argname="argument principal", value=principal, expected_type=type_hints["principal"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "permissions": permissions,
                "principal": principal,
            }

        @builtins.property
        def permissions(self) -> typing.List[builtins.str]:
            '''The permissions that are granted to the principal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datalakesettings-principalpermissions.html#cfn-lakeformation-datalakesettings-principalpermissions-permissions
            '''
            result = self._values.get("permissions")
            assert result is not None, "Required property 'permissions' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def principal(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDataLakeSettings.DataLakePrincipalProperty"]:
            '''The principal who is granted permissions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datalakesettings-principalpermissions.html#cfn-lakeformation-datalakesettings-principalpermissions-principal
            '''
            result = self._values.get("principal")
            assert result is not None, "Required property 'principal' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDataLakeSettings.DataLakePrincipalProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PrincipalPermissionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lakeformation.CfnDataLakeSettingsProps",
    jsii_struct_bases=[],
    name_mapping={
        "admins": "admins",
        "allow_external_data_filtering": "allowExternalDataFiltering",
        "authorized_session_tag_value_list": "authorizedSessionTagValueList",
        "create_database_default_permissions": "createDatabaseDefaultPermissions",
        "create_table_default_permissions": "createTableDefaultPermissions",
        "external_data_filtering_allow_list": "externalDataFilteringAllowList",
        "parameters": "parameters",
        "trusted_resource_owners": "trustedResourceOwners",
    },
)
class CfnDataLakeSettingsProps:
    def __init__(
        self,
        *,
        admins: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLakeSettings.DataLakePrincipalProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        allow_external_data_filtering: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        authorized_session_tag_value_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        create_database_default_permissions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLakeSettings.PrincipalPermissionsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        create_table_default_permissions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLakeSettings.PrincipalPermissionsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        external_data_filtering_allow_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLakeSettings.DataLakePrincipalProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        parameters: typing.Any = None,
        trusted_resource_owners: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDataLakeSettings``.

        :param admins: A list of AWS Lake Formation principals.
        :param allow_external_data_filtering: Whether to allow Amazon EMR clusters or other third-party query engines to access data managed by Lake Formation . If set to true, you allow Amazon EMR clusters or other third-party engines to access data in Amazon S3 locations that are registered with Lake Formation . If false or null, no third-party query engines will be able to access data in Amazon S3 locations that are registered with Lake Formation. For more information, see `External data filtering setting <https://docs.aws.amazon.com/lake-formation/latest/dg/initial-LF-setup.html#external-data-filter>`_ .
        :param authorized_session_tag_value_list: Lake Formation relies on a privileged process secured by Amazon EMR or the third party integrator to tag the user's role while assuming it. Lake Formation will publish the acceptable key-value pair, for example key = "LakeFormationTrustedCaller" and value = "TRUE" and the third party integrator must properly tag the temporary security credentials that will be used to call Lake Formation 's administrative API operations.
        :param create_database_default_permissions: Specifies whether access control on a newly created database is managed by Lake Formation permissions or exclusively by IAM permissions. A null value indicates that the access is controlled by Lake Formation permissions. ``ALL`` permissions assigned to ``IAM_ALLOWED_PRINCIPALS`` group indicates that the user's IAM permissions determine the access to the database. This is referred to as the setting "Use only IAM access control," and is to support backward compatibility with the AWS Glue permission model implemented by IAM permissions. The only permitted values are an empty array or an array that contains a single JSON object that grants ``ALL`` to ``IAM_ALLOWED_PRINCIPALS`` . For more information, see `Changing the default security settings for your data lake <https://docs.aws.amazon.com/lake-formation/latest/dg/change-settings.html>`_ .
        :param create_table_default_permissions: Specifies whether access control on a newly created table is managed by Lake Formation permissions or exclusively by IAM permissions. A null value indicates that the access is controlled by Lake Formation permissions. ``ALL`` permissions assigned to ``IAM_ALLOWED_PRINCIPALS`` group indicate that the user's IAM permissions determine the access to the table. This is referred to as the setting "Use only IAM access control," and is to support the backward compatibility with the AWS Glue permission model implemented by IAM permissions. The only permitted values are an empty array or an array that contains a single JSON object that grants ``ALL`` permissions to ``IAM_ALLOWED_PRINCIPALS`` . For more information, see `Changing the default security settings for your data lake <https://docs.aws.amazon.com/lake-formation/latest/dg/change-settings.html>`_ .
        :param external_data_filtering_allow_list: A list of the account IDs of AWS accounts with Amazon EMR clusters or third-party engines that are allwed to perform data filtering.
        :param parameters: A key-value map that provides an additional configuration on your data lake. ``CrossAccountVersion`` is the key you can configure in the ``Parameters`` field. Accepted values for the ``CrossAccountVersion`` key are 1, 2, and 3.
        :param trusted_resource_owners: An array of UTF-8 strings. A list of the resource-owning account IDs that the caller's account can use to share their user access details (user ARNs). The user ARNs can be logged in the resource owner's CloudTrail log. You may want to specify this property when you are in a high-trust boundary, such as the same team or company.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lakeformation as lakeformation
            
            # parameters: Any
            
            cfn_data_lake_settings_props = lakeformation.CfnDataLakeSettingsProps(
                admins=[lakeformation.CfnDataLakeSettings.DataLakePrincipalProperty(
                    data_lake_principal_identifier="dataLakePrincipalIdentifier"
                )],
                allow_external_data_filtering=False,
                authorized_session_tag_value_list=["authorizedSessionTagValueList"],
                create_database_default_permissions=[lakeformation.CfnDataLakeSettings.PrincipalPermissionsProperty(
                    permissions=["permissions"],
                    principal=lakeformation.CfnDataLakeSettings.DataLakePrincipalProperty(
                        data_lake_principal_identifier="dataLakePrincipalIdentifier"
                    )
                )],
                create_table_default_permissions=[lakeformation.CfnDataLakeSettings.PrincipalPermissionsProperty(
                    permissions=["permissions"],
                    principal=lakeformation.CfnDataLakeSettings.DataLakePrincipalProperty(
                        data_lake_principal_identifier="dataLakePrincipalIdentifier"
                    )
                )],
                external_data_filtering_allow_list=[lakeformation.CfnDataLakeSettings.DataLakePrincipalProperty(
                    data_lake_principal_identifier="dataLakePrincipalIdentifier"
                )],
                parameters=parameters,
                trusted_resource_owners=["trustedResourceOwners"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dce55f2e750b8b606563ee8be454eb95ace369e90671114b454db63f0cc7613d)
            check_type(argname="argument admins", value=admins, expected_type=type_hints["admins"])
            check_type(argname="argument allow_external_data_filtering", value=allow_external_data_filtering, expected_type=type_hints["allow_external_data_filtering"])
            check_type(argname="argument authorized_session_tag_value_list", value=authorized_session_tag_value_list, expected_type=type_hints["authorized_session_tag_value_list"])
            check_type(argname="argument create_database_default_permissions", value=create_database_default_permissions, expected_type=type_hints["create_database_default_permissions"])
            check_type(argname="argument create_table_default_permissions", value=create_table_default_permissions, expected_type=type_hints["create_table_default_permissions"])
            check_type(argname="argument external_data_filtering_allow_list", value=external_data_filtering_allow_list, expected_type=type_hints["external_data_filtering_allow_list"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument trusted_resource_owners", value=trusted_resource_owners, expected_type=type_hints["trusted_resource_owners"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if admins is not None:
            self._values["admins"] = admins
        if allow_external_data_filtering is not None:
            self._values["allow_external_data_filtering"] = allow_external_data_filtering
        if authorized_session_tag_value_list is not None:
            self._values["authorized_session_tag_value_list"] = authorized_session_tag_value_list
        if create_database_default_permissions is not None:
            self._values["create_database_default_permissions"] = create_database_default_permissions
        if create_table_default_permissions is not None:
            self._values["create_table_default_permissions"] = create_table_default_permissions
        if external_data_filtering_allow_list is not None:
            self._values["external_data_filtering_allow_list"] = external_data_filtering_allow_list
        if parameters is not None:
            self._values["parameters"] = parameters
        if trusted_resource_owners is not None:
            self._values["trusted_resource_owners"] = trusted_resource_owners

    @builtins.property
    def admins(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataLakeSettings.DataLakePrincipalProperty]]]]:
        '''A list of AWS Lake Formation principals.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-admins
        '''
        result = self._values.get("admins")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataLakeSettings.DataLakePrincipalProperty]]]], result)

    @builtins.property
    def allow_external_data_filtering(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to allow Amazon EMR clusters or other third-party query engines to access data managed by Lake Formation .

        If set to true, you allow Amazon EMR clusters or other third-party engines to access data in Amazon S3 locations that are registered with Lake Formation .

        If false or null, no third-party query engines will be able to access data in Amazon S3 locations that are registered with Lake Formation.

        For more information, see `External data filtering setting <https://docs.aws.amazon.com/lake-formation/latest/dg/initial-LF-setup.html#external-data-filter>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-allowexternaldatafiltering
        '''
        result = self._values.get("allow_external_data_filtering")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def authorized_session_tag_value_list(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Lake Formation relies on a privileged process secured by Amazon EMR or the third party integrator to tag the user's role while assuming it.

        Lake Formation will publish the acceptable key-value pair, for example key = "LakeFormationTrustedCaller" and value = "TRUE" and the third party integrator must properly tag the temporary security credentials that will be used to call Lake Formation 's administrative API operations.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-authorizedsessiontagvaluelist
        '''
        result = self._values.get("authorized_session_tag_value_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def create_database_default_permissions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataLakeSettings.PrincipalPermissionsProperty]]]]:
        '''Specifies whether access control on a newly created database is managed by Lake Formation permissions or exclusively by IAM permissions.

        A null value indicates that the access is controlled by Lake Formation permissions. ``ALL`` permissions assigned to ``IAM_ALLOWED_PRINCIPALS`` group indicates that the user's IAM permissions determine the access to the database. This is referred to as the setting "Use only IAM access control," and is to support backward compatibility with the AWS Glue permission model implemented by IAM permissions.

        The only permitted values are an empty array or an array that contains a single JSON object that grants ``ALL`` to ``IAM_ALLOWED_PRINCIPALS`` .

        For more information, see `Changing the default security settings for your data lake <https://docs.aws.amazon.com/lake-formation/latest/dg/change-settings.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-createdatabasedefaultpermissions
        '''
        result = self._values.get("create_database_default_permissions")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataLakeSettings.PrincipalPermissionsProperty]]]], result)

    @builtins.property
    def create_table_default_permissions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataLakeSettings.PrincipalPermissionsProperty]]]]:
        '''Specifies whether access control on a newly created table is managed by Lake Formation permissions or exclusively by IAM permissions.

        A null value indicates that the access is controlled by Lake Formation permissions. ``ALL`` permissions assigned to ``IAM_ALLOWED_PRINCIPALS`` group indicate that the user's IAM permissions determine the access to the table. This is referred to as the setting "Use only IAM access control," and is to support the backward compatibility with the AWS Glue permission model implemented by IAM permissions.

        The only permitted values are an empty array or an array that contains a single JSON object that grants ``ALL`` permissions to ``IAM_ALLOWED_PRINCIPALS`` .

        For more information, see `Changing the default security settings for your data lake <https://docs.aws.amazon.com/lake-formation/latest/dg/change-settings.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-createtabledefaultpermissions
        '''
        result = self._values.get("create_table_default_permissions")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataLakeSettings.PrincipalPermissionsProperty]]]], result)

    @builtins.property
    def external_data_filtering_allow_list(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataLakeSettings.DataLakePrincipalProperty]]]]:
        '''A list of the account IDs of AWS accounts with Amazon EMR clusters or third-party engines that are allwed to perform data filtering.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-externaldatafilteringallowlist
        '''
        result = self._values.get("external_data_filtering_allow_list")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataLakeSettings.DataLakePrincipalProperty]]]], result)

    @builtins.property
    def parameters(self) -> typing.Any:
        '''A key-value map that provides an additional configuration on your data lake.

        ``CrossAccountVersion`` is the key you can configure in the ``Parameters`` field. Accepted values for the ``CrossAccountVersion`` key are 1, 2, and 3.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Any, result)

    @builtins.property
    def trusted_resource_owners(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of UTF-8 strings.

        A list of the resource-owning account IDs that the caller's account can use to share their user access details (user ARNs). The user ARNs can be logged in the resource owner's CloudTrail log. You may want to specify this property when you are in a high-trust boundary, such as the same team or company.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-trustedresourceowners
        '''
        result = self._values.get("trusted_resource_owners")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataLakeSettingsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnPermissions(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lakeformation.CfnPermissions",
):
    '''The ``AWS::LakeFormation::Permissions`` resource represents the permissions that a principal has on an AWS Glue Data Catalog resource (such as AWS Glue database or AWS Glue tables).

    When you upload a permissions stack, the permissions are granted to the principal and when you remove the stack, the permissions are revoked from the principal. If you remove a stack, and the principal does not have the permissions referenced in the stack then AWS Lake Formation will throw an error because you can’t call revoke on non-existing permissions. To successfully remove the stack, you’ll need to regrant those permissions and then remove the stack.
    .. epigraph::

       New versions of AWS Lake Formation permission resources are now available. For more information, see: `AWS:LakeFormation::PrincipalPermissions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html>`_

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lakeformation as lakeformation
        
        cfn_permissions = lakeformation.CfnPermissions(self, "MyCfnPermissions",
            data_lake_principal=lakeformation.CfnPermissions.DataLakePrincipalProperty(
                data_lake_principal_identifier="dataLakePrincipalIdentifier"
            ),
            resource=lakeformation.CfnPermissions.ResourceProperty(
                database_resource=lakeformation.CfnPermissions.DatabaseResourceProperty(
                    catalog_id="catalogId",
                    name="name"
                ),
                data_location_resource=lakeformation.CfnPermissions.DataLocationResourceProperty(
                    catalog_id="catalogId",
                    s3_resource="s3Resource"
                ),
                table_resource=lakeformation.CfnPermissions.TableResourceProperty(
                    catalog_id="catalogId",
                    database_name="databaseName",
                    name="name",
                    table_wildcard=lakeformation.CfnPermissions.TableWildcardProperty()
                ),
                table_with_columns_resource=lakeformation.CfnPermissions.TableWithColumnsResourceProperty(
                    catalog_id="catalogId",
                    column_names=["columnNames"],
                    column_wildcard=lakeformation.CfnPermissions.ColumnWildcardProperty(
                        excluded_column_names=["excludedColumnNames"]
                    ),
                    database_name="databaseName",
                    name="name"
                )
            ),
        
            # the properties below are optional
            permissions=["permissions"],
            permissions_with_grant_option=["permissionsWithGrantOption"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        data_lake_principal: typing.Union[_IResolvable_da3f097b, typing.Union["CfnPermissions.DataLakePrincipalProperty", typing.Dict[builtins.str, typing.Any]]],
        resource: typing.Union[_IResolvable_da3f097b, typing.Union["CfnPermissions.ResourceProperty", typing.Dict[builtins.str, typing.Any]]],
        permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
        permissions_with_grant_option: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param data_lake_principal: The AWS Lake Formation principal.
        :param resource: A structure for the resource.
        :param permissions: The permissions granted or revoked.
        :param permissions_with_grant_option: Indicates the ability to grant permissions (as a subset of permissions granted).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66f9b8220129009f27ac675ce32ccf618706bd509a2bdf99308bcd0b7a7ecb36)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPermissionsProps(
            data_lake_principal=data_lake_principal,
            resource=resource,
            permissions=permissions,
            permissions_with_grant_option=permissions_with_grant_option,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e596145285f2a793cf97360dcf20f6bff154e42d413389fa60459a8fee6d280)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1ee971ab2aceb77af8d182ab99af94a6965b16a2c3d0275e663cdf73637933bf)
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
    @jsii.member(jsii_name="dataLakePrincipal")
    def data_lake_principal(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnPermissions.DataLakePrincipalProperty"]:
        '''The AWS Lake Formation principal.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnPermissions.DataLakePrincipalProperty"], jsii.get(self, "dataLakePrincipal"))

    @data_lake_principal.setter
    def data_lake_principal(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnPermissions.DataLakePrincipalProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b52466eba74fe39a155b91afd467a62a59fd8b7da0cdf280f844dfae547c7e88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataLakePrincipal", value)

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnPermissions.ResourceProperty"]:
        '''A structure for the resource.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnPermissions.ResourceProperty"], jsii.get(self, "resource"))

    @resource.setter
    def resource(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnPermissions.ResourceProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a8d760390e3b2e9ed402ee340c7169bf72a75fca3b15a45103c7e0e6e61a5b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resource", value)

    @builtins.property
    @jsii.member(jsii_name="permissions")
    def permissions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The permissions granted or revoked.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "permissions"))

    @permissions.setter
    def permissions(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1c9d158fab35ea7c0a56ddd6ec2e6b9628418e53bc9a07544a2abaf1f18dacb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissions", value)

    @builtins.property
    @jsii.member(jsii_name="permissionsWithGrantOption")
    def permissions_with_grant_option(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Indicates the ability to grant permissions (as a subset of permissions granted).'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "permissionsWithGrantOption"))

    @permissions_with_grant_option.setter
    def permissions_with_grant_option(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81251fb4fda47174588bc5781a51e64b3d055e355f7a6b70ecb93007b4046366)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionsWithGrantOption", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPermissions.ColumnWildcardProperty",
        jsii_struct_bases=[],
        name_mapping={"excluded_column_names": "excludedColumnNames"},
    )
    class ColumnWildcardProperty:
        def __init__(
            self,
            *,
            excluded_column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''A wildcard object, consisting of an optional list of excluded column names or indexes.

            :param excluded_column_names: Excludes column names. Any column with this name will be excluded.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-columnwildcard.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                column_wildcard_property = lakeformation.CfnPermissions.ColumnWildcardProperty(
                    excluded_column_names=["excludedColumnNames"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cf52b2441eb8a74ff7018cce9b6068a2ae059867acbdf38dce8ace97c7cb1145)
                check_type(argname="argument excluded_column_names", value=excluded_column_names, expected_type=type_hints["excluded_column_names"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if excluded_column_names is not None:
                self._values["excluded_column_names"] = excluded_column_names

        @builtins.property
        def excluded_column_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Excludes column names.

            Any column with this name will be excluded.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-columnwildcard.html#cfn-lakeformation-permissions-columnwildcard-excludedcolumnnames
            '''
            result = self._values.get("excluded_column_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ColumnWildcardProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPermissions.DataLakePrincipalProperty",
        jsii_struct_bases=[],
        name_mapping={"data_lake_principal_identifier": "dataLakePrincipalIdentifier"},
    )
    class DataLakePrincipalProperty:
        def __init__(
            self,
            *,
            data_lake_principal_identifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The Lake Formation principal.

            :param data_lake_principal_identifier: An identifier for the Lake Formation principal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalakeprincipal.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                data_lake_principal_property = lakeformation.CfnPermissions.DataLakePrincipalProperty(
                    data_lake_principal_identifier="dataLakePrincipalIdentifier"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__80d8592bcc661e98e594ef066a2f224d8bd0d848c79b77076a27b690bc10264a)
                check_type(argname="argument data_lake_principal_identifier", value=data_lake_principal_identifier, expected_type=type_hints["data_lake_principal_identifier"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if data_lake_principal_identifier is not None:
                self._values["data_lake_principal_identifier"] = data_lake_principal_identifier

        @builtins.property
        def data_lake_principal_identifier(self) -> typing.Optional[builtins.str]:
            '''An identifier for the Lake Formation principal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalakeprincipal.html#cfn-lakeformation-permissions-datalakeprincipal-datalakeprincipalidentifier
            '''
            result = self._values.get("data_lake_principal_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataLakePrincipalProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPermissions.DataLocationResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"catalog_id": "catalogId", "s3_resource": "s3Resource"},
    )
    class DataLocationResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: typing.Optional[builtins.str] = None,
            s3_resource: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A structure for a data location object where permissions are granted or revoked.

            :param catalog_id: The identifier for the Data Catalog . By default, it is the account ID of the caller.
            :param s3_resource: The Amazon Resource Name (ARN) that uniquely identifies the data location resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                data_location_resource_property = lakeformation.CfnPermissions.DataLocationResourceProperty(
                    catalog_id="catalogId",
                    s3_resource="s3Resource"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__143e8666ee32b6c4cfaf593713c8528521c39e68a778350ee9a6abbc28f00afd)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument s3_resource", value=s3_resource, expected_type=type_hints["s3_resource"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if catalog_id is not None:
                self._values["catalog_id"] = catalog_id
            if s3_resource is not None:
                self._values["s3_resource"] = s3_resource

        @builtins.property
        def catalog_id(self) -> typing.Optional[builtins.str]:
            '''The identifier for the Data Catalog .

            By default, it is the account ID of the caller.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html#cfn-lakeformation-permissions-datalocationresource-catalogid
            '''
            result = self._values.get("catalog_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_resource(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) that uniquely identifies the data location resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html#cfn-lakeformation-permissions-datalocationresource-s3resource
            '''
            result = self._values.get("s3_resource")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataLocationResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPermissions.DatabaseResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"catalog_id": "catalogId", "name": "name"},
    )
    class DatabaseResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A structure for the database object.

            :param catalog_id: The identifier for the Data Catalog . By default, it is the account ID of the caller.
            :param name: The name of the database resource. Unique to the Data Catalog.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-databaseresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                database_resource_property = lakeformation.CfnPermissions.DatabaseResourceProperty(
                    catalog_id="catalogId",
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b97daaaad005292df9c62b56d08c4c1f07af2aa89f795fc5055f09c33dc04502)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if catalog_id is not None:
                self._values["catalog_id"] = catalog_id
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def catalog_id(self) -> typing.Optional[builtins.str]:
            '''The identifier for the Data Catalog .

            By default, it is the account ID of the caller.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-databaseresource.html#cfn-lakeformation-permissions-databaseresource-catalogid
            '''
            result = self._values.get("catalog_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the database resource.

            Unique to the Data Catalog.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-databaseresource.html#cfn-lakeformation-permissions-databaseresource-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatabaseResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPermissions.ResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "database_resource": "databaseResource",
            "data_location_resource": "dataLocationResource",
            "table_resource": "tableResource",
            "table_with_columns_resource": "tableWithColumnsResource",
        },
    )
    class ResourceProperty:
        def __init__(
            self,
            *,
            database_resource: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPermissions.DatabaseResourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            data_location_resource: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPermissions.DataLocationResourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            table_resource: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPermissions.TableResourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            table_with_columns_resource: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPermissions.TableWithColumnsResourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A structure for the resource.

            :param database_resource: A structure for the database object.
            :param data_location_resource: A structure for a data location object where permissions are granted or revoked.
            :param table_resource: A structure for the table object. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.
            :param table_with_columns_resource: A structure for a table with columns object. This object is only used when granting a SELECT permission.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                resource_property = lakeformation.CfnPermissions.ResourceProperty(
                    database_resource=lakeformation.CfnPermissions.DatabaseResourceProperty(
                        catalog_id="catalogId",
                        name="name"
                    ),
                    data_location_resource=lakeformation.CfnPermissions.DataLocationResourceProperty(
                        catalog_id="catalogId",
                        s3_resource="s3Resource"
                    ),
                    table_resource=lakeformation.CfnPermissions.TableResourceProperty(
                        catalog_id="catalogId",
                        database_name="databaseName",
                        name="name",
                        table_wildcard=lakeformation.CfnPermissions.TableWildcardProperty()
                    ),
                    table_with_columns_resource=lakeformation.CfnPermissions.TableWithColumnsResourceProperty(
                        catalog_id="catalogId",
                        column_names=["columnNames"],
                        column_wildcard=lakeformation.CfnPermissions.ColumnWildcardProperty(
                            excluded_column_names=["excludedColumnNames"]
                        ),
                        database_name="databaseName",
                        name="name"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7e873d4ebccabb106e53e74b5438b8f89e526a4874c703f025c42839ae30566d)
                check_type(argname="argument database_resource", value=database_resource, expected_type=type_hints["database_resource"])
                check_type(argname="argument data_location_resource", value=data_location_resource, expected_type=type_hints["data_location_resource"])
                check_type(argname="argument table_resource", value=table_resource, expected_type=type_hints["table_resource"])
                check_type(argname="argument table_with_columns_resource", value=table_with_columns_resource, expected_type=type_hints["table_with_columns_resource"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if database_resource is not None:
                self._values["database_resource"] = database_resource
            if data_location_resource is not None:
                self._values["data_location_resource"] = data_location_resource
            if table_resource is not None:
                self._values["table_resource"] = table_resource
            if table_with_columns_resource is not None:
                self._values["table_with_columns_resource"] = table_with_columns_resource

        @builtins.property
        def database_resource(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPermissions.DatabaseResourceProperty"]]:
            '''A structure for the database object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-databaseresource
            '''
            result = self._values.get("database_resource")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPermissions.DatabaseResourceProperty"]], result)

        @builtins.property
        def data_location_resource(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPermissions.DataLocationResourceProperty"]]:
            '''A structure for a data location object where permissions are granted or revoked.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-datalocationresource
            '''
            result = self._values.get("data_location_resource")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPermissions.DataLocationResourceProperty"]], result)

        @builtins.property
        def table_resource(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPermissions.TableResourceProperty"]]:
            '''A structure for the table object.

            A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-tableresource
            '''
            result = self._values.get("table_resource")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPermissions.TableResourceProperty"]], result)

        @builtins.property
        def table_with_columns_resource(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPermissions.TableWithColumnsResourceProperty"]]:
            '''A structure for a table with columns object.

            This object is only used when granting a SELECT permission.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-tablewithcolumnsresource
            '''
            result = self._values.get("table_with_columns_resource")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPermissions.TableWithColumnsResourceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPermissions.TableResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "database_name": "databaseName",
            "name": "name",
            "table_wildcard": "tableWildcard",
        },
    )
    class TableResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: typing.Optional[builtins.str] = None,
            database_name: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            table_wildcard: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPermissions.TableWildcardProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A structure for the table object.

            A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

            :param catalog_id: The identifier for the Data Catalog . By default, it is the account ID of the caller.
            :param database_name: The name of the database for the table. Unique to a Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.
            :param name: The name of the table.
            :param table_wildcard: An empty object representing all tables under a database. If this field is specified instead of the ``Name`` field, all tables under ``DatabaseName`` will have permission changes applied.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                table_resource_property = lakeformation.CfnPermissions.TableResourceProperty(
                    catalog_id="catalogId",
                    database_name="databaseName",
                    name="name",
                    table_wildcard=lakeformation.CfnPermissions.TableWildcardProperty()
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__25c68a645287e81e1ea32708958d371278c40c2510ffac671ba40eeea7fe444e)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument table_wildcard", value=table_wildcard, expected_type=type_hints["table_wildcard"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if catalog_id is not None:
                self._values["catalog_id"] = catalog_id
            if database_name is not None:
                self._values["database_name"] = database_name
            if name is not None:
                self._values["name"] = name
            if table_wildcard is not None:
                self._values["table_wildcard"] = table_wildcard

        @builtins.property
        def catalog_id(self) -> typing.Optional[builtins.str]:
            '''The identifier for the Data Catalog .

            By default, it is the account ID of the caller.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-catalogid
            '''
            result = self._values.get("catalog_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def database_name(self) -> typing.Optional[builtins.str]:
            '''The name of the database for the table.

            Unique to a Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-databasename
            '''
            result = self._values.get("database_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def table_wildcard(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPermissions.TableWildcardProperty"]]:
            '''An empty object representing all tables under a database.

            If this field is specified instead of the ``Name`` field, all tables under ``DatabaseName`` will have permission changes applied.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-tablewildcard
            '''
            result = self._values.get("table_wildcard")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPermissions.TableWildcardProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TableResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPermissions.TableWildcardProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class TableWildcardProperty:
        def __init__(self) -> None:
            '''A wildcard object representing every table under a database.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewildcard.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                table_wildcard_property = lakeformation.CfnPermissions.TableWildcardProperty()
            '''
            self._values: typing.Dict[builtins.str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TableWildcardProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPermissions.TableWithColumnsResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "column_names": "columnNames",
            "column_wildcard": "columnWildcard",
            "database_name": "databaseName",
            "name": "name",
        },
    )
    class TableWithColumnsResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: typing.Optional[builtins.str] = None,
            column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
            column_wildcard: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPermissions.ColumnWildcardProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            database_name: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A structure for a table with columns object. This object is only used when granting a SELECT permission.

            This object must take a value for at least one of ``ColumnsNames`` , ``ColumnsIndexes`` , or ``ColumnsWildcard`` .

            :param catalog_id: The identifier for the Data Catalog . By default, it is the account ID of the caller.
            :param column_names: The list of column names for the table. At least one of ``ColumnNames`` or ``ColumnWildcard`` is required.
            :param column_wildcard: A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames`` or ``ColumnWildcard`` is required.
            :param database_name: The name of the database for the table with columns resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.
            :param name: The name of the table resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                table_with_columns_resource_property = lakeformation.CfnPermissions.TableWithColumnsResourceProperty(
                    catalog_id="catalogId",
                    column_names=["columnNames"],
                    column_wildcard=lakeformation.CfnPermissions.ColumnWildcardProperty(
                        excluded_column_names=["excludedColumnNames"]
                    ),
                    database_name="databaseName",
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fd66e1173aa0d6dbdb98124297f83efdbc21cf4278fca711775ba212a19929c4)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument column_names", value=column_names, expected_type=type_hints["column_names"])
                check_type(argname="argument column_wildcard", value=column_wildcard, expected_type=type_hints["column_wildcard"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if catalog_id is not None:
                self._values["catalog_id"] = catalog_id
            if column_names is not None:
                self._values["column_names"] = column_names
            if column_wildcard is not None:
                self._values["column_wildcard"] = column_wildcard
            if database_name is not None:
                self._values["database_name"] = database_name
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def catalog_id(self) -> typing.Optional[builtins.str]:
            '''The identifier for the Data Catalog .

            By default, it is the account ID of the caller.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-catalogid
            '''
            result = self._values.get("catalog_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def column_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The list of column names for the table.

            At least one of ``ColumnNames`` or ``ColumnWildcard`` is required.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-columnnames
            '''
            result = self._values.get("column_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def column_wildcard(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPermissions.ColumnWildcardProperty"]]:
            '''A wildcard specified by a ``ColumnWildcard`` object.

            At least one of ``ColumnNames`` or ``ColumnWildcard`` is required.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-columnwildcard
            '''
            result = self._values.get("column_wildcard")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPermissions.ColumnWildcardProperty"]], result)

        @builtins.property
        def database_name(self) -> typing.Optional[builtins.str]:
            '''The name of the database for the table with columns resource.

            Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-databasename
            '''
            result = self._values.get("database_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the table resource.

            A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TableWithColumnsResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lakeformation.CfnPermissionsProps",
    jsii_struct_bases=[],
    name_mapping={
        "data_lake_principal": "dataLakePrincipal",
        "resource": "resource",
        "permissions": "permissions",
        "permissions_with_grant_option": "permissionsWithGrantOption",
    },
)
class CfnPermissionsProps:
    def __init__(
        self,
        *,
        data_lake_principal: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPermissions.DataLakePrincipalProperty, typing.Dict[builtins.str, typing.Any]]],
        resource: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPermissions.ResourceProperty, typing.Dict[builtins.str, typing.Any]]],
        permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
        permissions_with_grant_option: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPermissions``.

        :param data_lake_principal: The AWS Lake Formation principal.
        :param resource: A structure for the resource.
        :param permissions: The permissions granted or revoked.
        :param permissions_with_grant_option: Indicates the ability to grant permissions (as a subset of permissions granted).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lakeformation as lakeformation
            
            cfn_permissions_props = lakeformation.CfnPermissionsProps(
                data_lake_principal=lakeformation.CfnPermissions.DataLakePrincipalProperty(
                    data_lake_principal_identifier="dataLakePrincipalIdentifier"
                ),
                resource=lakeformation.CfnPermissions.ResourceProperty(
                    database_resource=lakeformation.CfnPermissions.DatabaseResourceProperty(
                        catalog_id="catalogId",
                        name="name"
                    ),
                    data_location_resource=lakeformation.CfnPermissions.DataLocationResourceProperty(
                        catalog_id="catalogId",
                        s3_resource="s3Resource"
                    ),
                    table_resource=lakeformation.CfnPermissions.TableResourceProperty(
                        catalog_id="catalogId",
                        database_name="databaseName",
                        name="name",
                        table_wildcard=lakeformation.CfnPermissions.TableWildcardProperty()
                    ),
                    table_with_columns_resource=lakeformation.CfnPermissions.TableWithColumnsResourceProperty(
                        catalog_id="catalogId",
                        column_names=["columnNames"],
                        column_wildcard=lakeformation.CfnPermissions.ColumnWildcardProperty(
                            excluded_column_names=["excludedColumnNames"]
                        ),
                        database_name="databaseName",
                        name="name"
                    )
                ),
            
                # the properties below are optional
                permissions=["permissions"],
                permissions_with_grant_option=["permissionsWithGrantOption"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fb762048f92dd06746b23564061560f03db7ad3a9de2ed4abd1fe22d6b087f1)
            check_type(argname="argument data_lake_principal", value=data_lake_principal, expected_type=type_hints["data_lake_principal"])
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
            check_type(argname="argument permissions", value=permissions, expected_type=type_hints["permissions"])
            check_type(argname="argument permissions_with_grant_option", value=permissions_with_grant_option, expected_type=type_hints["permissions_with_grant_option"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_lake_principal": data_lake_principal,
            "resource": resource,
        }
        if permissions is not None:
            self._values["permissions"] = permissions
        if permissions_with_grant_option is not None:
            self._values["permissions_with_grant_option"] = permissions_with_grant_option

    @builtins.property
    def data_lake_principal(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnPermissions.DataLakePrincipalProperty]:
        '''The AWS Lake Formation principal.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-datalakeprincipal
        '''
        result = self._values.get("data_lake_principal")
        assert result is not None, "Required property 'data_lake_principal' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnPermissions.DataLakePrincipalProperty], result)

    @builtins.property
    def resource(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnPermissions.ResourceProperty]:
        '''A structure for the resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-resource
        '''
        result = self._values.get("resource")
        assert result is not None, "Required property 'resource' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnPermissions.ResourceProperty], result)

    @builtins.property
    def permissions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The permissions granted or revoked.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-permissions
        '''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def permissions_with_grant_option(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Indicates the ability to grant permissions (as a subset of permissions granted).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-permissionswithgrantoption
        '''
        result = self._values.get("permissions_with_grant_option")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPermissionsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnPrincipalPermissions(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lakeformation.CfnPrincipalPermissions",
):
    '''The ``AWS::LakeFormation::PrincipalPermissions`` resource represents the permissions that a principal has on a Data Catalog resource (such as AWS Glue databases or AWS Glue tables).

    When you create a ``PrincipalPermissions`` resource, the permissions are granted via the AWS Lake Formation ``GrantPermissions`` API operation. When you delete a ``PrincipalPermissions`` resource, the permissions on principal-resource pair are revoked via the AWS Lake Formation ``RevokePermissions`` API operation.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lakeformation as lakeformation
        
        # catalog: Any
        # table_wildcard: Any
        
        cfn_principal_permissions = lakeformation.CfnPrincipalPermissions(self, "MyCfnPrincipalPermissions",
            permissions=["permissions"],
            permissions_with_grant_option=["permissionsWithGrantOption"],
            principal=lakeformation.CfnPrincipalPermissions.DataLakePrincipalProperty(
                data_lake_principal_identifier="dataLakePrincipalIdentifier"
            ),
            resource=lakeformation.CfnPrincipalPermissions.ResourceProperty(
                catalog=catalog,
                database=lakeformation.CfnPrincipalPermissions.DatabaseResourceProperty(
                    catalog_id="catalogId",
                    name="name"
                ),
                data_cells_filter=lakeformation.CfnPrincipalPermissions.DataCellsFilterResourceProperty(
                    database_name="databaseName",
                    name="name",
                    table_catalog_id="tableCatalogId",
                    table_name="tableName"
                ),
                data_location=lakeformation.CfnPrincipalPermissions.DataLocationResourceProperty(
                    catalog_id="catalogId",
                    resource_arn="resourceArn"
                ),
                lf_tag=lakeformation.CfnPrincipalPermissions.LFTagKeyResourceProperty(
                    catalog_id="catalogId",
                    tag_key="tagKey",
                    tag_values=["tagValues"]
                ),
                lf_tag_policy=lakeformation.CfnPrincipalPermissions.LFTagPolicyResourceProperty(
                    catalog_id="catalogId",
                    expression=[lakeformation.CfnPrincipalPermissions.LFTagProperty(
                        tag_key="tagKey",
                        tag_values=["tagValues"]
                    )],
                    resource_type="resourceType"
                ),
                table=lakeformation.CfnPrincipalPermissions.TableResourceProperty(
                    catalog_id="catalogId",
                    database_name="databaseName",
        
                    # the properties below are optional
                    name="name",
                    table_wildcard=table_wildcard
                ),
                table_with_columns=lakeformation.CfnPrincipalPermissions.TableWithColumnsResourceProperty(
                    catalog_id="catalogId",
                    database_name="databaseName",
                    name="name",
        
                    # the properties below are optional
                    column_names=["columnNames"],
                    column_wildcard=lakeformation.CfnPrincipalPermissions.ColumnWildcardProperty(
                        excluded_column_names=["excludedColumnNames"]
                    )
                )
            ),
        
            # the properties below are optional
            catalog="catalog"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        permissions: typing.Sequence[builtins.str],
        permissions_with_grant_option: typing.Sequence[builtins.str],
        principal: typing.Union[_IResolvable_da3f097b, typing.Union["CfnPrincipalPermissions.DataLakePrincipalProperty", typing.Dict[builtins.str, typing.Any]]],
        resource: typing.Union[_IResolvable_da3f097b, typing.Union["CfnPrincipalPermissions.ResourceProperty", typing.Dict[builtins.str, typing.Any]]],
        catalog: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param permissions: The permissions granted or revoked.
        :param permissions_with_grant_option: Indicates the ability to grant permissions (as a subset of permissions granted).
        :param principal: The principal to be granted a permission.
        :param resource: The resource to be granted or revoked permissions.
        :param catalog: The identifier for the Data Catalog . By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2eb5d81db38bf28121ba5fc7c8223b5f9b99138c19ff95a360f576c85eee776b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPrincipalPermissionsProps(
            permissions=permissions,
            permissions_with_grant_option=permissions_with_grant_option,
            principal=principal,
            resource=resource,
            catalog=catalog,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19bcd0e8fdbb5452a744983c0bca1e00952558553e30a4edad79228574b0871f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__22b65ac740c32d3048bd381021c49a684f9331531de0a8d324a618515c95ed01)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrPrincipalIdentifier")
    def attr_principal_identifier(self) -> builtins.str:
        '''Json encoding of the input principal.

        For example: ``{"DataLakePrincipalIdentifier":"arn:aws:iam::123456789012:role/ExampleRole"}``

        :cloudformationAttribute: PrincipalIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPrincipalIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="attrResourceIdentifier")
    def attr_resource_identifier(self) -> builtins.str:
        '''Json encoding of the input resource.

        For example: ``{"Catalog":null,"Database":null,"Table":null,"TableWithColumns":null,"DataLocation":null,"DataCellsFilter":{"TableCatalogId":"123456789012","DatabaseName":"ExampleDatabase","TableName":"ExampleTable","Name":"ExampleFilter"},"LFTag":null,"LFTagPolicy":null}``

        :cloudformationAttribute: ResourceIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="permissions")
    def permissions(self) -> typing.List[builtins.str]:
        '''The permissions granted or revoked.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "permissions"))

    @permissions.setter
    def permissions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f09e32f0f3382686a05ba58d341882cae134bae9543b28783028d3a2e39e825b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissions", value)

    @builtins.property
    @jsii.member(jsii_name="permissionsWithGrantOption")
    def permissions_with_grant_option(self) -> typing.List[builtins.str]:
        '''Indicates the ability to grant permissions (as a subset of permissions granted).'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "permissionsWithGrantOption"))

    @permissions_with_grant_option.setter
    def permissions_with_grant_option(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__209371d03e969c4e61d2a38660dbb7441ca9c5e81a7ef95333acdd87a14ddd0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionsWithGrantOption", value)

    @builtins.property
    @jsii.member(jsii_name="principal")
    def principal(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnPrincipalPermissions.DataLakePrincipalProperty"]:
        '''The principal to be granted a permission.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnPrincipalPermissions.DataLakePrincipalProperty"], jsii.get(self, "principal"))

    @principal.setter
    def principal(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnPrincipalPermissions.DataLakePrincipalProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1a6247a71b5100a75980e912dd96720cd90892a708b86881a36004028079dd5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principal", value)

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnPrincipalPermissions.ResourceProperty"]:
        '''The resource to be granted or revoked permissions.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnPrincipalPermissions.ResourceProperty"], jsii.get(self, "resource"))

    @resource.setter
    def resource(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnPrincipalPermissions.ResourceProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2cdd4778f3b42b1dbeec69000654d251230f2d8c9b50b55439c66ca17567ad3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resource", value)

    @builtins.property
    @jsii.member(jsii_name="catalog")
    def catalog(self) -> typing.Optional[builtins.str]:
        '''The identifier for the Data Catalog .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalog"))

    @catalog.setter
    def catalog(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d30f0e637fa1c5ffeca70a22e3d7a1083c596f26d2b181bb4f54624dba336c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalog", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPrincipalPermissions.ColumnWildcardProperty",
        jsii_struct_bases=[],
        name_mapping={"excluded_column_names": "excludedColumnNames"},
    )
    class ColumnWildcardProperty:
        def __init__(
            self,
            *,
            excluded_column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''A wildcard object, consisting of an optional list of excluded column names or indexes.

            :param excluded_column_names: Excludes column names. Any column with this name will be excluded.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-columnwildcard.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                column_wildcard_property = lakeformation.CfnPrincipalPermissions.ColumnWildcardProperty(
                    excluded_column_names=["excludedColumnNames"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3c2462e1081a2c39e7bf1727f3edf2e24354c2a890e9dd0028ce66f6d0577e20)
                check_type(argname="argument excluded_column_names", value=excluded_column_names, expected_type=type_hints["excluded_column_names"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if excluded_column_names is not None:
                self._values["excluded_column_names"] = excluded_column_names

        @builtins.property
        def excluded_column_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Excludes column names.

            Any column with this name will be excluded.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-columnwildcard.html#cfn-lakeformation-principalpermissions-columnwildcard-excludedcolumnnames
            '''
            result = self._values.get("excluded_column_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ColumnWildcardProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPrincipalPermissions.DataCellsFilterResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "database_name": "databaseName",
            "name": "name",
            "table_catalog_id": "tableCatalogId",
            "table_name": "tableName",
        },
    )
    class DataCellsFilterResourceProperty:
        def __init__(
            self,
            *,
            database_name: builtins.str,
            name: builtins.str,
            table_catalog_id: builtins.str,
            table_name: builtins.str,
        ) -> None:
            '''A structure that describes certain columns on certain rows.

            :param database_name: A database in the Data Catalog .
            :param name: The name given by the user to the data filter cell.
            :param table_catalog_id: The ID of the catalog to which the table belongs.
            :param table_name: The name of the table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datacellsfilterresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                data_cells_filter_resource_property = lakeformation.CfnPrincipalPermissions.DataCellsFilterResourceProperty(
                    database_name="databaseName",
                    name="name",
                    table_catalog_id="tableCatalogId",
                    table_name="tableName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__33ec037517e7c5996eee712eb67decb6b3d04aa964f155335bb0a4730b194be7)
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument table_catalog_id", value=table_catalog_id, expected_type=type_hints["table_catalog_id"])
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "database_name": database_name,
                "name": name,
                "table_catalog_id": table_catalog_id,
                "table_name": table_name,
            }

        @builtins.property
        def database_name(self) -> builtins.str:
            '''A database in the Data Catalog .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datacellsfilterresource.html#cfn-lakeformation-principalpermissions-datacellsfilterresource-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name given by the user to the data filter cell.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datacellsfilterresource.html#cfn-lakeformation-principalpermissions-datacellsfilterresource-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_catalog_id(self) -> builtins.str:
            '''The ID of the catalog to which the table belongs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datacellsfilterresource.html#cfn-lakeformation-principalpermissions-datacellsfilterresource-tablecatalogid
            '''
            result = self._values.get("table_catalog_id")
            assert result is not None, "Required property 'table_catalog_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_name(self) -> builtins.str:
            '''The name of the table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datacellsfilterresource.html#cfn-lakeformation-principalpermissions-datacellsfilterresource-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataCellsFilterResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPrincipalPermissions.DataLakePrincipalProperty",
        jsii_struct_bases=[],
        name_mapping={"data_lake_principal_identifier": "dataLakePrincipalIdentifier"},
    )
    class DataLakePrincipalProperty:
        def __init__(
            self,
            *,
            data_lake_principal_identifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The AWS Lake Formation principal.

            :param data_lake_principal_identifier: An identifier for the AWS Lake Formation principal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datalakeprincipal.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                data_lake_principal_property = lakeformation.CfnPrincipalPermissions.DataLakePrincipalProperty(
                    data_lake_principal_identifier="dataLakePrincipalIdentifier"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__de361ca366cfcbb9bf826b663d0cfa9926ca81d247442348669309b4fc05c64e)
                check_type(argname="argument data_lake_principal_identifier", value=data_lake_principal_identifier, expected_type=type_hints["data_lake_principal_identifier"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if data_lake_principal_identifier is not None:
                self._values["data_lake_principal_identifier"] = data_lake_principal_identifier

        @builtins.property
        def data_lake_principal_identifier(self) -> typing.Optional[builtins.str]:
            '''An identifier for the AWS Lake Formation principal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datalakeprincipal.html#cfn-lakeformation-principalpermissions-datalakeprincipal-datalakeprincipalidentifier
            '''
            result = self._values.get("data_lake_principal_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataLakePrincipalProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPrincipalPermissions.DataLocationResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"catalog_id": "catalogId", "resource_arn": "resourceArn"},
    )
    class DataLocationResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: builtins.str,
            resource_arn: builtins.str,
        ) -> None:
            '''A structure for a data location object where permissions are granted or revoked.

            :param catalog_id: The identifier for the Data Catalog where the location is registered with AWS Lake Formation .
            :param resource_arn: The Amazon Resource Name (ARN) that uniquely identifies the data location resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datalocationresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                data_location_resource_property = lakeformation.CfnPrincipalPermissions.DataLocationResourceProperty(
                    catalog_id="catalogId",
                    resource_arn="resourceArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2ef403264bd2d9619e7538638731036dd217c08886e8a889112aaec3f409612f)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "catalog_id": catalog_id,
                "resource_arn": resource_arn,
            }

        @builtins.property
        def catalog_id(self) -> builtins.str:
            '''The identifier for the Data Catalog where the location is registered with AWS Lake Formation .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datalocationresource.html#cfn-lakeformation-principalpermissions-datalocationresource-catalogid
            '''
            result = self._values.get("catalog_id")
            assert result is not None, "Required property 'catalog_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def resource_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) that uniquely identifies the data location resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datalocationresource.html#cfn-lakeformation-principalpermissions-datalocationresource-resourcearn
            '''
            result = self._values.get("resource_arn")
            assert result is not None, "Required property 'resource_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataLocationResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPrincipalPermissions.DatabaseResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"catalog_id": "catalogId", "name": "name"},
    )
    class DatabaseResourceProperty:
        def __init__(self, *, catalog_id: builtins.str, name: builtins.str) -> None:
            '''A structure for the database object.

            :param catalog_id: The identifier for the Data Catalog. By default, it is the account ID of the caller.
            :param name: The name of the database resource. Unique to the Data Catalog.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-databaseresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                database_resource_property = lakeformation.CfnPrincipalPermissions.DatabaseResourceProperty(
                    catalog_id="catalogId",
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__140938f79b31a570727d46b681bf0dbe828eab77f52f9cdaa5caecbcf61c8537)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "catalog_id": catalog_id,
                "name": name,
            }

        @builtins.property
        def catalog_id(self) -> builtins.str:
            '''The identifier for the Data Catalog.

            By default, it is the account ID of the caller.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-databaseresource.html#cfn-lakeformation-principalpermissions-databaseresource-catalogid
            '''
            result = self._values.get("catalog_id")
            assert result is not None, "Required property 'catalog_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the database resource.

            Unique to the Data Catalog.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-databaseresource.html#cfn-lakeformation-principalpermissions-databaseresource-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatabaseResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPrincipalPermissions.LFTagKeyResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "tag_key": "tagKey",
            "tag_values": "tagValues",
        },
    )
    class LFTagKeyResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: builtins.str,
            tag_key: builtins.str,
            tag_values: typing.Sequence[builtins.str],
        ) -> None:
            '''A structure containing an LF-tag key and values for a resource.

            :param catalog_id: The identifier for the Data Catalog where the location is registered with Data Catalog .
            :param tag_key: The key-name for the LF-tag.
            :param tag_values: A list of possible values for the corresponding ``TagKey`` of an LF-tag key-value pair.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagkeyresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                l_fTag_key_resource_property = lakeformation.CfnPrincipalPermissions.LFTagKeyResourceProperty(
                    catalog_id="catalogId",
                    tag_key="tagKey",
                    tag_values=["tagValues"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1609270b64a1dfa63f7d47e0aa35028ab7fe44e010c798dbfd732fe2815564f9)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
                check_type(argname="argument tag_values", value=tag_values, expected_type=type_hints["tag_values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "catalog_id": catalog_id,
                "tag_key": tag_key,
                "tag_values": tag_values,
            }

        @builtins.property
        def catalog_id(self) -> builtins.str:
            '''The identifier for the Data Catalog where the location is registered with Data Catalog .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagkeyresource.html#cfn-lakeformation-principalpermissions-lftagkeyresource-catalogid
            '''
            result = self._values.get("catalog_id")
            assert result is not None, "Required property 'catalog_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def tag_key(self) -> builtins.str:
            '''The key-name for the LF-tag.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagkeyresource.html#cfn-lakeformation-principalpermissions-lftagkeyresource-tagkey
            '''
            result = self._values.get("tag_key")
            assert result is not None, "Required property 'tag_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def tag_values(self) -> typing.List[builtins.str]:
            '''A list of possible values for the corresponding ``TagKey`` of an LF-tag key-value pair.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagkeyresource.html#cfn-lakeformation-principalpermissions-lftagkeyresource-tagvalues
            '''
            result = self._values.get("tag_values")
            assert result is not None, "Required property 'tag_values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LFTagKeyResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPrincipalPermissions.LFTagPolicyResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "expression": "expression",
            "resource_type": "resourceType",
        },
    )
    class LFTagPolicyResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: builtins.str,
            expression: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPrincipalPermissions.LFTagProperty", typing.Dict[builtins.str, typing.Any]]]]],
            resource_type: builtins.str,
        ) -> None:
            '''A list of LF-tag conditions that define a resource's LF-tag policy.

            A structure that allows an admin to grant user permissions on certain conditions. For example, granting a role access to all columns that do not have the LF-tag 'PII' in tables that have the LF-tag 'Prod'.

            :param catalog_id: The identifier for the Data Catalog . The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.
            :param expression: A list of LF-tag conditions that apply to the resource's LF-tag policy.
            :param resource_type: The resource type for which the LF-tag policy applies.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagpolicyresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                l_fTag_policy_resource_property = lakeformation.CfnPrincipalPermissions.LFTagPolicyResourceProperty(
                    catalog_id="catalogId",
                    expression=[lakeformation.CfnPrincipalPermissions.LFTagProperty(
                        tag_key="tagKey",
                        tag_values=["tagValues"]
                    )],
                    resource_type="resourceType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__283f469e66d16220abd50df44457c58f1e228a52182f63247acce003afecb253)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
                check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "catalog_id": catalog_id,
                "expression": expression,
                "resource_type": resource_type,
            }

        @builtins.property
        def catalog_id(self) -> builtins.str:
            '''The identifier for the Data Catalog .

            The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagpolicyresource.html#cfn-lakeformation-principalpermissions-lftagpolicyresource-catalogid
            '''
            result = self._values.get("catalog_id")
            assert result is not None, "Required property 'catalog_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def expression(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPrincipalPermissions.LFTagProperty"]]]:
            '''A list of LF-tag conditions that apply to the resource's LF-tag policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagpolicyresource.html#cfn-lakeformation-principalpermissions-lftagpolicyresource-expression
            '''
            result = self._values.get("expression")
            assert result is not None, "Required property 'expression' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPrincipalPermissions.LFTagProperty"]]], result)

        @builtins.property
        def resource_type(self) -> builtins.str:
            '''The resource type for which the LF-tag policy applies.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagpolicyresource.html#cfn-lakeformation-principalpermissions-lftagpolicyresource-resourcetype
            '''
            result = self._values.get("resource_type")
            assert result is not None, "Required property 'resource_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LFTagPolicyResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPrincipalPermissions.LFTagProperty",
        jsii_struct_bases=[],
        name_mapping={"tag_key": "tagKey", "tag_values": "tagValues"},
    )
    class LFTagProperty:
        def __init__(
            self,
            *,
            tag_key: typing.Optional[builtins.str] = None,
            tag_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The LF-tag key and values attached to a resource.

            :param tag_key: The key-name for the LF-tag.
            :param tag_values: A list of possible values of the corresponding ``TagKey`` of an LF-tag key-value pair.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftag.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                l_fTag_property = lakeformation.CfnPrincipalPermissions.LFTagProperty(
                    tag_key="tagKey",
                    tag_values=["tagValues"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bc281e3f1ec44de3ce5ecf6071d61be4884986556a50643b2eb54c6b136660e8)
                check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
                check_type(argname="argument tag_values", value=tag_values, expected_type=type_hints["tag_values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if tag_key is not None:
                self._values["tag_key"] = tag_key
            if tag_values is not None:
                self._values["tag_values"] = tag_values

        @builtins.property
        def tag_key(self) -> typing.Optional[builtins.str]:
            '''The key-name for the LF-tag.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftag.html#cfn-lakeformation-principalpermissions-lftag-tagkey
            '''
            result = self._values.get("tag_key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tag_values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of possible values of the corresponding ``TagKey`` of an LF-tag key-value pair.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftag.html#cfn-lakeformation-principalpermissions-lftag-tagvalues
            '''
            result = self._values.get("tag_values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LFTagProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPrincipalPermissions.ResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog": "catalog",
            "database": "database",
            "data_cells_filter": "dataCellsFilter",
            "data_location": "dataLocation",
            "lf_tag": "lfTag",
            "lf_tag_policy": "lfTagPolicy",
            "table": "table",
            "table_with_columns": "tableWithColumns",
        },
    )
    class ResourceProperty:
        def __init__(
            self,
            *,
            catalog: typing.Any = None,
            database: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPrincipalPermissions.DatabaseResourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            data_cells_filter: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPrincipalPermissions.DataCellsFilterResourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            data_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPrincipalPermissions.DataLocationResourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            lf_tag: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPrincipalPermissions.LFTagKeyResourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            lf_tag_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPrincipalPermissions.LFTagPolicyResourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            table: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPrincipalPermissions.TableResourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            table_with_columns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPrincipalPermissions.TableWithColumnsResourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A structure for the resource.

            :param catalog: The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.
            :param database: The database for the resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database permissions to a principal.
            :param data_cells_filter: A data cell filter.
            :param data_location: The location of an Amazon S3 path where permissions are granted or revoked.
            :param lf_tag: The LF-tag key and values attached to a resource.
            :param lf_tag_policy: A list of LF-tag conditions that define a resource's LF-tag policy.
            :param table: The table for the resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.
            :param table_with_columns: The table with columns for the resource. A principal with permissions to this resource can select metadata from the columns of a table in the Data Catalog and the underlying data in Amazon S3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                # catalog: Any
                # table_wildcard: Any
                
                resource_property = lakeformation.CfnPrincipalPermissions.ResourceProperty(
                    catalog=catalog,
                    database=lakeformation.CfnPrincipalPermissions.DatabaseResourceProperty(
                        catalog_id="catalogId",
                        name="name"
                    ),
                    data_cells_filter=lakeformation.CfnPrincipalPermissions.DataCellsFilterResourceProperty(
                        database_name="databaseName",
                        name="name",
                        table_catalog_id="tableCatalogId",
                        table_name="tableName"
                    ),
                    data_location=lakeformation.CfnPrincipalPermissions.DataLocationResourceProperty(
                        catalog_id="catalogId",
                        resource_arn="resourceArn"
                    ),
                    lf_tag=lakeformation.CfnPrincipalPermissions.LFTagKeyResourceProperty(
                        catalog_id="catalogId",
                        tag_key="tagKey",
                        tag_values=["tagValues"]
                    ),
                    lf_tag_policy=lakeformation.CfnPrincipalPermissions.LFTagPolicyResourceProperty(
                        catalog_id="catalogId",
                        expression=[lakeformation.CfnPrincipalPermissions.LFTagProperty(
                            tag_key="tagKey",
                            tag_values=["tagValues"]
                        )],
                        resource_type="resourceType"
                    ),
                    table=lakeformation.CfnPrincipalPermissions.TableResourceProperty(
                        catalog_id="catalogId",
                        database_name="databaseName",
                
                        # the properties below are optional
                        name="name",
                        table_wildcard=table_wildcard
                    ),
                    table_with_columns=lakeformation.CfnPrincipalPermissions.TableWithColumnsResourceProperty(
                        catalog_id="catalogId",
                        database_name="databaseName",
                        name="name",
                
                        # the properties below are optional
                        column_names=["columnNames"],
                        column_wildcard=lakeformation.CfnPrincipalPermissions.ColumnWildcardProperty(
                            excluded_column_names=["excludedColumnNames"]
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e592c3f53e78e6beb0a0b9195318c2f90921f0d62b7646b0963a8f90306a02df)
                check_type(argname="argument catalog", value=catalog, expected_type=type_hints["catalog"])
                check_type(argname="argument database", value=database, expected_type=type_hints["database"])
                check_type(argname="argument data_cells_filter", value=data_cells_filter, expected_type=type_hints["data_cells_filter"])
                check_type(argname="argument data_location", value=data_location, expected_type=type_hints["data_location"])
                check_type(argname="argument lf_tag", value=lf_tag, expected_type=type_hints["lf_tag"])
                check_type(argname="argument lf_tag_policy", value=lf_tag_policy, expected_type=type_hints["lf_tag_policy"])
                check_type(argname="argument table", value=table, expected_type=type_hints["table"])
                check_type(argname="argument table_with_columns", value=table_with_columns, expected_type=type_hints["table_with_columns"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if catalog is not None:
                self._values["catalog"] = catalog
            if database is not None:
                self._values["database"] = database
            if data_cells_filter is not None:
                self._values["data_cells_filter"] = data_cells_filter
            if data_location is not None:
                self._values["data_location"] = data_location
            if lf_tag is not None:
                self._values["lf_tag"] = lf_tag
            if lf_tag_policy is not None:
                self._values["lf_tag_policy"] = lf_tag_policy
            if table is not None:
                self._values["table"] = table
            if table_with_columns is not None:
                self._values["table_with_columns"] = table_with_columns

        @builtins.property
        def catalog(self) -> typing.Any:
            '''The identifier for the Data Catalog.

            By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html#cfn-lakeformation-principalpermissions-resource-catalog
            '''
            result = self._values.get("catalog")
            return typing.cast(typing.Any, result)

        @builtins.property
        def database(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPrincipalPermissions.DatabaseResourceProperty"]]:
            '''The database for the resource.

            Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database permissions to a principal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html#cfn-lakeformation-principalpermissions-resource-database
            '''
            result = self._values.get("database")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPrincipalPermissions.DatabaseResourceProperty"]], result)

        @builtins.property
        def data_cells_filter(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPrincipalPermissions.DataCellsFilterResourceProperty"]]:
            '''A data cell filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html#cfn-lakeformation-principalpermissions-resource-datacellsfilter
            '''
            result = self._values.get("data_cells_filter")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPrincipalPermissions.DataCellsFilterResourceProperty"]], result)

        @builtins.property
        def data_location(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPrincipalPermissions.DataLocationResourceProperty"]]:
            '''The location of an Amazon S3 path where permissions are granted or revoked.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html#cfn-lakeformation-principalpermissions-resource-datalocation
            '''
            result = self._values.get("data_location")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPrincipalPermissions.DataLocationResourceProperty"]], result)

        @builtins.property
        def lf_tag(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPrincipalPermissions.LFTagKeyResourceProperty"]]:
            '''The LF-tag key and values attached to a resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html#cfn-lakeformation-principalpermissions-resource-lftag
            '''
            result = self._values.get("lf_tag")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPrincipalPermissions.LFTagKeyResourceProperty"]], result)

        @builtins.property
        def lf_tag_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPrincipalPermissions.LFTagPolicyResourceProperty"]]:
            '''A list of LF-tag conditions that define a resource's LF-tag policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html#cfn-lakeformation-principalpermissions-resource-lftagpolicy
            '''
            result = self._values.get("lf_tag_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPrincipalPermissions.LFTagPolicyResourceProperty"]], result)

        @builtins.property
        def table(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPrincipalPermissions.TableResourceProperty"]]:
            '''The table for the resource.

            A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html#cfn-lakeformation-principalpermissions-resource-table
            '''
            result = self._values.get("table")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPrincipalPermissions.TableResourceProperty"]], result)

        @builtins.property
        def table_with_columns(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPrincipalPermissions.TableWithColumnsResourceProperty"]]:
            '''The table with columns for the resource.

            A principal with permissions to this resource can select metadata from the columns of a table in the Data Catalog and the underlying data in Amazon S3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html#cfn-lakeformation-principalpermissions-resource-tablewithcolumns
            '''
            result = self._values.get("table_with_columns")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPrincipalPermissions.TableWithColumnsResourceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPrincipalPermissions.TableResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "database_name": "databaseName",
            "name": "name",
            "table_wildcard": "tableWildcard",
        },
    )
    class TableResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: builtins.str,
            database_name: builtins.str,
            name: typing.Optional[builtins.str] = None,
            table_wildcard: typing.Any = None,
        ) -> None:
            '''A structure for the table object.

            A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

            :param catalog_id: 
            :param database_name: The name of the database for the table. Unique to a Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.
            :param name: The name of the table.
            :param table_wildcard: A wildcard object representing every table under a database. At least one of ``TableResource$Name`` or ``TableResource$TableWildcard`` is required.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tableresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                # table_wildcard: Any
                
                table_resource_property = lakeformation.CfnPrincipalPermissions.TableResourceProperty(
                    catalog_id="catalogId",
                    database_name="databaseName",
                
                    # the properties below are optional
                    name="name",
                    table_wildcard=table_wildcard
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__460697d12e9edf8f8a085b7d266b08a9ca2a4e1a30fba2179bbe92d989da93bc)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument table_wildcard", value=table_wildcard, expected_type=type_hints["table_wildcard"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "catalog_id": catalog_id,
                "database_name": database_name,
            }
            if name is not None:
                self._values["name"] = name
            if table_wildcard is not None:
                self._values["table_wildcard"] = table_wildcard

        @builtins.property
        def catalog_id(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tableresource.html#cfn-lakeformation-principalpermissions-tableresource-catalogid
            '''
            result = self._values.get("catalog_id")
            assert result is not None, "Required property 'catalog_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def database_name(self) -> builtins.str:
            '''The name of the database for the table.

            Unique to a Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tableresource.html#cfn-lakeformation-principalpermissions-tableresource-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tableresource.html#cfn-lakeformation-principalpermissions-tableresource-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def table_wildcard(self) -> typing.Any:
            '''A wildcard object representing every table under a database.

            At least one of ``TableResource$Name`` or ``TableResource$TableWildcard`` is required.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tableresource.html#cfn-lakeformation-principalpermissions-tableresource-tablewildcard
            '''
            result = self._values.get("table_wildcard")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TableResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnPrincipalPermissions.TableWithColumnsResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "database_name": "databaseName",
            "name": "name",
            "column_names": "columnNames",
            "column_wildcard": "columnWildcard",
        },
    )
    class TableWithColumnsResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: builtins.str,
            database_name: builtins.str,
            name: builtins.str,
            column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
            column_wildcard: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPrincipalPermissions.ColumnWildcardProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A structure for a table with columns object. This object is only used when granting a SELECT permission.

            This object must take a value for at least one of ``ColumnsNames`` , ``ColumnsIndexes`` , or ``ColumnsWildcard`` .

            :param catalog_id: The identifier for the Data Catalog where the location is registered with AWS Lake Formation .
            :param database_name: The name of the database for the table with columns resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.
            :param name: The name of the table resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.
            :param column_names: The list of column names for the table. At least one of ``ColumnNames`` or ``ColumnWildcard`` is required.
            :param column_wildcard: A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames`` or ``ColumnWildcard`` is required.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tablewithcolumnsresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                table_with_columns_resource_property = lakeformation.CfnPrincipalPermissions.TableWithColumnsResourceProperty(
                    catalog_id="catalogId",
                    database_name="databaseName",
                    name="name",
                
                    # the properties below are optional
                    column_names=["columnNames"],
                    column_wildcard=lakeformation.CfnPrincipalPermissions.ColumnWildcardProperty(
                        excluded_column_names=["excludedColumnNames"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__03b5f72824b5f84378a1881d387545e376b17c9fad070955cb027ed54682496f)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument column_names", value=column_names, expected_type=type_hints["column_names"])
                check_type(argname="argument column_wildcard", value=column_wildcard, expected_type=type_hints["column_wildcard"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "catalog_id": catalog_id,
                "database_name": database_name,
                "name": name,
            }
            if column_names is not None:
                self._values["column_names"] = column_names
            if column_wildcard is not None:
                self._values["column_wildcard"] = column_wildcard

        @builtins.property
        def catalog_id(self) -> builtins.str:
            '''The identifier for the Data Catalog where the location is registered with AWS Lake Formation .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tablewithcolumnsresource.html#cfn-lakeformation-principalpermissions-tablewithcolumnsresource-catalogid
            '''
            result = self._values.get("catalog_id")
            assert result is not None, "Required property 'catalog_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def database_name(self) -> builtins.str:
            '''The name of the database for the table with columns resource.

            Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tablewithcolumnsresource.html#cfn-lakeformation-principalpermissions-tablewithcolumnsresource-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the table resource.

            A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tablewithcolumnsresource.html#cfn-lakeformation-principalpermissions-tablewithcolumnsresource-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def column_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The list of column names for the table.

            At least one of ``ColumnNames`` or ``ColumnWildcard`` is required.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tablewithcolumnsresource.html#cfn-lakeformation-principalpermissions-tablewithcolumnsresource-columnnames
            '''
            result = self._values.get("column_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def column_wildcard(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPrincipalPermissions.ColumnWildcardProperty"]]:
            '''A wildcard specified by a ``ColumnWildcard`` object.

            At least one of ``ColumnNames`` or ``ColumnWildcard`` is required.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tablewithcolumnsresource.html#cfn-lakeformation-principalpermissions-tablewithcolumnsresource-columnwildcard
            '''
            result = self._values.get("column_wildcard")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPrincipalPermissions.ColumnWildcardProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TableWithColumnsResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lakeformation.CfnPrincipalPermissionsProps",
    jsii_struct_bases=[],
    name_mapping={
        "permissions": "permissions",
        "permissions_with_grant_option": "permissionsWithGrantOption",
        "principal": "principal",
        "resource": "resource",
        "catalog": "catalog",
    },
)
class CfnPrincipalPermissionsProps:
    def __init__(
        self,
        *,
        permissions: typing.Sequence[builtins.str],
        permissions_with_grant_option: typing.Sequence[builtins.str],
        principal: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPrincipalPermissions.DataLakePrincipalProperty, typing.Dict[builtins.str, typing.Any]]],
        resource: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPrincipalPermissions.ResourceProperty, typing.Dict[builtins.str, typing.Any]]],
        catalog: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnPrincipalPermissions``.

        :param permissions: The permissions granted or revoked.
        :param permissions_with_grant_option: Indicates the ability to grant permissions (as a subset of permissions granted).
        :param principal: The principal to be granted a permission.
        :param resource: The resource to be granted or revoked permissions.
        :param catalog: The identifier for the Data Catalog . By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lakeformation as lakeformation
            
            # catalog: Any
            # table_wildcard: Any
            
            cfn_principal_permissions_props = lakeformation.CfnPrincipalPermissionsProps(
                permissions=["permissions"],
                permissions_with_grant_option=["permissionsWithGrantOption"],
                principal=lakeformation.CfnPrincipalPermissions.DataLakePrincipalProperty(
                    data_lake_principal_identifier="dataLakePrincipalIdentifier"
                ),
                resource=lakeformation.CfnPrincipalPermissions.ResourceProperty(
                    catalog=catalog,
                    database=lakeformation.CfnPrincipalPermissions.DatabaseResourceProperty(
                        catalog_id="catalogId",
                        name="name"
                    ),
                    data_cells_filter=lakeformation.CfnPrincipalPermissions.DataCellsFilterResourceProperty(
                        database_name="databaseName",
                        name="name",
                        table_catalog_id="tableCatalogId",
                        table_name="tableName"
                    ),
                    data_location=lakeformation.CfnPrincipalPermissions.DataLocationResourceProperty(
                        catalog_id="catalogId",
                        resource_arn="resourceArn"
                    ),
                    lf_tag=lakeformation.CfnPrincipalPermissions.LFTagKeyResourceProperty(
                        catalog_id="catalogId",
                        tag_key="tagKey",
                        tag_values=["tagValues"]
                    ),
                    lf_tag_policy=lakeformation.CfnPrincipalPermissions.LFTagPolicyResourceProperty(
                        catalog_id="catalogId",
                        expression=[lakeformation.CfnPrincipalPermissions.LFTagProperty(
                            tag_key="tagKey",
                            tag_values=["tagValues"]
                        )],
                        resource_type="resourceType"
                    ),
                    table=lakeformation.CfnPrincipalPermissions.TableResourceProperty(
                        catalog_id="catalogId",
                        database_name="databaseName",
            
                        # the properties below are optional
                        name="name",
                        table_wildcard=table_wildcard
                    ),
                    table_with_columns=lakeformation.CfnPrincipalPermissions.TableWithColumnsResourceProperty(
                        catalog_id="catalogId",
                        database_name="databaseName",
                        name="name",
            
                        # the properties below are optional
                        column_names=["columnNames"],
                        column_wildcard=lakeformation.CfnPrincipalPermissions.ColumnWildcardProperty(
                            excluded_column_names=["excludedColumnNames"]
                        )
                    )
                ),
            
                # the properties below are optional
                catalog="catalog"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73e7e8136a697c9d74a8f4c0e960e0b7f194ff011d73f2543cdd3c12b2d90a89)
            check_type(argname="argument permissions", value=permissions, expected_type=type_hints["permissions"])
            check_type(argname="argument permissions_with_grant_option", value=permissions_with_grant_option, expected_type=type_hints["permissions_with_grant_option"])
            check_type(argname="argument principal", value=principal, expected_type=type_hints["principal"])
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
            check_type(argname="argument catalog", value=catalog, expected_type=type_hints["catalog"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "permissions": permissions,
            "permissions_with_grant_option": permissions_with_grant_option,
            "principal": principal,
            "resource": resource,
        }
        if catalog is not None:
            self._values["catalog"] = catalog

    @builtins.property
    def permissions(self) -> typing.List[builtins.str]:
        '''The permissions granted or revoked.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html#cfn-lakeformation-principalpermissions-permissions
        '''
        result = self._values.get("permissions")
        assert result is not None, "Required property 'permissions' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def permissions_with_grant_option(self) -> typing.List[builtins.str]:
        '''Indicates the ability to grant permissions (as a subset of permissions granted).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html#cfn-lakeformation-principalpermissions-permissionswithgrantoption
        '''
        result = self._values.get("permissions_with_grant_option")
        assert result is not None, "Required property 'permissions_with_grant_option' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def principal(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnPrincipalPermissions.DataLakePrincipalProperty]:
        '''The principal to be granted a permission.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html#cfn-lakeformation-principalpermissions-principal
        '''
        result = self._values.get("principal")
        assert result is not None, "Required property 'principal' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnPrincipalPermissions.DataLakePrincipalProperty], result)

    @builtins.property
    def resource(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnPrincipalPermissions.ResourceProperty]:
        '''The resource to be granted or revoked permissions.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html#cfn-lakeformation-principalpermissions-resource
        '''
        result = self._values.get("resource")
        assert result is not None, "Required property 'resource' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnPrincipalPermissions.ResourceProperty], result)

    @builtins.property
    def catalog(self) -> typing.Optional[builtins.str]:
        '''The identifier for the Data Catalog .

        By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html#cfn-lakeformation-principalpermissions-catalog
        '''
        result = self._values.get("catalog")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPrincipalPermissionsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnResource(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lakeformation.CfnResource",
):
    '''The ``AWS::LakeFormation::Resource`` represents the data (  buckets and folders) that is being registered with AWS Lake Formation .

    During a stack operation, AWS CloudFormation calls the AWS Lake Formation ```RegisterResource`` <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-credential-vending.html#aws-lake-formation-api-credential-vending-RegisterResource>`_ API operation to register the resource. To remove a ``Resource`` type, AWS CloudFormation calls the AWS Lake Formation ```DeregisterResource`` <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-credential-vending.html#aws-lake-formation-api-credential-vending-DeregisterResource>`_ API operation.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lakeformation as lakeformation
        
        cfn_resource = lakeformation.CfnResource(self, "MyCfnResource",
            resource_arn="resourceArn",
            use_service_linked_role=False,
        
            # the properties below are optional
            role_arn="roleArn",
            with_federation=False
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        resource_arn: builtins.str,
        use_service_linked_role: typing.Union[builtins.bool, _IResolvable_da3f097b],
        role_arn: typing.Optional[builtins.str] = None,
        with_federation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param resource_arn: The Amazon Resource Name (ARN) of the resource.
        :param use_service_linked_role: Designates a trusted caller, an IAM principal, by registering this caller with the Data Catalog .
        :param role_arn: The IAM role that registered a resource.
        :param with_federation: Allows Lake Formation to assume a role to access tables in a federated database.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77f160cc137d98ca347392fcb58c5f304f21bc0d6002a000296781efbc738d18)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResourceProps(
            resource_arn=resource_arn,
            use_service_linked_role=use_service_linked_role,
            role_arn=role_arn,
            with_federation=with_federation,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c6da1642c1089cadccd989e51a5e96bb970a8075cf3f6b966626c7f45b326a9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b3d3a65816f635df590bcd7d17914e0fdc91a78e7ee100e397268c2086de3767)
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
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the resource.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__350838b588f5ff4a75f92a0fcad91ca84447a413b308fa046a6cf1130366f421)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value)

    @builtins.property
    @jsii.member(jsii_name="useServiceLinkedRole")
    def use_service_linked_role(
        self,
    ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Designates a trusted caller, an IAM principal, by registering this caller with the Data Catalog .'''
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], jsii.get(self, "useServiceLinkedRole"))

    @use_service_linked_role.setter
    def use_service_linked_role(
        self,
        value: typing.Union[builtins.bool, _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__323f8924235b86ebffca643b12a93c3311bed500c9739d5c3c0662d0382eb023)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useServiceLinkedRole", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The IAM role that registered a resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8729c424eda1d70b20b2af7a8d47b5b0907bc502a826742bc55e79595b679331)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="withFederation")
    def with_federation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Allows Lake Formation to assume a role to access tables in a federated database.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "withFederation"))

    @with_federation.setter
    def with_federation(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43ad1f5c90ca783dfc3845f6c844b5bd7bae99947226262f5e38e22cd1781c80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "withFederation", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lakeformation.CfnResourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "resource_arn": "resourceArn",
        "use_service_linked_role": "useServiceLinkedRole",
        "role_arn": "roleArn",
        "with_federation": "withFederation",
    },
)
class CfnResourceProps:
    def __init__(
        self,
        *,
        resource_arn: builtins.str,
        use_service_linked_role: typing.Union[builtins.bool, _IResolvable_da3f097b],
        role_arn: typing.Optional[builtins.str] = None,
        with_federation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnResource``.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource.
        :param use_service_linked_role: Designates a trusted caller, an IAM principal, by registering this caller with the Data Catalog .
        :param role_arn: The IAM role that registered a resource.
        :param with_federation: Allows Lake Formation to assume a role to access tables in a federated database.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lakeformation as lakeformation
            
            cfn_resource_props = lakeformation.CfnResourceProps(
                resource_arn="resourceArn",
                use_service_linked_role=False,
            
                # the properties below are optional
                role_arn="roleArn",
                with_federation=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03d17976afc3de932d23406856f83d1dc703649c384d479735a5b9747442d0cb)
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            check_type(argname="argument use_service_linked_role", value=use_service_linked_role, expected_type=type_hints["use_service_linked_role"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument with_federation", value=with_federation, expected_type=type_hints["with_federation"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_arn": resource_arn,
            "use_service_linked_role": use_service_linked_role,
        }
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if with_federation is not None:
            self._values["with_federation"] = with_federation

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-resourcearn
        '''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def use_service_linked_role(
        self,
    ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Designates a trusted caller, an IAM principal, by registering this caller with the Data Catalog .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-useservicelinkedrole
        '''
        result = self._values.get("use_service_linked_role")
        assert result is not None, "Required property 'use_service_linked_role' is missing"
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The IAM role that registered a resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-rolearn
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def with_federation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Allows Lake Formation to assume a role to access tables in a federated database.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-withfederation
        '''
        result = self._values.get("with_federation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnTag(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lakeformation.CfnTag",
):
    '''The ``AWS::LakeFormation::Tag`` resource represents an LF-tag, which consists of a key and one or more possible values for the key.

    During a stack operation, AWS CloudFormation calls the AWS Lake Formation ``CreateLFTag`` API to create a tag, and ``UpdateLFTag`` API to update a tag resource, and a ``DeleteLFTag`` to delete it.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tag.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lakeformation as lakeformation
        
        cfn_tag = lakeformation.CfnTag(self, "MyCfnTag",
            tag_key="tagKey",
            tag_values=["tagValues"],
        
            # the properties below are optional
            catalog_id="catalogId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        tag_key: builtins.str,
        tag_values: typing.Sequence[builtins.str],
        catalog_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param tag_key: UTF-8 string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html>`_ . The key-name for the LF-tag.
        :param tag_values: An array of UTF-8 strings, not less than 1 or more than 50 strings. A list of possible values of the corresponding ``TagKey`` of an LF-tag key-value pair.
        :param catalog_id: Catalog id string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html>`_ . The identifier for the Data Catalog . By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ab4580d70a54262a22e42ccbe6c6594abcec37e5afe9b1cbfd0fd0418c59431)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTagProps(
            tag_key=tag_key, tag_values=tag_values, catalog_id=catalog_id
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47f77c7bbae5ea15c764cb3abc0b58d8d821b05b5a80784e220180cca6fe9b66)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d8b40d308d7873c493f391a63e731eda50f65145c94c11b22d61188745d1a945)
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
    @jsii.member(jsii_name="tagKey")
    def tag_key(self) -> builtins.str:
        '''UTF-8 string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html>`_ .'''
        return typing.cast(builtins.str, jsii.get(self, "tagKey"))

    @tag_key.setter
    def tag_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fbcb72975cf0ee3620990532676c33868b098cf53b559c6194a08d201b95f31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagKey", value)

    @builtins.property
    @jsii.member(jsii_name="tagValues")
    def tag_values(self) -> typing.List[builtins.str]:
        '''An array of UTF-8 strings, not less than 1 or more than 50 strings.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tagValues"))

    @tag_values.setter
    def tag_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80bb5fbcbd5307f3df5ee1986a32e2f5aae66630f974eb64d2978d496fdeae5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagValues", value)

    @builtins.property
    @jsii.member(jsii_name="catalogId")
    def catalog_id(self) -> typing.Optional[builtins.str]:
        '''Catalog id string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html>`_ .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalogId"))

    @catalog_id.setter
    def catalog_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eaa84342ed3778234e50b59a7902fe1ae5969963910f0840f7acd48fe3ca02c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogId", value)


@jsii.implements(_IInspectable_c2943556)
class CfnTagAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lakeformation.CfnTagAssociation",
):
    '''The ``AWS::LakeFormation::TagAssociation`` resource represents an assignment of an LF-tag to a Data Catalog resource (database, table, or column).

    During a stack operation, CloudFormation calls AWS Lake Formation ``AddLFTagsToResource`` API to create a ``TagAssociation`` resource and calls the ``RemoveLFTagsToResource`` API to delete it.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tagassociation.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lakeformation as lakeformation
        
        # catalog: Any
        # table_wildcard: Any
        
        cfn_tag_association = lakeformation.CfnTagAssociation(self, "MyCfnTagAssociation",
            lf_tags=[lakeformation.CfnTagAssociation.LFTagPairProperty(
                catalog_id="catalogId",
                tag_key="tagKey",
                tag_values=["tagValues"]
            )],
            resource=lakeformation.CfnTagAssociation.ResourceProperty(
                catalog=catalog,
                database=lakeformation.CfnTagAssociation.DatabaseResourceProperty(
                    catalog_id="catalogId",
                    name="name"
                ),
                table=lakeformation.CfnTagAssociation.TableResourceProperty(
                    catalog_id="catalogId",
                    database_name="databaseName",
        
                    # the properties below are optional
                    name="name",
                    table_wildcard=table_wildcard
                ),
                table_with_columns=lakeformation.CfnTagAssociation.TableWithColumnsResourceProperty(
                    catalog_id="catalogId",
                    column_names=["columnNames"],
                    database_name="databaseName",
                    name="name"
                )
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        lf_tags: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTagAssociation.LFTagPairProperty", typing.Dict[builtins.str, typing.Any]]]]],
        resource: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTagAssociation.ResourceProperty", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param lf_tags: A structure containing an LF-tag key-value pair.
        :param resource: UTF-8 string (valid values: ``DATABASE | TABLE`` ). The resource for which the LF-tag policy applies.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8acf5bb30936a1aadf20248378b13173f88c413c53b86f2704c297fa991785bc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTagAssociationProps(lf_tags=lf_tags, resource=resource)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00d30fbfb4d7717f03913b6b2047fe6cf92a306a188af90335580e81820be66c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f8f0ff7d007fdb5ff1ddd156412e54a73afa92ab5d67c2ab9a7462a935f46a2a)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrResourceIdentifier")
    def attr_resource_identifier(self) -> builtins.str:
        '''Json encoding of the input resource.

        **Examples** - Database: ``{"Catalog":null,"Database":{"CatalogId":"123456789012","Name":"ExampleDbName"},"Table":null,"TableWithColumns":null}``

        - Table: ``{"Catalog":null,"Database":null,"Table":{"CatalogId":"123456789012","DatabaseName":"ExampleDbName","Name":"ExampleTableName","TableWildcard":null},"TableWithColumns":null}``
        - Columns: ``{"Catalog":null,"Database":null,"Table":null,"TableWithColumns":{"CatalogId":"123456789012","DatabaseName":"ExampleDbName","Name":"ExampleTableName","ColumnNames":["ExampleColName1","ExampleColName2"]}}``

        :cloudformationAttribute: ResourceIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="attrTagsIdentifier")
    def attr_tags_identifier(self) -> builtins.str:
        '''Json encoding of the input LFTags list.

        For example: ``[{"CatalogId":null,"TagKey":"tagKey1","TagValues":null},{"CatalogId":null,"TagKey":"tagKey2","TagValues":null}]``

        :cloudformationAttribute: TagsIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTagsIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="lfTags")
    def lf_tags(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTagAssociation.LFTagPairProperty"]]]:
        '''A structure containing an LF-tag key-value pair.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTagAssociation.LFTagPairProperty"]]], jsii.get(self, "lfTags"))

    @lf_tags.setter
    def lf_tags(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTagAssociation.LFTagPairProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6d1db075ec83dde76f00266e6cddc3b420dada457caaa5e255b18058750a857)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lfTags", value)

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnTagAssociation.ResourceProperty"]:
        '''UTF-8 string (valid values: ``DATABASE | TABLE`` ).'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTagAssociation.ResourceProperty"], jsii.get(self, "resource"))

    @resource.setter
    def resource(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnTagAssociation.ResourceProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45383055be449cd404e72feac8314eeb81ef7af09ed2a6c6e17e69427732ffaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resource", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnTagAssociation.DatabaseResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"catalog_id": "catalogId", "name": "name"},
    )
    class DatabaseResourceProperty:
        def __init__(self, *, catalog_id: builtins.str, name: builtins.str) -> None:
            '''A structure for the database object.

            :param catalog_id: The identifier for the Data Catalog . By default, it should be the account ID of the caller.
            :param name: The name of the database resource. Unique to the Data Catalog.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-databaseresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                database_resource_property = lakeformation.CfnTagAssociation.DatabaseResourceProperty(
                    catalog_id="catalogId",
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cf7b16670051c00dca24a5e711cb16c069679831729ad63136417fa6945427e1)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "catalog_id": catalog_id,
                "name": name,
            }

        @builtins.property
        def catalog_id(self) -> builtins.str:
            '''The identifier for the Data Catalog .

            By default, it should be the account ID of the caller.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-databaseresource.html#cfn-lakeformation-tagassociation-databaseresource-catalogid
            '''
            result = self._values.get("catalog_id")
            assert result is not None, "Required property 'catalog_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the database resource.

            Unique to the Data Catalog.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-databaseresource.html#cfn-lakeformation-tagassociation-databaseresource-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatabaseResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnTagAssociation.LFTagPairProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "tag_key": "tagKey",
            "tag_values": "tagValues",
        },
    )
    class LFTagPairProperty:
        def __init__(
            self,
            *,
            catalog_id: builtins.str,
            tag_key: builtins.str,
            tag_values: typing.Sequence[builtins.str],
        ) -> None:
            '''A structure containing the catalog ID, tag key, and tag values of an LF-tag key-value pair.

            :param catalog_id: The identifier for the Data Catalog . By default, it is the account ID of the caller.
            :param tag_key: The key-name for the LF-tag.
            :param tag_values: A list of possible values of the corresponding ``TagKey`` of an LF-tag key-value pair.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-lftagpair.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                l_fTag_pair_property = lakeformation.CfnTagAssociation.LFTagPairProperty(
                    catalog_id="catalogId",
                    tag_key="tagKey",
                    tag_values=["tagValues"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__24d317a6afba0c688fa3e820b1a80b841aa146ae55a11f9764e992bb67b53e6a)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
                check_type(argname="argument tag_values", value=tag_values, expected_type=type_hints["tag_values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "catalog_id": catalog_id,
                "tag_key": tag_key,
                "tag_values": tag_values,
            }

        @builtins.property
        def catalog_id(self) -> builtins.str:
            '''The identifier for the Data Catalog .

            By default, it is the account ID of the caller.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-lftagpair.html#cfn-lakeformation-tagassociation-lftagpair-catalogid
            '''
            result = self._values.get("catalog_id")
            assert result is not None, "Required property 'catalog_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def tag_key(self) -> builtins.str:
            '''The key-name for the LF-tag.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-lftagpair.html#cfn-lakeformation-tagassociation-lftagpair-tagkey
            '''
            result = self._values.get("tag_key")
            assert result is not None, "Required property 'tag_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def tag_values(self) -> typing.List[builtins.str]:
            '''A list of possible values of the corresponding ``TagKey`` of an LF-tag key-value pair.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-lftagpair.html#cfn-lakeformation-tagassociation-lftagpair-tagvalues
            '''
            result = self._values.get("tag_values")
            assert result is not None, "Required property 'tag_values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LFTagPairProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnTagAssociation.ResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog": "catalog",
            "database": "database",
            "table": "table",
            "table_with_columns": "tableWithColumns",
        },
    )
    class ResourceProperty:
        def __init__(
            self,
            *,
            catalog: typing.Any = None,
            database: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTagAssociation.DatabaseResourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            table: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTagAssociation.TableResourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            table_with_columns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTagAssociation.TableWithColumnsResourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A structure for the resource.

            :param catalog: The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.
            :param database: The database for the resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database permissions to a principal.
            :param table: The table for the resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.
            :param table_with_columns: The table with columns for the resource. A principal with permissions to this resource can select metadata from the columns of a table in the Data Catalog and the underlying data in Amazon S3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-resource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                # catalog: Any
                # table_wildcard: Any
                
                resource_property = lakeformation.CfnTagAssociation.ResourceProperty(
                    catalog=catalog,
                    database=lakeformation.CfnTagAssociation.DatabaseResourceProperty(
                        catalog_id="catalogId",
                        name="name"
                    ),
                    table=lakeformation.CfnTagAssociation.TableResourceProperty(
                        catalog_id="catalogId",
                        database_name="databaseName",
                
                        # the properties below are optional
                        name="name",
                        table_wildcard=table_wildcard
                    ),
                    table_with_columns=lakeformation.CfnTagAssociation.TableWithColumnsResourceProperty(
                        catalog_id="catalogId",
                        column_names=["columnNames"],
                        database_name="databaseName",
                        name="name"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__771be53d4223909a565deac2ac8cca767eba62a46e3a94374ec9c62981bfe3f4)
                check_type(argname="argument catalog", value=catalog, expected_type=type_hints["catalog"])
                check_type(argname="argument database", value=database, expected_type=type_hints["database"])
                check_type(argname="argument table", value=table, expected_type=type_hints["table"])
                check_type(argname="argument table_with_columns", value=table_with_columns, expected_type=type_hints["table_with_columns"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if catalog is not None:
                self._values["catalog"] = catalog
            if database is not None:
                self._values["database"] = database
            if table is not None:
                self._values["table"] = table
            if table_with_columns is not None:
                self._values["table_with_columns"] = table_with_columns

        @builtins.property
        def catalog(self) -> typing.Any:
            '''The identifier for the Data Catalog.

            By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-resource.html#cfn-lakeformation-tagassociation-resource-catalog
            '''
            result = self._values.get("catalog")
            return typing.cast(typing.Any, result)

        @builtins.property
        def database(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTagAssociation.DatabaseResourceProperty"]]:
            '''The database for the resource.

            Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database permissions to a principal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-resource.html#cfn-lakeformation-tagassociation-resource-database
            '''
            result = self._values.get("database")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTagAssociation.DatabaseResourceProperty"]], result)

        @builtins.property
        def table(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTagAssociation.TableResourceProperty"]]:
            '''The table for the resource.

            A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-resource.html#cfn-lakeformation-tagassociation-resource-table
            '''
            result = self._values.get("table")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTagAssociation.TableResourceProperty"]], result)

        @builtins.property
        def table_with_columns(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTagAssociation.TableWithColumnsResourceProperty"]]:
            '''The table with columns for the resource.

            A principal with permissions to this resource can select metadata from the columns of a table in the Data Catalog and the underlying data in Amazon S3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-resource.html#cfn-lakeformation-tagassociation-resource-tablewithcolumns
            '''
            result = self._values.get("table_with_columns")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTagAssociation.TableWithColumnsResourceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnTagAssociation.TableResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "database_name": "databaseName",
            "name": "name",
            "table_wildcard": "tableWildcard",
        },
    )
    class TableResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: builtins.str,
            database_name: builtins.str,
            name: typing.Optional[builtins.str] = None,
            table_wildcard: typing.Any = None,
        ) -> None:
            '''A structure for the table object.

            A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

            :param catalog_id: The identifier for the Data Catalog . By default, it is the account ID of the caller.
            :param database_name: The name of the database for the table. Unique to a Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.
            :param name: The name of the table.
            :param table_wildcard: A wildcard object representing every table under a database.This is an object with no properties that effectively behaves as a true or false depending on whether not it is passed as a parameter. The valid inputs for a property with this type in either yaml or json is null or {}. At least one of ``TableResource$Name`` or ``TableResource$TableWildcard`` is required.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tableresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                # table_wildcard: Any
                
                table_resource_property = lakeformation.CfnTagAssociation.TableResourceProperty(
                    catalog_id="catalogId",
                    database_name="databaseName",
                
                    # the properties below are optional
                    name="name",
                    table_wildcard=table_wildcard
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b74bf73d38244ebadbafb317c7161d0c2460899853927afac0594e09c3bd2b6b)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument table_wildcard", value=table_wildcard, expected_type=type_hints["table_wildcard"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "catalog_id": catalog_id,
                "database_name": database_name,
            }
            if name is not None:
                self._values["name"] = name
            if table_wildcard is not None:
                self._values["table_wildcard"] = table_wildcard

        @builtins.property
        def catalog_id(self) -> builtins.str:
            '''The identifier for the Data Catalog .

            By default, it is the account ID of the caller.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tableresource.html#cfn-lakeformation-tagassociation-tableresource-catalogid
            '''
            result = self._values.get("catalog_id")
            assert result is not None, "Required property 'catalog_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def database_name(self) -> builtins.str:
            '''The name of the database for the table.

            Unique to a Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tableresource.html#cfn-lakeformation-tagassociation-tableresource-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tableresource.html#cfn-lakeformation-tagassociation-tableresource-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def table_wildcard(self) -> typing.Any:
            '''A wildcard object representing every table under a database.This is an object with no properties that effectively behaves as a true or false depending on whether not it is passed as a parameter. The valid inputs for a property with this type in either yaml or json is null or {}.

            At least one of ``TableResource$Name`` or ``TableResource$TableWildcard`` is required.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tableresource.html#cfn-lakeformation-tagassociation-tableresource-tablewildcard
            '''
            result = self._values.get("table_wildcard")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TableResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lakeformation.CfnTagAssociation.TableWithColumnsResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "column_names": "columnNames",
            "database_name": "databaseName",
            "name": "name",
        },
    )
    class TableWithColumnsResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: builtins.str,
            column_names: typing.Sequence[builtins.str],
            database_name: builtins.str,
            name: builtins.str,
        ) -> None:
            '''A structure for a table with columns object. This object is only used when granting a SELECT permission.

            This object must take a value for at least one of ``ColumnsNames`` , ``ColumnsIndexes`` , or ``ColumnsWildcard`` .

            :param catalog_id: A wildcard object representing every table under a database. At least one of TableResource$Name or TableResource$TableWildcard is required.
            :param column_names: The list of column names for the table. At least one of ``ColumnNames`` or ``ColumnWildcard`` is required.
            :param database_name: The name of the database for the table with columns resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.
            :param name: The name of the table resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tablewithcolumnsresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lakeformation as lakeformation
                
                table_with_columns_resource_property = lakeformation.CfnTagAssociation.TableWithColumnsResourceProperty(
                    catalog_id="catalogId",
                    column_names=["columnNames"],
                    database_name="databaseName",
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dbfafd4ff73d1cb58139774825c816ddf21d5913087c696e01ca730edd773afc)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument column_names", value=column_names, expected_type=type_hints["column_names"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "catalog_id": catalog_id,
                "column_names": column_names,
                "database_name": database_name,
                "name": name,
            }

        @builtins.property
        def catalog_id(self) -> builtins.str:
            '''A wildcard object representing every table under a database.

            At least one of TableResource$Name or TableResource$TableWildcard is required.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tablewithcolumnsresource.html#cfn-lakeformation-tagassociation-tablewithcolumnsresource-catalogid
            '''
            result = self._values.get("catalog_id")
            assert result is not None, "Required property 'catalog_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def column_names(self) -> typing.List[builtins.str]:
            '''The list of column names for the table.

            At least one of ``ColumnNames`` or ``ColumnWildcard`` is required.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tablewithcolumnsresource.html#cfn-lakeformation-tagassociation-tablewithcolumnsresource-columnnames
            '''
            result = self._values.get("column_names")
            assert result is not None, "Required property 'column_names' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def database_name(self) -> builtins.str:
            '''The name of the database for the table with columns resource.

            Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tablewithcolumnsresource.html#cfn-lakeformation-tagassociation-tablewithcolumnsresource-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the table resource.

            A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tablewithcolumnsresource.html#cfn-lakeformation-tagassociation-tablewithcolumnsresource-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TableWithColumnsResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lakeformation.CfnTagAssociationProps",
    jsii_struct_bases=[],
    name_mapping={"lf_tags": "lfTags", "resource": "resource"},
)
class CfnTagAssociationProps:
    def __init__(
        self,
        *,
        lf_tags: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTagAssociation.LFTagPairProperty, typing.Dict[builtins.str, typing.Any]]]]],
        resource: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTagAssociation.ResourceProperty, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Properties for defining a ``CfnTagAssociation``.

        :param lf_tags: A structure containing an LF-tag key-value pair.
        :param resource: UTF-8 string (valid values: ``DATABASE | TABLE`` ). The resource for which the LF-tag policy applies.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tagassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lakeformation as lakeformation
            
            # catalog: Any
            # table_wildcard: Any
            
            cfn_tag_association_props = lakeformation.CfnTagAssociationProps(
                lf_tags=[lakeformation.CfnTagAssociation.LFTagPairProperty(
                    catalog_id="catalogId",
                    tag_key="tagKey",
                    tag_values=["tagValues"]
                )],
                resource=lakeformation.CfnTagAssociation.ResourceProperty(
                    catalog=catalog,
                    database=lakeformation.CfnTagAssociation.DatabaseResourceProperty(
                        catalog_id="catalogId",
                        name="name"
                    ),
                    table=lakeformation.CfnTagAssociation.TableResourceProperty(
                        catalog_id="catalogId",
                        database_name="databaseName",
            
                        # the properties below are optional
                        name="name",
                        table_wildcard=table_wildcard
                    ),
                    table_with_columns=lakeformation.CfnTagAssociation.TableWithColumnsResourceProperty(
                        catalog_id="catalogId",
                        column_names=["columnNames"],
                        database_name="databaseName",
                        name="name"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09609047193647568d1de78d490fc80cb1cdf61bef98c0fb3e950dab1637872c)
            check_type(argname="argument lf_tags", value=lf_tags, expected_type=type_hints["lf_tags"])
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "lf_tags": lf_tags,
            "resource": resource,
        }

    @builtins.property
    def lf_tags(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTagAssociation.LFTagPairProperty]]]:
        '''A structure containing an LF-tag key-value pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tagassociation.html#cfn-lakeformation-tagassociation-lftags
        '''
        result = self._values.get("lf_tags")
        assert result is not None, "Required property 'lf_tags' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTagAssociation.LFTagPairProperty]]], result)

    @builtins.property
    def resource(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnTagAssociation.ResourceProperty]:
        '''UTF-8 string (valid values: ``DATABASE | TABLE`` ).

        The resource for which the LF-tag policy applies.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tagassociation.html#cfn-lakeformation-tagassociation-resource
        '''
        result = self._values.get("resource")
        assert result is not None, "Required property 'resource' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnTagAssociation.ResourceProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTagAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lakeformation.CfnTagProps",
    jsii_struct_bases=[],
    name_mapping={
        "tag_key": "tagKey",
        "tag_values": "tagValues",
        "catalog_id": "catalogId",
    },
)
class CfnTagProps:
    def __init__(
        self,
        *,
        tag_key: builtins.str,
        tag_values: typing.Sequence[builtins.str],
        catalog_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnTag``.

        :param tag_key: UTF-8 string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html>`_ . The key-name for the LF-tag.
        :param tag_values: An array of UTF-8 strings, not less than 1 or more than 50 strings. A list of possible values of the corresponding ``TagKey`` of an LF-tag key-value pair.
        :param catalog_id: Catalog id string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html>`_ . The identifier for the Data Catalog . By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tag.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lakeformation as lakeformation
            
            cfn_tag_props = lakeformation.CfnTagProps(
                tag_key="tagKey",
                tag_values=["tagValues"],
            
                # the properties below are optional
                catalog_id="catalogId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__890263379fd065da90f35db0e5851466b70a7f3ccd4b91729cf24539c9e70fa6)
            check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
            check_type(argname="argument tag_values", value=tag_values, expected_type=type_hints["tag_values"])
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "tag_key": tag_key,
            "tag_values": tag_values,
        }
        if catalog_id is not None:
            self._values["catalog_id"] = catalog_id

    @builtins.property
    def tag_key(self) -> builtins.str:
        '''UTF-8 string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html>`_ .

        The key-name for the LF-tag.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tag.html#cfn-lakeformation-tag-tagkey
        '''
        result = self._values.get("tag_key")
        assert result is not None, "Required property 'tag_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tag_values(self) -> typing.List[builtins.str]:
        '''An array of UTF-8 strings, not less than 1 or more than 50 strings.

        A list of possible values of the corresponding ``TagKey`` of an LF-tag key-value pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tag.html#cfn-lakeformation-tag-tagvalues
        '''
        result = self._values.get("tag_values")
        assert result is not None, "Required property 'tag_values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def catalog_id(self) -> typing.Optional[builtins.str]:
        '''Catalog id string, not less than 1 or more than 255 bytes long, matching the `single-line string pattern <https://docs.aws.amazon.com/lake-formation/latest/dg/aws-lake-formation-api-aws-lake-formation-api-common.html>`_ .

        The identifier for the Data Catalog . By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tag.html#cfn-lakeformation-tag-catalogid
        '''
        result = self._values.get("catalog_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTagProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDataCellsFilter",
    "CfnDataCellsFilterProps",
    "CfnDataLakeSettings",
    "CfnDataLakeSettingsProps",
    "CfnPermissions",
    "CfnPermissionsProps",
    "CfnPrincipalPermissions",
    "CfnPrincipalPermissionsProps",
    "CfnResource",
    "CfnResourceProps",
    "CfnTag",
    "CfnTagAssociation",
    "CfnTagAssociationProps",
    "CfnTagProps",
]

publication.publish()

def _typecheckingstub__4a9e0f2e2c8572da6300632b42930370bb203310961a1d82af3036a8c04fd788(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    database_name: builtins.str,
    name: builtins.str,
    table_catalog_id: builtins.str,
    table_name: builtins.str,
    column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    column_wildcard: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataCellsFilter.ColumnWildcardProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    row_filter: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataCellsFilter.RowFilterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ec2c4ae3e05879746cc41d6b7ec6a03ba20902ffc48bd129aa397d1d5a70e7e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7550823f808ffe201e6847b495d6892ddb995ec5519cee9493e2f6a540da733(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc93dcc91058f9885e949d095cb9cbd4ebbf83657aef2c98bdbd7642aa2b641f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48e194f3f5e117b948f5fd8f39a3c23624f934ba178488c21dcbeb47739eb3d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a2c891466da3cee74414ca67472fd45c6fe92a42dbf54f91e90276b9db4a09d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b9edb03eab58adb69826ccb4eeac83e17f956f28af214b840626176e3b23986(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e63b539b5926a43d01e515712efb604ac6b3d1ede325bc1b9c5dffd65f6b333c(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24e7504a12b1b5d7e26809268009dbec0ff8e5b821de877742f07891ecfccf10(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataCellsFilter.ColumnWildcardProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9f504934d13512b5f3bc876387b568ad7594bcf89c9905c5e36a7ab25137e38(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataCellsFilter.RowFilterProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d84dab12def7ab74d756b3488b56485fbe9e3c5d2293a55ee2317a32e970e93a(
    *,
    excluded_column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7b949fde25ae1b3b377b26570479963a5dec16b47fe2674ce47b5ea088af049(
    *,
    all_rows_wildcard: typing.Any = None,
    filter_expression: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a431cb2c88a63c9acd6913435bb5a3f7e689fea9c26e811a77582b6774fc6a8(
    *,
    database_name: builtins.str,
    name: builtins.str,
    table_catalog_id: builtins.str,
    table_name: builtins.str,
    column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    column_wildcard: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataCellsFilter.ColumnWildcardProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    row_filter: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataCellsFilter.RowFilterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f70f29826d8a7fc5611588cb6eeb3680ada51f8de62dc227827dff9f54d92319(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    admins: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLakeSettings.DataLakePrincipalProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    allow_external_data_filtering: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    authorized_session_tag_value_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    create_database_default_permissions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLakeSettings.PrincipalPermissionsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    create_table_default_permissions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLakeSettings.PrincipalPermissionsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    external_data_filtering_allow_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLakeSettings.DataLakePrincipalProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    parameters: typing.Any = None,
    trusted_resource_owners: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45022e2f75497dc5031de0534471b774f37d3e0163dd1cf0944a879956918611(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__638c6babf62b74da5a2cf7141e8d1f010dd75138406d16700684bff77834fdb5(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df68ab1ab5b6831a2e0f48c47e111909fcae53ceb431cf9876b2a6b3ee4895a8(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataLakeSettings.DataLakePrincipalProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad4d063925881a74c4f1073af94f569441bb4b8f7c58ee42383196bbb4e64aad(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd0547c17046b539f4cc757ea06d70b24e27b41611578b3219bd0ca23fe6ecd0(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__436b96d2708f96f391be82ba6eaa6481bbecd3b17c06354069035866187d1b45(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataLakeSettings.PrincipalPermissionsProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60f9c70a917c1c3ef84f9fe5f53041f2cdd59022a7255ab1c017bbfc4891f92f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataLakeSettings.PrincipalPermissionsProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eeb2f0e282d2dada4492c1a03ccdd85cb8e0865b8f5fc9d4efeee92270845ca4(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataLakeSettings.DataLakePrincipalProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52aab4b55f0c39756a432c91d3eeabd5eb70c011e8f466df712c0d1151418341(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__674387b8d4744b1214561eb77053527136809ff4a2e9cd1a69f2ab7af63d2bce(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2170e5a67ab80501cee1e7b138e885605f96762aa99d98fe439758c186de8147(
    *,
    data_lake_principal_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71d0279f7a0c8de462002223da529999b8cfab83d83a4f5d4c771f0df4712e5f(
    *,
    permissions: typing.Sequence[builtins.str],
    principal: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLakeSettings.DataLakePrincipalProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dce55f2e750b8b606563ee8be454eb95ace369e90671114b454db63f0cc7613d(
    *,
    admins: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLakeSettings.DataLakePrincipalProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    allow_external_data_filtering: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    authorized_session_tag_value_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    create_database_default_permissions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLakeSettings.PrincipalPermissionsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    create_table_default_permissions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLakeSettings.PrincipalPermissionsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    external_data_filtering_allow_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLakeSettings.DataLakePrincipalProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    parameters: typing.Any = None,
    trusted_resource_owners: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66f9b8220129009f27ac675ce32ccf618706bd509a2bdf99308bcd0b7a7ecb36(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    data_lake_principal: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPermissions.DataLakePrincipalProperty, typing.Dict[builtins.str, typing.Any]]],
    resource: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPermissions.ResourceProperty, typing.Dict[builtins.str, typing.Any]]],
    permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
    permissions_with_grant_option: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e596145285f2a793cf97360dcf20f6bff154e42d413389fa60459a8fee6d280(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ee971ab2aceb77af8d182ab99af94a6965b16a2c3d0275e663cdf73637933bf(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b52466eba74fe39a155b91afd467a62a59fd8b7da0cdf280f844dfae547c7e88(
    value: typing.Union[_IResolvable_da3f097b, CfnPermissions.DataLakePrincipalProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a8d760390e3b2e9ed402ee340c7169bf72a75fca3b15a45103c7e0e6e61a5b9(
    value: typing.Union[_IResolvable_da3f097b, CfnPermissions.ResourceProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1c9d158fab35ea7c0a56ddd6ec2e6b9628418e53bc9a07544a2abaf1f18dacb(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81251fb4fda47174588bc5781a51e64b3d055e355f7a6b70ecb93007b4046366(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf52b2441eb8a74ff7018cce9b6068a2ae059867acbdf38dce8ace97c7cb1145(
    *,
    excluded_column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80d8592bcc661e98e594ef066a2f224d8bd0d848c79b77076a27b690bc10264a(
    *,
    data_lake_principal_identifier: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__143e8666ee32b6c4cfaf593713c8528521c39e68a778350ee9a6abbc28f00afd(
    *,
    catalog_id: typing.Optional[builtins.str] = None,
    s3_resource: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b97daaaad005292df9c62b56d08c4c1f07af2aa89f795fc5055f09c33dc04502(
    *,
    catalog_id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e873d4ebccabb106e53e74b5438b8f89e526a4874c703f025c42839ae30566d(
    *,
    database_resource: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPermissions.DatabaseResourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    data_location_resource: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPermissions.DataLocationResourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    table_resource: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPermissions.TableResourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    table_with_columns_resource: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPermissions.TableWithColumnsResourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25c68a645287e81e1ea32708958d371278c40c2510ffac671ba40eeea7fe444e(
    *,
    catalog_id: typing.Optional[builtins.str] = None,
    database_name: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    table_wildcard: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPermissions.TableWildcardProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd66e1173aa0d6dbdb98124297f83efdbc21cf4278fca711775ba212a19929c4(
    *,
    catalog_id: typing.Optional[builtins.str] = None,
    column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    column_wildcard: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPermissions.ColumnWildcardProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    database_name: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fb762048f92dd06746b23564061560f03db7ad3a9de2ed4abd1fe22d6b087f1(
    *,
    data_lake_principal: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPermissions.DataLakePrincipalProperty, typing.Dict[builtins.str, typing.Any]]],
    resource: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPermissions.ResourceProperty, typing.Dict[builtins.str, typing.Any]]],
    permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
    permissions_with_grant_option: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2eb5d81db38bf28121ba5fc7c8223b5f9b99138c19ff95a360f576c85eee776b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    permissions: typing.Sequence[builtins.str],
    permissions_with_grant_option: typing.Sequence[builtins.str],
    principal: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPrincipalPermissions.DataLakePrincipalProperty, typing.Dict[builtins.str, typing.Any]]],
    resource: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPrincipalPermissions.ResourceProperty, typing.Dict[builtins.str, typing.Any]]],
    catalog: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19bcd0e8fdbb5452a744983c0bca1e00952558553e30a4edad79228574b0871f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22b65ac740c32d3048bd381021c49a684f9331531de0a8d324a618515c95ed01(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f09e32f0f3382686a05ba58d341882cae134bae9543b28783028d3a2e39e825b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__209371d03e969c4e61d2a38660dbb7441ca9c5e81a7ef95333acdd87a14ddd0e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1a6247a71b5100a75980e912dd96720cd90892a708b86881a36004028079dd5(
    value: typing.Union[_IResolvable_da3f097b, CfnPrincipalPermissions.DataLakePrincipalProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2cdd4778f3b42b1dbeec69000654d251230f2d8c9b50b55439c66ca17567ad3(
    value: typing.Union[_IResolvable_da3f097b, CfnPrincipalPermissions.ResourceProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d30f0e637fa1c5ffeca70a22e3d7a1083c596f26d2b181bb4f54624dba336c8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c2462e1081a2c39e7bf1727f3edf2e24354c2a890e9dd0028ce66f6d0577e20(
    *,
    excluded_column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33ec037517e7c5996eee712eb67decb6b3d04aa964f155335bb0a4730b194be7(
    *,
    database_name: builtins.str,
    name: builtins.str,
    table_catalog_id: builtins.str,
    table_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de361ca366cfcbb9bf826b663d0cfa9926ca81d247442348669309b4fc05c64e(
    *,
    data_lake_principal_identifier: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ef403264bd2d9619e7538638731036dd217c08886e8a889112aaec3f409612f(
    *,
    catalog_id: builtins.str,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__140938f79b31a570727d46b681bf0dbe828eab77f52f9cdaa5caecbcf61c8537(
    *,
    catalog_id: builtins.str,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1609270b64a1dfa63f7d47e0aa35028ab7fe44e010c798dbfd732fe2815564f9(
    *,
    catalog_id: builtins.str,
    tag_key: builtins.str,
    tag_values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__283f469e66d16220abd50df44457c58f1e228a52182f63247acce003afecb253(
    *,
    catalog_id: builtins.str,
    expression: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPrincipalPermissions.LFTagProperty, typing.Dict[builtins.str, typing.Any]]]]],
    resource_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc281e3f1ec44de3ce5ecf6071d61be4884986556a50643b2eb54c6b136660e8(
    *,
    tag_key: typing.Optional[builtins.str] = None,
    tag_values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e592c3f53e78e6beb0a0b9195318c2f90921f0d62b7646b0963a8f90306a02df(
    *,
    catalog: typing.Any = None,
    database: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPrincipalPermissions.DatabaseResourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    data_cells_filter: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPrincipalPermissions.DataCellsFilterResourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    data_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPrincipalPermissions.DataLocationResourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    lf_tag: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPrincipalPermissions.LFTagKeyResourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    lf_tag_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPrincipalPermissions.LFTagPolicyResourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    table: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPrincipalPermissions.TableResourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    table_with_columns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPrincipalPermissions.TableWithColumnsResourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__460697d12e9edf8f8a085b7d266b08a9ca2a4e1a30fba2179bbe92d989da93bc(
    *,
    catalog_id: builtins.str,
    database_name: builtins.str,
    name: typing.Optional[builtins.str] = None,
    table_wildcard: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03b5f72824b5f84378a1881d387545e376b17c9fad070955cb027ed54682496f(
    *,
    catalog_id: builtins.str,
    database_name: builtins.str,
    name: builtins.str,
    column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    column_wildcard: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPrincipalPermissions.ColumnWildcardProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73e7e8136a697c9d74a8f4c0e960e0b7f194ff011d73f2543cdd3c12b2d90a89(
    *,
    permissions: typing.Sequence[builtins.str],
    permissions_with_grant_option: typing.Sequence[builtins.str],
    principal: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPrincipalPermissions.DataLakePrincipalProperty, typing.Dict[builtins.str, typing.Any]]],
    resource: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPrincipalPermissions.ResourceProperty, typing.Dict[builtins.str, typing.Any]]],
    catalog: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77f160cc137d98ca347392fcb58c5f304f21bc0d6002a000296781efbc738d18(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    resource_arn: builtins.str,
    use_service_linked_role: typing.Union[builtins.bool, _IResolvable_da3f097b],
    role_arn: typing.Optional[builtins.str] = None,
    with_federation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c6da1642c1089cadccd989e51a5e96bb970a8075cf3f6b966626c7f45b326a9(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3d3a65816f635df590bcd7d17914e0fdc91a78e7ee100e397268c2086de3767(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__350838b588f5ff4a75f92a0fcad91ca84447a413b308fa046a6cf1130366f421(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__323f8924235b86ebffca643b12a93c3311bed500c9739d5c3c0662d0382eb023(
    value: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8729c424eda1d70b20b2af7a8d47b5b0907bc502a826742bc55e79595b679331(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43ad1f5c90ca783dfc3845f6c844b5bd7bae99947226262f5e38e22cd1781c80(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03d17976afc3de932d23406856f83d1dc703649c384d479735a5b9747442d0cb(
    *,
    resource_arn: builtins.str,
    use_service_linked_role: typing.Union[builtins.bool, _IResolvable_da3f097b],
    role_arn: typing.Optional[builtins.str] = None,
    with_federation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ab4580d70a54262a22e42ccbe6c6594abcec37e5afe9b1cbfd0fd0418c59431(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    tag_key: builtins.str,
    tag_values: typing.Sequence[builtins.str],
    catalog_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47f77c7bbae5ea15c764cb3abc0b58d8d821b05b5a80784e220180cca6fe9b66(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8b40d308d7873c493f391a63e731eda50f65145c94c11b22d61188745d1a945(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fbcb72975cf0ee3620990532676c33868b098cf53b559c6194a08d201b95f31(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80bb5fbcbd5307f3df5ee1986a32e2f5aae66630f974eb64d2978d496fdeae5b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eaa84342ed3778234e50b59a7902fe1ae5969963910f0840f7acd48fe3ca02c6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8acf5bb30936a1aadf20248378b13173f88c413c53b86f2704c297fa991785bc(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    lf_tags: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTagAssociation.LFTagPairProperty, typing.Dict[builtins.str, typing.Any]]]]],
    resource: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTagAssociation.ResourceProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00d30fbfb4d7717f03913b6b2047fe6cf92a306a188af90335580e81820be66c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8f0ff7d007fdb5ff1ddd156412e54a73afa92ab5d67c2ab9a7462a935f46a2a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6d1db075ec83dde76f00266e6cddc3b420dada457caaa5e255b18058750a857(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTagAssociation.LFTagPairProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45383055be449cd404e72feac8314eeb81ef7af09ed2a6c6e17e69427732ffaf(
    value: typing.Union[_IResolvable_da3f097b, CfnTagAssociation.ResourceProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf7b16670051c00dca24a5e711cb16c069679831729ad63136417fa6945427e1(
    *,
    catalog_id: builtins.str,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24d317a6afba0c688fa3e820b1a80b841aa146ae55a11f9764e992bb67b53e6a(
    *,
    catalog_id: builtins.str,
    tag_key: builtins.str,
    tag_values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__771be53d4223909a565deac2ac8cca767eba62a46e3a94374ec9c62981bfe3f4(
    *,
    catalog: typing.Any = None,
    database: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTagAssociation.DatabaseResourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    table: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTagAssociation.TableResourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    table_with_columns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTagAssociation.TableWithColumnsResourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b74bf73d38244ebadbafb317c7161d0c2460899853927afac0594e09c3bd2b6b(
    *,
    catalog_id: builtins.str,
    database_name: builtins.str,
    name: typing.Optional[builtins.str] = None,
    table_wildcard: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbfafd4ff73d1cb58139774825c816ddf21d5913087c696e01ca730edd773afc(
    *,
    catalog_id: builtins.str,
    column_names: typing.Sequence[builtins.str],
    database_name: builtins.str,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09609047193647568d1de78d490fc80cb1cdf61bef98c0fb3e950dab1637872c(
    *,
    lf_tags: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTagAssociation.LFTagPairProperty, typing.Dict[builtins.str, typing.Any]]]]],
    resource: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTagAssociation.ResourceProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__890263379fd065da90f35db0e5851466b70a7f3ccd4b91729cf24539c9e70fa6(
    *,
    tag_key: builtins.str,
    tag_values: typing.Sequence[builtins.str],
    catalog_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
