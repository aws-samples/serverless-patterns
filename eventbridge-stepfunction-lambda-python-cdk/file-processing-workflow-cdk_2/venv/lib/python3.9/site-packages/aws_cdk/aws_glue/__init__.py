'''
# AWS Glue Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_glue as glue
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Glue construct libraries](https://constructs.dev/search?q=glue)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Glue resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Glue.html) directly.

> An experimental construct library for this service is available in preview. Since it is not stable yet, it is distributed
> as a separate package so that you can pin its version independently of the rest of the CDK. See the package:
>
> <span class="package-reference">@aws-cdk/aws-glue-alpha</span>

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Glue](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Glue.html).

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
class CfnClassifier(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_glue.CfnClassifier",
):
    '''The ``AWS::Glue::Classifier`` resource creates an AWS Glue classifier that categorizes data sources and specifies schemas.

    For more information, see `Adding Classifiers to a Crawler <https://docs.aws.amazon.com/glue/latest/dg/add-classifier.html>`_ and `Classifier Structure <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-classifiers.html#aws-glue-api-crawler-classifiers-Classifier>`_ in the *AWS Glue Developer Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-classifier.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_glue as glue
        
        cfn_classifier = glue.CfnClassifier(self, "MyCfnClassifier",
            csv_classifier=glue.CfnClassifier.CsvClassifierProperty(
                allow_single_column=False,
                contains_header="containsHeader",
                delimiter="delimiter",
                disable_value_trimming=False,
                header=["header"],
                name="name",
                quote_symbol="quoteSymbol"
            ),
            grok_classifier=glue.CfnClassifier.GrokClassifierProperty(
                classification="classification",
                grok_pattern="grokPattern",
        
                # the properties below are optional
                custom_patterns="customPatterns",
                name="name"
            ),
            json_classifier=glue.CfnClassifier.JsonClassifierProperty(
                json_path="jsonPath",
        
                # the properties below are optional
                name="name"
            ),
            xml_classifier=glue.CfnClassifier.XMLClassifierProperty(
                classification="classification",
                row_tag="rowTag",
        
                # the properties below are optional
                name="name"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        csv_classifier: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnClassifier.CsvClassifierProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        grok_classifier: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnClassifier.GrokClassifierProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        json_classifier: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnClassifier.JsonClassifierProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        xml_classifier: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnClassifier.XMLClassifierProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param csv_classifier: A classifier for comma-separated values (CSV).
        :param grok_classifier: A classifier that uses ``grok`` .
        :param json_classifier: A classifier for JSON content.
        :param xml_classifier: A classifier for XML content.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c31bd9435d221f14c31ca91edbb76c0650b44f88a5a16431a384ce5854e7dcad)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnClassifierProps(
            csv_classifier=csv_classifier,
            grok_classifier=grok_classifier,
            json_classifier=json_classifier,
            xml_classifier=xml_classifier,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e64f8d2a274e89a852157febbc2182dcdb6d685a9d95146fd826be8c2e235c78)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a98d3c148e3cc0a370f92962b0a2da4be9f04c87b7df15e7a8ef87c4ce340011)
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
    @jsii.member(jsii_name="csvClassifier")
    def csv_classifier(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnClassifier.CsvClassifierProperty"]]:
        '''A classifier for comma-separated values (CSV).'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnClassifier.CsvClassifierProperty"]], jsii.get(self, "csvClassifier"))

    @csv_classifier.setter
    def csv_classifier(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnClassifier.CsvClassifierProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5250a15edb331e6856f0a29ac71c9e1513817ae7d411a90f5455dc89a24868c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "csvClassifier", value)

    @builtins.property
    @jsii.member(jsii_name="grokClassifier")
    def grok_classifier(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnClassifier.GrokClassifierProperty"]]:
        '''A classifier that uses ``grok`` .'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnClassifier.GrokClassifierProperty"]], jsii.get(self, "grokClassifier"))

    @grok_classifier.setter
    def grok_classifier(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnClassifier.GrokClassifierProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e433b191953f00afa5a4fb4333937a124c4a4865d13433693cab445ff794619)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "grokClassifier", value)

    @builtins.property
    @jsii.member(jsii_name="jsonClassifier")
    def json_classifier(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnClassifier.JsonClassifierProperty"]]:
        '''A classifier for JSON content.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnClassifier.JsonClassifierProperty"]], jsii.get(self, "jsonClassifier"))

    @json_classifier.setter
    def json_classifier(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnClassifier.JsonClassifierProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a99cf38e8a5d3d6d2a91d7585371a72e04e5cab9a9dfbfba99cbaf227511f5ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jsonClassifier", value)

    @builtins.property
    @jsii.member(jsii_name="xmlClassifier")
    def xml_classifier(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnClassifier.XMLClassifierProperty"]]:
        '''A classifier for XML content.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnClassifier.XMLClassifierProperty"]], jsii.get(self, "xmlClassifier"))

    @xml_classifier.setter
    def xml_classifier(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnClassifier.XMLClassifierProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__204ba6e258d6c443b165b0772162d891e01db52b8bf7b049b0e9d4968dfbc7d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xmlClassifier", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnClassifier.CsvClassifierProperty",
        jsii_struct_bases=[],
        name_mapping={
            "allow_single_column": "allowSingleColumn",
            "contains_header": "containsHeader",
            "delimiter": "delimiter",
            "disable_value_trimming": "disableValueTrimming",
            "header": "header",
            "name": "name",
            "quote_symbol": "quoteSymbol",
        },
    )
    class CsvClassifierProperty:
        def __init__(
            self,
            *,
            allow_single_column: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            contains_header: typing.Optional[builtins.str] = None,
            delimiter: typing.Optional[builtins.str] = None,
            disable_value_trimming: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            header: typing.Optional[typing.Sequence[builtins.str]] = None,
            name: typing.Optional[builtins.str] = None,
            quote_symbol: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A classifier for custom ``CSV`` content.

            :param allow_single_column: Enables the processing of files that contain only one column.
            :param contains_header: Indicates whether the CSV file contains a header. A value of ``UNKNOWN`` specifies that the classifier will detect whether the CSV file contains headings. A value of ``PRESENT`` specifies that the CSV file contains headings. A value of ``ABSENT`` specifies that the CSV file does not contain headings.
            :param delimiter: A custom symbol to denote what separates each column entry in the row.
            :param disable_value_trimming: Specifies not to trim values before identifying the type of column values. The default value is ``true`` .
            :param header: A list of strings representing column names.
            :param name: The name of the classifier.
            :param quote_symbol: A custom symbol to denote what combines content into a single column value. It must be different from the column delimiter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-csvclassifier.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                csv_classifier_property = glue.CfnClassifier.CsvClassifierProperty(
                    allow_single_column=False,
                    contains_header="containsHeader",
                    delimiter="delimiter",
                    disable_value_trimming=False,
                    header=["header"],
                    name="name",
                    quote_symbol="quoteSymbol"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dd722ed29ebf9e1505b4d21b5e95cb0f8d4e96b052ed45a497086e92f8d1eb4c)
                check_type(argname="argument allow_single_column", value=allow_single_column, expected_type=type_hints["allow_single_column"])
                check_type(argname="argument contains_header", value=contains_header, expected_type=type_hints["contains_header"])
                check_type(argname="argument delimiter", value=delimiter, expected_type=type_hints["delimiter"])
                check_type(argname="argument disable_value_trimming", value=disable_value_trimming, expected_type=type_hints["disable_value_trimming"])
                check_type(argname="argument header", value=header, expected_type=type_hints["header"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument quote_symbol", value=quote_symbol, expected_type=type_hints["quote_symbol"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if allow_single_column is not None:
                self._values["allow_single_column"] = allow_single_column
            if contains_header is not None:
                self._values["contains_header"] = contains_header
            if delimiter is not None:
                self._values["delimiter"] = delimiter
            if disable_value_trimming is not None:
                self._values["disable_value_trimming"] = disable_value_trimming
            if header is not None:
                self._values["header"] = header
            if name is not None:
                self._values["name"] = name
            if quote_symbol is not None:
                self._values["quote_symbol"] = quote_symbol

        @builtins.property
        def allow_single_column(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Enables the processing of files that contain only one column.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-csvclassifier.html#cfn-glue-classifier-csvclassifier-allowsinglecolumn
            '''
            result = self._values.get("allow_single_column")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def contains_header(self) -> typing.Optional[builtins.str]:
            '''Indicates whether the CSV file contains a header.

            A value of ``UNKNOWN`` specifies that the classifier will detect whether the CSV file contains headings.

            A value of ``PRESENT`` specifies that the CSV file contains headings.

            A value of ``ABSENT`` specifies that the CSV file does not contain headings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-csvclassifier.html#cfn-glue-classifier-csvclassifier-containsheader
            '''
            result = self._values.get("contains_header")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def delimiter(self) -> typing.Optional[builtins.str]:
            '''A custom symbol to denote what separates each column entry in the row.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-csvclassifier.html#cfn-glue-classifier-csvclassifier-delimiter
            '''
            result = self._values.get("delimiter")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def disable_value_trimming(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies not to trim values before identifying the type of column values.

            The default value is ``true`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-csvclassifier.html#cfn-glue-classifier-csvclassifier-disablevaluetrimming
            '''
            result = self._values.get("disable_value_trimming")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def header(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of strings representing column names.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-csvclassifier.html#cfn-glue-classifier-csvclassifier-header
            '''
            result = self._values.get("header")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the classifier.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-csvclassifier.html#cfn-glue-classifier-csvclassifier-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def quote_symbol(self) -> typing.Optional[builtins.str]:
            '''A custom symbol to denote what combines content into a single column value.

            It must be different from the column delimiter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-csvclassifier.html#cfn-glue-classifier-csvclassifier-quotesymbol
            '''
            result = self._values.get("quote_symbol")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CsvClassifierProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnClassifier.GrokClassifierProperty",
        jsii_struct_bases=[],
        name_mapping={
            "classification": "classification",
            "grok_pattern": "grokPattern",
            "custom_patterns": "customPatterns",
            "name": "name",
        },
    )
    class GrokClassifierProperty:
        def __init__(
            self,
            *,
            classification: builtins.str,
            grok_pattern: builtins.str,
            custom_patterns: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A classifier that uses ``grok`` patterns.

            :param classification: An identifier of the data format that the classifier matches, such as Twitter, JSON, Omniture logs, and so on.
            :param grok_pattern: The grok pattern applied to a data store by this classifier. For more information, see built-in patterns in `Writing Custom Classifiers <https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html>`_ .
            :param custom_patterns: Optional custom grok patterns defined by this classifier. For more information, see custom patterns in `Writing Custom Classifiers <https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html>`_ .
            :param name: The name of the classifier.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-grokclassifier.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                grok_classifier_property = glue.CfnClassifier.GrokClassifierProperty(
                    classification="classification",
                    grok_pattern="grokPattern",
                
                    # the properties below are optional
                    custom_patterns="customPatterns",
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f202c9743be8e12fb8f1f3a29eafdc0152da5577c8be943f4da1e40c32ce952d)
                check_type(argname="argument classification", value=classification, expected_type=type_hints["classification"])
                check_type(argname="argument grok_pattern", value=grok_pattern, expected_type=type_hints["grok_pattern"])
                check_type(argname="argument custom_patterns", value=custom_patterns, expected_type=type_hints["custom_patterns"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "classification": classification,
                "grok_pattern": grok_pattern,
            }
            if custom_patterns is not None:
                self._values["custom_patterns"] = custom_patterns
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def classification(self) -> builtins.str:
            '''An identifier of the data format that the classifier matches, such as Twitter, JSON, Omniture logs, and so on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-grokclassifier.html#cfn-glue-classifier-grokclassifier-classification
            '''
            result = self._values.get("classification")
            assert result is not None, "Required property 'classification' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def grok_pattern(self) -> builtins.str:
            '''The grok pattern applied to a data store by this classifier.

            For more information, see built-in patterns in `Writing Custom Classifiers <https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-grokclassifier.html#cfn-glue-classifier-grokclassifier-grokpattern
            '''
            result = self._values.get("grok_pattern")
            assert result is not None, "Required property 'grok_pattern' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def custom_patterns(self) -> typing.Optional[builtins.str]:
            '''Optional custom grok patterns defined by this classifier.

            For more information, see custom patterns in `Writing Custom Classifiers <https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-grokclassifier.html#cfn-glue-classifier-grokclassifier-custompatterns
            '''
            result = self._values.get("custom_patterns")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the classifier.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-grokclassifier.html#cfn-glue-classifier-grokclassifier-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GrokClassifierProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnClassifier.JsonClassifierProperty",
        jsii_struct_bases=[],
        name_mapping={"json_path": "jsonPath", "name": "name"},
    )
    class JsonClassifierProperty:
        def __init__(
            self,
            *,
            json_path: builtins.str,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A classifier for ``JSON`` content.

            :param json_path: A ``JsonPath`` string defining the JSON data for the classifier to classify. AWS Glue supports a subset of ``JsonPath`` , as described in `Writing JsonPath Custom Classifiers <https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html#custom-classifier-json>`_ .
            :param name: The name of the classifier.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-jsonclassifier.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                json_classifier_property = glue.CfnClassifier.JsonClassifierProperty(
                    json_path="jsonPath",
                
                    # the properties below are optional
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a6b0562c401f5718be9d3ef21289193ef2c0168f41e441d7c38d624e0a079382)
                check_type(argname="argument json_path", value=json_path, expected_type=type_hints["json_path"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "json_path": json_path,
            }
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def json_path(self) -> builtins.str:
            '''A ``JsonPath`` string defining the JSON data for the classifier to classify.

            AWS Glue supports a subset of ``JsonPath`` , as described in `Writing JsonPath Custom Classifiers <https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html#custom-classifier-json>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-jsonclassifier.html#cfn-glue-classifier-jsonclassifier-jsonpath
            '''
            result = self._values.get("json_path")
            assert result is not None, "Required property 'json_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the classifier.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-jsonclassifier.html#cfn-glue-classifier-jsonclassifier-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JsonClassifierProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnClassifier.XMLClassifierProperty",
        jsii_struct_bases=[],
        name_mapping={
            "classification": "classification",
            "row_tag": "rowTag",
            "name": "name",
        },
    )
    class XMLClassifierProperty:
        def __init__(
            self,
            *,
            classification: builtins.str,
            row_tag: builtins.str,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A classifier for ``XML`` content.

            :param classification: An identifier of the data format that the classifier matches.
            :param row_tag: The XML tag designating the element that contains each record in an XML document being parsed. This can't identify a self-closing element (closed by ``/>`` ). An empty row element that contains only attributes can be parsed as long as it ends with a closing tag (for example, ``<row item_a="A" item_b="B"></row>`` is okay, but ``<row item_a="A" item_b="B" />`` is not).
            :param name: The name of the classifier.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-xmlclassifier.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                x_mLClassifier_property = glue.CfnClassifier.XMLClassifierProperty(
                    classification="classification",
                    row_tag="rowTag",
                
                    # the properties below are optional
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__094348bf3568d41b3cc714d3098201aa1e2ce70a5da5beedf13ad7647bdd439c)
                check_type(argname="argument classification", value=classification, expected_type=type_hints["classification"])
                check_type(argname="argument row_tag", value=row_tag, expected_type=type_hints["row_tag"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "classification": classification,
                "row_tag": row_tag,
            }
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def classification(self) -> builtins.str:
            '''An identifier of the data format that the classifier matches.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-xmlclassifier.html#cfn-glue-classifier-xmlclassifier-classification
            '''
            result = self._values.get("classification")
            assert result is not None, "Required property 'classification' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def row_tag(self) -> builtins.str:
            '''The XML tag designating the element that contains each record in an XML document being parsed.

            This can't identify a self-closing element (closed by ``/>`` ). An empty row element that contains only attributes can be parsed as long as it ends with a closing tag (for example, ``<row item_a="A" item_b="B"></row>`` is okay, but ``<row item_a="A" item_b="B" />`` is not).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-xmlclassifier.html#cfn-glue-classifier-xmlclassifier-rowtag
            '''
            result = self._values.get("row_tag")
            assert result is not None, "Required property 'row_tag' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the classifier.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-xmlclassifier.html#cfn-glue-classifier-xmlclassifier-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "XMLClassifierProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_glue.CfnClassifierProps",
    jsii_struct_bases=[],
    name_mapping={
        "csv_classifier": "csvClassifier",
        "grok_classifier": "grokClassifier",
        "json_classifier": "jsonClassifier",
        "xml_classifier": "xmlClassifier",
    },
)
class CfnClassifierProps:
    def __init__(
        self,
        *,
        csv_classifier: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnClassifier.CsvClassifierProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        grok_classifier: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnClassifier.GrokClassifierProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        json_classifier: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnClassifier.JsonClassifierProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        xml_classifier: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnClassifier.XMLClassifierProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnClassifier``.

        :param csv_classifier: A classifier for comma-separated values (CSV).
        :param grok_classifier: A classifier that uses ``grok`` .
        :param json_classifier: A classifier for JSON content.
        :param xml_classifier: A classifier for XML content.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-classifier.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_glue as glue
            
            cfn_classifier_props = glue.CfnClassifierProps(
                csv_classifier=glue.CfnClassifier.CsvClassifierProperty(
                    allow_single_column=False,
                    contains_header="containsHeader",
                    delimiter="delimiter",
                    disable_value_trimming=False,
                    header=["header"],
                    name="name",
                    quote_symbol="quoteSymbol"
                ),
                grok_classifier=glue.CfnClassifier.GrokClassifierProperty(
                    classification="classification",
                    grok_pattern="grokPattern",
            
                    # the properties below are optional
                    custom_patterns="customPatterns",
                    name="name"
                ),
                json_classifier=glue.CfnClassifier.JsonClassifierProperty(
                    json_path="jsonPath",
            
                    # the properties below are optional
                    name="name"
                ),
                xml_classifier=glue.CfnClassifier.XMLClassifierProperty(
                    classification="classification",
                    row_tag="rowTag",
            
                    # the properties below are optional
                    name="name"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f036110075bbf70f52e4d02f33e758480e5ed41c2ddf5774889968357c16fd9)
            check_type(argname="argument csv_classifier", value=csv_classifier, expected_type=type_hints["csv_classifier"])
            check_type(argname="argument grok_classifier", value=grok_classifier, expected_type=type_hints["grok_classifier"])
            check_type(argname="argument json_classifier", value=json_classifier, expected_type=type_hints["json_classifier"])
            check_type(argname="argument xml_classifier", value=xml_classifier, expected_type=type_hints["xml_classifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if csv_classifier is not None:
            self._values["csv_classifier"] = csv_classifier
        if grok_classifier is not None:
            self._values["grok_classifier"] = grok_classifier
        if json_classifier is not None:
            self._values["json_classifier"] = json_classifier
        if xml_classifier is not None:
            self._values["xml_classifier"] = xml_classifier

    @builtins.property
    def csv_classifier(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnClassifier.CsvClassifierProperty]]:
        '''A classifier for comma-separated values (CSV).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-classifier.html#cfn-glue-classifier-csvclassifier
        '''
        result = self._values.get("csv_classifier")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnClassifier.CsvClassifierProperty]], result)

    @builtins.property
    def grok_classifier(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnClassifier.GrokClassifierProperty]]:
        '''A classifier that uses ``grok`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-classifier.html#cfn-glue-classifier-grokclassifier
        '''
        result = self._values.get("grok_classifier")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnClassifier.GrokClassifierProperty]], result)

    @builtins.property
    def json_classifier(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnClassifier.JsonClassifierProperty]]:
        '''A classifier for JSON content.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-classifier.html#cfn-glue-classifier-jsonclassifier
        '''
        result = self._values.get("json_classifier")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnClassifier.JsonClassifierProperty]], result)

    @builtins.property
    def xml_classifier(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnClassifier.XMLClassifierProperty]]:
        '''A classifier for XML content.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-classifier.html#cfn-glue-classifier-xmlclassifier
        '''
        result = self._values.get("xml_classifier")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnClassifier.XMLClassifierProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClassifierProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnConnection(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_glue.CfnConnection",
):
    '''The ``AWS::Glue::Connection`` resource specifies an AWS Glue connection to a data source.

    For more information, see `Adding a Connection to Your Data Store <https://docs.aws.amazon.com/glue/latest/dg/populate-add-connection.html>`_ and `Connection Structure <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-connections.html#aws-glue-api-catalog-connections-Connection>`_ in the *AWS Glue Developer Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-connection.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_glue as glue
        
        # connection_properties: Any
        
        cfn_connection = glue.CfnConnection(self, "MyCfnConnection",
            catalog_id="catalogId",
            connection_input=glue.CfnConnection.ConnectionInputProperty(
                connection_type="connectionType",
        
                # the properties below are optional
                connection_properties=connection_properties,
                description="description",
                match_criteria=["matchCriteria"],
                name="name",
                physical_connection_requirements=glue.CfnConnection.PhysicalConnectionRequirementsProperty(
                    availability_zone="availabilityZone",
                    security_group_id_list=["securityGroupIdList"],
                    subnet_id="subnetId"
                )
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        catalog_id: builtins.str,
        connection_input: typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnection.ConnectionInputProperty", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param catalog_id: The ID of the data catalog to create the catalog object in. Currently, this should be the AWS account ID. .. epigraph:: To specify the account ID, you can use the ``Ref`` intrinsic function with the ``AWS::AccountId`` pseudo parameter. For example: ``!Ref AWS::AccountId`` .
        :param connection_input: The connection that you want to create.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed744b41db4675b65946b69de8e2f2df8beabc93f21d52abb4a5ce5d2e35d6e3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConnectionProps(
            catalog_id=catalog_id, connection_input=connection_input
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e547a83aa8b1312e498ca658e38bfef22a6326568f2ad4059850b9314ab882d7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__af52b4937be9d9e9227708cfce1a1bf8e680539b738b3353dbb661804261b361)
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
    @jsii.member(jsii_name="catalogId")
    def catalog_id(self) -> builtins.str:
        '''The ID of the data catalog to create the catalog object in.'''
        return typing.cast(builtins.str, jsii.get(self, "catalogId"))

    @catalog_id.setter
    def catalog_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d64fcdf69b5b53d13d7560a99def80cc1ea81eb69a521ae5d8d75a05c0f8be1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogId", value)

    @builtins.property
    @jsii.member(jsii_name="connectionInput")
    def connection_input(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnConnection.ConnectionInputProperty"]:
        '''The connection that you want to create.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnConnection.ConnectionInputProperty"], jsii.get(self, "connectionInput"))

    @connection_input.setter
    def connection_input(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnConnection.ConnectionInputProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3a76484105010dc758d81394f436d3461656f97faa1bf881b484b7db1731e0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionInput", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnConnection.ConnectionInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "connection_type": "connectionType",
            "connection_properties": "connectionProperties",
            "description": "description",
            "match_criteria": "matchCriteria",
            "name": "name",
            "physical_connection_requirements": "physicalConnectionRequirements",
        },
    )
    class ConnectionInputProperty:
        def __init__(
            self,
            *,
            connection_type: builtins.str,
            connection_properties: typing.Any = None,
            description: typing.Optional[builtins.str] = None,
            match_criteria: typing.Optional[typing.Sequence[builtins.str]] = None,
            name: typing.Optional[builtins.str] = None,
            physical_connection_requirements: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnection.PhysicalConnectionRequirementsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A structure that is used to specify a connection to create or update.

            :param connection_type: The type of the connection. Currently, these types are supported:. - ``JDBC`` - Designates a connection to a database through Java Database Connectivity (JDBC). ``JDBC`` Connections use the following ConnectionParameters. - Required: All of ( ``HOST`` , ``PORT`` , ``JDBC_ENGINE`` ) or ``JDBC_CONNECTION_URL`` . - Required: All of ( ``USERNAME`` , ``PASSWORD`` ) or ``SECRET_ID`` . - Optional: ``JDBC_ENFORCE_SSL`` , ``CUSTOM_JDBC_CERT`` , ``CUSTOM_JDBC_CERT_STRING`` , ``SKIP_CUSTOM_JDBC_CERT_VALIDATION`` . These parameters are used to configure SSL with JDBC. - ``KAFKA`` - Designates a connection to an Apache Kafka streaming platform. ``KAFKA`` Connections use the following ConnectionParameters. - Required: ``KAFKA_BOOTSTRAP_SERVERS`` . - Optional: ``KAFKA_SSL_ENABLED`` , ``KAFKA_CUSTOM_CERT`` , ``KAFKA_SKIP_CUSTOM_CERT_VALIDATION`` . These parameters are used to configure SSL with ``KAFKA`` . - Optional: ``KAFKA_CLIENT_KEYSTORE`` , ``KAFKA_CLIENT_KEYSTORE_PASSWORD`` , ``KAFKA_CLIENT_KEY_PASSWORD`` , ``ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD`` , ``ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD`` . These parameters are used to configure TLS client configuration with SSL in ``KAFKA`` . - Optional: ``KAFKA_SASL_MECHANISM`` . Can be specified as ``SCRAM-SHA-512`` , ``GSSAPI`` , or ``AWS_MSK_IAM`` . - Optional: ``KAFKA_SASL_SCRAM_USERNAME`` , ``KAFKA_SASL_SCRAM_PASSWORD`` , ``ENCRYPTED_KAFKA_SASL_SCRAM_PASSWORD`` . These parameters are used to configure SASL/SCRAM-SHA-512 authentication with ``KAFKA`` . - Optional: ``KAFKA_SASL_GSSAPI_KEYTAB`` , ``KAFKA_SASL_GSSAPI_KRB5_CONF`` , ``KAFKA_SASL_GSSAPI_SERVICE`` , ``KAFKA_SASL_GSSAPI_PRINCIPAL`` . These parameters are used to configure SASL/GSSAPI authentication with ``KAFKA`` . - ``MONGODB`` - Designates a connection to a MongoDB document database. ``MONGODB`` Connections use the following ConnectionParameters. - Required: ``CONNECTION_URL`` . - Required: All of ( ``USERNAME`` , ``PASSWORD`` ) or ``SECRET_ID`` . - ``NETWORK`` - Designates a network connection to a data source within an Amazon Virtual Private Cloud environment (Amazon VPC). ``NETWORK`` Connections do not require ConnectionParameters. Instead, provide a PhysicalConnectionRequirements. - ``MARKETPLACE`` - Uses configuration settings contained in a connector purchased from AWS Marketplace to read from and write to data stores that are not natively supported by AWS Glue . ``MARKETPLACE`` Connections use the following ConnectionParameters. - Required: ``CONNECTOR_TYPE`` , ``CONNECTOR_URL`` , ``CONNECTOR_CLASS_NAME`` , ``CONNECTION_URL`` . - Required for ``JDBC`` ``CONNECTOR_TYPE`` connections: All of ( ``USERNAME`` , ``PASSWORD`` ) or ``SECRET_ID`` . - ``CUSTOM`` - Uses configuration settings contained in a custom connector to read from and write to data stores that are not natively supported by AWS Glue . ``SFTP`` is not supported. For more information about how optional ConnectionProperties are used to configure features in AWS Glue , consult `AWS Glue connection properties <https://docs.aws.amazon.com/glue/latest/dg/connection-defining.html>`_ . For more information about how optional ConnectionProperties are used to configure features in AWS Glue Studio, consult `Using connectors and connections <https://docs.aws.amazon.com/glue/latest/ug/connectors-chapter.html>`_ .
            :param connection_properties: These key-value pairs define parameters for the connection.
            :param description: The description of the connection.
            :param match_criteria: A list of criteria that can be used in selecting this connection.
            :param name: The name of the connection. Connection will not function as expected without a name.
            :param physical_connection_requirements: A map of physical connection requirements, such as virtual private cloud (VPC) and ``SecurityGroup`` , that are needed to successfully make this connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-connection-connectioninput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                # connection_properties: Any
                
                connection_input_property = glue.CfnConnection.ConnectionInputProperty(
                    connection_type="connectionType",
                
                    # the properties below are optional
                    connection_properties=connection_properties,
                    description="description",
                    match_criteria=["matchCriteria"],
                    name="name",
                    physical_connection_requirements=glue.CfnConnection.PhysicalConnectionRequirementsProperty(
                        availability_zone="availabilityZone",
                        security_group_id_list=["securityGroupIdList"],
                        subnet_id="subnetId"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__74e68b34e0a01df244f744096d99b1ff48c5f31548a88acaaf6d555c46a2fb76)
                check_type(argname="argument connection_type", value=connection_type, expected_type=type_hints["connection_type"])
                check_type(argname="argument connection_properties", value=connection_properties, expected_type=type_hints["connection_properties"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument match_criteria", value=match_criteria, expected_type=type_hints["match_criteria"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument physical_connection_requirements", value=physical_connection_requirements, expected_type=type_hints["physical_connection_requirements"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "connection_type": connection_type,
            }
            if connection_properties is not None:
                self._values["connection_properties"] = connection_properties
            if description is not None:
                self._values["description"] = description
            if match_criteria is not None:
                self._values["match_criteria"] = match_criteria
            if name is not None:
                self._values["name"] = name
            if physical_connection_requirements is not None:
                self._values["physical_connection_requirements"] = physical_connection_requirements

        @builtins.property
        def connection_type(self) -> builtins.str:
            '''The type of the connection. Currently, these types are supported:.

            - ``JDBC`` - Designates a connection to a database through Java Database Connectivity (JDBC).

            ``JDBC`` Connections use the following ConnectionParameters.

            - Required: All of ( ``HOST`` , ``PORT`` , ``JDBC_ENGINE`` ) or ``JDBC_CONNECTION_URL`` .
            - Required: All of ( ``USERNAME`` , ``PASSWORD`` ) or ``SECRET_ID`` .
            - Optional: ``JDBC_ENFORCE_SSL`` , ``CUSTOM_JDBC_CERT`` , ``CUSTOM_JDBC_CERT_STRING`` , ``SKIP_CUSTOM_JDBC_CERT_VALIDATION`` . These parameters are used to configure SSL with JDBC.
            - ``KAFKA`` - Designates a connection to an Apache Kafka streaming platform.

            ``KAFKA`` Connections use the following ConnectionParameters.

            - Required: ``KAFKA_BOOTSTRAP_SERVERS`` .
            - Optional: ``KAFKA_SSL_ENABLED`` , ``KAFKA_CUSTOM_CERT`` , ``KAFKA_SKIP_CUSTOM_CERT_VALIDATION`` . These parameters are used to configure SSL with ``KAFKA`` .
            - Optional: ``KAFKA_CLIENT_KEYSTORE`` , ``KAFKA_CLIENT_KEYSTORE_PASSWORD`` , ``KAFKA_CLIENT_KEY_PASSWORD`` , ``ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD`` , ``ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD`` . These parameters are used to configure TLS client configuration with SSL in ``KAFKA`` .
            - Optional: ``KAFKA_SASL_MECHANISM`` . Can be specified as ``SCRAM-SHA-512`` , ``GSSAPI`` , or ``AWS_MSK_IAM`` .
            - Optional: ``KAFKA_SASL_SCRAM_USERNAME`` , ``KAFKA_SASL_SCRAM_PASSWORD`` , ``ENCRYPTED_KAFKA_SASL_SCRAM_PASSWORD`` . These parameters are used to configure SASL/SCRAM-SHA-512 authentication with ``KAFKA`` .
            - Optional: ``KAFKA_SASL_GSSAPI_KEYTAB`` , ``KAFKA_SASL_GSSAPI_KRB5_CONF`` , ``KAFKA_SASL_GSSAPI_SERVICE`` , ``KAFKA_SASL_GSSAPI_PRINCIPAL`` . These parameters are used to configure SASL/GSSAPI authentication with ``KAFKA`` .
            - ``MONGODB`` - Designates a connection to a MongoDB document database.

            ``MONGODB`` Connections use the following ConnectionParameters.

            - Required: ``CONNECTION_URL`` .
            - Required: All of ( ``USERNAME`` , ``PASSWORD`` ) or ``SECRET_ID`` .
            - ``NETWORK`` - Designates a network connection to a data source within an Amazon Virtual Private Cloud environment (Amazon VPC).

            ``NETWORK`` Connections do not require ConnectionParameters. Instead, provide a PhysicalConnectionRequirements.

            - ``MARKETPLACE`` - Uses configuration settings contained in a connector purchased from AWS Marketplace to read from and write to data stores that are not natively supported by AWS Glue .

            ``MARKETPLACE`` Connections use the following ConnectionParameters.

            - Required: ``CONNECTOR_TYPE`` , ``CONNECTOR_URL`` , ``CONNECTOR_CLASS_NAME`` , ``CONNECTION_URL`` .
            - Required for ``JDBC`` ``CONNECTOR_TYPE`` connections: All of ( ``USERNAME`` , ``PASSWORD`` ) or ``SECRET_ID`` .
            - ``CUSTOM`` - Uses configuration settings contained in a custom connector to read from and write to data stores that are not natively supported by AWS Glue .

            ``SFTP`` is not supported.

            For more information about how optional ConnectionProperties are used to configure features in AWS Glue , consult `AWS Glue connection properties <https://docs.aws.amazon.com/glue/latest/dg/connection-defining.html>`_ .

            For more information about how optional ConnectionProperties are used to configure features in AWS Glue Studio, consult `Using connectors and connections <https://docs.aws.amazon.com/glue/latest/ug/connectors-chapter.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-connection-connectioninput.html#cfn-glue-connection-connectioninput-connectiontype
            '''
            result = self._values.get("connection_type")
            assert result is not None, "Required property 'connection_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def connection_properties(self) -> typing.Any:
            '''These key-value pairs define parameters for the connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-connection-connectioninput.html#cfn-glue-connection-connectioninput-connectionproperties
            '''
            result = self._values.get("connection_properties")
            return typing.cast(typing.Any, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The description of the connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-connection-connectioninput.html#cfn-glue-connection-connectioninput-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def match_criteria(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of criteria that can be used in selecting this connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-connection-connectioninput.html#cfn-glue-connection-connectioninput-matchcriteria
            '''
            result = self._values.get("match_criteria")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the connection.

            Connection will not function as expected without a name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-connection-connectioninput.html#cfn-glue-connection-connectioninput-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def physical_connection_requirements(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.PhysicalConnectionRequirementsProperty"]]:
            '''A map of physical connection requirements, such as virtual private cloud (VPC) and ``SecurityGroup`` , that are needed to successfully make this connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-connection-connectioninput.html#cfn-glue-connection-connectioninput-physicalconnectionrequirements
            '''
            result = self._values.get("physical_connection_requirements")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnection.PhysicalConnectionRequirementsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConnectionInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnConnection.PhysicalConnectionRequirementsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "availability_zone": "availabilityZone",
            "security_group_id_list": "securityGroupIdList",
            "subnet_id": "subnetId",
        },
    )
    class PhysicalConnectionRequirementsProperty:
        def __init__(
            self,
            *,
            availability_zone: typing.Optional[builtins.str] = None,
            security_group_id_list: typing.Optional[typing.Sequence[builtins.str]] = None,
            subnet_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the physical requirements for a connection.

            :param availability_zone: The connection's Availability Zone. This field is redundant because the specified subnet implies the Availability Zone to be used. Currently the field must be populated, but it will be deprecated in the future.
            :param security_group_id_list: The security group ID list used by the connection.
            :param subnet_id: The subnet ID used by the connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-connection-physicalconnectionrequirements.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                physical_connection_requirements_property = glue.CfnConnection.PhysicalConnectionRequirementsProperty(
                    availability_zone="availabilityZone",
                    security_group_id_list=["securityGroupIdList"],
                    subnet_id="subnetId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__40f33bb16819b03c45621bf4ec1060b418651be3dfd02f581f0cf1a6cd12cdb3)
                check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
                check_type(argname="argument security_group_id_list", value=security_group_id_list, expected_type=type_hints["security_group_id_list"])
                check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if availability_zone is not None:
                self._values["availability_zone"] = availability_zone
            if security_group_id_list is not None:
                self._values["security_group_id_list"] = security_group_id_list
            if subnet_id is not None:
                self._values["subnet_id"] = subnet_id

        @builtins.property
        def availability_zone(self) -> typing.Optional[builtins.str]:
            '''The connection's Availability Zone.

            This field is redundant because the specified subnet implies the Availability Zone to be used. Currently the field must be populated, but it will be deprecated in the future.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-connection-physicalconnectionrequirements.html#cfn-glue-connection-physicalconnectionrequirements-availabilityzone
            '''
            result = self._values.get("availability_zone")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def security_group_id_list(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The security group ID list used by the connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-connection-physicalconnectionrequirements.html#cfn-glue-connection-physicalconnectionrequirements-securitygroupidlist
            '''
            result = self._values.get("security_group_id_list")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def subnet_id(self) -> typing.Optional[builtins.str]:
            '''The subnet ID used by the connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-connection-physicalconnectionrequirements.html#cfn-glue-connection-physicalconnectionrequirements-subnetid
            '''
            result = self._values.get("subnet_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PhysicalConnectionRequirementsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_glue.CfnConnectionProps",
    jsii_struct_bases=[],
    name_mapping={"catalog_id": "catalogId", "connection_input": "connectionInput"},
)
class CfnConnectionProps:
    def __init__(
        self,
        *,
        catalog_id: builtins.str,
        connection_input: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnection.ConnectionInputProperty, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Properties for defining a ``CfnConnection``.

        :param catalog_id: The ID of the data catalog to create the catalog object in. Currently, this should be the AWS account ID. .. epigraph:: To specify the account ID, you can use the ``Ref`` intrinsic function with the ``AWS::AccountId`` pseudo parameter. For example: ``!Ref AWS::AccountId`` .
        :param connection_input: The connection that you want to create.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-connection.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_glue as glue
            
            # connection_properties: Any
            
            cfn_connection_props = glue.CfnConnectionProps(
                catalog_id="catalogId",
                connection_input=glue.CfnConnection.ConnectionInputProperty(
                    connection_type="connectionType",
            
                    # the properties below are optional
                    connection_properties=connection_properties,
                    description="description",
                    match_criteria=["matchCriteria"],
                    name="name",
                    physical_connection_requirements=glue.CfnConnection.PhysicalConnectionRequirementsProperty(
                        availability_zone="availabilityZone",
                        security_group_id_list=["securityGroupIdList"],
                        subnet_id="subnetId"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff86c0b8645eadb56850c28ce69021a78b30a75c13614c05815d7faf9f9f1eca)
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
            check_type(argname="argument connection_input", value=connection_input, expected_type=type_hints["connection_input"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "catalog_id": catalog_id,
            "connection_input": connection_input,
        }

    @builtins.property
    def catalog_id(self) -> builtins.str:
        '''The ID of the data catalog to create the catalog object in.

        Currently, this should be the AWS account ID.
        .. epigraph::

           To specify the account ID, you can use the ``Ref`` intrinsic function with the ``AWS::AccountId`` pseudo parameter. For example: ``!Ref AWS::AccountId`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-connection.html#cfn-glue-connection-catalogid
        '''
        result = self._values.get("catalog_id")
        assert result is not None, "Required property 'catalog_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connection_input(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnConnection.ConnectionInputProperty]:
        '''The connection that you want to create.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-connection.html#cfn-glue-connection-connectioninput
        '''
        result = self._values.get("connection_input")
        assert result is not None, "Required property 'connection_input' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnConnection.ConnectionInputProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConnectionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnCrawler(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_glue.CfnCrawler",
):
    '''The ``AWS::Glue::Crawler`` resource specifies an AWS Glue crawler.

    For more information, see `Cataloging Tables with a Crawler <https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html>`_ and `Crawler Structure <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-crawling.html#aws-glue-api-crawler-crawling-Crawler>`_ in the *AWS Glue Developer Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_glue as glue
        
        # tags: Any
        
        cfn_crawler = glue.CfnCrawler(self, "MyCfnCrawler",
            role="role",
            targets=glue.CfnCrawler.TargetsProperty(
                catalog_targets=[glue.CfnCrawler.CatalogTargetProperty(
                    connection_name="connectionName",
                    database_name="databaseName",
                    dlq_event_queue_arn="dlqEventQueueArn",
                    event_queue_arn="eventQueueArn",
                    tables=["tables"]
                )],
                delta_targets=[glue.CfnCrawler.DeltaTargetProperty(
                    connection_name="connectionName",
                    create_native_delta_table=False,
                    delta_tables=["deltaTables"],
                    write_manifest=False
                )],
                dynamo_db_targets=[glue.CfnCrawler.DynamoDBTargetProperty(
                    path="path"
                )],
                jdbc_targets=[glue.CfnCrawler.JdbcTargetProperty(
                    connection_name="connectionName",
                    exclusions=["exclusions"],
                    path="path"
                )],
                mongo_db_targets=[glue.CfnCrawler.MongoDBTargetProperty(
                    connection_name="connectionName",
                    path="path"
                )],
                s3_targets=[glue.CfnCrawler.S3TargetProperty(
                    connection_name="connectionName",
                    dlq_event_queue_arn="dlqEventQueueArn",
                    event_queue_arn="eventQueueArn",
                    exclusions=["exclusions"],
                    path="path",
                    sample_size=123
                )]
            ),
        
            # the properties below are optional
            classifiers=["classifiers"],
            configuration="configuration",
            crawler_security_configuration="crawlerSecurityConfiguration",
            database_name="databaseName",
            description="description",
            name="name",
            recrawl_policy=glue.CfnCrawler.RecrawlPolicyProperty(
                recrawl_behavior="recrawlBehavior"
            ),
            schedule=glue.CfnCrawler.ScheduleProperty(
                schedule_expression="scheduleExpression"
            ),
            schema_change_policy=glue.CfnCrawler.SchemaChangePolicyProperty(
                delete_behavior="deleteBehavior",
                update_behavior="updateBehavior"
            ),
            table_prefix="tablePrefix",
            tags=tags
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        role: builtins.str,
        targets: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCrawler.TargetsProperty", typing.Dict[builtins.str, typing.Any]]],
        classifiers: typing.Optional[typing.Sequence[builtins.str]] = None,
        configuration: typing.Optional[builtins.str] = None,
        crawler_security_configuration: typing.Optional[builtins.str] = None,
        database_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        recrawl_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCrawler.RecrawlPolicyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCrawler.ScheduleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        schema_change_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCrawler.SchemaChangePolicyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        table_prefix: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param role: The Amazon Resource Name (ARN) of an IAM role that's used to access customer resources, such as Amazon Simple Storage Service (Amazon S3) data.
        :param targets: A collection of targets to crawl.
        :param classifiers: A list of UTF-8 strings that specify the names of custom classifiers that are associated with the crawler.
        :param configuration: Crawler configuration information. This versioned JSON string allows users to specify aspects of a crawler's behavior. For more information, see `Configuring a Crawler <https://docs.aws.amazon.com/glue/latest/dg/crawler-configuration.html>`_ .
        :param crawler_security_configuration: The name of the ``SecurityConfiguration`` structure to be used by this crawler.
        :param database_name: The name of the database in which the crawler's output is stored.
        :param description: A description of the crawler.
        :param name: The name of the crawler.
        :param recrawl_policy: A policy that specifies whether to crawl the entire dataset again, or to crawl only folders that were added since the last crawler run.
        :param schedule: For scheduled crawlers, the schedule when the crawler runs.
        :param schema_change_policy: The policy that specifies update and delete behaviors for the crawler. The policy tells the crawler what to do in the event that it detects a change in a table that already exists in the customer's database at the time of the crawl. The ``SchemaChangePolicy`` does not affect whether or how new tables and partitions are added. New tables and partitions are always created regardless of the ``SchemaChangePolicy`` on a crawler. The SchemaChangePolicy consists of two components, ``UpdateBehavior`` and ``DeleteBehavior`` .
        :param table_prefix: The prefix added to the names of tables that are created.
        :param tags: The tags to use with this crawler.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff9e598239ccebeecff8b5e3f5f0458f9de0c5c407db27837fb3122adfbb48ec)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCrawlerProps(
            role=role,
            targets=targets,
            classifiers=classifiers,
            configuration=configuration,
            crawler_security_configuration=crawler_security_configuration,
            database_name=database_name,
            description=description,
            name=name,
            recrawl_policy=recrawl_policy,
            schedule=schedule,
            schema_change_policy=schema_change_policy,
            table_prefix=table_prefix,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c4320c740e3b9cb750745ec213ccc0ddab6c6f8d0fb2cc3678b58a5eb96963b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6ba899fc83e9439ba1eeaaf05c1cdb7db00223ee9639e5684b994ecbeecdba12)
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
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of an IAM role that's used to access customer resources, such as Amazon Simple Storage Service (Amazon S3) data.'''
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d0f4795e30bdf52af75380422e6956fe78ac8cabb8c11c0f4d1f4c6efa13a72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value)

    @builtins.property
    @jsii.member(jsii_name="targets")
    def targets(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnCrawler.TargetsProperty"]:
        '''A collection of targets to crawl.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCrawler.TargetsProperty"], jsii.get(self, "targets"))

    @targets.setter
    def targets(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnCrawler.TargetsProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8f17e8d0442485526676f5689364bcd775336febf0f27ff8adca3138ea4323d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targets", value)

    @builtins.property
    @jsii.member(jsii_name="classifiers")
    def classifiers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of UTF-8 strings that specify the names of custom classifiers that are associated with the crawler.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "classifiers"))

    @classifiers.setter
    def classifiers(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc97ff23bae45ac9e65f21fa1ea785f07dad693833d84e93e2d73c22f67659d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "classifiers", value)

    @builtins.property
    @jsii.member(jsii_name="configuration")
    def configuration(self) -> typing.Optional[builtins.str]:
        '''Crawler configuration information.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__192c642ccc1851982655e5d714a44522ea0ae0644693504905373aeb461e6710)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuration", value)

    @builtins.property
    @jsii.member(jsii_name="crawlerSecurityConfiguration")
    def crawler_security_configuration(self) -> typing.Optional[builtins.str]:
        '''The name of the ``SecurityConfiguration`` structure to be used by this crawler.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "crawlerSecurityConfiguration"))

    @crawler_security_configuration.setter
    def crawler_security_configuration(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad2cd3791a15d37fb39d53dc3e9305c735cef04bef3c2bcd36f656e2e3d9a727)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "crawlerSecurityConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> typing.Optional[builtins.str]:
        '''The name of the database in which the crawler's output is stored.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c0bced28b99cf5d6601a1e7268fb7fc84fbb7db6c55eb201f867678b9006fa8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the crawler.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55e97c90536e63620917a74b9e753f3ef37d2ba4cc78a367b3c2692a6a9073d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the crawler.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35986739065f4f5528fa36a3a4743b76eb0937d555e5d7ad917e107db84e9d92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="recrawlPolicy")
    def recrawl_policy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCrawler.RecrawlPolicyProperty"]]:
        '''A policy that specifies whether to crawl the entire dataset again, or to crawl only folders that were added since the last crawler run.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCrawler.RecrawlPolicyProperty"]], jsii.get(self, "recrawlPolicy"))

    @recrawl_policy.setter
    def recrawl_policy(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCrawler.RecrawlPolicyProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83e372f1422865065a5a3898b76f8c4b4c2b501fffdd71b9c7bc33febbb10363)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recrawlPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCrawler.ScheduleProperty"]]:
        '''For scheduled crawlers, the schedule when the crawler runs.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCrawler.ScheduleProperty"]], jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCrawler.ScheduleProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57543db817586f6f96b889ad18bd67740cd8212822395c2ef09e8dfcd0130552)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedule", value)

    @builtins.property
    @jsii.member(jsii_name="schemaChangePolicy")
    def schema_change_policy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCrawler.SchemaChangePolicyProperty"]]:
        '''The policy that specifies update and delete behaviors for the crawler.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCrawler.SchemaChangePolicyProperty"]], jsii.get(self, "schemaChangePolicy"))

    @schema_change_policy.setter
    def schema_change_policy(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCrawler.SchemaChangePolicyProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14e3cba92ee30f03751c9fb3a0546500940820fefc42b0c7c3c2bc17bd5773b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaChangePolicy", value)

    @builtins.property
    @jsii.member(jsii_name="tablePrefix")
    def table_prefix(self) -> typing.Optional[builtins.str]:
        '''The prefix added to the names of tables that are created.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tablePrefix"))

    @table_prefix.setter
    def table_prefix(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49ba3e782c84d62bea6d1f3c7f0c9468d3b13099042cf162e2e35456bf59a264)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tablePrefix", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Any:
        '''The tags to use with this crawler.'''
        return typing.cast(typing.Any, jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43760f25278105b8154c121bf9dd9dcaa617159cbb1a2a43fedb1312640eb5a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnCrawler.CatalogTargetProperty",
        jsii_struct_bases=[],
        name_mapping={
            "connection_name": "connectionName",
            "database_name": "databaseName",
            "dlq_event_queue_arn": "dlqEventQueueArn",
            "event_queue_arn": "eventQueueArn",
            "tables": "tables",
        },
    )
    class CatalogTargetProperty:
        def __init__(
            self,
            *,
            connection_name: typing.Optional[builtins.str] = None,
            database_name: typing.Optional[builtins.str] = None,
            dlq_event_queue_arn: typing.Optional[builtins.str] = None,
            event_queue_arn: typing.Optional[builtins.str] = None,
            tables: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Specifies an AWS Glue Data Catalog target.

            :param connection_name: The name of the connection for an Amazon S3-backed Data Catalog table to be a target of the crawl when using a ``Catalog`` connection type paired with a ``NETWORK`` Connection type.
            :param database_name: The name of the database to be synchronized.
            :param dlq_event_queue_arn: A valid Amazon dead-letter SQS ARN. For example, ``arn:aws:sqs:region:account:deadLetterQueue`` .
            :param event_queue_arn: A valid Amazon SQS ARN. For example, ``arn:aws:sqs:region:account:sqs`` .
            :param tables: A list of the tables to be synchronized.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-catalogtarget.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                catalog_target_property = glue.CfnCrawler.CatalogTargetProperty(
                    connection_name="connectionName",
                    database_name="databaseName",
                    dlq_event_queue_arn="dlqEventQueueArn",
                    event_queue_arn="eventQueueArn",
                    tables=["tables"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f163f3382b5ca5c3414fe2db6d7ec2500afa6a106f4cda66075603ccfa491c62)
                check_type(argname="argument connection_name", value=connection_name, expected_type=type_hints["connection_name"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument dlq_event_queue_arn", value=dlq_event_queue_arn, expected_type=type_hints["dlq_event_queue_arn"])
                check_type(argname="argument event_queue_arn", value=event_queue_arn, expected_type=type_hints["event_queue_arn"])
                check_type(argname="argument tables", value=tables, expected_type=type_hints["tables"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if connection_name is not None:
                self._values["connection_name"] = connection_name
            if database_name is not None:
                self._values["database_name"] = database_name
            if dlq_event_queue_arn is not None:
                self._values["dlq_event_queue_arn"] = dlq_event_queue_arn
            if event_queue_arn is not None:
                self._values["event_queue_arn"] = event_queue_arn
            if tables is not None:
                self._values["tables"] = tables

        @builtins.property
        def connection_name(self) -> typing.Optional[builtins.str]:
            '''The name of the connection for an Amazon S3-backed Data Catalog table to be a target of the crawl when using a ``Catalog`` connection type paired with a ``NETWORK`` Connection type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-catalogtarget.html#cfn-glue-crawler-catalogtarget-connectionname
            '''
            result = self._values.get("connection_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def database_name(self) -> typing.Optional[builtins.str]:
            '''The name of the database to be synchronized.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-catalogtarget.html#cfn-glue-crawler-catalogtarget-databasename
            '''
            result = self._values.get("database_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dlq_event_queue_arn(self) -> typing.Optional[builtins.str]:
            '''A valid Amazon dead-letter SQS ARN.

            For example, ``arn:aws:sqs:region:account:deadLetterQueue`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-catalogtarget.html#cfn-glue-crawler-catalogtarget-dlqeventqueuearn
            '''
            result = self._values.get("dlq_event_queue_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def event_queue_arn(self) -> typing.Optional[builtins.str]:
            '''A valid Amazon SQS ARN.

            For example, ``arn:aws:sqs:region:account:sqs`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-catalogtarget.html#cfn-glue-crawler-catalogtarget-eventqueuearn
            '''
            result = self._values.get("event_queue_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tables(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of the tables to be synchronized.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-catalogtarget.html#cfn-glue-crawler-catalogtarget-tables
            '''
            result = self._values.get("tables")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CatalogTargetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnCrawler.DeltaTargetProperty",
        jsii_struct_bases=[],
        name_mapping={
            "connection_name": "connectionName",
            "create_native_delta_table": "createNativeDeltaTable",
            "delta_tables": "deltaTables",
            "write_manifest": "writeManifest",
        },
    )
    class DeltaTargetProperty:
        def __init__(
            self,
            *,
            connection_name: typing.Optional[builtins.str] = None,
            create_native_delta_table: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            delta_tables: typing.Optional[typing.Sequence[builtins.str]] = None,
            write_manifest: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Specifies a Delta data store to crawl one or more Delta tables.

            :param connection_name: The name of the connection to use to connect to the Delta table target.
            :param create_native_delta_table: Specifies whether the crawler will create native tables, to allow integration with query engines that support querying of the Delta transaction log directly.
            :param delta_tables: A list of the Amazon S3 paths to the Delta tables.
            :param write_manifest: Specifies whether to write the manifest files to the Delta table path.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-deltatarget.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                delta_target_property = glue.CfnCrawler.DeltaTargetProperty(
                    connection_name="connectionName",
                    create_native_delta_table=False,
                    delta_tables=["deltaTables"],
                    write_manifest=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a7510699883f74759e475bf2ece2842156b441164d538264f93242ebdacee3c2)
                check_type(argname="argument connection_name", value=connection_name, expected_type=type_hints["connection_name"])
                check_type(argname="argument create_native_delta_table", value=create_native_delta_table, expected_type=type_hints["create_native_delta_table"])
                check_type(argname="argument delta_tables", value=delta_tables, expected_type=type_hints["delta_tables"])
                check_type(argname="argument write_manifest", value=write_manifest, expected_type=type_hints["write_manifest"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if connection_name is not None:
                self._values["connection_name"] = connection_name
            if create_native_delta_table is not None:
                self._values["create_native_delta_table"] = create_native_delta_table
            if delta_tables is not None:
                self._values["delta_tables"] = delta_tables
            if write_manifest is not None:
                self._values["write_manifest"] = write_manifest

        @builtins.property
        def connection_name(self) -> typing.Optional[builtins.str]:
            '''The name of the connection to use to connect to the Delta table target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-deltatarget.html#cfn-glue-crawler-deltatarget-connectionname
            '''
            result = self._values.get("connection_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def create_native_delta_table(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether the crawler will create native tables, to allow integration with query engines that support querying of the Delta transaction log directly.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-deltatarget.html#cfn-glue-crawler-deltatarget-createnativedeltatable
            '''
            result = self._values.get("create_native_delta_table")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def delta_tables(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of the Amazon S3 paths to the Delta tables.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-deltatarget.html#cfn-glue-crawler-deltatarget-deltatables
            '''
            result = self._values.get("delta_tables")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def write_manifest(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether to write the manifest files to the Delta table path.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-deltatarget.html#cfn-glue-crawler-deltatarget-writemanifest
            '''
            result = self._values.get("write_manifest")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeltaTargetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnCrawler.DynamoDBTargetProperty",
        jsii_struct_bases=[],
        name_mapping={"path": "path"},
    )
    class DynamoDBTargetProperty:
        def __init__(self, *, path: typing.Optional[builtins.str] = None) -> None:
            '''Specifies an Amazon DynamoDB table to crawl.

            :param path: The name of the DynamoDB table to crawl.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-dynamodbtarget.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                dynamo_dBTarget_property = glue.CfnCrawler.DynamoDBTargetProperty(
                    path="path"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4c03ffc3d1fa17ed9770b2c448e87c012b6d363001f06ce8b95bdb9c62711274)
                check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if path is not None:
                self._values["path"] = path

        @builtins.property
        def path(self) -> typing.Optional[builtins.str]:
            '''The name of the DynamoDB table to crawl.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-dynamodbtarget.html#cfn-glue-crawler-dynamodbtarget-path
            '''
            result = self._values.get("path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DynamoDBTargetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnCrawler.JdbcTargetProperty",
        jsii_struct_bases=[],
        name_mapping={
            "connection_name": "connectionName",
            "exclusions": "exclusions",
            "path": "path",
        },
    )
    class JdbcTargetProperty:
        def __init__(
            self,
            *,
            connection_name: typing.Optional[builtins.str] = None,
            exclusions: typing.Optional[typing.Sequence[builtins.str]] = None,
            path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies a JDBC data store to crawl.

            :param connection_name: The name of the connection to use to connect to the JDBC target.
            :param exclusions: A list of glob patterns used to exclude from the crawl. For more information, see `Catalog Tables with a Crawler <https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html>`_ .
            :param path: The path of the JDBC target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-jdbctarget.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                jdbc_target_property = glue.CfnCrawler.JdbcTargetProperty(
                    connection_name="connectionName",
                    exclusions=["exclusions"],
                    path="path"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9cb27c7db73a5c6fa3740f2d4726f453641d40911229d3bb39f26c4402516cf6)
                check_type(argname="argument connection_name", value=connection_name, expected_type=type_hints["connection_name"])
                check_type(argname="argument exclusions", value=exclusions, expected_type=type_hints["exclusions"])
                check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if connection_name is not None:
                self._values["connection_name"] = connection_name
            if exclusions is not None:
                self._values["exclusions"] = exclusions
            if path is not None:
                self._values["path"] = path

        @builtins.property
        def connection_name(self) -> typing.Optional[builtins.str]:
            '''The name of the connection to use to connect to the JDBC target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-jdbctarget.html#cfn-glue-crawler-jdbctarget-connectionname
            '''
            result = self._values.get("connection_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def exclusions(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of glob patterns used to exclude from the crawl.

            For more information, see `Catalog Tables with a Crawler <https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-jdbctarget.html#cfn-glue-crawler-jdbctarget-exclusions
            '''
            result = self._values.get("exclusions")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def path(self) -> typing.Optional[builtins.str]:
            '''The path of the JDBC target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-jdbctarget.html#cfn-glue-crawler-jdbctarget-path
            '''
            result = self._values.get("path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JdbcTargetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnCrawler.MongoDBTargetProperty",
        jsii_struct_bases=[],
        name_mapping={"connection_name": "connectionName", "path": "path"},
    )
    class MongoDBTargetProperty:
        def __init__(
            self,
            *,
            connection_name: typing.Optional[builtins.str] = None,
            path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies an Amazon DocumentDB or MongoDB data store to crawl.

            :param connection_name: The name of the connection to use to connect to the Amazon DocumentDB or MongoDB target.
            :param path: The path of the Amazon DocumentDB or MongoDB target (database/collection).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-mongodbtarget.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                mongo_dBTarget_property = glue.CfnCrawler.MongoDBTargetProperty(
                    connection_name="connectionName",
                    path="path"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b27a374f7da5948658852ac367f177b833b9e06c48e0a246c211a7d7ede3af94)
                check_type(argname="argument connection_name", value=connection_name, expected_type=type_hints["connection_name"])
                check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if connection_name is not None:
                self._values["connection_name"] = connection_name
            if path is not None:
                self._values["path"] = path

        @builtins.property
        def connection_name(self) -> typing.Optional[builtins.str]:
            '''The name of the connection to use to connect to the Amazon DocumentDB or MongoDB target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-mongodbtarget.html#cfn-glue-crawler-mongodbtarget-connectionname
            '''
            result = self._values.get("connection_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def path(self) -> typing.Optional[builtins.str]:
            '''The path of the Amazon DocumentDB or MongoDB target (database/collection).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-mongodbtarget.html#cfn-glue-crawler-mongodbtarget-path
            '''
            result = self._values.get("path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MongoDBTargetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnCrawler.RecrawlPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"recrawl_behavior": "recrawlBehavior"},
    )
    class RecrawlPolicyProperty:
        def __init__(
            self,
            *,
            recrawl_behavior: typing.Optional[builtins.str] = None,
        ) -> None:
            '''When crawling an Amazon S3 data source after the first crawl is complete, specifies whether to crawl the entire dataset again or to crawl only folders that were added since the last crawler run.

            For more information, see `Incremental Crawls in AWS Glue <https://docs.aws.amazon.com/glue/latest/dg/incremental-crawls.html>`_ in the developer guide.

            :param recrawl_behavior: Specifies whether to crawl the entire dataset again or to crawl only folders that were added since the last crawler run. A value of ``CRAWL_EVERYTHING`` specifies crawling the entire dataset again. A value of ``CRAWL_NEW_FOLDERS_ONLY`` specifies crawling only folders that were added since the last crawler run. A value of ``CRAWL_EVENT_MODE`` specifies crawling only the changes identified by Amazon S3 events.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-recrawlpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                recrawl_policy_property = glue.CfnCrawler.RecrawlPolicyProperty(
                    recrawl_behavior="recrawlBehavior"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e40a02828fa90824e4069120d7dbc0e3e1eccbd3e09087ff5c6bb9b3005e1f4e)
                check_type(argname="argument recrawl_behavior", value=recrawl_behavior, expected_type=type_hints["recrawl_behavior"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if recrawl_behavior is not None:
                self._values["recrawl_behavior"] = recrawl_behavior

        @builtins.property
        def recrawl_behavior(self) -> typing.Optional[builtins.str]:
            '''Specifies whether to crawl the entire dataset again or to crawl only folders that were added since the last crawler run.

            A value of ``CRAWL_EVERYTHING`` specifies crawling the entire dataset again.

            A value of ``CRAWL_NEW_FOLDERS_ONLY`` specifies crawling only folders that were added since the last crawler run.

            A value of ``CRAWL_EVENT_MODE`` specifies crawling only the changes identified by Amazon S3 events.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-recrawlpolicy.html#cfn-glue-crawler-recrawlpolicy-recrawlbehavior
            '''
            result = self._values.get("recrawl_behavior")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecrawlPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnCrawler.S3TargetProperty",
        jsii_struct_bases=[],
        name_mapping={
            "connection_name": "connectionName",
            "dlq_event_queue_arn": "dlqEventQueueArn",
            "event_queue_arn": "eventQueueArn",
            "exclusions": "exclusions",
            "path": "path",
            "sample_size": "sampleSize",
        },
    )
    class S3TargetProperty:
        def __init__(
            self,
            *,
            connection_name: typing.Optional[builtins.str] = None,
            dlq_event_queue_arn: typing.Optional[builtins.str] = None,
            event_queue_arn: typing.Optional[builtins.str] = None,
            exclusions: typing.Optional[typing.Sequence[builtins.str]] = None,
            path: typing.Optional[builtins.str] = None,
            sample_size: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Specifies a data store in Amazon Simple Storage Service (Amazon S3).

            :param connection_name: The name of a connection which allows a job or crawler to access data in Amazon S3 within an Amazon Virtual Private Cloud environment (Amazon VPC).
            :param dlq_event_queue_arn: A valid Amazon dead-letter SQS ARN. For example, ``arn:aws:sqs:region:account:deadLetterQueue`` .
            :param event_queue_arn: A valid Amazon SQS ARN. For example, ``arn:aws:sqs:region:account:sqs`` .
            :param exclusions: A list of glob patterns used to exclude from the crawl. For more information, see `Catalog Tables with a Crawler <https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html>`_ .
            :param path: The path to the Amazon S3 target.
            :param sample_size: Sets the number of files in each leaf folder to be crawled when crawling sample files in a dataset. If not set, all the files are crawled. A valid value is an integer between 1 and 249.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-s3target.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                s3_target_property = glue.CfnCrawler.S3TargetProperty(
                    connection_name="connectionName",
                    dlq_event_queue_arn="dlqEventQueueArn",
                    event_queue_arn="eventQueueArn",
                    exclusions=["exclusions"],
                    path="path",
                    sample_size=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4086580ebeb74fac287364f6cbdacc62bee81dd975f186a492fc80c7037071c8)
                check_type(argname="argument connection_name", value=connection_name, expected_type=type_hints["connection_name"])
                check_type(argname="argument dlq_event_queue_arn", value=dlq_event_queue_arn, expected_type=type_hints["dlq_event_queue_arn"])
                check_type(argname="argument event_queue_arn", value=event_queue_arn, expected_type=type_hints["event_queue_arn"])
                check_type(argname="argument exclusions", value=exclusions, expected_type=type_hints["exclusions"])
                check_type(argname="argument path", value=path, expected_type=type_hints["path"])
                check_type(argname="argument sample_size", value=sample_size, expected_type=type_hints["sample_size"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if connection_name is not None:
                self._values["connection_name"] = connection_name
            if dlq_event_queue_arn is not None:
                self._values["dlq_event_queue_arn"] = dlq_event_queue_arn
            if event_queue_arn is not None:
                self._values["event_queue_arn"] = event_queue_arn
            if exclusions is not None:
                self._values["exclusions"] = exclusions
            if path is not None:
                self._values["path"] = path
            if sample_size is not None:
                self._values["sample_size"] = sample_size

        @builtins.property
        def connection_name(self) -> typing.Optional[builtins.str]:
            '''The name of a connection which allows a job or crawler to access data in Amazon S3 within an Amazon Virtual Private Cloud environment (Amazon VPC).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-s3target.html#cfn-glue-crawler-s3target-connectionname
            '''
            result = self._values.get("connection_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dlq_event_queue_arn(self) -> typing.Optional[builtins.str]:
            '''A valid Amazon dead-letter SQS ARN.

            For example, ``arn:aws:sqs:region:account:deadLetterQueue`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-s3target.html#cfn-glue-crawler-s3target-dlqeventqueuearn
            '''
            result = self._values.get("dlq_event_queue_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def event_queue_arn(self) -> typing.Optional[builtins.str]:
            '''A valid Amazon SQS ARN.

            For example, ``arn:aws:sqs:region:account:sqs`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-s3target.html#cfn-glue-crawler-s3target-eventqueuearn
            '''
            result = self._values.get("event_queue_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def exclusions(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of glob patterns used to exclude from the crawl.

            For more information, see `Catalog Tables with a Crawler <https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-s3target.html#cfn-glue-crawler-s3target-exclusions
            '''
            result = self._values.get("exclusions")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def path(self) -> typing.Optional[builtins.str]:
            '''The path to the Amazon S3 target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-s3target.html#cfn-glue-crawler-s3target-path
            '''
            result = self._values.get("path")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sample_size(self) -> typing.Optional[jsii.Number]:
            '''Sets the number of files in each leaf folder to be crawled when crawling sample files in a dataset.

            If not set, all the files are crawled. A valid value is an integer between 1 and 249.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-s3target.html#cfn-glue-crawler-s3target-samplesize
            '''
            result = self._values.get("sample_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3TargetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnCrawler.ScheduleProperty",
        jsii_struct_bases=[],
        name_mapping={"schedule_expression": "scheduleExpression"},
    )
    class ScheduleProperty:
        def __init__(
            self,
            *,
            schedule_expression: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A scheduling object using a ``cron`` statement to schedule an event.

            :param schedule_expression: A ``cron`` expression used to specify the schedule. For more information, see `Time-Based Schedules for Jobs and Crawlers <https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`_ . For example, to run something every day at 12:15 UTC, specify ``cron(15 12 * * ? *)`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-schedule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                schedule_property = glue.CfnCrawler.ScheduleProperty(
                    schedule_expression="scheduleExpression"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__665dbaef4a9e75ff541ec9b561a356e92755d78e1a5d1701fa9004482f92ed7e)
                check_type(argname="argument schedule_expression", value=schedule_expression, expected_type=type_hints["schedule_expression"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if schedule_expression is not None:
                self._values["schedule_expression"] = schedule_expression

        @builtins.property
        def schedule_expression(self) -> typing.Optional[builtins.str]:
            '''A ``cron`` expression used to specify the schedule.

            For more information, see `Time-Based Schedules for Jobs and Crawlers <https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`_ . For example, to run something every day at 12:15 UTC, specify ``cron(15 12 * * ? *)`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-schedule.html#cfn-glue-crawler-schedule-scheduleexpression
            '''
            result = self._values.get("schedule_expression")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScheduleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnCrawler.SchemaChangePolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delete_behavior": "deleteBehavior",
            "update_behavior": "updateBehavior",
        },
    )
    class SchemaChangePolicyProperty:
        def __init__(
            self,
            *,
            delete_behavior: typing.Optional[builtins.str] = None,
            update_behavior: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The policy that specifies update and delete behaviors for the crawler.

            The policy tells the crawler what to do in the event that it detects a change in a table that already exists in the customer's database at the time of the crawl. The ``SchemaChangePolicy`` does not affect whether or how new tables and partitions are added. New tables and partitions are always created regardless of the ``SchemaChangePolicy`` on a crawler.

            The SchemaChangePolicy consists of two components, ``UpdateBehavior`` and ``DeleteBehavior`` .

            :param delete_behavior: The deletion behavior when the crawler finds a deleted object. A value of ``LOG`` specifies that if a table or partition is found to no longer exist, do not delete it, only log that it was found to no longer exist. A value of ``DELETE_FROM_DATABASE`` specifies that if a table or partition is found to have been removed, delete it from the database. A value of ``DEPRECATE_IN_DATABASE`` specifies that if a table has been found to no longer exist, to add a property to the table that says "DEPRECATED" and includes a timestamp with the time of deprecation.
            :param update_behavior: The update behavior when the crawler finds a changed schema. A value of ``LOG`` specifies that if a table or a partition already exists, and a change is detected, do not update it, only log that a change was detected. Add new tables and new partitions (including on existing tables). A value of ``UPDATE_IN_DATABASE`` specifies that if a table or partition already exists, and a change is detected, update it. Add new tables and partitions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-schemachangepolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                schema_change_policy_property = glue.CfnCrawler.SchemaChangePolicyProperty(
                    delete_behavior="deleteBehavior",
                    update_behavior="updateBehavior"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__75f9df7f7ba86ceb8199c254017b595776e141c4c4688a6f26f8b203f610a9fd)
                check_type(argname="argument delete_behavior", value=delete_behavior, expected_type=type_hints["delete_behavior"])
                check_type(argname="argument update_behavior", value=update_behavior, expected_type=type_hints["update_behavior"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if delete_behavior is not None:
                self._values["delete_behavior"] = delete_behavior
            if update_behavior is not None:
                self._values["update_behavior"] = update_behavior

        @builtins.property
        def delete_behavior(self) -> typing.Optional[builtins.str]:
            '''The deletion behavior when the crawler finds a deleted object.

            A value of ``LOG`` specifies that if a table or partition is found to no longer exist, do not delete it, only log that it was found to no longer exist.

            A value of ``DELETE_FROM_DATABASE`` specifies that if a table or partition is found to have been removed, delete it from the database.

            A value of ``DEPRECATE_IN_DATABASE`` specifies that if a table has been found to no longer exist, to add a property to the table that says "DEPRECATED" and includes a timestamp with the time of deprecation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-schemachangepolicy.html#cfn-glue-crawler-schemachangepolicy-deletebehavior
            '''
            result = self._values.get("delete_behavior")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def update_behavior(self) -> typing.Optional[builtins.str]:
            '''The update behavior when the crawler finds a changed schema.

            A value of ``LOG`` specifies that if a table or a partition already exists, and a change is detected, do not update it, only log that a change was detected. Add new tables and new partitions (including on existing tables).

            A value of ``UPDATE_IN_DATABASE`` specifies that if a table or partition already exists, and a change is detected, update it. Add new tables and partitions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-schemachangepolicy.html#cfn-glue-crawler-schemachangepolicy-updatebehavior
            '''
            result = self._values.get("update_behavior")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SchemaChangePolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnCrawler.TargetsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_targets": "catalogTargets",
            "delta_targets": "deltaTargets",
            "dynamo_db_targets": "dynamoDbTargets",
            "jdbc_targets": "jdbcTargets",
            "mongo_db_targets": "mongoDbTargets",
            "s3_targets": "s3Targets",
        },
    )
    class TargetsProperty:
        def __init__(
            self,
            *,
            catalog_targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCrawler.CatalogTargetProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            delta_targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCrawler.DeltaTargetProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            dynamo_db_targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCrawler.DynamoDBTargetProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            jdbc_targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCrawler.JdbcTargetProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            mongo_db_targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCrawler.MongoDBTargetProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            s3_targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCrawler.S3TargetProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Specifies data stores to crawl.

            :param catalog_targets: Specifies AWS Glue Data Catalog targets.
            :param delta_targets: Specifies an array of Delta data store targets.
            :param dynamo_db_targets: Specifies Amazon DynamoDB targets.
            :param jdbc_targets: Specifies JDBC targets.
            :param mongo_db_targets: A list of Mongo DB targets.
            :param s3_targets: Specifies Amazon Simple Storage Service (Amazon S3) targets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-targets.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                targets_property = glue.CfnCrawler.TargetsProperty(
                    catalog_targets=[glue.CfnCrawler.CatalogTargetProperty(
                        connection_name="connectionName",
                        database_name="databaseName",
                        dlq_event_queue_arn="dlqEventQueueArn",
                        event_queue_arn="eventQueueArn",
                        tables=["tables"]
                    )],
                    delta_targets=[glue.CfnCrawler.DeltaTargetProperty(
                        connection_name="connectionName",
                        create_native_delta_table=False,
                        delta_tables=["deltaTables"],
                        write_manifest=False
                    )],
                    dynamo_db_targets=[glue.CfnCrawler.DynamoDBTargetProperty(
                        path="path"
                    )],
                    jdbc_targets=[glue.CfnCrawler.JdbcTargetProperty(
                        connection_name="connectionName",
                        exclusions=["exclusions"],
                        path="path"
                    )],
                    mongo_db_targets=[glue.CfnCrawler.MongoDBTargetProperty(
                        connection_name="connectionName",
                        path="path"
                    )],
                    s3_targets=[glue.CfnCrawler.S3TargetProperty(
                        connection_name="connectionName",
                        dlq_event_queue_arn="dlqEventQueueArn",
                        event_queue_arn="eventQueueArn",
                        exclusions=["exclusions"],
                        path="path",
                        sample_size=123
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fe7a457ca9245ce0e51373e4e1d8daf444f9da978c352bc8529931e53484771c)
                check_type(argname="argument catalog_targets", value=catalog_targets, expected_type=type_hints["catalog_targets"])
                check_type(argname="argument delta_targets", value=delta_targets, expected_type=type_hints["delta_targets"])
                check_type(argname="argument dynamo_db_targets", value=dynamo_db_targets, expected_type=type_hints["dynamo_db_targets"])
                check_type(argname="argument jdbc_targets", value=jdbc_targets, expected_type=type_hints["jdbc_targets"])
                check_type(argname="argument mongo_db_targets", value=mongo_db_targets, expected_type=type_hints["mongo_db_targets"])
                check_type(argname="argument s3_targets", value=s3_targets, expected_type=type_hints["s3_targets"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if catalog_targets is not None:
                self._values["catalog_targets"] = catalog_targets
            if delta_targets is not None:
                self._values["delta_targets"] = delta_targets
            if dynamo_db_targets is not None:
                self._values["dynamo_db_targets"] = dynamo_db_targets
            if jdbc_targets is not None:
                self._values["jdbc_targets"] = jdbc_targets
            if mongo_db_targets is not None:
                self._values["mongo_db_targets"] = mongo_db_targets
            if s3_targets is not None:
                self._values["s3_targets"] = s3_targets

        @builtins.property
        def catalog_targets(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCrawler.CatalogTargetProperty"]]]]:
            '''Specifies AWS Glue Data Catalog targets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-targets.html#cfn-glue-crawler-targets-catalogtargets
            '''
            result = self._values.get("catalog_targets")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCrawler.CatalogTargetProperty"]]]], result)

        @builtins.property
        def delta_targets(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCrawler.DeltaTargetProperty"]]]]:
            '''Specifies an array of Delta data store targets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-targets.html#cfn-glue-crawler-targets-deltatargets
            '''
            result = self._values.get("delta_targets")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCrawler.DeltaTargetProperty"]]]], result)

        @builtins.property
        def dynamo_db_targets(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCrawler.DynamoDBTargetProperty"]]]]:
            '''Specifies Amazon DynamoDB targets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-targets.html#cfn-glue-crawler-targets-dynamodbtargets
            '''
            result = self._values.get("dynamo_db_targets")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCrawler.DynamoDBTargetProperty"]]]], result)

        @builtins.property
        def jdbc_targets(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCrawler.JdbcTargetProperty"]]]]:
            '''Specifies JDBC targets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-targets.html#cfn-glue-crawler-targets-jdbctargets
            '''
            result = self._values.get("jdbc_targets")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCrawler.JdbcTargetProperty"]]]], result)

        @builtins.property
        def mongo_db_targets(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCrawler.MongoDBTargetProperty"]]]]:
            '''A list of Mongo DB targets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-targets.html#cfn-glue-crawler-targets-mongodbtargets
            '''
            result = self._values.get("mongo_db_targets")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCrawler.MongoDBTargetProperty"]]]], result)

        @builtins.property
        def s3_targets(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCrawler.S3TargetProperty"]]]]:
            '''Specifies Amazon Simple Storage Service (Amazon S3) targets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-targets.html#cfn-glue-crawler-targets-s3targets
            '''
            result = self._values.get("s3_targets")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCrawler.S3TargetProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_glue.CfnCrawlerProps",
    jsii_struct_bases=[],
    name_mapping={
        "role": "role",
        "targets": "targets",
        "classifiers": "classifiers",
        "configuration": "configuration",
        "crawler_security_configuration": "crawlerSecurityConfiguration",
        "database_name": "databaseName",
        "description": "description",
        "name": "name",
        "recrawl_policy": "recrawlPolicy",
        "schedule": "schedule",
        "schema_change_policy": "schemaChangePolicy",
        "table_prefix": "tablePrefix",
        "tags": "tags",
    },
)
class CfnCrawlerProps:
    def __init__(
        self,
        *,
        role: builtins.str,
        targets: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCrawler.TargetsProperty, typing.Dict[builtins.str, typing.Any]]],
        classifiers: typing.Optional[typing.Sequence[builtins.str]] = None,
        configuration: typing.Optional[builtins.str] = None,
        crawler_security_configuration: typing.Optional[builtins.str] = None,
        database_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        recrawl_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCrawler.RecrawlPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCrawler.ScheduleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        schema_change_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCrawler.SchemaChangePolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        table_prefix: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
    ) -> None:
        '''Properties for defining a ``CfnCrawler``.

        :param role: The Amazon Resource Name (ARN) of an IAM role that's used to access customer resources, such as Amazon Simple Storage Service (Amazon S3) data.
        :param targets: A collection of targets to crawl.
        :param classifiers: A list of UTF-8 strings that specify the names of custom classifiers that are associated with the crawler.
        :param configuration: Crawler configuration information. This versioned JSON string allows users to specify aspects of a crawler's behavior. For more information, see `Configuring a Crawler <https://docs.aws.amazon.com/glue/latest/dg/crawler-configuration.html>`_ .
        :param crawler_security_configuration: The name of the ``SecurityConfiguration`` structure to be used by this crawler.
        :param database_name: The name of the database in which the crawler's output is stored.
        :param description: A description of the crawler.
        :param name: The name of the crawler.
        :param recrawl_policy: A policy that specifies whether to crawl the entire dataset again, or to crawl only folders that were added since the last crawler run.
        :param schedule: For scheduled crawlers, the schedule when the crawler runs.
        :param schema_change_policy: The policy that specifies update and delete behaviors for the crawler. The policy tells the crawler what to do in the event that it detects a change in a table that already exists in the customer's database at the time of the crawl. The ``SchemaChangePolicy`` does not affect whether or how new tables and partitions are added. New tables and partitions are always created regardless of the ``SchemaChangePolicy`` on a crawler. The SchemaChangePolicy consists of two components, ``UpdateBehavior`` and ``DeleteBehavior`` .
        :param table_prefix: The prefix added to the names of tables that are created.
        :param tags: The tags to use with this crawler.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_glue as glue
            
            # tags: Any
            
            cfn_crawler_props = glue.CfnCrawlerProps(
                role="role",
                targets=glue.CfnCrawler.TargetsProperty(
                    catalog_targets=[glue.CfnCrawler.CatalogTargetProperty(
                        connection_name="connectionName",
                        database_name="databaseName",
                        dlq_event_queue_arn="dlqEventQueueArn",
                        event_queue_arn="eventQueueArn",
                        tables=["tables"]
                    )],
                    delta_targets=[glue.CfnCrawler.DeltaTargetProperty(
                        connection_name="connectionName",
                        create_native_delta_table=False,
                        delta_tables=["deltaTables"],
                        write_manifest=False
                    )],
                    dynamo_db_targets=[glue.CfnCrawler.DynamoDBTargetProperty(
                        path="path"
                    )],
                    jdbc_targets=[glue.CfnCrawler.JdbcTargetProperty(
                        connection_name="connectionName",
                        exclusions=["exclusions"],
                        path="path"
                    )],
                    mongo_db_targets=[glue.CfnCrawler.MongoDBTargetProperty(
                        connection_name="connectionName",
                        path="path"
                    )],
                    s3_targets=[glue.CfnCrawler.S3TargetProperty(
                        connection_name="connectionName",
                        dlq_event_queue_arn="dlqEventQueueArn",
                        event_queue_arn="eventQueueArn",
                        exclusions=["exclusions"],
                        path="path",
                        sample_size=123
                    )]
                ),
            
                # the properties below are optional
                classifiers=["classifiers"],
                configuration="configuration",
                crawler_security_configuration="crawlerSecurityConfiguration",
                database_name="databaseName",
                description="description",
                name="name",
                recrawl_policy=glue.CfnCrawler.RecrawlPolicyProperty(
                    recrawl_behavior="recrawlBehavior"
                ),
                schedule=glue.CfnCrawler.ScheduleProperty(
                    schedule_expression="scheduleExpression"
                ),
                schema_change_policy=glue.CfnCrawler.SchemaChangePolicyProperty(
                    delete_behavior="deleteBehavior",
                    update_behavior="updateBehavior"
                ),
                table_prefix="tablePrefix",
                tags=tags
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51125dcaf0f55fdaefa50d6b9c05a6e431008538b8ab24abc0fbe126f61c382c)
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument targets", value=targets, expected_type=type_hints["targets"])
            check_type(argname="argument classifiers", value=classifiers, expected_type=type_hints["classifiers"])
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument crawler_security_configuration", value=crawler_security_configuration, expected_type=type_hints["crawler_security_configuration"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument recrawl_policy", value=recrawl_policy, expected_type=type_hints["recrawl_policy"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument schema_change_policy", value=schema_change_policy, expected_type=type_hints["schema_change_policy"])
            check_type(argname="argument table_prefix", value=table_prefix, expected_type=type_hints["table_prefix"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role": role,
            "targets": targets,
        }
        if classifiers is not None:
            self._values["classifiers"] = classifiers
        if configuration is not None:
            self._values["configuration"] = configuration
        if crawler_security_configuration is not None:
            self._values["crawler_security_configuration"] = crawler_security_configuration
        if database_name is not None:
            self._values["database_name"] = database_name
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if recrawl_policy is not None:
            self._values["recrawl_policy"] = recrawl_policy
        if schedule is not None:
            self._values["schedule"] = schedule
        if schema_change_policy is not None:
            self._values["schema_change_policy"] = schema_change_policy
        if table_prefix is not None:
            self._values["table_prefix"] = table_prefix
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def role(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of an IAM role that's used to access customer resources, such as Amazon Simple Storage Service (Amazon S3) data.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html#cfn-glue-crawler-role
        '''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def targets(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnCrawler.TargetsProperty]:
        '''A collection of targets to crawl.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html#cfn-glue-crawler-targets
        '''
        result = self._values.get("targets")
        assert result is not None, "Required property 'targets' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnCrawler.TargetsProperty], result)

    @builtins.property
    def classifiers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of UTF-8 strings that specify the names of custom classifiers that are associated with the crawler.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html#cfn-glue-crawler-classifiers
        '''
        result = self._values.get("classifiers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def configuration(self) -> typing.Optional[builtins.str]:
        '''Crawler configuration information.

        This versioned JSON string allows users to specify aspects of a crawler's behavior. For more information, see `Configuring a Crawler <https://docs.aws.amazon.com/glue/latest/dg/crawler-configuration.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html#cfn-glue-crawler-configuration
        '''
        result = self._values.get("configuration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def crawler_security_configuration(self) -> typing.Optional[builtins.str]:
        '''The name of the ``SecurityConfiguration`` structure to be used by this crawler.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html#cfn-glue-crawler-crawlersecurityconfiguration
        '''
        result = self._values.get("crawler_security_configuration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def database_name(self) -> typing.Optional[builtins.str]:
        '''The name of the database in which the crawler's output is stored.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html#cfn-glue-crawler-databasename
        '''
        result = self._values.get("database_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the crawler.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html#cfn-glue-crawler-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the crawler.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html#cfn-glue-crawler-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recrawl_policy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCrawler.RecrawlPolicyProperty]]:
        '''A policy that specifies whether to crawl the entire dataset again, or to crawl only folders that were added since the last crawler run.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html#cfn-glue-crawler-recrawlpolicy
        '''
        result = self._values.get("recrawl_policy")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCrawler.RecrawlPolicyProperty]], result)

    @builtins.property
    def schedule(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCrawler.ScheduleProperty]]:
        '''For scheduled crawlers, the schedule when the crawler runs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html#cfn-glue-crawler-schedule
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCrawler.ScheduleProperty]], result)

    @builtins.property
    def schema_change_policy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCrawler.SchemaChangePolicyProperty]]:
        '''The policy that specifies update and delete behaviors for the crawler.

        The policy tells the crawler what to do in the event that it detects a change in a table that already exists in the customer's database at the time of the crawl. The ``SchemaChangePolicy`` does not affect whether or how new tables and partitions are added. New tables and partitions are always created regardless of the ``SchemaChangePolicy`` on a crawler.

        The SchemaChangePolicy consists of two components, ``UpdateBehavior`` and ``DeleteBehavior`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html#cfn-glue-crawler-schemachangepolicy
        '''
        result = self._values.get("schema_change_policy")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCrawler.SchemaChangePolicyProperty]], result)

    @builtins.property
    def table_prefix(self) -> typing.Optional[builtins.str]:
        '''The prefix added to the names of tables that are created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html#cfn-glue-crawler-tableprefix
        '''
        result = self._values.get("table_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''The tags to use with this crawler.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html#cfn-glue-crawler-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCrawlerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnDataCatalogEncryptionSettings(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_glue.CfnDataCatalogEncryptionSettings",
):
    '''Sets the security configuration for a specified catalog.

    After the configuration has been set, the specified encryption is applied to every catalog write thereafter.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-datacatalogencryptionsettings.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_glue as glue
        
        cfn_data_catalog_encryption_settings = glue.CfnDataCatalogEncryptionSettings(self, "MyCfnDataCatalogEncryptionSettings",
            catalog_id="catalogId",
            data_catalog_encryption_settings=glue.CfnDataCatalogEncryptionSettings.DataCatalogEncryptionSettingsProperty(
                connection_password_encryption=glue.CfnDataCatalogEncryptionSettings.ConnectionPasswordEncryptionProperty(
                    kms_key_id="kmsKeyId",
                    return_connection_password_encrypted=False
                ),
                encryption_at_rest=glue.CfnDataCatalogEncryptionSettings.EncryptionAtRestProperty(
                    catalog_encryption_mode="catalogEncryptionMode",
                    sse_aws_kms_key_id="sseAwsKmsKeyId"
                )
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        catalog_id: builtins.str,
        data_catalog_encryption_settings: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataCatalogEncryptionSettings.DataCatalogEncryptionSettingsProperty", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param catalog_id: The ID of the Data Catalog in which the settings are created.
        :param data_catalog_encryption_settings: Contains configuration information for maintaining Data Catalog security.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__282fa6292001a27626ebcdd16c3756f6c1f39e2fce0bffe2aa07015e603b0c74)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDataCatalogEncryptionSettingsProps(
            catalog_id=catalog_id,
            data_catalog_encryption_settings=data_catalog_encryption_settings,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4e1e9ace4bcb120e971fb9f4d836733533c524cf73881927356077e8a876243)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6c9dd3472041f0c72b01ac8da059b956f55ea8a163f3d588982e26081d26472a)
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
    @jsii.member(jsii_name="catalogId")
    def catalog_id(self) -> builtins.str:
        '''The ID of the Data Catalog in which the settings are created.'''
        return typing.cast(builtins.str, jsii.get(self, "catalogId"))

    @catalog_id.setter
    def catalog_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01920d02ae9ef51342dbd5a647a412a6e68458011da6333a12e4cbce3c46addd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogId", value)

    @builtins.property
    @jsii.member(jsii_name="dataCatalogEncryptionSettings")
    def data_catalog_encryption_settings(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnDataCatalogEncryptionSettings.DataCatalogEncryptionSettingsProperty"]:
        '''Contains configuration information for maintaining Data Catalog security.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDataCatalogEncryptionSettings.DataCatalogEncryptionSettingsProperty"], jsii.get(self, "dataCatalogEncryptionSettings"))

    @data_catalog_encryption_settings.setter
    def data_catalog_encryption_settings(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnDataCatalogEncryptionSettings.DataCatalogEncryptionSettingsProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0fe99133f601e0dba434462eeee0ca24bdba16dd90df4d18a9865152672243b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataCatalogEncryptionSettings", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnDataCatalogEncryptionSettings.ConnectionPasswordEncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "kms_key_id": "kmsKeyId",
            "return_connection_password_encrypted": "returnConnectionPasswordEncrypted",
        },
    )
    class ConnectionPasswordEncryptionProperty:
        def __init__(
            self,
            *,
            kms_key_id: typing.Optional[builtins.str] = None,
            return_connection_password_encrypted: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The data structure used by the Data Catalog to encrypt the password as part of ``CreateConnection`` or ``UpdateConnection`` and store it in the ``ENCRYPTED_PASSWORD`` field in the connection properties.

            You can enable catalog encryption or only password encryption.

            When a ``CreationConnection`` request arrives containing a password, the Data Catalog first encrypts the password using your AWS KMS key. It then encrypts the whole connection object again if catalog encryption is also enabled.

            This encryption requires that you set AWS KMS key permissions to enable or restrict access on the password key according to your security requirements. For example, you might want only administrators to have decrypt permission on the password key.

            :param kms_key_id: An AWS KMS key that is used to encrypt the connection password. If connection password protection is enabled, the caller of ``CreateConnection`` and ``UpdateConnection`` needs at least ``kms:Encrypt`` permission on the specified AWS KMS key, to encrypt passwords before storing them in the Data Catalog. You can set the decrypt permission to enable or restrict access on the password key according to your security requirements.
            :param return_connection_password_encrypted: When the ``ReturnConnectionPasswordEncrypted`` flag is set to "true", passwords remain encrypted in the responses of ``GetConnection`` and ``GetConnections`` . This encryption takes effect independently from catalog encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-datacatalogencryptionsettings-connectionpasswordencryption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                connection_password_encryption_property = glue.CfnDataCatalogEncryptionSettings.ConnectionPasswordEncryptionProperty(
                    kms_key_id="kmsKeyId",
                    return_connection_password_encrypted=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__34fc71f63e95ce1add57dfdd2e0ed274fd6575145b30e9f35229e487efafb211)
                check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
                check_type(argname="argument return_connection_password_encrypted", value=return_connection_password_encrypted, expected_type=type_hints["return_connection_password_encrypted"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id
            if return_connection_password_encrypted is not None:
                self._values["return_connection_password_encrypted"] = return_connection_password_encrypted

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''An AWS KMS key that is used to encrypt the connection password.

            If connection password protection is enabled, the caller of ``CreateConnection`` and ``UpdateConnection`` needs at least ``kms:Encrypt`` permission on the specified AWS KMS key, to encrypt passwords before storing them in the Data Catalog. You can set the decrypt permission to enable or restrict access on the password key according to your security requirements.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-datacatalogencryptionsettings-connectionpasswordencryption.html#cfn-glue-datacatalogencryptionsettings-connectionpasswordencryption-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def return_connection_password_encrypted(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When the ``ReturnConnectionPasswordEncrypted`` flag is set to "true", passwords remain encrypted in the responses of ``GetConnection`` and ``GetConnections`` .

            This encryption takes effect independently from catalog encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-datacatalogencryptionsettings-connectionpasswordencryption.html#cfn-glue-datacatalogencryptionsettings-connectionpasswordencryption-returnconnectionpasswordencrypted
            '''
            result = self._values.get("return_connection_password_encrypted")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConnectionPasswordEncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnDataCatalogEncryptionSettings.DataCatalogEncryptionSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "connection_password_encryption": "connectionPasswordEncryption",
            "encryption_at_rest": "encryptionAtRest",
        },
    )
    class DataCatalogEncryptionSettingsProperty:
        def __init__(
            self,
            *,
            connection_password_encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataCatalogEncryptionSettings.ConnectionPasswordEncryptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            encryption_at_rest: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataCatalogEncryptionSettings.EncryptionAtRestProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains configuration information for maintaining Data Catalog security.

            :param connection_password_encryption: When connection password protection is enabled, the Data Catalog uses a customer-provided key to encrypt the password as part of ``CreateConnection`` or ``UpdateConnection`` and store it in the ``ENCRYPTED_PASSWORD`` field in the connection properties. You can enable catalog encryption or only password encryption.
            :param encryption_at_rest: Specifies the encryption-at-rest configuration for the Data Catalog.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-datacatalogencryptionsettings-datacatalogencryptionsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                data_catalog_encryption_settings_property = glue.CfnDataCatalogEncryptionSettings.DataCatalogEncryptionSettingsProperty(
                    connection_password_encryption=glue.CfnDataCatalogEncryptionSettings.ConnectionPasswordEncryptionProperty(
                        kms_key_id="kmsKeyId",
                        return_connection_password_encrypted=False
                    ),
                    encryption_at_rest=glue.CfnDataCatalogEncryptionSettings.EncryptionAtRestProperty(
                        catalog_encryption_mode="catalogEncryptionMode",
                        sse_aws_kms_key_id="sseAwsKmsKeyId"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f00201a45ca678da32495cdf8e4750f6ee26f926e576c207f665e4982e5d8cbd)
                check_type(argname="argument connection_password_encryption", value=connection_password_encryption, expected_type=type_hints["connection_password_encryption"])
                check_type(argname="argument encryption_at_rest", value=encryption_at_rest, expected_type=type_hints["encryption_at_rest"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if connection_password_encryption is not None:
                self._values["connection_password_encryption"] = connection_password_encryption
            if encryption_at_rest is not None:
                self._values["encryption_at_rest"] = encryption_at_rest

        @builtins.property
        def connection_password_encryption(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataCatalogEncryptionSettings.ConnectionPasswordEncryptionProperty"]]:
            '''When connection password protection is enabled, the Data Catalog uses a customer-provided key to encrypt the password as part of ``CreateConnection`` or ``UpdateConnection`` and store it in the ``ENCRYPTED_PASSWORD`` field in the connection properties.

            You can enable catalog encryption or only password encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-datacatalogencryptionsettings-datacatalogencryptionsettings.html#cfn-glue-datacatalogencryptionsettings-datacatalogencryptionsettings-connectionpasswordencryption
            '''
            result = self._values.get("connection_password_encryption")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataCatalogEncryptionSettings.ConnectionPasswordEncryptionProperty"]], result)

        @builtins.property
        def encryption_at_rest(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataCatalogEncryptionSettings.EncryptionAtRestProperty"]]:
            '''Specifies the encryption-at-rest configuration for the Data Catalog.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-datacatalogencryptionsettings-datacatalogencryptionsettings.html#cfn-glue-datacatalogencryptionsettings-datacatalogencryptionsettings-encryptionatrest
            '''
            result = self._values.get("encryption_at_rest")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataCatalogEncryptionSettings.EncryptionAtRestProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataCatalogEncryptionSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnDataCatalogEncryptionSettings.EncryptionAtRestProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_encryption_mode": "catalogEncryptionMode",
            "sse_aws_kms_key_id": "sseAwsKmsKeyId",
        },
    )
    class EncryptionAtRestProperty:
        def __init__(
            self,
            *,
            catalog_encryption_mode: typing.Optional[builtins.str] = None,
            sse_aws_kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the encryption-at-rest configuration for the Data Catalog.

            :param catalog_encryption_mode: The encryption-at-rest mode for encrypting Data Catalog data.
            :param sse_aws_kms_key_id: The ID of the AWS KMS key to use for encryption at rest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-datacatalogencryptionsettings-encryptionatrest.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                encryption_at_rest_property = glue.CfnDataCatalogEncryptionSettings.EncryptionAtRestProperty(
                    catalog_encryption_mode="catalogEncryptionMode",
                    sse_aws_kms_key_id="sseAwsKmsKeyId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b55ae3f68b9a52d4f03ea46854dfc3c74490f427c278113fe4c847eaf6e6143d)
                check_type(argname="argument catalog_encryption_mode", value=catalog_encryption_mode, expected_type=type_hints["catalog_encryption_mode"])
                check_type(argname="argument sse_aws_kms_key_id", value=sse_aws_kms_key_id, expected_type=type_hints["sse_aws_kms_key_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if catalog_encryption_mode is not None:
                self._values["catalog_encryption_mode"] = catalog_encryption_mode
            if sse_aws_kms_key_id is not None:
                self._values["sse_aws_kms_key_id"] = sse_aws_kms_key_id

        @builtins.property
        def catalog_encryption_mode(self) -> typing.Optional[builtins.str]:
            '''The encryption-at-rest mode for encrypting Data Catalog data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-datacatalogencryptionsettings-encryptionatrest.html#cfn-glue-datacatalogencryptionsettings-encryptionatrest-catalogencryptionmode
            '''
            result = self._values.get("catalog_encryption_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sse_aws_kms_key_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the AWS KMS key to use for encryption at rest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-datacatalogencryptionsettings-encryptionatrest.html#cfn-glue-datacatalogencryptionsettings-encryptionatrest-sseawskmskeyid
            '''
            result = self._values.get("sse_aws_kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionAtRestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_glue.CfnDataCatalogEncryptionSettingsProps",
    jsii_struct_bases=[],
    name_mapping={
        "catalog_id": "catalogId",
        "data_catalog_encryption_settings": "dataCatalogEncryptionSettings",
    },
)
class CfnDataCatalogEncryptionSettingsProps:
    def __init__(
        self,
        *,
        catalog_id: builtins.str,
        data_catalog_encryption_settings: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataCatalogEncryptionSettings.DataCatalogEncryptionSettingsProperty, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Properties for defining a ``CfnDataCatalogEncryptionSettings``.

        :param catalog_id: The ID of the Data Catalog in which the settings are created.
        :param data_catalog_encryption_settings: Contains configuration information for maintaining Data Catalog security.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-datacatalogencryptionsettings.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_glue as glue
            
            cfn_data_catalog_encryption_settings_props = glue.CfnDataCatalogEncryptionSettingsProps(
                catalog_id="catalogId",
                data_catalog_encryption_settings=glue.CfnDataCatalogEncryptionSettings.DataCatalogEncryptionSettingsProperty(
                    connection_password_encryption=glue.CfnDataCatalogEncryptionSettings.ConnectionPasswordEncryptionProperty(
                        kms_key_id="kmsKeyId",
                        return_connection_password_encrypted=False
                    ),
                    encryption_at_rest=glue.CfnDataCatalogEncryptionSettings.EncryptionAtRestProperty(
                        catalog_encryption_mode="catalogEncryptionMode",
                        sse_aws_kms_key_id="sseAwsKmsKeyId"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3517f092be8bfa15079cf31c36ac6d8b4bfcf20615da68fd5127533210ef5c4)
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
            check_type(argname="argument data_catalog_encryption_settings", value=data_catalog_encryption_settings, expected_type=type_hints["data_catalog_encryption_settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "catalog_id": catalog_id,
            "data_catalog_encryption_settings": data_catalog_encryption_settings,
        }

    @builtins.property
    def catalog_id(self) -> builtins.str:
        '''The ID of the Data Catalog in which the settings are created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-datacatalogencryptionsettings.html#cfn-glue-datacatalogencryptionsettings-catalogid
        '''
        result = self._values.get("catalog_id")
        assert result is not None, "Required property 'catalog_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_catalog_encryption_settings(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnDataCatalogEncryptionSettings.DataCatalogEncryptionSettingsProperty]:
        '''Contains configuration information for maintaining Data Catalog security.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-datacatalogencryptionsettings.html#cfn-glue-datacatalogencryptionsettings-datacatalogencryptionsettings
        '''
        result = self._values.get("data_catalog_encryption_settings")
        assert result is not None, "Required property 'data_catalog_encryption_settings' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnDataCatalogEncryptionSettings.DataCatalogEncryptionSettingsProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataCatalogEncryptionSettingsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnDataQualityRuleset(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_glue.CfnDataQualityRuleset",
):
    '''The ``AWS::Glue::DataQualityRuleset`` resource specifies a data quality ruleset with DQDL rules applied to a specified AWS Glue table.

    For more information, see AWS Glue Data Quality in the AWS Glue Developer Guide.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-dataqualityruleset.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_glue as glue
        
        # tags: Any
        
        cfn_data_quality_ruleset = glue.CfnDataQualityRuleset(self, "MyCfnDataQualityRuleset",
            client_token="clientToken",
            description="description",
            name="name",
            ruleset="ruleset",
            tags=tags,
            target_table=glue.CfnDataQualityRuleset.DataQualityTargetTableProperty(
                database_name="databaseName",
                table_name="tableName"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        client_token: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        ruleset: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
        target_table: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataQualityRuleset.DataQualityTargetTableProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param client_token: Used for idempotency and is recommended to be set to a random ID (such as a UUID) to avoid creating or starting multiple instances of the same resource.
        :param description: A description of the data quality ruleset.
        :param name: The name of the data quality ruleset.
        :param ruleset: A Data Quality Definition Language (DQDL) ruleset. For more information see the AWS Glue Developer Guide.
        :param tags: A list of tags applied to the data quality ruleset.
        :param target_table: An object representing an AWS Glue table.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cd6788453c5f421cc94877f7bd1430bf0188a7b66044acb47e85a138c2525bc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDataQualityRulesetProps(
            client_token=client_token,
            description=description,
            name=name,
            ruleset=ruleset,
            tags=tags,
            target_table=target_table,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__821cea04f03dd8ae13ef8a301a29741a754cfa451c98bf537c239b6333df0af5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2adc51e0237315dfdb93e5fccd4fccd0705f44e751c4ac91b448d6d8fb5bcb43)
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
    @jsii.member(jsii_name="clientToken")
    def client_token(self) -> typing.Optional[builtins.str]:
        '''Used for idempotency and is recommended to be set to a random ID (such as a UUID) to avoid creating or starting multiple instances of the same resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientToken"))

    @client_token.setter
    def client_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb7412aa32bb9c0fa23c3df7527a57c842aabf5ffa622d5ab6cd6540caa2e57a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientToken", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the data quality ruleset.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e22bc2d9629c173f100a1ee8aea1f132a9bc0e287ff0e2b88d829b304c3de308)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the data quality ruleset.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c19fdaeabb94e016ab468e10db4486c501c8a4f296c51d5fd475d3ea7f6ab92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="ruleset")
    def ruleset(self) -> typing.Optional[builtins.str]:
        '''A Data Quality Definition Language (DQDL) ruleset.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleset"))

    @ruleset.setter
    def ruleset(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f89426cd75d9e88eba122cc29f0542dfceb62cfb21e07d8b912deed58918f8db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleset", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Any:
        '''A list of tags applied to the data quality ruleset.'''
        return typing.cast(typing.Any, jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__809d4010b3349232ca0d6023603914d402aeeedd96245959f582ca639b97209d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="targetTable")
    def target_table(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataQualityRuleset.DataQualityTargetTableProperty"]]:
        '''An object representing an AWS Glue table.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataQualityRuleset.DataQualityTargetTableProperty"]], jsii.get(self, "targetTable"))

    @target_table.setter
    def target_table(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataQualityRuleset.DataQualityTargetTableProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2eee281115746d453b02c60bac1ee159c50e3f758af73dcf2d6ada02e2cc1d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetTable", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnDataQualityRuleset.DataQualityTargetTableProperty",
        jsii_struct_bases=[],
        name_mapping={"database_name": "databaseName", "table_name": "tableName"},
    )
    class DataQualityTargetTableProperty:
        def __init__(
            self,
            *,
            database_name: typing.Optional[builtins.str] = None,
            table_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An object representing an AWS Glue table.

            :param database_name: The name of the database where the AWS Glue table exists.
            :param table_name: The name of the AWS Glue table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-dataqualityruleset-dataqualitytargettable.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                data_quality_target_table_property = glue.CfnDataQualityRuleset.DataQualityTargetTableProperty(
                    database_name="databaseName",
                    table_name="tableName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ead7fcb21ac05404e5bd5b515921d45f020c05cc414cc713cd438ccf815c1417)
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if database_name is not None:
                self._values["database_name"] = database_name
            if table_name is not None:
                self._values["table_name"] = table_name

        @builtins.property
        def database_name(self) -> typing.Optional[builtins.str]:
            '''The name of the database where the AWS Glue table exists.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-dataqualityruleset-dataqualitytargettable.html#cfn-glue-dataqualityruleset-dataqualitytargettable-databasename
            '''
            result = self._values.get("database_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def table_name(self) -> typing.Optional[builtins.str]:
            '''The name of the AWS Glue table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-dataqualityruleset-dataqualitytargettable.html#cfn-glue-dataqualityruleset-dataqualitytargettable-tablename
            '''
            result = self._values.get("table_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataQualityTargetTableProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_glue.CfnDataQualityRulesetProps",
    jsii_struct_bases=[],
    name_mapping={
        "client_token": "clientToken",
        "description": "description",
        "name": "name",
        "ruleset": "ruleset",
        "tags": "tags",
        "target_table": "targetTable",
    },
)
class CfnDataQualityRulesetProps:
    def __init__(
        self,
        *,
        client_token: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        ruleset: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
        target_table: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataQualityRuleset.DataQualityTargetTableProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDataQualityRuleset``.

        :param client_token: Used for idempotency and is recommended to be set to a random ID (such as a UUID) to avoid creating or starting multiple instances of the same resource.
        :param description: A description of the data quality ruleset.
        :param name: The name of the data quality ruleset.
        :param ruleset: A Data Quality Definition Language (DQDL) ruleset. For more information see the AWS Glue Developer Guide.
        :param tags: A list of tags applied to the data quality ruleset.
        :param target_table: An object representing an AWS Glue table.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-dataqualityruleset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_glue as glue
            
            # tags: Any
            
            cfn_data_quality_ruleset_props = glue.CfnDataQualityRulesetProps(
                client_token="clientToken",
                description="description",
                name="name",
                ruleset="ruleset",
                tags=tags,
                target_table=glue.CfnDataQualityRuleset.DataQualityTargetTableProperty(
                    database_name="databaseName",
                    table_name="tableName"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffd76843e7c0bf19ed341799bd6544ae909492cbfe595bc8806ea114fc1b01f1)
            check_type(argname="argument client_token", value=client_token, expected_type=type_hints["client_token"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument ruleset", value=ruleset, expected_type=type_hints["ruleset"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument target_table", value=target_table, expected_type=type_hints["target_table"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if client_token is not None:
            self._values["client_token"] = client_token
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if ruleset is not None:
            self._values["ruleset"] = ruleset
        if tags is not None:
            self._values["tags"] = tags
        if target_table is not None:
            self._values["target_table"] = target_table

    @builtins.property
    def client_token(self) -> typing.Optional[builtins.str]:
        '''Used for idempotency and is recommended to be set to a random ID (such as a UUID) to avoid creating or starting multiple instances of the same resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-dataqualityruleset.html#cfn-glue-dataqualityruleset-clienttoken
        '''
        result = self._values.get("client_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the data quality ruleset.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-dataqualityruleset.html#cfn-glue-dataqualityruleset-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the data quality ruleset.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-dataqualityruleset.html#cfn-glue-dataqualityruleset-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ruleset(self) -> typing.Optional[builtins.str]:
        '''A Data Quality Definition Language (DQDL) ruleset.

        For more information see the AWS Glue Developer Guide.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-dataqualityruleset.html#cfn-glue-dataqualityruleset-ruleset
        '''
        result = self._values.get("ruleset")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''A list of tags applied to the data quality ruleset.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-dataqualityruleset.html#cfn-glue-dataqualityruleset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    @builtins.property
    def target_table(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataQualityRuleset.DataQualityTargetTableProperty]]:
        '''An object representing an AWS Glue table.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-dataqualityruleset.html#cfn-glue-dataqualityruleset-targettable
        '''
        result = self._values.get("target_table")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataQualityRuleset.DataQualityTargetTableProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataQualityRulesetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnDatabase(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_glue.CfnDatabase",
):
    '''The ``AWS::Glue::Database`` resource specifies a logical grouping of tables in AWS Glue .

    For more information, see `Defining a Database in Your Data Catalog <https://docs.aws.amazon.com/glue/latest/dg/define-database.html>`_ and `Database Structure <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-databases.html#aws-glue-api-catalog-databases-Database>`_ in the *AWS Glue Developer Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-database.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_glue as glue
        
        # parameters: Any
        
        cfn_database = glue.CfnDatabase(self, "MyCfnDatabase",
            catalog_id="catalogId",
            database_input=glue.CfnDatabase.DatabaseInputProperty(
                create_table_default_permissions=[glue.CfnDatabase.PrincipalPrivilegesProperty(
                    permissions=["permissions"],
                    principal=glue.CfnDatabase.DataLakePrincipalProperty(
                        data_lake_principal_identifier="dataLakePrincipalIdentifier"
                    )
                )],
                description="description",
                federated_database=glue.CfnDatabase.FederatedDatabaseProperty(
                    connection_name="connectionName",
                    identifier="identifier"
                ),
                location_uri="locationUri",
                name="name",
                parameters=parameters,
                target_database=glue.CfnDatabase.DatabaseIdentifierProperty(
                    catalog_id="catalogId",
                    database_name="databaseName"
                )
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        catalog_id: builtins.str,
        database_input: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDatabase.DatabaseInputProperty", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param catalog_id: The AWS account ID for the account in which to create the catalog object. .. epigraph:: To specify the account ID, you can use the ``Ref`` intrinsic function with the ``AWS::AccountId`` pseudo parameter. For example: ``!Ref AWS::AccountId``
        :param database_input: The metadata for the database.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7145103c869df1a981612b4445af4fee59059eebaa09d55e36fa9961bbd0d271)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDatabaseProps(catalog_id=catalog_id, database_input=database_input)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0e83df07074fd6e3bd554052571366deb1febf7f69f6452ca58261d50898a69)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dc3a63206fa9807ebcdb35676de76b49507fbd5baf5ec473e655fb4ae8d37882)
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
    @jsii.member(jsii_name="catalogId")
    def catalog_id(self) -> builtins.str:
        '''The AWS account ID for the account in which to create the catalog object.'''
        return typing.cast(builtins.str, jsii.get(self, "catalogId"))

    @catalog_id.setter
    def catalog_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86a8e89801bb5dac6dbcec69f62eb5089c97eac21e4a7b226afccf50df44b861)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogId", value)

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnDatabase.DatabaseInputProperty"]:
        '''The metadata for the database.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDatabase.DatabaseInputProperty"], jsii.get(self, "databaseInput"))

    @database_input.setter
    def database_input(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnDatabase.DatabaseInputProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e2364f804df0cc3d57e45e3e5c68968dc857adcab1747035408147542b2d495)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseInput", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnDatabase.DataLakePrincipalProperty",
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

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-datalakeprincipal.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                data_lake_principal_property = glue.CfnDatabase.DataLakePrincipalProperty(
                    data_lake_principal_identifier="dataLakePrincipalIdentifier"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6fa63353d4d392cf6a598ebd7c80b56747ad0b7973313267f52becc342ac17de)
                check_type(argname="argument data_lake_principal_identifier", value=data_lake_principal_identifier, expected_type=type_hints["data_lake_principal_identifier"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if data_lake_principal_identifier is not None:
                self._values["data_lake_principal_identifier"] = data_lake_principal_identifier

        @builtins.property
        def data_lake_principal_identifier(self) -> typing.Optional[builtins.str]:
            '''An identifier for the AWS Lake Formation principal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-datalakeprincipal.html#cfn-glue-database-datalakeprincipal-datalakeprincipalidentifier
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
        jsii_type="aws-cdk-lib.aws_glue.CfnDatabase.DatabaseIdentifierProperty",
        jsii_struct_bases=[],
        name_mapping={"catalog_id": "catalogId", "database_name": "databaseName"},
    )
    class DatabaseIdentifierProperty:
        def __init__(
            self,
            *,
            catalog_id: typing.Optional[builtins.str] = None,
            database_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A structure that describes a target database for resource linking.

            :param catalog_id: The ID of the Data Catalog in which the database resides.
            :param database_name: The name of the catalog database.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseidentifier.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                database_identifier_property = glue.CfnDatabase.DatabaseIdentifierProperty(
                    catalog_id="catalogId",
                    database_name="databaseName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5e1e09205087e89c58802ef33b1c27bb5ad9de3db3e6419d7c72b490675f5e27)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if catalog_id is not None:
                self._values["catalog_id"] = catalog_id
            if database_name is not None:
                self._values["database_name"] = database_name

        @builtins.property
        def catalog_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the Data Catalog in which the database resides.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseidentifier.html#cfn-glue-database-databaseidentifier-catalogid
            '''
            result = self._values.get("catalog_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def database_name(self) -> typing.Optional[builtins.str]:
            '''The name of the catalog database.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseidentifier.html#cfn-glue-database-databaseidentifier-databasename
            '''
            result = self._values.get("database_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatabaseIdentifierProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnDatabase.DatabaseInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "create_table_default_permissions": "createTableDefaultPermissions",
            "description": "description",
            "federated_database": "federatedDatabase",
            "location_uri": "locationUri",
            "name": "name",
            "parameters": "parameters",
            "target_database": "targetDatabase",
        },
    )
    class DatabaseInputProperty:
        def __init__(
            self,
            *,
            create_table_default_permissions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDatabase.PrincipalPrivilegesProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            description: typing.Optional[builtins.str] = None,
            federated_database: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDatabase.FederatedDatabaseProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            location_uri: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            parameters: typing.Any = None,
            target_database: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDatabase.DatabaseIdentifierProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The structure used to create or update a database.

            :param create_table_default_permissions: Creates a set of default permissions on the table for principals. Used by AWS Lake Formation . Not used in the normal course of AWS Glue operations.
            :param description: A description of the database.
            :param federated_database: A ``FederatedDatabase`` structure that references an entity outside the AWS Glue Data Catalog .
            :param location_uri: The location of the database (for example, an HDFS path).
            :param name: The name of the database. For Hive compatibility, this is folded to lowercase when it is stored.
            :param parameters: These key-value pairs define parameters and properties of the database.
            :param target_database: A ``DatabaseIdentifier`` structure that describes a target database for resource linking.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                # parameters: Any
                
                database_input_property = glue.CfnDatabase.DatabaseInputProperty(
                    create_table_default_permissions=[glue.CfnDatabase.PrincipalPrivilegesProperty(
                        permissions=["permissions"],
                        principal=glue.CfnDatabase.DataLakePrincipalProperty(
                            data_lake_principal_identifier="dataLakePrincipalIdentifier"
                        )
                    )],
                    description="description",
                    federated_database=glue.CfnDatabase.FederatedDatabaseProperty(
                        connection_name="connectionName",
                        identifier="identifier"
                    ),
                    location_uri="locationUri",
                    name="name",
                    parameters=parameters,
                    target_database=glue.CfnDatabase.DatabaseIdentifierProperty(
                        catalog_id="catalogId",
                        database_name="databaseName"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4066647dd15931f0ef186e76b4d72a1a31dd7f45cce5691790e1c5709a696c3d)
                check_type(argname="argument create_table_default_permissions", value=create_table_default_permissions, expected_type=type_hints["create_table_default_permissions"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument federated_database", value=federated_database, expected_type=type_hints["federated_database"])
                check_type(argname="argument location_uri", value=location_uri, expected_type=type_hints["location_uri"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
                check_type(argname="argument target_database", value=target_database, expected_type=type_hints["target_database"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if create_table_default_permissions is not None:
                self._values["create_table_default_permissions"] = create_table_default_permissions
            if description is not None:
                self._values["description"] = description
            if federated_database is not None:
                self._values["federated_database"] = federated_database
            if location_uri is not None:
                self._values["location_uri"] = location_uri
            if name is not None:
                self._values["name"] = name
            if parameters is not None:
                self._values["parameters"] = parameters
            if target_database is not None:
                self._values["target_database"] = target_database

        @builtins.property
        def create_table_default_permissions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDatabase.PrincipalPrivilegesProperty"]]]]:
            '''Creates a set of default permissions on the table for principals.

            Used by AWS Lake Formation . Not used in the normal course of AWS Glue operations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseinput.html#cfn-glue-database-databaseinput-createtabledefaultpermissions
            '''
            result = self._values.get("create_table_default_permissions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDatabase.PrincipalPrivilegesProperty"]]]], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''A description of the database.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseinput.html#cfn-glue-database-databaseinput-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def federated_database(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDatabase.FederatedDatabaseProperty"]]:
            '''A ``FederatedDatabase`` structure that references an entity outside the AWS Glue Data Catalog .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseinput.html#cfn-glue-database-databaseinput-federateddatabase
            '''
            result = self._values.get("federated_database")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDatabase.FederatedDatabaseProperty"]], result)

        @builtins.property
        def location_uri(self) -> typing.Optional[builtins.str]:
            '''The location of the database (for example, an HDFS path).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseinput.html#cfn-glue-database-databaseinput-locationuri
            '''
            result = self._values.get("location_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the database.

            For Hive compatibility, this is folded to lowercase when it is stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseinput.html#cfn-glue-database-databaseinput-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parameters(self) -> typing.Any:
            '''These key-value pairs define parameters and properties of the database.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseinput.html#cfn-glue-database-databaseinput-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Any, result)

        @builtins.property
        def target_database(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDatabase.DatabaseIdentifierProperty"]]:
            '''A ``DatabaseIdentifier`` structure that describes a target database for resource linking.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseinput.html#cfn-glue-database-databaseinput-targetdatabase
            '''
            result = self._values.get("target_database")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDatabase.DatabaseIdentifierProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatabaseInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnDatabase.FederatedDatabaseProperty",
        jsii_struct_bases=[],
        name_mapping={"connection_name": "connectionName", "identifier": "identifier"},
    )
    class FederatedDatabaseProperty:
        def __init__(
            self,
            *,
            connection_name: typing.Optional[builtins.str] = None,
            identifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A ``FederatedDatabase`` structure that references an entity outside the AWS Glue Data Catalog .

            :param connection_name: The name of the connection to the external metastore.
            :param identifier: A unique identifier for the federated database.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-federateddatabase.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                federated_database_property = glue.CfnDatabase.FederatedDatabaseProperty(
                    connection_name="connectionName",
                    identifier="identifier"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d5d4932721a3226e798772e900af6d3cb2ecce08df6276ce369fcbac2f8da038)
                check_type(argname="argument connection_name", value=connection_name, expected_type=type_hints["connection_name"])
                check_type(argname="argument identifier", value=identifier, expected_type=type_hints["identifier"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if connection_name is not None:
                self._values["connection_name"] = connection_name
            if identifier is not None:
                self._values["identifier"] = identifier

        @builtins.property
        def connection_name(self) -> typing.Optional[builtins.str]:
            '''The name of the connection to the external metastore.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-federateddatabase.html#cfn-glue-database-federateddatabase-connectionname
            '''
            result = self._values.get("connection_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def identifier(self) -> typing.Optional[builtins.str]:
            '''A unique identifier for the federated database.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-federateddatabase.html#cfn-glue-database-federateddatabase-identifier
            '''
            result = self._values.get("identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FederatedDatabaseProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnDatabase.PrincipalPrivilegesProperty",
        jsii_struct_bases=[],
        name_mapping={"permissions": "permissions", "principal": "principal"},
    )
    class PrincipalPrivilegesProperty:
        def __init__(
            self,
            *,
            permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
            principal: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDatabase.DataLakePrincipalProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''the permissions granted to a principal.

            :param permissions: The permissions that are granted to the principal.
            :param principal: The principal who is granted permissions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-principalprivileges.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                principal_privileges_property = glue.CfnDatabase.PrincipalPrivilegesProperty(
                    permissions=["permissions"],
                    principal=glue.CfnDatabase.DataLakePrincipalProperty(
                        data_lake_principal_identifier="dataLakePrincipalIdentifier"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d43a817f676c64836757736236e2f064cc4dd36dc5c52414d08763ab68e9ed24)
                check_type(argname="argument permissions", value=permissions, expected_type=type_hints["permissions"])
                check_type(argname="argument principal", value=principal, expected_type=type_hints["principal"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if permissions is not None:
                self._values["permissions"] = permissions
            if principal is not None:
                self._values["principal"] = principal

        @builtins.property
        def permissions(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The permissions that are granted to the principal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-principalprivileges.html#cfn-glue-database-principalprivileges-permissions
            '''
            result = self._values.get("permissions")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def principal(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDatabase.DataLakePrincipalProperty"]]:
            '''The principal who is granted permissions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-principalprivileges.html#cfn-glue-database-principalprivileges-principal
            '''
            result = self._values.get("principal")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDatabase.DataLakePrincipalProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PrincipalPrivilegesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_glue.CfnDatabaseProps",
    jsii_struct_bases=[],
    name_mapping={"catalog_id": "catalogId", "database_input": "databaseInput"},
)
class CfnDatabaseProps:
    def __init__(
        self,
        *,
        catalog_id: builtins.str,
        database_input: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDatabase.DatabaseInputProperty, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Properties for defining a ``CfnDatabase``.

        :param catalog_id: The AWS account ID for the account in which to create the catalog object. .. epigraph:: To specify the account ID, you can use the ``Ref`` intrinsic function with the ``AWS::AccountId`` pseudo parameter. For example: ``!Ref AWS::AccountId``
        :param database_input: The metadata for the database.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-database.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_glue as glue
            
            # parameters: Any
            
            cfn_database_props = glue.CfnDatabaseProps(
                catalog_id="catalogId",
                database_input=glue.CfnDatabase.DatabaseInputProperty(
                    create_table_default_permissions=[glue.CfnDatabase.PrincipalPrivilegesProperty(
                        permissions=["permissions"],
                        principal=glue.CfnDatabase.DataLakePrincipalProperty(
                            data_lake_principal_identifier="dataLakePrincipalIdentifier"
                        )
                    )],
                    description="description",
                    federated_database=glue.CfnDatabase.FederatedDatabaseProperty(
                        connection_name="connectionName",
                        identifier="identifier"
                    ),
                    location_uri="locationUri",
                    name="name",
                    parameters=parameters,
                    target_database=glue.CfnDatabase.DatabaseIdentifierProperty(
                        catalog_id="catalogId",
                        database_name="databaseName"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2352883ee521541265e5630512401b3837ac0875c8b4eced9967bf612ebac267)
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
            check_type(argname="argument database_input", value=database_input, expected_type=type_hints["database_input"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "catalog_id": catalog_id,
            "database_input": database_input,
        }

    @builtins.property
    def catalog_id(self) -> builtins.str:
        '''The AWS account ID for the account in which to create the catalog object.

        .. epigraph::

           To specify the account ID, you can use the ``Ref`` intrinsic function with the ``AWS::AccountId`` pseudo parameter. For example: ``!Ref AWS::AccountId``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-database.html#cfn-glue-database-catalogid
        '''
        result = self._values.get("catalog_id")
        assert result is not None, "Required property 'catalog_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def database_input(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnDatabase.DatabaseInputProperty]:
        '''The metadata for the database.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-database.html#cfn-glue-database-databaseinput
        '''
        result = self._values.get("database_input")
        assert result is not None, "Required property 'database_input' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnDatabase.DatabaseInputProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDatabaseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnDevEndpoint(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_glue.CfnDevEndpoint",
):
    '''The ``AWS::Glue::DevEndpoint`` resource specifies a development endpoint where a developer can remotely debug ETL scripts for AWS Glue .

    For more information, see `DevEndpoint Structure <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-dev-endpoint.html#aws-glue-api-jobs-dev-endpoint-DevEndpoint>`_ in the AWS Glue Developer Guide.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_glue as glue
        
        # arguments_: Any
        # tags: Any
        
        cfn_dev_endpoint = glue.CfnDevEndpoint(self, "MyCfnDevEndpoint",
            role_arn="roleArn",
        
            # the properties below are optional
            arguments=arguments_,
            endpoint_name="endpointName",
            extra_jars_s3_path="extraJarsS3Path",
            extra_python_libs_s3_path="extraPythonLibsS3Path",
            glue_version="glueVersion",
            number_of_nodes=123,
            number_of_workers=123,
            public_key="publicKey",
            public_keys=["publicKeys"],
            security_configuration="securityConfiguration",
            security_group_ids=["securityGroupIds"],
            subnet_id="subnetId",
            tags=tags,
            worker_type="workerType"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        role_arn: builtins.str,
        arguments: typing.Any = None,
        endpoint_name: typing.Optional[builtins.str] = None,
        extra_jars_s3_path: typing.Optional[builtins.str] = None,
        extra_python_libs_s3_path: typing.Optional[builtins.str] = None,
        glue_version: typing.Optional[builtins.str] = None,
        number_of_nodes: typing.Optional[jsii.Number] = None,
        number_of_workers: typing.Optional[jsii.Number] = None,
        public_key: typing.Optional[builtins.str] = None,
        public_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        security_configuration: typing.Optional[builtins.str] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
        worker_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param role_arn: The Amazon Resource Name (ARN) of the IAM role used in this ``DevEndpoint`` .
        :param arguments: A map of arguments used to configure the ``DevEndpoint`` . Valid arguments are: - ``"--enable-glue-datacatalog": ""`` - ``"GLUE_PYTHON_VERSION": "3"`` - ``"GLUE_PYTHON_VERSION": "2"`` You can specify a version of Python support for development endpoints by using the ``Arguments`` parameter in the ``CreateDevEndpoint`` or ``UpdateDevEndpoint`` APIs. If no arguments are provided, the version defaults to Python 2.
        :param endpoint_name: The name of the ``DevEndpoint`` .
        :param extra_jars_s3_path: The path to one or more Java ``.jar`` files in an S3 bucket that should be loaded in your ``DevEndpoint`` . .. epigraph:: You can only use pure Java/Scala libraries with a ``DevEndpoint`` .
        :param extra_python_libs_s3_path: The paths to one or more Python libraries in an Amazon S3 bucket that should be loaded in your ``DevEndpoint`` . Multiple values must be complete paths separated by a comma. .. epigraph:: You can only use pure Python libraries with a ``DevEndpoint`` . Libraries that rely on C extensions, such as the `pandas <https://docs.aws.amazon.com/http://pandas.pydata.org/>`_ Python data analysis library, are not currently supported.
        :param glue_version: The AWS Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The Python version indicates the version supported for running your ETL scripts on development endpoints. For more information about the available AWS Glue versions and corresponding Spark and Python versions, see `Glue version <https://docs.aws.amazon.com/glue/latest/dg/add-job.html>`_ in the developer guide. Development endpoints that are created without specifying a Glue version default to Glue 0.9. You can specify a version of Python support for development endpoints by using the ``Arguments`` parameter in the ``CreateDevEndpoint`` or ``UpdateDevEndpoint`` APIs. If no arguments are provided, the version defaults to Python 2.
        :param number_of_nodes: The number of AWS Glue Data Processing Units (DPUs) allocated to this ``DevEndpoint`` .
        :param number_of_workers: The number of workers of a defined ``workerType`` that are allocated to the development endpoint. The maximum number of workers you can define are 299 for ``G.1X`` , and 149 for ``G.2X`` .
        :param public_key: The public key to be used by this ``DevEndpoint`` for authentication. This attribute is provided for backward compatibility because the recommended attribute to use is public keys.
        :param public_keys: A list of public keys to be used by the ``DevEndpoints`` for authentication. Using this attribute is preferred over a single public key because the public keys allow you to have a different private key per client. .. epigraph:: If you previously created an endpoint with a public key, you must remove that key to be able to set a list of public keys. Call the ``UpdateDevEndpoint`` API operation with the public key content in the ``deletePublicKeys`` attribute, and the list of new keys in the ``addPublicKeys`` attribute.
        :param security_configuration: The name of the ``SecurityConfiguration`` structure to be used with this ``DevEndpoint`` .
        :param security_group_ids: A list of security group identifiers used in this ``DevEndpoint`` .
        :param subnet_id: The subnet ID for this ``DevEndpoint`` .
        :param tags: The tags to use with this DevEndpoint.
        :param worker_type: The type of predefined worker that is allocated to the development endpoint. Accepts a value of Standard, G.1X, or G.2X. - For the ``Standard`` worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker. - For the ``G.1X`` worker type, each worker maps to 1 DPU (4 vCPU, 16 GB of memory, 64 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs. - For the ``G.2X`` worker type, each worker maps to 2 DPU (8 vCPU, 32 GB of memory, 128 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs. Known issue: when a development endpoint is created with the ``G.2X`` ``WorkerType`` configuration, the Spark drivers for the development endpoint will run on 4 vCPU, 16 GB of memory, and a 64 GB disk.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f207845d994208ff1660ad2df9e045c11ca6d377ac8544937edbec1dddebfba7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDevEndpointProps(
            role_arn=role_arn,
            arguments=arguments,
            endpoint_name=endpoint_name,
            extra_jars_s3_path=extra_jars_s3_path,
            extra_python_libs_s3_path=extra_python_libs_s3_path,
            glue_version=glue_version,
            number_of_nodes=number_of_nodes,
            number_of_workers=number_of_workers,
            public_key=public_key,
            public_keys=public_keys,
            security_configuration=security_configuration,
            security_group_ids=security_group_ids,
            subnet_id=subnet_id,
            tags=tags,
            worker_type=worker_type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25858fc016328e41980e9e383fa8c74ea692bfca06ad7f98509c9506b91dffa6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__70743942c06388357f2f720c4ada83418cff43d779d1a2cadbeff13e0ec993bd)
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
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role used in this ``DevEndpoint`` .'''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3ba742e80db6ba15b810adbf5224257106f26a45069b05aa0962cf9d1acae18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="arguments")
    def arguments(self) -> typing.Any:
        '''A map of arguments used to configure the ``DevEndpoint`` .'''
        return typing.cast(typing.Any, jsii.get(self, "arguments"))

    @arguments.setter
    def arguments(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f7cd2d66e90d13b73d70f0cea82d85557e58e9448ea913c041c3bb9890fac7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arguments", value)

    @builtins.property
    @jsii.member(jsii_name="endpointName")
    def endpoint_name(self) -> typing.Optional[builtins.str]:
        '''The name of the ``DevEndpoint`` .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointName"))

    @endpoint_name.setter
    def endpoint_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3656b1b0d044829185242e72e3a9d78c819cbc0c4b0c7432f1eb535414b5b17)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointName", value)

    @builtins.property
    @jsii.member(jsii_name="extraJarsS3Path")
    def extra_jars_s3_path(self) -> typing.Optional[builtins.str]:
        '''The path to one or more Java ``.jar`` files in an S3 bucket that should be loaded in your ``DevEndpoint`` .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "extraJarsS3Path"))

    @extra_jars_s3_path.setter
    def extra_jars_s3_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e22b746e679f7c726ffcfb4c2ec05837d1aa0389da49de5598456a876e1b554a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extraJarsS3Path", value)

    @builtins.property
    @jsii.member(jsii_name="extraPythonLibsS3Path")
    def extra_python_libs_s3_path(self) -> typing.Optional[builtins.str]:
        '''The paths to one or more Python libraries in an Amazon S3 bucket that should be loaded in your ``DevEndpoint`` .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "extraPythonLibsS3Path"))

    @extra_python_libs_s3_path.setter
    def extra_python_libs_s3_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36f713fcb7ab5c574cc125a1fb44accac20e28686e76d617cf782eb65f0f7ba4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extraPythonLibsS3Path", value)

    @builtins.property
    @jsii.member(jsii_name="glueVersion")
    def glue_version(self) -> typing.Optional[builtins.str]:
        '''The AWS Glue version determines the versions of Apache Spark and Python that AWS Glue supports.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "glueVersion"))

    @glue_version.setter
    def glue_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98ce29d45190375e16a82b2017ac8c9f720adba1c61cee92540176217662a1c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "glueVersion", value)

    @builtins.property
    @jsii.member(jsii_name="numberOfNodes")
    def number_of_nodes(self) -> typing.Optional[jsii.Number]:
        '''The number of AWS Glue Data Processing Units (DPUs) allocated to this ``DevEndpoint`` .'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numberOfNodes"))

    @number_of_nodes.setter
    def number_of_nodes(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4235e3cff351beb8894679d614311c5f7e1ecc504f7d84835c7517c54fc6044a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numberOfNodes", value)

    @builtins.property
    @jsii.member(jsii_name="numberOfWorkers")
    def number_of_workers(self) -> typing.Optional[jsii.Number]:
        '''The number of workers of a defined ``workerType`` that are allocated to the development endpoint.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numberOfWorkers"))

    @number_of_workers.setter
    def number_of_workers(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9452cc6cc6f8a5fd5473515eef605e3672e7be0d39a719c23950636d6003249a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numberOfWorkers", value)

    @builtins.property
    @jsii.member(jsii_name="publicKey")
    def public_key(self) -> typing.Optional[builtins.str]:
        '''The public key to be used by this ``DevEndpoint`` for authentication.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicKey"))

    @public_key.setter
    def public_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb34f4cce325bffcbaf7901df0a55caf15f7878b322e8314762796d8323cfc20)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicKey", value)

    @builtins.property
    @jsii.member(jsii_name="publicKeys")
    def public_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of public keys to be used by the ``DevEndpoints`` for authentication.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "publicKeys"))

    @public_keys.setter
    def public_keys(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8943aff10625ef6c28e1a4686a3e4090206cdedd2fc46827336359b904a9cdbb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicKeys", value)

    @builtins.property
    @jsii.member(jsii_name="securityConfiguration")
    def security_configuration(self) -> typing.Optional[builtins.str]:
        '''The name of the ``SecurityConfiguration`` structure to be used with this ``DevEndpoint`` .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityConfiguration"))

    @security_configuration.setter
    def security_configuration(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec27168647e97503a81f083dd382a6a5792e1c7a34be7ce7c8e3ce1b24ca0eca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of security group identifiers used in this ``DevEndpoint`` .'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc83e99874e70b5e3e40d0d86646d5472a372806976261bd02f95cbed414fd29)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''The subnet ID for this ``DevEndpoint`` .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1fd805ade2dd824f981ba7d8026f5d5425fb676f266db5338e748229fe33c40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Any:
        '''The tags to use with this DevEndpoint.'''
        return typing.cast(typing.Any, jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03002f2a13cc3cbf7cf9bb6d6a81931afcc4646ea26bd164b4b95dcd73f6fa3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="workerType")
    def worker_type(self) -> typing.Optional[builtins.str]:
        '''The type of predefined worker that is allocated to the development endpoint.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workerType"))

    @worker_type.setter
    def worker_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce7ed9ca11cbfba09db8e54f347bcd3ff43297ea4bb0dc406683cb9e0186fa1e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workerType", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_glue.CfnDevEndpointProps",
    jsii_struct_bases=[],
    name_mapping={
        "role_arn": "roleArn",
        "arguments": "arguments",
        "endpoint_name": "endpointName",
        "extra_jars_s3_path": "extraJarsS3Path",
        "extra_python_libs_s3_path": "extraPythonLibsS3Path",
        "glue_version": "glueVersion",
        "number_of_nodes": "numberOfNodes",
        "number_of_workers": "numberOfWorkers",
        "public_key": "publicKey",
        "public_keys": "publicKeys",
        "security_configuration": "securityConfiguration",
        "security_group_ids": "securityGroupIds",
        "subnet_id": "subnetId",
        "tags": "tags",
        "worker_type": "workerType",
    },
)
class CfnDevEndpointProps:
    def __init__(
        self,
        *,
        role_arn: builtins.str,
        arguments: typing.Any = None,
        endpoint_name: typing.Optional[builtins.str] = None,
        extra_jars_s3_path: typing.Optional[builtins.str] = None,
        extra_python_libs_s3_path: typing.Optional[builtins.str] = None,
        glue_version: typing.Optional[builtins.str] = None,
        number_of_nodes: typing.Optional[jsii.Number] = None,
        number_of_workers: typing.Optional[jsii.Number] = None,
        public_key: typing.Optional[builtins.str] = None,
        public_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        security_configuration: typing.Optional[builtins.str] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
        worker_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnDevEndpoint``.

        :param role_arn: The Amazon Resource Name (ARN) of the IAM role used in this ``DevEndpoint`` .
        :param arguments: A map of arguments used to configure the ``DevEndpoint`` . Valid arguments are: - ``"--enable-glue-datacatalog": ""`` - ``"GLUE_PYTHON_VERSION": "3"`` - ``"GLUE_PYTHON_VERSION": "2"`` You can specify a version of Python support for development endpoints by using the ``Arguments`` parameter in the ``CreateDevEndpoint`` or ``UpdateDevEndpoint`` APIs. If no arguments are provided, the version defaults to Python 2.
        :param endpoint_name: The name of the ``DevEndpoint`` .
        :param extra_jars_s3_path: The path to one or more Java ``.jar`` files in an S3 bucket that should be loaded in your ``DevEndpoint`` . .. epigraph:: You can only use pure Java/Scala libraries with a ``DevEndpoint`` .
        :param extra_python_libs_s3_path: The paths to one or more Python libraries in an Amazon S3 bucket that should be loaded in your ``DevEndpoint`` . Multiple values must be complete paths separated by a comma. .. epigraph:: You can only use pure Python libraries with a ``DevEndpoint`` . Libraries that rely on C extensions, such as the `pandas <https://docs.aws.amazon.com/http://pandas.pydata.org/>`_ Python data analysis library, are not currently supported.
        :param glue_version: The AWS Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The Python version indicates the version supported for running your ETL scripts on development endpoints. For more information about the available AWS Glue versions and corresponding Spark and Python versions, see `Glue version <https://docs.aws.amazon.com/glue/latest/dg/add-job.html>`_ in the developer guide. Development endpoints that are created without specifying a Glue version default to Glue 0.9. You can specify a version of Python support for development endpoints by using the ``Arguments`` parameter in the ``CreateDevEndpoint`` or ``UpdateDevEndpoint`` APIs. If no arguments are provided, the version defaults to Python 2.
        :param number_of_nodes: The number of AWS Glue Data Processing Units (DPUs) allocated to this ``DevEndpoint`` .
        :param number_of_workers: The number of workers of a defined ``workerType`` that are allocated to the development endpoint. The maximum number of workers you can define are 299 for ``G.1X`` , and 149 for ``G.2X`` .
        :param public_key: The public key to be used by this ``DevEndpoint`` for authentication. This attribute is provided for backward compatibility because the recommended attribute to use is public keys.
        :param public_keys: A list of public keys to be used by the ``DevEndpoints`` for authentication. Using this attribute is preferred over a single public key because the public keys allow you to have a different private key per client. .. epigraph:: If you previously created an endpoint with a public key, you must remove that key to be able to set a list of public keys. Call the ``UpdateDevEndpoint`` API operation with the public key content in the ``deletePublicKeys`` attribute, and the list of new keys in the ``addPublicKeys`` attribute.
        :param security_configuration: The name of the ``SecurityConfiguration`` structure to be used with this ``DevEndpoint`` .
        :param security_group_ids: A list of security group identifiers used in this ``DevEndpoint`` .
        :param subnet_id: The subnet ID for this ``DevEndpoint`` .
        :param tags: The tags to use with this DevEndpoint.
        :param worker_type: The type of predefined worker that is allocated to the development endpoint. Accepts a value of Standard, G.1X, or G.2X. - For the ``Standard`` worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker. - For the ``G.1X`` worker type, each worker maps to 1 DPU (4 vCPU, 16 GB of memory, 64 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs. - For the ``G.2X`` worker type, each worker maps to 2 DPU (8 vCPU, 32 GB of memory, 128 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs. Known issue: when a development endpoint is created with the ``G.2X`` ``WorkerType`` configuration, the Spark drivers for the development endpoint will run on 4 vCPU, 16 GB of memory, and a 64 GB disk.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_glue as glue
            
            # arguments_: Any
            # tags: Any
            
            cfn_dev_endpoint_props = glue.CfnDevEndpointProps(
                role_arn="roleArn",
            
                # the properties below are optional
                arguments=arguments_,
                endpoint_name="endpointName",
                extra_jars_s3_path="extraJarsS3Path",
                extra_python_libs_s3_path="extraPythonLibsS3Path",
                glue_version="glueVersion",
                number_of_nodes=123,
                number_of_workers=123,
                public_key="publicKey",
                public_keys=["publicKeys"],
                security_configuration="securityConfiguration",
                security_group_ids=["securityGroupIds"],
                subnet_id="subnetId",
                tags=tags,
                worker_type="workerType"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__789306655393b50bec94a0cbbc4385fd0d7103127d033ea3eaabe59af1f46804)
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument arguments", value=arguments, expected_type=type_hints["arguments"])
            check_type(argname="argument endpoint_name", value=endpoint_name, expected_type=type_hints["endpoint_name"])
            check_type(argname="argument extra_jars_s3_path", value=extra_jars_s3_path, expected_type=type_hints["extra_jars_s3_path"])
            check_type(argname="argument extra_python_libs_s3_path", value=extra_python_libs_s3_path, expected_type=type_hints["extra_python_libs_s3_path"])
            check_type(argname="argument glue_version", value=glue_version, expected_type=type_hints["glue_version"])
            check_type(argname="argument number_of_nodes", value=number_of_nodes, expected_type=type_hints["number_of_nodes"])
            check_type(argname="argument number_of_workers", value=number_of_workers, expected_type=type_hints["number_of_workers"])
            check_type(argname="argument public_key", value=public_key, expected_type=type_hints["public_key"])
            check_type(argname="argument public_keys", value=public_keys, expected_type=type_hints["public_keys"])
            check_type(argname="argument security_configuration", value=security_configuration, expected_type=type_hints["security_configuration"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument worker_type", value=worker_type, expected_type=type_hints["worker_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role_arn": role_arn,
        }
        if arguments is not None:
            self._values["arguments"] = arguments
        if endpoint_name is not None:
            self._values["endpoint_name"] = endpoint_name
        if extra_jars_s3_path is not None:
            self._values["extra_jars_s3_path"] = extra_jars_s3_path
        if extra_python_libs_s3_path is not None:
            self._values["extra_python_libs_s3_path"] = extra_python_libs_s3_path
        if glue_version is not None:
            self._values["glue_version"] = glue_version
        if number_of_nodes is not None:
            self._values["number_of_nodes"] = number_of_nodes
        if number_of_workers is not None:
            self._values["number_of_workers"] = number_of_workers
        if public_key is not None:
            self._values["public_key"] = public_key
        if public_keys is not None:
            self._values["public_keys"] = public_keys
        if security_configuration is not None:
            self._values["security_configuration"] = security_configuration
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if subnet_id is not None:
            self._values["subnet_id"] = subnet_id
        if tags is not None:
            self._values["tags"] = tags
        if worker_type is not None:
            self._values["worker_type"] = worker_type

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role used in this ``DevEndpoint`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html#cfn-glue-devendpoint-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def arguments(self) -> typing.Any:
        '''A map of arguments used to configure the ``DevEndpoint`` .

        Valid arguments are:

        - ``"--enable-glue-datacatalog": ""``
        - ``"GLUE_PYTHON_VERSION": "3"``
        - ``"GLUE_PYTHON_VERSION": "2"``

        You can specify a version of Python support for development endpoints by using the ``Arguments`` parameter in the ``CreateDevEndpoint`` or ``UpdateDevEndpoint`` APIs. If no arguments are provided, the version defaults to Python 2.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html#cfn-glue-devendpoint-arguments
        '''
        result = self._values.get("arguments")
        return typing.cast(typing.Any, result)

    @builtins.property
    def endpoint_name(self) -> typing.Optional[builtins.str]:
        '''The name of the ``DevEndpoint`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html#cfn-glue-devendpoint-endpointname
        '''
        result = self._values.get("endpoint_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extra_jars_s3_path(self) -> typing.Optional[builtins.str]:
        '''The path to one or more Java ``.jar`` files in an S3 bucket that should be loaded in your ``DevEndpoint`` .

        .. epigraph::

           You can only use pure Java/Scala libraries with a ``DevEndpoint`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html#cfn-glue-devendpoint-extrajarss3path
        '''
        result = self._values.get("extra_jars_s3_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extra_python_libs_s3_path(self) -> typing.Optional[builtins.str]:
        '''The paths to one or more Python libraries in an Amazon S3 bucket that should be loaded in your ``DevEndpoint`` .

        Multiple values must be complete paths separated by a comma.
        .. epigraph::

           You can only use pure Python libraries with a ``DevEndpoint`` . Libraries that rely on C extensions, such as the `pandas <https://docs.aws.amazon.com/http://pandas.pydata.org/>`_ Python data analysis library, are not currently supported.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html#cfn-glue-devendpoint-extrapythonlibss3path
        '''
        result = self._values.get("extra_python_libs_s3_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def glue_version(self) -> typing.Optional[builtins.str]:
        '''The AWS Glue version determines the versions of Apache Spark and Python that AWS Glue supports.

        The Python version indicates the version supported for running your ETL scripts on development endpoints.

        For more information about the available AWS Glue versions and corresponding Spark and Python versions, see `Glue version <https://docs.aws.amazon.com/glue/latest/dg/add-job.html>`_ in the developer guide.

        Development endpoints that are created without specifying a Glue version default to Glue 0.9.

        You can specify a version of Python support for development endpoints by using the ``Arguments`` parameter in the ``CreateDevEndpoint`` or ``UpdateDevEndpoint`` APIs. If no arguments are provided, the version defaults to Python 2.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html#cfn-glue-devendpoint-glueversion
        '''
        result = self._values.get("glue_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def number_of_nodes(self) -> typing.Optional[jsii.Number]:
        '''The number of AWS Glue Data Processing Units (DPUs) allocated to this ``DevEndpoint`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html#cfn-glue-devendpoint-numberofnodes
        '''
        result = self._values.get("number_of_nodes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def number_of_workers(self) -> typing.Optional[jsii.Number]:
        '''The number of workers of a defined ``workerType`` that are allocated to the development endpoint.

        The maximum number of workers you can define are 299 for ``G.1X`` , and 149 for ``G.2X`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html#cfn-glue-devendpoint-numberofworkers
        '''
        result = self._values.get("number_of_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def public_key(self) -> typing.Optional[builtins.str]:
        '''The public key to be used by this ``DevEndpoint`` for authentication.

        This attribute is provided for backward compatibility because the recommended attribute to use is public keys.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html#cfn-glue-devendpoint-publickey
        '''
        result = self._values.get("public_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of public keys to be used by the ``DevEndpoints`` for authentication.

        Using this attribute is preferred over a single public key because the public keys allow you to have a different private key per client.
        .. epigraph::

           If you previously created an endpoint with a public key, you must remove that key to be able to set a list of public keys. Call the ``UpdateDevEndpoint`` API operation with the public key content in the ``deletePublicKeys`` attribute, and the list of new keys in the ``addPublicKeys`` attribute.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html#cfn-glue-devendpoint-publickeys
        '''
        result = self._values.get("public_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def security_configuration(self) -> typing.Optional[builtins.str]:
        '''The name of the ``SecurityConfiguration`` structure to be used with this ``DevEndpoint`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html#cfn-glue-devendpoint-securityconfiguration
        '''
        result = self._values.get("security_configuration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of security group identifiers used in this ``DevEndpoint`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html#cfn-glue-devendpoint-securitygroupids
        '''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''The subnet ID for this ``DevEndpoint`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html#cfn-glue-devendpoint-subnetid
        '''
        result = self._values.get("subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''The tags to use with this DevEndpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html#cfn-glue-devendpoint-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    @builtins.property
    def worker_type(self) -> typing.Optional[builtins.str]:
        '''The type of predefined worker that is allocated to the development endpoint.

        Accepts a value of Standard, G.1X, or G.2X.

        - For the ``Standard`` worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.
        - For the ``G.1X`` worker type, each worker maps to 1 DPU (4 vCPU, 16 GB of memory, 64 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.
        - For the ``G.2X`` worker type, each worker maps to 2 DPU (8 vCPU, 32 GB of memory, 128 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.

        Known issue: when a development endpoint is created with the ``G.2X`` ``WorkerType`` configuration, the Spark drivers for the development endpoint will run on 4 vCPU, 16 GB of memory, and a 64 GB disk.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html#cfn-glue-devendpoint-workertype
        '''
        result = self._values.get("worker_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDevEndpointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnJob(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_glue.CfnJob",
):
    '''The ``AWS::Glue::Job`` resource specifies an AWS Glue job in the data catalog.

    For more information, see `Adding Jobs in AWS Glue <https://docs.aws.amazon.com/glue/latest/dg/add-job.html>`_ and `Job Structure <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-job.html#aws-glue-api-jobs-job-Job>`_ in the *AWS Glue Developer Guide.*

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_glue as glue
        
        # default_arguments: Any
        # non_overridable_arguments: Any
        # tags: Any
        
        cfn_job = glue.CfnJob(self, "MyCfnJob",
            command=glue.CfnJob.JobCommandProperty(
                name="name",
                python_version="pythonVersion",
                runtime="runtime",
                script_location="scriptLocation"
            ),
            role="role",
        
            # the properties below are optional
            allocated_capacity=123,
            connections=glue.CfnJob.ConnectionsListProperty(
                connections=["connections"]
            ),
            default_arguments=default_arguments,
            description="description",
            execution_class="executionClass",
            execution_property=glue.CfnJob.ExecutionPropertyProperty(
                max_concurrent_runs=123
            ),
            glue_version="glueVersion",
            log_uri="logUri",
            max_capacity=123,
            max_retries=123,
            name="name",
            non_overridable_arguments=non_overridable_arguments,
            notification_property=glue.CfnJob.NotificationPropertyProperty(
                notify_delay_after=123
            ),
            number_of_workers=123,
            security_configuration="securityConfiguration",
            tags=tags,
            timeout=123,
            worker_type="workerType"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        command: typing.Union[_IResolvable_da3f097b, typing.Union["CfnJob.JobCommandProperty", typing.Dict[builtins.str, typing.Any]]],
        role: builtins.str,
        allocated_capacity: typing.Optional[jsii.Number] = None,
        connections: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJob.ConnectionsListProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        default_arguments: typing.Any = None,
        description: typing.Optional[builtins.str] = None,
        execution_class: typing.Optional[builtins.str] = None,
        execution_property: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJob.ExecutionPropertyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        glue_version: typing.Optional[builtins.str] = None,
        log_uri: typing.Optional[builtins.str] = None,
        max_capacity: typing.Optional[jsii.Number] = None,
        max_retries: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        non_overridable_arguments: typing.Any = None,
        notification_property: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJob.NotificationPropertyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        number_of_workers: typing.Optional[jsii.Number] = None,
        security_configuration: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
        timeout: typing.Optional[jsii.Number] = None,
        worker_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param command: The code that executes a job.
        :param role: The name or Amazon Resource Name (ARN) of the IAM role associated with this job.
        :param allocated_capacity: This parameter is no longer supported. Use ``MaxCapacity`` instead. The number of capacity units that are allocated to this job.
        :param connections: The connections used for this job.
        :param default_arguments: The default arguments for this job, specified as name-value pairs. You can specify arguments here that your own job-execution script consumes, in addition to arguments that AWS Glue itself consumes. For information about how to specify and consume your own job arguments, see `Calling AWS Glue APIs in Python <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`_ in the *AWS Glue Developer Guide* . For information about the key-value pairs that AWS Glue consumes to set up your job, see `Special Parameters Used by AWS Glue <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`_ in the *AWS Glue Developer Guide* .
        :param description: A description of the job.
        :param execution_class: Indicates whether the job is run with a standard or flexible execution class. The standard execution class is ideal for time-sensitive workloads that require fast job startup and dedicated resources. The flexible execution class is appropriate for time-insensitive jobs whose start and completion times may vary. Only jobs with AWS Glue version 3.0 and above and command type ``glueetl`` will be allowed to set ``ExecutionClass`` to ``FLEX`` . The flexible execution class is available for Spark jobs.
        :param execution_property: The maximum number of concurrent runs that are allowed for this job.
        :param glue_version: Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The Python version indicates the version supported for jobs of type Spark. For more information about the available AWS Glue versions and corresponding Spark and Python versions, see `Glue version <https://docs.aws.amazon.com/glue/latest/dg/add-job.html>`_ in the developer guide. Jobs that are created without specifying a Glue version default to Glue 0.9.
        :param log_uri: This field is reserved for future use.
        :param max_capacity: The number of AWS Glue data processing units (DPUs) that can be allocated when this job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. Do not set ``Max Capacity`` if using ``WorkerType`` and ``NumberOfWorkers`` . The value that can be allocated for ``MaxCapacity`` depends on whether you are running a Python shell job or an Apache Spark ETL job: - When you specify a Python shell job ( ``JobCommand.Name`` ="pythonshell"), you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU. - When you specify an Apache Spark ETL job ( ``JobCommand.Name`` ="glueetl"), you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a fractional DPU allocation.
        :param max_retries: The maximum number of times to retry this job after a JobRun fails.
        :param name: The name you assign to this job definition.
        :param non_overridable_arguments: Non-overridable arguments for this job, specified as name-value pairs.
        :param notification_property: Specifies configuration properties of a notification.
        :param number_of_workers: The number of workers of a defined ``workerType`` that are allocated when a job runs. The maximum number of workers you can define are 299 for ``G.1X`` , and 149 for ``G.2X`` .
        :param security_configuration: The name of the ``SecurityConfiguration`` structure to be used with this job.
        :param tags: The tags to use with this job.
        :param timeout: The job timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours).
        :param worker_type: The type of predefined worker that is allocated when a job runs. Accepts a value of G.1X, G.2X, G.4X, G.8X or G.025X for Spark jobs. Accepts the value Z.2X for Ray jobs. - For the ``G.1X`` worker type, each worker maps to 1 DPU (4 vCPUs, 16 GB of memory) with 84GB disk (approximately 34GB free), and provides 1 executor per worker. We recommend this worker type for workloads such as data transforms, joins, and queries, to offers a scalable and cost effective way to run most jobs. - For the ``G.2X`` worker type, each worker maps to 2 DPU (8 vCPUs, 32 GB of memory) with 128GB disk (approximately 77GB free), and provides 1 executor per worker. We recommend this worker type for workloads such as data transforms, joins, and queries, to offers a scalable and cost effective way to run most jobs. - For the ``G.4X`` worker type, each worker maps to 4 DPU (16 vCPUs, 64 GB of memory) with 256GB disk (approximately 235GB free), and provides 1 executor per worker. We recommend this worker type for jobs whose workloads contain your most demanding transforms, aggregations, joins, and queries. This worker type is available only for AWS Glue version 3.0 or later Spark ETL jobs in the following AWS Regions: US East (Ohio), US East (N. Virginia), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Canada (Central), Europe (Frankfurt), Europe (Ireland), and Europe (Stockholm). - For the ``G.8X`` worker type, each worker maps to 8 DPU (32 vCPUs, 128 GB of memory) with 512GB disk (approximately 487GB free), and provides 1 executor per worker. We recommend this worker type for jobs whose workloads contain your most demanding transforms, aggregations, joins, and queries. This worker type is available only for AWS Glue version 3.0 or later Spark ETL jobs, in the same AWS Regions as supported for the ``G.4X`` worker type. - For the ``G.025X`` worker type, each worker maps to 0.25 DPU (2 vCPUs, 4 GB of memory) with 84GB disk (approximately 34GB free), and provides 1 executor per worker. We recommend this worker type for low volume streaming jobs. This worker type is only available for AWS Glue version 3.0 streaming jobs. - For the ``Z.2X`` worker type, each worker maps to 2 M-DPU (8vCPUs, 64 GB of memory) with 128 GB disk (approximately 120GB free), and provides up to 8 Ray workers based on the autoscaler.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bea698eff4ea1d2bc08b1ab842f318f77ba719c0241a0959453e26989b5b53e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnJobProps(
            command=command,
            role=role,
            allocated_capacity=allocated_capacity,
            connections=connections,
            default_arguments=default_arguments,
            description=description,
            execution_class=execution_class,
            execution_property=execution_property,
            glue_version=glue_version,
            log_uri=log_uri,
            max_capacity=max_capacity,
            max_retries=max_retries,
            name=name,
            non_overridable_arguments=non_overridable_arguments,
            notification_property=notification_property,
            number_of_workers=number_of_workers,
            security_configuration=security_configuration,
            tags=tags,
            timeout=timeout,
            worker_type=worker_type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d425131e9ab8979b5db307155c42bb9935456dd21866bba5ed461a9c8c90df3c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ff736c600c4721825d122a059a265a3c60efe89b58ef836fd0db2d0e1b7f6ae1)
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
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="command")
    def command(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnJob.JobCommandProperty"]:
        '''The code that executes a job.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnJob.JobCommandProperty"], jsii.get(self, "command"))

    @command.setter
    def command(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnJob.JobCommandProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92e6559d7b7e4750985b75f86ff0ead213e6dcf804f0f9d87d12c5dd11ef4b68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "command", value)

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        '''The name or Amazon Resource Name (ARN) of the IAM role associated with this job.'''
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6215be83f5dcb82628d4c0f7daff3e6e5a40b7ba8133cbdd559c85f264c8248)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value)

    @builtins.property
    @jsii.member(jsii_name="allocatedCapacity")
    def allocated_capacity(self) -> typing.Optional[jsii.Number]:
        '''This parameter is no longer supported.

        Use ``MaxCapacity`` instead.
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "allocatedCapacity"))

    @allocated_capacity.setter
    def allocated_capacity(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e8f0c1f38624103ad14795e648b3d5168a0409e14719e267939220545367271)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocatedCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="connections")
    def connections(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJob.ConnectionsListProperty"]]:
        '''The connections used for this job.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJob.ConnectionsListProperty"]], jsii.get(self, "connections"))

    @connections.setter
    def connections(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJob.ConnectionsListProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54148ad575a4b3d562b59f1200c3e45bd7838ddba81c25e024f8359b11bcc075)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connections", value)

    @builtins.property
    @jsii.member(jsii_name="defaultArguments")
    def default_arguments(self) -> typing.Any:
        '''The default arguments for this job, specified as name-value pairs.'''
        return typing.cast(typing.Any, jsii.get(self, "defaultArguments"))

    @default_arguments.setter
    def default_arguments(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e02555d63017f6d2d384ad19fac040a7af8d997186aa0f5944d58f0edeb3d405)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultArguments", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the job.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c83f3f89400406aba1208c6fc333278a0e35af3b3730a8e266df0815d59250ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="executionClass")
    def execution_class(self) -> typing.Optional[builtins.str]:
        '''Indicates whether the job is run with a standard or flexible execution class.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionClass"))

    @execution_class.setter
    def execution_class(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c98638b6313e2e604e3d982eb0c830608a266977cd3c1a3547296e48a712e454)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionClass", value)

    @builtins.property
    @jsii.member(jsii_name="executionProperty")
    def execution_property(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJob.ExecutionPropertyProperty"]]:
        '''The maximum number of concurrent runs that are allowed for this job.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJob.ExecutionPropertyProperty"]], jsii.get(self, "executionProperty"))

    @execution_property.setter
    def execution_property(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJob.ExecutionPropertyProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__288a9558b01117977548bd27d8b359f6aabd127fbbae8871f921f4f4ad731aa0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionProperty", value)

    @builtins.property
    @jsii.member(jsii_name="glueVersion")
    def glue_version(self) -> typing.Optional[builtins.str]:
        '''Glue version determines the versions of Apache Spark and Python that AWS Glue supports.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "glueVersion"))

    @glue_version.setter
    def glue_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f36e5a6a7d1a062f3bf5d8b7176a1f0f8c07bc3e7e725aefec8d86d74b346411)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "glueVersion", value)

    @builtins.property
    @jsii.member(jsii_name="logUri")
    def log_uri(self) -> typing.Optional[builtins.str]:
        '''This field is reserved for future use.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logUri"))

    @log_uri.setter
    def log_uri(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ca81eaaed120981305eb66586283b558b72d3b37cb0098234ec82c56f1d637a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logUri", value)

    @builtins.property
    @jsii.member(jsii_name="maxCapacity")
    def max_capacity(self) -> typing.Optional[jsii.Number]:
        '''The number of AWS Glue data processing units (DPUs) that can be allocated when this job runs.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxCapacity"))

    @max_capacity.setter
    def max_capacity(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a764dd1178d54ad958e98a11fae132faf1dc82baf8cc6de7a480139bec56d6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="maxRetries")
    def max_retries(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry this job after a JobRun fails.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRetries"))

    @max_retries.setter
    def max_retries(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__747e11b9e0393534a2a604c6185f8016b6350fbf93c4b5cc55c96315ddb87867)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxRetries", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name you assign to this job definition.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34834931355b72bf0842139ae8010d5c3e556cc67c00f907c4e39b8297ecae5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="nonOverridableArguments")
    def non_overridable_arguments(self) -> typing.Any:
        '''Non-overridable arguments for this job, specified as name-value pairs.'''
        return typing.cast(typing.Any, jsii.get(self, "nonOverridableArguments"))

    @non_overridable_arguments.setter
    def non_overridable_arguments(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68288520cd14059f70bcdca01796f4f53b90b28bd9200d4a3771f70a8977093c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nonOverridableArguments", value)

    @builtins.property
    @jsii.member(jsii_name="notificationProperty")
    def notification_property(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJob.NotificationPropertyProperty"]]:
        '''Specifies configuration properties of a notification.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJob.NotificationPropertyProperty"]], jsii.get(self, "notificationProperty"))

    @notification_property.setter
    def notification_property(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJob.NotificationPropertyProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__886cabf7d73da58088c752153f330c0b15d55d0334b2e6e1429c361c244fa40b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationProperty", value)

    @builtins.property
    @jsii.member(jsii_name="numberOfWorkers")
    def number_of_workers(self) -> typing.Optional[jsii.Number]:
        '''The number of workers of a defined ``workerType`` that are allocated when a job runs.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numberOfWorkers"))

    @number_of_workers.setter
    def number_of_workers(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3dd8b61874c785b7e401c38c72a26b663aafa165c05e223526a1b04215648b44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numberOfWorkers", value)

    @builtins.property
    @jsii.member(jsii_name="securityConfiguration")
    def security_configuration(self) -> typing.Optional[builtins.str]:
        '''The name of the ``SecurityConfiguration`` structure to be used with this job.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityConfiguration"))

    @security_configuration.setter
    def security_configuration(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__686551f876de8c0263f876f1f95fa84db57247f0bfd43e39fd7e27705da22d75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Any:
        '''The tags to use with this job.'''
        return typing.cast(typing.Any, jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__542d438feaf9522e0e8293fe9c53267730a064a757ebc71e8aa9fd97d002c38c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> typing.Optional[jsii.Number]:
        '''The job timeout in minutes.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c12c03e51261ea1008482a07620562f930d2ee59fec35bf127da7d754e08de3d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value)

    @builtins.property
    @jsii.member(jsii_name="workerType")
    def worker_type(self) -> typing.Optional[builtins.str]:
        '''The type of predefined worker that is allocated when a job runs.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workerType"))

    @worker_type.setter
    def worker_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6b16368f5ffc1ef3ea15b397687a68037aa7eebf6a316b97ece9c4f3e17d49f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workerType", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnJob.ConnectionsListProperty",
        jsii_struct_bases=[],
        name_mapping={"connections": "connections"},
    )
    class ConnectionsListProperty:
        def __init__(
            self,
            *,
            connections: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Specifies the connections used by a job.

            :param connections: A list of connections used by the job.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-connectionslist.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                connections_list_property = glue.CfnJob.ConnectionsListProperty(
                    connections=["connections"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3c7dc433e6f7c5ca3d12814ece3fac51b4dbb146e7e2fd378ced704cb23f9b13)
                check_type(argname="argument connections", value=connections, expected_type=type_hints["connections"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if connections is not None:
                self._values["connections"] = connections

        @builtins.property
        def connections(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of connections used by the job.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-connectionslist.html#cfn-glue-job-connectionslist-connections
            '''
            result = self._values.get("connections")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConnectionsListProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnJob.ExecutionPropertyProperty",
        jsii_struct_bases=[],
        name_mapping={"max_concurrent_runs": "maxConcurrentRuns"},
    )
    class ExecutionPropertyProperty:
        def __init__(
            self,
            *,
            max_concurrent_runs: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''An execution property of a job.

            :param max_concurrent_runs: The maximum number of concurrent runs allowed for the job. The default is 1. An error is returned when this threshold is reached. The maximum value you can specify is controlled by a service limit.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-executionproperty.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                execution_property_property = glue.CfnJob.ExecutionPropertyProperty(
                    max_concurrent_runs=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__520e2daea7c2ab288e9c6e2ba71dcb41ab10da7ecd61430c90a856eae7bdd314)
                check_type(argname="argument max_concurrent_runs", value=max_concurrent_runs, expected_type=type_hints["max_concurrent_runs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if max_concurrent_runs is not None:
                self._values["max_concurrent_runs"] = max_concurrent_runs

        @builtins.property
        def max_concurrent_runs(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of concurrent runs allowed for the job.

            The default is 1. An error is returned when this threshold is reached. The maximum value you can specify is controlled by a service limit.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-executionproperty.html#cfn-glue-job-executionproperty-maxconcurrentruns
            '''
            result = self._values.get("max_concurrent_runs")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExecutionPropertyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnJob.JobCommandProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "python_version": "pythonVersion",
            "runtime": "runtime",
            "script_location": "scriptLocation",
        },
    )
    class JobCommandProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            python_version: typing.Optional[builtins.str] = None,
            runtime: typing.Optional[builtins.str] = None,
            script_location: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies code executed when a job is run.

            :param name: The name of the job command. For an Apache Spark ETL job, this must be ``glueetl`` . For a Python shell job, it must be ``pythonshell`` . For an Apache Spark streaming ETL job, this must be ``gluestreaming`` . For a Ray job, this must be ``glueray`` .
            :param python_version: The Python version being used to execute a Python shell job. Allowed values are 3 or 3.9. Version 2 is deprecated.
            :param runtime: In Ray jobs, Runtime is used to specify the versions of Ray, Python and additional libraries available in your environment. This field is not used in other job types. For supported runtime environment values, see `Working with Ray jobs <https://docs.aws.amazon.com/glue/latest/dg/ray-jobs-section.html>`_ in the AWS Glue Developer Guide.
            :param script_location: Specifies the Amazon Simple Storage Service (Amazon S3) path to a script that executes a job (required).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-jobcommand.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                job_command_property = glue.CfnJob.JobCommandProperty(
                    name="name",
                    python_version="pythonVersion",
                    runtime="runtime",
                    script_location="scriptLocation"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__87fac9903ef58adfafce7d1cfda786501500eb9ea0b225cf51bfa32f2798403e)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument python_version", value=python_version, expected_type=type_hints["python_version"])
                check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
                check_type(argname="argument script_location", value=script_location, expected_type=type_hints["script_location"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if python_version is not None:
                self._values["python_version"] = python_version
            if runtime is not None:
                self._values["runtime"] = runtime
            if script_location is not None:
                self._values["script_location"] = script_location

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the job command.

            For an Apache Spark ETL job, this must be ``glueetl`` . For a Python shell job, it must be ``pythonshell`` . For an Apache Spark streaming ETL job, this must be ``gluestreaming`` . For a Ray job, this must be ``glueray`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-jobcommand.html#cfn-glue-job-jobcommand-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def python_version(self) -> typing.Optional[builtins.str]:
            '''The Python version being used to execute a Python shell job.

            Allowed values are 3 or 3.9. Version 2 is deprecated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-jobcommand.html#cfn-glue-job-jobcommand-pythonversion
            '''
            result = self._values.get("python_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def runtime(self) -> typing.Optional[builtins.str]:
            '''In Ray jobs, Runtime is used to specify the versions of Ray, Python and additional libraries available in your environment.

            This field is not used in other job types. For supported runtime environment values, see `Working with Ray jobs <https://docs.aws.amazon.com/glue/latest/dg/ray-jobs-section.html>`_ in the AWS Glue Developer Guide.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-jobcommand.html#cfn-glue-job-jobcommand-runtime
            '''
            result = self._values.get("runtime")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def script_location(self) -> typing.Optional[builtins.str]:
            '''Specifies the Amazon Simple Storage Service (Amazon S3) path to a script that executes a job (required).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-jobcommand.html#cfn-glue-job-jobcommand-scriptlocation
            '''
            result = self._values.get("script_location")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JobCommandProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnJob.NotificationPropertyProperty",
        jsii_struct_bases=[],
        name_mapping={"notify_delay_after": "notifyDelayAfter"},
    )
    class NotificationPropertyProperty:
        def __init__(
            self,
            *,
            notify_delay_after: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Specifies configuration properties of a notification.

            :param notify_delay_after: After a job run starts, the number of minutes to wait before sending a job run delay notification.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-notificationproperty.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                notification_property_property = glue.CfnJob.NotificationPropertyProperty(
                    notify_delay_after=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0d87f46f82fb4abde6f1cc1fdfc015cb65e4bb0f311eb52da272f4e484d5117b)
                check_type(argname="argument notify_delay_after", value=notify_delay_after, expected_type=type_hints["notify_delay_after"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if notify_delay_after is not None:
                self._values["notify_delay_after"] = notify_delay_after

        @builtins.property
        def notify_delay_after(self) -> typing.Optional[jsii.Number]:
            '''After a job run starts, the number of minutes to wait before sending a job run delay notification.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-notificationproperty.html#cfn-glue-job-notificationproperty-notifydelayafter
            '''
            result = self._values.get("notify_delay_after")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NotificationPropertyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_glue.CfnJobProps",
    jsii_struct_bases=[],
    name_mapping={
        "command": "command",
        "role": "role",
        "allocated_capacity": "allocatedCapacity",
        "connections": "connections",
        "default_arguments": "defaultArguments",
        "description": "description",
        "execution_class": "executionClass",
        "execution_property": "executionProperty",
        "glue_version": "glueVersion",
        "log_uri": "logUri",
        "max_capacity": "maxCapacity",
        "max_retries": "maxRetries",
        "name": "name",
        "non_overridable_arguments": "nonOverridableArguments",
        "notification_property": "notificationProperty",
        "number_of_workers": "numberOfWorkers",
        "security_configuration": "securityConfiguration",
        "tags": "tags",
        "timeout": "timeout",
        "worker_type": "workerType",
    },
)
class CfnJobProps:
    def __init__(
        self,
        *,
        command: typing.Union[_IResolvable_da3f097b, typing.Union[CfnJob.JobCommandProperty, typing.Dict[builtins.str, typing.Any]]],
        role: builtins.str,
        allocated_capacity: typing.Optional[jsii.Number] = None,
        connections: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJob.ConnectionsListProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        default_arguments: typing.Any = None,
        description: typing.Optional[builtins.str] = None,
        execution_class: typing.Optional[builtins.str] = None,
        execution_property: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJob.ExecutionPropertyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        glue_version: typing.Optional[builtins.str] = None,
        log_uri: typing.Optional[builtins.str] = None,
        max_capacity: typing.Optional[jsii.Number] = None,
        max_retries: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        non_overridable_arguments: typing.Any = None,
        notification_property: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJob.NotificationPropertyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        number_of_workers: typing.Optional[jsii.Number] = None,
        security_configuration: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
        timeout: typing.Optional[jsii.Number] = None,
        worker_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnJob``.

        :param command: The code that executes a job.
        :param role: The name or Amazon Resource Name (ARN) of the IAM role associated with this job.
        :param allocated_capacity: This parameter is no longer supported. Use ``MaxCapacity`` instead. The number of capacity units that are allocated to this job.
        :param connections: The connections used for this job.
        :param default_arguments: The default arguments for this job, specified as name-value pairs. You can specify arguments here that your own job-execution script consumes, in addition to arguments that AWS Glue itself consumes. For information about how to specify and consume your own job arguments, see `Calling AWS Glue APIs in Python <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`_ in the *AWS Glue Developer Guide* . For information about the key-value pairs that AWS Glue consumes to set up your job, see `Special Parameters Used by AWS Glue <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`_ in the *AWS Glue Developer Guide* .
        :param description: A description of the job.
        :param execution_class: Indicates whether the job is run with a standard or flexible execution class. The standard execution class is ideal for time-sensitive workloads that require fast job startup and dedicated resources. The flexible execution class is appropriate for time-insensitive jobs whose start and completion times may vary. Only jobs with AWS Glue version 3.0 and above and command type ``glueetl`` will be allowed to set ``ExecutionClass`` to ``FLEX`` . The flexible execution class is available for Spark jobs.
        :param execution_property: The maximum number of concurrent runs that are allowed for this job.
        :param glue_version: Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The Python version indicates the version supported for jobs of type Spark. For more information about the available AWS Glue versions and corresponding Spark and Python versions, see `Glue version <https://docs.aws.amazon.com/glue/latest/dg/add-job.html>`_ in the developer guide. Jobs that are created without specifying a Glue version default to Glue 0.9.
        :param log_uri: This field is reserved for future use.
        :param max_capacity: The number of AWS Glue data processing units (DPUs) that can be allocated when this job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. Do not set ``Max Capacity`` if using ``WorkerType`` and ``NumberOfWorkers`` . The value that can be allocated for ``MaxCapacity`` depends on whether you are running a Python shell job or an Apache Spark ETL job: - When you specify a Python shell job ( ``JobCommand.Name`` ="pythonshell"), you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU. - When you specify an Apache Spark ETL job ( ``JobCommand.Name`` ="glueetl"), you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a fractional DPU allocation.
        :param max_retries: The maximum number of times to retry this job after a JobRun fails.
        :param name: The name you assign to this job definition.
        :param non_overridable_arguments: Non-overridable arguments for this job, specified as name-value pairs.
        :param notification_property: Specifies configuration properties of a notification.
        :param number_of_workers: The number of workers of a defined ``workerType`` that are allocated when a job runs. The maximum number of workers you can define are 299 for ``G.1X`` , and 149 for ``G.2X`` .
        :param security_configuration: The name of the ``SecurityConfiguration`` structure to be used with this job.
        :param tags: The tags to use with this job.
        :param timeout: The job timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours).
        :param worker_type: The type of predefined worker that is allocated when a job runs. Accepts a value of G.1X, G.2X, G.4X, G.8X or G.025X for Spark jobs. Accepts the value Z.2X for Ray jobs. - For the ``G.1X`` worker type, each worker maps to 1 DPU (4 vCPUs, 16 GB of memory) with 84GB disk (approximately 34GB free), and provides 1 executor per worker. We recommend this worker type for workloads such as data transforms, joins, and queries, to offers a scalable and cost effective way to run most jobs. - For the ``G.2X`` worker type, each worker maps to 2 DPU (8 vCPUs, 32 GB of memory) with 128GB disk (approximately 77GB free), and provides 1 executor per worker. We recommend this worker type for workloads such as data transforms, joins, and queries, to offers a scalable and cost effective way to run most jobs. - For the ``G.4X`` worker type, each worker maps to 4 DPU (16 vCPUs, 64 GB of memory) with 256GB disk (approximately 235GB free), and provides 1 executor per worker. We recommend this worker type for jobs whose workloads contain your most demanding transforms, aggregations, joins, and queries. This worker type is available only for AWS Glue version 3.0 or later Spark ETL jobs in the following AWS Regions: US East (Ohio), US East (N. Virginia), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Canada (Central), Europe (Frankfurt), Europe (Ireland), and Europe (Stockholm). - For the ``G.8X`` worker type, each worker maps to 8 DPU (32 vCPUs, 128 GB of memory) with 512GB disk (approximately 487GB free), and provides 1 executor per worker. We recommend this worker type for jobs whose workloads contain your most demanding transforms, aggregations, joins, and queries. This worker type is available only for AWS Glue version 3.0 or later Spark ETL jobs, in the same AWS Regions as supported for the ``G.4X`` worker type. - For the ``G.025X`` worker type, each worker maps to 0.25 DPU (2 vCPUs, 4 GB of memory) with 84GB disk (approximately 34GB free), and provides 1 executor per worker. We recommend this worker type for low volume streaming jobs. This worker type is only available for AWS Glue version 3.0 streaming jobs. - For the ``Z.2X`` worker type, each worker maps to 2 M-DPU (8vCPUs, 64 GB of memory) with 128 GB disk (approximately 120GB free), and provides up to 8 Ray workers based on the autoscaler.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_glue as glue
            
            # default_arguments: Any
            # non_overridable_arguments: Any
            # tags: Any
            
            cfn_job_props = glue.CfnJobProps(
                command=glue.CfnJob.JobCommandProperty(
                    name="name",
                    python_version="pythonVersion",
                    runtime="runtime",
                    script_location="scriptLocation"
                ),
                role="role",
            
                # the properties below are optional
                allocated_capacity=123,
                connections=glue.CfnJob.ConnectionsListProperty(
                    connections=["connections"]
                ),
                default_arguments=default_arguments,
                description="description",
                execution_class="executionClass",
                execution_property=glue.CfnJob.ExecutionPropertyProperty(
                    max_concurrent_runs=123
                ),
                glue_version="glueVersion",
                log_uri="logUri",
                max_capacity=123,
                max_retries=123,
                name="name",
                non_overridable_arguments=non_overridable_arguments,
                notification_property=glue.CfnJob.NotificationPropertyProperty(
                    notify_delay_after=123
                ),
                number_of_workers=123,
                security_configuration="securityConfiguration",
                tags=tags,
                timeout=123,
                worker_type="workerType"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b5bd8295520fa719be46f80478ae155292fb66f6fc3016eb114b6fabf6050df)
            check_type(argname="argument command", value=command, expected_type=type_hints["command"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument allocated_capacity", value=allocated_capacity, expected_type=type_hints["allocated_capacity"])
            check_type(argname="argument connections", value=connections, expected_type=type_hints["connections"])
            check_type(argname="argument default_arguments", value=default_arguments, expected_type=type_hints["default_arguments"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument execution_class", value=execution_class, expected_type=type_hints["execution_class"])
            check_type(argname="argument execution_property", value=execution_property, expected_type=type_hints["execution_property"])
            check_type(argname="argument glue_version", value=glue_version, expected_type=type_hints["glue_version"])
            check_type(argname="argument log_uri", value=log_uri, expected_type=type_hints["log_uri"])
            check_type(argname="argument max_capacity", value=max_capacity, expected_type=type_hints["max_capacity"])
            check_type(argname="argument max_retries", value=max_retries, expected_type=type_hints["max_retries"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument non_overridable_arguments", value=non_overridable_arguments, expected_type=type_hints["non_overridable_arguments"])
            check_type(argname="argument notification_property", value=notification_property, expected_type=type_hints["notification_property"])
            check_type(argname="argument number_of_workers", value=number_of_workers, expected_type=type_hints["number_of_workers"])
            check_type(argname="argument security_configuration", value=security_configuration, expected_type=type_hints["security_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument worker_type", value=worker_type, expected_type=type_hints["worker_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "command": command,
            "role": role,
        }
        if allocated_capacity is not None:
            self._values["allocated_capacity"] = allocated_capacity
        if connections is not None:
            self._values["connections"] = connections
        if default_arguments is not None:
            self._values["default_arguments"] = default_arguments
        if description is not None:
            self._values["description"] = description
        if execution_class is not None:
            self._values["execution_class"] = execution_class
        if execution_property is not None:
            self._values["execution_property"] = execution_property
        if glue_version is not None:
            self._values["glue_version"] = glue_version
        if log_uri is not None:
            self._values["log_uri"] = log_uri
        if max_capacity is not None:
            self._values["max_capacity"] = max_capacity
        if max_retries is not None:
            self._values["max_retries"] = max_retries
        if name is not None:
            self._values["name"] = name
        if non_overridable_arguments is not None:
            self._values["non_overridable_arguments"] = non_overridable_arguments
        if notification_property is not None:
            self._values["notification_property"] = notification_property
        if number_of_workers is not None:
            self._values["number_of_workers"] = number_of_workers
        if security_configuration is not None:
            self._values["security_configuration"] = security_configuration
        if tags is not None:
            self._values["tags"] = tags
        if timeout is not None:
            self._values["timeout"] = timeout
        if worker_type is not None:
            self._values["worker_type"] = worker_type

    @builtins.property
    def command(self) -> typing.Union[_IResolvable_da3f097b, CfnJob.JobCommandProperty]:
        '''The code that executes a job.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-command
        '''
        result = self._values.get("command")
        assert result is not None, "Required property 'command' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnJob.JobCommandProperty], result)

    @builtins.property
    def role(self) -> builtins.str:
        '''The name or Amazon Resource Name (ARN) of the IAM role associated with this job.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-role
        '''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allocated_capacity(self) -> typing.Optional[jsii.Number]:
        '''This parameter is no longer supported. Use ``MaxCapacity`` instead.

        The number of capacity units that are allocated to this job.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-allocatedcapacity
        '''
        result = self._values.get("allocated_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def connections(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnJob.ConnectionsListProperty]]:
        '''The connections used for this job.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-connections
        '''
        result = self._values.get("connections")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnJob.ConnectionsListProperty]], result)

    @builtins.property
    def default_arguments(self) -> typing.Any:
        '''The default arguments for this job, specified as name-value pairs.

        You can specify arguments here that your own job-execution script consumes, in addition to arguments that AWS Glue itself consumes.

        For information about how to specify and consume your own job arguments, see `Calling AWS Glue APIs in Python <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`_ in the *AWS Glue Developer Guide* .

        For information about the key-value pairs that AWS Glue consumes to set up your job, see `Special Parameters Used by AWS Glue <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`_ in the *AWS Glue Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-defaultarguments
        '''
        result = self._values.get("default_arguments")
        return typing.cast(typing.Any, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the job.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def execution_class(self) -> typing.Optional[builtins.str]:
        '''Indicates whether the job is run with a standard or flexible execution class.

        The standard execution class is ideal for time-sensitive workloads that require fast job startup and dedicated resources.

        The flexible execution class is appropriate for time-insensitive jobs whose start and completion times may vary.

        Only jobs with AWS Glue version 3.0 and above and command type ``glueetl`` will be allowed to set ``ExecutionClass`` to ``FLEX`` . The flexible execution class is available for Spark jobs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-executionclass
        '''
        result = self._values.get("execution_class")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def execution_property(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnJob.ExecutionPropertyProperty]]:
        '''The maximum number of concurrent runs that are allowed for this job.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-executionproperty
        '''
        result = self._values.get("execution_property")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnJob.ExecutionPropertyProperty]], result)

    @builtins.property
    def glue_version(self) -> typing.Optional[builtins.str]:
        '''Glue version determines the versions of Apache Spark and Python that AWS Glue supports.

        The Python version indicates the version supported for jobs of type Spark.

        For more information about the available AWS Glue versions and corresponding Spark and Python versions, see `Glue version <https://docs.aws.amazon.com/glue/latest/dg/add-job.html>`_ in the developer guide.

        Jobs that are created without specifying a Glue version default to Glue 0.9.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-glueversion
        '''
        result = self._values.get("glue_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_uri(self) -> typing.Optional[builtins.str]:
        '''This field is reserved for future use.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-loguri
        '''
        result = self._values.get("log_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_capacity(self) -> typing.Optional[jsii.Number]:
        '''The number of AWS Glue data processing units (DPUs) that can be allocated when this job runs.

        A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory.

        Do not set ``Max Capacity`` if using ``WorkerType`` and ``NumberOfWorkers`` .

        The value that can be allocated for ``MaxCapacity`` depends on whether you are running a Python shell job or an Apache Spark ETL job:

        - When you specify a Python shell job ( ``JobCommand.Name`` ="pythonshell"), you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.
        - When you specify an Apache Spark ETL job ( ``JobCommand.Name`` ="glueetl"), you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a fractional DPU allocation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-maxcapacity
        '''
        result = self._values.get("max_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_retries(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry this job after a JobRun fails.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-maxretries
        '''
        result = self._values.get("max_retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name you assign to this job definition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def non_overridable_arguments(self) -> typing.Any:
        '''Non-overridable arguments for this job, specified as name-value pairs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-nonoverridablearguments
        '''
        result = self._values.get("non_overridable_arguments")
        return typing.cast(typing.Any, result)

    @builtins.property
    def notification_property(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnJob.NotificationPropertyProperty]]:
        '''Specifies configuration properties of a notification.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-notificationproperty
        '''
        result = self._values.get("notification_property")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnJob.NotificationPropertyProperty]], result)

    @builtins.property
    def number_of_workers(self) -> typing.Optional[jsii.Number]:
        '''The number of workers of a defined ``workerType`` that are allocated when a job runs.

        The maximum number of workers you can define are 299 for ``G.1X`` , and 149 for ``G.2X`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-numberofworkers
        '''
        result = self._values.get("number_of_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def security_configuration(self) -> typing.Optional[builtins.str]:
        '''The name of the ``SecurityConfiguration`` structure to be used with this job.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-securityconfiguration
        '''
        result = self._values.get("security_configuration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''The tags to use with this job.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    @builtins.property
    def timeout(self) -> typing.Optional[jsii.Number]:
        '''The job timeout in minutes.

        This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-timeout
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def worker_type(self) -> typing.Optional[builtins.str]:
        '''The type of predefined worker that is allocated when a job runs.

        Accepts a value of G.1X, G.2X, G.4X, G.8X or G.025X for Spark jobs. Accepts the value Z.2X for Ray jobs.

        - For the ``G.1X`` worker type, each worker maps to 1 DPU (4 vCPUs, 16 GB of memory) with 84GB disk (approximately 34GB free), and provides 1 executor per worker. We recommend this worker type for workloads such as data transforms, joins, and queries, to offers a scalable and cost effective way to run most jobs.
        - For the ``G.2X`` worker type, each worker maps to 2 DPU (8 vCPUs, 32 GB of memory) with 128GB disk (approximately 77GB free), and provides 1 executor per worker. We recommend this worker type for workloads such as data transforms, joins, and queries, to offers a scalable and cost effective way to run most jobs.
        - For the ``G.4X`` worker type, each worker maps to 4 DPU (16 vCPUs, 64 GB of memory) with 256GB disk (approximately 235GB free), and provides 1 executor per worker. We recommend this worker type for jobs whose workloads contain your most demanding transforms, aggregations, joins, and queries. This worker type is available only for AWS Glue version 3.0 or later Spark ETL jobs in the following AWS Regions: US East (Ohio), US East (N. Virginia), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Canada (Central), Europe (Frankfurt), Europe (Ireland), and Europe (Stockholm).
        - For the ``G.8X`` worker type, each worker maps to 8 DPU (32 vCPUs, 128 GB of memory) with 512GB disk (approximately 487GB free), and provides 1 executor per worker. We recommend this worker type for jobs whose workloads contain your most demanding transforms, aggregations, joins, and queries. This worker type is available only for AWS Glue version 3.0 or later Spark ETL jobs, in the same AWS Regions as supported for the ``G.4X`` worker type.
        - For the ``G.025X`` worker type, each worker maps to 0.25 DPU (2 vCPUs, 4 GB of memory) with 84GB disk (approximately 34GB free), and provides 1 executor per worker. We recommend this worker type for low volume streaming jobs. This worker type is only available for AWS Glue version 3.0 streaming jobs.
        - For the ``Z.2X`` worker type, each worker maps to 2 M-DPU (8vCPUs, 64 GB of memory) with 128 GB disk (approximately 120GB free), and provides up to 8 Ray workers based on the autoscaler.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html#cfn-glue-job-workertype
        '''
        result = self._values.get("worker_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnJobProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnMLTransform(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_glue.CfnMLTransform",
):
    '''The AWS::Glue::MLTransform is an AWS Glue resource type that manages machine learning transforms.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_glue as glue
        
        # tags: Any
        
        cfn_mLTransform = glue.CfnMLTransform(self, "MyCfnMLTransform",
            input_record_tables=glue.CfnMLTransform.InputRecordTablesProperty(
                glue_tables=[glue.CfnMLTransform.GlueTablesProperty(
                    database_name="databaseName",
                    table_name="tableName",
        
                    # the properties below are optional
                    catalog_id="catalogId",
                    connection_name="connectionName"
                )]
            ),
            role="role",
            transform_parameters=glue.CfnMLTransform.TransformParametersProperty(
                transform_type="transformType",
        
                # the properties below are optional
                find_matches_parameters=glue.CfnMLTransform.FindMatchesParametersProperty(
                    primary_key_column_name="primaryKeyColumnName",
        
                    # the properties below are optional
                    accuracy_cost_tradeoff=123,
                    enforce_provided_labels=False,
                    precision_recall_tradeoff=123
                )
            ),
        
            # the properties below are optional
            description="description",
            glue_version="glueVersion",
            max_capacity=123,
            max_retries=123,
            name="name",
            number_of_workers=123,
            tags=tags,
            timeout=123,
            transform_encryption=glue.CfnMLTransform.TransformEncryptionProperty(
                ml_user_data_encryption=glue.CfnMLTransform.MLUserDataEncryptionProperty(
                    ml_user_data_encryption_mode="mlUserDataEncryptionMode",
        
                    # the properties below are optional
                    kms_key_id="kmsKeyId"
                ),
                task_run_security_configuration_name="taskRunSecurityConfigurationName"
            ),
            worker_type="workerType"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        input_record_tables: typing.Union[_IResolvable_da3f097b, typing.Union["CfnMLTransform.InputRecordTablesProperty", typing.Dict[builtins.str, typing.Any]]],
        role: builtins.str,
        transform_parameters: typing.Union[_IResolvable_da3f097b, typing.Union["CfnMLTransform.TransformParametersProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        glue_version: typing.Optional[builtins.str] = None,
        max_capacity: typing.Optional[jsii.Number] = None,
        max_retries: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        number_of_workers: typing.Optional[jsii.Number] = None,
        tags: typing.Any = None,
        timeout: typing.Optional[jsii.Number] = None,
        transform_encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMLTransform.TransformEncryptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        worker_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param input_record_tables: A list of AWS Glue table definitions used by the transform.
        :param role: The name or Amazon Resource Name (ARN) of the IAM role with the required permissions. The required permissions include both AWS Glue service role permissions to AWS Glue resources, and Amazon S3 permissions required by the transform. - This role needs AWS Glue service role permissions to allow access to resources in AWS Glue . See `Attach a Policy to IAM Users That Access AWS Glue <https://docs.aws.amazon.com/glue/latest/dg/attach-policy-iam-user.html>`_ . - This role needs permission to your Amazon Simple Storage Service (Amazon S3) sources, targets, temporary directory, scripts, and any libraries used by the task run for this transform.
        :param transform_parameters: The algorithm-specific parameters that are associated with the machine learning transform.
        :param description: A user-defined, long-form description text for the machine learning transform.
        :param glue_version: This value determines which version of AWS Glue this machine learning transform is compatible with. Glue 1.0 is recommended for most customers. If the value is not set, the Glue compatibility defaults to Glue 0.9. For more information, see `AWS Glue Versions <https://docs.aws.amazon.com/glue/latest/dg/release-notes.html#release-notes-versions>`_ in the developer guide.
        :param max_capacity: The number of AWS Glue data processing units (DPUs) that are allocated to task runs for this transform. You can allocate from 2 to 100 DPUs; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the `AWS Glue pricing page <https://docs.aws.amazon.com/glue/pricing/>`_ . ``MaxCapacity`` is a mutually exclusive option with ``NumberOfWorkers`` and ``WorkerType`` . - If either ``NumberOfWorkers`` or ``WorkerType`` is set, then ``MaxCapacity`` cannot be set. - If ``MaxCapacity`` is set then neither ``NumberOfWorkers`` or ``WorkerType`` can be set. - If ``WorkerType`` is set, then ``NumberOfWorkers`` is required (and vice versa). - ``MaxCapacity`` and ``NumberOfWorkers`` must both be at least 1. When the ``WorkerType`` field is set to a value other than ``Standard`` , the ``MaxCapacity`` field is set automatically and becomes read-only.
        :param max_retries: The maximum number of times to retry after an ``MLTaskRun`` of the machine learning transform fails.
        :param name: A user-defined name for the machine learning transform. Names are required to be unique. ``Name`` is optional:. - If you supply ``Name`` , the stack cannot be repeatedly created. - If ``Name`` is not provided, a randomly generated name will be used instead.
        :param number_of_workers: The number of workers of a defined ``workerType`` that are allocated when a task of the transform runs. If ``WorkerType`` is set, then ``NumberOfWorkers`` is required (and vice versa).
        :param tags: The tags to use with this machine learning transform. You may use tags to limit access to the machine learning transform. For more information about tags in AWS Glue , see `AWS Tags in AWS Glue <https://docs.aws.amazon.com/glue/latest/dg/monitor-tags.html>`_ in the developer guide.
        :param timeout: The timeout in minutes of the machine learning transform.
        :param transform_encryption: The encryption-at-rest settings of the transform that apply to accessing user data. Machine learning transforms can access user data encrypted in Amazon S3 using KMS. Additionally, imported labels and trained transforms can now be encrypted using a customer provided KMS key.
        :param worker_type: The type of predefined worker that is allocated when a task of this transform runs. Accepts a value of Standard, G.1X, or G.2X. - For the ``Standard`` worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker. - For the ``G.1X`` worker type, each worker provides 4 vCPU, 16 GB of memory and a 64GB disk, and 1 executor per worker. - For the ``G.2X`` worker type, each worker provides 8 vCPU, 32 GB of memory and a 128GB disk, and 1 executor per worker. ``MaxCapacity`` is a mutually exclusive option with ``NumberOfWorkers`` and ``WorkerType`` . - If either ``NumberOfWorkers`` or ``WorkerType`` is set, then ``MaxCapacity`` cannot be set. - If ``MaxCapacity`` is set then neither ``NumberOfWorkers`` or ``WorkerType`` can be set. - If ``WorkerType`` is set, then ``NumberOfWorkers`` is required (and vice versa). - ``MaxCapacity`` and ``NumberOfWorkers`` must both be at least 1.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53d1d58fe97e9c17e46132b4f82f741ba019c774fe0bb3bdba1d51dbefe20295)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMLTransformProps(
            input_record_tables=input_record_tables,
            role=role,
            transform_parameters=transform_parameters,
            description=description,
            glue_version=glue_version,
            max_capacity=max_capacity,
            max_retries=max_retries,
            name=name,
            number_of_workers=number_of_workers,
            tags=tags,
            timeout=timeout,
            transform_encryption=transform_encryption,
            worker_type=worker_type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17b628057d4918b2654a169e223fdc7952223107b4c9c602966d2f6978fffbac)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0a38f97a53150f570084eea59308e238fbdc6786009a78ad9b014ea3066fb96a)
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
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="inputRecordTables")
    def input_record_tables(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnMLTransform.InputRecordTablesProperty"]:
        '''A list of AWS Glue table definitions used by the transform.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnMLTransform.InputRecordTablesProperty"], jsii.get(self, "inputRecordTables"))

    @input_record_tables.setter
    def input_record_tables(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnMLTransform.InputRecordTablesProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54fd840993f985c80395aeca9c3bc8723d003f9914e7c4e4a7890214daecad59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputRecordTables", value)

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        '''The name or Amazon Resource Name (ARN) of the IAM role with the required permissions.'''
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee501d5b7fc7fb085aeae9cabacd68b8b8d9f9866700a8a370252e40d31650bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value)

    @builtins.property
    @jsii.member(jsii_name="transformParameters")
    def transform_parameters(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnMLTransform.TransformParametersProperty"]:
        '''The algorithm-specific parameters that are associated with the machine learning transform.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnMLTransform.TransformParametersProperty"], jsii.get(self, "transformParameters"))

    @transform_parameters.setter
    def transform_parameters(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnMLTransform.TransformParametersProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32022d812fa908378c1d2e724a2377474b2ce1f4f966dddbf71ad1f1c9d13dff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transformParameters", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A user-defined, long-form description text for the machine learning transform.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f2e6f1cc38d1a413374f9b9d4c02417e959e5f3077812b1cd868c70d042a16f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="glueVersion")
    def glue_version(self) -> typing.Optional[builtins.str]:
        '''This value determines which version of AWS Glue this machine learning transform is compatible with.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "glueVersion"))

    @glue_version.setter
    def glue_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4646b4f4efc89b1d9dc0884d55d7b11dd5293a19543a11bd2e2263d781af4a1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "glueVersion", value)

    @builtins.property
    @jsii.member(jsii_name="maxCapacity")
    def max_capacity(self) -> typing.Optional[jsii.Number]:
        '''The number of AWS Glue data processing units (DPUs) that are allocated to task runs for this transform.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxCapacity"))

    @max_capacity.setter
    def max_capacity(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d7678713b6284330c12e1b7e5e0121d21dec44a07c295ccf2831f5ebfda27c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="maxRetries")
    def max_retries(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry after an ``MLTaskRun`` of the machine learning transform fails.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRetries"))

    @max_retries.setter
    def max_retries(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b160c59f4536e5ba52b74262cc6c6277e29a9bb5d974893cb0aee1fdf2a93fa2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxRetries", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''A user-defined name for the machine learning transform.

        Names are required to be unique. ``Name`` is optional:.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97cb29ae8ccb30f3ace545620215abebebb628b2c7d82e15cb1e9519bb20db6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="numberOfWorkers")
    def number_of_workers(self) -> typing.Optional[jsii.Number]:
        '''The number of workers of a defined ``workerType`` that are allocated when a task of the transform runs.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numberOfWorkers"))

    @number_of_workers.setter
    def number_of_workers(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c04ef8b7c306add821bddff56dbf5750b8115ac7dcd8c9ef30267c9df9f57ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numberOfWorkers", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Any:
        '''The tags to use with this machine learning transform.'''
        return typing.cast(typing.Any, jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bcba5ebc0f231f7604a777a23c7985de7effc5b17647f8eb4388c48526da0ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> typing.Optional[jsii.Number]:
        '''The timeout in minutes of the machine learning transform.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d453ce28abce1d452e03956918ae4226d76e061240e5ae5102f955efe877cfc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value)

    @builtins.property
    @jsii.member(jsii_name="transformEncryption")
    def transform_encryption(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMLTransform.TransformEncryptionProperty"]]:
        '''The encryption-at-rest settings of the transform that apply to accessing user data.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMLTransform.TransformEncryptionProperty"]], jsii.get(self, "transformEncryption"))

    @transform_encryption.setter
    def transform_encryption(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMLTransform.TransformEncryptionProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e334953b8c4313c154db54fc8c4faa48859bad94c59b631d2bf8ead2740ffad1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transformEncryption", value)

    @builtins.property
    @jsii.member(jsii_name="workerType")
    def worker_type(self) -> typing.Optional[builtins.str]:
        '''The type of predefined worker that is allocated when a task of this transform runs.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workerType"))

    @worker_type.setter
    def worker_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f54a6e39b64aa4029e491424b0cd24a6797c45e24fe6065a5fccd306f38e053)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workerType", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnMLTransform.FindMatchesParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "primary_key_column_name": "primaryKeyColumnName",
            "accuracy_cost_tradeoff": "accuracyCostTradeoff",
            "enforce_provided_labels": "enforceProvidedLabels",
            "precision_recall_tradeoff": "precisionRecallTradeoff",
        },
    )
    class FindMatchesParametersProperty:
        def __init__(
            self,
            *,
            primary_key_column_name: builtins.str,
            accuracy_cost_tradeoff: typing.Optional[jsii.Number] = None,
            enforce_provided_labels: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            precision_recall_tradeoff: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The parameters to configure the find matches transform.

            :param primary_key_column_name: The name of a column that uniquely identifies rows in the source table. Used to help identify matching records.
            :param accuracy_cost_tradeoff: The value that is selected when tuning your transform for a balance between accuracy and cost. A value of 0.5 means that the system balances accuracy and cost concerns. A value of 1.0 means a bias purely for accuracy, which typically results in a higher cost, sometimes substantially higher. A value of 0.0 means a bias purely for cost, which results in a less accurate ``FindMatches`` transform, sometimes with unacceptable accuracy. Accuracy measures how well the transform finds true positives and true negatives. Increasing accuracy requires more machine resources and cost. But it also results in increased recall. Cost measures how many compute resources, and thus money, are consumed to run the transform.
            :param enforce_provided_labels: The value to switch on or off to force the output to match the provided labels from users. If the value is ``True`` , the ``find matches`` transform forces the output to match the provided labels. The results override the normal conflation results. If the value is ``False`` , the ``find matches`` transform does not ensure all the labels provided are respected, and the results rely on the trained model. Note that setting this value to true may increase the conflation execution time.
            :param precision_recall_tradeoff: The value selected when tuning your transform for a balance between precision and recall. A value of 0.5 means no preference; a value of 1.0 means a bias purely for precision, and a value of 0.0 means a bias for recall. Because this is a tradeoff, choosing values close to 1.0 means very low recall, and choosing values close to 0.0 results in very low precision. The precision metric indicates how often your model is correct when it predicts a match. The recall metric indicates that for an actual match, how often your model predicts the match.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-findmatchesparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                find_matches_parameters_property = glue.CfnMLTransform.FindMatchesParametersProperty(
                    primary_key_column_name="primaryKeyColumnName",
                
                    # the properties below are optional
                    accuracy_cost_tradeoff=123,
                    enforce_provided_labels=False,
                    precision_recall_tradeoff=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bb960ae42c6510d9bffddd8ca5eefc269b84bdc4e274fa58d90d24d5550e89e8)
                check_type(argname="argument primary_key_column_name", value=primary_key_column_name, expected_type=type_hints["primary_key_column_name"])
                check_type(argname="argument accuracy_cost_tradeoff", value=accuracy_cost_tradeoff, expected_type=type_hints["accuracy_cost_tradeoff"])
                check_type(argname="argument enforce_provided_labels", value=enforce_provided_labels, expected_type=type_hints["enforce_provided_labels"])
                check_type(argname="argument precision_recall_tradeoff", value=precision_recall_tradeoff, expected_type=type_hints["precision_recall_tradeoff"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "primary_key_column_name": primary_key_column_name,
            }
            if accuracy_cost_tradeoff is not None:
                self._values["accuracy_cost_tradeoff"] = accuracy_cost_tradeoff
            if enforce_provided_labels is not None:
                self._values["enforce_provided_labels"] = enforce_provided_labels
            if precision_recall_tradeoff is not None:
                self._values["precision_recall_tradeoff"] = precision_recall_tradeoff

        @builtins.property
        def primary_key_column_name(self) -> builtins.str:
            '''The name of a column that uniquely identifies rows in the source table.

            Used to help identify matching records.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-findmatchesparameters.html#cfn-glue-mltransform-findmatchesparameters-primarykeycolumnname
            '''
            result = self._values.get("primary_key_column_name")
            assert result is not None, "Required property 'primary_key_column_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def accuracy_cost_tradeoff(self) -> typing.Optional[jsii.Number]:
            '''The value that is selected when tuning your transform for a balance between accuracy and cost.

            A value of 0.5 means that the system balances accuracy and cost concerns. A value of 1.0 means a bias purely for accuracy, which typically results in a higher cost, sometimes substantially higher. A value of 0.0 means a bias purely for cost, which results in a less accurate ``FindMatches`` transform, sometimes with unacceptable accuracy.

            Accuracy measures how well the transform finds true positives and true negatives. Increasing accuracy requires more machine resources and cost. But it also results in increased recall.

            Cost measures how many compute resources, and thus money, are consumed to run the transform.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-findmatchesparameters.html#cfn-glue-mltransform-findmatchesparameters-accuracycosttradeoff
            '''
            result = self._values.get("accuracy_cost_tradeoff")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def enforce_provided_labels(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The value to switch on or off to force the output to match the provided labels from users.

            If the value is ``True`` , the ``find matches`` transform forces the output to match the provided labels. The results override the normal conflation results. If the value is ``False`` , the ``find matches`` transform does not ensure all the labels provided are respected, and the results rely on the trained model.

            Note that setting this value to true may increase the conflation execution time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-findmatchesparameters.html#cfn-glue-mltransform-findmatchesparameters-enforceprovidedlabels
            '''
            result = self._values.get("enforce_provided_labels")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def precision_recall_tradeoff(self) -> typing.Optional[jsii.Number]:
            '''The value selected when tuning your transform for a balance between precision and recall.

            A value of 0.5 means no preference; a value of 1.0 means a bias purely for precision, and a value of 0.0 means a bias for recall. Because this is a tradeoff, choosing values close to 1.0 means very low recall, and choosing values close to 0.0 results in very low precision.

            The precision metric indicates how often your model is correct when it predicts a match.

            The recall metric indicates that for an actual match, how often your model predicts the match.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-findmatchesparameters.html#cfn-glue-mltransform-findmatchesparameters-precisionrecalltradeoff
            '''
            result = self._values.get("precision_recall_tradeoff")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FindMatchesParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnMLTransform.GlueTablesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "database_name": "databaseName",
            "table_name": "tableName",
            "catalog_id": "catalogId",
            "connection_name": "connectionName",
        },
    )
    class GlueTablesProperty:
        def __init__(
            self,
            *,
            database_name: builtins.str,
            table_name: builtins.str,
            catalog_id: typing.Optional[builtins.str] = None,
            connection_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The database and table in the AWS Glue Data Catalog that is used for input or output data.

            :param database_name: A database name in the AWS Glue Data Catalog .
            :param table_name: A table name in the AWS Glue Data Catalog .
            :param catalog_id: A unique identifier for the AWS Glue Data Catalog .
            :param connection_name: The name of the connection to the AWS Glue Data Catalog .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-gluetables.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                glue_tables_property = glue.CfnMLTransform.GlueTablesProperty(
                    database_name="databaseName",
                    table_name="tableName",
                
                    # the properties below are optional
                    catalog_id="catalogId",
                    connection_name="connectionName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__017d4f0d02247f62a0dc37d383358ecd0448dfa33a9ea50bdbbb69eb66944468)
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument connection_name", value=connection_name, expected_type=type_hints["connection_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "database_name": database_name,
                "table_name": table_name,
            }
            if catalog_id is not None:
                self._values["catalog_id"] = catalog_id
            if connection_name is not None:
                self._values["connection_name"] = connection_name

        @builtins.property
        def database_name(self) -> builtins.str:
            '''A database name in the AWS Glue Data Catalog .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-gluetables.html#cfn-glue-mltransform-gluetables-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_name(self) -> builtins.str:
            '''A table name in the AWS Glue Data Catalog .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-gluetables.html#cfn-glue-mltransform-gluetables-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def catalog_id(self) -> typing.Optional[builtins.str]:
            '''A unique identifier for the AWS Glue Data Catalog .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-gluetables.html#cfn-glue-mltransform-gluetables-catalogid
            '''
            result = self._values.get("catalog_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def connection_name(self) -> typing.Optional[builtins.str]:
            '''The name of the connection to the AWS Glue Data Catalog .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-gluetables.html#cfn-glue-mltransform-gluetables-connectionname
            '''
            result = self._values.get("connection_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GlueTablesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnMLTransform.InputRecordTablesProperty",
        jsii_struct_bases=[],
        name_mapping={"glue_tables": "glueTables"},
    )
    class InputRecordTablesProperty:
        def __init__(
            self,
            *,
            glue_tables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMLTransform.GlueTablesProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''A list of AWS Glue table definitions used by the transform.

            :param glue_tables: The database and table in the AWS Glue Data Catalog that is used for input or output data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-inputrecordtables.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                input_record_tables_property = glue.CfnMLTransform.InputRecordTablesProperty(
                    glue_tables=[glue.CfnMLTransform.GlueTablesProperty(
                        database_name="databaseName",
                        table_name="tableName",
                
                        # the properties below are optional
                        catalog_id="catalogId",
                        connection_name="connectionName"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f4731f5241b81024e6091aa4dadb760cb188ad13cdde880df977f150a45c3918)
                check_type(argname="argument glue_tables", value=glue_tables, expected_type=type_hints["glue_tables"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if glue_tables is not None:
                self._values["glue_tables"] = glue_tables

        @builtins.property
        def glue_tables(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMLTransform.GlueTablesProperty"]]]]:
            '''The database and table in the AWS Glue Data Catalog that is used for input or output data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-inputrecordtables.html#cfn-glue-mltransform-inputrecordtables-gluetables
            '''
            result = self._values.get("glue_tables")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMLTransform.GlueTablesProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputRecordTablesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnMLTransform.MLUserDataEncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ml_user_data_encryption_mode": "mlUserDataEncryptionMode",
            "kms_key_id": "kmsKeyId",
        },
    )
    class MLUserDataEncryptionProperty:
        def __init__(
            self,
            *,
            ml_user_data_encryption_mode: builtins.str,
            kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The encryption-at-rest settings of the transform that apply to accessing user data.

            :param ml_user_data_encryption_mode: The encryption mode applied to user data. Valid values are:. - DISABLED: encryption is disabled. - SSEKMS: use of server-side encryption with AWS Key Management Service (SSE-KMS) for user data stored in Amazon S3.
            :param kms_key_id: The ID for the customer-provided KMS key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-mluserdataencryption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                m_lUser_data_encryption_property = glue.CfnMLTransform.MLUserDataEncryptionProperty(
                    ml_user_data_encryption_mode="mlUserDataEncryptionMode",
                
                    # the properties below are optional
                    kms_key_id="kmsKeyId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ecd370c09a22e068431da60552211124971655ed94a2a502fe3964bd9bb6bdde)
                check_type(argname="argument ml_user_data_encryption_mode", value=ml_user_data_encryption_mode, expected_type=type_hints["ml_user_data_encryption_mode"])
                check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "ml_user_data_encryption_mode": ml_user_data_encryption_mode,
            }
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def ml_user_data_encryption_mode(self) -> builtins.str:
            '''The encryption mode applied to user data. Valid values are:.

            - DISABLED: encryption is disabled.
            - SSEKMS: use of server-side encryption with AWS Key Management Service (SSE-KMS) for user data
              stored in Amazon S3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-mluserdataencryption.html#cfn-glue-mltransform-mluserdataencryption-mluserdataencryptionmode
            '''
            result = self._values.get("ml_user_data_encryption_mode")
            assert result is not None, "Required property 'ml_user_data_encryption_mode' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''The ID for the customer-provided KMS key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-mluserdataencryption.html#cfn-glue-mltransform-mluserdataencryption-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MLUserDataEncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnMLTransform.TransformEncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ml_user_data_encryption": "mlUserDataEncryption",
            "task_run_security_configuration_name": "taskRunSecurityConfigurationName",
        },
    )
    class TransformEncryptionProperty:
        def __init__(
            self,
            *,
            ml_user_data_encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMLTransform.MLUserDataEncryptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            task_run_security_configuration_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The encryption-at-rest settings of the transform that apply to accessing user data.

            Machine learning
            transforms can access user data encrypted in Amazon S3 using KMS.

            Additionally, imported labels and trained transforms can now be encrypted using a customer provided
            KMS key.

            :param ml_user_data_encryption: The encryption-at-rest settings of the transform that apply to accessing user data.
            :param task_run_security_configuration_name: The name of the security configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformencryption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                transform_encryption_property = glue.CfnMLTransform.TransformEncryptionProperty(
                    ml_user_data_encryption=glue.CfnMLTransform.MLUserDataEncryptionProperty(
                        ml_user_data_encryption_mode="mlUserDataEncryptionMode",
                
                        # the properties below are optional
                        kms_key_id="kmsKeyId"
                    ),
                    task_run_security_configuration_name="taskRunSecurityConfigurationName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bf35b8d358e083dc66c9259f80d1b243e0aa377d776b55769dfe34361e9fa673)
                check_type(argname="argument ml_user_data_encryption", value=ml_user_data_encryption, expected_type=type_hints["ml_user_data_encryption"])
                check_type(argname="argument task_run_security_configuration_name", value=task_run_security_configuration_name, expected_type=type_hints["task_run_security_configuration_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ml_user_data_encryption is not None:
                self._values["ml_user_data_encryption"] = ml_user_data_encryption
            if task_run_security_configuration_name is not None:
                self._values["task_run_security_configuration_name"] = task_run_security_configuration_name

        @builtins.property
        def ml_user_data_encryption(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMLTransform.MLUserDataEncryptionProperty"]]:
            '''The encryption-at-rest settings of the transform that apply to accessing user data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformencryption.html#cfn-glue-mltransform-transformencryption-mluserdataencryption
            '''
            result = self._values.get("ml_user_data_encryption")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMLTransform.MLUserDataEncryptionProperty"]], result)

        @builtins.property
        def task_run_security_configuration_name(self) -> typing.Optional[builtins.str]:
            '''The name of the security configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformencryption.html#cfn-glue-mltransform-transformencryption-taskrunsecurityconfigurationname
            '''
            result = self._values.get("task_run_security_configuration_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TransformEncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnMLTransform.TransformParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "transform_type": "transformType",
            "find_matches_parameters": "findMatchesParameters",
        },
    )
    class TransformParametersProperty:
        def __init__(
            self,
            *,
            transform_type: builtins.str,
            find_matches_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMLTransform.FindMatchesParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The algorithm-specific parameters that are associated with the machine learning transform.

            :param transform_type: The type of machine learning transform. ``FIND_MATCHES`` is the only option. For information about the types of machine learning transforms, see `Creating Machine Learning Transforms <https://docs.aws.amazon.com/glue/latest/dg/add-job-machine-learning-transform.html>`_ .
            :param find_matches_parameters: The parameters for the find matches algorithm.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                transform_parameters_property = glue.CfnMLTransform.TransformParametersProperty(
                    transform_type="transformType",
                
                    # the properties below are optional
                    find_matches_parameters=glue.CfnMLTransform.FindMatchesParametersProperty(
                        primary_key_column_name="primaryKeyColumnName",
                
                        # the properties below are optional
                        accuracy_cost_tradeoff=123,
                        enforce_provided_labels=False,
                        precision_recall_tradeoff=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__27d8f07bc63a2f9d168ac15d71b18b3b52c19f2d86354f5fe7d1f2b5ea5a0e01)
                check_type(argname="argument transform_type", value=transform_type, expected_type=type_hints["transform_type"])
                check_type(argname="argument find_matches_parameters", value=find_matches_parameters, expected_type=type_hints["find_matches_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "transform_type": transform_type,
            }
            if find_matches_parameters is not None:
                self._values["find_matches_parameters"] = find_matches_parameters

        @builtins.property
        def transform_type(self) -> builtins.str:
            '''The type of machine learning transform. ``FIND_MATCHES`` is the only option.

            For information about the types of machine learning transforms, see `Creating Machine Learning Transforms <https://docs.aws.amazon.com/glue/latest/dg/add-job-machine-learning-transform.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformparameters.html#cfn-glue-mltransform-transformparameters-transformtype
            '''
            result = self._values.get("transform_type")
            assert result is not None, "Required property 'transform_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def find_matches_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMLTransform.FindMatchesParametersProperty"]]:
            '''The parameters for the find matches algorithm.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformparameters.html#cfn-glue-mltransform-transformparameters-findmatchesparameters
            '''
            result = self._values.get("find_matches_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMLTransform.FindMatchesParametersProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TransformParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_glue.CfnMLTransformProps",
    jsii_struct_bases=[],
    name_mapping={
        "input_record_tables": "inputRecordTables",
        "role": "role",
        "transform_parameters": "transformParameters",
        "description": "description",
        "glue_version": "glueVersion",
        "max_capacity": "maxCapacity",
        "max_retries": "maxRetries",
        "name": "name",
        "number_of_workers": "numberOfWorkers",
        "tags": "tags",
        "timeout": "timeout",
        "transform_encryption": "transformEncryption",
        "worker_type": "workerType",
    },
)
class CfnMLTransformProps:
    def __init__(
        self,
        *,
        input_record_tables: typing.Union[_IResolvable_da3f097b, typing.Union[CfnMLTransform.InputRecordTablesProperty, typing.Dict[builtins.str, typing.Any]]],
        role: builtins.str,
        transform_parameters: typing.Union[_IResolvable_da3f097b, typing.Union[CfnMLTransform.TransformParametersProperty, typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        glue_version: typing.Optional[builtins.str] = None,
        max_capacity: typing.Optional[jsii.Number] = None,
        max_retries: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        number_of_workers: typing.Optional[jsii.Number] = None,
        tags: typing.Any = None,
        timeout: typing.Optional[jsii.Number] = None,
        transform_encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMLTransform.TransformEncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        worker_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnMLTransform``.

        :param input_record_tables: A list of AWS Glue table definitions used by the transform.
        :param role: The name or Amazon Resource Name (ARN) of the IAM role with the required permissions. The required permissions include both AWS Glue service role permissions to AWS Glue resources, and Amazon S3 permissions required by the transform. - This role needs AWS Glue service role permissions to allow access to resources in AWS Glue . See `Attach a Policy to IAM Users That Access AWS Glue <https://docs.aws.amazon.com/glue/latest/dg/attach-policy-iam-user.html>`_ . - This role needs permission to your Amazon Simple Storage Service (Amazon S3) sources, targets, temporary directory, scripts, and any libraries used by the task run for this transform.
        :param transform_parameters: The algorithm-specific parameters that are associated with the machine learning transform.
        :param description: A user-defined, long-form description text for the machine learning transform.
        :param glue_version: This value determines which version of AWS Glue this machine learning transform is compatible with. Glue 1.0 is recommended for most customers. If the value is not set, the Glue compatibility defaults to Glue 0.9. For more information, see `AWS Glue Versions <https://docs.aws.amazon.com/glue/latest/dg/release-notes.html#release-notes-versions>`_ in the developer guide.
        :param max_capacity: The number of AWS Glue data processing units (DPUs) that are allocated to task runs for this transform. You can allocate from 2 to 100 DPUs; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the `AWS Glue pricing page <https://docs.aws.amazon.com/glue/pricing/>`_ . ``MaxCapacity`` is a mutually exclusive option with ``NumberOfWorkers`` and ``WorkerType`` . - If either ``NumberOfWorkers`` or ``WorkerType`` is set, then ``MaxCapacity`` cannot be set. - If ``MaxCapacity`` is set then neither ``NumberOfWorkers`` or ``WorkerType`` can be set. - If ``WorkerType`` is set, then ``NumberOfWorkers`` is required (and vice versa). - ``MaxCapacity`` and ``NumberOfWorkers`` must both be at least 1. When the ``WorkerType`` field is set to a value other than ``Standard`` , the ``MaxCapacity`` field is set automatically and becomes read-only.
        :param max_retries: The maximum number of times to retry after an ``MLTaskRun`` of the machine learning transform fails.
        :param name: A user-defined name for the machine learning transform. Names are required to be unique. ``Name`` is optional:. - If you supply ``Name`` , the stack cannot be repeatedly created. - If ``Name`` is not provided, a randomly generated name will be used instead.
        :param number_of_workers: The number of workers of a defined ``workerType`` that are allocated when a task of the transform runs. If ``WorkerType`` is set, then ``NumberOfWorkers`` is required (and vice versa).
        :param tags: The tags to use with this machine learning transform. You may use tags to limit access to the machine learning transform. For more information about tags in AWS Glue , see `AWS Tags in AWS Glue <https://docs.aws.amazon.com/glue/latest/dg/monitor-tags.html>`_ in the developer guide.
        :param timeout: The timeout in minutes of the machine learning transform.
        :param transform_encryption: The encryption-at-rest settings of the transform that apply to accessing user data. Machine learning transforms can access user data encrypted in Amazon S3 using KMS. Additionally, imported labels and trained transforms can now be encrypted using a customer provided KMS key.
        :param worker_type: The type of predefined worker that is allocated when a task of this transform runs. Accepts a value of Standard, G.1X, or G.2X. - For the ``Standard`` worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker. - For the ``G.1X`` worker type, each worker provides 4 vCPU, 16 GB of memory and a 64GB disk, and 1 executor per worker. - For the ``G.2X`` worker type, each worker provides 8 vCPU, 32 GB of memory and a 128GB disk, and 1 executor per worker. ``MaxCapacity`` is a mutually exclusive option with ``NumberOfWorkers`` and ``WorkerType`` . - If either ``NumberOfWorkers`` or ``WorkerType`` is set, then ``MaxCapacity`` cannot be set. - If ``MaxCapacity`` is set then neither ``NumberOfWorkers`` or ``WorkerType`` can be set. - If ``WorkerType`` is set, then ``NumberOfWorkers`` is required (and vice versa). - ``MaxCapacity`` and ``NumberOfWorkers`` must both be at least 1.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_glue as glue
            
            # tags: Any
            
            cfn_mLTransform_props = glue.CfnMLTransformProps(
                input_record_tables=glue.CfnMLTransform.InputRecordTablesProperty(
                    glue_tables=[glue.CfnMLTransform.GlueTablesProperty(
                        database_name="databaseName",
                        table_name="tableName",
            
                        # the properties below are optional
                        catalog_id="catalogId",
                        connection_name="connectionName"
                    )]
                ),
                role="role",
                transform_parameters=glue.CfnMLTransform.TransformParametersProperty(
                    transform_type="transformType",
            
                    # the properties below are optional
                    find_matches_parameters=glue.CfnMLTransform.FindMatchesParametersProperty(
                        primary_key_column_name="primaryKeyColumnName",
            
                        # the properties below are optional
                        accuracy_cost_tradeoff=123,
                        enforce_provided_labels=False,
                        precision_recall_tradeoff=123
                    )
                ),
            
                # the properties below are optional
                description="description",
                glue_version="glueVersion",
                max_capacity=123,
                max_retries=123,
                name="name",
                number_of_workers=123,
                tags=tags,
                timeout=123,
                transform_encryption=glue.CfnMLTransform.TransformEncryptionProperty(
                    ml_user_data_encryption=glue.CfnMLTransform.MLUserDataEncryptionProperty(
                        ml_user_data_encryption_mode="mlUserDataEncryptionMode",
            
                        # the properties below are optional
                        kms_key_id="kmsKeyId"
                    ),
                    task_run_security_configuration_name="taskRunSecurityConfigurationName"
                ),
                worker_type="workerType"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__320c2c3396b30a5429b1cfe63b51777e981f1bc44756e68b10eda51ae9545c44)
            check_type(argname="argument input_record_tables", value=input_record_tables, expected_type=type_hints["input_record_tables"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument transform_parameters", value=transform_parameters, expected_type=type_hints["transform_parameters"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument glue_version", value=glue_version, expected_type=type_hints["glue_version"])
            check_type(argname="argument max_capacity", value=max_capacity, expected_type=type_hints["max_capacity"])
            check_type(argname="argument max_retries", value=max_retries, expected_type=type_hints["max_retries"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument number_of_workers", value=number_of_workers, expected_type=type_hints["number_of_workers"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument transform_encryption", value=transform_encryption, expected_type=type_hints["transform_encryption"])
            check_type(argname="argument worker_type", value=worker_type, expected_type=type_hints["worker_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "input_record_tables": input_record_tables,
            "role": role,
            "transform_parameters": transform_parameters,
        }
        if description is not None:
            self._values["description"] = description
        if glue_version is not None:
            self._values["glue_version"] = glue_version
        if max_capacity is not None:
            self._values["max_capacity"] = max_capacity
        if max_retries is not None:
            self._values["max_retries"] = max_retries
        if name is not None:
            self._values["name"] = name
        if number_of_workers is not None:
            self._values["number_of_workers"] = number_of_workers
        if tags is not None:
            self._values["tags"] = tags
        if timeout is not None:
            self._values["timeout"] = timeout
        if transform_encryption is not None:
            self._values["transform_encryption"] = transform_encryption
        if worker_type is not None:
            self._values["worker_type"] = worker_type

    @builtins.property
    def input_record_tables(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnMLTransform.InputRecordTablesProperty]:
        '''A list of AWS Glue table definitions used by the transform.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html#cfn-glue-mltransform-inputrecordtables
        '''
        result = self._values.get("input_record_tables")
        assert result is not None, "Required property 'input_record_tables' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnMLTransform.InputRecordTablesProperty], result)

    @builtins.property
    def role(self) -> builtins.str:
        '''The name or Amazon Resource Name (ARN) of the IAM role with the required permissions.

        The required permissions include both AWS Glue service role permissions to AWS Glue resources, and Amazon S3 permissions required by the transform.

        - This role needs AWS Glue service role permissions to allow access to resources in AWS Glue . See `Attach a Policy to IAM Users That Access AWS Glue <https://docs.aws.amazon.com/glue/latest/dg/attach-policy-iam-user.html>`_ .
        - This role needs permission to your Amazon Simple Storage Service (Amazon S3) sources, targets, temporary directory, scripts, and any libraries used by the task run for this transform.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html#cfn-glue-mltransform-role
        '''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def transform_parameters(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnMLTransform.TransformParametersProperty]:
        '''The algorithm-specific parameters that are associated with the machine learning transform.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html#cfn-glue-mltransform-transformparameters
        '''
        result = self._values.get("transform_parameters")
        assert result is not None, "Required property 'transform_parameters' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnMLTransform.TransformParametersProperty], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A user-defined, long-form description text for the machine learning transform.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html#cfn-glue-mltransform-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def glue_version(self) -> typing.Optional[builtins.str]:
        '''This value determines which version of AWS Glue this machine learning transform is compatible with.

        Glue 1.0 is recommended for most customers. If the value is not set, the Glue compatibility defaults to Glue 0.9. For more information, see `AWS Glue Versions <https://docs.aws.amazon.com/glue/latest/dg/release-notes.html#release-notes-versions>`_ in the developer guide.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html#cfn-glue-mltransform-glueversion
        '''
        result = self._values.get("glue_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_capacity(self) -> typing.Optional[jsii.Number]:
        '''The number of AWS Glue data processing units (DPUs) that are allocated to task runs for this transform.

        You can allocate from 2 to 100 DPUs; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the `AWS Glue pricing page <https://docs.aws.amazon.com/glue/pricing/>`_ .

        ``MaxCapacity`` is a mutually exclusive option with ``NumberOfWorkers`` and ``WorkerType`` .

        - If either ``NumberOfWorkers`` or ``WorkerType`` is set, then ``MaxCapacity`` cannot be set.
        - If ``MaxCapacity`` is set then neither ``NumberOfWorkers`` or ``WorkerType`` can be set.
        - If ``WorkerType`` is set, then ``NumberOfWorkers`` is required (and vice versa).
        - ``MaxCapacity`` and ``NumberOfWorkers`` must both be at least 1.

        When the ``WorkerType`` field is set to a value other than ``Standard`` , the ``MaxCapacity`` field is set automatically and becomes read-only.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html#cfn-glue-mltransform-maxcapacity
        '''
        result = self._values.get("max_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_retries(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry after an ``MLTaskRun`` of the machine learning transform fails.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html#cfn-glue-mltransform-maxretries
        '''
        result = self._values.get("max_retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''A user-defined name for the machine learning transform. Names are required to be unique. ``Name`` is optional:.

        - If you supply ``Name`` , the stack cannot be repeatedly created.
        - If ``Name`` is not provided, a randomly generated name will be used instead.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html#cfn-glue-mltransform-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def number_of_workers(self) -> typing.Optional[jsii.Number]:
        '''The number of workers of a defined ``workerType`` that are allocated when a task of the transform runs.

        If ``WorkerType`` is set, then ``NumberOfWorkers`` is required (and vice versa).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html#cfn-glue-mltransform-numberofworkers
        '''
        result = self._values.get("number_of_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''The tags to use with this machine learning transform.

        You may use tags to limit access to the machine learning transform. For more information about tags in AWS Glue , see `AWS Tags in AWS Glue <https://docs.aws.amazon.com/glue/latest/dg/monitor-tags.html>`_ in the developer guide.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html#cfn-glue-mltransform-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    @builtins.property
    def timeout(self) -> typing.Optional[jsii.Number]:
        '''The timeout in minutes of the machine learning transform.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html#cfn-glue-mltransform-timeout
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def transform_encryption(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMLTransform.TransformEncryptionProperty]]:
        '''The encryption-at-rest settings of the transform that apply to accessing user data.

        Machine learning
        transforms can access user data encrypted in Amazon S3 using KMS.

        Additionally, imported labels and trained transforms can now be encrypted using a customer provided
        KMS key.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html#cfn-glue-mltransform-transformencryption
        '''
        result = self._values.get("transform_encryption")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMLTransform.TransformEncryptionProperty]], result)

    @builtins.property
    def worker_type(self) -> typing.Optional[builtins.str]:
        '''The type of predefined worker that is allocated when a task of this transform runs.

        Accepts a value of Standard, G.1X, or G.2X.

        - For the ``Standard`` worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.
        - For the ``G.1X`` worker type, each worker provides 4 vCPU, 16 GB of memory and a 64GB disk, and 1 executor per worker.
        - For the ``G.2X`` worker type, each worker provides 8 vCPU, 32 GB of memory and a 128GB disk, and 1 executor per worker.

        ``MaxCapacity`` is a mutually exclusive option with ``NumberOfWorkers`` and ``WorkerType`` .

        - If either ``NumberOfWorkers`` or ``WorkerType`` is set, then ``MaxCapacity`` cannot be set.
        - If ``MaxCapacity`` is set then neither ``NumberOfWorkers`` or ``WorkerType`` can be set.
        - If ``WorkerType`` is set, then ``NumberOfWorkers`` is required (and vice versa).
        - ``MaxCapacity`` and ``NumberOfWorkers`` must both be at least 1.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html#cfn-glue-mltransform-workertype
        '''
        result = self._values.get("worker_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMLTransformProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnPartition(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_glue.CfnPartition",
):
    '''The ``AWS::Glue::Partition`` resource creates an AWS Glue partition, which represents a slice of table data.

    For more information, see `CreatePartition Action <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-partitions.html#aws-glue-api-catalog-partitions-CreatePartition>`_ and `Partition Structure <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-partitions.html#aws-glue-api-catalog-partitions-Partition>`_ in the *AWS Glue Developer Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-partition.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_glue as glue
        
        # parameters: Any
        # skewed_column_value_location_maps: Any
        
        cfn_partition = glue.CfnPartition(self, "MyCfnPartition",
            catalog_id="catalogId",
            database_name="databaseName",
            partition_input=glue.CfnPartition.PartitionInputProperty(
                values=["values"],
        
                # the properties below are optional
                parameters=parameters,
                storage_descriptor=glue.CfnPartition.StorageDescriptorProperty(
                    bucket_columns=["bucketColumns"],
                    columns=[glue.CfnPartition.ColumnProperty(
                        name="name",
        
                        # the properties below are optional
                        comment="comment",
                        type="type"
                    )],
                    compressed=False,
                    input_format="inputFormat",
                    location="location",
                    number_of_buckets=123,
                    output_format="outputFormat",
                    parameters=parameters,
                    schema_reference=glue.CfnPartition.SchemaReferenceProperty(
                        schema_id=glue.CfnPartition.SchemaIdProperty(
                            registry_name="registryName",
                            schema_arn="schemaArn",
                            schema_name="schemaName"
                        ),
                        schema_version_id="schemaVersionId",
                        schema_version_number=123
                    ),
                    serde_info=glue.CfnPartition.SerdeInfoProperty(
                        name="name",
                        parameters=parameters,
                        serialization_library="serializationLibrary"
                    ),
                    skewed_info=glue.CfnPartition.SkewedInfoProperty(
                        skewed_column_names=["skewedColumnNames"],
                        skewed_column_value_location_maps=skewed_column_value_location_maps,
                        skewed_column_values=["skewedColumnValues"]
                    ),
                    sort_columns=[glue.CfnPartition.OrderProperty(
                        column="column",
        
                        # the properties below are optional
                        sort_order=123
                    )],
                    stored_as_sub_directories=False
                )
            ),
            table_name="tableName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        catalog_id: builtins.str,
        database_name: builtins.str,
        partition_input: typing.Union[_IResolvable_da3f097b, typing.Union["CfnPartition.PartitionInputProperty", typing.Dict[builtins.str, typing.Any]]],
        table_name: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param catalog_id: The AWS account ID of the catalog in which the partion is to be created. .. epigraph:: To specify the account ID, you can use the ``Ref`` intrinsic function with the ``AWS::AccountId`` pseudo parameter. For example: ``!Ref AWS::AccountId``
        :param database_name: The name of the catalog database in which to create the partition.
        :param partition_input: The structure used to create and update a partition.
        :param table_name: The name of the metadata table in which the partition is to be created.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a7cb666e01a9021862d0b0ab8ac8df4a82cacbe6e60f96bbb3750ad2762477d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPartitionProps(
            catalog_id=catalog_id,
            database_name=database_name,
            partition_input=partition_input,
            table_name=table_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78b5b937bbcdbead6e9c098e9cd77435e7317295bfb6d1904684e13a384ac6d6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f644fc0761047bcbda0ea8aac635dce186b45d62461ee98ed3e439f77acd2fab)
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
    @jsii.member(jsii_name="catalogId")
    def catalog_id(self) -> builtins.str:
        '''The AWS account ID of the catalog in which the partion is to be created.'''
        return typing.cast(builtins.str, jsii.get(self, "catalogId"))

    @catalog_id.setter
    def catalog_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f05fc58a7dc1eb68d886a76ecea23887719e05c9a816ad3a6a82999eda2fdf9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogId", value)

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        '''The name of the catalog database in which to create the partition.'''
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2762d2587b458636fd5397b14953879deb18c5a9e411047982e4ecff34ece56c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="partitionInput")
    def partition_input(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnPartition.PartitionInputProperty"]:
        '''The structure used to create and update a partition.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnPartition.PartitionInputProperty"], jsii.get(self, "partitionInput"))

    @partition_input.setter
    def partition_input(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnPartition.PartitionInputProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a04341e86b5b0abb4af36bb01085e5230c242739cfcb7d8670acc5c03597f004)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partitionInput", value)

    @builtins.property
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> builtins.str:
        '''The name of the metadata table in which the partition is to be created.'''
        return typing.cast(builtins.str, jsii.get(self, "tableName"))

    @table_name.setter
    def table_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__407a57f0321dcc4b1394792773d1290f6cc36a639f46075ab9d69357bcf87d5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableName", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnPartition.ColumnProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "comment": "comment", "type": "type"},
    )
    class ColumnProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            comment: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A column in a ``Table`` .

            :param name: The name of the ``Column`` .
            :param comment: A free-form text comment.
            :param type: The data type of the ``Column`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-column.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                column_property = glue.CfnPartition.ColumnProperty(
                    name="name",
                
                    # the properties below are optional
                    comment="comment",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4128b3824d24d7248464514a703ec957c021fee39eab508d95517af968ceaca8)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }
            if comment is not None:
                self._values["comment"] = comment
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the ``Column`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-column.html#cfn-glue-partition-column-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def comment(self) -> typing.Optional[builtins.str]:
            '''A free-form text comment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-column.html#cfn-glue-partition-column-comment
            '''
            result = self._values.get("comment")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The data type of the ``Column`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-column.html#cfn-glue-partition-column-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ColumnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnPartition.OrderProperty",
        jsii_struct_bases=[],
        name_mapping={"column": "column", "sort_order": "sortOrder"},
    )
    class OrderProperty:
        def __init__(
            self,
            *,
            column: builtins.str,
            sort_order: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Specifies the sort order of a sorted column.

            :param column: The name of the column.
            :param sort_order: Indicates that the column is sorted in ascending order ( ``== 1`` ), or in descending order ( ``==0`` ).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-order.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                order_property = glue.CfnPartition.OrderProperty(
                    column="column",
                
                    # the properties below are optional
                    sort_order=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__086400f3f7469a3643555e94ddf84e766852816562334968079941d386daac37)
                check_type(argname="argument column", value=column, expected_type=type_hints["column"])
                check_type(argname="argument sort_order", value=sort_order, expected_type=type_hints["sort_order"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "column": column,
            }
            if sort_order is not None:
                self._values["sort_order"] = sort_order

        @builtins.property
        def column(self) -> builtins.str:
            '''The name of the column.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-order.html#cfn-glue-partition-order-column
            '''
            result = self._values.get("column")
            assert result is not None, "Required property 'column' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sort_order(self) -> typing.Optional[jsii.Number]:
            '''Indicates that the column is sorted in ascending order ( ``== 1`` ), or in descending order ( ``==0`` ).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-order.html#cfn-glue-partition-order-sortorder
            '''
            result = self._values.get("sort_order")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OrderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnPartition.PartitionInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "values": "values",
            "parameters": "parameters",
            "storage_descriptor": "storageDescriptor",
        },
    )
    class PartitionInputProperty:
        def __init__(
            self,
            *,
            values: typing.Sequence[builtins.str],
            parameters: typing.Any = None,
            storage_descriptor: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPartition.StorageDescriptorProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The structure used to create and update a partition.

            :param values: The values of the partition. Although this parameter is not required by the SDK, you must specify this parameter for a valid input. The values for the keys for the new partition must be passed as an array of String objects that must be ordered in the same order as the partition keys appearing in the Amazon S3 prefix. Otherwise AWS Glue will add the values to the wrong keys.
            :param parameters: These key-value pairs define partition parameters.
            :param storage_descriptor: Provides information about the physical location where the partition is stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-partitioninput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                # parameters: Any
                # skewed_column_value_location_maps: Any
                
                partition_input_property = glue.CfnPartition.PartitionInputProperty(
                    values=["values"],
                
                    # the properties below are optional
                    parameters=parameters,
                    storage_descriptor=glue.CfnPartition.StorageDescriptorProperty(
                        bucket_columns=["bucketColumns"],
                        columns=[glue.CfnPartition.ColumnProperty(
                            name="name",
                
                            # the properties below are optional
                            comment="comment",
                            type="type"
                        )],
                        compressed=False,
                        input_format="inputFormat",
                        location="location",
                        number_of_buckets=123,
                        output_format="outputFormat",
                        parameters=parameters,
                        schema_reference=glue.CfnPartition.SchemaReferenceProperty(
                            schema_id=glue.CfnPartition.SchemaIdProperty(
                                registry_name="registryName",
                                schema_arn="schemaArn",
                                schema_name="schemaName"
                            ),
                            schema_version_id="schemaVersionId",
                            schema_version_number=123
                        ),
                        serde_info=glue.CfnPartition.SerdeInfoProperty(
                            name="name",
                            parameters=parameters,
                            serialization_library="serializationLibrary"
                        ),
                        skewed_info=glue.CfnPartition.SkewedInfoProperty(
                            skewed_column_names=["skewedColumnNames"],
                            skewed_column_value_location_maps=skewed_column_value_location_maps,
                            skewed_column_values=["skewedColumnValues"]
                        ),
                        sort_columns=[glue.CfnPartition.OrderProperty(
                            column="column",
                
                            # the properties below are optional
                            sort_order=123
                        )],
                        stored_as_sub_directories=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1d5dfe9bb6765a27446a89b60a666937eef85988d6bf0f139dc62f6db7ab5937)
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
                check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
                check_type(argname="argument storage_descriptor", value=storage_descriptor, expected_type=type_hints["storage_descriptor"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "values": values,
            }
            if parameters is not None:
                self._values["parameters"] = parameters
            if storage_descriptor is not None:
                self._values["storage_descriptor"] = storage_descriptor

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            '''The values of the partition.

            Although this parameter is not required by the SDK, you must specify this parameter for a valid input.

            The values for the keys for the new partition must be passed as an array of String objects that must be ordered in the same order as the partition keys appearing in the Amazon S3 prefix. Otherwise AWS Glue will add the values to the wrong keys.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-partitioninput.html#cfn-glue-partition-partitioninput-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def parameters(self) -> typing.Any:
            '''These key-value pairs define partition parameters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-partitioninput.html#cfn-glue-partition-partitioninput-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Any, result)

        @builtins.property
        def storage_descriptor(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartition.StorageDescriptorProperty"]]:
            '''Provides information about the physical location where the partition is stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-partitioninput.html#cfn-glue-partition-partitioninput-storagedescriptor
            '''
            result = self._values.get("storage_descriptor")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartition.StorageDescriptorProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PartitionInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnPartition.SchemaIdProperty",
        jsii_struct_bases=[],
        name_mapping={
            "registry_name": "registryName",
            "schema_arn": "schemaArn",
            "schema_name": "schemaName",
        },
    )
    class SchemaIdProperty:
        def __init__(
            self,
            *,
            registry_name: typing.Optional[builtins.str] = None,
            schema_arn: typing.Optional[builtins.str] = None,
            schema_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A structure that contains schema identity fields.

            Either this or the ``SchemaVersionId`` has to be
            provided.

            :param registry_name: The name of the schema registry that contains the schema.
            :param schema_arn: The Amazon Resource Name (ARN) of the schema. One of ``SchemaArn`` or ``SchemaName`` has to be provided.
            :param schema_name: The name of the schema. One of ``SchemaArn`` or ``SchemaName`` has to be provided.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-schemaid.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                schema_id_property = glue.CfnPartition.SchemaIdProperty(
                    registry_name="registryName",
                    schema_arn="schemaArn",
                    schema_name="schemaName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__da4bd669a07bac042fbbb4e023a90f07ceff6ab8a5afbbb2c55a826769faca15)
                check_type(argname="argument registry_name", value=registry_name, expected_type=type_hints["registry_name"])
                check_type(argname="argument schema_arn", value=schema_arn, expected_type=type_hints["schema_arn"])
                check_type(argname="argument schema_name", value=schema_name, expected_type=type_hints["schema_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if registry_name is not None:
                self._values["registry_name"] = registry_name
            if schema_arn is not None:
                self._values["schema_arn"] = schema_arn
            if schema_name is not None:
                self._values["schema_name"] = schema_name

        @builtins.property
        def registry_name(self) -> typing.Optional[builtins.str]:
            '''The name of the schema registry that contains the schema.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-schemaid.html#cfn-glue-partition-schemaid-registryname
            '''
            result = self._values.get("registry_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def schema_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the schema.

            One of ``SchemaArn`` or ``SchemaName`` has to be
            provided.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-schemaid.html#cfn-glue-partition-schemaid-schemaarn
            '''
            result = self._values.get("schema_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def schema_name(self) -> typing.Optional[builtins.str]:
            '''The name of the schema.

            One of ``SchemaArn`` or ``SchemaName`` has to be provided.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-schemaid.html#cfn-glue-partition-schemaid-schemaname
            '''
            result = self._values.get("schema_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SchemaIdProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnPartition.SchemaReferenceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "schema_id": "schemaId",
            "schema_version_id": "schemaVersionId",
            "schema_version_number": "schemaVersionNumber",
        },
    )
    class SchemaReferenceProperty:
        def __init__(
            self,
            *,
            schema_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPartition.SchemaIdProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            schema_version_id: typing.Optional[builtins.str] = None,
            schema_version_number: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''An object that references a schema stored in the AWS Glue Schema Registry.

            :param schema_id: A structure that contains schema identity fields. Either this or the ``SchemaVersionId`` has to be provided.
            :param schema_version_id: The unique ID assigned to a version of the schema. Either this or the ``SchemaId`` has to be provided.
            :param schema_version_number: The version number of the schema.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-schemareference.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                schema_reference_property = glue.CfnPartition.SchemaReferenceProperty(
                    schema_id=glue.CfnPartition.SchemaIdProperty(
                        registry_name="registryName",
                        schema_arn="schemaArn",
                        schema_name="schemaName"
                    ),
                    schema_version_id="schemaVersionId",
                    schema_version_number=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__be049becd9a1c1413e38e320ee3a71c5d2abe254bfc360c441dbb95d19c793d5)
                check_type(argname="argument schema_id", value=schema_id, expected_type=type_hints["schema_id"])
                check_type(argname="argument schema_version_id", value=schema_version_id, expected_type=type_hints["schema_version_id"])
                check_type(argname="argument schema_version_number", value=schema_version_number, expected_type=type_hints["schema_version_number"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if schema_id is not None:
                self._values["schema_id"] = schema_id
            if schema_version_id is not None:
                self._values["schema_version_id"] = schema_version_id
            if schema_version_number is not None:
                self._values["schema_version_number"] = schema_version_number

        @builtins.property
        def schema_id(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartition.SchemaIdProperty"]]:
            '''A structure that contains schema identity fields.

            Either this or the ``SchemaVersionId`` has to be
            provided.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-schemareference.html#cfn-glue-partition-schemareference-schemaid
            '''
            result = self._values.get("schema_id")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartition.SchemaIdProperty"]], result)

        @builtins.property
        def schema_version_id(self) -> typing.Optional[builtins.str]:
            '''The unique ID assigned to a version of the schema.

            Either this or the ``SchemaId`` has to be provided.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-schemareference.html#cfn-glue-partition-schemareference-schemaversionid
            '''
            result = self._values.get("schema_version_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def schema_version_number(self) -> typing.Optional[jsii.Number]:
            '''The version number of the schema.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-schemareference.html#cfn-glue-partition-schemareference-schemaversionnumber
            '''
            result = self._values.get("schema_version_number")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SchemaReferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnPartition.SerdeInfoProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "parameters": "parameters",
            "serialization_library": "serializationLibrary",
        },
    )
    class SerdeInfoProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            parameters: typing.Any = None,
            serialization_library: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about a serialization/deserialization program (SerDe) that serves as an extractor and loader.

            :param name: Name of the SerDe.
            :param parameters: These key-value pairs define initialization parameters for the SerDe.
            :param serialization_library: Usually the class that implements the SerDe. An example is ``org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-serdeinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                # parameters: Any
                
                serde_info_property = glue.CfnPartition.SerdeInfoProperty(
                    name="name",
                    parameters=parameters,
                    serialization_library="serializationLibrary"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4c43ded18a2aa53ebee991696cce2d20a8ba939c244937cbcf36e93d11432061)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
                check_type(argname="argument serialization_library", value=serialization_library, expected_type=type_hints["serialization_library"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if parameters is not None:
                self._values["parameters"] = parameters
            if serialization_library is not None:
                self._values["serialization_library"] = serialization_library

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''Name of the SerDe.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-serdeinfo.html#cfn-glue-partition-serdeinfo-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parameters(self) -> typing.Any:
            '''These key-value pairs define initialization parameters for the SerDe.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-serdeinfo.html#cfn-glue-partition-serdeinfo-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Any, result)

        @builtins.property
        def serialization_library(self) -> typing.Optional[builtins.str]:
            '''Usually the class that implements the SerDe.

            An example is ``org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-serdeinfo.html#cfn-glue-partition-serdeinfo-serializationlibrary
            '''
            result = self._values.get("serialization_library")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SerdeInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnPartition.SkewedInfoProperty",
        jsii_struct_bases=[],
        name_mapping={
            "skewed_column_names": "skewedColumnNames",
            "skewed_column_value_location_maps": "skewedColumnValueLocationMaps",
            "skewed_column_values": "skewedColumnValues",
        },
    )
    class SkewedInfoProperty:
        def __init__(
            self,
            *,
            skewed_column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
            skewed_column_value_location_maps: typing.Any = None,
            skewed_column_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Specifies skewed values in a table.

            Skewed values are those that occur with very high frequency.

            :param skewed_column_names: A list of names of columns that contain skewed values.
            :param skewed_column_value_location_maps: A mapping of skewed values to the columns that contain them.
            :param skewed_column_values: A list of values that appear so frequently as to be considered skewed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-skewedinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                # skewed_column_value_location_maps: Any
                
                skewed_info_property = glue.CfnPartition.SkewedInfoProperty(
                    skewed_column_names=["skewedColumnNames"],
                    skewed_column_value_location_maps=skewed_column_value_location_maps,
                    skewed_column_values=["skewedColumnValues"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7435667120cf63046fa2c7684e85f094807aa6e5e2cd23406caa6e5569843a1f)
                check_type(argname="argument skewed_column_names", value=skewed_column_names, expected_type=type_hints["skewed_column_names"])
                check_type(argname="argument skewed_column_value_location_maps", value=skewed_column_value_location_maps, expected_type=type_hints["skewed_column_value_location_maps"])
                check_type(argname="argument skewed_column_values", value=skewed_column_values, expected_type=type_hints["skewed_column_values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if skewed_column_names is not None:
                self._values["skewed_column_names"] = skewed_column_names
            if skewed_column_value_location_maps is not None:
                self._values["skewed_column_value_location_maps"] = skewed_column_value_location_maps
            if skewed_column_values is not None:
                self._values["skewed_column_values"] = skewed_column_values

        @builtins.property
        def skewed_column_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of names of columns that contain skewed values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-skewedinfo.html#cfn-glue-partition-skewedinfo-skewedcolumnnames
            '''
            result = self._values.get("skewed_column_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def skewed_column_value_location_maps(self) -> typing.Any:
            '''A mapping of skewed values to the columns that contain them.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-skewedinfo.html#cfn-glue-partition-skewedinfo-skewedcolumnvaluelocationmaps
            '''
            result = self._values.get("skewed_column_value_location_maps")
            return typing.cast(typing.Any, result)

        @builtins.property
        def skewed_column_values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of values that appear so frequently as to be considered skewed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-skewedinfo.html#cfn-glue-partition-skewedinfo-skewedcolumnvalues
            '''
            result = self._values.get("skewed_column_values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SkewedInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnPartition.StorageDescriptorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_columns": "bucketColumns",
            "columns": "columns",
            "compressed": "compressed",
            "input_format": "inputFormat",
            "location": "location",
            "number_of_buckets": "numberOfBuckets",
            "output_format": "outputFormat",
            "parameters": "parameters",
            "schema_reference": "schemaReference",
            "serde_info": "serdeInfo",
            "skewed_info": "skewedInfo",
            "sort_columns": "sortColumns",
            "stored_as_sub_directories": "storedAsSubDirectories",
        },
    )
    class StorageDescriptorProperty:
        def __init__(
            self,
            *,
            bucket_columns: typing.Optional[typing.Sequence[builtins.str]] = None,
            columns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPartition.ColumnProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            compressed: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            input_format: typing.Optional[builtins.str] = None,
            location: typing.Optional[builtins.str] = None,
            number_of_buckets: typing.Optional[jsii.Number] = None,
            output_format: typing.Optional[builtins.str] = None,
            parameters: typing.Any = None,
            schema_reference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPartition.SchemaReferenceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            serde_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPartition.SerdeInfoProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            skewed_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPartition.SkewedInfoProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sort_columns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPartition.OrderProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            stored_as_sub_directories: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Describes the physical storage of table data.

            :param bucket_columns: A list of reducer grouping columns, clustering columns, and bucketing columns in the table.
            :param columns: A list of the ``Columns`` in the table.
            :param compressed: ``True`` if the data in the table is compressed, or ``False`` if not.
            :param input_format: The input format: ``SequenceFileInputFormat`` (binary), or ``TextInputFormat`` , or a custom format.
            :param location: The physical location of the table. By default, this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.
            :param number_of_buckets: The number of buckets. You must specify this property if the partition contains any dimension columns.
            :param output_format: The output format: ``SequenceFileOutputFormat`` (binary), or ``IgnoreKeyTextOutputFormat`` , or a custom format.
            :param parameters: The user-supplied properties in key-value form.
            :param schema_reference: An object that references a schema stored in the AWS Glue Schema Registry.
            :param serde_info: The serialization/deserialization (SerDe) information.
            :param skewed_info: The information about values that appear frequently in a column (skewed values).
            :param sort_columns: A list specifying the sort order of each bucket in the table.
            :param stored_as_sub_directories: ``True`` if the table data is stored in subdirectories, or ``False`` if not.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-storagedescriptor.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                # parameters: Any
                # skewed_column_value_location_maps: Any
                
                storage_descriptor_property = glue.CfnPartition.StorageDescriptorProperty(
                    bucket_columns=["bucketColumns"],
                    columns=[glue.CfnPartition.ColumnProperty(
                        name="name",
                
                        # the properties below are optional
                        comment="comment",
                        type="type"
                    )],
                    compressed=False,
                    input_format="inputFormat",
                    location="location",
                    number_of_buckets=123,
                    output_format="outputFormat",
                    parameters=parameters,
                    schema_reference=glue.CfnPartition.SchemaReferenceProperty(
                        schema_id=glue.CfnPartition.SchemaIdProperty(
                            registry_name="registryName",
                            schema_arn="schemaArn",
                            schema_name="schemaName"
                        ),
                        schema_version_id="schemaVersionId",
                        schema_version_number=123
                    ),
                    serde_info=glue.CfnPartition.SerdeInfoProperty(
                        name="name",
                        parameters=parameters,
                        serialization_library="serializationLibrary"
                    ),
                    skewed_info=glue.CfnPartition.SkewedInfoProperty(
                        skewed_column_names=["skewedColumnNames"],
                        skewed_column_value_location_maps=skewed_column_value_location_maps,
                        skewed_column_values=["skewedColumnValues"]
                    ),
                    sort_columns=[glue.CfnPartition.OrderProperty(
                        column="column",
                
                        # the properties below are optional
                        sort_order=123
                    )],
                    stored_as_sub_directories=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__96dc3348b2a22bbbc2a529f40eb4fdbd644f9e0e8660ca12ec5e132cbb27421f)
                check_type(argname="argument bucket_columns", value=bucket_columns, expected_type=type_hints["bucket_columns"])
                check_type(argname="argument columns", value=columns, expected_type=type_hints["columns"])
                check_type(argname="argument compressed", value=compressed, expected_type=type_hints["compressed"])
                check_type(argname="argument input_format", value=input_format, expected_type=type_hints["input_format"])
                check_type(argname="argument location", value=location, expected_type=type_hints["location"])
                check_type(argname="argument number_of_buckets", value=number_of_buckets, expected_type=type_hints["number_of_buckets"])
                check_type(argname="argument output_format", value=output_format, expected_type=type_hints["output_format"])
                check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
                check_type(argname="argument schema_reference", value=schema_reference, expected_type=type_hints["schema_reference"])
                check_type(argname="argument serde_info", value=serde_info, expected_type=type_hints["serde_info"])
                check_type(argname="argument skewed_info", value=skewed_info, expected_type=type_hints["skewed_info"])
                check_type(argname="argument sort_columns", value=sort_columns, expected_type=type_hints["sort_columns"])
                check_type(argname="argument stored_as_sub_directories", value=stored_as_sub_directories, expected_type=type_hints["stored_as_sub_directories"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if bucket_columns is not None:
                self._values["bucket_columns"] = bucket_columns
            if columns is not None:
                self._values["columns"] = columns
            if compressed is not None:
                self._values["compressed"] = compressed
            if input_format is not None:
                self._values["input_format"] = input_format
            if location is not None:
                self._values["location"] = location
            if number_of_buckets is not None:
                self._values["number_of_buckets"] = number_of_buckets
            if output_format is not None:
                self._values["output_format"] = output_format
            if parameters is not None:
                self._values["parameters"] = parameters
            if schema_reference is not None:
                self._values["schema_reference"] = schema_reference
            if serde_info is not None:
                self._values["serde_info"] = serde_info
            if skewed_info is not None:
                self._values["skewed_info"] = skewed_info
            if sort_columns is not None:
                self._values["sort_columns"] = sort_columns
            if stored_as_sub_directories is not None:
                self._values["stored_as_sub_directories"] = stored_as_sub_directories

        @builtins.property
        def bucket_columns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of reducer grouping columns, clustering columns, and bucketing columns in the table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-storagedescriptor.html#cfn-glue-partition-storagedescriptor-bucketcolumns
            '''
            result = self._values.get("bucket_columns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def columns(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPartition.ColumnProperty"]]]]:
            '''A list of the ``Columns`` in the table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-storagedescriptor.html#cfn-glue-partition-storagedescriptor-columns
            '''
            result = self._values.get("columns")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPartition.ColumnProperty"]]]], result)

        @builtins.property
        def compressed(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``True`` if the data in the table is compressed, or ``False`` if not.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-storagedescriptor.html#cfn-glue-partition-storagedescriptor-compressed
            '''
            result = self._values.get("compressed")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def input_format(self) -> typing.Optional[builtins.str]:
            '''The input format: ``SequenceFileInputFormat`` (binary), or ``TextInputFormat`` , or a custom format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-storagedescriptor.html#cfn-glue-partition-storagedescriptor-inputformat
            '''
            result = self._values.get("input_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def location(self) -> typing.Optional[builtins.str]:
            '''The physical location of the table.

            By default, this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-storagedescriptor.html#cfn-glue-partition-storagedescriptor-location
            '''
            result = self._values.get("location")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def number_of_buckets(self) -> typing.Optional[jsii.Number]:
            '''The number of buckets.

            You must specify this property if the partition contains any dimension columns.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-storagedescriptor.html#cfn-glue-partition-storagedescriptor-numberofbuckets
            '''
            result = self._values.get("number_of_buckets")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def output_format(self) -> typing.Optional[builtins.str]:
            '''The output format: ``SequenceFileOutputFormat`` (binary), or ``IgnoreKeyTextOutputFormat`` , or a custom format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-storagedescriptor.html#cfn-glue-partition-storagedescriptor-outputformat
            '''
            result = self._values.get("output_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parameters(self) -> typing.Any:
            '''The user-supplied properties in key-value form.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-storagedescriptor.html#cfn-glue-partition-storagedescriptor-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Any, result)

        @builtins.property
        def schema_reference(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartition.SchemaReferenceProperty"]]:
            '''An object that references a schema stored in the AWS Glue Schema Registry.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-storagedescriptor.html#cfn-glue-partition-storagedescriptor-schemareference
            '''
            result = self._values.get("schema_reference")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartition.SchemaReferenceProperty"]], result)

        @builtins.property
        def serde_info(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartition.SerdeInfoProperty"]]:
            '''The serialization/deserialization (SerDe) information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-storagedescriptor.html#cfn-glue-partition-storagedescriptor-serdeinfo
            '''
            result = self._values.get("serde_info")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartition.SerdeInfoProperty"]], result)

        @builtins.property
        def skewed_info(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartition.SkewedInfoProperty"]]:
            '''The information about values that appear frequently in a column (skewed values).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-storagedescriptor.html#cfn-glue-partition-storagedescriptor-skewedinfo
            '''
            result = self._values.get("skewed_info")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartition.SkewedInfoProperty"]], result)

        @builtins.property
        def sort_columns(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPartition.OrderProperty"]]]]:
            '''A list specifying the sort order of each bucket in the table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-storagedescriptor.html#cfn-glue-partition-storagedescriptor-sortcolumns
            '''
            result = self._values.get("sort_columns")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPartition.OrderProperty"]]]], result)

        @builtins.property
        def stored_as_sub_directories(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``True`` if the table data is stored in subdirectories, or ``False`` if not.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-storagedescriptor.html#cfn-glue-partition-storagedescriptor-storedassubdirectories
            '''
            result = self._values.get("stored_as_sub_directories")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StorageDescriptorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_glue.CfnPartitionProps",
    jsii_struct_bases=[],
    name_mapping={
        "catalog_id": "catalogId",
        "database_name": "databaseName",
        "partition_input": "partitionInput",
        "table_name": "tableName",
    },
)
class CfnPartitionProps:
    def __init__(
        self,
        *,
        catalog_id: builtins.str,
        database_name: builtins.str,
        partition_input: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPartition.PartitionInputProperty, typing.Dict[builtins.str, typing.Any]]],
        table_name: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnPartition``.

        :param catalog_id: The AWS account ID of the catalog in which the partion is to be created. .. epigraph:: To specify the account ID, you can use the ``Ref`` intrinsic function with the ``AWS::AccountId`` pseudo parameter. For example: ``!Ref AWS::AccountId``
        :param database_name: The name of the catalog database in which to create the partition.
        :param partition_input: The structure used to create and update a partition.
        :param table_name: The name of the metadata table in which the partition is to be created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-partition.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_glue as glue
            
            # parameters: Any
            # skewed_column_value_location_maps: Any
            
            cfn_partition_props = glue.CfnPartitionProps(
                catalog_id="catalogId",
                database_name="databaseName",
                partition_input=glue.CfnPartition.PartitionInputProperty(
                    values=["values"],
            
                    # the properties below are optional
                    parameters=parameters,
                    storage_descriptor=glue.CfnPartition.StorageDescriptorProperty(
                        bucket_columns=["bucketColumns"],
                        columns=[glue.CfnPartition.ColumnProperty(
                            name="name",
            
                            # the properties below are optional
                            comment="comment",
                            type="type"
                        )],
                        compressed=False,
                        input_format="inputFormat",
                        location="location",
                        number_of_buckets=123,
                        output_format="outputFormat",
                        parameters=parameters,
                        schema_reference=glue.CfnPartition.SchemaReferenceProperty(
                            schema_id=glue.CfnPartition.SchemaIdProperty(
                                registry_name="registryName",
                                schema_arn="schemaArn",
                                schema_name="schemaName"
                            ),
                            schema_version_id="schemaVersionId",
                            schema_version_number=123
                        ),
                        serde_info=glue.CfnPartition.SerdeInfoProperty(
                            name="name",
                            parameters=parameters,
                            serialization_library="serializationLibrary"
                        ),
                        skewed_info=glue.CfnPartition.SkewedInfoProperty(
                            skewed_column_names=["skewedColumnNames"],
                            skewed_column_value_location_maps=skewed_column_value_location_maps,
                            skewed_column_values=["skewedColumnValues"]
                        ),
                        sort_columns=[glue.CfnPartition.OrderProperty(
                            column="column",
            
                            # the properties below are optional
                            sort_order=123
                        )],
                        stored_as_sub_directories=False
                    )
                ),
                table_name="tableName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e44f0759b77ba4f2a6fc23f3b51c3b9b3a8893e479e1a1f17da4181d294dea48)
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument partition_input", value=partition_input, expected_type=type_hints["partition_input"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "catalog_id": catalog_id,
            "database_name": database_name,
            "partition_input": partition_input,
            "table_name": table_name,
        }

    @builtins.property
    def catalog_id(self) -> builtins.str:
        '''The AWS account ID of the catalog in which the partion is to be created.

        .. epigraph::

           To specify the account ID, you can use the ``Ref`` intrinsic function with the ``AWS::AccountId`` pseudo parameter. For example: ``!Ref AWS::AccountId``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-partition.html#cfn-glue-partition-catalogid
        '''
        result = self._values.get("catalog_id")
        assert result is not None, "Required property 'catalog_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def database_name(self) -> builtins.str:
        '''The name of the catalog database in which to create the partition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-partition.html#cfn-glue-partition-databasename
        '''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def partition_input(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnPartition.PartitionInputProperty]:
        '''The structure used to create and update a partition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-partition.html#cfn-glue-partition-partitioninput
        '''
        result = self._values.get("partition_input")
        assert result is not None, "Required property 'partition_input' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnPartition.PartitionInputProperty], result)

    @builtins.property
    def table_name(self) -> builtins.str:
        '''The name of the metadata table in which the partition is to be created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-partition.html#cfn-glue-partition-tablename
        '''
        result = self._values.get("table_name")
        assert result is not None, "Required property 'table_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPartitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnRegistry(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_glue.CfnRegistry",
):
    '''The AWS::Glue::Registry is an AWS Glue resource type that manages registries of schemas in the AWS Glue Schema Registry.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-registry.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_glue as glue
        
        cfn_registry = glue.CfnRegistry(self, "MyCfnRegistry",
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
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the registry.
        :param description: A description of the registry.
        :param tags: AWS tags that contain a key value pair and may be searched by console, command line, or API.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5de9a299a2bf41c1ad28fbb79cc31782da6bbeccfd6ad8c09014110dec87fcb6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRegistryProps(name=name, description=description, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc8a013f30adcd1edf09a70d6cb3498fabc5c2275ef048bccad07b556f68c139)
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
            type_hints = typing.get_type_hints(_typecheckingstub__488adf133bcfcc60051c0a11031a6cf7f8f1578dc2bdf68315cd037cba2c8d45)
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
        '''Amazon Resource Name for the created Registry.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

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
        '''The name of the registry.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b08a23e9e0a8332240d398591fb00a0705ae1c744f78c8c7f99d6d42cbbbfe2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the registry.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86912387bdaf3c2b7844a0b55fafc22c116e70b5bcd99b91ed151e3649a7d992)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''AWS tags that contain a key value pair and may be searched by console, command line, or API.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3addc589422a8772c97f55547db6d321590b6a3078e00ea158feb432c9141727)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_glue.CfnRegistryProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "description": "description", "tags": "tags"},
)
class CfnRegistryProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRegistry``.

        :param name: The name of the registry.
        :param description: A description of the registry.
        :param tags: AWS tags that contain a key value pair and may be searched by console, command line, or API.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-registry.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_glue as glue
            
            cfn_registry_props = glue.CfnRegistryProps(
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
            type_hints = typing.get_type_hints(_typecheckingstub__a9d85e07a2dcc4ae5cd073c48fc5eb424c7446e4be042407f1f89c111ef9bba1)
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
        '''The name of the registry.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-registry.html#cfn-glue-registry-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the registry.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-registry.html#cfn-glue-registry-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''AWS tags that contain a key value pair and may be searched by console, command line, or API.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-registry.html#cfn-glue-registry-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRegistryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnSchema(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_glue.CfnSchema",
):
    '''The ``AWS::Glue::Schema`` is an AWS Glue resource type that manages schemas in the AWS Glue Schema Registry.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schema.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_glue as glue
        
        cfn_schema = glue.CfnSchema(self, "MyCfnSchema",
            compatibility="compatibility",
            data_format="dataFormat",
            name="name",
            schema_definition="schemaDefinition",
        
            # the properties below are optional
            checkpoint_version=glue.CfnSchema.SchemaVersionProperty(
                is_latest=False,
                version_number=123
            ),
            description="description",
            registry=glue.CfnSchema.RegistryProperty(
                arn="arn",
                name="name"
            ),
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
        compatibility: builtins.str,
        data_format: builtins.str,
        name: builtins.str,
        schema_definition: builtins.str,
        checkpoint_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSchema.SchemaVersionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        registry: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSchema.RegistryProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param compatibility: The compatibility mode of the schema.
        :param data_format: The data format of the schema definition. Currently only ``AVRO`` is supported.
        :param name: Name of the schema to be created of max length of 255, and may only contain letters, numbers, hyphen, underscore, dollar sign, or hash mark. No whitespace.
        :param schema_definition: The schema definition using the ``DataFormat`` setting for ``SchemaName`` .
        :param checkpoint_version: Specify the ``VersionNumber`` or the ``IsLatest`` for setting the checkpoint for the schema. This is only required for updating a checkpoint.
        :param description: A description of the schema if specified when created.
        :param registry: The registry where a schema is stored.
        :param tags: AWS tags that contain a key value pair and may be searched by console, command line, or API.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c24fd21e2dfff4073f4fd8235eb4e6907b6a19fef52a7e12e6cc32797cc23f2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSchemaProps(
            compatibility=compatibility,
            data_format=data_format,
            name=name,
            schema_definition=schema_definition,
            checkpoint_version=checkpoint_version,
            description=description,
            registry=registry,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__032942ae67479a8dd85c055f92ab4293be2dd277171c761f4c8e973149ffe307)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f0c653bd170b326c508ed7517a107d65cc72284d82d39ce6c114dcccde4b40a6)
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
        '''The Amazon Resource Name (ARN) of the schema.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrInitialSchemaVersionId")
    def attr_initial_schema_version_id(self) -> builtins.str:
        '''Represents the version ID associated with the initial schema version.

        :cloudformationAttribute: InitialSchemaVersionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrInitialSchemaVersionId"))

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
    @jsii.member(jsii_name="compatibility")
    def compatibility(self) -> builtins.str:
        '''The compatibility mode of the schema.'''
        return typing.cast(builtins.str, jsii.get(self, "compatibility"))

    @compatibility.setter
    def compatibility(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b73978872411b0a345203986e3747c7d8e8aa6c7a7d84c98ea032c8a52dbfe31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compatibility", value)

    @builtins.property
    @jsii.member(jsii_name="dataFormat")
    def data_format(self) -> builtins.str:
        '''The data format of the schema definition.'''
        return typing.cast(builtins.str, jsii.get(self, "dataFormat"))

    @data_format.setter
    def data_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5e37c443190efe6042f27de7c8f6bcb3356c41291ed3f6e60f326b159aa86c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataFormat", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''Name of the schema to be created of max length of 255, and may only contain letters, numbers, hyphen, underscore, dollar sign, or hash mark.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff3dcb47edaa294c6caf2b08476ad6ab296e0af75fac6f4cff50f7d0702daa85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="schemaDefinition")
    def schema_definition(self) -> builtins.str:
        '''The schema definition using the ``DataFormat`` setting for ``SchemaName`` .'''
        return typing.cast(builtins.str, jsii.get(self, "schemaDefinition"))

    @schema_definition.setter
    def schema_definition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0425f83d697fdeb65b7ad72b89add3f188c811ceb74503e3deeda6f8fd774134)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaDefinition", value)

    @builtins.property
    @jsii.member(jsii_name="checkpointVersion")
    def checkpoint_version(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSchema.SchemaVersionProperty"]]:
        '''Specify the ``VersionNumber`` or the ``IsLatest`` for setting the checkpoint for the schema.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSchema.SchemaVersionProperty"]], jsii.get(self, "checkpointVersion"))

    @checkpoint_version.setter
    def checkpoint_version(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSchema.SchemaVersionProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e496b746565a2a907c7b308108c0f360ed6e1d756d065268762427d0c0195ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checkpointVersion", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the schema if specified when created.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__256a8ca904755342242bfb57993a7b4a73841aa88a6f73b4533a2ecca3f961d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="registry")
    def registry(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSchema.RegistryProperty"]]:
        '''The registry where a schema is stored.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSchema.RegistryProperty"]], jsii.get(self, "registry"))

    @registry.setter
    def registry(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSchema.RegistryProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9180e06f6739c2a1783c2974f71f4a42d49ca8423d693d37b0c96b31d3092bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registry", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''AWS tags that contain a key value pair and may be searched by console, command line, or API.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2060d4f7f98e703465a1d2f6e55970d3e0767652cb30c60bd1dfb69101403c47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnSchema.RegistryProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn", "name": "name"},
    )
    class RegistryProperty:
        def __init__(
            self,
            *,
            arn: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies a registry in the AWS Glue Schema Registry.

            :param arn: The Amazon Resource Name (ARN) of the registry.
            :param name: The name of the registry.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-schema-registry.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                registry_property = glue.CfnSchema.RegistryProperty(
                    arn="arn",
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a294a0c13681e2402296e02dfba512363ce2418d91d7d958543bbf10879c5c9c)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the registry.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-schema-registry.html#cfn-glue-schema-registry-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the registry.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-schema-registry.html#cfn-glue-schema-registry-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RegistryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnSchema.SchemaVersionProperty",
        jsii_struct_bases=[],
        name_mapping={"is_latest": "isLatest", "version_number": "versionNumber"},
    )
    class SchemaVersionProperty:
        def __init__(
            self,
            *,
            is_latest: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            version_number: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Specifies the version of a schema.

            :param is_latest: Indicates if this version is the latest version of the schema.
            :param version_number: The version number of the schema.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-schema-schemaversion.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                schema_version_property = glue.CfnSchema.SchemaVersionProperty(
                    is_latest=False,
                    version_number=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2e90fb9d4f51c449f67d6d38fa8a393062e21c0ebc8dcff0751d9836010ae6bf)
                check_type(argname="argument is_latest", value=is_latest, expected_type=type_hints["is_latest"])
                check_type(argname="argument version_number", value=version_number, expected_type=type_hints["version_number"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if is_latest is not None:
                self._values["is_latest"] = is_latest
            if version_number is not None:
                self._values["version_number"] = version_number

        @builtins.property
        def is_latest(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates if this version is the latest version of the schema.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-schema-schemaversion.html#cfn-glue-schema-schemaversion-islatest
            '''
            result = self._values.get("is_latest")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def version_number(self) -> typing.Optional[jsii.Number]:
            '''The version number of the schema.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-schema-schemaversion.html#cfn-glue-schema-schemaversion-versionnumber
            '''
            result = self._values.get("version_number")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SchemaVersionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_glue.CfnSchemaProps",
    jsii_struct_bases=[],
    name_mapping={
        "compatibility": "compatibility",
        "data_format": "dataFormat",
        "name": "name",
        "schema_definition": "schemaDefinition",
        "checkpoint_version": "checkpointVersion",
        "description": "description",
        "registry": "registry",
        "tags": "tags",
    },
)
class CfnSchemaProps:
    def __init__(
        self,
        *,
        compatibility: builtins.str,
        data_format: builtins.str,
        name: builtins.str,
        schema_definition: builtins.str,
        checkpoint_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchema.SchemaVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        registry: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchema.RegistryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSchema``.

        :param compatibility: The compatibility mode of the schema.
        :param data_format: The data format of the schema definition. Currently only ``AVRO`` is supported.
        :param name: Name of the schema to be created of max length of 255, and may only contain letters, numbers, hyphen, underscore, dollar sign, or hash mark. No whitespace.
        :param schema_definition: The schema definition using the ``DataFormat`` setting for ``SchemaName`` .
        :param checkpoint_version: Specify the ``VersionNumber`` or the ``IsLatest`` for setting the checkpoint for the schema. This is only required for updating a checkpoint.
        :param description: A description of the schema if specified when created.
        :param registry: The registry where a schema is stored.
        :param tags: AWS tags that contain a key value pair and may be searched by console, command line, or API.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schema.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_glue as glue
            
            cfn_schema_props = glue.CfnSchemaProps(
                compatibility="compatibility",
                data_format="dataFormat",
                name="name",
                schema_definition="schemaDefinition",
            
                # the properties below are optional
                checkpoint_version=glue.CfnSchema.SchemaVersionProperty(
                    is_latest=False,
                    version_number=123
                ),
                description="description",
                registry=glue.CfnSchema.RegistryProperty(
                    arn="arn",
                    name="name"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbb4fb2ee83fa315d5be44ea6b3b74388d44b2e9cd9fac352aa28801b198dc21)
            check_type(argname="argument compatibility", value=compatibility, expected_type=type_hints["compatibility"])
            check_type(argname="argument data_format", value=data_format, expected_type=type_hints["data_format"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument schema_definition", value=schema_definition, expected_type=type_hints["schema_definition"])
            check_type(argname="argument checkpoint_version", value=checkpoint_version, expected_type=type_hints["checkpoint_version"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument registry", value=registry, expected_type=type_hints["registry"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "compatibility": compatibility,
            "data_format": data_format,
            "name": name,
            "schema_definition": schema_definition,
        }
        if checkpoint_version is not None:
            self._values["checkpoint_version"] = checkpoint_version
        if description is not None:
            self._values["description"] = description
        if registry is not None:
            self._values["registry"] = registry
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def compatibility(self) -> builtins.str:
        '''The compatibility mode of the schema.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schema.html#cfn-glue-schema-compatibility
        '''
        result = self._values.get("compatibility")
        assert result is not None, "Required property 'compatibility' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_format(self) -> builtins.str:
        '''The data format of the schema definition.

        Currently only ``AVRO`` is supported.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schema.html#cfn-glue-schema-dataformat
        '''
        result = self._values.get("data_format")
        assert result is not None, "Required property 'data_format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the schema to be created of max length of 255, and may only contain letters, numbers, hyphen, underscore, dollar sign, or hash mark.

        No whitespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schema.html#cfn-glue-schema-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schema_definition(self) -> builtins.str:
        '''The schema definition using the ``DataFormat`` setting for ``SchemaName`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schema.html#cfn-glue-schema-schemadefinition
        '''
        result = self._values.get("schema_definition")
        assert result is not None, "Required property 'schema_definition' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def checkpoint_version(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSchema.SchemaVersionProperty]]:
        '''Specify the ``VersionNumber`` or the ``IsLatest`` for setting the checkpoint for the schema.

        This is only required for updating a checkpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schema.html#cfn-glue-schema-checkpointversion
        '''
        result = self._values.get("checkpoint_version")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSchema.SchemaVersionProperty]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the schema if specified when created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schema.html#cfn-glue-schema-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def registry(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSchema.RegistryProperty]]:
        '''The registry where a schema is stored.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schema.html#cfn-glue-schema-registry
        '''
        result = self._values.get("registry")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSchema.RegistryProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''AWS tags that contain a key value pair and may be searched by console, command line, or API.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schema.html#cfn-glue-schema-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSchemaProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSchemaVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_glue.CfnSchemaVersion",
):
    '''The ``AWS::Glue::SchemaVersion`` is an AWS Glue resource type that manages schema versions of schemas in the AWS Glue Schema Registry.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversion.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_glue as glue
        
        cfn_schema_version = glue.CfnSchemaVersion(self, "MyCfnSchemaVersion",
            schema=glue.CfnSchemaVersion.SchemaProperty(
                registry_name="registryName",
                schema_arn="schemaArn",
                schema_name="schemaName"
            ),
            schema_definition="schemaDefinition"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        schema: typing.Union[_IResolvable_da3f097b, typing.Union["CfnSchemaVersion.SchemaProperty", typing.Dict[builtins.str, typing.Any]]],
        schema_definition: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param schema: The schema that includes the schema version.
        :param schema_definition: The schema definition for the schema version.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da5c949b18973d69cdae418c5f7d35241c93c30bd7bc7107898aaaaceb698e6e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSchemaVersionProps(
            schema=schema, schema_definition=schema_definition
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d9452a9d70f3e83a829bffc8890b5cfcb4a0c94403e5c71cf3e3ebe8bbd2492)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cb5cfc17ffddec9de88bdc242538249096b5eead4c8b77fb57579bb17b81c824)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrVersionId")
    def attr_version_id(self) -> builtins.str:
        '''Represents the version ID associated with the schema version.

        :cloudformationAttribute: VersionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVersionId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnSchemaVersion.SchemaProperty"]:
        '''The schema that includes the schema version.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnSchemaVersion.SchemaProperty"], jsii.get(self, "schema"))

    @schema.setter
    def schema(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnSchemaVersion.SchemaProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5443b6104677a75bc9caf64ee057fa55e785bec78f049fc4f5e67efd29bf7461)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schema", value)

    @builtins.property
    @jsii.member(jsii_name="schemaDefinition")
    def schema_definition(self) -> builtins.str:
        '''The schema definition for the schema version.'''
        return typing.cast(builtins.str, jsii.get(self, "schemaDefinition"))

    @schema_definition.setter
    def schema_definition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e456dd17518782fc61b283ca5fd68bf909fb10c1e515b9fb474ecbc27c8e77fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaDefinition", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnSchemaVersion.SchemaProperty",
        jsii_struct_bases=[],
        name_mapping={
            "registry_name": "registryName",
            "schema_arn": "schemaArn",
            "schema_name": "schemaName",
        },
    )
    class SchemaProperty:
        def __init__(
            self,
            *,
            registry_name: typing.Optional[builtins.str] = None,
            schema_arn: typing.Optional[builtins.str] = None,
            schema_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A wrapper structure to contain schema identity fields.

            Either ``SchemaArn`` , or ``SchemaName`` and ``RegistryName`` has to be provided.

            :param registry_name: The name of the registry where the schema is stored. Either ``SchemaArn`` , or ``SchemaName`` and ``RegistryName`` has to be provided.
            :param schema_arn: The Amazon Resource Name (ARN) of the schema. Either ``SchemaArn`` , or ``SchemaName`` and ``RegistryName`` has to be provided.
            :param schema_name: The name of the schema. Either ``SchemaArn`` , or ``SchemaName`` and ``RegistryName`` has to be provided.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-schemaversion-schema.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                schema_property = glue.CfnSchemaVersion.SchemaProperty(
                    registry_name="registryName",
                    schema_arn="schemaArn",
                    schema_name="schemaName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f58a0cb66904ee076f56bd0f3a3a196888dbbbe43086cf8bbd9b49084a112846)
                check_type(argname="argument registry_name", value=registry_name, expected_type=type_hints["registry_name"])
                check_type(argname="argument schema_arn", value=schema_arn, expected_type=type_hints["schema_arn"])
                check_type(argname="argument schema_name", value=schema_name, expected_type=type_hints["schema_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if registry_name is not None:
                self._values["registry_name"] = registry_name
            if schema_arn is not None:
                self._values["schema_arn"] = schema_arn
            if schema_name is not None:
                self._values["schema_name"] = schema_name

        @builtins.property
        def registry_name(self) -> typing.Optional[builtins.str]:
            '''The name of the registry where the schema is stored.

            Either ``SchemaArn`` , or ``SchemaName`` and ``RegistryName`` has to be provided.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-schemaversion-schema.html#cfn-glue-schemaversion-schema-registryname
            '''
            result = self._values.get("registry_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def schema_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the schema.

            Either ``SchemaArn`` , or ``SchemaName`` and ``RegistryName`` has to be provided.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-schemaversion-schema.html#cfn-glue-schemaversion-schema-schemaarn
            '''
            result = self._values.get("schema_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def schema_name(self) -> typing.Optional[builtins.str]:
            '''The name of the schema.

            Either ``SchemaArn`` , or ``SchemaName`` and ``RegistryName`` has to be provided.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-schemaversion-schema.html#cfn-glue-schemaversion-schema-schemaname
            '''
            result = self._values.get("schema_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SchemaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnSchemaVersionMetadata(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_glue.CfnSchemaVersionMetadata",
):
    '''The ``AWS::Glue::SchemaVersionMetadata`` is an AWS Glue resource type that defines the metadata key-value pairs for a schema version in AWS Glue Schema Registry.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversionmetadata.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_glue as glue
        
        cfn_schema_version_metadata = glue.CfnSchemaVersionMetadata(self, "MyCfnSchemaVersionMetadata",
            key="key",
            schema_version_id="schemaVersionId",
            value="value"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        key: builtins.str,
        schema_version_id: builtins.str,
        value: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param key: A metadata key in a key-value pair for metadata.
        :param schema_version_id: The version number of the schema.
        :param value: A metadata key's corresponding value.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a9a3e2496aeeeaf0a9f2c36f1a1d9a7ad7e6c6e6875c4024e3b0fdc4efba8f7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSchemaVersionMetadataProps(
            key=key, schema_version_id=schema_version_id, value=value
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bac3436fdb71de23e44fca8189770fd0ac700ebf763f7dcd804162c147430a02)
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
            type_hints = typing.get_type_hints(_typecheckingstub__93a32ac74bba3f51224a5f766cdd3a3caeaefa0b4e23580ca45bda0d4aef86ef)
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
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        '''A metadata key in a key-value pair for metadata.'''
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09ba199b752efbd3e189be84aa34a757c8f25ccebe52ad436e40c984b8b3bc6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="schemaVersionId")
    def schema_version_id(self) -> builtins.str:
        '''The version number of the schema.'''
        return typing.cast(builtins.str, jsii.get(self, "schemaVersionId"))

    @schema_version_id.setter
    def schema_version_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe366520765f5ad7f7a4e96a3e9d66b34f59675ae226488e2e7c96301b098c2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaVersionId", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        '''A metadata key's corresponding value.'''
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70216207f8d7da97cc8c8430c3dd8593322988412423bfad46412dc2c24ae7d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_glue.CfnSchemaVersionMetadataProps",
    jsii_struct_bases=[],
    name_mapping={
        "key": "key",
        "schema_version_id": "schemaVersionId",
        "value": "value",
    },
)
class CfnSchemaVersionMetadataProps:
    def __init__(
        self,
        *,
        key: builtins.str,
        schema_version_id: builtins.str,
        value: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnSchemaVersionMetadata``.

        :param key: A metadata key in a key-value pair for metadata.
        :param schema_version_id: The version number of the schema.
        :param value: A metadata key's corresponding value.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversionmetadata.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_glue as glue
            
            cfn_schema_version_metadata_props = glue.CfnSchemaVersionMetadataProps(
                key="key",
                schema_version_id="schemaVersionId",
                value="value"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d673339819d7914956c800afb9c521310733b754757fa3b69916588124f4856c)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument schema_version_id", value=schema_version_id, expected_type=type_hints["schema_version_id"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "schema_version_id": schema_version_id,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''A metadata key in a key-value pair for metadata.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversionmetadata.html#cfn-glue-schemaversionmetadata-key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schema_version_id(self) -> builtins.str:
        '''The version number of the schema.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversionmetadata.html#cfn-glue-schemaversionmetadata-schemaversionid
        '''
        result = self._values.get("schema_version_id")
        assert result is not None, "Required property 'schema_version_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''A metadata key's corresponding value.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversionmetadata.html#cfn-glue-schemaversionmetadata-value
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSchemaVersionMetadataProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_glue.CfnSchemaVersionProps",
    jsii_struct_bases=[],
    name_mapping={"schema": "schema", "schema_definition": "schemaDefinition"},
)
class CfnSchemaVersionProps:
    def __init__(
        self,
        *,
        schema: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchemaVersion.SchemaProperty, typing.Dict[builtins.str, typing.Any]]],
        schema_definition: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnSchemaVersion``.

        :param schema: The schema that includes the schema version.
        :param schema_definition: The schema definition for the schema version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_glue as glue
            
            cfn_schema_version_props = glue.CfnSchemaVersionProps(
                schema=glue.CfnSchemaVersion.SchemaProperty(
                    registry_name="registryName",
                    schema_arn="schemaArn",
                    schema_name="schemaName"
                ),
                schema_definition="schemaDefinition"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eeab38cc4ae72ae0d45e70c51097046996a15bcbd57776c5c6711c1cc3c34753)
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            check_type(argname="argument schema_definition", value=schema_definition, expected_type=type_hints["schema_definition"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "schema": schema,
            "schema_definition": schema_definition,
        }

    @builtins.property
    def schema(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnSchemaVersion.SchemaProperty]:
        '''The schema that includes the schema version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversion.html#cfn-glue-schemaversion-schema
        '''
        result = self._values.get("schema")
        assert result is not None, "Required property 'schema' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnSchemaVersion.SchemaProperty], result)

    @builtins.property
    def schema_definition(self) -> builtins.str:
        '''The schema definition for the schema version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversion.html#cfn-glue-schemaversion-schemadefinition
        '''
        result = self._values.get("schema_definition")
        assert result is not None, "Required property 'schema_definition' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSchemaVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSecurityConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_glue.CfnSecurityConfiguration",
):
    '''Creates a new security configuration.

    A security configuration is a set of security properties that can be used by AWS Glue . You can use a security configuration to encrypt data at rest. For information about using security configurations in AWS Glue , see `Encrypting Data Written by Crawlers, Jobs, and Development Endpoints <https://docs.aws.amazon.com/glue/latest/dg/encryption-security-configuration.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-securityconfiguration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_glue as glue
        
        cfn_security_configuration = glue.CfnSecurityConfiguration(self, "MyCfnSecurityConfiguration",
            encryption_configuration=glue.CfnSecurityConfiguration.EncryptionConfigurationProperty(
                cloud_watch_encryption=glue.CfnSecurityConfiguration.CloudWatchEncryptionProperty(
                    cloud_watch_encryption_mode="cloudWatchEncryptionMode",
                    kms_key_arn="kmsKeyArn"
                ),
                job_bookmarks_encryption=glue.CfnSecurityConfiguration.JobBookmarksEncryptionProperty(
                    job_bookmarks_encryption_mode="jobBookmarksEncryptionMode",
                    kms_key_arn="kmsKeyArn"
                ),
                s3_encryptions=[glue.CfnSecurityConfiguration.S3EncryptionProperty(
                    kms_key_arn="kmsKeyArn",
                    s3_encryption_mode="s3EncryptionMode"
                )]
            ),
            name="name"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        encryption_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnSecurityConfiguration.EncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param encryption_configuration: The encryption configuration associated with this security configuration.
        :param name: The name of the security configuration.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c75e7a9665c1990bc4f5c74c4d708791cc9808fb5f2dd7221d5808a570d6ca4f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSecurityConfigurationProps(
            encryption_configuration=encryption_configuration, name=name
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edb3649bcf711595ed0e7f1ff5f9487f357ca680d6c33c94cce0d4945c1110ca)
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
            type_hints = typing.get_type_hints(_typecheckingstub__76a673725f7d43dfd4d86005be3140e85bafdb23ee1eec2302634a8e2738146f)
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
    @jsii.member(jsii_name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnSecurityConfiguration.EncryptionConfigurationProperty"]:
        '''The encryption configuration associated with this security configuration.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnSecurityConfiguration.EncryptionConfigurationProperty"], jsii.get(self, "encryptionConfiguration"))

    @encryption_configuration.setter
    def encryption_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnSecurityConfiguration.EncryptionConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41a8b680be4f05190dbfd222f5985022aede1900f04a5407fb5617312ab60e00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the security configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8331f03d77759f61a97615e9eeefbfcaa25822091618cf7de977db83cbfd7d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnSecurityConfiguration.CloudWatchEncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_watch_encryption_mode": "cloudWatchEncryptionMode",
            "kms_key_arn": "kmsKeyArn",
        },
    )
    class CloudWatchEncryptionProperty:
        def __init__(
            self,
            *,
            cloud_watch_encryption_mode: typing.Optional[builtins.str] = None,
            kms_key_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies how Amazon CloudWatch data should be encrypted.

            :param cloud_watch_encryption_mode: The encryption mode to use for CloudWatch data.
            :param kms_key_arn: The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-cloudwatchencryption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                cloud_watch_encryption_property = glue.CfnSecurityConfiguration.CloudWatchEncryptionProperty(
                    cloud_watch_encryption_mode="cloudWatchEncryptionMode",
                    kms_key_arn="kmsKeyArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__368c78d5e54f1e192576beedf15b669bbe7d53dbacdbe73327838ca2c71a5e9c)
                check_type(argname="argument cloud_watch_encryption_mode", value=cloud_watch_encryption_mode, expected_type=type_hints["cloud_watch_encryption_mode"])
                check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cloud_watch_encryption_mode is not None:
                self._values["cloud_watch_encryption_mode"] = cloud_watch_encryption_mode
            if kms_key_arn is not None:
                self._values["kms_key_arn"] = kms_key_arn

        @builtins.property
        def cloud_watch_encryption_mode(self) -> typing.Optional[builtins.str]:
            '''The encryption mode to use for CloudWatch data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-cloudwatchencryption.html#cfn-glue-securityconfiguration-cloudwatchencryption-cloudwatchencryptionmode
            '''
            result = self._values.get("cloud_watch_encryption_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def kms_key_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-cloudwatchencryption.html#cfn-glue-securityconfiguration-cloudwatchencryption-kmskeyarn
            '''
            result = self._values.get("kms_key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchEncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnSecurityConfiguration.EncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_watch_encryption": "cloudWatchEncryption",
            "job_bookmarks_encryption": "jobBookmarksEncryption",
            "s3_encryptions": "s3Encryptions",
        },
    )
    class EncryptionConfigurationProperty:
        def __init__(
            self,
            *,
            cloud_watch_encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSecurityConfiguration.CloudWatchEncryptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            job_bookmarks_encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSecurityConfiguration.JobBookmarksEncryptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_encryptions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSecurityConfiguration.S3EncryptionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Specifies an encryption configuration.

            :param cloud_watch_encryption: The encryption configuration for Amazon CloudWatch.
            :param job_bookmarks_encryption: The encryption configuration for job bookmarks.
            :param s3_encryptions: The encyption configuration for Amazon Simple Storage Service (Amazon S3) data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-encryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                encryption_configuration_property = glue.CfnSecurityConfiguration.EncryptionConfigurationProperty(
                    cloud_watch_encryption=glue.CfnSecurityConfiguration.CloudWatchEncryptionProperty(
                        cloud_watch_encryption_mode="cloudWatchEncryptionMode",
                        kms_key_arn="kmsKeyArn"
                    ),
                    job_bookmarks_encryption=glue.CfnSecurityConfiguration.JobBookmarksEncryptionProperty(
                        job_bookmarks_encryption_mode="jobBookmarksEncryptionMode",
                        kms_key_arn="kmsKeyArn"
                    ),
                    s3_encryptions=[glue.CfnSecurityConfiguration.S3EncryptionProperty(
                        kms_key_arn="kmsKeyArn",
                        s3_encryption_mode="s3EncryptionMode"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a6be244b0a6c6cf18e64a0019f78450ca4ed5b5a8db428f106e8577b9d4c685e)
                check_type(argname="argument cloud_watch_encryption", value=cloud_watch_encryption, expected_type=type_hints["cloud_watch_encryption"])
                check_type(argname="argument job_bookmarks_encryption", value=job_bookmarks_encryption, expected_type=type_hints["job_bookmarks_encryption"])
                check_type(argname="argument s3_encryptions", value=s3_encryptions, expected_type=type_hints["s3_encryptions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cloud_watch_encryption is not None:
                self._values["cloud_watch_encryption"] = cloud_watch_encryption
            if job_bookmarks_encryption is not None:
                self._values["job_bookmarks_encryption"] = job_bookmarks_encryption
            if s3_encryptions is not None:
                self._values["s3_encryptions"] = s3_encryptions

        @builtins.property
        def cloud_watch_encryption(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSecurityConfiguration.CloudWatchEncryptionProperty"]]:
            '''The encryption configuration for Amazon CloudWatch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-encryptionconfiguration.html#cfn-glue-securityconfiguration-encryptionconfiguration-cloudwatchencryption
            '''
            result = self._values.get("cloud_watch_encryption")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSecurityConfiguration.CloudWatchEncryptionProperty"]], result)

        @builtins.property
        def job_bookmarks_encryption(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSecurityConfiguration.JobBookmarksEncryptionProperty"]]:
            '''The encryption configuration for job bookmarks.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-encryptionconfiguration.html#cfn-glue-securityconfiguration-encryptionconfiguration-jobbookmarksencryption
            '''
            result = self._values.get("job_bookmarks_encryption")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSecurityConfiguration.JobBookmarksEncryptionProperty"]], result)

        @builtins.property
        def s3_encryptions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSecurityConfiguration.S3EncryptionProperty"]]]]:
            '''The encyption configuration for Amazon Simple Storage Service (Amazon S3) data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-encryptionconfiguration.html#cfn-glue-securityconfiguration-encryptionconfiguration-s3encryptions
            '''
            result = self._values.get("s3_encryptions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSecurityConfiguration.S3EncryptionProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnSecurityConfiguration.JobBookmarksEncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "job_bookmarks_encryption_mode": "jobBookmarksEncryptionMode",
            "kms_key_arn": "kmsKeyArn",
        },
    )
    class JobBookmarksEncryptionProperty:
        def __init__(
            self,
            *,
            job_bookmarks_encryption_mode: typing.Optional[builtins.str] = None,
            kms_key_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies how job bookmark data should be encrypted.

            :param job_bookmarks_encryption_mode: The encryption mode to use for job bookmarks data.
            :param kms_key_arn: The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-jobbookmarksencryption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                job_bookmarks_encryption_property = glue.CfnSecurityConfiguration.JobBookmarksEncryptionProperty(
                    job_bookmarks_encryption_mode="jobBookmarksEncryptionMode",
                    kms_key_arn="kmsKeyArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6b53a1d7654ab253ef322d5aaa00ef3c7b70301e4abe429e8f48779118b20214)
                check_type(argname="argument job_bookmarks_encryption_mode", value=job_bookmarks_encryption_mode, expected_type=type_hints["job_bookmarks_encryption_mode"])
                check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if job_bookmarks_encryption_mode is not None:
                self._values["job_bookmarks_encryption_mode"] = job_bookmarks_encryption_mode
            if kms_key_arn is not None:
                self._values["kms_key_arn"] = kms_key_arn

        @builtins.property
        def job_bookmarks_encryption_mode(self) -> typing.Optional[builtins.str]:
            '''The encryption mode to use for job bookmarks data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-jobbookmarksencryption.html#cfn-glue-securityconfiguration-jobbookmarksencryption-jobbookmarksencryptionmode
            '''
            result = self._values.get("job_bookmarks_encryption_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def kms_key_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-jobbookmarksencryption.html#cfn-glue-securityconfiguration-jobbookmarksencryption-kmskeyarn
            '''
            result = self._values.get("kms_key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JobBookmarksEncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnSecurityConfiguration.S3EncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "kms_key_arn": "kmsKeyArn",
            "s3_encryption_mode": "s3EncryptionMode",
        },
    )
    class S3EncryptionProperty:
        def __init__(
            self,
            *,
            kms_key_arn: typing.Optional[builtins.str] = None,
            s3_encryption_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies how Amazon Simple Storage Service (Amazon S3) data should be encrypted.

            :param kms_key_arn: The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.
            :param s3_encryption_mode: The encryption mode to use for Amazon S3 data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-s3encryption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                s3_encryption_property = glue.CfnSecurityConfiguration.S3EncryptionProperty(
                    kms_key_arn="kmsKeyArn",
                    s3_encryption_mode="s3EncryptionMode"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__67ce5f76883b1039f240fd048a55ad06c44c08bb06b2064044add8b05be50eb8)
                check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
                check_type(argname="argument s3_encryption_mode", value=s3_encryption_mode, expected_type=type_hints["s3_encryption_mode"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if kms_key_arn is not None:
                self._values["kms_key_arn"] = kms_key_arn
            if s3_encryption_mode is not None:
                self._values["s3_encryption_mode"] = s3_encryption_mode

        @builtins.property
        def kms_key_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-s3encryption.html#cfn-glue-securityconfiguration-s3encryption-kmskeyarn
            '''
            result = self._values.get("kms_key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_encryption_mode(self) -> typing.Optional[builtins.str]:
            '''The encryption mode to use for Amazon S3 data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-s3encryption.html#cfn-glue-securityconfiguration-s3encryption-s3encryptionmode
            '''
            result = self._values.get("s3_encryption_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3EncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_glue.CfnSecurityConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "encryption_configuration": "encryptionConfiguration",
        "name": "name",
    },
)
class CfnSecurityConfigurationProps:
    def __init__(
        self,
        *,
        encryption_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityConfiguration.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnSecurityConfiguration``.

        :param encryption_configuration: The encryption configuration associated with this security configuration.
        :param name: The name of the security configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-securityconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_glue as glue
            
            cfn_security_configuration_props = glue.CfnSecurityConfigurationProps(
                encryption_configuration=glue.CfnSecurityConfiguration.EncryptionConfigurationProperty(
                    cloud_watch_encryption=glue.CfnSecurityConfiguration.CloudWatchEncryptionProperty(
                        cloud_watch_encryption_mode="cloudWatchEncryptionMode",
                        kms_key_arn="kmsKeyArn"
                    ),
                    job_bookmarks_encryption=glue.CfnSecurityConfiguration.JobBookmarksEncryptionProperty(
                        job_bookmarks_encryption_mode="jobBookmarksEncryptionMode",
                        kms_key_arn="kmsKeyArn"
                    ),
                    s3_encryptions=[glue.CfnSecurityConfiguration.S3EncryptionProperty(
                        kms_key_arn="kmsKeyArn",
                        s3_encryption_mode="s3EncryptionMode"
                    )]
                ),
                name="name"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5cc25b086c49f8ea0218f40bb10d196be50cfd3ed39b43b3782a73ab6215552)
            check_type(argname="argument encryption_configuration", value=encryption_configuration, expected_type=type_hints["encryption_configuration"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "encryption_configuration": encryption_configuration,
            "name": name,
        }

    @builtins.property
    def encryption_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnSecurityConfiguration.EncryptionConfigurationProperty]:
        '''The encryption configuration associated with this security configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-securityconfiguration.html#cfn-glue-securityconfiguration-encryptionconfiguration
        '''
        result = self._values.get("encryption_configuration")
        assert result is not None, "Required property 'encryption_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnSecurityConfiguration.EncryptionConfigurationProperty], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the security configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-securityconfiguration.html#cfn-glue-securityconfiguration-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSecurityConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnTable(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_glue.CfnTable",
):
    '''The ``AWS::Glue::Table`` resource specifies tabular data in the AWS Glue data catalog.

    For more information, see `Defining Tables in the AWS Glue Data Catalog <https://docs.aws.amazon.com/glue/latest/dg/tables-described.html>`_ and `Table Structure <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-Table>`_ in the *AWS Glue Developer Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-table.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_glue as glue
        
        # parameters: Any
        # skewed_column_value_location_maps: Any
        
        cfn_table = glue.CfnTable(self, "MyCfnTable",
            catalog_id="catalogId",
            database_name="databaseName",
            table_input=glue.CfnTable.TableInputProperty(
                description="description",
                name="name",
                owner="owner",
                parameters=parameters,
                partition_keys=[glue.CfnTable.ColumnProperty(
                    name="name",
        
                    # the properties below are optional
                    comment="comment",
                    type="type"
                )],
                retention=123,
                storage_descriptor=glue.CfnTable.StorageDescriptorProperty(
                    bucket_columns=["bucketColumns"],
                    columns=[glue.CfnTable.ColumnProperty(
                        name="name",
        
                        # the properties below are optional
                        comment="comment",
                        type="type"
                    )],
                    compressed=False,
                    input_format="inputFormat",
                    location="location",
                    number_of_buckets=123,
                    output_format="outputFormat",
                    parameters=parameters,
                    schema_reference=glue.CfnTable.SchemaReferenceProperty(
                        schema_id=glue.CfnTable.SchemaIdProperty(
                            registry_name="registryName",
                            schema_arn="schemaArn",
                            schema_name="schemaName"
                        ),
                        schema_version_id="schemaVersionId",
                        schema_version_number=123
                    ),
                    serde_info=glue.CfnTable.SerdeInfoProperty(
                        name="name",
                        parameters=parameters,
                        serialization_library="serializationLibrary"
                    ),
                    skewed_info=glue.CfnTable.SkewedInfoProperty(
                        skewed_column_names=["skewedColumnNames"],
                        skewed_column_value_location_maps=skewed_column_value_location_maps,
                        skewed_column_values=["skewedColumnValues"]
                    ),
                    sort_columns=[glue.CfnTable.OrderProperty(
                        column="column",
                        sort_order=123
                    )],
                    stored_as_sub_directories=False
                ),
                table_type="tableType",
                target_table=glue.CfnTable.TableIdentifierProperty(
                    catalog_id="catalogId",
                    database_name="databaseName",
                    name="name"
                ),
                view_expanded_text="viewExpandedText",
                view_original_text="viewOriginalText"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        catalog_id: builtins.str,
        database_name: builtins.str,
        table_input: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTable.TableInputProperty", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param catalog_id: The ID of the Data Catalog in which to create the ``Table`` .
        :param database_name: The name of the database where the table metadata resides. For Hive compatibility, this must be all lowercase.
        :param table_input: A structure used to define a table.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63721068e81107cadbf3e418ec393de98f88a141604f2bb1044b5ae302e922ad)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTableProps(
            catalog_id=catalog_id, database_name=database_name, table_input=table_input
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19801c3c5af0f333bf6e5e99c3031543e54a8cf3b68bccf6cc457fd27b0f044e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__93805e92164ccafb607348423ac63ddda887c45f7d48102bc24275f7c7e179ed)
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
    @jsii.member(jsii_name="catalogId")
    def catalog_id(self) -> builtins.str:
        '''The ID of the Data Catalog in which to create the ``Table`` .'''
        return typing.cast(builtins.str, jsii.get(self, "catalogId"))

    @catalog_id.setter
    def catalog_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1518e6f292d33421716de5a7971329e9e9458a0245c61bae2b6f6d4dc066edb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogId", value)

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        '''The name of the database where the table metadata resides.'''
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3fa952b72d41b65e2c9a7ed9081c9236064d05e026dd37d5608da4cae676e88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="tableInput")
    def table_input(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnTable.TableInputProperty"]:
        '''A structure used to define a table.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTable.TableInputProperty"], jsii.get(self, "tableInput"))

    @table_input.setter
    def table_input(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnTable.TableInputProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9200a2bfb582a6d400aba47da5ed4d77a8ca52ee0956131ca52cdc58253cb811)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableInput", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnTable.ColumnProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "comment": "comment", "type": "type"},
    )
    class ColumnProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            comment: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A column in a ``Table`` .

            :param name: The name of the ``Column`` .
            :param comment: A free-form text comment.
            :param type: The data type of the ``Column`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-column.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                column_property = glue.CfnTable.ColumnProperty(
                    name="name",
                
                    # the properties below are optional
                    comment="comment",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__341bb786dd6f598e8fcaf71f90ff3da761cc3d8304f5ad4f6619ba17f44144aa)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }
            if comment is not None:
                self._values["comment"] = comment
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the ``Column`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-column.html#cfn-glue-table-column-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def comment(self) -> typing.Optional[builtins.str]:
            '''A free-form text comment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-column.html#cfn-glue-table-column-comment
            '''
            result = self._values.get("comment")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The data type of the ``Column`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-column.html#cfn-glue-table-column-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ColumnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnTable.OrderProperty",
        jsii_struct_bases=[],
        name_mapping={"column": "column", "sort_order": "sortOrder"},
    )
    class OrderProperty:
        def __init__(self, *, column: builtins.str, sort_order: jsii.Number) -> None:
            '''Specifies the sort order of a sorted column.

            :param column: The name of the column.
            :param sort_order: Indicates that the column is sorted in ascending order ( ``== 1`` ), or in descending order ( ``==0`` ).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-order.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                order_property = glue.CfnTable.OrderProperty(
                    column="column",
                    sort_order=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0ef4b90841abfe4615325735c716d9eaa2a8839a68d0c4650f1bb4275935dfa1)
                check_type(argname="argument column", value=column, expected_type=type_hints["column"])
                check_type(argname="argument sort_order", value=sort_order, expected_type=type_hints["sort_order"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "column": column,
                "sort_order": sort_order,
            }

        @builtins.property
        def column(self) -> builtins.str:
            '''The name of the column.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-order.html#cfn-glue-table-order-column
            '''
            result = self._values.get("column")
            assert result is not None, "Required property 'column' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sort_order(self) -> jsii.Number:
            '''Indicates that the column is sorted in ascending order ( ``== 1`` ), or in descending order ( ``==0`` ).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-order.html#cfn-glue-table-order-sortorder
            '''
            result = self._values.get("sort_order")
            assert result is not None, "Required property 'sort_order' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OrderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnTable.SchemaIdProperty",
        jsii_struct_bases=[],
        name_mapping={
            "registry_name": "registryName",
            "schema_arn": "schemaArn",
            "schema_name": "schemaName",
        },
    )
    class SchemaIdProperty:
        def __init__(
            self,
            *,
            registry_name: typing.Optional[builtins.str] = None,
            schema_arn: typing.Optional[builtins.str] = None,
            schema_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A structure that contains schema identity fields.

            Either this or the ``SchemaVersionId`` has to be
            provided.

            :param registry_name: The name of the schema registry that contains the schema.
            :param schema_arn: The Amazon Resource Name (ARN) of the schema. One of ``SchemaArn`` or ``SchemaName`` has to be provided.
            :param schema_name: The name of the schema. One of ``SchemaArn`` or ``SchemaName`` has to be provided.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-schemaid.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                schema_id_property = glue.CfnTable.SchemaIdProperty(
                    registry_name="registryName",
                    schema_arn="schemaArn",
                    schema_name="schemaName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__213074459ce3731da4f39ec028b3a7336f7b03aa4c9acead9a5d83aab68dd299)
                check_type(argname="argument registry_name", value=registry_name, expected_type=type_hints["registry_name"])
                check_type(argname="argument schema_arn", value=schema_arn, expected_type=type_hints["schema_arn"])
                check_type(argname="argument schema_name", value=schema_name, expected_type=type_hints["schema_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if registry_name is not None:
                self._values["registry_name"] = registry_name
            if schema_arn is not None:
                self._values["schema_arn"] = schema_arn
            if schema_name is not None:
                self._values["schema_name"] = schema_name

        @builtins.property
        def registry_name(self) -> typing.Optional[builtins.str]:
            '''The name of the schema registry that contains the schema.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-schemaid.html#cfn-glue-table-schemaid-registryname
            '''
            result = self._values.get("registry_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def schema_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the schema.

            One of ``SchemaArn`` or ``SchemaName`` has to be
            provided.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-schemaid.html#cfn-glue-table-schemaid-schemaarn
            '''
            result = self._values.get("schema_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def schema_name(self) -> typing.Optional[builtins.str]:
            '''The name of the schema.

            One of ``SchemaArn`` or ``SchemaName`` has to be provided.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-schemaid.html#cfn-glue-table-schemaid-schemaname
            '''
            result = self._values.get("schema_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SchemaIdProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnTable.SchemaReferenceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "schema_id": "schemaId",
            "schema_version_id": "schemaVersionId",
            "schema_version_number": "schemaVersionNumber",
        },
    )
    class SchemaReferenceProperty:
        def __init__(
            self,
            *,
            schema_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTable.SchemaIdProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            schema_version_id: typing.Optional[builtins.str] = None,
            schema_version_number: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''An object that references a schema stored in the AWS Glue Schema Registry.

            :param schema_id: A structure that contains schema identity fields. Either this or the ``SchemaVersionId`` has to be provided.
            :param schema_version_id: The unique ID assigned to a version of the schema. Either this or the ``SchemaId`` has to be provided.
            :param schema_version_number: The version number of the schema.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-schemareference.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                schema_reference_property = glue.CfnTable.SchemaReferenceProperty(
                    schema_id=glue.CfnTable.SchemaIdProperty(
                        registry_name="registryName",
                        schema_arn="schemaArn",
                        schema_name="schemaName"
                    ),
                    schema_version_id="schemaVersionId",
                    schema_version_number=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a6f714e7fb5c6d7bfdf385116f7f3dbd2eceb979753572daea288d033fe34254)
                check_type(argname="argument schema_id", value=schema_id, expected_type=type_hints["schema_id"])
                check_type(argname="argument schema_version_id", value=schema_version_id, expected_type=type_hints["schema_version_id"])
                check_type(argname="argument schema_version_number", value=schema_version_number, expected_type=type_hints["schema_version_number"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if schema_id is not None:
                self._values["schema_id"] = schema_id
            if schema_version_id is not None:
                self._values["schema_version_id"] = schema_version_id
            if schema_version_number is not None:
                self._values["schema_version_number"] = schema_version_number

        @builtins.property
        def schema_id(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTable.SchemaIdProperty"]]:
            '''A structure that contains schema identity fields.

            Either this or the ``SchemaVersionId`` has to be
            provided.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-schemareference.html#cfn-glue-table-schemareference-schemaid
            '''
            result = self._values.get("schema_id")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTable.SchemaIdProperty"]], result)

        @builtins.property
        def schema_version_id(self) -> typing.Optional[builtins.str]:
            '''The unique ID assigned to a version of the schema.

            Either this or the ``SchemaId`` has to be provided.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-schemareference.html#cfn-glue-table-schemareference-schemaversionid
            '''
            result = self._values.get("schema_version_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def schema_version_number(self) -> typing.Optional[jsii.Number]:
            '''The version number of the schema.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-schemareference.html#cfn-glue-table-schemareference-schemaversionnumber
            '''
            result = self._values.get("schema_version_number")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SchemaReferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnTable.SerdeInfoProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "parameters": "parameters",
            "serialization_library": "serializationLibrary",
        },
    )
    class SerdeInfoProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            parameters: typing.Any = None,
            serialization_library: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about a serialization/deserialization program (SerDe) that serves as an extractor and loader.

            :param name: Name of the SerDe.
            :param parameters: These key-value pairs define initialization parameters for the SerDe.
            :param serialization_library: Usually the class that implements the SerDe. An example is ``org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-serdeinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                # parameters: Any
                
                serde_info_property = glue.CfnTable.SerdeInfoProperty(
                    name="name",
                    parameters=parameters,
                    serialization_library="serializationLibrary"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e7540ba85e270907160df5e52f6d2f15874b400f181d969a4c9106d88b8081d5)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
                check_type(argname="argument serialization_library", value=serialization_library, expected_type=type_hints["serialization_library"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if parameters is not None:
                self._values["parameters"] = parameters
            if serialization_library is not None:
                self._values["serialization_library"] = serialization_library

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''Name of the SerDe.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-serdeinfo.html#cfn-glue-table-serdeinfo-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parameters(self) -> typing.Any:
            '''These key-value pairs define initialization parameters for the SerDe.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-serdeinfo.html#cfn-glue-table-serdeinfo-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Any, result)

        @builtins.property
        def serialization_library(self) -> typing.Optional[builtins.str]:
            '''Usually the class that implements the SerDe.

            An example is ``org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-serdeinfo.html#cfn-glue-table-serdeinfo-serializationlibrary
            '''
            result = self._values.get("serialization_library")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SerdeInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnTable.SkewedInfoProperty",
        jsii_struct_bases=[],
        name_mapping={
            "skewed_column_names": "skewedColumnNames",
            "skewed_column_value_location_maps": "skewedColumnValueLocationMaps",
            "skewed_column_values": "skewedColumnValues",
        },
    )
    class SkewedInfoProperty:
        def __init__(
            self,
            *,
            skewed_column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
            skewed_column_value_location_maps: typing.Any = None,
            skewed_column_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Specifies skewed values in a table.

            Skewed values are those that occur with very high frequency.

            :param skewed_column_names: A list of names of columns that contain skewed values.
            :param skewed_column_value_location_maps: A mapping of skewed values to the columns that contain them.
            :param skewed_column_values: A list of values that appear so frequently as to be considered skewed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-skewedinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                # skewed_column_value_location_maps: Any
                
                skewed_info_property = glue.CfnTable.SkewedInfoProperty(
                    skewed_column_names=["skewedColumnNames"],
                    skewed_column_value_location_maps=skewed_column_value_location_maps,
                    skewed_column_values=["skewedColumnValues"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__74aa76421b217af4a6e44cf71728cfad7a6ee7c23170fcb750c074e1a95d2616)
                check_type(argname="argument skewed_column_names", value=skewed_column_names, expected_type=type_hints["skewed_column_names"])
                check_type(argname="argument skewed_column_value_location_maps", value=skewed_column_value_location_maps, expected_type=type_hints["skewed_column_value_location_maps"])
                check_type(argname="argument skewed_column_values", value=skewed_column_values, expected_type=type_hints["skewed_column_values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if skewed_column_names is not None:
                self._values["skewed_column_names"] = skewed_column_names
            if skewed_column_value_location_maps is not None:
                self._values["skewed_column_value_location_maps"] = skewed_column_value_location_maps
            if skewed_column_values is not None:
                self._values["skewed_column_values"] = skewed_column_values

        @builtins.property
        def skewed_column_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of names of columns that contain skewed values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-skewedinfo.html#cfn-glue-table-skewedinfo-skewedcolumnnames
            '''
            result = self._values.get("skewed_column_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def skewed_column_value_location_maps(self) -> typing.Any:
            '''A mapping of skewed values to the columns that contain them.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-skewedinfo.html#cfn-glue-table-skewedinfo-skewedcolumnvaluelocationmaps
            '''
            result = self._values.get("skewed_column_value_location_maps")
            return typing.cast(typing.Any, result)

        @builtins.property
        def skewed_column_values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of values that appear so frequently as to be considered skewed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-skewedinfo.html#cfn-glue-table-skewedinfo-skewedcolumnvalues
            '''
            result = self._values.get("skewed_column_values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SkewedInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnTable.StorageDescriptorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_columns": "bucketColumns",
            "columns": "columns",
            "compressed": "compressed",
            "input_format": "inputFormat",
            "location": "location",
            "number_of_buckets": "numberOfBuckets",
            "output_format": "outputFormat",
            "parameters": "parameters",
            "schema_reference": "schemaReference",
            "serde_info": "serdeInfo",
            "skewed_info": "skewedInfo",
            "sort_columns": "sortColumns",
            "stored_as_sub_directories": "storedAsSubDirectories",
        },
    )
    class StorageDescriptorProperty:
        def __init__(
            self,
            *,
            bucket_columns: typing.Optional[typing.Sequence[builtins.str]] = None,
            columns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTable.ColumnProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            compressed: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            input_format: typing.Optional[builtins.str] = None,
            location: typing.Optional[builtins.str] = None,
            number_of_buckets: typing.Optional[jsii.Number] = None,
            output_format: typing.Optional[builtins.str] = None,
            parameters: typing.Any = None,
            schema_reference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTable.SchemaReferenceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            serde_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTable.SerdeInfoProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            skewed_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTable.SkewedInfoProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sort_columns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTable.OrderProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            stored_as_sub_directories: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Describes the physical storage of table data.

            :param bucket_columns: A list of reducer grouping columns, clustering columns, and bucketing columns in the table.
            :param columns: A list of the ``Columns`` in the table.
            :param compressed: ``True`` if the data in the table is compressed, or ``False`` if not.
            :param input_format: The input format: ``SequenceFileInputFormat`` (binary), or ``TextInputFormat`` , or a custom format.
            :param location: The physical location of the table. By default, this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.
            :param number_of_buckets: Must be specified if the table contains any dimension columns.
            :param output_format: The output format: ``SequenceFileOutputFormat`` (binary), or ``IgnoreKeyTextOutputFormat`` , or a custom format.
            :param parameters: The user-supplied properties in key-value form.
            :param schema_reference: An object that references a schema stored in the AWS Glue Schema Registry.
            :param serde_info: The serialization/deserialization (SerDe) information.
            :param skewed_info: The information about values that appear frequently in a column (skewed values).
            :param sort_columns: A list specifying the sort order of each bucket in the table.
            :param stored_as_sub_directories: ``True`` if the table data is stored in subdirectories, or ``False`` if not.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-storagedescriptor.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                # parameters: Any
                # skewed_column_value_location_maps: Any
                
                storage_descriptor_property = glue.CfnTable.StorageDescriptorProperty(
                    bucket_columns=["bucketColumns"],
                    columns=[glue.CfnTable.ColumnProperty(
                        name="name",
                
                        # the properties below are optional
                        comment="comment",
                        type="type"
                    )],
                    compressed=False,
                    input_format="inputFormat",
                    location="location",
                    number_of_buckets=123,
                    output_format="outputFormat",
                    parameters=parameters,
                    schema_reference=glue.CfnTable.SchemaReferenceProperty(
                        schema_id=glue.CfnTable.SchemaIdProperty(
                            registry_name="registryName",
                            schema_arn="schemaArn",
                            schema_name="schemaName"
                        ),
                        schema_version_id="schemaVersionId",
                        schema_version_number=123
                    ),
                    serde_info=glue.CfnTable.SerdeInfoProperty(
                        name="name",
                        parameters=parameters,
                        serialization_library="serializationLibrary"
                    ),
                    skewed_info=glue.CfnTable.SkewedInfoProperty(
                        skewed_column_names=["skewedColumnNames"],
                        skewed_column_value_location_maps=skewed_column_value_location_maps,
                        skewed_column_values=["skewedColumnValues"]
                    ),
                    sort_columns=[glue.CfnTable.OrderProperty(
                        column="column",
                        sort_order=123
                    )],
                    stored_as_sub_directories=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__95dc40dfb9eed01d30a631a9ddab00c9a5d1b2a3111b03046997bd45a3a28100)
                check_type(argname="argument bucket_columns", value=bucket_columns, expected_type=type_hints["bucket_columns"])
                check_type(argname="argument columns", value=columns, expected_type=type_hints["columns"])
                check_type(argname="argument compressed", value=compressed, expected_type=type_hints["compressed"])
                check_type(argname="argument input_format", value=input_format, expected_type=type_hints["input_format"])
                check_type(argname="argument location", value=location, expected_type=type_hints["location"])
                check_type(argname="argument number_of_buckets", value=number_of_buckets, expected_type=type_hints["number_of_buckets"])
                check_type(argname="argument output_format", value=output_format, expected_type=type_hints["output_format"])
                check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
                check_type(argname="argument schema_reference", value=schema_reference, expected_type=type_hints["schema_reference"])
                check_type(argname="argument serde_info", value=serde_info, expected_type=type_hints["serde_info"])
                check_type(argname="argument skewed_info", value=skewed_info, expected_type=type_hints["skewed_info"])
                check_type(argname="argument sort_columns", value=sort_columns, expected_type=type_hints["sort_columns"])
                check_type(argname="argument stored_as_sub_directories", value=stored_as_sub_directories, expected_type=type_hints["stored_as_sub_directories"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if bucket_columns is not None:
                self._values["bucket_columns"] = bucket_columns
            if columns is not None:
                self._values["columns"] = columns
            if compressed is not None:
                self._values["compressed"] = compressed
            if input_format is not None:
                self._values["input_format"] = input_format
            if location is not None:
                self._values["location"] = location
            if number_of_buckets is not None:
                self._values["number_of_buckets"] = number_of_buckets
            if output_format is not None:
                self._values["output_format"] = output_format
            if parameters is not None:
                self._values["parameters"] = parameters
            if schema_reference is not None:
                self._values["schema_reference"] = schema_reference
            if serde_info is not None:
                self._values["serde_info"] = serde_info
            if skewed_info is not None:
                self._values["skewed_info"] = skewed_info
            if sort_columns is not None:
                self._values["sort_columns"] = sort_columns
            if stored_as_sub_directories is not None:
                self._values["stored_as_sub_directories"] = stored_as_sub_directories

        @builtins.property
        def bucket_columns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of reducer grouping columns, clustering columns, and bucketing columns in the table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-storagedescriptor.html#cfn-glue-table-storagedescriptor-bucketcolumns
            '''
            result = self._values.get("bucket_columns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def columns(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTable.ColumnProperty"]]]]:
            '''A list of the ``Columns`` in the table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-storagedescriptor.html#cfn-glue-table-storagedescriptor-columns
            '''
            result = self._values.get("columns")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTable.ColumnProperty"]]]], result)

        @builtins.property
        def compressed(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``True`` if the data in the table is compressed, or ``False`` if not.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-storagedescriptor.html#cfn-glue-table-storagedescriptor-compressed
            '''
            result = self._values.get("compressed")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def input_format(self) -> typing.Optional[builtins.str]:
            '''The input format: ``SequenceFileInputFormat`` (binary), or ``TextInputFormat`` , or a custom format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-storagedescriptor.html#cfn-glue-table-storagedescriptor-inputformat
            '''
            result = self._values.get("input_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def location(self) -> typing.Optional[builtins.str]:
            '''The physical location of the table.

            By default, this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-storagedescriptor.html#cfn-glue-table-storagedescriptor-location
            '''
            result = self._values.get("location")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def number_of_buckets(self) -> typing.Optional[jsii.Number]:
            '''Must be specified if the table contains any dimension columns.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-storagedescriptor.html#cfn-glue-table-storagedescriptor-numberofbuckets
            '''
            result = self._values.get("number_of_buckets")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def output_format(self) -> typing.Optional[builtins.str]:
            '''The output format: ``SequenceFileOutputFormat`` (binary), or ``IgnoreKeyTextOutputFormat`` , or a custom format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-storagedescriptor.html#cfn-glue-table-storagedescriptor-outputformat
            '''
            result = self._values.get("output_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parameters(self) -> typing.Any:
            '''The user-supplied properties in key-value form.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-storagedescriptor.html#cfn-glue-table-storagedescriptor-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Any, result)

        @builtins.property
        def schema_reference(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTable.SchemaReferenceProperty"]]:
            '''An object that references a schema stored in the AWS Glue Schema Registry.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-storagedescriptor.html#cfn-glue-table-storagedescriptor-schemareference
            '''
            result = self._values.get("schema_reference")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTable.SchemaReferenceProperty"]], result)

        @builtins.property
        def serde_info(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTable.SerdeInfoProperty"]]:
            '''The serialization/deserialization (SerDe) information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-storagedescriptor.html#cfn-glue-table-storagedescriptor-serdeinfo
            '''
            result = self._values.get("serde_info")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTable.SerdeInfoProperty"]], result)

        @builtins.property
        def skewed_info(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTable.SkewedInfoProperty"]]:
            '''The information about values that appear frequently in a column (skewed values).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-storagedescriptor.html#cfn-glue-table-storagedescriptor-skewedinfo
            '''
            result = self._values.get("skewed_info")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTable.SkewedInfoProperty"]], result)

        @builtins.property
        def sort_columns(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTable.OrderProperty"]]]]:
            '''A list specifying the sort order of each bucket in the table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-storagedescriptor.html#cfn-glue-table-storagedescriptor-sortcolumns
            '''
            result = self._values.get("sort_columns")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTable.OrderProperty"]]]], result)

        @builtins.property
        def stored_as_sub_directories(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''``True`` if the table data is stored in subdirectories, or ``False`` if not.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-storagedescriptor.html#cfn-glue-table-storagedescriptor-storedassubdirectories
            '''
            result = self._values.get("stored_as_sub_directories")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StorageDescriptorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnTable.TableIdentifierProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "database_name": "databaseName",
            "name": "name",
        },
    )
    class TableIdentifierProperty:
        def __init__(
            self,
            *,
            catalog_id: typing.Optional[builtins.str] = None,
            database_name: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A structure that describes a target table for resource linking.

            :param catalog_id: The ID of the Data Catalog in which the table resides.
            :param database_name: The name of the catalog database that contains the target table.
            :param name: The name of the target table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableidentifier.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                table_identifier_property = glue.CfnTable.TableIdentifierProperty(
                    catalog_id="catalogId",
                    database_name="databaseName",
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cd9fe33086eb487e31769dc922bd060b39cb7e1a4f01a8e8bfa04311b57918e5)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if catalog_id is not None:
                self._values["catalog_id"] = catalog_id
            if database_name is not None:
                self._values["database_name"] = database_name
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def catalog_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the Data Catalog in which the table resides.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableidentifier.html#cfn-glue-table-tableidentifier-catalogid
            '''
            result = self._values.get("catalog_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def database_name(self) -> typing.Optional[builtins.str]:
            '''The name of the catalog database that contains the target table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableidentifier.html#cfn-glue-table-tableidentifier-databasename
            '''
            result = self._values.get("database_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the target table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableidentifier.html#cfn-glue-table-tableidentifier-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TableIdentifierProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnTable.TableInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "description": "description",
            "name": "name",
            "owner": "owner",
            "parameters": "parameters",
            "partition_keys": "partitionKeys",
            "retention": "retention",
            "storage_descriptor": "storageDescriptor",
            "table_type": "tableType",
            "target_table": "targetTable",
            "view_expanded_text": "viewExpandedText",
            "view_original_text": "viewOriginalText",
        },
    )
    class TableInputProperty:
        def __init__(
            self,
            *,
            description: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            owner: typing.Optional[builtins.str] = None,
            parameters: typing.Any = None,
            partition_keys: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTable.ColumnProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            retention: typing.Optional[jsii.Number] = None,
            storage_descriptor: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTable.StorageDescriptorProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            table_type: typing.Optional[builtins.str] = None,
            target_table: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTable.TableIdentifierProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            view_expanded_text: typing.Optional[builtins.str] = None,
            view_original_text: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A structure used to define a table.

            :param description: A description of the table.
            :param name: The table name. For Hive compatibility, this is folded to lowercase when it is stored.
            :param owner: The table owner. Included for Apache Hive compatibility. Not used in the normal course of AWS Glue operations.
            :param parameters: These key-value pairs define properties associated with the table.
            :param partition_keys: A list of columns by which the table is partitioned. Only primitive types are supported as partition keys. When you create a table used by Amazon Athena, and you do not specify any ``partitionKeys`` , you must at least set the value of ``partitionKeys`` to an empty list. For example: ``"PartitionKeys": []``
            :param retention: The retention time for this table.
            :param storage_descriptor: A storage descriptor containing information about the physical storage of this table.
            :param table_type: The type of this table. AWS Glue will create tables with the ``EXTERNAL_TABLE`` type. Other services, such as Athena, may create tables with additional table types. AWS Glue related table types: - **EXTERNAL_TABLE** - Hive compatible attribute - indicates a non-Hive managed table. - **GOVERNED** - Used by AWS Lake Formation . The AWS Glue Data Catalog understands ``GOVERNED`` .
            :param target_table: A ``TableIdentifier`` structure that describes a target table for resource linking.
            :param view_expanded_text: Included for Apache Hive compatibility. Not used in the normal course of AWS Glue operations.
            :param view_original_text: Included for Apache Hive compatibility. Not used in the normal course of AWS Glue operations. If the table is a ``VIRTUAL_VIEW`` , certain Athena configuration encoded in base64.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                # parameters: Any
                # skewed_column_value_location_maps: Any
                
                table_input_property = glue.CfnTable.TableInputProperty(
                    description="description",
                    name="name",
                    owner="owner",
                    parameters=parameters,
                    partition_keys=[glue.CfnTable.ColumnProperty(
                        name="name",
                
                        # the properties below are optional
                        comment="comment",
                        type="type"
                    )],
                    retention=123,
                    storage_descriptor=glue.CfnTable.StorageDescriptorProperty(
                        bucket_columns=["bucketColumns"],
                        columns=[glue.CfnTable.ColumnProperty(
                            name="name",
                
                            # the properties below are optional
                            comment="comment",
                            type="type"
                        )],
                        compressed=False,
                        input_format="inputFormat",
                        location="location",
                        number_of_buckets=123,
                        output_format="outputFormat",
                        parameters=parameters,
                        schema_reference=glue.CfnTable.SchemaReferenceProperty(
                            schema_id=glue.CfnTable.SchemaIdProperty(
                                registry_name="registryName",
                                schema_arn="schemaArn",
                                schema_name="schemaName"
                            ),
                            schema_version_id="schemaVersionId",
                            schema_version_number=123
                        ),
                        serde_info=glue.CfnTable.SerdeInfoProperty(
                            name="name",
                            parameters=parameters,
                            serialization_library="serializationLibrary"
                        ),
                        skewed_info=glue.CfnTable.SkewedInfoProperty(
                            skewed_column_names=["skewedColumnNames"],
                            skewed_column_value_location_maps=skewed_column_value_location_maps,
                            skewed_column_values=["skewedColumnValues"]
                        ),
                        sort_columns=[glue.CfnTable.OrderProperty(
                            column="column",
                            sort_order=123
                        )],
                        stored_as_sub_directories=False
                    ),
                    table_type="tableType",
                    target_table=glue.CfnTable.TableIdentifierProperty(
                        catalog_id="catalogId",
                        database_name="databaseName",
                        name="name"
                    ),
                    view_expanded_text="viewExpandedText",
                    view_original_text="viewOriginalText"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2cd7cfcabe0becfeb1771268e35d45d44b6f88db622d180509f833411ccf0096)
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument owner", value=owner, expected_type=type_hints["owner"])
                check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
                check_type(argname="argument partition_keys", value=partition_keys, expected_type=type_hints["partition_keys"])
                check_type(argname="argument retention", value=retention, expected_type=type_hints["retention"])
                check_type(argname="argument storage_descriptor", value=storage_descriptor, expected_type=type_hints["storage_descriptor"])
                check_type(argname="argument table_type", value=table_type, expected_type=type_hints["table_type"])
                check_type(argname="argument target_table", value=target_table, expected_type=type_hints["target_table"])
                check_type(argname="argument view_expanded_text", value=view_expanded_text, expected_type=type_hints["view_expanded_text"])
                check_type(argname="argument view_original_text", value=view_original_text, expected_type=type_hints["view_original_text"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if description is not None:
                self._values["description"] = description
            if name is not None:
                self._values["name"] = name
            if owner is not None:
                self._values["owner"] = owner
            if parameters is not None:
                self._values["parameters"] = parameters
            if partition_keys is not None:
                self._values["partition_keys"] = partition_keys
            if retention is not None:
                self._values["retention"] = retention
            if storage_descriptor is not None:
                self._values["storage_descriptor"] = storage_descriptor
            if table_type is not None:
                self._values["table_type"] = table_type
            if target_table is not None:
                self._values["target_table"] = target_table
            if view_expanded_text is not None:
                self._values["view_expanded_text"] = view_expanded_text
            if view_original_text is not None:
                self._values["view_original_text"] = view_original_text

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''A description of the table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.html#cfn-glue-table-tableinput-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The table name.

            For Hive compatibility, this is folded to lowercase when it is stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.html#cfn-glue-table-tableinput-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def owner(self) -> typing.Optional[builtins.str]:
            '''The table owner.

            Included for Apache Hive compatibility. Not used in the normal course of AWS Glue operations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.html#cfn-glue-table-tableinput-owner
            '''
            result = self._values.get("owner")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parameters(self) -> typing.Any:
            '''These key-value pairs define properties associated with the table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.html#cfn-glue-table-tableinput-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Any, result)

        @builtins.property
        def partition_keys(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTable.ColumnProperty"]]]]:
            '''A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.

            When you create a table used by Amazon Athena, and you do not specify any ``partitionKeys`` , you must at least set the value of ``partitionKeys`` to an empty list. For example:

            ``"PartitionKeys": []``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.html#cfn-glue-table-tableinput-partitionkeys
            '''
            result = self._values.get("partition_keys")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTable.ColumnProperty"]]]], result)

        @builtins.property
        def retention(self) -> typing.Optional[jsii.Number]:
            '''The retention time for this table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.html#cfn-glue-table-tableinput-retention
            '''
            result = self._values.get("retention")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def storage_descriptor(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTable.StorageDescriptorProperty"]]:
            '''A storage descriptor containing information about the physical storage of this table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.html#cfn-glue-table-tableinput-storagedescriptor
            '''
            result = self._values.get("storage_descriptor")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTable.StorageDescriptorProperty"]], result)

        @builtins.property
        def table_type(self) -> typing.Optional[builtins.str]:
            '''The type of this table.

            AWS Glue will create tables with the ``EXTERNAL_TABLE`` type. Other services, such as Athena, may create tables with additional table types.

            AWS Glue related table types:

            - **EXTERNAL_TABLE** - Hive compatible attribute - indicates a non-Hive managed table.
            - **GOVERNED** - Used by AWS Lake Formation . The AWS Glue Data Catalog understands ``GOVERNED`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.html#cfn-glue-table-tableinput-tabletype
            '''
            result = self._values.get("table_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_table(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTable.TableIdentifierProperty"]]:
            '''A ``TableIdentifier`` structure that describes a target table for resource linking.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.html#cfn-glue-table-tableinput-targettable
            '''
            result = self._values.get("target_table")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTable.TableIdentifierProperty"]], result)

        @builtins.property
        def view_expanded_text(self) -> typing.Optional[builtins.str]:
            '''Included for Apache Hive compatibility.

            Not used in the normal course of AWS Glue operations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.html#cfn-glue-table-tableinput-viewexpandedtext
            '''
            result = self._values.get("view_expanded_text")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def view_original_text(self) -> typing.Optional[builtins.str]:
            '''Included for Apache Hive compatibility.

            Not used in the normal course of AWS Glue operations. If the table is a ``VIRTUAL_VIEW`` , certain Athena configuration encoded in base64.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.html#cfn-glue-table-tableinput-vieworiginaltext
            '''
            result = self._values.get("view_original_text")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TableInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_glue.CfnTableProps",
    jsii_struct_bases=[],
    name_mapping={
        "catalog_id": "catalogId",
        "database_name": "databaseName",
        "table_input": "tableInput",
    },
)
class CfnTableProps:
    def __init__(
        self,
        *,
        catalog_id: builtins.str,
        database_name: builtins.str,
        table_input: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.TableInputProperty, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Properties for defining a ``CfnTable``.

        :param catalog_id: The ID of the Data Catalog in which to create the ``Table`` .
        :param database_name: The name of the database where the table metadata resides. For Hive compatibility, this must be all lowercase.
        :param table_input: A structure used to define a table.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-table.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_glue as glue
            
            # parameters: Any
            # skewed_column_value_location_maps: Any
            
            cfn_table_props = glue.CfnTableProps(
                catalog_id="catalogId",
                database_name="databaseName",
                table_input=glue.CfnTable.TableInputProperty(
                    description="description",
                    name="name",
                    owner="owner",
                    parameters=parameters,
                    partition_keys=[glue.CfnTable.ColumnProperty(
                        name="name",
            
                        # the properties below are optional
                        comment="comment",
                        type="type"
                    )],
                    retention=123,
                    storage_descriptor=glue.CfnTable.StorageDescriptorProperty(
                        bucket_columns=["bucketColumns"],
                        columns=[glue.CfnTable.ColumnProperty(
                            name="name",
            
                            # the properties below are optional
                            comment="comment",
                            type="type"
                        )],
                        compressed=False,
                        input_format="inputFormat",
                        location="location",
                        number_of_buckets=123,
                        output_format="outputFormat",
                        parameters=parameters,
                        schema_reference=glue.CfnTable.SchemaReferenceProperty(
                            schema_id=glue.CfnTable.SchemaIdProperty(
                                registry_name="registryName",
                                schema_arn="schemaArn",
                                schema_name="schemaName"
                            ),
                            schema_version_id="schemaVersionId",
                            schema_version_number=123
                        ),
                        serde_info=glue.CfnTable.SerdeInfoProperty(
                            name="name",
                            parameters=parameters,
                            serialization_library="serializationLibrary"
                        ),
                        skewed_info=glue.CfnTable.SkewedInfoProperty(
                            skewed_column_names=["skewedColumnNames"],
                            skewed_column_value_location_maps=skewed_column_value_location_maps,
                            skewed_column_values=["skewedColumnValues"]
                        ),
                        sort_columns=[glue.CfnTable.OrderProperty(
                            column="column",
                            sort_order=123
                        )],
                        stored_as_sub_directories=False
                    ),
                    table_type="tableType",
                    target_table=glue.CfnTable.TableIdentifierProperty(
                        catalog_id="catalogId",
                        database_name="databaseName",
                        name="name"
                    ),
                    view_expanded_text="viewExpandedText",
                    view_original_text="viewOriginalText"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fa7a95b739eec87307cf104cf3e05eef39d32fd60cc53851b43bd980ef557e0)
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument table_input", value=table_input, expected_type=type_hints["table_input"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "catalog_id": catalog_id,
            "database_name": database_name,
            "table_input": table_input,
        }

    @builtins.property
    def catalog_id(self) -> builtins.str:
        '''The ID of the Data Catalog in which to create the ``Table`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-table.html#cfn-glue-table-catalogid
        '''
        result = self._values.get("catalog_id")
        assert result is not None, "Required property 'catalog_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def database_name(self) -> builtins.str:
        '''The name of the database where the table metadata resides.

        For Hive compatibility, this must be all lowercase.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-table.html#cfn-glue-table-databasename
        '''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_input(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnTable.TableInputProperty]:
        '''A structure used to define a table.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-table.html#cfn-glue-table-tableinput
        '''
        result = self._values.get("table_input")
        assert result is not None, "Required property 'table_input' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnTable.TableInputProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTableProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnTrigger(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_glue.CfnTrigger",
):
    '''The ``AWS::Glue::Trigger`` resource specifies triggers that run AWS Glue jobs.

    For more information, see `Triggering Jobs in AWS Glue <https://docs.aws.amazon.com/glue/latest/dg/trigger-job.html>`_ and `Trigger Structure <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-trigger.html#aws-glue-api-jobs-trigger-Trigger>`_ in the *AWS Glue Developer Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-trigger.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_glue as glue
        
        # arguments_: Any
        # tags: Any
        
        cfn_trigger = glue.CfnTrigger(self, "MyCfnTrigger",
            actions=[glue.CfnTrigger.ActionProperty(
                arguments=arguments_,
                crawler_name="crawlerName",
                job_name="jobName",
                notification_property=glue.CfnTrigger.NotificationPropertyProperty(
                    notify_delay_after=123
                ),
                security_configuration="securityConfiguration",
                timeout=123
            )],
            type="type",
        
            # the properties below are optional
            description="description",
            event_batching_condition=glue.CfnTrigger.EventBatchingConditionProperty(
                batch_size=123,
        
                # the properties below are optional
                batch_window=123
            ),
            name="name",
            predicate=glue.CfnTrigger.PredicateProperty(
                conditions=[glue.CfnTrigger.ConditionProperty(
                    crawler_name="crawlerName",
                    crawl_state="crawlState",
                    job_name="jobName",
                    logical_operator="logicalOperator",
                    state="state"
                )],
                logical="logical"
            ),
            schedule="schedule",
            start_on_creation=False,
            tags=tags,
            workflow_name="workflowName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        actions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTrigger.ActionProperty", typing.Dict[builtins.str, typing.Any]]]]],
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        event_batching_condition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTrigger.EventBatchingConditionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        predicate: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTrigger.PredicateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        schedule: typing.Optional[builtins.str] = None,
        start_on_creation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        tags: typing.Any = None,
        workflow_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param actions: The actions initiated by this trigger.
        :param type: The type of trigger that this is.
        :param description: A description of this trigger.
        :param event_batching_condition: Batch condition that must be met (specified number of events received or batch time window expired) before EventBridge event trigger fires.
        :param name: The name of the trigger.
        :param predicate: The predicate of this trigger, which defines when it will fire.
        :param schedule: A ``cron`` expression used to specify the schedule. For more information, see `Time-Based Schedules for Jobs and Crawlers <https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`_ in the *AWS Glue Developer Guide* . For example, to run something every day at 12:15 UTC, specify ``cron(15 12 * * ? *)`` .
        :param start_on_creation: Set to true to start ``SCHEDULED`` and ``CONDITIONAL`` triggers when created. True is not supported for ``ON_DEMAND`` triggers.
        :param tags: The tags to use with this trigger.
        :param workflow_name: The name of the workflow associated with the trigger.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8db15edfea6b1fa74e017c6bb7603bed442e4f78f4c3c138f4dcc562cc8030ae)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTriggerProps(
            actions=actions,
            type=type,
            description=description,
            event_batching_condition=event_batching_condition,
            name=name,
            predicate=predicate,
            schedule=schedule,
            start_on_creation=start_on_creation,
            tags=tags,
            workflow_name=workflow_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0eaa05c4b1b14e1818059890f7eb0ac7a86490e54a9132ffd1b4d9178ea5d849)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7feee79b38582fea07a55bfd3425e4cc1f74b6e95e460a2a3f07af8648b09408)
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
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="actions")
    def actions(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTrigger.ActionProperty"]]]:
        '''The actions initiated by this trigger.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTrigger.ActionProperty"]]], jsii.get(self, "actions"))

    @actions.setter
    def actions(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTrigger.ActionProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53d40032b3434d3f5e99c83dacf150ee68e626c8b767443757082d57b51f20e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actions", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of trigger that this is.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c40487beec9ee28746c40fb85d90ed73d85349d2b1310591566c8a389d11491)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of this trigger.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a076c3439af46ca0fd80eee9d6b5b51664f94b7328360e3909babe56dec9a68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="eventBatchingCondition")
    def event_batching_condition(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTrigger.EventBatchingConditionProperty"]]:
        '''Batch condition that must be met (specified number of events received or batch time window expired) before EventBridge event trigger fires.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTrigger.EventBatchingConditionProperty"]], jsii.get(self, "eventBatchingCondition"))

    @event_batching_condition.setter
    def event_batching_condition(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTrigger.EventBatchingConditionProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__194582de5e8e5febbe9a4cbc4a1e55c5a1e16e7befac99be36a1217527cc1b08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventBatchingCondition", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the trigger.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c195c948ebb78674c5a524b87ee0245a04d0f596e0a692d1eb19ef4e9c11d00a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="predicate")
    def predicate(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTrigger.PredicateProperty"]]:
        '''The predicate of this trigger, which defines when it will fire.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTrigger.PredicateProperty"]], jsii.get(self, "predicate"))

    @predicate.setter
    def predicate(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTrigger.PredicateProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89999604a37adfda2b629e7c87daa4774ff7b411d1a7dd82765ddaea3e8db560)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "predicate", value)

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> typing.Optional[builtins.str]:
        '''A ``cron`` expression used to specify the schedule.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__619711c62d98e25126265055c5714cbf3e2603579cec35909c8ddac5c1ec55f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedule", value)

    @builtins.property
    @jsii.member(jsii_name="startOnCreation")
    def start_on_creation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Set to true to start ``SCHEDULED`` and ``CONDITIONAL`` triggers when created.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "startOnCreation"))

    @start_on_creation.setter
    def start_on_creation(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68315158d369a16e86c793787be78f9303c715936ab11872da4b50150509337c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startOnCreation", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Any:
        '''The tags to use with this trigger.'''
        return typing.cast(typing.Any, jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b0b45c89e6532f144a9dfed7dc674b60a42cbe0a87f33d0c9422d7ae3603da7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="workflowName")
    def workflow_name(self) -> typing.Optional[builtins.str]:
        '''The name of the workflow associated with the trigger.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workflowName"))

    @workflow_name.setter
    def workflow_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf30f6c51932d46e70bffc0458c6c0fb8cb8525d3df1b7d576068ebaddc0e640)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workflowName", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnTrigger.ActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arguments": "arguments",
            "crawler_name": "crawlerName",
            "job_name": "jobName",
            "notification_property": "notificationProperty",
            "security_configuration": "securityConfiguration",
            "timeout": "timeout",
        },
    )
    class ActionProperty:
        def __init__(
            self,
            *,
            arguments: typing.Any = None,
            crawler_name: typing.Optional[builtins.str] = None,
            job_name: typing.Optional[builtins.str] = None,
            notification_property: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTrigger.NotificationPropertyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            security_configuration: typing.Optional[builtins.str] = None,
            timeout: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Defines an action to be initiated by a trigger.

            :param arguments: The job arguments used when this trigger fires. For this job run, they replace the default arguments set in the job definition itself. You can specify arguments here that your own job-execution script consumes, in addition to arguments that AWS Glue itself consumes. For information about how to specify and consume your own job arguments, see `Calling AWS Glue APIs in Python <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`_ in the *AWS Glue Developer Guide* . For information about the key-value pairs that AWS Glue consumes to set up your job, see the `Special Parameters Used by AWS Glue <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`_ topic in the developer guide.
            :param crawler_name: The name of the crawler to be used with this action.
            :param job_name: The name of a job to be executed.
            :param notification_property: Specifies configuration properties of a job run notification.
            :param security_configuration: The name of the ``SecurityConfiguration`` structure to be used with this action.
            :param timeout: The ``JobRun`` timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours). This overrides the timeout value set in the parent job.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-action.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                # arguments_: Any
                
                action_property = glue.CfnTrigger.ActionProperty(
                    arguments=arguments_,
                    crawler_name="crawlerName",
                    job_name="jobName",
                    notification_property=glue.CfnTrigger.NotificationPropertyProperty(
                        notify_delay_after=123
                    ),
                    security_configuration="securityConfiguration",
                    timeout=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__447a682fdfeec31ab40716697e095ee0c352e04c8ce1613acdeea726195c5ddf)
                check_type(argname="argument arguments", value=arguments, expected_type=type_hints["arguments"])
                check_type(argname="argument crawler_name", value=crawler_name, expected_type=type_hints["crawler_name"])
                check_type(argname="argument job_name", value=job_name, expected_type=type_hints["job_name"])
                check_type(argname="argument notification_property", value=notification_property, expected_type=type_hints["notification_property"])
                check_type(argname="argument security_configuration", value=security_configuration, expected_type=type_hints["security_configuration"])
                check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if arguments is not None:
                self._values["arguments"] = arguments
            if crawler_name is not None:
                self._values["crawler_name"] = crawler_name
            if job_name is not None:
                self._values["job_name"] = job_name
            if notification_property is not None:
                self._values["notification_property"] = notification_property
            if security_configuration is not None:
                self._values["security_configuration"] = security_configuration
            if timeout is not None:
                self._values["timeout"] = timeout

        @builtins.property
        def arguments(self) -> typing.Any:
            '''The job arguments used when this trigger fires.

            For this job run, they replace the default arguments set in the job definition itself.

            You can specify arguments here that your own job-execution script consumes, in addition to arguments that AWS Glue itself consumes.

            For information about how to specify and consume your own job arguments, see `Calling AWS Glue APIs in Python <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`_ in the *AWS Glue Developer Guide* .

            For information about the key-value pairs that AWS Glue consumes to set up your job, see the `Special Parameters Used by AWS Glue <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`_ topic in the developer guide.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-action.html#cfn-glue-trigger-action-arguments
            '''
            result = self._values.get("arguments")
            return typing.cast(typing.Any, result)

        @builtins.property
        def crawler_name(self) -> typing.Optional[builtins.str]:
            '''The name of the crawler to be used with this action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-action.html#cfn-glue-trigger-action-crawlername
            '''
            result = self._values.get("crawler_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def job_name(self) -> typing.Optional[builtins.str]:
            '''The name of a job to be executed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-action.html#cfn-glue-trigger-action-jobname
            '''
            result = self._values.get("job_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def notification_property(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTrigger.NotificationPropertyProperty"]]:
            '''Specifies configuration properties of a job run notification.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-action.html#cfn-glue-trigger-action-notificationproperty
            '''
            result = self._values.get("notification_property")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTrigger.NotificationPropertyProperty"]], result)

        @builtins.property
        def security_configuration(self) -> typing.Optional[builtins.str]:
            '''The name of the ``SecurityConfiguration`` structure to be used with this action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-action.html#cfn-glue-trigger-action-securityconfiguration
            '''
            result = self._values.get("security_configuration")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timeout(self) -> typing.Optional[jsii.Number]:
            '''The ``JobRun`` timeout in minutes.

            This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours). This overrides the timeout value set in the parent job.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-action.html#cfn-glue-trigger-action-timeout
            '''
            result = self._values.get("timeout")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnTrigger.ConditionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "crawler_name": "crawlerName",
            "crawl_state": "crawlState",
            "job_name": "jobName",
            "logical_operator": "logicalOperator",
            "state": "state",
        },
    )
    class ConditionProperty:
        def __init__(
            self,
            *,
            crawler_name: typing.Optional[builtins.str] = None,
            crawl_state: typing.Optional[builtins.str] = None,
            job_name: typing.Optional[builtins.str] = None,
            logical_operator: typing.Optional[builtins.str] = None,
            state: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines a condition under which a trigger fires.

            :param crawler_name: The name of the crawler to which this condition applies.
            :param crawl_state: The state of the crawler to which this condition applies.
            :param job_name: The name of the job whose ``JobRuns`` this condition applies to, and on which this trigger waits.
            :param logical_operator: A logical operator.
            :param state: The condition state. Currently, the values supported are ``SUCCEEDED`` , ``STOPPED`` , ``TIMEOUT`` , and ``FAILED`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-condition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                condition_property = glue.CfnTrigger.ConditionProperty(
                    crawler_name="crawlerName",
                    crawl_state="crawlState",
                    job_name="jobName",
                    logical_operator="logicalOperator",
                    state="state"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ada6798ea699e13790200a1ce7e2ca63bd7eb26d5c745fb9ad03c6a5fe653c70)
                check_type(argname="argument crawler_name", value=crawler_name, expected_type=type_hints["crawler_name"])
                check_type(argname="argument crawl_state", value=crawl_state, expected_type=type_hints["crawl_state"])
                check_type(argname="argument job_name", value=job_name, expected_type=type_hints["job_name"])
                check_type(argname="argument logical_operator", value=logical_operator, expected_type=type_hints["logical_operator"])
                check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if crawler_name is not None:
                self._values["crawler_name"] = crawler_name
            if crawl_state is not None:
                self._values["crawl_state"] = crawl_state
            if job_name is not None:
                self._values["job_name"] = job_name
            if logical_operator is not None:
                self._values["logical_operator"] = logical_operator
            if state is not None:
                self._values["state"] = state

        @builtins.property
        def crawler_name(self) -> typing.Optional[builtins.str]:
            '''The name of the crawler to which this condition applies.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-condition.html#cfn-glue-trigger-condition-crawlername
            '''
            result = self._values.get("crawler_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def crawl_state(self) -> typing.Optional[builtins.str]:
            '''The state of the crawler to which this condition applies.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-condition.html#cfn-glue-trigger-condition-crawlstate
            '''
            result = self._values.get("crawl_state")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def job_name(self) -> typing.Optional[builtins.str]:
            '''The name of the job whose ``JobRuns`` this condition applies to, and on which this trigger waits.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-condition.html#cfn-glue-trigger-condition-jobname
            '''
            result = self._values.get("job_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def logical_operator(self) -> typing.Optional[builtins.str]:
            '''A logical operator.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-condition.html#cfn-glue-trigger-condition-logicaloperator
            '''
            result = self._values.get("logical_operator")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def state(self) -> typing.Optional[builtins.str]:
            '''The condition state.

            Currently, the values supported are ``SUCCEEDED`` , ``STOPPED`` , ``TIMEOUT`` , and ``FAILED`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-condition.html#cfn-glue-trigger-condition-state
            '''
            result = self._values.get("state")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnTrigger.EventBatchingConditionProperty",
        jsii_struct_bases=[],
        name_mapping={"batch_size": "batchSize", "batch_window": "batchWindow"},
    )
    class EventBatchingConditionProperty:
        def __init__(
            self,
            *,
            batch_size: jsii.Number,
            batch_window: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Batch condition that must be met (specified number of events received or batch time window expired) before EventBridge event trigger fires.

            :param batch_size: Number of events that must be received from Amazon EventBridge before EventBridge event trigger fires.
            :param batch_window: Window of time in seconds after which EventBridge event trigger fires. Window starts when first event is received.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-eventbatchingcondition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                event_batching_condition_property = glue.CfnTrigger.EventBatchingConditionProperty(
                    batch_size=123,
                
                    # the properties below are optional
                    batch_window=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ace5e9c479229705a32735a5104d72eb05ba1dc95f28ce3ecae1b4f0d5591681)
                check_type(argname="argument batch_size", value=batch_size, expected_type=type_hints["batch_size"])
                check_type(argname="argument batch_window", value=batch_window, expected_type=type_hints["batch_window"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "batch_size": batch_size,
            }
            if batch_window is not None:
                self._values["batch_window"] = batch_window

        @builtins.property
        def batch_size(self) -> jsii.Number:
            '''Number of events that must be received from Amazon EventBridge before EventBridge event trigger fires.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-eventbatchingcondition.html#cfn-glue-trigger-eventbatchingcondition-batchsize
            '''
            result = self._values.get("batch_size")
            assert result is not None, "Required property 'batch_size' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def batch_window(self) -> typing.Optional[jsii.Number]:
            '''Window of time in seconds after which EventBridge event trigger fires.

            Window starts when first event is received.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-eventbatchingcondition.html#cfn-glue-trigger-eventbatchingcondition-batchwindow
            '''
            result = self._values.get("batch_window")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventBatchingConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnTrigger.NotificationPropertyProperty",
        jsii_struct_bases=[],
        name_mapping={"notify_delay_after": "notifyDelayAfter"},
    )
    class NotificationPropertyProperty:
        def __init__(
            self,
            *,
            notify_delay_after: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Specifies configuration properties of a job run notification.

            :param notify_delay_after: After a job run starts, the number of minutes to wait before sending a job run delay notification.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-notificationproperty.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                notification_property_property = glue.CfnTrigger.NotificationPropertyProperty(
                    notify_delay_after=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9dba53ce68e34fb74bdafe21cd27a275d4fc3658f9a966098739aadba8f14d8a)
                check_type(argname="argument notify_delay_after", value=notify_delay_after, expected_type=type_hints["notify_delay_after"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if notify_delay_after is not None:
                self._values["notify_delay_after"] = notify_delay_after

        @builtins.property
        def notify_delay_after(self) -> typing.Optional[jsii.Number]:
            '''After a job run starts, the number of minutes to wait before sending a job run delay notification.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-notificationproperty.html#cfn-glue-trigger-notificationproperty-notifydelayafter
            '''
            result = self._values.get("notify_delay_after")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NotificationPropertyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_glue.CfnTrigger.PredicateProperty",
        jsii_struct_bases=[],
        name_mapping={"conditions": "conditions", "logical": "logical"},
    )
    class PredicateProperty:
        def __init__(
            self,
            *,
            conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTrigger.ConditionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            logical: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines the predicate of the trigger, which determines when it fires.

            :param conditions: A list of the conditions that determine when the trigger will fire.
            :param logical: An optional field if only one condition is listed. If multiple conditions are listed, then this field is required.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-predicate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_glue as glue
                
                predicate_property = glue.CfnTrigger.PredicateProperty(
                    conditions=[glue.CfnTrigger.ConditionProperty(
                        crawler_name="crawlerName",
                        crawl_state="crawlState",
                        job_name="jobName",
                        logical_operator="logicalOperator",
                        state="state"
                    )],
                    logical="logical"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a59467c007dcc8cafa31e77259eebd72b608f9b3a0d7bb269217aba9a34fdcd8)
                check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
                check_type(argname="argument logical", value=logical, expected_type=type_hints["logical"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if conditions is not None:
                self._values["conditions"] = conditions
            if logical is not None:
                self._values["logical"] = logical

        @builtins.property
        def conditions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTrigger.ConditionProperty"]]]]:
            '''A list of the conditions that determine when the trigger will fire.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-predicate.html#cfn-glue-trigger-predicate-conditions
            '''
            result = self._values.get("conditions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTrigger.ConditionProperty"]]]], result)

        @builtins.property
        def logical(self) -> typing.Optional[builtins.str]:
            '''An optional field if only one condition is listed.

            If multiple conditions are listed, then this field is required.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-predicate.html#cfn-glue-trigger-predicate-logical
            '''
            result = self._values.get("logical")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PredicateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_glue.CfnTriggerProps",
    jsii_struct_bases=[],
    name_mapping={
        "actions": "actions",
        "type": "type",
        "description": "description",
        "event_batching_condition": "eventBatchingCondition",
        "name": "name",
        "predicate": "predicate",
        "schedule": "schedule",
        "start_on_creation": "startOnCreation",
        "tags": "tags",
        "workflow_name": "workflowName",
    },
)
class CfnTriggerProps:
    def __init__(
        self,
        *,
        actions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrigger.ActionProperty, typing.Dict[builtins.str, typing.Any]]]]],
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        event_batching_condition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrigger.EventBatchingConditionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        predicate: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrigger.PredicateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        schedule: typing.Optional[builtins.str] = None,
        start_on_creation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        tags: typing.Any = None,
        workflow_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnTrigger``.

        :param actions: The actions initiated by this trigger.
        :param type: The type of trigger that this is.
        :param description: A description of this trigger.
        :param event_batching_condition: Batch condition that must be met (specified number of events received or batch time window expired) before EventBridge event trigger fires.
        :param name: The name of the trigger.
        :param predicate: The predicate of this trigger, which defines when it will fire.
        :param schedule: A ``cron`` expression used to specify the schedule. For more information, see `Time-Based Schedules for Jobs and Crawlers <https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`_ in the *AWS Glue Developer Guide* . For example, to run something every day at 12:15 UTC, specify ``cron(15 12 * * ? *)`` .
        :param start_on_creation: Set to true to start ``SCHEDULED`` and ``CONDITIONAL`` triggers when created. True is not supported for ``ON_DEMAND`` triggers.
        :param tags: The tags to use with this trigger.
        :param workflow_name: The name of the workflow associated with the trigger.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-trigger.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_glue as glue
            
            # arguments_: Any
            # tags: Any
            
            cfn_trigger_props = glue.CfnTriggerProps(
                actions=[glue.CfnTrigger.ActionProperty(
                    arguments=arguments_,
                    crawler_name="crawlerName",
                    job_name="jobName",
                    notification_property=glue.CfnTrigger.NotificationPropertyProperty(
                        notify_delay_after=123
                    ),
                    security_configuration="securityConfiguration",
                    timeout=123
                )],
                type="type",
            
                # the properties below are optional
                description="description",
                event_batching_condition=glue.CfnTrigger.EventBatchingConditionProperty(
                    batch_size=123,
            
                    # the properties below are optional
                    batch_window=123
                ),
                name="name",
                predicate=glue.CfnTrigger.PredicateProperty(
                    conditions=[glue.CfnTrigger.ConditionProperty(
                        crawler_name="crawlerName",
                        crawl_state="crawlState",
                        job_name="jobName",
                        logical_operator="logicalOperator",
                        state="state"
                    )],
                    logical="logical"
                ),
                schedule="schedule",
                start_on_creation=False,
                tags=tags,
                workflow_name="workflowName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__784653657e04e37fef0f1a1cad2dd3968ecec5929ea90e9d792e16ce48fec46e)
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument event_batching_condition", value=event_batching_condition, expected_type=type_hints["event_batching_condition"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument predicate", value=predicate, expected_type=type_hints["predicate"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument start_on_creation", value=start_on_creation, expected_type=type_hints["start_on_creation"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument workflow_name", value=workflow_name, expected_type=type_hints["workflow_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "actions": actions,
            "type": type,
        }
        if description is not None:
            self._values["description"] = description
        if event_batching_condition is not None:
            self._values["event_batching_condition"] = event_batching_condition
        if name is not None:
            self._values["name"] = name
        if predicate is not None:
            self._values["predicate"] = predicate
        if schedule is not None:
            self._values["schedule"] = schedule
        if start_on_creation is not None:
            self._values["start_on_creation"] = start_on_creation
        if tags is not None:
            self._values["tags"] = tags
        if workflow_name is not None:
            self._values["workflow_name"] = workflow_name

    @builtins.property
    def actions(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTrigger.ActionProperty]]]:
        '''The actions initiated by this trigger.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-trigger.html#cfn-glue-trigger-actions
        '''
        result = self._values.get("actions")
        assert result is not None, "Required property 'actions' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTrigger.ActionProperty]]], result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of trigger that this is.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-trigger.html#cfn-glue-trigger-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of this trigger.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-trigger.html#cfn-glue-trigger-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def event_batching_condition(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTrigger.EventBatchingConditionProperty]]:
        '''Batch condition that must be met (specified number of events received or batch time window expired) before EventBridge event trigger fires.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-trigger.html#cfn-glue-trigger-eventbatchingcondition
        '''
        result = self._values.get("event_batching_condition")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTrigger.EventBatchingConditionProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the trigger.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-trigger.html#cfn-glue-trigger-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def predicate(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTrigger.PredicateProperty]]:
        '''The predicate of this trigger, which defines when it will fire.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-trigger.html#cfn-glue-trigger-predicate
        '''
        result = self._values.get("predicate")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTrigger.PredicateProperty]], result)

    @builtins.property
    def schedule(self) -> typing.Optional[builtins.str]:
        '''A ``cron`` expression used to specify the schedule.

        For more information, see `Time-Based Schedules for Jobs and Crawlers <https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`_ in the *AWS Glue Developer Guide* . For example, to run something every day at 12:15 UTC, specify ``cron(15 12 * * ? *)`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-trigger.html#cfn-glue-trigger-schedule
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_on_creation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Set to true to start ``SCHEDULED`` and ``CONDITIONAL`` triggers when created.

        True is not supported for ``ON_DEMAND`` triggers.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-trigger.html#cfn-glue-trigger-startoncreation
        '''
        result = self._values.get("start_on_creation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''The tags to use with this trigger.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-trigger.html#cfn-glue-trigger-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    @builtins.property
    def workflow_name(self) -> typing.Optional[builtins.str]:
        '''The name of the workflow associated with the trigger.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-trigger.html#cfn-glue-trigger-workflowname
        '''
        result = self._values.get("workflow_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTriggerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnWorkflow(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_glue.CfnWorkflow",
):
    '''The ``AWS::Glue::Workflow`` is an AWS Glue resource type that manages AWS Glue workflows.

    A workflow is a container for a set of related jobs, crawlers, and triggers in AWS Glue . Using a workflow, you can design a complex multi-job extract, transform, and load (ETL) activity that AWS Glue can execute and track as single entity.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-workflow.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_glue as glue
        
        # default_run_properties: Any
        # tags: Any
        
        cfn_workflow = glue.CfnWorkflow(self, "MyCfnWorkflow",
            default_run_properties=default_run_properties,
            description="description",
            max_concurrent_runs=123,
            name="name",
            tags=tags
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        default_run_properties: typing.Any = None,
        description: typing.Optional[builtins.str] = None,
        max_concurrent_runs: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param default_run_properties: A collection of properties to be used as part of each execution of the workflow.
        :param description: A description of the workflow.
        :param max_concurrent_runs: You can use this parameter to prevent unwanted multiple updates to data, to control costs, or in some cases, to prevent exceeding the maximum number of concurrent runs of any of the component jobs. If you leave this parameter blank, there is no limit to the number of concurrent workflow runs.
        :param name: The name of the workflow representing the flow.
        :param tags: The tags to use with this workflow.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6c744c641379ecc5fd54ce4fcbe0501c332b7726b6037690528980d8b6c8f33)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnWorkflowProps(
            default_run_properties=default_run_properties,
            description=description,
            max_concurrent_runs=max_concurrent_runs,
            name=name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ccd23d031aa65b14694ae7bcf464a4c55d4ce28e67cc115e5a3a9b916b37323)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1bddbab3355f6eba94edc925da3c1a12b170435872bf1671a9d9951649478274)
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
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="defaultRunProperties")
    def default_run_properties(self) -> typing.Any:
        '''A collection of properties to be used as part of each execution of the workflow.'''
        return typing.cast(typing.Any, jsii.get(self, "defaultRunProperties"))

    @default_run_properties.setter
    def default_run_properties(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44dfd2cb43609bdf14cd367fdb19e4b1ca604d3264c983f445f606fe9e35818f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultRunProperties", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the workflow.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__111cdaa83ed7e77873f89337e876aecddb9e6d748ce7b22cd537261bb2c0040e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="maxConcurrentRuns")
    def max_concurrent_runs(self) -> typing.Optional[jsii.Number]:
        '''You can use this parameter to prevent unwanted multiple updates to data, to control costs, or in some cases, to prevent exceeding the maximum number of concurrent runs of any of the component jobs.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConcurrentRuns"))

    @max_concurrent_runs.setter
    def max_concurrent_runs(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41a06b4a8c873f8b95edfbe239c7699899e5c1a8a74755383d7c6c587b34c348)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConcurrentRuns", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the workflow representing the flow.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e19cad13834aa6cc47e532030a314d08f3c215dfcce008b2e0227db3d71718e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Any:
        '''The tags to use with this workflow.'''
        return typing.cast(typing.Any, jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__588bdefa1fb0e0005b05a203dd64a0a1b8395bced0853eefec4b1943820f9259)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_glue.CfnWorkflowProps",
    jsii_struct_bases=[],
    name_mapping={
        "default_run_properties": "defaultRunProperties",
        "description": "description",
        "max_concurrent_runs": "maxConcurrentRuns",
        "name": "name",
        "tags": "tags",
    },
)
class CfnWorkflowProps:
    def __init__(
        self,
        *,
        default_run_properties: typing.Any = None,
        description: typing.Optional[builtins.str] = None,
        max_concurrent_runs: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
    ) -> None:
        '''Properties for defining a ``CfnWorkflow``.

        :param default_run_properties: A collection of properties to be used as part of each execution of the workflow.
        :param description: A description of the workflow.
        :param max_concurrent_runs: You can use this parameter to prevent unwanted multiple updates to data, to control costs, or in some cases, to prevent exceeding the maximum number of concurrent runs of any of the component jobs. If you leave this parameter blank, there is no limit to the number of concurrent workflow runs.
        :param name: The name of the workflow representing the flow.
        :param tags: The tags to use with this workflow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-workflow.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_glue as glue
            
            # default_run_properties: Any
            # tags: Any
            
            cfn_workflow_props = glue.CfnWorkflowProps(
                default_run_properties=default_run_properties,
                description="description",
                max_concurrent_runs=123,
                name="name",
                tags=tags
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2fbf58b972f40f14f50a92e85a2c44b7714f052d44776dc875496359365c5db)
            check_type(argname="argument default_run_properties", value=default_run_properties, expected_type=type_hints["default_run_properties"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument max_concurrent_runs", value=max_concurrent_runs, expected_type=type_hints["max_concurrent_runs"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if default_run_properties is not None:
            self._values["default_run_properties"] = default_run_properties
        if description is not None:
            self._values["description"] = description
        if max_concurrent_runs is not None:
            self._values["max_concurrent_runs"] = max_concurrent_runs
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def default_run_properties(self) -> typing.Any:
        '''A collection of properties to be used as part of each execution of the workflow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-workflow.html#cfn-glue-workflow-defaultrunproperties
        '''
        result = self._values.get("default_run_properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the workflow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-workflow.html#cfn-glue-workflow-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_concurrent_runs(self) -> typing.Optional[jsii.Number]:
        '''You can use this parameter to prevent unwanted multiple updates to data, to control costs, or in some cases, to prevent exceeding the maximum number of concurrent runs of any of the component jobs.

        If you leave this parameter blank, there is no limit to the number of concurrent workflow runs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-workflow.html#cfn-glue-workflow-maxconcurrentruns
        '''
        result = self._values.get("max_concurrent_runs")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the workflow representing the flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-workflow.html#cfn-glue-workflow-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''The tags to use with this workflow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-workflow.html#cfn-glue-workflow-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWorkflowProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnClassifier",
    "CfnClassifierProps",
    "CfnConnection",
    "CfnConnectionProps",
    "CfnCrawler",
    "CfnCrawlerProps",
    "CfnDataCatalogEncryptionSettings",
    "CfnDataCatalogEncryptionSettingsProps",
    "CfnDataQualityRuleset",
    "CfnDataQualityRulesetProps",
    "CfnDatabase",
    "CfnDatabaseProps",
    "CfnDevEndpoint",
    "CfnDevEndpointProps",
    "CfnJob",
    "CfnJobProps",
    "CfnMLTransform",
    "CfnMLTransformProps",
    "CfnPartition",
    "CfnPartitionProps",
    "CfnRegistry",
    "CfnRegistryProps",
    "CfnSchema",
    "CfnSchemaProps",
    "CfnSchemaVersion",
    "CfnSchemaVersionMetadata",
    "CfnSchemaVersionMetadataProps",
    "CfnSchemaVersionProps",
    "CfnSecurityConfiguration",
    "CfnSecurityConfigurationProps",
    "CfnTable",
    "CfnTableProps",
    "CfnTrigger",
    "CfnTriggerProps",
    "CfnWorkflow",
    "CfnWorkflowProps",
]

publication.publish()

def _typecheckingstub__c31bd9435d221f14c31ca91edbb76c0650b44f88a5a16431a384ce5854e7dcad(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    csv_classifier: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnClassifier.CsvClassifierProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    grok_classifier: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnClassifier.GrokClassifierProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    json_classifier: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnClassifier.JsonClassifierProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    xml_classifier: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnClassifier.XMLClassifierProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e64f8d2a274e89a852157febbc2182dcdb6d685a9d95146fd826be8c2e235c78(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a98d3c148e3cc0a370f92962b0a2da4be9f04c87b7df15e7a8ef87c4ce340011(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5250a15edb331e6856f0a29ac71c9e1513817ae7d411a90f5455dc89a24868c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnClassifier.CsvClassifierProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e433b191953f00afa5a4fb4333937a124c4a4865d13433693cab445ff794619(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnClassifier.GrokClassifierProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a99cf38e8a5d3d6d2a91d7585371a72e04e5cab9a9dfbfba99cbaf227511f5ab(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnClassifier.JsonClassifierProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__204ba6e258d6c443b165b0772162d891e01db52b8bf7b049b0e9d4968dfbc7d4(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnClassifier.XMLClassifierProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd722ed29ebf9e1505b4d21b5e95cb0f8d4e96b052ed45a497086e92f8d1eb4c(
    *,
    allow_single_column: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    contains_header: typing.Optional[builtins.str] = None,
    delimiter: typing.Optional[builtins.str] = None,
    disable_value_trimming: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    header: typing.Optional[typing.Sequence[builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
    quote_symbol: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f202c9743be8e12fb8f1f3a29eafdc0152da5577c8be943f4da1e40c32ce952d(
    *,
    classification: builtins.str,
    grok_pattern: builtins.str,
    custom_patterns: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6b0562c401f5718be9d3ef21289193ef2c0168f41e441d7c38d624e0a079382(
    *,
    json_path: builtins.str,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__094348bf3568d41b3cc714d3098201aa1e2ce70a5da5beedf13ad7647bdd439c(
    *,
    classification: builtins.str,
    row_tag: builtins.str,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f036110075bbf70f52e4d02f33e758480e5ed41c2ddf5774889968357c16fd9(
    *,
    csv_classifier: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnClassifier.CsvClassifierProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    grok_classifier: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnClassifier.GrokClassifierProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    json_classifier: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnClassifier.JsonClassifierProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    xml_classifier: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnClassifier.XMLClassifierProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed744b41db4675b65946b69de8e2f2df8beabc93f21d52abb4a5ce5d2e35d6e3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    catalog_id: builtins.str,
    connection_input: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnection.ConnectionInputProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e547a83aa8b1312e498ca658e38bfef22a6326568f2ad4059850b9314ab882d7(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af52b4937be9d9e9227708cfce1a1bf8e680539b738b3353dbb661804261b361(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d64fcdf69b5b53d13d7560a99def80cc1ea81eb69a521ae5d8d75a05c0f8be1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3a76484105010dc758d81394f436d3461656f97faa1bf881b484b7db1731e0b(
    value: typing.Union[_IResolvable_da3f097b, CfnConnection.ConnectionInputProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74e68b34e0a01df244f744096d99b1ff48c5f31548a88acaaf6d555c46a2fb76(
    *,
    connection_type: builtins.str,
    connection_properties: typing.Any = None,
    description: typing.Optional[builtins.str] = None,
    match_criteria: typing.Optional[typing.Sequence[builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
    physical_connection_requirements: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnection.PhysicalConnectionRequirementsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40f33bb16819b03c45621bf4ec1060b418651be3dfd02f581f0cf1a6cd12cdb3(
    *,
    availability_zone: typing.Optional[builtins.str] = None,
    security_group_id_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff86c0b8645eadb56850c28ce69021a78b30a75c13614c05815d7faf9f9f1eca(
    *,
    catalog_id: builtins.str,
    connection_input: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnection.ConnectionInputProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff9e598239ccebeecff8b5e3f5f0458f9de0c5c407db27837fb3122adfbb48ec(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    role: builtins.str,
    targets: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCrawler.TargetsProperty, typing.Dict[builtins.str, typing.Any]]],
    classifiers: typing.Optional[typing.Sequence[builtins.str]] = None,
    configuration: typing.Optional[builtins.str] = None,
    crawler_security_configuration: typing.Optional[builtins.str] = None,
    database_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    recrawl_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCrawler.RecrawlPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCrawler.ScheduleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    schema_change_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCrawler.SchemaChangePolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    table_prefix: typing.Optional[builtins.str] = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c4320c740e3b9cb750745ec213ccc0ddab6c6f8d0fb2cc3678b58a5eb96963b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ba899fc83e9439ba1eeaaf05c1cdb7db00223ee9639e5684b994ecbeecdba12(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d0f4795e30bdf52af75380422e6956fe78ac8cabb8c11c0f4d1f4c6efa13a72(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8f17e8d0442485526676f5689364bcd775336febf0f27ff8adca3138ea4323d(
    value: typing.Union[_IResolvable_da3f097b, CfnCrawler.TargetsProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc97ff23bae45ac9e65f21fa1ea785f07dad693833d84e93e2d73c22f67659d6(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__192c642ccc1851982655e5d714a44522ea0ae0644693504905373aeb461e6710(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad2cd3791a15d37fb39d53dc3e9305c735cef04bef3c2bcd36f656e2e3d9a727(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c0bced28b99cf5d6601a1e7268fb7fc84fbb7db6c55eb201f867678b9006fa8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55e97c90536e63620917a74b9e753f3ef37d2ba4cc78a367b3c2692a6a9073d8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35986739065f4f5528fa36a3a4743b76eb0937d555e5d7ad917e107db84e9d92(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83e372f1422865065a5a3898b76f8c4b4c2b501fffdd71b9c7bc33febbb10363(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCrawler.RecrawlPolicyProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57543db817586f6f96b889ad18bd67740cd8212822395c2ef09e8dfcd0130552(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCrawler.ScheduleProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14e3cba92ee30f03751c9fb3a0546500940820fefc42b0c7c3c2bc17bd5773b5(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCrawler.SchemaChangePolicyProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49ba3e782c84d62bea6d1f3c7f0c9468d3b13099042cf162e2e35456bf59a264(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43760f25278105b8154c121bf9dd9dcaa617159cbb1a2a43fedb1312640eb5a0(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f163f3382b5ca5c3414fe2db6d7ec2500afa6a106f4cda66075603ccfa491c62(
    *,
    connection_name: typing.Optional[builtins.str] = None,
    database_name: typing.Optional[builtins.str] = None,
    dlq_event_queue_arn: typing.Optional[builtins.str] = None,
    event_queue_arn: typing.Optional[builtins.str] = None,
    tables: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7510699883f74759e475bf2ece2842156b441164d538264f93242ebdacee3c2(
    *,
    connection_name: typing.Optional[builtins.str] = None,
    create_native_delta_table: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    delta_tables: typing.Optional[typing.Sequence[builtins.str]] = None,
    write_manifest: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c03ffc3d1fa17ed9770b2c448e87c012b6d363001f06ce8b95bdb9c62711274(
    *,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cb27c7db73a5c6fa3740f2d4726f453641d40911229d3bb39f26c4402516cf6(
    *,
    connection_name: typing.Optional[builtins.str] = None,
    exclusions: typing.Optional[typing.Sequence[builtins.str]] = None,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b27a374f7da5948658852ac367f177b833b9e06c48e0a246c211a7d7ede3af94(
    *,
    connection_name: typing.Optional[builtins.str] = None,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e40a02828fa90824e4069120d7dbc0e3e1eccbd3e09087ff5c6bb9b3005e1f4e(
    *,
    recrawl_behavior: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4086580ebeb74fac287364f6cbdacc62bee81dd975f186a492fc80c7037071c8(
    *,
    connection_name: typing.Optional[builtins.str] = None,
    dlq_event_queue_arn: typing.Optional[builtins.str] = None,
    event_queue_arn: typing.Optional[builtins.str] = None,
    exclusions: typing.Optional[typing.Sequence[builtins.str]] = None,
    path: typing.Optional[builtins.str] = None,
    sample_size: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__665dbaef4a9e75ff541ec9b561a356e92755d78e1a5d1701fa9004482f92ed7e(
    *,
    schedule_expression: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75f9df7f7ba86ceb8199c254017b595776e141c4c4688a6f26f8b203f610a9fd(
    *,
    delete_behavior: typing.Optional[builtins.str] = None,
    update_behavior: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe7a457ca9245ce0e51373e4e1d8daf444f9da978c352bc8529931e53484771c(
    *,
    catalog_targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCrawler.CatalogTargetProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    delta_targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCrawler.DeltaTargetProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    dynamo_db_targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCrawler.DynamoDBTargetProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    jdbc_targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCrawler.JdbcTargetProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    mongo_db_targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCrawler.MongoDBTargetProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    s3_targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCrawler.S3TargetProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51125dcaf0f55fdaefa50d6b9c05a6e431008538b8ab24abc0fbe126f61c382c(
    *,
    role: builtins.str,
    targets: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCrawler.TargetsProperty, typing.Dict[builtins.str, typing.Any]]],
    classifiers: typing.Optional[typing.Sequence[builtins.str]] = None,
    configuration: typing.Optional[builtins.str] = None,
    crawler_security_configuration: typing.Optional[builtins.str] = None,
    database_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    recrawl_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCrawler.RecrawlPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCrawler.ScheduleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    schema_change_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCrawler.SchemaChangePolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    table_prefix: typing.Optional[builtins.str] = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__282fa6292001a27626ebcdd16c3756f6c1f39e2fce0bffe2aa07015e603b0c74(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    catalog_id: builtins.str,
    data_catalog_encryption_settings: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataCatalogEncryptionSettings.DataCatalogEncryptionSettingsProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4e1e9ace4bcb120e971fb9f4d836733533c524cf73881927356077e8a876243(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c9dd3472041f0c72b01ac8da059b956f55ea8a163f3d588982e26081d26472a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01920d02ae9ef51342dbd5a647a412a6e68458011da6333a12e4cbce3c46addd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0fe99133f601e0dba434462eeee0ca24bdba16dd90df4d18a9865152672243b(
    value: typing.Union[_IResolvable_da3f097b, CfnDataCatalogEncryptionSettings.DataCatalogEncryptionSettingsProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34fc71f63e95ce1add57dfdd2e0ed274fd6575145b30e9f35229e487efafb211(
    *,
    kms_key_id: typing.Optional[builtins.str] = None,
    return_connection_password_encrypted: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f00201a45ca678da32495cdf8e4750f6ee26f926e576c207f665e4982e5d8cbd(
    *,
    connection_password_encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataCatalogEncryptionSettings.ConnectionPasswordEncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    encryption_at_rest: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataCatalogEncryptionSettings.EncryptionAtRestProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b55ae3f68b9a52d4f03ea46854dfc3c74490f427c278113fe4c847eaf6e6143d(
    *,
    catalog_encryption_mode: typing.Optional[builtins.str] = None,
    sse_aws_kms_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3517f092be8bfa15079cf31c36ac6d8b4bfcf20615da68fd5127533210ef5c4(
    *,
    catalog_id: builtins.str,
    data_catalog_encryption_settings: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataCatalogEncryptionSettings.DataCatalogEncryptionSettingsProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cd6788453c5f421cc94877f7bd1430bf0188a7b66044acb47e85a138c2525bc(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    client_token: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    ruleset: typing.Optional[builtins.str] = None,
    tags: typing.Any = None,
    target_table: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataQualityRuleset.DataQualityTargetTableProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__821cea04f03dd8ae13ef8a301a29741a754cfa451c98bf537c239b6333df0af5(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2adc51e0237315dfdb93e5fccd4fccd0705f44e751c4ac91b448d6d8fb5bcb43(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb7412aa32bb9c0fa23c3df7527a57c842aabf5ffa622d5ab6cd6540caa2e57a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e22bc2d9629c173f100a1ee8aea1f132a9bc0e287ff0e2b88d829b304c3de308(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c19fdaeabb94e016ab468e10db4486c501c8a4f296c51d5fd475d3ea7f6ab92(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f89426cd75d9e88eba122cc29f0542dfceb62cfb21e07d8b912deed58918f8db(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__809d4010b3349232ca0d6023603914d402aeeedd96245959f582ca639b97209d(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2eee281115746d453b02c60bac1ee159c50e3f758af73dcf2d6ada02e2cc1d0(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataQualityRuleset.DataQualityTargetTableProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ead7fcb21ac05404e5bd5b515921d45f020c05cc414cc713cd438ccf815c1417(
    *,
    database_name: typing.Optional[builtins.str] = None,
    table_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffd76843e7c0bf19ed341799bd6544ae909492cbfe595bc8806ea114fc1b01f1(
    *,
    client_token: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    ruleset: typing.Optional[builtins.str] = None,
    tags: typing.Any = None,
    target_table: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataQualityRuleset.DataQualityTargetTableProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7145103c869df1a981612b4445af4fee59059eebaa09d55e36fa9961bbd0d271(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    catalog_id: builtins.str,
    database_input: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDatabase.DatabaseInputProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0e83df07074fd6e3bd554052571366deb1febf7f69f6452ca58261d50898a69(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc3a63206fa9807ebcdb35676de76b49507fbd5baf5ec473e655fb4ae8d37882(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86a8e89801bb5dac6dbcec69f62eb5089c97eac21e4a7b226afccf50df44b861(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e2364f804df0cc3d57e45e3e5c68968dc857adcab1747035408147542b2d495(
    value: typing.Union[_IResolvable_da3f097b, CfnDatabase.DatabaseInputProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fa63353d4d392cf6a598ebd7c80b56747ad0b7973313267f52becc342ac17de(
    *,
    data_lake_principal_identifier: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e1e09205087e89c58802ef33b1c27bb5ad9de3db3e6419d7c72b490675f5e27(
    *,
    catalog_id: typing.Optional[builtins.str] = None,
    database_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4066647dd15931f0ef186e76b4d72a1a31dd7f45cce5691790e1c5709a696c3d(
    *,
    create_table_default_permissions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDatabase.PrincipalPrivilegesProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    federated_database: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDatabase.FederatedDatabaseProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    location_uri: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    parameters: typing.Any = None,
    target_database: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDatabase.DatabaseIdentifierProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5d4932721a3226e798772e900af6d3cb2ecce08df6276ce369fcbac2f8da038(
    *,
    connection_name: typing.Optional[builtins.str] = None,
    identifier: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d43a817f676c64836757736236e2f064cc4dd36dc5c52414d08763ab68e9ed24(
    *,
    permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
    principal: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDatabase.DataLakePrincipalProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2352883ee521541265e5630512401b3837ac0875c8b4eced9967bf612ebac267(
    *,
    catalog_id: builtins.str,
    database_input: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDatabase.DatabaseInputProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f207845d994208ff1660ad2df9e045c11ca6d377ac8544937edbec1dddebfba7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    role_arn: builtins.str,
    arguments: typing.Any = None,
    endpoint_name: typing.Optional[builtins.str] = None,
    extra_jars_s3_path: typing.Optional[builtins.str] = None,
    extra_python_libs_s3_path: typing.Optional[builtins.str] = None,
    glue_version: typing.Optional[builtins.str] = None,
    number_of_nodes: typing.Optional[jsii.Number] = None,
    number_of_workers: typing.Optional[jsii.Number] = None,
    public_key: typing.Optional[builtins.str] = None,
    public_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    security_configuration: typing.Optional[builtins.str] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_id: typing.Optional[builtins.str] = None,
    tags: typing.Any = None,
    worker_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25858fc016328e41980e9e383fa8c74ea692bfca06ad7f98509c9506b91dffa6(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70743942c06388357f2f720c4ada83418cff43d779d1a2cadbeff13e0ec993bd(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3ba742e80db6ba15b810adbf5224257106f26a45069b05aa0962cf9d1acae18(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f7cd2d66e90d13b73d70f0cea82d85557e58e9448ea913c041c3bb9890fac7e(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3656b1b0d044829185242e72e3a9d78c819cbc0c4b0c7432f1eb535414b5b17(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e22b746e679f7c726ffcfb4c2ec05837d1aa0389da49de5598456a876e1b554a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36f713fcb7ab5c574cc125a1fb44accac20e28686e76d617cf782eb65f0f7ba4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98ce29d45190375e16a82b2017ac8c9f720adba1c61cee92540176217662a1c3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4235e3cff351beb8894679d614311c5f7e1ecc504f7d84835c7517c54fc6044a(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9452cc6cc6f8a5fd5473515eef605e3672e7be0d39a719c23950636d6003249a(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb34f4cce325bffcbaf7901df0a55caf15f7878b322e8314762796d8323cfc20(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8943aff10625ef6c28e1a4686a3e4090206cdedd2fc46827336359b904a9cdbb(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec27168647e97503a81f083dd382a6a5792e1c7a34be7ce7c8e3ce1b24ca0eca(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc83e99874e70b5e3e40d0d86646d5472a372806976261bd02f95cbed414fd29(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1fd805ade2dd824f981ba7d8026f5d5425fb676f266db5338e748229fe33c40(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03002f2a13cc3cbf7cf9bb6d6a81931afcc4646ea26bd164b4b95dcd73f6fa3f(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce7ed9ca11cbfba09db8e54f347bcd3ff43297ea4bb0dc406683cb9e0186fa1e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__789306655393b50bec94a0cbbc4385fd0d7103127d033ea3eaabe59af1f46804(
    *,
    role_arn: builtins.str,
    arguments: typing.Any = None,
    endpoint_name: typing.Optional[builtins.str] = None,
    extra_jars_s3_path: typing.Optional[builtins.str] = None,
    extra_python_libs_s3_path: typing.Optional[builtins.str] = None,
    glue_version: typing.Optional[builtins.str] = None,
    number_of_nodes: typing.Optional[jsii.Number] = None,
    number_of_workers: typing.Optional[jsii.Number] = None,
    public_key: typing.Optional[builtins.str] = None,
    public_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    security_configuration: typing.Optional[builtins.str] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_id: typing.Optional[builtins.str] = None,
    tags: typing.Any = None,
    worker_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bea698eff4ea1d2bc08b1ab842f318f77ba719c0241a0959453e26989b5b53e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    command: typing.Union[_IResolvable_da3f097b, typing.Union[CfnJob.JobCommandProperty, typing.Dict[builtins.str, typing.Any]]],
    role: builtins.str,
    allocated_capacity: typing.Optional[jsii.Number] = None,
    connections: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJob.ConnectionsListProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    default_arguments: typing.Any = None,
    description: typing.Optional[builtins.str] = None,
    execution_class: typing.Optional[builtins.str] = None,
    execution_property: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJob.ExecutionPropertyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    glue_version: typing.Optional[builtins.str] = None,
    log_uri: typing.Optional[builtins.str] = None,
    max_capacity: typing.Optional[jsii.Number] = None,
    max_retries: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
    non_overridable_arguments: typing.Any = None,
    notification_property: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJob.NotificationPropertyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    number_of_workers: typing.Optional[jsii.Number] = None,
    security_configuration: typing.Optional[builtins.str] = None,
    tags: typing.Any = None,
    timeout: typing.Optional[jsii.Number] = None,
    worker_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d425131e9ab8979b5db307155c42bb9935456dd21866bba5ed461a9c8c90df3c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff736c600c4721825d122a059a265a3c60efe89b58ef836fd0db2d0e1b7f6ae1(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92e6559d7b7e4750985b75f86ff0ead213e6dcf804f0f9d87d12c5dd11ef4b68(
    value: typing.Union[_IResolvable_da3f097b, CfnJob.JobCommandProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6215be83f5dcb82628d4c0f7daff3e6e5a40b7ba8133cbdd559c85f264c8248(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e8f0c1f38624103ad14795e648b3d5168a0409e14719e267939220545367271(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54148ad575a4b3d562b59f1200c3e45bd7838ddba81c25e024f8359b11bcc075(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnJob.ConnectionsListProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e02555d63017f6d2d384ad19fac040a7af8d997186aa0f5944d58f0edeb3d405(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c83f3f89400406aba1208c6fc333278a0e35af3b3730a8e266df0815d59250ef(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c98638b6313e2e604e3d982eb0c830608a266977cd3c1a3547296e48a712e454(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__288a9558b01117977548bd27d8b359f6aabd127fbbae8871f921f4f4ad731aa0(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnJob.ExecutionPropertyProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f36e5a6a7d1a062f3bf5d8b7176a1f0f8c07bc3e7e725aefec8d86d74b346411(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ca81eaaed120981305eb66586283b558b72d3b37cb0098234ec82c56f1d637a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a764dd1178d54ad958e98a11fae132faf1dc82baf8cc6de7a480139bec56d6c(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__747e11b9e0393534a2a604c6185f8016b6350fbf93c4b5cc55c96315ddb87867(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34834931355b72bf0842139ae8010d5c3e556cc67c00f907c4e39b8297ecae5d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68288520cd14059f70bcdca01796f4f53b90b28bd9200d4a3771f70a8977093c(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__886cabf7d73da58088c752153f330c0b15d55d0334b2e6e1429c361c244fa40b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnJob.NotificationPropertyProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dd8b61874c785b7e401c38c72a26b663aafa165c05e223526a1b04215648b44(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__686551f876de8c0263f876f1f95fa84db57247f0bfd43e39fd7e27705da22d75(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__542d438feaf9522e0e8293fe9c53267730a064a757ebc71e8aa9fd97d002c38c(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c12c03e51261ea1008482a07620562f930d2ee59fec35bf127da7d754e08de3d(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6b16368f5ffc1ef3ea15b397687a68037aa7eebf6a316b97ece9c4f3e17d49f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c7dc433e6f7c5ca3d12814ece3fac51b4dbb146e7e2fd378ced704cb23f9b13(
    *,
    connections: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__520e2daea7c2ab288e9c6e2ba71dcb41ab10da7ecd61430c90a856eae7bdd314(
    *,
    max_concurrent_runs: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87fac9903ef58adfafce7d1cfda786501500eb9ea0b225cf51bfa32f2798403e(
    *,
    name: typing.Optional[builtins.str] = None,
    python_version: typing.Optional[builtins.str] = None,
    runtime: typing.Optional[builtins.str] = None,
    script_location: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d87f46f82fb4abde6f1cc1fdfc015cb65e4bb0f311eb52da272f4e484d5117b(
    *,
    notify_delay_after: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b5bd8295520fa719be46f80478ae155292fb66f6fc3016eb114b6fabf6050df(
    *,
    command: typing.Union[_IResolvable_da3f097b, typing.Union[CfnJob.JobCommandProperty, typing.Dict[builtins.str, typing.Any]]],
    role: builtins.str,
    allocated_capacity: typing.Optional[jsii.Number] = None,
    connections: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJob.ConnectionsListProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    default_arguments: typing.Any = None,
    description: typing.Optional[builtins.str] = None,
    execution_class: typing.Optional[builtins.str] = None,
    execution_property: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJob.ExecutionPropertyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    glue_version: typing.Optional[builtins.str] = None,
    log_uri: typing.Optional[builtins.str] = None,
    max_capacity: typing.Optional[jsii.Number] = None,
    max_retries: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
    non_overridable_arguments: typing.Any = None,
    notification_property: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJob.NotificationPropertyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    number_of_workers: typing.Optional[jsii.Number] = None,
    security_configuration: typing.Optional[builtins.str] = None,
    tags: typing.Any = None,
    timeout: typing.Optional[jsii.Number] = None,
    worker_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53d1d58fe97e9c17e46132b4f82f741ba019c774fe0bb3bdba1d51dbefe20295(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    input_record_tables: typing.Union[_IResolvable_da3f097b, typing.Union[CfnMLTransform.InputRecordTablesProperty, typing.Dict[builtins.str, typing.Any]]],
    role: builtins.str,
    transform_parameters: typing.Union[_IResolvable_da3f097b, typing.Union[CfnMLTransform.TransformParametersProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    glue_version: typing.Optional[builtins.str] = None,
    max_capacity: typing.Optional[jsii.Number] = None,
    max_retries: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
    number_of_workers: typing.Optional[jsii.Number] = None,
    tags: typing.Any = None,
    timeout: typing.Optional[jsii.Number] = None,
    transform_encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMLTransform.TransformEncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    worker_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17b628057d4918b2654a169e223fdc7952223107b4c9c602966d2f6978fffbac(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a38f97a53150f570084eea59308e238fbdc6786009a78ad9b014ea3066fb96a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54fd840993f985c80395aeca9c3bc8723d003f9914e7c4e4a7890214daecad59(
    value: typing.Union[_IResolvable_da3f097b, CfnMLTransform.InputRecordTablesProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee501d5b7fc7fb085aeae9cabacd68b8b8d9f9866700a8a370252e40d31650bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32022d812fa908378c1d2e724a2377474b2ce1f4f966dddbf71ad1f1c9d13dff(
    value: typing.Union[_IResolvable_da3f097b, CfnMLTransform.TransformParametersProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f2e6f1cc38d1a413374f9b9d4c02417e959e5f3077812b1cd868c70d042a16f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4646b4f4efc89b1d9dc0884d55d7b11dd5293a19543a11bd2e2263d781af4a1d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d7678713b6284330c12e1b7e5e0121d21dec44a07c295ccf2831f5ebfda27c6(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b160c59f4536e5ba52b74262cc6c6277e29a9bb5d974893cb0aee1fdf2a93fa2(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97cb29ae8ccb30f3ace545620215abebebb628b2c7d82e15cb1e9519bb20db6c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c04ef8b7c306add821bddff56dbf5750b8115ac7dcd8c9ef30267c9df9f57ce(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bcba5ebc0f231f7604a777a23c7985de7effc5b17647f8eb4388c48526da0ea(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d453ce28abce1d452e03956918ae4226d76e061240e5ae5102f955efe877cfc(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e334953b8c4313c154db54fc8c4faa48859bad94c59b631d2bf8ead2740ffad1(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMLTransform.TransformEncryptionProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f54a6e39b64aa4029e491424b0cd24a6797c45e24fe6065a5fccd306f38e053(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb960ae42c6510d9bffddd8ca5eefc269b84bdc4e274fa58d90d24d5550e89e8(
    *,
    primary_key_column_name: builtins.str,
    accuracy_cost_tradeoff: typing.Optional[jsii.Number] = None,
    enforce_provided_labels: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    precision_recall_tradeoff: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__017d4f0d02247f62a0dc37d383358ecd0448dfa33a9ea50bdbbb69eb66944468(
    *,
    database_name: builtins.str,
    table_name: builtins.str,
    catalog_id: typing.Optional[builtins.str] = None,
    connection_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4731f5241b81024e6091aa4dadb760cb188ad13cdde880df977f150a45c3918(
    *,
    glue_tables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMLTransform.GlueTablesProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecd370c09a22e068431da60552211124971655ed94a2a502fe3964bd9bb6bdde(
    *,
    ml_user_data_encryption_mode: builtins.str,
    kms_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf35b8d358e083dc66c9259f80d1b243e0aa377d776b55769dfe34361e9fa673(
    *,
    ml_user_data_encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMLTransform.MLUserDataEncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    task_run_security_configuration_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27d8f07bc63a2f9d168ac15d71b18b3b52c19f2d86354f5fe7d1f2b5ea5a0e01(
    *,
    transform_type: builtins.str,
    find_matches_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMLTransform.FindMatchesParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__320c2c3396b30a5429b1cfe63b51777e981f1bc44756e68b10eda51ae9545c44(
    *,
    input_record_tables: typing.Union[_IResolvable_da3f097b, typing.Union[CfnMLTransform.InputRecordTablesProperty, typing.Dict[builtins.str, typing.Any]]],
    role: builtins.str,
    transform_parameters: typing.Union[_IResolvable_da3f097b, typing.Union[CfnMLTransform.TransformParametersProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    glue_version: typing.Optional[builtins.str] = None,
    max_capacity: typing.Optional[jsii.Number] = None,
    max_retries: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
    number_of_workers: typing.Optional[jsii.Number] = None,
    tags: typing.Any = None,
    timeout: typing.Optional[jsii.Number] = None,
    transform_encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMLTransform.TransformEncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    worker_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a7cb666e01a9021862d0b0ab8ac8df4a82cacbe6e60f96bbb3750ad2762477d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    catalog_id: builtins.str,
    database_name: builtins.str,
    partition_input: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPartition.PartitionInputProperty, typing.Dict[builtins.str, typing.Any]]],
    table_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78b5b937bbcdbead6e9c098e9cd77435e7317295bfb6d1904684e13a384ac6d6(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f644fc0761047bcbda0ea8aac635dce186b45d62461ee98ed3e439f77acd2fab(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f05fc58a7dc1eb68d886a76ecea23887719e05c9a816ad3a6a82999eda2fdf9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2762d2587b458636fd5397b14953879deb18c5a9e411047982e4ecff34ece56c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a04341e86b5b0abb4af36bb01085e5230c242739cfcb7d8670acc5c03597f004(
    value: typing.Union[_IResolvable_da3f097b, CfnPartition.PartitionInputProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__407a57f0321dcc4b1394792773d1290f6cc36a639f46075ab9d69357bcf87d5e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4128b3824d24d7248464514a703ec957c021fee39eab508d95517af968ceaca8(
    *,
    name: builtins.str,
    comment: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__086400f3f7469a3643555e94ddf84e766852816562334968079941d386daac37(
    *,
    column: builtins.str,
    sort_order: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d5dfe9bb6765a27446a89b60a666937eef85988d6bf0f139dc62f6db7ab5937(
    *,
    values: typing.Sequence[builtins.str],
    parameters: typing.Any = None,
    storage_descriptor: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPartition.StorageDescriptorProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da4bd669a07bac042fbbb4e023a90f07ceff6ab8a5afbbb2c55a826769faca15(
    *,
    registry_name: typing.Optional[builtins.str] = None,
    schema_arn: typing.Optional[builtins.str] = None,
    schema_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be049becd9a1c1413e38e320ee3a71c5d2abe254bfc360c441dbb95d19c793d5(
    *,
    schema_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPartition.SchemaIdProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    schema_version_id: typing.Optional[builtins.str] = None,
    schema_version_number: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c43ded18a2aa53ebee991696cce2d20a8ba939c244937cbcf36e93d11432061(
    *,
    name: typing.Optional[builtins.str] = None,
    parameters: typing.Any = None,
    serialization_library: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7435667120cf63046fa2c7684e85f094807aa6e5e2cd23406caa6e5569843a1f(
    *,
    skewed_column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    skewed_column_value_location_maps: typing.Any = None,
    skewed_column_values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96dc3348b2a22bbbc2a529f40eb4fdbd644f9e0e8660ca12ec5e132cbb27421f(
    *,
    bucket_columns: typing.Optional[typing.Sequence[builtins.str]] = None,
    columns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPartition.ColumnProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    compressed: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    input_format: typing.Optional[builtins.str] = None,
    location: typing.Optional[builtins.str] = None,
    number_of_buckets: typing.Optional[jsii.Number] = None,
    output_format: typing.Optional[builtins.str] = None,
    parameters: typing.Any = None,
    schema_reference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPartition.SchemaReferenceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    serde_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPartition.SerdeInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    skewed_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPartition.SkewedInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sort_columns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPartition.OrderProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    stored_as_sub_directories: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e44f0759b77ba4f2a6fc23f3b51c3b9b3a8893e479e1a1f17da4181d294dea48(
    *,
    catalog_id: builtins.str,
    database_name: builtins.str,
    partition_input: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPartition.PartitionInputProperty, typing.Dict[builtins.str, typing.Any]]],
    table_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5de9a299a2bf41c1ad28fbb79cc31782da6bbeccfd6ad8c09014110dec87fcb6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc8a013f30adcd1edf09a70d6cb3498fabc5c2275ef048bccad07b556f68c139(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__488adf133bcfcc60051c0a11031a6cf7f8f1578dc2bdf68315cd037cba2c8d45(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b08a23e9e0a8332240d398591fb00a0705ae1c744f78c8c7f99d6d42cbbbfe2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86912387bdaf3c2b7844a0b55fafc22c116e70b5bcd99b91ed151e3649a7d992(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3addc589422a8772c97f55547db6d321590b6a3078e00ea158feb432c9141727(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9d85e07a2dcc4ae5cd073c48fc5eb424c7446e4be042407f1f89c111ef9bba1(
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c24fd21e2dfff4073f4fd8235eb4e6907b6a19fef52a7e12e6cc32797cc23f2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    compatibility: builtins.str,
    data_format: builtins.str,
    name: builtins.str,
    schema_definition: builtins.str,
    checkpoint_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchema.SchemaVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    registry: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchema.RegistryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__032942ae67479a8dd85c055f92ab4293be2dd277171c761f4c8e973149ffe307(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0c653bd170b326c508ed7517a107d65cc72284d82d39ce6c114dcccde4b40a6(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b73978872411b0a345203986e3747c7d8e8aa6c7a7d84c98ea032c8a52dbfe31(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5e37c443190efe6042f27de7c8f6bcb3356c41291ed3f6e60f326b159aa86c6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff3dcb47edaa294c6caf2b08476ad6ab296e0af75fac6f4cff50f7d0702daa85(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0425f83d697fdeb65b7ad72b89add3f188c811ceb74503e3deeda6f8fd774134(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e496b746565a2a907c7b308108c0f360ed6e1d756d065268762427d0c0195ca(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSchema.SchemaVersionProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__256a8ca904755342242bfb57993a7b4a73841aa88a6f73b4533a2ecca3f961d4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9180e06f6739c2a1783c2974f71f4a42d49ca8423d693d37b0c96b31d3092bb(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSchema.RegistryProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2060d4f7f98e703465a1d2f6e55970d3e0767652cb30c60bd1dfb69101403c47(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a294a0c13681e2402296e02dfba512363ce2418d91d7d958543bbf10879c5c9c(
    *,
    arn: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e90fb9d4f51c449f67d6d38fa8a393062e21c0ebc8dcff0751d9836010ae6bf(
    *,
    is_latest: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    version_number: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbb4fb2ee83fa315d5be44ea6b3b74388d44b2e9cd9fac352aa28801b198dc21(
    *,
    compatibility: builtins.str,
    data_format: builtins.str,
    name: builtins.str,
    schema_definition: builtins.str,
    checkpoint_version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchema.SchemaVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    registry: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchema.RegistryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da5c949b18973d69cdae418c5f7d35241c93c30bd7bc7107898aaaaceb698e6e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    schema: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchemaVersion.SchemaProperty, typing.Dict[builtins.str, typing.Any]]],
    schema_definition: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d9452a9d70f3e83a829bffc8890b5cfcb4a0c94403e5c71cf3e3ebe8bbd2492(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb5cfc17ffddec9de88bdc242538249096b5eead4c8b77fb57579bb17b81c824(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5443b6104677a75bc9caf64ee057fa55e785bec78f049fc4f5e67efd29bf7461(
    value: typing.Union[_IResolvable_da3f097b, CfnSchemaVersion.SchemaProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e456dd17518782fc61b283ca5fd68bf909fb10c1e515b9fb474ecbc27c8e77fe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f58a0cb66904ee076f56bd0f3a3a196888dbbbe43086cf8bbd9b49084a112846(
    *,
    registry_name: typing.Optional[builtins.str] = None,
    schema_arn: typing.Optional[builtins.str] = None,
    schema_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a9a3e2496aeeeaf0a9f2c36f1a1d9a7ad7e6c6e6875c4024e3b0fdc4efba8f7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    key: builtins.str,
    schema_version_id: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bac3436fdb71de23e44fca8189770fd0ac700ebf763f7dcd804162c147430a02(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93a32ac74bba3f51224a5f766cdd3a3caeaefa0b4e23580ca45bda0d4aef86ef(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09ba199b752efbd3e189be84aa34a757c8f25ccebe52ad436e40c984b8b3bc6c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe366520765f5ad7f7a4e96a3e9d66b34f59675ae226488e2e7c96301b098c2a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70216207f8d7da97cc8c8430c3dd8593322988412423bfad46412dc2c24ae7d6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d673339819d7914956c800afb9c521310733b754757fa3b69916588124f4856c(
    *,
    key: builtins.str,
    schema_version_id: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eeab38cc4ae72ae0d45e70c51097046996a15bcbd57776c5c6711c1cc3c34753(
    *,
    schema: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchemaVersion.SchemaProperty, typing.Dict[builtins.str, typing.Any]]],
    schema_definition: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c75e7a9665c1990bc4f5c74c4d708791cc9808fb5f2dd7221d5808a570d6ca4f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    encryption_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityConfiguration.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edb3649bcf711595ed0e7f1ff5f9487f357ca680d6c33c94cce0d4945c1110ca(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76a673725f7d43dfd4d86005be3140e85bafdb23ee1eec2302634a8e2738146f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41a8b680be4f05190dbfd222f5985022aede1900f04a5407fb5617312ab60e00(
    value: typing.Union[_IResolvable_da3f097b, CfnSecurityConfiguration.EncryptionConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8331f03d77759f61a97615e9eeefbfcaa25822091618cf7de977db83cbfd7d9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__368c78d5e54f1e192576beedf15b669bbe7d53dbacdbe73327838ca2c71a5e9c(
    *,
    cloud_watch_encryption_mode: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6be244b0a6c6cf18e64a0019f78450ca4ed5b5a8db428f106e8577b9d4c685e(
    *,
    cloud_watch_encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityConfiguration.CloudWatchEncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    job_bookmarks_encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityConfiguration.JobBookmarksEncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_encryptions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityConfiguration.S3EncryptionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b53a1d7654ab253ef322d5aaa00ef3c7b70301e4abe429e8f48779118b20214(
    *,
    job_bookmarks_encryption_mode: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67ce5f76883b1039f240fd048a55ad06c44c08bb06b2064044add8b05be50eb8(
    *,
    kms_key_arn: typing.Optional[builtins.str] = None,
    s3_encryption_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5cc25b086c49f8ea0218f40bb10d196be50cfd3ed39b43b3782a73ab6215552(
    *,
    encryption_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityConfiguration.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63721068e81107cadbf3e418ec393de98f88a141604f2bb1044b5ae302e922ad(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    catalog_id: builtins.str,
    database_name: builtins.str,
    table_input: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.TableInputProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19801c3c5af0f333bf6e5e99c3031543e54a8cf3b68bccf6cc457fd27b0f044e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93805e92164ccafb607348423ac63ddda887c45f7d48102bc24275f7c7e179ed(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1518e6f292d33421716de5a7971329e9e9458a0245c61bae2b6f6d4dc066edb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3fa952b72d41b65e2c9a7ed9081c9236064d05e026dd37d5608da4cae676e88(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9200a2bfb582a6d400aba47da5ed4d77a8ca52ee0956131ca52cdc58253cb811(
    value: typing.Union[_IResolvable_da3f097b, CfnTable.TableInputProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__341bb786dd6f598e8fcaf71f90ff3da761cc3d8304f5ad4f6619ba17f44144aa(
    *,
    name: builtins.str,
    comment: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ef4b90841abfe4615325735c716d9eaa2a8839a68d0c4650f1bb4275935dfa1(
    *,
    column: builtins.str,
    sort_order: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__213074459ce3731da4f39ec028b3a7336f7b03aa4c9acead9a5d83aab68dd299(
    *,
    registry_name: typing.Optional[builtins.str] = None,
    schema_arn: typing.Optional[builtins.str] = None,
    schema_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6f714e7fb5c6d7bfdf385116f7f3dbd2eceb979753572daea288d033fe34254(
    *,
    schema_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.SchemaIdProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    schema_version_id: typing.Optional[builtins.str] = None,
    schema_version_number: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7540ba85e270907160df5e52f6d2f15874b400f181d969a4c9106d88b8081d5(
    *,
    name: typing.Optional[builtins.str] = None,
    parameters: typing.Any = None,
    serialization_library: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74aa76421b217af4a6e44cf71728cfad7a6ee7c23170fcb750c074e1a95d2616(
    *,
    skewed_column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    skewed_column_value_location_maps: typing.Any = None,
    skewed_column_values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95dc40dfb9eed01d30a631a9ddab00c9a5d1b2a3111b03046997bd45a3a28100(
    *,
    bucket_columns: typing.Optional[typing.Sequence[builtins.str]] = None,
    columns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.ColumnProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    compressed: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    input_format: typing.Optional[builtins.str] = None,
    location: typing.Optional[builtins.str] = None,
    number_of_buckets: typing.Optional[jsii.Number] = None,
    output_format: typing.Optional[builtins.str] = None,
    parameters: typing.Any = None,
    schema_reference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.SchemaReferenceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    serde_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.SerdeInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    skewed_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.SkewedInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sort_columns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.OrderProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    stored_as_sub_directories: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd9fe33086eb487e31769dc922bd060b39cb7e1a4f01a8e8bfa04311b57918e5(
    *,
    catalog_id: typing.Optional[builtins.str] = None,
    database_name: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cd7cfcabe0becfeb1771268e35d45d44b6f88db622d180509f833411ccf0096(
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    owner: typing.Optional[builtins.str] = None,
    parameters: typing.Any = None,
    partition_keys: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.ColumnProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    retention: typing.Optional[jsii.Number] = None,
    storage_descriptor: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.StorageDescriptorProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    table_type: typing.Optional[builtins.str] = None,
    target_table: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.TableIdentifierProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    view_expanded_text: typing.Optional[builtins.str] = None,
    view_original_text: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fa7a95b739eec87307cf104cf3e05eef39d32fd60cc53851b43bd980ef557e0(
    *,
    catalog_id: builtins.str,
    database_name: builtins.str,
    table_input: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.TableInputProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8db15edfea6b1fa74e017c6bb7603bed442e4f78f4c3c138f4dcc562cc8030ae(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    actions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrigger.ActionProperty, typing.Dict[builtins.str, typing.Any]]]]],
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    event_batching_condition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrigger.EventBatchingConditionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    predicate: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrigger.PredicateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    schedule: typing.Optional[builtins.str] = None,
    start_on_creation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Any = None,
    workflow_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0eaa05c4b1b14e1818059890f7eb0ac7a86490e54a9132ffd1b4d9178ea5d849(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7feee79b38582fea07a55bfd3425e4cc1f74b6e95e460a2a3f07af8648b09408(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53d40032b3434d3f5e99c83dacf150ee68e626c8b767443757082d57b51f20e4(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTrigger.ActionProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c40487beec9ee28746c40fb85d90ed73d85349d2b1310591566c8a389d11491(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a076c3439af46ca0fd80eee9d6b5b51664f94b7328360e3909babe56dec9a68(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__194582de5e8e5febbe9a4cbc4a1e55c5a1e16e7befac99be36a1217527cc1b08(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTrigger.EventBatchingConditionProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c195c948ebb78674c5a524b87ee0245a04d0f596e0a692d1eb19ef4e9c11d00a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89999604a37adfda2b629e7c87daa4774ff7b411d1a7dd82765ddaea3e8db560(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTrigger.PredicateProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__619711c62d98e25126265055c5714cbf3e2603579cec35909c8ddac5c1ec55f5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68315158d369a16e86c793787be78f9303c715936ab11872da4b50150509337c(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b0b45c89e6532f144a9dfed7dc674b60a42cbe0a87f33d0c9422d7ae3603da7(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf30f6c51932d46e70bffc0458c6c0fb8cb8525d3df1b7d576068ebaddc0e640(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__447a682fdfeec31ab40716697e095ee0c352e04c8ce1613acdeea726195c5ddf(
    *,
    arguments: typing.Any = None,
    crawler_name: typing.Optional[builtins.str] = None,
    job_name: typing.Optional[builtins.str] = None,
    notification_property: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrigger.NotificationPropertyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    security_configuration: typing.Optional[builtins.str] = None,
    timeout: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ada6798ea699e13790200a1ce7e2ca63bd7eb26d5c745fb9ad03c6a5fe653c70(
    *,
    crawler_name: typing.Optional[builtins.str] = None,
    crawl_state: typing.Optional[builtins.str] = None,
    job_name: typing.Optional[builtins.str] = None,
    logical_operator: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ace5e9c479229705a32735a5104d72eb05ba1dc95f28ce3ecae1b4f0d5591681(
    *,
    batch_size: jsii.Number,
    batch_window: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dba53ce68e34fb74bdafe21cd27a275d4fc3658f9a966098739aadba8f14d8a(
    *,
    notify_delay_after: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a59467c007dcc8cafa31e77259eebd72b608f9b3a0d7bb269217aba9a34fdcd8(
    *,
    conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrigger.ConditionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    logical: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__784653657e04e37fef0f1a1cad2dd3968ecec5929ea90e9d792e16ce48fec46e(
    *,
    actions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrigger.ActionProperty, typing.Dict[builtins.str, typing.Any]]]]],
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    event_batching_condition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrigger.EventBatchingConditionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    predicate: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrigger.PredicateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    schedule: typing.Optional[builtins.str] = None,
    start_on_creation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Any = None,
    workflow_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6c744c641379ecc5fd54ce4fcbe0501c332b7726b6037690528980d8b6c8f33(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    default_run_properties: typing.Any = None,
    description: typing.Optional[builtins.str] = None,
    max_concurrent_runs: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ccd23d031aa65b14694ae7bcf464a4c55d4ce28e67cc115e5a3a9b916b37323(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bddbab3355f6eba94edc925da3c1a12b170435872bf1671a9d9951649478274(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44dfd2cb43609bdf14cd367fdb19e4b1ca604d3264c983f445f606fe9e35818f(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__111cdaa83ed7e77873f89337e876aecddb9e6d748ce7b22cd537261bb2c0040e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41a06b4a8c873f8b95edfbe239c7699899e5c1a8a74755383d7c6c587b34c348(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e19cad13834aa6cc47e532030a314d08f3c215dfcce008b2e0227db3d71718e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__588bdefa1fb0e0005b05a203dd64a0a1b8395bced0853eefec4b1943820f9259(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2fbf58b972f40f14f50a92e85a2c44b7714f052d44776dc875496359365c5db(
    *,
    default_run_properties: typing.Any = None,
    description: typing.Optional[builtins.str] = None,
    max_concurrent_runs: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass
