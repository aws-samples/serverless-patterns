'''
# AWS WAF Regional Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_wafregional as wafregional
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for WAFRegional construct libraries](https://constructs.dev/search?q=wafregional)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::WAFRegional resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_WAFRegional.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::WAFRegional](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_WAFRegional.html).

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
class CfnByteMatchSet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_wafregional.CfnByteMatchSet",
):
    '''.. epigraph::

   This is *AWS WAF Classic* documentation.

    For more information, see `AWS WAF Classic <https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html>`_ in the developer guide.
    .. epigraph::

       *For the latest version of AWS WAF* , use the AWS WAF V2 API and see the `AWS WAF Developer Guide <https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html>`_ . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

    The ``AWS::WAFRegional::ByteMatchSet`` resource creates an AWS WAF ``ByteMatchSet`` that identifies a part of a web request that you want to inspect.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-bytematchset.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_wafregional as wafregional
        
        cfn_byte_match_set = wafregional.CfnByteMatchSet(self, "MyCfnByteMatchSet",
            name="name",
        
            # the properties below are optional
            byte_match_tuples=[wafregional.CfnByteMatchSet.ByteMatchTupleProperty(
                field_to_match=wafregional.CfnByteMatchSet.FieldToMatchProperty(
                    type="type",
        
                    # the properties below are optional
                    data="data"
                ),
                positional_constraint="positionalConstraint",
                text_transformation="textTransformation",
        
                # the properties below are optional
                target_string="targetString",
                target_string_base64="targetStringBase64"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        byte_match_tuples: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnByteMatchSet.ByteMatchTupleProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: A friendly name or description of the ``ByteMatchSet`` . You can't change ``Name`` after you create a ``ByteMatchSet`` .
        :param byte_match_tuples: Specifies the bytes (typically a string that corresponds with ASCII characters) that you want AWS WAF to search for in web requests, the location in requests that you want AWS WAF to search, and other settings.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e708169d746906ecd9d668a57583fd77b92049101a7b42aaf2d48555f189e6e8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnByteMatchSetProps(name=name, byte_match_tuples=byte_match_tuples)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea460cfe61ff551d95ffb61ada21b904430d986ea13f30d0c4b789ed5946b4cd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e7f70a1150cc6a5ccbb4a8525c046cb151ebfcef8d6e8610d8822dd25b44909d)
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
        '''A friendly name or description of the ``ByteMatchSet`` .'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e3fd8c2f928a54bc15ca33b7b11d1b205815279375aa299a6e66e53c81a69d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="byteMatchTuples")
    def byte_match_tuples(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnByteMatchSet.ByteMatchTupleProperty"]]]]:
        '''Specifies the bytes (typically a string that corresponds with ASCII characters) that you want AWS WAF to search for in web requests, the location in requests that you want AWS WAF to search, and other settings.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnByteMatchSet.ByteMatchTupleProperty"]]]], jsii.get(self, "byteMatchTuples"))

    @byte_match_tuples.setter
    def byte_match_tuples(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnByteMatchSet.ByteMatchTupleProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3bdd0c3bf2f1a3268342f199ac37f3c9d3704be0bf88f0b85a5b4fac81294cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "byteMatchTuples", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wafregional.CfnByteMatchSet.ByteMatchTupleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "field_to_match": "fieldToMatch",
            "positional_constraint": "positionalConstraint",
            "text_transformation": "textTransformation",
            "target_string": "targetString",
            "target_string_base64": "targetStringBase64",
        },
    )
    class ByteMatchTupleProperty:
        def __init__(
            self,
            *,
            field_to_match: typing.Union[_IResolvable_da3f097b, typing.Union["CfnByteMatchSet.FieldToMatchProperty", typing.Dict[builtins.str, typing.Any]]],
            positional_constraint: builtins.str,
            text_transformation: builtins.str,
            target_string: typing.Optional[builtins.str] = None,
            target_string_base64: typing.Optional[builtins.str] = None,
        ) -> None:
            '''.. epigraph::

   This is *AWS WAF Classic* documentation.

            For more information, see `AWS WAF Classic <https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html>`_ in the developer guide.
            .. epigraph::

               *For the latest version of AWS WAF* , use the AWS WAF V2 API and see the `AWS WAF Developer Guide <https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html>`_ . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

            The bytes (typically a string that corresponds with ASCII characters) that you want AWS WAF to search for in web requests, the location in requests that you want AWS WAF to search, and other settings.

            :param field_to_match: The part of a web request that you want AWS WAF to inspect, such as a specific header or a query string.
            :param positional_constraint: Within the portion of a web request that you want to search (for example, in the query string, if any), specify where you want AWS WAF to search. Valid values include the following: *CONTAINS* The specified part of the web request must include the value of ``TargetString`` , but the location doesn't matter. *CONTAINS_WORD* The specified part of the web request must include the value of ``TargetString`` , and ``TargetString`` must contain only alphanumeric characters or underscore (A-Z, a-z, 0-9, or _). In addition, ``TargetString`` must be a word, which means one of the following: - ``TargetString`` exactly matches the value of the specified part of the web request, such as the value of a header. - ``TargetString`` is at the beginning of the specified part of the web request and is followed by a character other than an alphanumeric character or underscore (_), for example, ``BadBot;`` . - ``TargetString`` is at the end of the specified part of the web request and is preceded by a character other than an alphanumeric character or underscore (_), for example, ``;BadBot`` . - ``TargetString`` is in the middle of the specified part of the web request and is preceded and followed by characters other than alphanumeric characters or underscore (_), for example, ``-BadBot;`` . *EXACTLY* The value of the specified part of the web request must exactly match the value of ``TargetString`` . *STARTS_WITH* The value of ``TargetString`` must appear at the beginning of the specified part of the web request. *ENDS_WITH* The value of ``TargetString`` must appear at the end of the specified part of the web request.
            :param text_transformation: Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF . If you specify a transformation, AWS WAF performs the transformation on ``FieldToMatch`` before inspecting it for a match. You can only specify a single type of TextTransformation. *CMD_LINE* When you're concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations: - Delete the following characters: \\ " ' ^ - Delete spaces before the following characters: / ( - Replace the following characters with a space: , ; - Replace multiple spaces with one space - Convert uppercase letters (A-Z) to lowercase (a-z) *COMPRESS_WHITE_SPACE* Use this option to replace the following characters with a space character (decimal 32): - \\f, formfeed, decimal 12 - \\t, tab, decimal 9 - \\n, newline, decimal 10 - \\r, carriage return, decimal 13 - \\v, vertical tab, decimal 11 - non-breaking space, decimal 160 ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space. *HTML_ENTITY_DECODE* Use this option to replace HTML-encoded characters with unencoded characters. ``HTML_ENTITY_DECODE`` performs the following operations: - Replaces ``(ampersand)quot;`` with ``"`` - Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160 - Replaces ``(ampersand)lt;`` with a "less than" symbol - Replaces ``(ampersand)gt;`` with ``>`` - Replaces characters that are represented in hexadecimal format, ``(ampersand)#xhhhh;`` , with the corresponding characters - Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` , with the corresponding characters *LOWERCASE* Use this option to convert uppercase letters (A-Z) to lowercase (a-z). *URL_DECODE* Use this option to decode a URL-encoded value. *NONE* Specify ``NONE`` if you don't want to perform any text transformations.
            :param target_string: The value that you want AWS WAF to search for. AWS WAF searches for the specified string in the part of web requests that you specified in ``FieldToMatch`` . The maximum length of the value is 50 bytes. You must specify this property or the ``TargetStringBase64`` property. Valid values depend on the values that you specified for ``FieldToMatch`` : - ``HEADER`` : The value that you want AWS WAF to search for in the request header that you specified in ``FieldToMatch`` , for example, the value of the ``User-Agent`` or ``Referer`` header. - ``METHOD`` : The HTTP method, which indicates the type of operation specified in the request. - ``QUERY_STRING`` : The value that you want AWS WAF to search for in the query string, which is the part of a URL that appears after a ``?`` character. - ``URI`` : The value that you want AWS WAF to search for in the part of a URL that identifies a resource, for example, ``/images/daily-ad.jpg`` . - ``BODY`` : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. - ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30 characters. - ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but instead of inspecting a single parameter, AWS WAF inspects all parameters within the query string for the value or regex pattern that you specify in ``TargetString`` . If ``TargetString`` includes alphabetic characters A-Z and a-z, note that the value is case sensitive.
            :param target_string_base64: The base64-encoded value that AWS WAF searches for. AWS CloudFormation sends this value to AWS WAF without encoding it. You must specify this property or the ``TargetString`` property. AWS WAF searches for this value in a specific part of web requests, which you define in the ``FieldToMatch`` property. Valid values depend on the Type value in the ``FieldToMatch`` property. For example, for a ``METHOD`` type, you must specify HTTP methods such as ``DELETE, GET, HEAD, OPTIONS, PATCH, POST`` , and ``PUT`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wafregional as wafregional
                
                byte_match_tuple_property = wafregional.CfnByteMatchSet.ByteMatchTupleProperty(
                    field_to_match=wafregional.CfnByteMatchSet.FieldToMatchProperty(
                        type="type",
                
                        # the properties below are optional
                        data="data"
                    ),
                    positional_constraint="positionalConstraint",
                    text_transformation="textTransformation",
                
                    # the properties below are optional
                    target_string="targetString",
                    target_string_base64="targetStringBase64"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9e44b397423d4132bd5d65f37916270d0ba93f2dc8760e37e7d32874c2346364)
                check_type(argname="argument field_to_match", value=field_to_match, expected_type=type_hints["field_to_match"])
                check_type(argname="argument positional_constraint", value=positional_constraint, expected_type=type_hints["positional_constraint"])
                check_type(argname="argument text_transformation", value=text_transformation, expected_type=type_hints["text_transformation"])
                check_type(argname="argument target_string", value=target_string, expected_type=type_hints["target_string"])
                check_type(argname="argument target_string_base64", value=target_string_base64, expected_type=type_hints["target_string_base64"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "field_to_match": field_to_match,
                "positional_constraint": positional_constraint,
                "text_transformation": text_transformation,
            }
            if target_string is not None:
                self._values["target_string"] = target_string
            if target_string_base64 is not None:
                self._values["target_string_base64"] = target_string_base64

        @builtins.property
        def field_to_match(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnByteMatchSet.FieldToMatchProperty"]:
            '''The part of a web request that you want AWS WAF to inspect, such as a specific header or a query string.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html#cfn-wafregional-bytematchset-bytematchtuple-fieldtomatch
            '''
            result = self._values.get("field_to_match")
            assert result is not None, "Required property 'field_to_match' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnByteMatchSet.FieldToMatchProperty"], result)

        @builtins.property
        def positional_constraint(self) -> builtins.str:
            '''Within the portion of a web request that you want to search (for example, in the query string, if any), specify where you want AWS WAF to search.

            Valid values include the following:

            *CONTAINS*

            The specified part of the web request must include the value of ``TargetString`` , but the location doesn't matter.

            *CONTAINS_WORD*

            The specified part of the web request must include the value of ``TargetString`` , and ``TargetString`` must contain only alphanumeric characters or underscore (A-Z, a-z, 0-9, or _). In addition, ``TargetString`` must be a word, which means one of the following:

            - ``TargetString`` exactly matches the value of the specified part of the web request, such as the value of a header.
            - ``TargetString`` is at the beginning of the specified part of the web request and is followed by a character other than an alphanumeric character or underscore (_), for example, ``BadBot;`` .
            - ``TargetString`` is at the end of the specified part of the web request and is preceded by a character other than an alphanumeric character or underscore (_), for example, ``;BadBot`` .
            - ``TargetString`` is in the middle of the specified part of the web request and is preceded and followed by characters other than alphanumeric characters or underscore (_), for example, ``-BadBot;`` .

            *EXACTLY*

            The value of the specified part of the web request must exactly match the value of ``TargetString`` .

            *STARTS_WITH*

            The value of ``TargetString`` must appear at the beginning of the specified part of the web request.

            *ENDS_WITH*

            The value of ``TargetString`` must appear at the end of the specified part of the web request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html#cfn-wafregional-bytematchset-bytematchtuple-positionalconstraint
            '''
            result = self._values.get("positional_constraint")
            assert result is not None, "Required property 'positional_constraint' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def text_transformation(self) -> builtins.str:
            '''Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF .

            If you specify a transformation, AWS WAF performs the transformation on ``FieldToMatch`` before inspecting it for a match.

            You can only specify a single type of TextTransformation.

            *CMD_LINE*

            When you're concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

            - Delete the following characters: \\ " ' ^
            - Delete spaces before the following characters: / (
            - Replace the following characters with a space: , ;
            - Replace multiple spaces with one space
            - Convert uppercase letters (A-Z) to lowercase (a-z)

            *COMPRESS_WHITE_SPACE*

            Use this option to replace the following characters with a space character (decimal 32):

            - \\f, formfeed, decimal 12
            - \\t, tab, decimal 9
            - \\n, newline, decimal 10
            - \\r, carriage return, decimal 13
            - \\v, vertical tab, decimal 11
            - non-breaking space, decimal 160

            ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

            *HTML_ENTITY_DECODE*

            Use this option to replace HTML-encoded characters with unencoded characters. ``HTML_ENTITY_DECODE`` performs the following operations:

            - Replaces ``(ampersand)quot;`` with ``"``
            - Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160
            - Replaces ``(ampersand)lt;`` with a "less than" symbol
            - Replaces ``(ampersand)gt;`` with ``>``
            - Replaces characters that are represented in hexadecimal format, ``(ampersand)#xhhhh;`` , with the corresponding characters
            - Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` , with the corresponding characters

            *LOWERCASE*

            Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

            *URL_DECODE*

            Use this option to decode a URL-encoded value.

            *NONE*

            Specify ``NONE`` if you don't want to perform any text transformations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html#cfn-wafregional-bytematchset-bytematchtuple-texttransformation
            '''
            result = self._values.get("text_transformation")
            assert result is not None, "Required property 'text_transformation' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def target_string(self) -> typing.Optional[builtins.str]:
            '''The value that you want AWS WAF to search for.

            AWS WAF searches for the specified string in the part of web requests that you specified in ``FieldToMatch`` . The maximum length of the value is 50 bytes.

            You must specify this property or the ``TargetStringBase64`` property.

            Valid values depend on the values that you specified for ``FieldToMatch`` :

            - ``HEADER`` : The value that you want AWS WAF to search for in the request header that you specified in ``FieldToMatch`` , for example, the value of the ``User-Agent`` or ``Referer`` header.
            - ``METHOD`` : The HTTP method, which indicates the type of operation specified in the request.
            - ``QUERY_STRING`` : The value that you want AWS WAF to search for in the query string, which is the part of a URL that appears after a ``?`` character.
            - ``URI`` : The value that you want AWS WAF to search for in the part of a URL that identifies a resource, for example, ``/images/daily-ad.jpg`` .
            - ``BODY`` : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set.
            - ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30 characters.
            - ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but instead of inspecting a single parameter, AWS WAF inspects all parameters within the query string for the value or regex pattern that you specify in ``TargetString`` .

            If ``TargetString`` includes alphabetic characters A-Z and a-z, note that the value is case sensitive.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html#cfn-wafregional-bytematchset-bytematchtuple-targetstring
            '''
            result = self._values.get("target_string")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_string_base64(self) -> typing.Optional[builtins.str]:
            '''The base64-encoded value that AWS WAF searches for. AWS CloudFormation sends this value to AWS WAF without encoding it.

            You must specify this property or the ``TargetString`` property.

            AWS WAF searches for this value in a specific part of web requests, which you define in the ``FieldToMatch`` property.

            Valid values depend on the Type value in the ``FieldToMatch`` property. For example, for a ``METHOD`` type, you must specify HTTP methods such as ``DELETE, GET, HEAD, OPTIONS, PATCH, POST`` , and ``PUT`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html#cfn-wafregional-bytematchset-bytematchtuple-targetstringbase64
            '''
            result = self._values.get("target_string_base64")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ByteMatchTupleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wafregional.CfnByteMatchSet.FieldToMatchProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "data": "data"},
    )
    class FieldToMatchProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            data: typing.Optional[builtins.str] = None,
        ) -> None:
            '''.. epigraph::

   This is *AWS WAF Classic* documentation.

            For more information, see `AWS WAF Classic <https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html>`_ in the developer guide.
            .. epigraph::

               *For the latest version of AWS WAF* , use the AWS WAF V2 API and see the `AWS WAF Developer Guide <https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html>`_ . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

            Specifies where in a web request to look for ``TargetString`` .

            :param type: The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following: - ``HEADER`` : A specified request header, for example, the value of the ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the header in ``Data`` . - ``METHOD`` : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. - ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a ``?`` character, if any. - ``URI`` : The part of a web request that identifies a resource, for example, ``/images/daily-ad.jpg`` . - ``BODY`` : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. - ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30 characters. - ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in ``TargetString`` .
            :param data: When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the header is not case sensitive. When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The parameter name is not case sensitive. If the value of ``Type`` is any other value, omit ``Data`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-fieldtomatch.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wafregional as wafregional
                
                field_to_match_property = wafregional.CfnByteMatchSet.FieldToMatchProperty(
                    type="type",
                
                    # the properties below are optional
                    data="data"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__640c9a931daf57d6d8a41f83df9bd8de256aec1220f1b860b3316bd9134494d2)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if data is not None:
                self._values["data"] = data

        @builtins.property
        def type(self) -> builtins.str:
            '''The part of the web request that you want AWS WAF to search for a specified string.

            Parts of a request that you can search include the following:

            - ``HEADER`` : A specified request header, for example, the value of the ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the header in ``Data`` .
            - ``METHOD`` : The HTTP method, which indicated the type of operation that the request is asking the origin to perform.
            - ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a ``?`` character, if any.
            - ``URI`` : The part of a web request that identifies a resource, for example, ``/images/daily-ad.jpg`` .
            - ``BODY`` : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set.
            - ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30 characters.
            - ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in ``TargetString`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-fieldtomatch.html#cfn-wafregional-bytematchset-fieldtomatch-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def data(self) -> typing.Optional[builtins.str]:
            '''When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS WAF to search, for example, ``User-Agent`` or ``Referer`` .

            The name of the header is not case sensitive.

            When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The parameter name is not case sensitive.

            If the value of ``Type`` is any other value, omit ``Data`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-fieldtomatch.html#cfn-wafregional-bytematchset-fieldtomatch-data
            '''
            result = self._values.get("data")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FieldToMatchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_wafregional.CfnByteMatchSetProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "byte_match_tuples": "byteMatchTuples"},
)
class CfnByteMatchSetProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        byte_match_tuples: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnByteMatchSet.ByteMatchTupleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnByteMatchSet``.

        :param name: A friendly name or description of the ``ByteMatchSet`` . You can't change ``Name`` after you create a ``ByteMatchSet`` .
        :param byte_match_tuples: Specifies the bytes (typically a string that corresponds with ASCII characters) that you want AWS WAF to search for in web requests, the location in requests that you want AWS WAF to search, and other settings.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-bytematchset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_wafregional as wafregional
            
            cfn_byte_match_set_props = wafregional.CfnByteMatchSetProps(
                name="name",
            
                # the properties below are optional
                byte_match_tuples=[wafregional.CfnByteMatchSet.ByteMatchTupleProperty(
                    field_to_match=wafregional.CfnByteMatchSet.FieldToMatchProperty(
                        type="type",
            
                        # the properties below are optional
                        data="data"
                    ),
                    positional_constraint="positionalConstraint",
                    text_transformation="textTransformation",
            
                    # the properties below are optional
                    target_string="targetString",
                    target_string_base64="targetStringBase64"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d3315ca0f0c432ea54dc0a28b013ee804e72f866e20f3164467df22a3679b29)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument byte_match_tuples", value=byte_match_tuples, expected_type=type_hints["byte_match_tuples"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if byte_match_tuples is not None:
            self._values["byte_match_tuples"] = byte_match_tuples

    @builtins.property
    def name(self) -> builtins.str:
        '''A friendly name or description of the ``ByteMatchSet`` .

        You can't change ``Name`` after you create a ``ByteMatchSet`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-bytematchset.html#cfn-wafregional-bytematchset-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def byte_match_tuples(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnByteMatchSet.ByteMatchTupleProperty]]]]:
        '''Specifies the bytes (typically a string that corresponds with ASCII characters) that you want AWS WAF to search for in web requests, the location in requests that you want AWS WAF to search, and other settings.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-bytematchset.html#cfn-wafregional-bytematchset-bytematchtuples
        '''
        result = self._values.get("byte_match_tuples")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnByteMatchSet.ByteMatchTupleProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnByteMatchSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnGeoMatchSet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_wafregional.CfnGeoMatchSet",
):
    '''.. epigraph::

   This is *AWS WAF Classic* documentation.

    For more information, see `AWS WAF Classic <https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html>`_ in the developer guide.
    .. epigraph::

       *For the latest version of AWS WAF* , use the AWS WAF V2 API and see the `AWS WAF Developer Guide <https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html>`_ . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

    Contains one or more countries that AWS WAF will search for.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-geomatchset.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_wafregional as wafregional
        
        cfn_geo_match_set = wafregional.CfnGeoMatchSet(self, "MyCfnGeoMatchSet",
            name="name",
        
            # the properties below are optional
            geo_match_constraints=[wafregional.CfnGeoMatchSet.GeoMatchConstraintProperty(
                type="type",
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
        geo_match_constraints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGeoMatchSet.GeoMatchConstraintProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: A friendly name or description of the ``GeoMatchSet`` . You can't change the name of an ``GeoMatchSet`` after you create it.
        :param geo_match_constraints: An array of ``GeoMatchConstraint`` objects, which contain the country that you want AWS WAF to search for.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f5defa886ad07662ce07608ef11d4f182985ba3ca56ba02873d46b5f8629b43)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGeoMatchSetProps(
            name=name, geo_match_constraints=geo_match_constraints
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f6bafffd0f7b74cee5606a2d95f943cc5ac49a2560960db6fdfdb298b40f982)
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
            type_hints = typing.get_type_hints(_typecheckingstub__65322f9d0fd5be8dfe4ab1e62760ccd49f6559e244979e10e7e0ac91c5761924)
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
        '''A friendly name or description of the ``GeoMatchSet`` .'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd355eff3f62f2152cd03e0b7ce0da682ff29432c59a743bb4a649626c9c2af7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="geoMatchConstraints")
    def geo_match_constraints(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGeoMatchSet.GeoMatchConstraintProperty"]]]]:
        '''An array of ``GeoMatchConstraint`` objects, which contain the country that you want AWS WAF to search for.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGeoMatchSet.GeoMatchConstraintProperty"]]]], jsii.get(self, "geoMatchConstraints"))

    @geo_match_constraints.setter
    def geo_match_constraints(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGeoMatchSet.GeoMatchConstraintProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64d21a9e81545c51476c160c33fa317b6908f4f1b44d7a03d47b22d5bd55391e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "geoMatchConstraints", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wafregional.CfnGeoMatchSet.GeoMatchConstraintProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "value": "value"},
    )
    class GeoMatchConstraintProperty:
        def __init__(self, *, type: builtins.str, value: builtins.str) -> None:
            '''.. epigraph::

   This is *AWS WAF Classic* documentation.

            For more information, see `AWS WAF Classic <https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html>`_ in the developer guide.
            .. epigraph::

               *For the latest version of AWS WAF* , use the AWS WAF V2 API and see the `AWS WAF Developer Guide <https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html>`_ . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

            The country from which web requests originate that you want AWS WAF to search for.

            :param type: The type of geographical area you want AWS WAF to search for. Currently ``Country`` is the only valid value.
            :param value: The country that you want AWS WAF to search for.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-geomatchset-geomatchconstraint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wafregional as wafregional
                
                geo_match_constraint_property = wafregional.CfnGeoMatchSet.GeoMatchConstraintProperty(
                    type="type",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bdccc52297904d6ff0d4704e82129d56f752a9d570c4f100e64bb95fbde18278)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
                "value": value,
            }

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of geographical area you want AWS WAF to search for.

            Currently ``Country`` is the only valid value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-geomatchset-geomatchconstraint.html#cfn-wafregional-geomatchset-geomatchconstraint-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The country that you want AWS WAF to search for.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-geomatchset-geomatchconstraint.html#cfn-wafregional-geomatchset-geomatchconstraint-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GeoMatchConstraintProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_wafregional.CfnGeoMatchSetProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "geo_match_constraints": "geoMatchConstraints"},
)
class CfnGeoMatchSetProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        geo_match_constraints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGeoMatchSet.GeoMatchConstraintProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnGeoMatchSet``.

        :param name: A friendly name or description of the ``GeoMatchSet`` . You can't change the name of an ``GeoMatchSet`` after you create it.
        :param geo_match_constraints: An array of ``GeoMatchConstraint`` objects, which contain the country that you want AWS WAF to search for.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-geomatchset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_wafregional as wafregional
            
            cfn_geo_match_set_props = wafregional.CfnGeoMatchSetProps(
                name="name",
            
                # the properties below are optional
                geo_match_constraints=[wafregional.CfnGeoMatchSet.GeoMatchConstraintProperty(
                    type="type",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ce26d9ffd24f477f686b44477cc2e54588d1ce675a04c4e2970b3226c84d38e)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument geo_match_constraints", value=geo_match_constraints, expected_type=type_hints["geo_match_constraints"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if geo_match_constraints is not None:
            self._values["geo_match_constraints"] = geo_match_constraints

    @builtins.property
    def name(self) -> builtins.str:
        '''A friendly name or description of the ``GeoMatchSet`` .

        You can't change the name of an ``GeoMatchSet`` after you create it.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-geomatchset.html#cfn-wafregional-geomatchset-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def geo_match_constraints(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGeoMatchSet.GeoMatchConstraintProperty]]]]:
        '''An array of ``GeoMatchConstraint`` objects, which contain the country that you want AWS WAF to search for.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-geomatchset.html#cfn-wafregional-geomatchset-geomatchconstraints
        '''
        result = self._values.get("geo_match_constraints")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGeoMatchSet.GeoMatchConstraintProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGeoMatchSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnIPSet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_wafregional.CfnIPSet",
):
    '''.. epigraph::

   This is *AWS WAF Classic* documentation.

    For more information, see `AWS WAF Classic <https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html>`_ in the developer guide.
    .. epigraph::

       *For the latest version of AWS WAF* , use the AWS WAF V2 API and see the `AWS WAF Developer Guide <https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html>`_ . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

    Contains one or more IP addresses or blocks of IP addresses specified in Classless Inter-Domain Routing (CIDR) notation. AWS WAF supports IPv4 address ranges: /8 and any range between /16 through /32. AWS WAF supports IPv6 address ranges: /24, /32, /48, /56, /64, and /128.

    To specify an individual IP address, you specify the four-part IP address followed by a ``/32`` , for example, 192.0.2.0/32. To block a range of IP addresses, you can specify /8 or any range between /16 through /32 (for IPv4) or /24, /32, /48, /56, /64, or /128 (for IPv6). For more information about CIDR notation, see the Wikipedia entry `Classless Inter-Domain Routing <https://docs.aws.amazon.com/https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ipset.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_wafregional as wafregional
        
        cfn_iPSet = wafregional.CfnIPSet(self, "MyCfnIPSet",
            name="name",
        
            # the properties below are optional
            ip_set_descriptors=[{
                "type": "type",
                "value": "value"
            }]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        ip_set_descriptors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIPSet.IPSetDescriptorProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: A friendly name or description of the ``IPSet`` . You can't change the name of an ``IPSet`` after you create it.
        :param ip_set_descriptors: The IP address type ( ``IPV4`` or ``IPV6`` ) and the IP address range (in CIDR notation) that web requests originate from.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24af5fe749b4ec99d6661f61836984c1ee1ea8f65bfb2e1309de62e8148e8adf)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnIPSetProps(name=name, ip_set_descriptors=ip_set_descriptors)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e517874a1630bb2cdf2cae335ebbaa598305f5e5f1f4904a234e310e13f7e33e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5e59cc971a79420af060d720f9dab45125bdab1f1d161d6fd0212288059240ea)
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
        '''A friendly name or description of the ``IPSet`` .'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e8d9bc40ccea4e69d11cc36300ed6e414f959745336a30e2f40940cc8f4efe2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="ipSetDescriptors")
    def ip_set_descriptors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnIPSet.IPSetDescriptorProperty"]]]]:
        '''The IP address type ( ``IPV4`` or ``IPV6`` ) and the IP address range (in CIDR notation) that web requests originate from.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnIPSet.IPSetDescriptorProperty"]]]], jsii.get(self, "ipSetDescriptors"))

    @ip_set_descriptors.setter
    def ip_set_descriptors(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnIPSet.IPSetDescriptorProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6d42c2bbdf2fdfd5f1729c0ee8fa6b528f0ec97e34d0bccd32a470e817f41f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipSetDescriptors", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wafregional.CfnIPSet.IPSetDescriptorProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "value": "value"},
    )
    class IPSetDescriptorProperty:
        def __init__(self, *, type: builtins.str, value: builtins.str) -> None:
            '''.. epigraph::

   This is *AWS WAF Classic* documentation.

            For more information, see `AWS WAF Classic <https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html>`_ in the developer guide.
            .. epigraph::

               *For the latest version of AWS WAF* , use the AWS WAF V2 API and see the `AWS WAF Developer Guide <https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html>`_ . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

            Specifies the IP address type ( ``IPV4`` or ``IPV6`` ) and the IP address range (in CIDR format) that web requests originate from.

            :param type: Specify ``IPV4`` or ``IPV6`` .
            :param value: Specify an IPv4 address by using CIDR notation. For example:. - To configure AWS WAF to allow, block, or count requests that originated from the IP address 192.0.2.44, specify ``192.0.2.44/32`` . - To configure AWS WAF to allow, block, or count requests that originated from IP addresses from 192.0.2.0 to 192.0.2.255, specify ``192.0.2.0/24`` . For more information about CIDR notation, see the Wikipedia entry `Classless Inter-Domain Routing <https://docs.aws.amazon.com/https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`_ . Specify an IPv6 address by using CIDR notation. For example: - To configure AWS WAF to allow, block, or count requests that originated from the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify ``1111:0000:0000:0000:0000:0000:0000:0111/128`` . - To configure AWS WAF to allow, block, or count requests that originated from IP addresses 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify ``1111:0000:0000:0000:0000:0000:0000:0000/64`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ipset-ipsetdescriptor.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wafregional as wafregional
                
                i_pSet_descriptor_property = {
                    "type": "type",
                    "value": "value"
                }
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1fc3d521e61aad5c8ee04774898a6f73b99447c7fa553cc634602b002683f070)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
                "value": value,
            }

        @builtins.property
        def type(self) -> builtins.str:
            '''Specify ``IPV4`` or ``IPV6`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ipset-ipsetdescriptor.html#cfn-wafregional-ipset-ipsetdescriptor-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''Specify an IPv4 address by using CIDR notation. For example:.

            - To configure AWS WAF to allow, block, or count requests that originated from the IP address 192.0.2.44, specify ``192.0.2.44/32`` .
            - To configure AWS WAF to allow, block, or count requests that originated from IP addresses from 192.0.2.0 to 192.0.2.255, specify ``192.0.2.0/24`` .

            For more information about CIDR notation, see the Wikipedia entry `Classless Inter-Domain Routing <https://docs.aws.amazon.com/https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`_ .

            Specify an IPv6 address by using CIDR notation. For example:

            - To configure AWS WAF to allow, block, or count requests that originated from the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify ``1111:0000:0000:0000:0000:0000:0000:0111/128`` .
            - To configure AWS WAF to allow, block, or count requests that originated from IP addresses 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify ``1111:0000:0000:0000:0000:0000:0000:0000/64`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ipset-ipsetdescriptor.html#cfn-wafregional-ipset-ipsetdescriptor-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IPSetDescriptorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_wafregional.CfnIPSetProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "ip_set_descriptors": "ipSetDescriptors"},
)
class CfnIPSetProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        ip_set_descriptors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIPSet.IPSetDescriptorProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnIPSet``.

        :param name: A friendly name or description of the ``IPSet`` . You can't change the name of an ``IPSet`` after you create it.
        :param ip_set_descriptors: The IP address type ( ``IPV4`` or ``IPV6`` ) and the IP address range (in CIDR notation) that web requests originate from.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ipset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_wafregional as wafregional
            
            cfn_iPSet_props = wafregional.CfnIPSetProps(
                name="name",
            
                # the properties below are optional
                ip_set_descriptors=[{
                    "type": "type",
                    "value": "value"
                }]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66ca7761765b7ff9b3a37c94c1330ce44b8771049c38acc8da230f52e7db0708)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument ip_set_descriptors", value=ip_set_descriptors, expected_type=type_hints["ip_set_descriptors"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if ip_set_descriptors is not None:
            self._values["ip_set_descriptors"] = ip_set_descriptors

    @builtins.property
    def name(self) -> builtins.str:
        '''A friendly name or description of the ``IPSet`` .

        You can't change the name of an ``IPSet`` after you create it.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ipset.html#cfn-wafregional-ipset-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ip_set_descriptors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnIPSet.IPSetDescriptorProperty]]]]:
        '''The IP address type ( ``IPV4`` or ``IPV6`` ) and the IP address range (in CIDR notation) that web requests originate from.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ipset.html#cfn-wafregional-ipset-ipsetdescriptors
        '''
        result = self._values.get("ip_set_descriptors")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnIPSet.IPSetDescriptorProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnIPSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnRateBasedRule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_wafregional.CfnRateBasedRule",
):
    '''.. epigraph::

   This is *AWS WAF Classic* documentation.

    For more information, see `AWS WAF Classic <https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html>`_ in the developer guide.
    .. epigraph::

       *For the latest version of AWS WAF* , use the AWS WAF V2 API and see the `AWS WAF Developer Guide <https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html>`_ . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

    A ``RateBasedRule`` is identical to a regular ``Rule`` , with one addition: a ``RateBasedRule`` counts the number of requests that arrive from a specified IP address every five minutes. For example, based on recent requests that you've seen from an attacker, you might create a ``RateBasedRule`` that includes the following conditions:

    - The requests come from 192.0.2.44.
    - They contain the value ``BadBot`` in the ``User-Agent`` header.

    In the rule, you also define the rate limit as 15,000.

    Requests that meet both of these conditions and exceed 15,000 requests every five minutes trigger the rule's action (block or count), which is defined in the web ACL.

    Note you can only create rate-based rules using an AWS CloudFormation template. To add the rate-based rules created through AWS CloudFormation to a web ACL, use the AWS WAF console, API, or command line interface (CLI). For more information, see `UpdateWebACL <https://docs.aws.amazon.com/waf/latest/APIReference/API_regional_UpdateWebACL.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ratebasedrule.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_wafregional as wafregional
        
        cfn_rate_based_rule = wafregional.CfnRateBasedRule(self, "MyCfnRateBasedRule",
            metric_name="metricName",
            name="name",
            rate_key="rateKey",
            rate_limit=123,
        
            # the properties below are optional
            match_predicates=[wafregional.CfnRateBasedRule.PredicateProperty(
                data_id="dataId",
                negated=False,
                type="type"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        metric_name: builtins.str,
        name: builtins.str,
        rate_key: builtins.str,
        rate_limit: jsii.Number,
        match_predicates: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRateBasedRule.PredicateProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param metric_name: A name for the metrics for a ``RateBasedRule`` . The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can't contain whitespace or metric names reserved for AWS WAF , including "All" and "Default_Action." You can't change the name of the metric after you create the ``RateBasedRule`` .
        :param name: A friendly name or description for a ``RateBasedRule`` . You can't change the name of a ``RateBasedRule`` after you create it.
        :param rate_key: The field that AWS WAF uses to determine if requests are likely arriving from single source and thus subject to rate monitoring. The only valid value for ``RateKey`` is ``IP`` . ``IP`` indicates that requests arriving from the same IP address are subject to the ``RateLimit`` that is specified in the ``RateBasedRule`` .
        :param rate_limit: The maximum number of requests, which have an identical value in the field specified by the ``RateKey`` , allowed in a five-minute period. If the number of requests exceeds the ``RateLimit`` and the other predicates specified in the rule are also met, AWS WAF triggers the action that is specified for this rule.
        :param match_predicates: The ``Predicates`` object contains one ``Predicate`` element for each ``ByteMatchSet`` , ``IPSet`` , or ``SqlInjectionMatchSet>`` object that you want to include in a ``RateBasedRule`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e3a48130b6ea11cbba89c4d925188b1035288d0d20e62521703f08011393fa3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRateBasedRuleProps(
            metric_name=metric_name,
            name=name,
            rate_key=rate_key,
            rate_limit=rate_limit,
            match_predicates=match_predicates,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe15f950b117768ac352dd2f4184cee3df82ef2ee62d049f3cdc241483ab0d1d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3e95faf77cdcbaa5b2c40b3bcdf27d9ffe50f7ffeed4938a93f049bfc7a4dc2c)
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
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        '''A name for the metrics for a ``RateBasedRule`` .'''
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cfbc388b210d0582e04f751e60b45dd5b6bd3e72f02db2e98e85bef7ef56773)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A friendly name or description for a ``RateBasedRule`` .'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18ee093de7963dade7fd8f8af22735ddb09cbd49363ebb15bb550835d9a10364)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="rateKey")
    def rate_key(self) -> builtins.str:
        '''The field that AWS WAF uses to determine if requests are likely arriving from single source and thus subject to rate monitoring.'''
        return typing.cast(builtins.str, jsii.get(self, "rateKey"))

    @rate_key.setter
    def rate_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3936a70c79c88ceefcad7595ee96846e384c29bd9b33e3ff8ff346064fde0d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rateKey", value)

    @builtins.property
    @jsii.member(jsii_name="rateLimit")
    def rate_limit(self) -> jsii.Number:
        '''The maximum number of requests, which have an identical value in the field specified by the ``RateKey`` , allowed in a five-minute period.'''
        return typing.cast(jsii.Number, jsii.get(self, "rateLimit"))

    @rate_limit.setter
    def rate_limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05afa6fb83dc358397e8b0131bf464c079de2a415360ff4939536959254d4e24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rateLimit", value)

    @builtins.property
    @jsii.member(jsii_name="matchPredicates")
    def match_predicates(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRateBasedRule.PredicateProperty"]]]]:
        '''The ``Predicates`` object contains one ``Predicate`` element for each ``ByteMatchSet`` , ``IPSet`` , or ``SqlInjectionMatchSet>`` object that you want to include in a ``RateBasedRule`` .'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRateBasedRule.PredicateProperty"]]]], jsii.get(self, "matchPredicates"))

    @match_predicates.setter
    def match_predicates(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRateBasedRule.PredicateProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d03374c15b5e840bcddc8023a356ee3f22e2a776ff29025aa619ae7a754b2559)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchPredicates", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wafregional.CfnRateBasedRule.PredicateProperty",
        jsii_struct_bases=[],
        name_mapping={"data_id": "dataId", "negated": "negated", "type": "type"},
    )
    class PredicateProperty:
        def __init__(
            self,
            *,
            data_id: builtins.str,
            negated: typing.Union[builtins.bool, _IResolvable_da3f097b],
            type: builtins.str,
        ) -> None:
            '''Specifies the ``ByteMatchSet`` , ``IPSet`` , ``SqlInjectionMatchSet`` , ``XssMatchSet`` , ``RegexMatchSet`` , ``GeoMatchSet`` , and ``SizeConstraintSet`` objects that you want to add to a ``Rule`` and, for each object, indicates whether you want to negate the settings, for example, requests that do NOT originate from the IP address 192.0.2.44.

            :param data_id: A unique identifier for a predicate in a ``Rule`` , such as ``ByteMatchSetId`` or ``IPSetId`` . The ID is returned by the corresponding ``Create`` or ``List`` command.
            :param negated: Set ``Negated`` to ``False`` if you want AWS WAF to allow, block, or count requests based on the settings in the specified ``ByteMatchSet`` , ``IPSet`` , ``SqlInjectionMatchSet`` , ``XssMatchSet`` , ``RegexMatchSet`` , ``GeoMatchSet`` , or ``SizeConstraintSet`` . For example, if an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow or block requests based on that IP address. Set ``Negated`` to ``True`` if you want AWS WAF to allow or block a request based on the negation of the settings in the ``ByteMatchSet`` , ``IPSet`` , ``SqlInjectionMatchSet`` , ``XssMatchSet`` , ``RegexMatchSet`` , ``GeoMatchSet`` , or ``SizeConstraintSet`` >. For example, if an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow, block, or count requests based on all IP addresses *except* ``192.0.2.44`` .
            :param type: The type of predicate in a ``Rule`` , such as ``ByteMatch`` or ``IPSet`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ratebasedrule-predicate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wafregional as wafregional
                
                predicate_property = wafregional.CfnRateBasedRule.PredicateProperty(
                    data_id="dataId",
                    negated=False,
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2d862aab74caa6d90bd5f556c0ed61443009c5c844166ebbd2e40c13a6ed14e2)
                check_type(argname="argument data_id", value=data_id, expected_type=type_hints["data_id"])
                check_type(argname="argument negated", value=negated, expected_type=type_hints["negated"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "data_id": data_id,
                "negated": negated,
                "type": type,
            }

        @builtins.property
        def data_id(self) -> builtins.str:
            '''A unique identifier for a predicate in a ``Rule`` , such as ``ByteMatchSetId`` or ``IPSetId`` .

            The ID is returned by the corresponding ``Create`` or ``List`` command.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ratebasedrule-predicate.html#cfn-wafregional-ratebasedrule-predicate-dataid
            '''
            result = self._values.get("data_id")
            assert result is not None, "Required property 'data_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def negated(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Set ``Negated`` to ``False`` if you want AWS WAF to allow, block, or count requests based on the settings in the specified ``ByteMatchSet`` , ``IPSet`` , ``SqlInjectionMatchSet`` , ``XssMatchSet`` , ``RegexMatchSet`` , ``GeoMatchSet`` , or ``SizeConstraintSet`` .

            For example, if an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow or block requests based on that IP address.

            Set ``Negated`` to ``True`` if you want AWS WAF to allow or block a request based on the negation of the settings in the ``ByteMatchSet`` , ``IPSet`` , ``SqlInjectionMatchSet`` , ``XssMatchSet`` , ``RegexMatchSet`` , ``GeoMatchSet`` , or ``SizeConstraintSet`` >. For example, if an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow, block, or count requests based on all IP addresses *except* ``192.0.2.44`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ratebasedrule-predicate.html#cfn-wafregional-ratebasedrule-predicate-negated
            '''
            result = self._values.get("negated")
            assert result is not None, "Required property 'negated' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of predicate in a ``Rule`` , such as ``ByteMatch`` or ``IPSet`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ratebasedrule-predicate.html#cfn-wafregional-ratebasedrule-predicate-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PredicateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_wafregional.CfnRateBasedRuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "metric_name": "metricName",
        "name": "name",
        "rate_key": "rateKey",
        "rate_limit": "rateLimit",
        "match_predicates": "matchPredicates",
    },
)
class CfnRateBasedRuleProps:
    def __init__(
        self,
        *,
        metric_name: builtins.str,
        name: builtins.str,
        rate_key: builtins.str,
        rate_limit: jsii.Number,
        match_predicates: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRateBasedRule.PredicateProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRateBasedRule``.

        :param metric_name: A name for the metrics for a ``RateBasedRule`` . The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can't contain whitespace or metric names reserved for AWS WAF , including "All" and "Default_Action." You can't change the name of the metric after you create the ``RateBasedRule`` .
        :param name: A friendly name or description for a ``RateBasedRule`` . You can't change the name of a ``RateBasedRule`` after you create it.
        :param rate_key: The field that AWS WAF uses to determine if requests are likely arriving from single source and thus subject to rate monitoring. The only valid value for ``RateKey`` is ``IP`` . ``IP`` indicates that requests arriving from the same IP address are subject to the ``RateLimit`` that is specified in the ``RateBasedRule`` .
        :param rate_limit: The maximum number of requests, which have an identical value in the field specified by the ``RateKey`` , allowed in a five-minute period. If the number of requests exceeds the ``RateLimit`` and the other predicates specified in the rule are also met, AWS WAF triggers the action that is specified for this rule.
        :param match_predicates: The ``Predicates`` object contains one ``Predicate`` element for each ``ByteMatchSet`` , ``IPSet`` , or ``SqlInjectionMatchSet>`` object that you want to include in a ``RateBasedRule`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ratebasedrule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_wafregional as wafregional
            
            cfn_rate_based_rule_props = wafregional.CfnRateBasedRuleProps(
                metric_name="metricName",
                name="name",
                rate_key="rateKey",
                rate_limit=123,
            
                # the properties below are optional
                match_predicates=[wafregional.CfnRateBasedRule.PredicateProperty(
                    data_id="dataId",
                    negated=False,
                    type="type"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a5eb8767b8573e01975210155ccbe383a96e2861b6e27912a562e89c4067821)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument rate_key", value=rate_key, expected_type=type_hints["rate_key"])
            check_type(argname="argument rate_limit", value=rate_limit, expected_type=type_hints["rate_limit"])
            check_type(argname="argument match_predicates", value=match_predicates, expected_type=type_hints["match_predicates"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metric_name": metric_name,
            "name": name,
            "rate_key": rate_key,
            "rate_limit": rate_limit,
        }
        if match_predicates is not None:
            self._values["match_predicates"] = match_predicates

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''A name for the metrics for a ``RateBasedRule`` .

        The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can't contain whitespace or metric names reserved for AWS WAF , including "All" and "Default_Action." You can't change the name of the metric after you create the ``RateBasedRule`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ratebasedrule.html#cfn-wafregional-ratebasedrule-metricname
        '''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A friendly name or description for a ``RateBasedRule`` .

        You can't change the name of a ``RateBasedRule`` after you create it.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ratebasedrule.html#cfn-wafregional-ratebasedrule-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rate_key(self) -> builtins.str:
        '''The field that AWS WAF uses to determine if requests are likely arriving from single source and thus subject to rate monitoring.

        The only valid value for ``RateKey`` is ``IP`` . ``IP`` indicates that requests arriving from the same IP address are subject to the ``RateLimit`` that is specified in the ``RateBasedRule`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ratebasedrule.html#cfn-wafregional-ratebasedrule-ratekey
        '''
        result = self._values.get("rate_key")
        assert result is not None, "Required property 'rate_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rate_limit(self) -> jsii.Number:
        '''The maximum number of requests, which have an identical value in the field specified by the ``RateKey`` , allowed in a five-minute period.

        If the number of requests exceeds the ``RateLimit`` and the other predicates specified in the rule are also met, AWS WAF triggers the action that is specified for this rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ratebasedrule.html#cfn-wafregional-ratebasedrule-ratelimit
        '''
        result = self._values.get("rate_limit")
        assert result is not None, "Required property 'rate_limit' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def match_predicates(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnRateBasedRule.PredicateProperty]]]]:
        '''The ``Predicates`` object contains one ``Predicate`` element for each ``ByteMatchSet`` , ``IPSet`` , or ``SqlInjectionMatchSet>`` object that you want to include in a ``RateBasedRule`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ratebasedrule.html#cfn-wafregional-ratebasedrule-matchpredicates
        '''
        result = self._values.get("match_predicates")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnRateBasedRule.PredicateProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRateBasedRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnRegexPatternSet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_wafregional.CfnRegexPatternSet",
):
    '''The ``RegexPatternSet`` specifies the regular expression (regex) pattern that you want AWS WAF to search for, such as ``B[a@]dB[o0]t`` .

    You can then configure AWS WAF to reject those requests.

    Note that you can only create regex pattern sets using a AWS CloudFormation template. To add the regex pattern sets created through AWS CloudFormation to a RegexMatchSet, use the AWS WAF console, API, or command line interface (CLI). For more information, see `UpdateRegexMatchSet <https://docs.aws.amazon.com/waf/latest/APIReference/API_regional_UpdateRegexMatchSet.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-regexpatternset.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_wafregional as wafregional
        
        cfn_regex_pattern_set = wafregional.CfnRegexPatternSet(self, "MyCfnRegexPatternSet",
            name="name",
            regex_pattern_strings=["regexPatternStrings"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        regex_pattern_strings: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: A friendly name or description of the ``RegexPatternSet`` . You can't change ``Name`` after you create a ``RegexPatternSet`` .
        :param regex_pattern_strings: Specifies the regular expression (regex) patterns that you want AWS WAF to search for, such as ``B[a@]dB[o0]t`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc3290467cef7693ba0befd862e65e1c1db0f772a4356bde5baff5c34f116b38)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRegexPatternSetProps(
            name=name, regex_pattern_strings=regex_pattern_strings
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00571de7ee75e9fb7d683c9f103043ed8aea8e0e3aacc3f28c181c84dfc2b916)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d8280578e704e7c17c211a898942b98f9f0a27a21d61aebfb93c7b554b5a310e)
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
        '''A friendly name or description of the ``RegexPatternSet`` .'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8a9c9bc78e70485e2b2192fe0f5562437ca978b52817dea6b0fa3ea2aa2e212)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="regexPatternStrings")
    def regex_pattern_strings(self) -> typing.List[builtins.str]:
        '''Specifies the regular expression (regex) patterns that you want AWS WAF to search for, such as ``B[a@]dB[o0]t`` .'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "regexPatternStrings"))

    @regex_pattern_strings.setter
    def regex_pattern_strings(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c733d882b2636c9f3e83cbe3d3d3c45524e31baf8e0aefb580fcf499692ae821)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regexPatternStrings", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_wafregional.CfnRegexPatternSetProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "regex_pattern_strings": "regexPatternStrings"},
)
class CfnRegexPatternSetProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        regex_pattern_strings: typing.Sequence[builtins.str],
    ) -> None:
        '''Properties for defining a ``CfnRegexPatternSet``.

        :param name: A friendly name or description of the ``RegexPatternSet`` . You can't change ``Name`` after you create a ``RegexPatternSet`` .
        :param regex_pattern_strings: Specifies the regular expression (regex) patterns that you want AWS WAF to search for, such as ``B[a@]dB[o0]t`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-regexpatternset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_wafregional as wafregional
            
            cfn_regex_pattern_set_props = wafregional.CfnRegexPatternSetProps(
                name="name",
                regex_pattern_strings=["regexPatternStrings"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd2ba4ff373b9395d24df058327f71925859a4bbea04883bbecccd2cf281db74)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument regex_pattern_strings", value=regex_pattern_strings, expected_type=type_hints["regex_pattern_strings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "regex_pattern_strings": regex_pattern_strings,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''A friendly name or description of the ``RegexPatternSet`` .

        You can't change ``Name`` after you create a ``RegexPatternSet`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-regexpatternset.html#cfn-wafregional-regexpatternset-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def regex_pattern_strings(self) -> typing.List[builtins.str]:
        '''Specifies the regular expression (regex) patterns that you want AWS WAF to search for, such as ``B[a@]dB[o0]t`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-regexpatternset.html#cfn-wafregional-regexpatternset-regexpatternstrings
        '''
        result = self._values.get("regex_pattern_strings")
        assert result is not None, "Required property 'regex_pattern_strings' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRegexPatternSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnRule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_wafregional.CfnRule",
):
    '''.. epigraph::

   This is *AWS WAF Classic* documentation.

    For more information, see `AWS WAF Classic <https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html>`_ in the developer guide.
    .. epigraph::

       *For the latest version of AWS WAF* , use the AWS WAF V2 API and see the `AWS WAF Developer Guide <https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html>`_ . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

    A combination of ``ByteMatchSet`` , ``IPSet`` , and/or ``SqlInjectionMatchSet`` objects that identify the web requests that you want to allow, block, or count. For example, you might create a ``Rule`` that includes the following predicates:

    - An ``IPSet`` that causes AWS WAF to search for web requests that originate from the IP address ``192.0.2.44``
    - A ``ByteMatchSet`` that causes AWS WAF to search for web requests for which the value of the ``User-Agent`` header is ``BadBot`` .

    To match the settings in this ``Rule`` , a request must originate from ``192.0.2.44`` AND include a ``User-Agent`` header for which the value is ``BadBot`` .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-rule.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_wafregional as wafregional
        
        cfn_rule = wafregional.CfnRule(self, "MyCfnRule",
            metric_name="metricName",
            name="name",
        
            # the properties below are optional
            predicates=[wafregional.CfnRule.PredicateProperty(
                data_id="dataId",
                negated=False,
                type="type"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        metric_name: builtins.str,
        name: builtins.str,
        predicates: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRule.PredicateProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param metric_name: A name for the metrics for this ``Rule`` . The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and "Default_Action." You can't change ``MetricName`` after you create the ``Rule`` .
        :param name: The friendly name or description for the ``Rule`` . You can't change the name of a ``Rule`` after you create it.
        :param predicates: The ``Predicates`` object contains one ``Predicate`` element for each ``ByteMatchSet`` , ``IPSet`` , or ``SqlInjectionMatchSet`` object that you want to include in a ``Rule`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e8feae8cde7fd0a6a33c087a6bc2f530d0a2d84faa4c8473adff422fe6705fe)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRuleProps(metric_name=metric_name, name=name, predicates=predicates)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7702269394d1e5c3a77ce69b746f977ab20cd8769b7a0b2b47bb0bb1cf466f16)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3e8db74916fdd8e035f7d8fdf7c40ba0ff2149e206496918548e19340d4e9de8)
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
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        '''A name for the metrics for this ``Rule`` .'''
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6582f1ad9068d271bf929638d404c43ce4a7294b13f162946e1d16969c363edd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The friendly name or description for the ``Rule`` .'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae5c51af1e876790fd6d0be1510173bf597796956acb2d0e6a515db559ed94c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="predicates")
    def predicates(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRule.PredicateProperty"]]]]:
        '''The ``Predicates`` object contains one ``Predicate`` element for each ``ByteMatchSet`` , ``IPSet`` , or ``SqlInjectionMatchSet`` object that you want to include in a ``Rule`` .'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRule.PredicateProperty"]]]], jsii.get(self, "predicates"))

    @predicates.setter
    def predicates(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRule.PredicateProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f724ad55a0692458dfb9454847b548911c8e6b4f0c4ee20bc0195bd82c54f3ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "predicates", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wafregional.CfnRule.PredicateProperty",
        jsii_struct_bases=[],
        name_mapping={"data_id": "dataId", "negated": "negated", "type": "type"},
    )
    class PredicateProperty:
        def __init__(
            self,
            *,
            data_id: builtins.str,
            negated: typing.Union[builtins.bool, _IResolvable_da3f097b],
            type: builtins.str,
        ) -> None:
            '''Specifies the ``ByteMatchSet`` , ``IPSet`` , ``SqlInjectionMatchSet`` , ``XssMatchSet`` , ``RegexMatchSet`` , ``GeoMatchSet`` , and ``SizeConstraintSet`` objects that you want to add to a ``Rule`` and, for each object, indicates whether you want to negate the settings, for example, requests that do NOT originate from the IP address 192.0.2.44.

            :param data_id: A unique identifier for a predicate in a ``Rule`` , such as ``ByteMatchSetId`` or ``IPSetId`` . The ID is returned by the corresponding ``Create`` or ``List`` command.
            :param negated: Set ``Negated`` to ``False`` if you want AWS WAF to allow, block, or count requests based on the settings in the specified ``ByteMatchSet`` , ``IPSet`` , ``SqlInjectionMatchSet`` , ``XssMatchSet`` , ``RegexMatchSet`` , ``GeoMatchSet`` , or ``SizeConstraintSet`` . For example, if an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow or block requests based on that IP address. Set ``Negated`` to ``True`` if you want AWS WAF to allow or block a request based on the negation of the settings in the ``ByteMatchSet`` , ``IPSet`` , ``SqlInjectionMatchSet`` , ``XssMatchSet`` , ``RegexMatchSet`` , ``GeoMatchSet`` , or ``SizeConstraintSet`` . For example, if an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow, block, or count requests based on all IP addresses *except* ``192.0.2.44`` .
            :param type: The type of predicate in a ``Rule`` , such as ``ByteMatch`` or ``IPSet`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-rule-predicate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wafregional as wafregional
                
                predicate_property = wafregional.CfnRule.PredicateProperty(
                    data_id="dataId",
                    negated=False,
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3cc39471795f985fdd66736c51389bb4064b463605d224670988abb34e37881e)
                check_type(argname="argument data_id", value=data_id, expected_type=type_hints["data_id"])
                check_type(argname="argument negated", value=negated, expected_type=type_hints["negated"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "data_id": data_id,
                "negated": negated,
                "type": type,
            }

        @builtins.property
        def data_id(self) -> builtins.str:
            '''A unique identifier for a predicate in a ``Rule`` , such as ``ByteMatchSetId`` or ``IPSetId`` .

            The ID is returned by the corresponding ``Create`` or ``List`` command.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-rule-predicate.html#cfn-wafregional-rule-predicate-dataid
            '''
            result = self._values.get("data_id")
            assert result is not None, "Required property 'data_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def negated(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Set ``Negated`` to ``False`` if you want AWS WAF to allow, block, or count requests based on the settings in the specified ``ByteMatchSet`` , ``IPSet`` , ``SqlInjectionMatchSet`` , ``XssMatchSet`` , ``RegexMatchSet`` , ``GeoMatchSet`` , or ``SizeConstraintSet`` .

            For example, if an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow or block requests based on that IP address.

            Set ``Negated`` to ``True`` if you want AWS WAF to allow or block a request based on the negation of the settings in the ``ByteMatchSet`` , ``IPSet`` , ``SqlInjectionMatchSet`` , ``XssMatchSet`` , ``RegexMatchSet`` , ``GeoMatchSet`` , or ``SizeConstraintSet`` . For example, if an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow, block, or count requests based on all IP addresses *except* ``192.0.2.44`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-rule-predicate.html#cfn-wafregional-rule-predicate-negated
            '''
            result = self._values.get("negated")
            assert result is not None, "Required property 'negated' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of predicate in a ``Rule`` , such as ``ByteMatch`` or ``IPSet`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-rule-predicate.html#cfn-wafregional-rule-predicate-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PredicateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_wafregional.CfnRuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "metric_name": "metricName",
        "name": "name",
        "predicates": "predicates",
    },
)
class CfnRuleProps:
    def __init__(
        self,
        *,
        metric_name: builtins.str,
        name: builtins.str,
        predicates: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.PredicateProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRule``.

        :param metric_name: A name for the metrics for this ``Rule`` . The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and "Default_Action." You can't change ``MetricName`` after you create the ``Rule`` .
        :param name: The friendly name or description for the ``Rule`` . You can't change the name of a ``Rule`` after you create it.
        :param predicates: The ``Predicates`` object contains one ``Predicate`` element for each ``ByteMatchSet`` , ``IPSet`` , or ``SqlInjectionMatchSet`` object that you want to include in a ``Rule`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-rule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_wafregional as wafregional
            
            cfn_rule_props = wafregional.CfnRuleProps(
                metric_name="metricName",
                name="name",
            
                # the properties below are optional
                predicates=[wafregional.CfnRule.PredicateProperty(
                    data_id="dataId",
                    negated=False,
                    type="type"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdc102021e417a504401cd27c9a5d604cd6be3ce5473501b852f107ddfdb257b)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument predicates", value=predicates, expected_type=type_hints["predicates"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metric_name": metric_name,
            "name": name,
        }
        if predicates is not None:
            self._values["predicates"] = predicates

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''A name for the metrics for this ``Rule`` .

        The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and "Default_Action." You can't change ``MetricName`` after you create the ``Rule`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-rule.html#cfn-wafregional-rule-metricname
        '''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The friendly name or description for the ``Rule`` .

        You can't change the name of a ``Rule`` after you create it.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-rule.html#cfn-wafregional-rule-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def predicates(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnRule.PredicateProperty]]]]:
        '''The ``Predicates`` object contains one ``Predicate`` element for each ``ByteMatchSet`` , ``IPSet`` , or ``SqlInjectionMatchSet`` object that you want to include in a ``Rule`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-rule.html#cfn-wafregional-rule-predicates
        '''
        result = self._values.get("predicates")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnRule.PredicateProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSizeConstraintSet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_wafregional.CfnSizeConstraintSet",
):
    '''.. epigraph::

   This is *AWS WAF Classic* documentation.

    For more information, see `AWS WAF Classic <https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html>`_ in the developer guide.
    .. epigraph::

       *For the latest version of AWS WAF* , use the AWS WAF V2 API and see the `AWS WAF Developer Guide <https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html>`_ . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

    A complex type that contains ``SizeConstraint`` objects, which specify the parts of web requests that you want AWS WAF to inspect the size of. If a ``SizeConstraintSet`` contains more than one ``SizeConstraint`` object, a request only needs to match one constraint to be considered a match.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sizeconstraintset.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_wafregional as wafregional
        
        cfn_size_constraint_set = wafregional.CfnSizeConstraintSet(self, "MyCfnSizeConstraintSet",
            name="name",
        
            # the properties below are optional
            size_constraints=[wafregional.CfnSizeConstraintSet.SizeConstraintProperty(
                comparison_operator="comparisonOperator",
                field_to_match=wafregional.CfnSizeConstraintSet.FieldToMatchProperty(
                    type="type",
        
                    # the properties below are optional
                    data="data"
                ),
                size=123,
                text_transformation="textTransformation"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        size_constraints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSizeConstraintSet.SizeConstraintProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name, if any, of the ``SizeConstraintSet`` .
        :param size_constraints: The size constraint and the part of the web request to check.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3617242c65fe4a2405945be806ebc94732125d50948fdc61e6bfc3017667c0b3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSizeConstraintSetProps(name=name, size_constraints=size_constraints)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8e40f87fdc57eff0e9208037fed9950431c54262a5933c7fc441600b2f2952b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__87c74e8a80680d49334aed17e7005e3d0784bb5ae261700d5945a65e7011d076)
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
        '''The name, if any, of the ``SizeConstraintSet`` .'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff5fd08bc9276e64954323aeff7d7f98ba67f832e5bfa54e3a04eafd0977cfbb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sizeConstraints")
    def size_constraints(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSizeConstraintSet.SizeConstraintProperty"]]]]:
        '''The size constraint and the part of the web request to check.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSizeConstraintSet.SizeConstraintProperty"]]]], jsii.get(self, "sizeConstraints"))

    @size_constraints.setter
    def size_constraints(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSizeConstraintSet.SizeConstraintProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed10db9ee0b6303854a666f25e1251855886884dd58f67884c32b8f4bdbfe468)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizeConstraints", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wafregional.CfnSizeConstraintSet.FieldToMatchProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "data": "data"},
    )
    class FieldToMatchProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            data: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The part of a web request that you want AWS WAF to inspect, such as a specific header or a query string.

            :param type: The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following: - ``HEADER`` : A specified request header, for example, the value of the ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the header in ``Data`` . - ``METHOD`` : The HTTP method, which indicates the type of operation that the request is asking the origin to perform. - ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a ``?`` character, if any. - ``URI`` : The part of a web request that identifies a resource, for example, ``/images/daily-ad.jpg`` . - ``BODY`` : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. - ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30 characters. - ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in ``TargetString`` .
            :param data: When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the header is not case sensitive. When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The parameter name is not case sensitive. If the value of ``Type`` is any other value, omit ``Data`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-fieldtomatch.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wafregional as wafregional
                
                field_to_match_property = wafregional.CfnSizeConstraintSet.FieldToMatchProperty(
                    type="type",
                
                    # the properties below are optional
                    data="data"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4c9becc0d0d2ffe051374f750cd582e90321160bd7a3123162da9a16e0226be8)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if data is not None:
                self._values["data"] = data

        @builtins.property
        def type(self) -> builtins.str:
            '''The part of the web request that you want AWS WAF to search for a specified string.

            Parts of a request that you can search include the following:

            - ``HEADER`` : A specified request header, for example, the value of the ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the header in ``Data`` .
            - ``METHOD`` : The HTTP method, which indicates the type of operation that the request is asking the origin to perform.
            - ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a ``?`` character, if any.
            - ``URI`` : The part of a web request that identifies a resource, for example, ``/images/daily-ad.jpg`` .
            - ``BODY`` : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set.
            - ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30 characters.
            - ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in ``TargetString`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-fieldtomatch.html#cfn-wafregional-sizeconstraintset-fieldtomatch-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def data(self) -> typing.Optional[builtins.str]:
            '''When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS WAF to search, for example, ``User-Agent`` or ``Referer`` .

            The name of the header is not case sensitive.

            When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The parameter name is not case sensitive.

            If the value of ``Type`` is any other value, omit ``Data`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-fieldtomatch.html#cfn-wafregional-sizeconstraintset-fieldtomatch-data
            '''
            result = self._values.get("data")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FieldToMatchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wafregional.CfnSizeConstraintSet.SizeConstraintProperty",
        jsii_struct_bases=[],
        name_mapping={
            "comparison_operator": "comparisonOperator",
            "field_to_match": "fieldToMatch",
            "size": "size",
            "text_transformation": "textTransformation",
        },
    )
    class SizeConstraintProperty:
        def __init__(
            self,
            *,
            comparison_operator: builtins.str,
            field_to_match: typing.Union[_IResolvable_da3f097b, typing.Union["CfnSizeConstraintSet.FieldToMatchProperty", typing.Dict[builtins.str, typing.Any]]],
            size: jsii.Number,
            text_transformation: builtins.str,
        ) -> None:
            '''.. epigraph::

   This is *AWS WAF Classic* documentation.

            For more information, see `AWS WAF Classic <https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html>`_ in the developer guide.
            .. epigraph::

               *For the latest version of AWS WAF* , use the AWS WAF V2 API and see the `AWS WAF Developer Guide <https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html>`_ . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

            Specifies a constraint on the size of a part of the web request. AWS WAF uses the ``Size`` , ``ComparisonOperator`` , and ``FieldToMatch`` to build an expression in the form of " ``Size`` ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that expression is true, the ``SizeConstraint`` is considered to match.

            :param comparison_operator: The type of comparison you want AWS WAF to perform. AWS WAF uses this in combination with the provided ``Size`` and ``FieldToMatch`` to build an expression in the form of " ``Size`` ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that expression is true, the ``SizeConstraint`` is considered to match. *EQ* : Used to test if the ``Size`` is equal to the size of the ``FieldToMatch`` *NE* : Used to test if the ``Size`` is not equal to the size of the ``FieldToMatch`` *LE* : Used to test if the ``Size`` is less than or equal to the size of the ``FieldToMatch`` *LT* : Used to test if the ``Size`` is strictly less than the size of the ``FieldToMatch`` *GE* : Used to test if the ``Size`` is greater than or equal to the size of the ``FieldToMatch`` *GT* : Used to test if the ``Size`` is strictly greater than the size of the ``FieldToMatch``
            :param field_to_match: The part of a web request that you want AWS WAF to inspect, such as a specific header or a query string.
            :param size: The size in bytes that you want AWS WAF to compare against the size of the specified ``FieldToMatch`` . AWS WAF uses this in combination with ``ComparisonOperator`` and ``FieldToMatch`` to build an expression in the form of " ``Size`` ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that expression is true, the ``SizeConstraint`` is considered to match. Valid values for size are 0 - 21474836480 bytes (0 - 20 GB). If you specify ``URI`` for the value of ``Type`` , the / in the URI path that you specify counts as one character. For example, the URI ``/logo.jpg`` is nine characters long.
            :param text_transformation: Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF . If you specify a transformation, AWS WAF performs the transformation on ``FieldToMatch`` before inspecting a request for a match. You can only specify a single type of TextTransformation. Note that if you choose ``BODY`` for the value of ``Type`` , you must choose ``NONE`` for ``TextTransformation`` because the API Gateway API or Application Load Balancer forward only the first 8192 bytes for inspection. *NONE* Specify ``NONE`` if you don't want to perform any text transformations. *CMD_LINE* When you're concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations: - Delete the following characters: \\ " ' ^ - Delete spaces before the following characters: / ( - Replace the following characters with a space: , ; - Replace multiple spaces with one space - Convert uppercase letters (A-Z) to lowercase (a-z) *COMPRESS_WHITE_SPACE* Use this option to replace the following characters with a space character (decimal 32): - \\f, formfeed, decimal 12 - \\t, tab, decimal 9 - \\n, newline, decimal 10 - \\r, carriage return, decimal 13 - \\v, vertical tab, decimal 11 - non-breaking space, decimal 160 ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space. *HTML_ENTITY_DECODE* Use this option to replace HTML-encoded characters with unencoded characters. ``HTML_ENTITY_DECODE`` performs the following operations: - Replaces ``(ampersand)quot;`` with ``"`` - Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160 - Replaces ``(ampersand)lt;`` with a "less than" symbol - Replaces ``(ampersand)gt;`` with ``>`` - Replaces characters that are represented in hexadecimal format, ``(ampersand)#xhhhh;`` , with the corresponding characters - Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` , with the corresponding characters *LOWERCASE* Use this option to convert uppercase letters (A-Z) to lowercase (a-z). *URL_DECODE* Use this option to decode a URL-encoded value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-sizeconstraint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wafregional as wafregional
                
                size_constraint_property = wafregional.CfnSizeConstraintSet.SizeConstraintProperty(
                    comparison_operator="comparisonOperator",
                    field_to_match=wafregional.CfnSizeConstraintSet.FieldToMatchProperty(
                        type="type",
                
                        # the properties below are optional
                        data="data"
                    ),
                    size=123,
                    text_transformation="textTransformation"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1bd0b350acf83dad556bc4a4642cf56c05406c80b304c48c6f9978cc0b6fcefd)
                check_type(argname="argument comparison_operator", value=comparison_operator, expected_type=type_hints["comparison_operator"])
                check_type(argname="argument field_to_match", value=field_to_match, expected_type=type_hints["field_to_match"])
                check_type(argname="argument size", value=size, expected_type=type_hints["size"])
                check_type(argname="argument text_transformation", value=text_transformation, expected_type=type_hints["text_transformation"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "comparison_operator": comparison_operator,
                "field_to_match": field_to_match,
                "size": size,
                "text_transformation": text_transformation,
            }

        @builtins.property
        def comparison_operator(self) -> builtins.str:
            '''The type of comparison you want AWS WAF to perform.

            AWS WAF uses this in combination with the provided ``Size`` and ``FieldToMatch`` to build an expression in the form of " ``Size`` ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that expression is true, the ``SizeConstraint`` is considered to match.

            *EQ* : Used to test if the ``Size`` is equal to the size of the ``FieldToMatch``

            *NE* : Used to test if the ``Size`` is not equal to the size of the ``FieldToMatch``

            *LE* : Used to test if the ``Size`` is less than or equal to the size of the ``FieldToMatch``

            *LT* : Used to test if the ``Size`` is strictly less than the size of the ``FieldToMatch``

            *GE* : Used to test if the ``Size`` is greater than or equal to the size of the ``FieldToMatch``

            *GT* : Used to test if the ``Size`` is strictly greater than the size of the ``FieldToMatch``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-sizeconstraint.html#cfn-wafregional-sizeconstraintset-sizeconstraint-comparisonoperator
            '''
            result = self._values.get("comparison_operator")
            assert result is not None, "Required property 'comparison_operator' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def field_to_match(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnSizeConstraintSet.FieldToMatchProperty"]:
            '''The part of a web request that you want AWS WAF to inspect, such as a specific header or a query string.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-sizeconstraint.html#cfn-wafregional-sizeconstraintset-sizeconstraint-fieldtomatch
            '''
            result = self._values.get("field_to_match")
            assert result is not None, "Required property 'field_to_match' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnSizeConstraintSet.FieldToMatchProperty"], result)

        @builtins.property
        def size(self) -> jsii.Number:
            '''The size in bytes that you want AWS WAF to compare against the size of the specified ``FieldToMatch`` .

            AWS WAF uses this in combination with ``ComparisonOperator`` and ``FieldToMatch`` to build an expression in the form of " ``Size`` ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that expression is true, the ``SizeConstraint`` is considered to match.

            Valid values for size are 0 - 21474836480 bytes (0 - 20 GB).

            If you specify ``URI`` for the value of ``Type`` , the / in the URI path that you specify counts as one character. For example, the URI ``/logo.jpg`` is nine characters long.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-sizeconstraint.html#cfn-wafregional-sizeconstraintset-sizeconstraint-size
            '''
            result = self._values.get("size")
            assert result is not None, "Required property 'size' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def text_transformation(self) -> builtins.str:
            '''Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF .

            If you specify a transformation, AWS WAF performs the transformation on ``FieldToMatch`` before inspecting a request for a match.

            You can only specify a single type of TextTransformation.

            Note that if you choose ``BODY`` for the value of ``Type`` , you must choose ``NONE`` for ``TextTransformation`` because the API Gateway API or Application Load Balancer forward only the first 8192 bytes for inspection.

            *NONE*

            Specify ``NONE`` if you don't want to perform any text transformations.

            *CMD_LINE*

            When you're concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

            - Delete the following characters: \\ " ' ^
            - Delete spaces before the following characters: / (
            - Replace the following characters with a space: , ;
            - Replace multiple spaces with one space
            - Convert uppercase letters (A-Z) to lowercase (a-z)

            *COMPRESS_WHITE_SPACE*

            Use this option to replace the following characters with a space character (decimal 32):

            - \\f, formfeed, decimal 12
            - \\t, tab, decimal 9
            - \\n, newline, decimal 10
            - \\r, carriage return, decimal 13
            - \\v, vertical tab, decimal 11
            - non-breaking space, decimal 160

            ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

            *HTML_ENTITY_DECODE*

            Use this option to replace HTML-encoded characters with unencoded characters. ``HTML_ENTITY_DECODE`` performs the following operations:

            - Replaces ``(ampersand)quot;`` with ``"``
            - Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160
            - Replaces ``(ampersand)lt;`` with a "less than" symbol
            - Replaces ``(ampersand)gt;`` with ``>``
            - Replaces characters that are represented in hexadecimal format, ``(ampersand)#xhhhh;`` , with the corresponding characters
            - Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` , with the corresponding characters

            *LOWERCASE*

            Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

            *URL_DECODE*

            Use this option to decode a URL-encoded value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-sizeconstraint.html#cfn-wafregional-sizeconstraintset-sizeconstraint-texttransformation
            '''
            result = self._values.get("text_transformation")
            assert result is not None, "Required property 'text_transformation' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SizeConstraintProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_wafregional.CfnSizeConstraintSetProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "size_constraints": "sizeConstraints"},
)
class CfnSizeConstraintSetProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        size_constraints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSizeConstraintSet.SizeConstraintProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSizeConstraintSet``.

        :param name: The name, if any, of the ``SizeConstraintSet`` .
        :param size_constraints: The size constraint and the part of the web request to check.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sizeconstraintset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_wafregional as wafregional
            
            cfn_size_constraint_set_props = wafregional.CfnSizeConstraintSetProps(
                name="name",
            
                # the properties below are optional
                size_constraints=[wafregional.CfnSizeConstraintSet.SizeConstraintProperty(
                    comparison_operator="comparisonOperator",
                    field_to_match=wafregional.CfnSizeConstraintSet.FieldToMatchProperty(
                        type="type",
            
                        # the properties below are optional
                        data="data"
                    ),
                    size=123,
                    text_transformation="textTransformation"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf80c55882638ea37cfa7a142fc6f1adcee512250a5dc52e55c3ebaf0d3916f9)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument size_constraints", value=size_constraints, expected_type=type_hints["size_constraints"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if size_constraints is not None:
            self._values["size_constraints"] = size_constraints

    @builtins.property
    def name(self) -> builtins.str:
        '''The name, if any, of the ``SizeConstraintSet`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sizeconstraintset.html#cfn-wafregional-sizeconstraintset-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def size_constraints(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnSizeConstraintSet.SizeConstraintProperty]]]]:
        '''The size constraint and the part of the web request to check.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sizeconstraintset.html#cfn-wafregional-sizeconstraintset-sizeconstraints
        '''
        result = self._values.get("size_constraints")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnSizeConstraintSet.SizeConstraintProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSizeConstraintSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSqlInjectionMatchSet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_wafregional.CfnSqlInjectionMatchSet",
):
    '''.. epigraph::

   This is *AWS WAF Classic* documentation.

    For more information, see `AWS WAF Classic <https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html>`_ in the developer guide.
    .. epigraph::

       *For the latest version of AWS WAF* , use the AWS WAF V2 API and see the `AWS WAF Developer Guide <https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html>`_ . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

    A complex type that contains ``SqlInjectionMatchTuple`` objects, which specify the parts of web requests that you want AWS WAF to inspect for snippets of malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header. If a ``SqlInjectionMatchSet`` contains more than one ``SqlInjectionMatchTuple`` object, a request needs to include snippets of SQL code in only one of the specified parts of the request to be considered a match.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sqlinjectionmatchset.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_wafregional as wafregional
        
        cfn_sql_injection_match_set = wafregional.CfnSqlInjectionMatchSet(self, "MyCfnSqlInjectionMatchSet",
            name="name",
        
            # the properties below are optional
            sql_injection_match_tuples=[wafregional.CfnSqlInjectionMatchSet.SqlInjectionMatchTupleProperty(
                field_to_match=wafregional.CfnSqlInjectionMatchSet.FieldToMatchProperty(
                    type="type",
        
                    # the properties below are optional
                    data="data"
                ),
                text_transformation="textTransformation"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        sql_injection_match_tuples: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSqlInjectionMatchSet.SqlInjectionMatchTupleProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name, if any, of the ``SqlInjectionMatchSet`` .
        :param sql_injection_match_tuples: Specifies the parts of web requests that you want to inspect for snippets of malicious SQL code.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd9e0f900ac8b2a5f047d3bd88768dc62f95c2451091386675727ceef64e59a8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSqlInjectionMatchSetProps(
            name=name, sql_injection_match_tuples=sql_injection_match_tuples
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c31baabf0f1513b14ade51b1baa82fd3a13ebf2f9d357484ef5e959a3167f52)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7a7e4f5a844750e6530efce17048877a42dd27c09734193ce34675fee637e8a0)
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
        '''The name, if any, of the ``SqlInjectionMatchSet`` .'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__821f3800915744d3ffeab016ddfa93507a82ab75f2469faeb24a18e99c0a8e16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sqlInjectionMatchTuples")
    def sql_injection_match_tuples(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSqlInjectionMatchSet.SqlInjectionMatchTupleProperty"]]]]:
        '''Specifies the parts of web requests that you want to inspect for snippets of malicious SQL code.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSqlInjectionMatchSet.SqlInjectionMatchTupleProperty"]]]], jsii.get(self, "sqlInjectionMatchTuples"))

    @sql_injection_match_tuples.setter
    def sql_injection_match_tuples(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSqlInjectionMatchSet.SqlInjectionMatchTupleProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36e43d4ce4ce856f540724f26bbc23e2cb13b58361de226358a8285ca8e3eba5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sqlInjectionMatchTuples", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wafregional.CfnSqlInjectionMatchSet.FieldToMatchProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "data": "data"},
    )
    class FieldToMatchProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            data: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The part of a web request that you want AWS WAF to inspect, such as a specific header or a query string.

            :param type: The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following: - ``HEADER`` : A specified request header, for example, the value of the ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the header in ``Data`` . - ``METHOD`` : The HTTP method, which indicates the type of operation that the request is asking the origin to perform. - ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a ``?`` character, if any. - ``URI`` : The part of a web request that identifies a resource, for example, ``/images/daily-ad.jpg`` . - ``BODY`` : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. - ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30 characters. - ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in ``TargetString`` .
            :param data: When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the header is not case sensitive. When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The parameter name is not case sensitive. If the value of ``Type`` is any other value, omit ``Data`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-fieldtomatch.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wafregional as wafregional
                
                field_to_match_property = wafregional.CfnSqlInjectionMatchSet.FieldToMatchProperty(
                    type="type",
                
                    # the properties below are optional
                    data="data"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__74bf0200de57ed765f39e71220fec1aa20f6ac62241a5295a52368b0b8791950)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if data is not None:
                self._values["data"] = data

        @builtins.property
        def type(self) -> builtins.str:
            '''The part of the web request that you want AWS WAF to search for a specified string.

            Parts of a request that you can search include the following:

            - ``HEADER`` : A specified request header, for example, the value of the ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the header in ``Data`` .
            - ``METHOD`` : The HTTP method, which indicates the type of operation that the request is asking the origin to perform.
            - ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a ``?`` character, if any.
            - ``URI`` : The part of a web request that identifies a resource, for example, ``/images/daily-ad.jpg`` .
            - ``BODY`` : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set.
            - ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30 characters.
            - ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in ``TargetString`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-fieldtomatch.html#cfn-wafregional-sqlinjectionmatchset-fieldtomatch-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def data(self) -> typing.Optional[builtins.str]:
            '''When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS WAF to search, for example, ``User-Agent`` or ``Referer`` .

            The name of the header is not case sensitive.

            When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The parameter name is not case sensitive.

            If the value of ``Type`` is any other value, omit ``Data`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-fieldtomatch.html#cfn-wafregional-sqlinjectionmatchset-fieldtomatch-data
            '''
            result = self._values.get("data")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FieldToMatchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wafregional.CfnSqlInjectionMatchSet.SqlInjectionMatchTupleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "field_to_match": "fieldToMatch",
            "text_transformation": "textTransformation",
        },
    )
    class SqlInjectionMatchTupleProperty:
        def __init__(
            self,
            *,
            field_to_match: typing.Union[_IResolvable_da3f097b, typing.Union["CfnSqlInjectionMatchSet.FieldToMatchProperty", typing.Dict[builtins.str, typing.Any]]],
            text_transformation: builtins.str,
        ) -> None:
            '''.. epigraph::

   This is *AWS WAF Classic* documentation.

            For more information, see `AWS WAF Classic <https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html>`_ in the developer guide.
            .. epigraph::

               *For the latest version of AWS WAF* , use the AWS WAF V2 API and see the `AWS WAF Developer Guide <https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html>`_ . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

            Specifies the part of a web request that you want AWS WAF to inspect for snippets of malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.

            :param field_to_match: The part of a web request that you want AWS WAF to inspect, such as a specific header or a query string.
            :param text_transformation: Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF . If you specify a transformation, AWS WAF performs the transformation on ``FieldToMatch`` before inspecting it for a match. You can only specify a single type of TextTransformation. *CMD_LINE* When you're concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations: - Delete the following characters: \\ " ' ^ - Delete spaces before the following characters: / ( - Replace the following characters with a space: , ; - Replace multiple spaces with one space - Convert uppercase letters (A-Z) to lowercase (a-z) *COMPRESS_WHITE_SPACE* Use this option to replace the following characters with a space character (decimal 32): - \\f, formfeed, decimal 12 - \\t, tab, decimal 9 - \\n, newline, decimal 10 - \\r, carriage return, decimal 13 - \\v, vertical tab, decimal 11 - non-breaking space, decimal 160 ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space. *HTML_ENTITY_DECODE* Use this option to replace HTML-encoded characters with unencoded characters. ``HTML_ENTITY_DECODE`` performs the following operations: - Replaces ``(ampersand)quot;`` with ``"`` - Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160 - Replaces ``(ampersand)lt;`` with a "less than" symbol - Replaces ``(ampersand)gt;`` with ``>`` - Replaces characters that are represented in hexadecimal format, ``(ampersand)#xhhhh;`` , with the corresponding characters - Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` , with the corresponding characters *LOWERCASE* Use this option to convert uppercase letters (A-Z) to lowercase (a-z). *URL_DECODE* Use this option to decode a URL-encoded value. *NONE* Specify ``NONE`` if you don't want to perform any text transformations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuple.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wafregional as wafregional
                
                sql_injection_match_tuple_property = wafregional.CfnSqlInjectionMatchSet.SqlInjectionMatchTupleProperty(
                    field_to_match=wafregional.CfnSqlInjectionMatchSet.FieldToMatchProperty(
                        type="type",
                
                        # the properties below are optional
                        data="data"
                    ),
                    text_transformation="textTransformation"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1a28b84fb8065ea3716ec026d7e9acbc436d5c02ce29d073ed967129e4304751)
                check_type(argname="argument field_to_match", value=field_to_match, expected_type=type_hints["field_to_match"])
                check_type(argname="argument text_transformation", value=text_transformation, expected_type=type_hints["text_transformation"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "field_to_match": field_to_match,
                "text_transformation": text_transformation,
            }

        @builtins.property
        def field_to_match(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnSqlInjectionMatchSet.FieldToMatchProperty"]:
            '''The part of a web request that you want AWS WAF to inspect, such as a specific header or a query string.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuple.html#cfn-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuple-fieldtomatch
            '''
            result = self._values.get("field_to_match")
            assert result is not None, "Required property 'field_to_match' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnSqlInjectionMatchSet.FieldToMatchProperty"], result)

        @builtins.property
        def text_transformation(self) -> builtins.str:
            '''Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF .

            If you specify a transformation, AWS WAF performs the transformation on ``FieldToMatch`` before inspecting it for a match.

            You can only specify a single type of TextTransformation.

            *CMD_LINE*

            When you're concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

            - Delete the following characters: \\ " ' ^
            - Delete spaces before the following characters: / (
            - Replace the following characters with a space: , ;
            - Replace multiple spaces with one space
            - Convert uppercase letters (A-Z) to lowercase (a-z)

            *COMPRESS_WHITE_SPACE*

            Use this option to replace the following characters with a space character (decimal 32):

            - \\f, formfeed, decimal 12
            - \\t, tab, decimal 9
            - \\n, newline, decimal 10
            - \\r, carriage return, decimal 13
            - \\v, vertical tab, decimal 11
            - non-breaking space, decimal 160

            ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

            *HTML_ENTITY_DECODE*

            Use this option to replace HTML-encoded characters with unencoded characters. ``HTML_ENTITY_DECODE`` performs the following operations:

            - Replaces ``(ampersand)quot;`` with ``"``
            - Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160
            - Replaces ``(ampersand)lt;`` with a "less than" symbol
            - Replaces ``(ampersand)gt;`` with ``>``
            - Replaces characters that are represented in hexadecimal format, ``(ampersand)#xhhhh;`` , with the corresponding characters
            - Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` , with the corresponding characters

            *LOWERCASE*

            Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

            *URL_DECODE*

            Use this option to decode a URL-encoded value.

            *NONE*

            Specify ``NONE`` if you don't want to perform any text transformations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuple.html#cfn-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuple-texttransformation
            '''
            result = self._values.get("text_transformation")
            assert result is not None, "Required property 'text_transformation' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SqlInjectionMatchTupleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_wafregional.CfnSqlInjectionMatchSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "sql_injection_match_tuples": "sqlInjectionMatchTuples",
    },
)
class CfnSqlInjectionMatchSetProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        sql_injection_match_tuples: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSqlInjectionMatchSet.SqlInjectionMatchTupleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSqlInjectionMatchSet``.

        :param name: The name, if any, of the ``SqlInjectionMatchSet`` .
        :param sql_injection_match_tuples: Specifies the parts of web requests that you want to inspect for snippets of malicious SQL code.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sqlinjectionmatchset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_wafregional as wafregional
            
            cfn_sql_injection_match_set_props = wafregional.CfnSqlInjectionMatchSetProps(
                name="name",
            
                # the properties below are optional
                sql_injection_match_tuples=[wafregional.CfnSqlInjectionMatchSet.SqlInjectionMatchTupleProperty(
                    field_to_match=wafregional.CfnSqlInjectionMatchSet.FieldToMatchProperty(
                        type="type",
            
                        # the properties below are optional
                        data="data"
                    ),
                    text_transformation="textTransformation"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb86879a015cba2fd0a9fb28d3c9e047ee07933c06f46f2a05813de3c6381635)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument sql_injection_match_tuples", value=sql_injection_match_tuples, expected_type=type_hints["sql_injection_match_tuples"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if sql_injection_match_tuples is not None:
            self._values["sql_injection_match_tuples"] = sql_injection_match_tuples

    @builtins.property
    def name(self) -> builtins.str:
        '''The name, if any, of the ``SqlInjectionMatchSet`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sqlinjectionmatchset.html#cfn-wafregional-sqlinjectionmatchset-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sql_injection_match_tuples(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnSqlInjectionMatchSet.SqlInjectionMatchTupleProperty]]]]:
        '''Specifies the parts of web requests that you want to inspect for snippets of malicious SQL code.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sqlinjectionmatchset.html#cfn-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuples
        '''
        result = self._values.get("sql_injection_match_tuples")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnSqlInjectionMatchSet.SqlInjectionMatchTupleProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSqlInjectionMatchSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnWebACL(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_wafregional.CfnWebACL",
):
    '''.. epigraph::

   This is *AWS WAF Classic* documentation.

    For more information, see `AWS WAF Classic <https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html>`_ in the developer guide.
    .. epigraph::

       *For the latest version of AWS WAF* , use the AWS WAF V2 API and see the `AWS WAF Developer Guide <https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html>`_ . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

    Contains the ``Rules`` that identify the requests that you want to allow, block, or count. In a ``WebACL`` , you also specify a default action ( ``ALLOW`` or ``BLOCK`` ), and the action for each ``Rule`` that you add to a ``WebACL`` , for example, block requests from specified IP addresses or block requests from specified referrers. If you add more than one ``Rule`` to a ``WebACL`` , a request needs to match only one of the specifications to be allowed, blocked, or counted.

    To identify the requests that you want AWS WAF to filter, you associate the ``WebACL`` with an API Gateway API or an Application Load Balancer.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webacl.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_wafregional as wafregional
        
        cfn_web_aCL = wafregional.CfnWebACL(self, "MyCfnWebACL",
            default_action=wafregional.CfnWebACL.ActionProperty(
                type="type"
            ),
            metric_name="metricName",
            name="name",
        
            # the properties below are optional
            rules=[wafregional.CfnWebACL.RuleProperty(
                action=wafregional.CfnWebACL.ActionProperty(
                    type="type"
                ),
                priority=123,
                rule_id="ruleId"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        default_action: typing.Union[_IResolvable_da3f097b, typing.Union["CfnWebACL.ActionProperty", typing.Dict[builtins.str, typing.Any]]],
        metric_name: builtins.str,
        name: builtins.str,
        rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWebACL.RuleProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param default_action: The action to perform if none of the ``Rules`` contained in the ``WebACL`` match. The action is specified by the ``WafAction`` object.
        :param metric_name: A name for the metrics for this ``WebACL`` . The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and "Default_Action." You can't change ``MetricName`` after you create the ``WebACL`` .
        :param name: A friendly name or description of the ``WebACL`` . You can't change the name of a ``WebACL`` after you create it.
        :param rules: An array that contains the action for each ``Rule`` in a ``WebACL`` , the priority of the ``Rule`` , and the ID of the ``Rule`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bbcf3ac61d0d160341c299ed8c698832684f26d4d66c66355b14ce961df6cef)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnWebACLProps(
            default_action=default_action,
            metric_name=metric_name,
            name=name,
            rules=rules,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7caa7370a567ade45061b9605b6a2991e0fe950a040b571df7af810782a6a7bc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__70baf8aa1d2fae728d92ebcb1b1b41e271fc0139a0df321ca6ed54be42baec75)
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
    @jsii.member(jsii_name="defaultAction")
    def default_action(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnWebACL.ActionProperty"]:
        '''The action to perform if none of the ``Rules`` contained in the ``WebACL`` match.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnWebACL.ActionProperty"], jsii.get(self, "defaultAction"))

    @default_action.setter
    def default_action(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnWebACL.ActionProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77ebb156369f514370c9d0394df040b6c1a65390666b14f4b2014ed062090372)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultAction", value)

    @builtins.property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        '''A name for the metrics for this ``WebACL`` .'''
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b28a8b8d04c4894c1e5a03fe466ec9793e98903572ce75ad9a56b4cda168dac9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A friendly name or description of the ``WebACL`` .'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4df8480fe6c8bb9b2ce04f20747aba2732012493135eba84c25bf8de8de7a518)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="rules")
    def rules(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWebACL.RuleProperty"]]]]:
        '''An array that contains the action for each ``Rule`` in a ``WebACL`` , the priority of the ``Rule`` , and the ID of the ``Rule`` .'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWebACL.RuleProperty"]]]], jsii.get(self, "rules"))

    @rules.setter
    def rules(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWebACL.RuleProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85b5c49e2fff4c79f26f8fd7230c235f59a86330019aab07ac103a5155cdb287)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rules", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wafregional.CfnWebACL.ActionProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type"},
    )
    class ActionProperty:
        def __init__(self, *, type: builtins.str) -> None:
            '''Specifies the action AWS WAF takes when a web request matches or doesn't match all rule conditions.

            :param type: For actions that are associated with a rule, the action that AWS WAF takes when a web request matches all conditions in a rule. For the default action of a web access control list (ACL), the action that AWS WAF takes when a web request doesn't match all conditions in any rule. Valid settings include the following: - ``ALLOW`` : AWS WAF allows requests - ``BLOCK`` : AWS WAF blocks requests - ``COUNT`` : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can't specify ``COUNT`` for the default action for a WebACL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-action.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wafregional as wafregional
                
                action_property = wafregional.CfnWebACL.ActionProperty(
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__339aa0a3190591eb6decea7cc939e8523cb62edf7e5b9a54a26b59779e8751d2)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }

        @builtins.property
        def type(self) -> builtins.str:
            '''For actions that are associated with a rule, the action that AWS WAF takes when a web request matches all conditions in a rule.

            For the default action of a web access control list (ACL), the action that AWS WAF takes when a web request doesn't match all conditions in any rule.

            Valid settings include the following:

            - ``ALLOW`` : AWS WAF allows requests
            - ``BLOCK`` : AWS WAF blocks requests
            - ``COUNT`` : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can't specify ``COUNT`` for the default action for a WebACL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-action.html#cfn-wafregional-webacl-action-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wafregional.CfnWebACL.RuleProperty",
        jsii_struct_bases=[],
        name_mapping={"action": "action", "priority": "priority", "rule_id": "ruleId"},
    )
    class RuleProperty:
        def __init__(
            self,
            *,
            action: typing.Union[_IResolvable_da3f097b, typing.Union["CfnWebACL.ActionProperty", typing.Dict[builtins.str, typing.Any]]],
            priority: jsii.Number,
            rule_id: builtins.str,
        ) -> None:
            '''A combination of ``ByteMatchSet`` , ``IPSet`` , and/or ``SqlInjectionMatchSet`` objects that identify the web requests that you want to allow, block, or count.

            For example, you might create a ``Rule`` that includes the following predicates:

            - An ``IPSet`` that causes AWS WAF to search for web requests that originate from the IP address ``192.0.2.44``
            - A ``ByteMatchSet`` that causes AWS WAF to search for web requests for which the value of the ``User-Agent`` header is ``BadBot`` .

            To match the settings in this ``Rule`` , a request must originate from ``192.0.2.44`` AND include a ``User-Agent`` header for which the value is ``BadBot`` .

            :param action: The action that AWS WAF takes when a web request matches all conditions in the rule, such as allow, block, or count the request.
            :param priority: The order in which AWS WAF evaluates the rules in a web ACL. AWS WAF evaluates rules with a lower value before rules with a higher value. The value must be a unique integer. If you have multiple rules in a web ACL, the priority numbers do not need to be consecutive.
            :param rule_id: The ID of an AWS WAF Regional rule to associate with a web ACL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-rule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wafregional as wafregional
                
                rule_property = wafregional.CfnWebACL.RuleProperty(
                    action=wafregional.CfnWebACL.ActionProperty(
                        type="type"
                    ),
                    priority=123,
                    rule_id="ruleId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__53f188e2bb16fe5c29e970330e42ef69ce460a6476590d3c0b823b6ee2953bcf)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
                check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
                check_type(argname="argument rule_id", value=rule_id, expected_type=type_hints["rule_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "action": action,
                "priority": priority,
                "rule_id": rule_id,
            }

        @builtins.property
        def action(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnWebACL.ActionProperty"]:
            '''The action that AWS WAF takes when a web request matches all conditions in the rule, such as allow, block, or count the request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-rule.html#cfn-wafregional-webacl-rule-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnWebACL.ActionProperty"], result)

        @builtins.property
        def priority(self) -> jsii.Number:
            '''The order in which AWS WAF evaluates the rules in a web ACL.

            AWS WAF evaluates rules with a lower value before rules with a higher value. The value must be a unique integer. If you have multiple rules in a web ACL, the priority numbers do not need to be consecutive.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-rule.html#cfn-wafregional-webacl-rule-priority
            '''
            result = self._values.get("priority")
            assert result is not None, "Required property 'priority' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def rule_id(self) -> builtins.str:
            '''The ID of an AWS WAF Regional rule to associate with a web ACL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-rule.html#cfn-wafregional-webacl-rule-ruleid
            '''
            result = self._values.get("rule_id")
            assert result is not None, "Required property 'rule_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnWebACLAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_wafregional.CfnWebACLAssociation",
):
    '''.. epigraph::

   This is *AWS WAF Classic* documentation.

    For more information, see `AWS WAF Classic <https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html>`_ in the developer guide.
    .. epigraph::

       *For the latest version of AWS WAF* , use the AWS WAF V2 API and see the `AWS WAF Developer Guide <https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html>`_ . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

    The AWS::WAFRegional::WebACLAssociation resource associates an AWS WAF Regional web access control group (ACL) with a resource.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webaclassociation.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_wafregional as wafregional
        
        cfn_web_aCLAssociation = wafregional.CfnWebACLAssociation(self, "MyCfnWebACLAssociation",
            resource_arn="resourceArn",
            web_acl_id="webAclId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        resource_arn: builtins.str,
        web_acl_id: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param resource_arn: The Amazon Resource Name (ARN) of the resource to protect with the web ACL.
        :param web_acl_id: A unique identifier (ID) for the web ACL.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39793199b53ca00e4e43a3114987c2b16cb141a0a8debae9a9c51e5d58f33c24)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnWebACLAssociationProps(
            resource_arn=resource_arn, web_acl_id=web_acl_id
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbe41a5c19e716a5b8ce56955b8a44779f4970efb6934ba18920d0a2eefa95ca)
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
            type_hints = typing.get_type_hints(_typecheckingstub__906fbb320712283460373a5d2bdfd95cd5f42a199b20514d933ad5156ec10abd)
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
        '''The Amazon Resource Name (ARN) of the resource to protect with the web ACL.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4515d8b3823db93c464de0c55c368072f036b513e8ac7f100f29ac4c0278c858)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value)

    @builtins.property
    @jsii.member(jsii_name="webAclId")
    def web_acl_id(self) -> builtins.str:
        '''A unique identifier (ID) for the web ACL.'''
        return typing.cast(builtins.str, jsii.get(self, "webAclId"))

    @web_acl_id.setter
    def web_acl_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40feff6d9c61c27d87193f055fb66ab40c303a0cffbc391a343043044018c4c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "webAclId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_wafregional.CfnWebACLAssociationProps",
    jsii_struct_bases=[],
    name_mapping={"resource_arn": "resourceArn", "web_acl_id": "webAclId"},
)
class CfnWebACLAssociationProps:
    def __init__(self, *, resource_arn: builtins.str, web_acl_id: builtins.str) -> None:
        '''Properties for defining a ``CfnWebACLAssociation``.

        :param resource_arn: The Amazon Resource Name (ARN) of the resource to protect with the web ACL.
        :param web_acl_id: A unique identifier (ID) for the web ACL.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webaclassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_wafregional as wafregional
            
            cfn_web_aCLAssociation_props = wafregional.CfnWebACLAssociationProps(
                resource_arn="resourceArn",
                web_acl_id="webAclId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ae44785c9827e49a48b32868ea26704c6bc211021143d19de80d20425709d39)
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            check_type(argname="argument web_acl_id", value=web_acl_id, expected_type=type_hints["web_acl_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_arn": resource_arn,
            "web_acl_id": web_acl_id,
        }

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the resource to protect with the web ACL.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webaclassociation.html#cfn-wafregional-webaclassociation-resourcearn
        '''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def web_acl_id(self) -> builtins.str:
        '''A unique identifier (ID) for the web ACL.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webaclassociation.html#cfn-wafregional-webaclassociation-webaclid
        '''
        result = self._values.get("web_acl_id")
        assert result is not None, "Required property 'web_acl_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWebACLAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_wafregional.CfnWebACLProps",
    jsii_struct_bases=[],
    name_mapping={
        "default_action": "defaultAction",
        "metric_name": "metricName",
        "name": "name",
        "rules": "rules",
    },
)
class CfnWebACLProps:
    def __init__(
        self,
        *,
        default_action: typing.Union[_IResolvable_da3f097b, typing.Union[CfnWebACL.ActionProperty, typing.Dict[builtins.str, typing.Any]]],
        metric_name: builtins.str,
        name: builtins.str,
        rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWebACL.RuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnWebACL``.

        :param default_action: The action to perform if none of the ``Rules`` contained in the ``WebACL`` match. The action is specified by the ``WafAction`` object.
        :param metric_name: A name for the metrics for this ``WebACL`` . The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and "Default_Action." You can't change ``MetricName`` after you create the ``WebACL`` .
        :param name: A friendly name or description of the ``WebACL`` . You can't change the name of a ``WebACL`` after you create it.
        :param rules: An array that contains the action for each ``Rule`` in a ``WebACL`` , the priority of the ``Rule`` , and the ID of the ``Rule`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webacl.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_wafregional as wafregional
            
            cfn_web_aCLProps = wafregional.CfnWebACLProps(
                default_action=wafregional.CfnWebACL.ActionProperty(
                    type="type"
                ),
                metric_name="metricName",
                name="name",
            
                # the properties below are optional
                rules=[wafregional.CfnWebACL.RuleProperty(
                    action=wafregional.CfnWebACL.ActionProperty(
                        type="type"
                    ),
                    priority=123,
                    rule_id="ruleId"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__000aafbc61e54d9f58102054221c8d77d52d3eca2a7cedba5af2e2fcde422968)
            check_type(argname="argument default_action", value=default_action, expected_type=type_hints["default_action"])
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "default_action": default_action,
            "metric_name": metric_name,
            "name": name,
        }
        if rules is not None:
            self._values["rules"] = rules

    @builtins.property
    def default_action(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnWebACL.ActionProperty]:
        '''The action to perform if none of the ``Rules`` contained in the ``WebACL`` match.

        The action is specified by the ``WafAction`` object.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webacl.html#cfn-wafregional-webacl-defaultaction
        '''
        result = self._values.get("default_action")
        assert result is not None, "Required property 'default_action' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnWebACL.ActionProperty], result)

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''A name for the metrics for this ``WebACL`` .

        The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and "Default_Action." You can't change ``MetricName`` after you create the ``WebACL`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webacl.html#cfn-wafregional-webacl-metricname
        '''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A friendly name or description of the ``WebACL`` .

        You can't change the name of a ``WebACL`` after you create it.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webacl.html#cfn-wafregional-webacl-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rules(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnWebACL.RuleProperty]]]]:
        '''An array that contains the action for each ``Rule`` in a ``WebACL`` , the priority of the ``Rule`` , and the ID of the ``Rule`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webacl.html#cfn-wafregional-webacl-rules
        '''
        result = self._values.get("rules")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnWebACL.RuleProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWebACLProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnXssMatchSet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_wafregional.CfnXssMatchSet",
):
    '''.. epigraph::

   This is *AWS WAF Classic* documentation.

    For more information, see `AWS WAF Classic <https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html>`_ in the developer guide.
    .. epigraph::

       *For the latest version of AWS WAF* , use the AWS WAF V2 API and see the `AWS WAF Developer Guide <https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html>`_ . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

    A complex type that contains ``XssMatchTuple`` objects, which specify the parts of web requests that you want AWS WAF to inspect for cross-site scripting attacks and, if you want AWS WAF to inspect a header, the name of the header. If a ``XssMatchSet`` contains more than one ``XssMatchTuple`` object, a request needs to include cross-site scripting attacks in only one of the specified parts of the request to be considered a match.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-xssmatchset.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_wafregional as wafregional
        
        cfn_xss_match_set = wafregional.CfnXssMatchSet(self, "MyCfnXssMatchSet",
            name="name",
        
            # the properties below are optional
            xss_match_tuples=[wafregional.CfnXssMatchSet.XssMatchTupleProperty(
                field_to_match=wafregional.CfnXssMatchSet.FieldToMatchProperty(
                    type="type",
        
                    # the properties below are optional
                    data="data"
                ),
                text_transformation="textTransformation"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        xss_match_tuples: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnXssMatchSet.XssMatchTupleProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name, if any, of the ``XssMatchSet`` .
        :param xss_match_tuples: Specifies the parts of web requests that you want to inspect for cross-site scripting attacks.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b678a59295ccf6f6a1ebf6fd8e7c0db6e955a4478206fd92f0c9021be28f048)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnXssMatchSetProps(name=name, xss_match_tuples=xss_match_tuples)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8862c3f6a8a90fac054bf377747a203a8010a186bce6ef7550482191779e5673)
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
            type_hints = typing.get_type_hints(_typecheckingstub__062d1f341a04bd2a465294aca3fe1923f21d3f7848ad3add51bd5198a7218830)
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
        '''The name, if any, of the ``XssMatchSet`` .'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6b521f961f32fd7c0fba3550b6cd0760612db2638155844312ab9d4c1ff6d8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="xssMatchTuples")
    def xss_match_tuples(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnXssMatchSet.XssMatchTupleProperty"]]]]:
        '''Specifies the parts of web requests that you want to inspect for cross-site scripting attacks.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnXssMatchSet.XssMatchTupleProperty"]]]], jsii.get(self, "xssMatchTuples"))

    @xss_match_tuples.setter
    def xss_match_tuples(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnXssMatchSet.XssMatchTupleProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7573e70ff835de51119b3f9673f5e0a0ef03d347ac12352c2ecf975d234f0915)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xssMatchTuples", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wafregional.CfnXssMatchSet.FieldToMatchProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "data": "data"},
    )
    class FieldToMatchProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            data: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The part of a web request that you want AWS WAF to inspect, such as a specific header or a query string.

            :param type: The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following: - ``HEADER`` : A specified request header, for example, the value of the ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the header in ``Data`` . - ``METHOD`` : The HTTP method, which indicates the type of operation that the request is asking the origin to perform. - ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a ``?`` character, if any. - ``URI`` : The part of a web request that identifies a resource, for example, ``/images/daily-ad.jpg`` . - ``BODY`` : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. - ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30 characters. - ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in ``TargetString`` .
            :param data: When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the header is not case sensitive. When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The parameter name is not case sensitive. If the value of ``Type`` is any other value, omit ``Data`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-fieldtomatch.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wafregional as wafregional
                
                field_to_match_property = wafregional.CfnXssMatchSet.FieldToMatchProperty(
                    type="type",
                
                    # the properties below are optional
                    data="data"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8832f1bd269d6d2286eb9390f554e7974fce880eecbac338b3ebc8b6831611f0)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if data is not None:
                self._values["data"] = data

        @builtins.property
        def type(self) -> builtins.str:
            '''The part of the web request that you want AWS WAF to search for a specified string.

            Parts of a request that you can search include the following:

            - ``HEADER`` : A specified request header, for example, the value of the ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the header in ``Data`` .
            - ``METHOD`` : The HTTP method, which indicates the type of operation that the request is asking the origin to perform.
            - ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a ``?`` character, if any.
            - ``URI`` : The part of a web request that identifies a resource, for example, ``/images/daily-ad.jpg`` .
            - ``BODY`` : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set.
            - ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30 characters.
            - ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in ``TargetString`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-fieldtomatch.html#cfn-wafregional-xssmatchset-fieldtomatch-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def data(self) -> typing.Optional[builtins.str]:
            '''When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS WAF to search, for example, ``User-Agent`` or ``Referer`` .

            The name of the header is not case sensitive.

            When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The parameter name is not case sensitive.

            If the value of ``Type`` is any other value, omit ``Data`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-fieldtomatch.html#cfn-wafregional-xssmatchset-fieldtomatch-data
            '''
            result = self._values.get("data")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FieldToMatchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wafregional.CfnXssMatchSet.XssMatchTupleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "field_to_match": "fieldToMatch",
            "text_transformation": "textTransformation",
        },
    )
    class XssMatchTupleProperty:
        def __init__(
            self,
            *,
            field_to_match: typing.Union[_IResolvable_da3f097b, typing.Union["CfnXssMatchSet.FieldToMatchProperty", typing.Dict[builtins.str, typing.Any]]],
            text_transformation: builtins.str,
        ) -> None:
            '''.. epigraph::

   This is *AWS WAF Classic* documentation.

            For more information, see `AWS WAF Classic <https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html>`_ in the developer guide.
            .. epigraph::

               *For the latest version of AWS WAF* , use the AWS WAF V2 API and see the `AWS WAF Developer Guide <https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html>`_ . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

            Specifies the part of a web request that you want AWS WAF to inspect for cross-site scripting attacks and, if you want AWS WAF to inspect a header, the name of the header.

            :param field_to_match: The part of a web request that you want AWS WAF to inspect, such as a specified header or a query string.
            :param text_transformation: Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF . If you specify a transformation, AWS WAF performs the transformation on ``FieldToMatch`` before inspecting it for a match. You can only specify a single type of TextTransformation. *CMD_LINE* When you're concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations: - Delete the following characters: \\ " ' ^ - Delete spaces before the following characters: / ( - Replace the following characters with a space: , ; - Replace multiple spaces with one space - Convert uppercase letters (A-Z) to lowercase (a-z) *COMPRESS_WHITE_SPACE* Use this option to replace the following characters with a space character (decimal 32): - \\f, formfeed, decimal 12 - \\t, tab, decimal 9 - \\n, newline, decimal 10 - \\r, carriage return, decimal 13 - \\v, vertical tab, decimal 11 - non-breaking space, decimal 160 ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space. *HTML_ENTITY_DECODE* Use this option to replace HTML-encoded characters with unencoded characters. ``HTML_ENTITY_DECODE`` performs the following operations: - Replaces ``(ampersand)quot;`` with ``"`` - Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160 - Replaces ``(ampersand)lt;`` with a "less than" symbol - Replaces ``(ampersand)gt;`` with ``>`` - Replaces characters that are represented in hexadecimal format, ``(ampersand)#xhhhh;`` , with the corresponding characters - Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` , with the corresponding characters *LOWERCASE* Use this option to convert uppercase letters (A-Z) to lowercase (a-z). *URL_DECODE* Use this option to decode a URL-encoded value. *NONE* Specify ``NONE`` if you don't want to perform any text transformations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-xssmatchtuple.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wafregional as wafregional
                
                xss_match_tuple_property = wafregional.CfnXssMatchSet.XssMatchTupleProperty(
                    field_to_match=wafregional.CfnXssMatchSet.FieldToMatchProperty(
                        type="type",
                
                        # the properties below are optional
                        data="data"
                    ),
                    text_transformation="textTransformation"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__86e49651456c9dd49db43bf292fa1c7bb5f1c316cd7ed28e07995b11e3fae9e7)
                check_type(argname="argument field_to_match", value=field_to_match, expected_type=type_hints["field_to_match"])
                check_type(argname="argument text_transformation", value=text_transformation, expected_type=type_hints["text_transformation"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "field_to_match": field_to_match,
                "text_transformation": text_transformation,
            }

        @builtins.property
        def field_to_match(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnXssMatchSet.FieldToMatchProperty"]:
            '''The part of a web request that you want AWS WAF to inspect, such as a specified header or a query string.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-xssmatchtuple.html#cfn-wafregional-xssmatchset-xssmatchtuple-fieldtomatch
            '''
            result = self._values.get("field_to_match")
            assert result is not None, "Required property 'field_to_match' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnXssMatchSet.FieldToMatchProperty"], result)

        @builtins.property
        def text_transformation(self) -> builtins.str:
            '''Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF .

            If you specify a transformation, AWS WAF performs the transformation on ``FieldToMatch`` before inspecting it for a match.

            You can only specify a single type of TextTransformation.

            *CMD_LINE*

            When you're concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

            - Delete the following characters: \\ " ' ^
            - Delete spaces before the following characters: / (
            - Replace the following characters with a space: , ;
            - Replace multiple spaces with one space
            - Convert uppercase letters (A-Z) to lowercase (a-z)

            *COMPRESS_WHITE_SPACE*

            Use this option to replace the following characters with a space character (decimal 32):

            - \\f, formfeed, decimal 12
            - \\t, tab, decimal 9
            - \\n, newline, decimal 10
            - \\r, carriage return, decimal 13
            - \\v, vertical tab, decimal 11
            - non-breaking space, decimal 160

            ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

            *HTML_ENTITY_DECODE*

            Use this option to replace HTML-encoded characters with unencoded characters. ``HTML_ENTITY_DECODE`` performs the following operations:

            - Replaces ``(ampersand)quot;`` with ``"``
            - Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160
            - Replaces ``(ampersand)lt;`` with a "less than" symbol
            - Replaces ``(ampersand)gt;`` with ``>``
            - Replaces characters that are represented in hexadecimal format, ``(ampersand)#xhhhh;`` , with the corresponding characters
            - Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` , with the corresponding characters

            *LOWERCASE*

            Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

            *URL_DECODE*

            Use this option to decode a URL-encoded value.

            *NONE*

            Specify ``NONE`` if you don't want to perform any text transformations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-xssmatchtuple.html#cfn-wafregional-xssmatchset-xssmatchtuple-texttransformation
            '''
            result = self._values.get("text_transformation")
            assert result is not None, "Required property 'text_transformation' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "XssMatchTupleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_wafregional.CfnXssMatchSetProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "xss_match_tuples": "xssMatchTuples"},
)
class CfnXssMatchSetProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        xss_match_tuples: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnXssMatchSet.XssMatchTupleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnXssMatchSet``.

        :param name: The name, if any, of the ``XssMatchSet`` .
        :param xss_match_tuples: Specifies the parts of web requests that you want to inspect for cross-site scripting attacks.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-xssmatchset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_wafregional as wafregional
            
            cfn_xss_match_set_props = wafregional.CfnXssMatchSetProps(
                name="name",
            
                # the properties below are optional
                xss_match_tuples=[wafregional.CfnXssMatchSet.XssMatchTupleProperty(
                    field_to_match=wafregional.CfnXssMatchSet.FieldToMatchProperty(
                        type="type",
            
                        # the properties below are optional
                        data="data"
                    ),
                    text_transformation="textTransformation"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__226d7e9140a891516c1c39937b2335bc5329713cb50c4e5f0758e8d4fc74c4f7)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument xss_match_tuples", value=xss_match_tuples, expected_type=type_hints["xss_match_tuples"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if xss_match_tuples is not None:
            self._values["xss_match_tuples"] = xss_match_tuples

    @builtins.property
    def name(self) -> builtins.str:
        '''The name, if any, of the ``XssMatchSet`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-xssmatchset.html#cfn-wafregional-xssmatchset-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def xss_match_tuples(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnXssMatchSet.XssMatchTupleProperty]]]]:
        '''Specifies the parts of web requests that you want to inspect for cross-site scripting attacks.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-xssmatchset.html#cfn-wafregional-xssmatchset-xssmatchtuples
        '''
        result = self._values.get("xss_match_tuples")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnXssMatchSet.XssMatchTupleProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnXssMatchSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnByteMatchSet",
    "CfnByteMatchSetProps",
    "CfnGeoMatchSet",
    "CfnGeoMatchSetProps",
    "CfnIPSet",
    "CfnIPSetProps",
    "CfnRateBasedRule",
    "CfnRateBasedRuleProps",
    "CfnRegexPatternSet",
    "CfnRegexPatternSetProps",
    "CfnRule",
    "CfnRuleProps",
    "CfnSizeConstraintSet",
    "CfnSizeConstraintSetProps",
    "CfnSqlInjectionMatchSet",
    "CfnSqlInjectionMatchSetProps",
    "CfnWebACL",
    "CfnWebACLAssociation",
    "CfnWebACLAssociationProps",
    "CfnWebACLProps",
    "CfnXssMatchSet",
    "CfnXssMatchSetProps",
]

publication.publish()

def _typecheckingstub__e708169d746906ecd9d668a57583fd77b92049101a7b42aaf2d48555f189e6e8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    byte_match_tuples: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnByteMatchSet.ByteMatchTupleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea460cfe61ff551d95ffb61ada21b904430d986ea13f30d0c4b789ed5946b4cd(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7f70a1150cc6a5ccbb4a8525c046cb151ebfcef8d6e8610d8822dd25b44909d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e3fd8c2f928a54bc15ca33b7b11d1b205815279375aa299a6e66e53c81a69d8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3bdd0c3bf2f1a3268342f199ac37f3c9d3704be0bf88f0b85a5b4fac81294cf(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnByteMatchSet.ByteMatchTupleProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e44b397423d4132bd5d65f37916270d0ba93f2dc8760e37e7d32874c2346364(
    *,
    field_to_match: typing.Union[_IResolvable_da3f097b, typing.Union[CfnByteMatchSet.FieldToMatchProperty, typing.Dict[builtins.str, typing.Any]]],
    positional_constraint: builtins.str,
    text_transformation: builtins.str,
    target_string: typing.Optional[builtins.str] = None,
    target_string_base64: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__640c9a931daf57d6d8a41f83df9bd8de256aec1220f1b860b3316bd9134494d2(
    *,
    type: builtins.str,
    data: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d3315ca0f0c432ea54dc0a28b013ee804e72f866e20f3164467df22a3679b29(
    *,
    name: builtins.str,
    byte_match_tuples: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnByteMatchSet.ByteMatchTupleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f5defa886ad07662ce07608ef11d4f182985ba3ca56ba02873d46b5f8629b43(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    geo_match_constraints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGeoMatchSet.GeoMatchConstraintProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f6bafffd0f7b74cee5606a2d95f943cc5ac49a2560960db6fdfdb298b40f982(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65322f9d0fd5be8dfe4ab1e62760ccd49f6559e244979e10e7e0ac91c5761924(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd355eff3f62f2152cd03e0b7ce0da682ff29432c59a743bb4a649626c9c2af7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64d21a9e81545c51476c160c33fa317b6908f4f1b44d7a03d47b22d5bd55391e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGeoMatchSet.GeoMatchConstraintProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdccc52297904d6ff0d4704e82129d56f752a9d570c4f100e64bb95fbde18278(
    *,
    type: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ce26d9ffd24f477f686b44477cc2e54588d1ce675a04c4e2970b3226c84d38e(
    *,
    name: builtins.str,
    geo_match_constraints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGeoMatchSet.GeoMatchConstraintProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24af5fe749b4ec99d6661f61836984c1ee1ea8f65bfb2e1309de62e8148e8adf(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    ip_set_descriptors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIPSet.IPSetDescriptorProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e517874a1630bb2cdf2cae335ebbaa598305f5e5f1f4904a234e310e13f7e33e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e59cc971a79420af060d720f9dab45125bdab1f1d161d6fd0212288059240ea(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e8d9bc40ccea4e69d11cc36300ed6e414f959745336a30e2f40940cc8f4efe2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6d42c2bbdf2fdfd5f1729c0ee8fa6b528f0ec97e34d0bccd32a470e817f41f0(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnIPSet.IPSetDescriptorProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fc3d521e61aad5c8ee04774898a6f73b99447c7fa553cc634602b002683f070(
    *,
    type: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66ca7761765b7ff9b3a37c94c1330ce44b8771049c38acc8da230f52e7db0708(
    *,
    name: builtins.str,
    ip_set_descriptors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIPSet.IPSetDescriptorProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e3a48130b6ea11cbba89c4d925188b1035288d0d20e62521703f08011393fa3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    metric_name: builtins.str,
    name: builtins.str,
    rate_key: builtins.str,
    rate_limit: jsii.Number,
    match_predicates: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRateBasedRule.PredicateProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe15f950b117768ac352dd2f4184cee3df82ef2ee62d049f3cdc241483ab0d1d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e95faf77cdcbaa5b2c40b3bcdf27d9ffe50f7ffeed4938a93f049bfc7a4dc2c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cfbc388b210d0582e04f751e60b45dd5b6bd3e72f02db2e98e85bef7ef56773(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18ee093de7963dade7fd8f8af22735ddb09cbd49363ebb15bb550835d9a10364(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3936a70c79c88ceefcad7595ee96846e384c29bd9b33e3ff8ff346064fde0d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05afa6fb83dc358397e8b0131bf464c079de2a415360ff4939536959254d4e24(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d03374c15b5e840bcddc8023a356ee3f22e2a776ff29025aa619ae7a754b2559(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnRateBasedRule.PredicateProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d862aab74caa6d90bd5f556c0ed61443009c5c844166ebbd2e40c13a6ed14e2(
    *,
    data_id: builtins.str,
    negated: typing.Union[builtins.bool, _IResolvable_da3f097b],
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a5eb8767b8573e01975210155ccbe383a96e2861b6e27912a562e89c4067821(
    *,
    metric_name: builtins.str,
    name: builtins.str,
    rate_key: builtins.str,
    rate_limit: jsii.Number,
    match_predicates: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRateBasedRule.PredicateProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc3290467cef7693ba0befd862e65e1c1db0f772a4356bde5baff5c34f116b38(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    regex_pattern_strings: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00571de7ee75e9fb7d683c9f103043ed8aea8e0e3aacc3f28c181c84dfc2b916(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8280578e704e7c17c211a898942b98f9f0a27a21d61aebfb93c7b554b5a310e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8a9c9bc78e70485e2b2192fe0f5562437ca978b52817dea6b0fa3ea2aa2e212(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c733d882b2636c9f3e83cbe3d3d3c45524e31baf8e0aefb580fcf499692ae821(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd2ba4ff373b9395d24df058327f71925859a4bbea04883bbecccd2cf281db74(
    *,
    name: builtins.str,
    regex_pattern_strings: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e8feae8cde7fd0a6a33c087a6bc2f530d0a2d84faa4c8473adff422fe6705fe(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    metric_name: builtins.str,
    name: builtins.str,
    predicates: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.PredicateProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7702269394d1e5c3a77ce69b746f977ab20cd8769b7a0b2b47bb0bb1cf466f16(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e8db74916fdd8e035f7d8fdf7c40ba0ff2149e206496918548e19340d4e9de8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6582f1ad9068d271bf929638d404c43ce4a7294b13f162946e1d16969c363edd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae5c51af1e876790fd6d0be1510173bf597796956acb2d0e6a515db559ed94c6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f724ad55a0692458dfb9454847b548911c8e6b4f0c4ee20bc0195bd82c54f3ec(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnRule.PredicateProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cc39471795f985fdd66736c51389bb4064b463605d224670988abb34e37881e(
    *,
    data_id: builtins.str,
    negated: typing.Union[builtins.bool, _IResolvable_da3f097b],
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdc102021e417a504401cd27c9a5d604cd6be3ce5473501b852f107ddfdb257b(
    *,
    metric_name: builtins.str,
    name: builtins.str,
    predicates: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.PredicateProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3617242c65fe4a2405945be806ebc94732125d50948fdc61e6bfc3017667c0b3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    size_constraints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSizeConstraintSet.SizeConstraintProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8e40f87fdc57eff0e9208037fed9950431c54262a5933c7fc441600b2f2952b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87c74e8a80680d49334aed17e7005e3d0784bb5ae261700d5945a65e7011d076(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff5fd08bc9276e64954323aeff7d7f98ba67f832e5bfa54e3a04eafd0977cfbb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed10db9ee0b6303854a666f25e1251855886884dd58f67884c32b8f4bdbfe468(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnSizeConstraintSet.SizeConstraintProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c9becc0d0d2ffe051374f750cd582e90321160bd7a3123162da9a16e0226be8(
    *,
    type: builtins.str,
    data: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bd0b350acf83dad556bc4a4642cf56c05406c80b304c48c6f9978cc0b6fcefd(
    *,
    comparison_operator: builtins.str,
    field_to_match: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSizeConstraintSet.FieldToMatchProperty, typing.Dict[builtins.str, typing.Any]]],
    size: jsii.Number,
    text_transformation: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf80c55882638ea37cfa7a142fc6f1adcee512250a5dc52e55c3ebaf0d3916f9(
    *,
    name: builtins.str,
    size_constraints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSizeConstraintSet.SizeConstraintProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd9e0f900ac8b2a5f047d3bd88768dc62f95c2451091386675727ceef64e59a8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    sql_injection_match_tuples: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSqlInjectionMatchSet.SqlInjectionMatchTupleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c31baabf0f1513b14ade51b1baa82fd3a13ebf2f9d357484ef5e959a3167f52(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a7e4f5a844750e6530efce17048877a42dd27c09734193ce34675fee637e8a0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__821f3800915744d3ffeab016ddfa93507a82ab75f2469faeb24a18e99c0a8e16(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36e43d4ce4ce856f540724f26bbc23e2cb13b58361de226358a8285ca8e3eba5(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnSqlInjectionMatchSet.SqlInjectionMatchTupleProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74bf0200de57ed765f39e71220fec1aa20f6ac62241a5295a52368b0b8791950(
    *,
    type: builtins.str,
    data: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a28b84fb8065ea3716ec026d7e9acbc436d5c02ce29d073ed967129e4304751(
    *,
    field_to_match: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSqlInjectionMatchSet.FieldToMatchProperty, typing.Dict[builtins.str, typing.Any]]],
    text_transformation: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb86879a015cba2fd0a9fb28d3c9e047ee07933c06f46f2a05813de3c6381635(
    *,
    name: builtins.str,
    sql_injection_match_tuples: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSqlInjectionMatchSet.SqlInjectionMatchTupleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bbcf3ac61d0d160341c299ed8c698832684f26d4d66c66355b14ce961df6cef(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    default_action: typing.Union[_IResolvable_da3f097b, typing.Union[CfnWebACL.ActionProperty, typing.Dict[builtins.str, typing.Any]]],
    metric_name: builtins.str,
    name: builtins.str,
    rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWebACL.RuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7caa7370a567ade45061b9605b6a2991e0fe950a040b571df7af810782a6a7bc(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70baf8aa1d2fae728d92ebcb1b1b41e271fc0139a0df321ca6ed54be42baec75(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77ebb156369f514370c9d0394df040b6c1a65390666b14f4b2014ed062090372(
    value: typing.Union[_IResolvable_da3f097b, CfnWebACL.ActionProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b28a8b8d04c4894c1e5a03fe466ec9793e98903572ce75ad9a56b4cda168dac9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4df8480fe6c8bb9b2ce04f20747aba2732012493135eba84c25bf8de8de7a518(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85b5c49e2fff4c79f26f8fd7230c235f59a86330019aab07ac103a5155cdb287(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnWebACL.RuleProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__339aa0a3190591eb6decea7cc939e8523cb62edf7e5b9a54a26b59779e8751d2(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53f188e2bb16fe5c29e970330e42ef69ce460a6476590d3c0b823b6ee2953bcf(
    *,
    action: typing.Union[_IResolvable_da3f097b, typing.Union[CfnWebACL.ActionProperty, typing.Dict[builtins.str, typing.Any]]],
    priority: jsii.Number,
    rule_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39793199b53ca00e4e43a3114987c2b16cb141a0a8debae9a9c51e5d58f33c24(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    resource_arn: builtins.str,
    web_acl_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbe41a5c19e716a5b8ce56955b8a44779f4970efb6934ba18920d0a2eefa95ca(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__906fbb320712283460373a5d2bdfd95cd5f42a199b20514d933ad5156ec10abd(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4515d8b3823db93c464de0c55c368072f036b513e8ac7f100f29ac4c0278c858(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40feff6d9c61c27d87193f055fb66ab40c303a0cffbc391a343043044018c4c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ae44785c9827e49a48b32868ea26704c6bc211021143d19de80d20425709d39(
    *,
    resource_arn: builtins.str,
    web_acl_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__000aafbc61e54d9f58102054221c8d77d52d3eca2a7cedba5af2e2fcde422968(
    *,
    default_action: typing.Union[_IResolvable_da3f097b, typing.Union[CfnWebACL.ActionProperty, typing.Dict[builtins.str, typing.Any]]],
    metric_name: builtins.str,
    name: builtins.str,
    rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWebACL.RuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b678a59295ccf6f6a1ebf6fd8e7c0db6e955a4478206fd92f0c9021be28f048(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    xss_match_tuples: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnXssMatchSet.XssMatchTupleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8862c3f6a8a90fac054bf377747a203a8010a186bce6ef7550482191779e5673(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__062d1f341a04bd2a465294aca3fe1923f21d3f7848ad3add51bd5198a7218830(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6b521f961f32fd7c0fba3550b6cd0760612db2638155844312ab9d4c1ff6d8f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7573e70ff835de51119b3f9673f5e0a0ef03d347ac12352c2ecf975d234f0915(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnXssMatchSet.XssMatchTupleProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8832f1bd269d6d2286eb9390f554e7974fce880eecbac338b3ebc8b6831611f0(
    *,
    type: builtins.str,
    data: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86e49651456c9dd49db43bf292fa1c7bb5f1c316cd7ed28e07995b11e3fae9e7(
    *,
    field_to_match: typing.Union[_IResolvable_da3f097b, typing.Union[CfnXssMatchSet.FieldToMatchProperty, typing.Dict[builtins.str, typing.Any]]],
    text_transformation: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__226d7e9140a891516c1c39937b2335bc5329713cb50c4e5f0758e8d4fc74c4f7(
    *,
    name: builtins.str,
    xss_match_tuples: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnXssMatchSet.XssMatchTupleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
