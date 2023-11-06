'''
# AWS::Macie Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_macie as macie
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Macie construct libraries](https://constructs.dev/search?q=macie)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Macie resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Macie.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Macie](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Macie.html).

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
class CfnAllowList(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_macie.CfnAllowList",
):
    '''The ``AWS::Macie::AllowList`` resource specifies an allow list.

    In Amazon Macie , an allow list defines specific text or a text pattern for Macie to ignore when it inspects data sources for sensitive data. If data matches text or a text pattern in an allow list, Macie doesn’t report the data in sensitive data findings or sensitive data discovery results, even if the data matches the criteria of a custom data identifier or a managed data identifier. You can create and use allow lists in all the AWS Regions where Macie is currently available except the Asia Pacific (Osaka) Region.

    Macie supports two types of allow lists:

    - *Predefined text* - For this type of list ( ``S3WordsList`` ), you create a line-delimited plaintext file that lists specific text to ignore, and you store the file in an Amazon Simple Storage Service ( Amazon S3 ) bucket. You then configure settings for Macie to access the list in the bucket.

    This type of list typically contains specific words, phrases, and other kinds of character sequences that aren’t sensitive, aren't likely to change, and don’t necessarily adhere to a common pattern. If you use this type of list, Macie doesn't report occurrences of text that exactly match a complete entry in the list. Macie treats each entry in the list as a string literal value. Matches aren't case sensitive.

    - *Regular expression* - For this type of list ( ``Regex`` ), you specify a regular expression that defines a text pattern to ignore. Unlike an allow list with predefined text, you store the regex and all other list settings in Macie .

    This type of list is helpful if you want to specify text that isn’t sensitive but varies or is likely to change while also adhering to a common pattern. If you use this type of list, Macie doesn't report occurrences of text that completely match the pattern defined by the list.

    For more information, see `Defining sensitive data exceptions with allow lists <https://docs.aws.amazon.com/macie/latest/user/allow-lists.html>`_ in the *Amazon Macie User Guide* .

    An ``AWS::Macie::Session`` resource must exist for an AWS account before you can create an ``AWS::Macie::AllowList`` resource for the account. Use a `DependsOn attribute <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html>`_ to ensure that an ``AWS::Macie::Session`` resource is created before other Macie resources are created for an account. For example, ``"DependsOn": "Session"`` .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-allowlist.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_macie as macie
        
        cfn_allow_list = macie.CfnAllowList(self, "MyCfnAllowList",
            criteria=macie.CfnAllowList.CriteriaProperty(
                regex="regex",
                s3_words_list=macie.CfnAllowList.S3WordsListProperty(
                    bucket_name="bucketName",
                    object_key="objectKey"
                )
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
        criteria: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAllowList.CriteriaProperty", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param criteria: The criteria that specify the text or text pattern to ignore. The criteria can be the location and name of an Amazon S3 object that lists specific text to ignore ( ``S3WordsList`` ), or a regular expression ( ``Regex`` ) that defines a text pattern to ignore.
        :param name: A custom name for the allow list. The name can contain 1-128 characters.
        :param description: A custom description of the allow list. The description can contain 1-512 characters.
        :param tags: An array of key-value pairs to apply to the allow list. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef55cb8aaca32dcf264ac0e8768dc1c5a0b1471c41c8de3c9575f20000ca4bd9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAllowListProps(
            criteria=criteria, name=name, description=description, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de89a42feae1bdccf1b7fb468bda2c5700b1aa71c5c523cb2c69a8c666ae8e2a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7369f7a4bca5c49d764dbf34faf902a40c52828d8fba955e4eca05e9adcaff7a)
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
        '''The Amazon Resource Name (ARN) of the allow list.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The unique identifier for the allow list.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The current status of the allow list, which indicates whether Amazon Macie can access and use the list's criteria.

        If the list's criteria specify a regular expression ( ``Regex`` ), this value is typically ``OK`` . Macie can compile the expression. If the list's criteria specify an Amazon S3 object ( ``S3WordsList`` ), possible values are:

        - ``OK`` - Macie can retrieve and parse the contents of the object.
        - ``S3_OBJECT_ACCESS_DENIED`` - Macie isn't allowed to access the object or the object is encrypted with a customer managed AWS KMS key that Macie isn't allowed to use. Check the bucket policy and other permissions settings for the bucket and the object. If the object is encrypted, also ensure that it's encrypted with a key that Macie is allowed to use.
        - ``S3_OBJECT_EMPTY`` - Macie can retrieve the object but the object doesn't contain any content. Ensure that the object contains the correct entries. Also ensure that the list's criteria specify the correct bucket and object names.
        - ``S3_OBJECT_NOT_FOUND`` - The object doesn't exist in Amazon S3 . Ensure that the list's criteria specify the correct bucket and object names.
        - ``S3_OBJECT_OVERSIZE`` - Macie can retrieve the object. However, the object contains too many entries or its storage size exceeds the quota for an allow list. Try breaking the list into multiple files and ensure that each file doesn't exceed any quotas. Then configure list settings in Macie for each file.
        - ``S3_THROTTLED`` - Amazon S3 throttled the request to retrieve the object. Wait a few minutes and then try again.
        - ``S3_USER_ACCESS_DENIED`` - Amazon S3 denied the request to retrieve the object. If the specified object exists, you're not allowed to access it or it's encrypted with an AWS KMS key that you're not allowed to use. Work with your AWS administrator to ensure that the list's criteria specify the correct bucket and object names, and you have read access to the bucket and the object. If the object is encrypted, also ensure that it's encrypted with a key that you're allowed to use.
        - ``UNKNOWN_ERROR`` - A transient or internal error occurred when Macie attempted to retrieve or parse the object. Wait a few minutes and then try again. A list can also have this status if it's encrypted with a key that Amazon S3 and Macie can't access or use.

        For more information, see `Allow list options and requirements <https://docs.aws.amazon.com/macie/latest/user/allow-lists-options.html>`_ in the *Amazon Macie User Guide* .

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

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
    @jsii.member(jsii_name="criteria")
    def criteria(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnAllowList.CriteriaProperty"]:
        '''The criteria that specify the text or text pattern to ignore.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAllowList.CriteriaProperty"], jsii.get(self, "criteria"))

    @criteria.setter
    def criteria(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnAllowList.CriteriaProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e4ae58b4636b7db31b0fa3adc3410ae3d14049fa02c2bd307123f1749460647)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "criteria", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A custom name for the allow list.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d690571d1b7ea81f4eaac91920c04dab927cd0ddc18b3539a84afdcb50cfdc4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A custom description of the allow list.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eff0733233420991a19ec573286f220cf810fc8bd281a542a9fa2c82daf4c241)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to the allow list.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__142a3b637b387ca2f41ecc60f7492ab453fed61355af5abfd8c68c74fc8f0c16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_macie.CfnAllowList.CriteriaProperty",
        jsii_struct_bases=[],
        name_mapping={"regex": "regex", "s3_words_list": "s3WordsList"},
    )
    class CriteriaProperty:
        def __init__(
            self,
            *,
            regex: typing.Optional[builtins.str] = None,
            s3_words_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAllowList.S3WordsListProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the criteria for an allow list, which is a list that defines specific text or a text pattern to ignore when inspecting data sources for sensitive data.

            The criteria can be:

            - The location and name of an Amazon Simple Storage Service ( Amazon S3 ) object that lists specific, predefined text to ignore ( ``S3WordsList`` ), or
            - A regular expression ( ``Regex`` ) that defines a text pattern to ignore.

            The criteria must specify either an S3 object or a regular expression. It can't specify both.

            :param regex: The regular expression ( *regex* ) that defines the text pattern to ignore. The expression can contain 1-512 characters.
            :param s3_words_list: The location and name of an Amazon S3 object that lists specific text to ignore.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-allowlist-criteria.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_macie as macie
                
                criteria_property = macie.CfnAllowList.CriteriaProperty(
                    regex="regex",
                    s3_words_list=macie.CfnAllowList.S3WordsListProperty(
                        bucket_name="bucketName",
                        object_key="objectKey"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__916c849be567db5e8b2d28b4262b1b5e6cc4efa0cc6749b882394480f94b0f1a)
                check_type(argname="argument regex", value=regex, expected_type=type_hints["regex"])
                check_type(argname="argument s3_words_list", value=s3_words_list, expected_type=type_hints["s3_words_list"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if regex is not None:
                self._values["regex"] = regex
            if s3_words_list is not None:
                self._values["s3_words_list"] = s3_words_list

        @builtins.property
        def regex(self) -> typing.Optional[builtins.str]:
            '''The regular expression ( *regex* ) that defines the text pattern to ignore.

            The expression can contain 1-512 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-allowlist-criteria.html#cfn-macie-allowlist-criteria-regex
            '''
            result = self._values.get("regex")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_words_list(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAllowList.S3WordsListProperty"]]:
            '''The location and name of an Amazon S3 object that lists specific text to ignore.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-allowlist-criteria.html#cfn-macie-allowlist-criteria-s3wordslist
            '''
            result = self._values.get("s3_words_list")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAllowList.S3WordsListProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CriteriaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_macie.CfnAllowList.S3WordsListProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket_name": "bucketName", "object_key": "objectKey"},
    )
    class S3WordsListProperty:
        def __init__(
            self,
            *,
            bucket_name: builtins.str,
            object_key: builtins.str,
        ) -> None:
            '''Specifies the location and name of an Amazon Simple Storage Service ( Amazon S3 ) object that lists specific, predefined text to ignore when inspecting data sources for sensitive data.

            :param bucket_name: The full name of the S3 bucket that contains the object. This value correlates to the ``Name`` field of a bucket's properties in Amazon S3 . This value is case sensitive. In addition, don't use wildcard characters or specify partial values for the name.
            :param object_key: The full name of the S3 object. This value correlates to the ``Key`` field of an object's properties in Amazon S3 . If the name includes a path, include the complete path. For example, ``AllowLists/Macie/MyList.txt`` . This value is case sensitive. In addition, don't use wildcard characters or specify partial values for the name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-allowlist-s3wordslist.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_macie as macie
                
                s3_words_list_property = macie.CfnAllowList.S3WordsListProperty(
                    bucket_name="bucketName",
                    object_key="objectKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6728338d9836f378990a221bfcb5d4ebc176286721060379316cb044250d5933)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument object_key", value=object_key, expected_type=type_hints["object_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_name": bucket_name,
                "object_key": object_key,
            }

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''The full name of the S3 bucket that contains the object.

            This value correlates to the ``Name`` field of a bucket's properties in Amazon S3 .

            This value is case sensitive. In addition, don't use wildcard characters or specify partial values for the name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-allowlist-s3wordslist.html#cfn-macie-allowlist-s3wordslist-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def object_key(self) -> builtins.str:
            '''The full name of the S3 object.

            This value correlates to the ``Key`` field of an object's properties in Amazon S3 . If the name includes a path, include the complete path. For example, ``AllowLists/Macie/MyList.txt`` .

            This value is case sensitive. In addition, don't use wildcard characters or specify partial values for the name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-allowlist-s3wordslist.html#cfn-macie-allowlist-s3wordslist-objectkey
            '''
            result = self._values.get("object_key")
            assert result is not None, "Required property 'object_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3WordsListProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_macie.CfnAllowListProps",
    jsii_struct_bases=[],
    name_mapping={
        "criteria": "criteria",
        "name": "name",
        "description": "description",
        "tags": "tags",
    },
)
class CfnAllowListProps:
    def __init__(
        self,
        *,
        criteria: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAllowList.CriteriaProperty, typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAllowList``.

        :param criteria: The criteria that specify the text or text pattern to ignore. The criteria can be the location and name of an Amazon S3 object that lists specific text to ignore ( ``S3WordsList`` ), or a regular expression ( ``Regex`` ) that defines a text pattern to ignore.
        :param name: A custom name for the allow list. The name can contain 1-128 characters.
        :param description: A custom description of the allow list. The description can contain 1-512 characters.
        :param tags: An array of key-value pairs to apply to the allow list. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-allowlist.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_macie as macie
            
            cfn_allow_list_props = macie.CfnAllowListProps(
                criteria=macie.CfnAllowList.CriteriaProperty(
                    regex="regex",
                    s3_words_list=macie.CfnAllowList.S3WordsListProperty(
                        bucket_name="bucketName",
                        object_key="objectKey"
                    )
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
            type_hints = typing.get_type_hints(_typecheckingstub__4cde4980d3f47e6973fbc0136f9a40cf0f5706f781fb45f3cc0aad4b99e96d39)
            check_type(argname="argument criteria", value=criteria, expected_type=type_hints["criteria"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "criteria": criteria,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def criteria(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnAllowList.CriteriaProperty]:
        '''The criteria that specify the text or text pattern to ignore.

        The criteria can be the location and name of an Amazon S3 object that lists specific text to ignore ( ``S3WordsList`` ), or a regular expression ( ``Regex`` ) that defines a text pattern to ignore.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-allowlist.html#cfn-macie-allowlist-criteria
        '''
        result = self._values.get("criteria")
        assert result is not None, "Required property 'criteria' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnAllowList.CriteriaProperty], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A custom name for the allow list.

        The name can contain 1-128 characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-allowlist.html#cfn-macie-allowlist-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A custom description of the allow list.

        The description can contain 1-512 characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-allowlist.html#cfn-macie-allowlist-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to the allow list.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-allowlist.html#cfn-macie-allowlist-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAllowListProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnCustomDataIdentifier(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_macie.CfnCustomDataIdentifier",
):
    '''The ``AWS::Macie::CustomDataIdentifier`` resource specifies a custom data identifier.

    A *custom data identifier* is a set of custom criteria for Amazon Macie to use when it inspects data sources for sensitive data. The criteria consist of a regular expression ( *regex* ) that defines a text pattern to match and, optionally, character sequences and a proximity rule that refine the results. The character sequences can be:

    - *Keywords* , which are words or phrases that must be in proximity of text that matches the regex, or
    - *Ignore words* , which are words or phrases to exclude from the results.

    By using custom data identifiers, you can supplement the managed data identifiers that Macie provides and detect sensitive data that reflects your particular scenarios, intellectual property, or proprietary data. For more information, see `Building custom data identifiers <https://docs.aws.amazon.com/macie/latest/user/custom-data-identifiers.html>`_ in the *Amazon Macie User Guide* .

    An ``AWS::Macie::Session`` resource must exist for an AWS account before you can create an ``AWS::Macie::CustomDataIdentifier`` resource for the account. Use a `DependsOn attribute <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html>`_ to ensure that an ``AWS::Macie::Session`` resource is created before other Macie resources are created for an account. For example, ``"DependsOn": "Session"`` .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_macie as macie
        
        cfn_custom_data_identifier = macie.CfnCustomDataIdentifier(self, "MyCfnCustomDataIdentifier",
            name="name",
            regex="regex",
        
            # the properties below are optional
            description="description",
            ignore_words=["ignoreWords"],
            keywords=["keywords"],
            maximum_match_distance=123
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        regex: builtins.str,
        description: typing.Optional[builtins.str] = None,
        ignore_words: typing.Optional[typing.Sequence[builtins.str]] = None,
        keywords: typing.Optional[typing.Sequence[builtins.str]] = None,
        maximum_match_distance: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: A custom name for the custom data identifier. The name can contain 1-128 characters. Avoid including sensitive data in the name of a custom data identifier. Users of the account might be able to see the name, depending on the actions that they're allowed to perform in Amazon Macie .
        :param regex: The regular expression ( *regex* ) that defines the text pattern to match. The expression can contain 1-512 characters.
        :param description: A custom description of the custom data identifier. The description can contain 1-512 characters. Avoid including sensitive data in the description. Users of the account might be able to see the description, depending on the actions that they're allowed to perform in Amazon Macie .
        :param ignore_words: An array of character sequences ( *ignore words* ) to exclude from the results. If text matches the regular expression ( ``Regex`` ) but it contains a string in this array, Amazon Macie ignores the text and doesn't include it in the results. The array can contain 1-10 ignore words. Each ignore word can contain 4-90 UTF-8 characters. Ignore words are case sensitive.
        :param keywords: An array of character sequences ( *keywords* ), one of which must precede and be in proximity ( ``MaximumMatchDistance`` ) of the regular expression ( ``Regex`` ) to match. The array can contain 1-50 keywords. Each keyword can contain 3-90 UTF-8 characters. Keywords aren't case sensitive.
        :param maximum_match_distance: The maximum number of characters that can exist between the end of at least one complete character sequence specified by the ``Keywords`` array and the end of text that matches the regular expression ( ``Regex`` ). If a complete keyword precedes all the text that matches the regular expression and the keyword is within the specified distance, Amazon Macie includes the result. The distance can be 1-300 characters. The default value is 50.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8462f70ed2396867e691499b8338ee06166375569e4774b35cad18418587284c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCustomDataIdentifierProps(
            name=name,
            regex=regex,
            description=description,
            ignore_words=ignore_words,
            keywords=keywords,
            maximum_match_distance=maximum_match_distance,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75e9300d86a3080fc43c5b9e06f708ec6e0be23ca1a8b8c548c28f04d4a38b47)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6c2273c82378b08a1921a6584b6eafca3f9442f8236c8797614cdc38e93f50a4)
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
        '''The Amazon Resource Name (ARN) of the custom data identifier.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The unique identifier for the custom data identifier.

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
        '''A custom name for the custom data identifier.

        The name can contain 1-128 characters.
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56bafc0e98388f95c36a25cdb08ac16d1b32e9b68fc70fc559070e909e26043f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="regex")
    def regex(self) -> builtins.str:
        '''The regular expression ( *regex* ) that defines the text pattern to match.'''
        return typing.cast(builtins.str, jsii.get(self, "regex"))

    @regex.setter
    def regex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1a88698a8e31c22c8a96936b106ec14252c0df95a0c621ffc59448549cfe4f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regex", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A custom description of the custom data identifier.

        The description can contain 1-512 characters.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f4eac22a0be7a58617fc706b4a6f4df1d7c10d4fd1bcb1bc7c87ecb091280ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreWords")
    def ignore_words(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of character sequences ( *ignore words* ) to exclude from the results.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ignoreWords"))

    @ignore_words.setter
    def ignore_words(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35dff10296c96b79146377714bebc3cb572a5fc32fda7088add5e2e9c20cfb52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreWords", value)

    @builtins.property
    @jsii.member(jsii_name="keywords")
    def keywords(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of character sequences ( *keywords* ), one of which must precede and be in proximity ( ``MaximumMatchDistance`` ) of the regular expression ( ``Regex`` ) to match.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "keywords"))

    @keywords.setter
    def keywords(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1910816738c1d222482ca791d3639f1eb091753a7bef0627a18c8298817c4083)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keywords", value)

    @builtins.property
    @jsii.member(jsii_name="maximumMatchDistance")
    def maximum_match_distance(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of characters that can exist between the end of at least one complete character sequence specified by the ``Keywords`` array and the end of text that matches the regular expression ( ``Regex`` ).'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumMatchDistance"))

    @maximum_match_distance.setter
    def maximum_match_distance(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__baadf50a05df72179523cc44ce07f1d05939df835131681e825e51b9a74778eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumMatchDistance", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_macie.CfnCustomDataIdentifierProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "regex": "regex",
        "description": "description",
        "ignore_words": "ignoreWords",
        "keywords": "keywords",
        "maximum_match_distance": "maximumMatchDistance",
    },
)
class CfnCustomDataIdentifierProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        regex: builtins.str,
        description: typing.Optional[builtins.str] = None,
        ignore_words: typing.Optional[typing.Sequence[builtins.str]] = None,
        keywords: typing.Optional[typing.Sequence[builtins.str]] = None,
        maximum_match_distance: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``CfnCustomDataIdentifier``.

        :param name: A custom name for the custom data identifier. The name can contain 1-128 characters. Avoid including sensitive data in the name of a custom data identifier. Users of the account might be able to see the name, depending on the actions that they're allowed to perform in Amazon Macie .
        :param regex: The regular expression ( *regex* ) that defines the text pattern to match. The expression can contain 1-512 characters.
        :param description: A custom description of the custom data identifier. The description can contain 1-512 characters. Avoid including sensitive data in the description. Users of the account might be able to see the description, depending on the actions that they're allowed to perform in Amazon Macie .
        :param ignore_words: An array of character sequences ( *ignore words* ) to exclude from the results. If text matches the regular expression ( ``Regex`` ) but it contains a string in this array, Amazon Macie ignores the text and doesn't include it in the results. The array can contain 1-10 ignore words. Each ignore word can contain 4-90 UTF-8 characters. Ignore words are case sensitive.
        :param keywords: An array of character sequences ( *keywords* ), one of which must precede and be in proximity ( ``MaximumMatchDistance`` ) of the regular expression ( ``Regex`` ) to match. The array can contain 1-50 keywords. Each keyword can contain 3-90 UTF-8 characters. Keywords aren't case sensitive.
        :param maximum_match_distance: The maximum number of characters that can exist between the end of at least one complete character sequence specified by the ``Keywords`` array and the end of text that matches the regular expression ( ``Regex`` ). If a complete keyword precedes all the text that matches the regular expression and the keyword is within the specified distance, Amazon Macie includes the result. The distance can be 1-300 characters. The default value is 50.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_macie as macie
            
            cfn_custom_data_identifier_props = macie.CfnCustomDataIdentifierProps(
                name="name",
                regex="regex",
            
                # the properties below are optional
                description="description",
                ignore_words=["ignoreWords"],
                keywords=["keywords"],
                maximum_match_distance=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b153bc4a75175074214978bb8d0954e3d477b6896260fae9394ce3a3f3ef2463)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument regex", value=regex, expected_type=type_hints["regex"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument ignore_words", value=ignore_words, expected_type=type_hints["ignore_words"])
            check_type(argname="argument keywords", value=keywords, expected_type=type_hints["keywords"])
            check_type(argname="argument maximum_match_distance", value=maximum_match_distance, expected_type=type_hints["maximum_match_distance"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "regex": regex,
        }
        if description is not None:
            self._values["description"] = description
        if ignore_words is not None:
            self._values["ignore_words"] = ignore_words
        if keywords is not None:
            self._values["keywords"] = keywords
        if maximum_match_distance is not None:
            self._values["maximum_match_distance"] = maximum_match_distance

    @builtins.property
    def name(self) -> builtins.str:
        '''A custom name for the custom data identifier. The name can contain 1-128 characters.

        Avoid including sensitive data in the name of a custom data identifier. Users of the account might be able to see the name, depending on the actions that they're allowed to perform in Amazon Macie .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def regex(self) -> builtins.str:
        '''The regular expression ( *regex* ) that defines the text pattern to match.

        The expression can contain 1-512 characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-regex
        '''
        result = self._values.get("regex")
        assert result is not None, "Required property 'regex' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A custom description of the custom data identifier. The description can contain 1-512 characters.

        Avoid including sensitive data in the description. Users of the account might be able to see the description, depending on the actions that they're allowed to perform in Amazon Macie .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ignore_words(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of character sequences ( *ignore words* ) to exclude from the results.

        If text matches the regular expression ( ``Regex`` ) but it contains a string in this array, Amazon Macie ignores the text and doesn't include it in the results.

        The array can contain 1-10 ignore words. Each ignore word can contain 4-90 UTF-8 characters. Ignore words are case sensitive.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-ignorewords
        '''
        result = self._values.get("ignore_words")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def keywords(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of character sequences ( *keywords* ), one of which must precede and be in proximity ( ``MaximumMatchDistance`` ) of the regular expression ( ``Regex`` ) to match.

        The array can contain 1-50 keywords. Each keyword can contain 3-90 UTF-8 characters. Keywords aren't case sensitive.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-keywords
        '''
        result = self._values.get("keywords")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def maximum_match_distance(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of characters that can exist between the end of at least one complete character sequence specified by the ``Keywords`` array and the end of text that matches the regular expression ( ``Regex`` ).

        If a complete keyword precedes all the text that matches the regular expression and the keyword is within the specified distance, Amazon Macie includes the result.

        The distance can be 1-300 characters. The default value is 50.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-maximummatchdistance
        '''
        result = self._values.get("maximum_match_distance")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCustomDataIdentifierProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnFindingsFilter(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_macie.CfnFindingsFilter",
):
    '''The ``AWS::Macie::FindingsFilter`` resource specifies a findings filter.

    In Amazon Macie , a *findings filter* , also referred to as a *filter rule* , is a set of custom criteria that specifies which findings to include or exclude from the results of a query for findings. The criteria can help you identify and focus on findings that have specific characteristics, such as severity, type, or the name of an affected AWS resource. You can also configure a findings filter to suppress (automatically archive) findings that match the filter's criteria. For more information, see `Filtering findings <https://docs.aws.amazon.com/macie/latest/user/findings-filter-overview.html>`_ in the *Amazon Macie User Guide* .

    An ``AWS::Macie::Session`` resource must exist for an AWS account before you can create an ``AWS::Macie::FindingsFilter`` resource for the account. Use a `DependsOn attribute <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html>`_ to ensure that an ``AWS::Macie::Session`` resource is created before other Macie resources are created for an account. For example, ``"DependsOn": "Session"`` .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_macie as macie
        
        cfn_findings_filter = macie.CfnFindingsFilter(self, "MyCfnFindingsFilter",
            finding_criteria=macie.CfnFindingsFilter.FindingCriteriaProperty(
                criterion={
                    "criterion_key": macie.CfnFindingsFilter.CriterionAdditionalPropertiesProperty(
                        eq=["eq"],
                        gt=123,
                        gte=123,
                        lt=123,
                        lte=123,
                        neq=["neq"]
                    )
                }
            ),
            name="name",
        
            # the properties below are optional
            action="action",
            description="description",
            position=123
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        finding_criteria: typing.Union[_IResolvable_da3f097b, typing.Union["CfnFindingsFilter.FindingCriteriaProperty", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        action: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        position: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param finding_criteria: The criteria to use to filter findings.
        :param name: A custom name for the findings filter. The name can contain 3-64 characters. Avoid including sensitive data in the name. Users of the account might be able to see the name, depending on the actions that they're allowed to perform in Amazon Macie .
        :param action: The action to perform on findings that match the filter criteria ( ``FindingCriteria`` ). Valid values are:. - ``ARCHIVE`` - Suppress (automatically archive) the findings. - ``NOOP`` - Don't perform any action on the findings.
        :param description: A custom description of the findings filter. The description can contain 1-512 characters. Avoid including sensitive data in the description. Users of the account might be able to see the description, depending on the actions that they're allowed to perform in Amazon Macie .
        :param position: The position of the findings filter in the list of saved filters on the Amazon Macie console. This value also determines the order in which the filter is applied to findings, relative to other filters that are also applied to findings.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11b08ade332eec06142e65a0667c3f977a9418dbb1685fc4d53acba74840039e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFindingsFilterProps(
            finding_criteria=finding_criteria,
            name=name,
            action=action,
            description=description,
            position=position,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a93c27322ef7d4277d7a472e492eca4e1a6e853c53d3268dc2ece902bef2ea0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__70f86624cef1fb49b3b96cefbc1b1ef17881bea27e106666e69078116a2c0ce5)
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
        '''The Amazon Resource Name (ARN) of the findings filter.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrFindingsFilterListItems")
    def attr_findings_filter_list_items(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: FindingsFilterListItems
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrFindingsFilterListItems"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The unique identifier for the findings filter.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="findingCriteria")
    def finding_criteria(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnFindingsFilter.FindingCriteriaProperty"]:
        '''The criteria to use to filter findings.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnFindingsFilter.FindingCriteriaProperty"], jsii.get(self, "findingCriteria"))

    @finding_criteria.setter
    def finding_criteria(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnFindingsFilter.FindingCriteriaProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dca4bea48d84a530685d7cefc7aab036a382728b48d306044f2a518d375e31af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "findingCriteria", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A custom name for the findings filter.

        The name can contain 3-64 characters.
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d67d6558f4b26d340cf216d4866559bbaf532c9defe9a11eb199af1a7d2433c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> typing.Optional[builtins.str]:
        '''The action to perform on findings that match the filter criteria ( ``FindingCriteria`` ).

        Valid values are:.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "action"))

    @action.setter
    def action(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41dfbe847eece32f936f8bf3bb5d835d163ba85d1ce1a626fe00a0cb995afaa0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A custom description of the findings filter.

        The description can contain 1-512 characters.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03fc2464c8c604a167f22170fbed859036b5124a2e5d8b3f089b061f6bf605cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="position")
    def position(self) -> typing.Optional[jsii.Number]:
        '''The position of the findings filter in the list of saved filters on the Amazon Macie console.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "position"))

    @position.setter
    def position(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c60836229071347a8b3064cb2b271455290f497cd552169c6180768b3a67ea2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "position", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_macie.CfnFindingsFilter.CriterionAdditionalPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "eq": "eq",
            "gt": "gt",
            "gte": "gte",
            "lt": "lt",
            "lte": "lte",
            "neq": "neq",
        },
    )
    class CriterionAdditionalPropertiesProperty:
        def __init__(
            self,
            *,
            eq: typing.Optional[typing.Sequence[builtins.str]] = None,
            gt: typing.Optional[jsii.Number] = None,
            gte: typing.Optional[jsii.Number] = None,
            lt: typing.Optional[jsii.Number] = None,
            lte: typing.Optional[jsii.Number] = None,
            neq: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Specifies a condition that defines the property, operator, and one or more values to use in a findings filter.

            A *findings filter* , also referred to as a *filter rule* , is a set of custom criteria that specifies which findings to include or exclude from the results of a query for findings. You can also configure a findings filter to suppress (automatically archive) findings that match the filter's criteria. For more information, see `Filtering findings <https://docs.aws.amazon.com/macie/latest/user/findings-filter-overview.html>`_ in the *Amazon Macie User Guide* .

            :param eq: The value for the specified property matches (equals) the specified value. If you specify multiple values, Amazon Macie uses OR logic to join the values.
            :param gt: The value for the specified property is greater than the specified value.
            :param gte: The value for the specified property is greater than or equal to the specified value.
            :param lt: The value for the specified property is less than the specified value.
            :param lte: The value for the specified property is less than or equal to the specified value.
            :param neq: The value for the specified property doesn't match (doesn't equal) the specified value. If you specify multiple values, Amazon Macie uses OR logic to join the values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-criterionadditionalproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_macie as macie
                
                criterion_additional_properties_property = macie.CfnFindingsFilter.CriterionAdditionalPropertiesProperty(
                    eq=["eq"],
                    gt=123,
                    gte=123,
                    lt=123,
                    lte=123,
                    neq=["neq"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3cc0e94f951064d75bcef2cb73a1a20831df93d286eb235e35e3f7f153419f00)
                check_type(argname="argument eq", value=eq, expected_type=type_hints["eq"])
                check_type(argname="argument gt", value=gt, expected_type=type_hints["gt"])
                check_type(argname="argument gte", value=gte, expected_type=type_hints["gte"])
                check_type(argname="argument lt", value=lt, expected_type=type_hints["lt"])
                check_type(argname="argument lte", value=lte, expected_type=type_hints["lte"])
                check_type(argname="argument neq", value=neq, expected_type=type_hints["neq"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if eq is not None:
                self._values["eq"] = eq
            if gt is not None:
                self._values["gt"] = gt
            if gte is not None:
                self._values["gte"] = gte
            if lt is not None:
                self._values["lt"] = lt
            if lte is not None:
                self._values["lte"] = lte
            if neq is not None:
                self._values["neq"] = neq

        @builtins.property
        def eq(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The value for the specified property matches (equals) the specified value.

            If you specify multiple values, Amazon Macie uses OR logic to join the values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-criterionadditionalproperties.html#cfn-macie-findingsfilter-criterionadditionalproperties-eq
            '''
            result = self._values.get("eq")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def gt(self) -> typing.Optional[jsii.Number]:
            '''The value for the specified property is greater than the specified value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-criterionadditionalproperties.html#cfn-macie-findingsfilter-criterionadditionalproperties-gt
            '''
            result = self._values.get("gt")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def gte(self) -> typing.Optional[jsii.Number]:
            '''The value for the specified property is greater than or equal to the specified value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-criterionadditionalproperties.html#cfn-macie-findingsfilter-criterionadditionalproperties-gte
            '''
            result = self._values.get("gte")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def lt(self) -> typing.Optional[jsii.Number]:
            '''The value for the specified property is less than the specified value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-criterionadditionalproperties.html#cfn-macie-findingsfilter-criterionadditionalproperties-lt
            '''
            result = self._values.get("lt")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def lte(self) -> typing.Optional[jsii.Number]:
            '''The value for the specified property is less than or equal to the specified value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-criterionadditionalproperties.html#cfn-macie-findingsfilter-criterionadditionalproperties-lte
            '''
            result = self._values.get("lte")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def neq(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The value for the specified property doesn't match (doesn't equal) the specified value.

            If you specify multiple values, Amazon Macie uses OR logic to join the values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-criterionadditionalproperties.html#cfn-macie-findingsfilter-criterionadditionalproperties-neq
            '''
            result = self._values.get("neq")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CriterionAdditionalPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_macie.CfnFindingsFilter.FindingCriteriaProperty",
        jsii_struct_bases=[],
        name_mapping={"criterion": "criterion"},
    )
    class FindingCriteriaProperty:
        def __init__(
            self,
            *,
            criterion: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union["CfnFindingsFilter.CriterionAdditionalPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Specifies, as a map, one or more property-based conditions for a findings filter.

            A *findings filter* , also referred to as a *filter rule* , is a set of custom criteria that specifies which findings to include or exclude from the results of a query for findings. You can also configure a findings filter to suppress (automatically archive) findings that match the filter's criteria. For more information, see `Filtering findings <https://docs.aws.amazon.com/macie/latest/user/findings-filter-overview.html>`_ in the *Amazon Macie User Guide* .

            :param criterion: Specifies a condition that defines the property, operator, and one or more values to use to filter the results.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-findingcriteria.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_macie as macie
                
                finding_criteria_property = macie.CfnFindingsFilter.FindingCriteriaProperty(
                    criterion={
                        "criterion_key": macie.CfnFindingsFilter.CriterionAdditionalPropertiesProperty(
                            eq=["eq"],
                            gt=123,
                            gte=123,
                            lt=123,
                            lte=123,
                            neq=["neq"]
                        )
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bfa11a0d6136e31dcc0f57ce160cc975d2fd8978372183978096da64d7bb37e8)
                check_type(argname="argument criterion", value=criterion, expected_type=type_hints["criterion"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if criterion is not None:
                self._values["criterion"] = criterion

        @builtins.property
        def criterion(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnFindingsFilter.CriterionAdditionalPropertiesProperty"]]]]:
            '''Specifies a condition that defines the property, operator, and one or more values to use to filter the results.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-findingcriteria.html#cfn-macie-findingsfilter-findingcriteria-criterion
            '''
            result = self._values.get("criterion")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnFindingsFilter.CriterionAdditionalPropertiesProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FindingCriteriaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_macie.CfnFindingsFilter.FindingsFilterListItemProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id", "name": "name"},
    )
    class FindingsFilterListItemProperty:
        def __init__(
            self,
            *,
            id: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param id: 
            :param name: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-findingsfilterlistitem.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_macie as macie
                
                findings_filter_list_item_property = macie.CfnFindingsFilter.FindingsFilterListItemProperty(
                    id="id",
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b7156e20d45f08aa3f36cbd419e31b5c99ba4fc02173fd094581cde0ddf8a628)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if id is not None:
                self._values["id"] = id
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def id(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-findingsfilterlistitem.html#cfn-macie-findingsfilter-findingsfilterlistitem-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-findingsfilterlistitem.html#cfn-macie-findingsfilter-findingsfilterlistitem-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FindingsFilterListItemProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_macie.CfnFindingsFilterProps",
    jsii_struct_bases=[],
    name_mapping={
        "finding_criteria": "findingCriteria",
        "name": "name",
        "action": "action",
        "description": "description",
        "position": "position",
    },
)
class CfnFindingsFilterProps:
    def __init__(
        self,
        *,
        finding_criteria: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFindingsFilter.FindingCriteriaProperty, typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        action: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        position: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``CfnFindingsFilter``.

        :param finding_criteria: The criteria to use to filter findings.
        :param name: A custom name for the findings filter. The name can contain 3-64 characters. Avoid including sensitive data in the name. Users of the account might be able to see the name, depending on the actions that they're allowed to perform in Amazon Macie .
        :param action: The action to perform on findings that match the filter criteria ( ``FindingCriteria`` ). Valid values are:. - ``ARCHIVE`` - Suppress (automatically archive) the findings. - ``NOOP`` - Don't perform any action on the findings.
        :param description: A custom description of the findings filter. The description can contain 1-512 characters. Avoid including sensitive data in the description. Users of the account might be able to see the description, depending on the actions that they're allowed to perform in Amazon Macie .
        :param position: The position of the findings filter in the list of saved filters on the Amazon Macie console. This value also determines the order in which the filter is applied to findings, relative to other filters that are also applied to findings.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_macie as macie
            
            cfn_findings_filter_props = macie.CfnFindingsFilterProps(
                finding_criteria=macie.CfnFindingsFilter.FindingCriteriaProperty(
                    criterion={
                        "criterion_key": macie.CfnFindingsFilter.CriterionAdditionalPropertiesProperty(
                            eq=["eq"],
                            gt=123,
                            gte=123,
                            lt=123,
                            lte=123,
                            neq=["neq"]
                        )
                    }
                ),
                name="name",
            
                # the properties below are optional
                action="action",
                description="description",
                position=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4769b70b8b409b7293b4cfb98a775272d6996bc39a6b96c3ad8c76c7aae51f1)
            check_type(argname="argument finding_criteria", value=finding_criteria, expected_type=type_hints["finding_criteria"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument position", value=position, expected_type=type_hints["position"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "finding_criteria": finding_criteria,
            "name": name,
        }
        if action is not None:
            self._values["action"] = action
        if description is not None:
            self._values["description"] = description
        if position is not None:
            self._values["position"] = position

    @builtins.property
    def finding_criteria(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnFindingsFilter.FindingCriteriaProperty]:
        '''The criteria to use to filter findings.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-findingcriteria
        '''
        result = self._values.get("finding_criteria")
        assert result is not None, "Required property 'finding_criteria' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnFindingsFilter.FindingCriteriaProperty], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A custom name for the findings filter. The name can contain 3-64 characters.

        Avoid including sensitive data in the name. Users of the account might be able to see the name, depending on the actions that they're allowed to perform in Amazon Macie .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def action(self) -> typing.Optional[builtins.str]:
        '''The action to perform on findings that match the filter criteria ( ``FindingCriteria`` ). Valid values are:.

        - ``ARCHIVE`` - Suppress (automatically archive) the findings.
        - ``NOOP`` - Don't perform any action on the findings.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-action
        '''
        result = self._values.get("action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A custom description of the findings filter. The description can contain 1-512 characters.

        Avoid including sensitive data in the description. Users of the account might be able to see the description, depending on the actions that they're allowed to perform in Amazon Macie .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def position(self) -> typing.Optional[jsii.Number]:
        '''The position of the findings filter in the list of saved filters on the Amazon Macie console.

        This value also determines the order in which the filter is applied to findings, relative to other filters that are also applied to findings.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-position
        '''
        result = self._values.get("position")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFindingsFilterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSession(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_macie.CfnSession",
):
    '''The ``AWS::Macie::Session`` resource represents the Amazon Macie service and certain configuration settings for an Amazon Macie account in a specific AWS Region .

    It enables Macie to become operational for a specific account in a specific Region. An account can have only one session in each Region.

    You must create an ``AWS::Macie::Session`` resource for an account before you can create other types of resources for the account. Use a `DependsOn attribute <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html>`_ to ensure that an ``AWS::Macie::Session`` resource is created before other Macie resources are created for an account. For example, ``"DependsOn": "Session"`` .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_macie as macie
        
        cfn_session = macie.CfnSession(self, "MyCfnSession",
            finding_publishing_frequency="findingPublishingFrequency",
            status="status"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        finding_publishing_frequency: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param finding_publishing_frequency: Specifies how often Amazon Macie publishes updates to policy findings for the account. This includes publishing updates to AWS Security Hub and Amazon EventBridge (formerly Amazon CloudWatch Events ). Valid values are: - FIFTEEN_MINUTES - ONE_HOUR - SIX_HOURS Default: - "SIX_HOURS"
        :param status: The status of Amazon Macie for the account. Valid values are: ``ENABLED`` , start or resume all Macie activities for the account; and, ``PAUSED`` , suspend all Macie activities for the account. Default: - "ENABLED"
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__459832705822182508c6f2e0693fc53e3b0d82a4e148ecfdd93f163e3afc3417)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSessionProps(
            finding_publishing_frequency=finding_publishing_frequency, status=status
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56a78d5968f4acb7046cb1b0be5462b857c06e6bc787c27f94c2f393e3f681e9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3e43074ce924e3f898d598fd4b912046beaaf89bc693c659909791046eca7b32)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAwsAccountId")
    def attr_aws_account_id(self) -> builtins.str:
        '''The account ID for the AWS account in which the Amazon Macie session is created.

        :cloudformationAttribute: AwsAccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAwsAccountId"))

    @builtins.property
    @jsii.member(jsii_name="attrServiceRole")
    def attr_service_role(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the service-linked role that allows Amazon Macie to monitor and analyze data in AWS resources for the account.

        :cloudformationAttribute: ServiceRole
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceRole"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="findingPublishingFrequency")
    def finding_publishing_frequency(self) -> typing.Optional[builtins.str]:
        '''Specifies how often Amazon Macie publishes updates to policy findings for the account.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "findingPublishingFrequency"))

    @finding_publishing_frequency.setter
    def finding_publishing_frequency(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbab990e35f30e653778479d30de4521365d972399b5f819c47f60195a95dab3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "findingPublishingFrequency", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of Amazon Macie for the account.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e25551195a36935d5b88ee54046aee0f17d2de93fdfb0eaa1a2571fd568ef3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_macie.CfnSessionProps",
    jsii_struct_bases=[],
    name_mapping={
        "finding_publishing_frequency": "findingPublishingFrequency",
        "status": "status",
    },
)
class CfnSessionProps:
    def __init__(
        self,
        *,
        finding_publishing_frequency: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnSession``.

        :param finding_publishing_frequency: Specifies how often Amazon Macie publishes updates to policy findings for the account. This includes publishing updates to AWS Security Hub and Amazon EventBridge (formerly Amazon CloudWatch Events ). Valid values are: - FIFTEEN_MINUTES - ONE_HOUR - SIX_HOURS Default: - "SIX_HOURS"
        :param status: The status of Amazon Macie for the account. Valid values are: ``ENABLED`` , start or resume all Macie activities for the account; and, ``PAUSED`` , suspend all Macie activities for the account. Default: - "ENABLED"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_macie as macie
            
            cfn_session_props = macie.CfnSessionProps(
                finding_publishing_frequency="findingPublishingFrequency",
                status="status"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b2377975304db82e025e7e966713f33964f9e33889db82b2e26a095d3fb3f14)
            check_type(argname="argument finding_publishing_frequency", value=finding_publishing_frequency, expected_type=type_hints["finding_publishing_frequency"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if finding_publishing_frequency is not None:
            self._values["finding_publishing_frequency"] = finding_publishing_frequency
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def finding_publishing_frequency(self) -> typing.Optional[builtins.str]:
        '''Specifies how often Amazon Macie publishes updates to policy findings for the account.

        This includes publishing updates to AWS Security Hub and Amazon EventBridge (formerly Amazon CloudWatch Events ). Valid values are:

        - FIFTEEN_MINUTES
        - ONE_HOUR
        - SIX_HOURS

        :default: - "SIX_HOURS"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html#cfn-macie-session-findingpublishingfrequency
        '''
        result = self._values.get("finding_publishing_frequency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of Amazon Macie for the account.

        Valid values are: ``ENABLED`` , start or resume all Macie activities for the account; and, ``PAUSED`` , suspend all Macie activities for the account.

        :default: - "ENABLED"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html#cfn-macie-session-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSessionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAllowList",
    "CfnAllowListProps",
    "CfnCustomDataIdentifier",
    "CfnCustomDataIdentifierProps",
    "CfnFindingsFilter",
    "CfnFindingsFilterProps",
    "CfnSession",
    "CfnSessionProps",
]

publication.publish()

def _typecheckingstub__ef55cb8aaca32dcf264ac0e8768dc1c5a0b1471c41c8de3c9575f20000ca4bd9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    criteria: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAllowList.CriteriaProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de89a42feae1bdccf1b7fb468bda2c5700b1aa71c5c523cb2c69a8c666ae8e2a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7369f7a4bca5c49d764dbf34faf902a40c52828d8fba955e4eca05e9adcaff7a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e4ae58b4636b7db31b0fa3adc3410ae3d14049fa02c2bd307123f1749460647(
    value: typing.Union[_IResolvable_da3f097b, CfnAllowList.CriteriaProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d690571d1b7ea81f4eaac91920c04dab927cd0ddc18b3539a84afdcb50cfdc4c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eff0733233420991a19ec573286f220cf810fc8bd281a542a9fa2c82daf4c241(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__142a3b637b387ca2f41ecc60f7492ab453fed61355af5abfd8c68c74fc8f0c16(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__916c849be567db5e8b2d28b4262b1b5e6cc4efa0cc6749b882394480f94b0f1a(
    *,
    regex: typing.Optional[builtins.str] = None,
    s3_words_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAllowList.S3WordsListProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6728338d9836f378990a221bfcb5d4ebc176286721060379316cb044250d5933(
    *,
    bucket_name: builtins.str,
    object_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cde4980d3f47e6973fbc0136f9a40cf0f5706f781fb45f3cc0aad4b99e96d39(
    *,
    criteria: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAllowList.CriteriaProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8462f70ed2396867e691499b8338ee06166375569e4774b35cad18418587284c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    regex: builtins.str,
    description: typing.Optional[builtins.str] = None,
    ignore_words: typing.Optional[typing.Sequence[builtins.str]] = None,
    keywords: typing.Optional[typing.Sequence[builtins.str]] = None,
    maximum_match_distance: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75e9300d86a3080fc43c5b9e06f708ec6e0be23ca1a8b8c548c28f04d4a38b47(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c2273c82378b08a1921a6584b6eafca3f9442f8236c8797614cdc38e93f50a4(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56bafc0e98388f95c36a25cdb08ac16d1b32e9b68fc70fc559070e909e26043f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1a88698a8e31c22c8a96936b106ec14252c0df95a0c621ffc59448549cfe4f4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f4eac22a0be7a58617fc706b4a6f4df1d7c10d4fd1bcb1bc7c87ecb091280ab(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35dff10296c96b79146377714bebc3cb572a5fc32fda7088add5e2e9c20cfb52(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1910816738c1d222482ca791d3639f1eb091753a7bef0627a18c8298817c4083(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baadf50a05df72179523cc44ce07f1d05939df835131681e825e51b9a74778eb(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b153bc4a75175074214978bb8d0954e3d477b6896260fae9394ce3a3f3ef2463(
    *,
    name: builtins.str,
    regex: builtins.str,
    description: typing.Optional[builtins.str] = None,
    ignore_words: typing.Optional[typing.Sequence[builtins.str]] = None,
    keywords: typing.Optional[typing.Sequence[builtins.str]] = None,
    maximum_match_distance: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11b08ade332eec06142e65a0667c3f977a9418dbb1685fc4d53acba74840039e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    finding_criteria: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFindingsFilter.FindingCriteriaProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    action: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    position: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a93c27322ef7d4277d7a472e492eca4e1a6e853c53d3268dc2ece902bef2ea0(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70f86624cef1fb49b3b96cefbc1b1ef17881bea27e106666e69078116a2c0ce5(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dca4bea48d84a530685d7cefc7aab036a382728b48d306044f2a518d375e31af(
    value: typing.Union[_IResolvable_da3f097b, CfnFindingsFilter.FindingCriteriaProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d67d6558f4b26d340cf216d4866559bbaf532c9defe9a11eb199af1a7d2433c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41dfbe847eece32f936f8bf3bb5d835d163ba85d1ce1a626fe00a0cb995afaa0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03fc2464c8c604a167f22170fbed859036b5124a2e5d8b3f089b061f6bf605cb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c60836229071347a8b3064cb2b271455290f497cd552169c6180768b3a67ea2e(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cc0e94f951064d75bcef2cb73a1a20831df93d286eb235e35e3f7f153419f00(
    *,
    eq: typing.Optional[typing.Sequence[builtins.str]] = None,
    gt: typing.Optional[jsii.Number] = None,
    gte: typing.Optional[jsii.Number] = None,
    lt: typing.Optional[jsii.Number] = None,
    lte: typing.Optional[jsii.Number] = None,
    neq: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfa11a0d6136e31dcc0f57ce160cc975d2fd8978372183978096da64d7bb37e8(
    *,
    criterion: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnFindingsFilter.CriterionAdditionalPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7156e20d45f08aa3f36cbd419e31b5c99ba4fc02173fd094581cde0ddf8a628(
    *,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4769b70b8b409b7293b4cfb98a775272d6996bc39a6b96c3ad8c76c7aae51f1(
    *,
    finding_criteria: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFindingsFilter.FindingCriteriaProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    action: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    position: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__459832705822182508c6f2e0693fc53e3b0d82a4e148ecfdd93f163e3afc3417(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    finding_publishing_frequency: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56a78d5968f4acb7046cb1b0be5462b857c06e6bc787c27f94c2f393e3f681e9(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e43074ce924e3f898d598fd4b912046beaaf89bc693c659909791046eca7b32(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbab990e35f30e653778479d30de4521365d972399b5f819c47f60195a95dab3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e25551195a36935d5b88ee54046aee0f17d2de93fdfb0eaa1a2571fd568ef3f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b2377975304db82e025e7e966713f33964f9e33889db82b2e26a095d3fb3f14(
    *,
    finding_publishing_frequency: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
