'''
# AWS::Comprehend Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_comprehend as comprehend
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Comprehend construct libraries](https://constructs.dev/search?q=comprehend)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Comprehend resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Comprehend.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Comprehend](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Comprehend.html).

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
class CfnDocumentClassifier(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_comprehend.CfnDocumentClassifier",
):
    '''This resource creates and trains a document classifier to categorize documents.

    You provide a set of training documents that are labeled with the categories that you want to identify. After the classifier is trained you can use it to categorize a set of labeled documents into the categories. For more information, see `Document Classification <https://docs.aws.amazon.com/comprehend/latest/dg/how-document-classification.html>`_ in the Comprehend Developer Guide.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-documentclassifier.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_comprehend as comprehend
        
        cfn_document_classifier = comprehend.CfnDocumentClassifier(self, "MyCfnDocumentClassifier",
            data_access_role_arn="dataAccessRoleArn",
            document_classifier_name="documentClassifierName",
            input_data_config=comprehend.CfnDocumentClassifier.DocumentClassifierInputDataConfigProperty(
                augmented_manifests=[comprehend.CfnDocumentClassifier.AugmentedManifestsListItemProperty(
                    attribute_names=["attributeNames"],
                    s3_uri="s3Uri",
        
                    # the properties below are optional
                    split="split"
                )],
                data_format="dataFormat",
                document_reader_config=comprehend.CfnDocumentClassifier.DocumentReaderConfigProperty(
                    document_read_action="documentReadAction",
        
                    # the properties below are optional
                    document_read_mode="documentReadMode",
                    feature_types=["featureTypes"]
                ),
                documents=comprehend.CfnDocumentClassifier.DocumentClassifierDocumentsProperty(
                    s3_uri="s3Uri",
        
                    # the properties below are optional
                    test_s3_uri="testS3Uri"
                ),
                document_type="documentType",
                label_delimiter="labelDelimiter",
                s3_uri="s3Uri",
                test_s3_uri="testS3Uri"
            ),
            language_code="languageCode",
        
            # the properties below are optional
            mode="mode",
            model_kms_key_id="modelKmsKeyId",
            model_policy="modelPolicy",
            output_data_config=comprehend.CfnDocumentClassifier.DocumentClassifierOutputDataConfigProperty(
                kms_key_id="kmsKeyId",
                s3_uri="s3Uri"
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            version_name="versionName",
            volume_kms_key_id="volumeKmsKeyId",
            vpc_config=comprehend.CfnDocumentClassifier.VpcConfigProperty(
                security_group_ids=["securityGroupIds"],
                subnets=["subnets"]
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        data_access_role_arn: builtins.str,
        document_classifier_name: builtins.str,
        input_data_config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDocumentClassifier.DocumentClassifierInputDataConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        language_code: builtins.str,
        mode: typing.Optional[builtins.str] = None,
        model_kms_key_id: typing.Optional[builtins.str] = None,
        model_policy: typing.Optional[builtins.str] = None,
        output_data_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDocumentClassifier.DocumentClassifierOutputDataConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        version_name: typing.Optional[builtins.str] = None,
        volume_kms_key_id: typing.Optional[builtins.str] = None,
        vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDocumentClassifier.VpcConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param data_access_role_arn: The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.
        :param document_classifier_name: The name of the document classifier.
        :param input_data_config: Specifies the format and location of the input data for the job.
        :param language_code: The language of the input documents. You can specify any of the languages supported by Amazon Comprehend. All documents must be in the same language.
        :param mode: Indicates the mode in which the classifier will be trained. The classifier can be trained in multi-class mode, which identifies one and only one class for each document, or multi-label mode, which identifies one or more labels for each document. In multi-label mode, multiple labels for an individual document are separated by a delimiter. The default delimiter between labels is a pipe (|).
        :param model_kms_key_id: ID for the AWS KMS key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats: - KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"`` - Amazon Resource Name (ARN) of a KMS Key: ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``
        :param model_policy: The resource-based policy to attach to your custom document classifier model. You can use this policy to allow another AWS account to import your custom model. Provide your policy as a JSON body that you enter as a UTF-8 encoded string without line breaks. To provide valid JSON, enclose the attribute names and values in double quotes. If the JSON body is also enclosed in double quotes, then you must escape the double quotes that are inside the policy: ``"{\\"attribute\\": \\"value\\", \\"attribute\\": [\\"value\\"]}"`` To avoid escaping quotes, you can use single quotes to enclose the policy and double quotes to enclose the JSON names and values: ``'{"attribute": "value", "attribute": ["value"]}'``
        :param output_data_config: Provides output results configuration parameters for custom classifier jobs.
        :param tags: Tags to associate with the document classifier. A tag is a key-value pair that adds as a metadata to a resource used by Amazon Comprehend. For example, a tag with "Sales" as the key might be added to a resource to indicate its use by the sales department.
        :param version_name: The version name given to the newly created classifier. Version names can have a maximum of 256 characters. Alphanumeric characters, hyphens (-) and underscores (_) are allowed. The version name must be unique among all models with the same classifier name in the AWS account / AWS Region .
        :param volume_kms_key_id: ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats: - KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"`` - Amazon Resource Name (ARN) of a KMS Key: ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``
        :param vpc_config: Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources you are using for your custom classifier. For more information, see `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0da43afef06b62227e1171021a9a7ce43e2e481fa3c1ff8263e87fc9d8a04a11)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDocumentClassifierProps(
            data_access_role_arn=data_access_role_arn,
            document_classifier_name=document_classifier_name,
            input_data_config=input_data_config,
            language_code=language_code,
            mode=mode,
            model_kms_key_id=model_kms_key_id,
            model_policy=model_policy,
            output_data_config=output_data_config,
            tags=tags,
            version_name=version_name,
            volume_kms_key_id=volume_kms_key_id,
            vpc_config=vpc_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92e2c4b33fb017d2bc9b1ee4c697a9167f78647f346ac5244d2bc0fd757caafc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__287be59af197ae51a952af63959a3e03141cb3cc954016e70bb810f820be527d)
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
        '''The Amazon Resource Name (ARN) of the document classifier.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="dataAccessRoleArn")
    def data_access_role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.'''
        return typing.cast(builtins.str, jsii.get(self, "dataAccessRoleArn"))

    @data_access_role_arn.setter
    def data_access_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b37e87366af30e1867ccce78466a7f4c6d746af1145b7d79190f47f81c93150)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataAccessRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="documentClassifierName")
    def document_classifier_name(self) -> builtins.str:
        '''The name of the document classifier.'''
        return typing.cast(builtins.str, jsii.get(self, "documentClassifierName"))

    @document_classifier_name.setter
    def document_classifier_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__638faf1cde59d08f5f01020564bc1e88a6cea30b7dabcd32bafb9e2a19679e22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "documentClassifierName", value)

    @builtins.property
    @jsii.member(jsii_name="inputDataConfig")
    def input_data_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnDocumentClassifier.DocumentClassifierInputDataConfigProperty"]:
        '''Specifies the format and location of the input data for the job.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDocumentClassifier.DocumentClassifierInputDataConfigProperty"], jsii.get(self, "inputDataConfig"))

    @input_data_config.setter
    def input_data_config(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnDocumentClassifier.DocumentClassifierInputDataConfigProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72e4443e99a7ca079c78d2d3e95ad08de986276725c191c60fe4bb9c079cb943)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputDataConfig", value)

    @builtins.property
    @jsii.member(jsii_name="languageCode")
    def language_code(self) -> builtins.str:
        '''The language of the input documents.'''
        return typing.cast(builtins.str, jsii.get(self, "languageCode"))

    @language_code.setter
    def language_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e3dc92e7423146f7bc3fa270f51b1ccf6814b377e155ee2ed7fa29304a9af1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "languageCode", value)

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> typing.Optional[builtins.str]:
        '''Indicates the mode in which the classifier will be trained.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a57a1c717c1a0c5a74255154c12499f2db8a5c7a4fa572ddbcd498ad15f6521)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="modelKmsKeyId")
    def model_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''ID for the AWS KMS key that Amazon Comprehend uses to encrypt trained custom models.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modelKmsKeyId"))

    @model_kms_key_id.setter
    def model_kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef8b3a8450ff07c6f8a82db094f1c024cdae25ff4129f6dfa51b3a56a75ba47f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modelKmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="modelPolicy")
    def model_policy(self) -> typing.Optional[builtins.str]:
        '''The resource-based policy to attach to your custom document classifier model.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modelPolicy"))

    @model_policy.setter
    def model_policy(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04fae6cd4c58f60cada64d8d21b84531af3aa7e5eaf941164906bbef62922cdb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modelPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="outputDataConfig")
    def output_data_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDocumentClassifier.DocumentClassifierOutputDataConfigProperty"]]:
        '''Provides output results configuration parameters for custom classifier jobs.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDocumentClassifier.DocumentClassifierOutputDataConfigProperty"]], jsii.get(self, "outputDataConfig"))

    @output_data_config.setter
    def output_data_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDocumentClassifier.DocumentClassifierOutputDataConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77e41c78333ebb35c2df89407137e02c535908d5a9507232b4191645cf0b545b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputDataConfig", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags to associate with the document classifier.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c98bb6f280f6bbf3f16d43daf50dcb88973e23a7318af37a5a3b1abcea57d5c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="versionName")
    def version_name(self) -> typing.Optional[builtins.str]:
        '''The version name given to the newly created classifier.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionName"))

    @version_name.setter
    def version_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cfd73724bd487f3406d963cae58c0001de744cd65d9ffc08a8c4cbd317494ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versionName", value)

    @builtins.property
    @jsii.member(jsii_name="volumeKmsKeyId")
    def volume_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeKmsKeyId"))

    @volume_kms_key_id.setter
    def volume_kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__344f34dca22ae27ea74f0d21ce8353bfd4b47f3b3f4d5bbb468ee6c3d66a5bae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeKmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="vpcConfig")
    def vpc_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDocumentClassifier.VpcConfigProperty"]]:
        '''Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources you are using for your custom classifier.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDocumentClassifier.VpcConfigProperty"]], jsii.get(self, "vpcConfig"))

    @vpc_config.setter
    def vpc_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDocumentClassifier.VpcConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abdfe2fb65b1015aa13bcd7af0d9989b0bf86879cf9af256182e344894204fd3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcConfig", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_comprehend.CfnDocumentClassifier.AugmentedManifestsListItemProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attribute_names": "attributeNames",
            "s3_uri": "s3Uri",
            "split": "split",
        },
    )
    class AugmentedManifestsListItemProperty:
        def __init__(
            self,
            *,
            attribute_names: typing.Sequence[builtins.str],
            s3_uri: builtins.str,
            split: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An augmented manifest file that provides training data for your custom model.

            An augmented manifest file is a labeled dataset that is produced by Amazon SageMaker Ground Truth.

            :param attribute_names: The JSON attribute that contains the annotations for your training documents. The number of attribute names that you specify depends on whether your augmented manifest file is the output of a single labeling job or a chained labeling job. If your file is the output of a single labeling job, specify the LabelAttributeName key that was used when the job was created in Ground Truth. If your file is the output of a chained labeling job, specify the LabelAttributeName key for one or more jobs in the chain. Each LabelAttributeName key provides the annotations from an individual job.
            :param s3_uri: The Amazon S3 location of the augmented manifest file.
            :param split: The purpose of the data you've provided in the augmented manifest. You can either train or test this data. If you don't specify, the default is train. TRAIN - all of the documents in the manifest will be used for training. If no test documents are provided, Amazon Comprehend will automatically reserve a portion of the training documents for testing. TEST - all of the documents in the manifest will be used for testing.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-augmentedmanifestslistitem.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_comprehend as comprehend
                
                augmented_manifests_list_item_property = comprehend.CfnDocumentClassifier.AugmentedManifestsListItemProperty(
                    attribute_names=["attributeNames"],
                    s3_uri="s3Uri",
                
                    # the properties below are optional
                    split="split"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0e7be165e53934b67c373db8aca52b6ed7c0c1d73712fc19358c759cd06f6d7d)
                check_type(argname="argument attribute_names", value=attribute_names, expected_type=type_hints["attribute_names"])
                check_type(argname="argument s3_uri", value=s3_uri, expected_type=type_hints["s3_uri"])
                check_type(argname="argument split", value=split, expected_type=type_hints["split"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "attribute_names": attribute_names,
                "s3_uri": s3_uri,
            }
            if split is not None:
                self._values["split"] = split

        @builtins.property
        def attribute_names(self) -> typing.List[builtins.str]:
            '''The JSON attribute that contains the annotations for your training documents.

            The number of attribute names that you specify depends on whether your augmented manifest file is the output of a single labeling job or a chained labeling job.

            If your file is the output of a single labeling job, specify the LabelAttributeName key that was used when the job was created in Ground Truth.

            If your file is the output of a chained labeling job, specify the LabelAttributeName key for one or more jobs in the chain. Each LabelAttributeName key provides the annotations from an individual job.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-augmentedmanifestslistitem.html#cfn-comprehend-documentclassifier-augmentedmanifestslistitem-attributenames
            '''
            result = self._values.get("attribute_names")
            assert result is not None, "Required property 'attribute_names' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def s3_uri(self) -> builtins.str:
            '''The Amazon S3 location of the augmented manifest file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-augmentedmanifestslistitem.html#cfn-comprehend-documentclassifier-augmentedmanifestslistitem-s3uri
            '''
            result = self._values.get("s3_uri")
            assert result is not None, "Required property 's3_uri' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def split(self) -> typing.Optional[builtins.str]:
            '''The purpose of the data you've provided in the augmented manifest.

            You can either train or test this data. If you don't specify, the default is train.

            TRAIN - all of the documents in the manifest will be used for training. If no test documents are provided, Amazon Comprehend will automatically reserve a portion of the training documents for testing.

            TEST - all of the documents in the manifest will be used for testing.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-augmentedmanifestslistitem.html#cfn-comprehend-documentclassifier-augmentedmanifestslistitem-split
            '''
            result = self._values.get("split")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AugmentedManifestsListItemProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_comprehend.CfnDocumentClassifier.DocumentClassifierDocumentsProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_uri": "s3Uri", "test_s3_uri": "testS3Uri"},
    )
    class DocumentClassifierDocumentsProperty:
        def __init__(
            self,
            *,
            s3_uri: builtins.str,
            test_s3_uri: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The location of the training documents.

            This parameter is required in a request to create a semi-structured document classification model.

            :param s3_uri: The S3 URI location of the training documents specified in the S3Uri CSV file.
            :param test_s3_uri: The S3 URI location of the test documents included in the TestS3Uri CSV file. This field is not required if you do not specify a test CSV file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentclassifierdocuments.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_comprehend as comprehend
                
                document_classifier_documents_property = comprehend.CfnDocumentClassifier.DocumentClassifierDocumentsProperty(
                    s3_uri="s3Uri",
                
                    # the properties below are optional
                    test_s3_uri="testS3Uri"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9b9a924b5e8313e96401e175a3cc69b5e202e2094cfee26902965392b9115295)
                check_type(argname="argument s3_uri", value=s3_uri, expected_type=type_hints["s3_uri"])
                check_type(argname="argument test_s3_uri", value=test_s3_uri, expected_type=type_hints["test_s3_uri"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "s3_uri": s3_uri,
            }
            if test_s3_uri is not None:
                self._values["test_s3_uri"] = test_s3_uri

        @builtins.property
        def s3_uri(self) -> builtins.str:
            '''The S3 URI location of the training documents specified in the S3Uri CSV file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentclassifierdocuments.html#cfn-comprehend-documentclassifier-documentclassifierdocuments-s3uri
            '''
            result = self._values.get("s3_uri")
            assert result is not None, "Required property 's3_uri' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def test_s3_uri(self) -> typing.Optional[builtins.str]:
            '''The S3 URI location of the test documents included in the TestS3Uri CSV file.

            This field is not required if you do not specify a test CSV file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentclassifierdocuments.html#cfn-comprehend-documentclassifier-documentclassifierdocuments-tests3uri
            '''
            result = self._values.get("test_s3_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DocumentClassifierDocumentsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_comprehend.CfnDocumentClassifier.DocumentClassifierInputDataConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "augmented_manifests": "augmentedManifests",
            "data_format": "dataFormat",
            "document_reader_config": "documentReaderConfig",
            "documents": "documents",
            "document_type": "documentType",
            "label_delimiter": "labelDelimiter",
            "s3_uri": "s3Uri",
            "test_s3_uri": "testS3Uri",
        },
    )
    class DocumentClassifierInputDataConfigProperty:
        def __init__(
            self,
            *,
            augmented_manifests: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDocumentClassifier.AugmentedManifestsListItemProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            data_format: typing.Optional[builtins.str] = None,
            document_reader_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDocumentClassifier.DocumentReaderConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            documents: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDocumentClassifier.DocumentClassifierDocumentsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            document_type: typing.Optional[builtins.str] = None,
            label_delimiter: typing.Optional[builtins.str] = None,
            s3_uri: typing.Optional[builtins.str] = None,
            test_s3_uri: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The input properties for training a document classifier.

            For more information on how the input file is formatted, see `Preparing training data <https://docs.aws.amazon.com/comprehend/latest/dg/prep-classifier-data.html>`_ in the Comprehend Developer Guide.

            :param augmented_manifests: A list of augmented manifest files that provide training data for your custom model. An augmented manifest file is a labeled dataset that is produced by Amazon SageMaker Ground Truth. This parameter is required if you set ``DataFormat`` to ``AUGMENTED_MANIFEST`` .
            :param data_format: The format of your training data:. - ``COMPREHEND_CSV`` : A two-column CSV file, where labels are provided in the first column, and documents are provided in the second. If you use this value, you must provide the ``S3Uri`` parameter in your request. - ``AUGMENTED_MANIFEST`` : A labeled dataset that is produced by Amazon SageMaker Ground Truth. This file is in JSON lines format. Each line is a complete JSON object that contains a training document and its associated labels. If you use this value, you must provide the ``AugmentedManifests`` parameter in your request. If you don't specify a value, Amazon Comprehend uses ``COMPREHEND_CSV`` as the default.
            :param document_reader_config: 
            :param documents: The S3 location of the training documents. This parameter is required in a request to create a native document model.
            :param document_type: The type of input documents for training the model. Provide plain-text documents to create a plain-text model, and provide semi-structured documents to create a native document model.
            :param label_delimiter: Indicates the delimiter used to separate each label for training a multi-label classifier. The default delimiter between labels is a pipe (|). You can use a different character as a delimiter (if it's an allowed character) by specifying it under Delimiter for labels. If the training documents use a delimiter other than the default or the delimiter you specify, the labels on that line will be combined to make a single unique label, such as LABELLABELLABEL.
            :param s3_uri: The Amazon S3 URI for the input data. The S3 bucket must be in the same Region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of input files. For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input. This parameter is required if you set ``DataFormat`` to ``COMPREHEND_CSV`` .
            :param test_s3_uri: This specifies the Amazon S3 location that contains the test annotations for the document classifier. The URI must be in the same AWS Region as the API endpoint that you are calling.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentclassifierinputdataconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_comprehend as comprehend
                
                document_classifier_input_data_config_property = comprehend.CfnDocumentClassifier.DocumentClassifierInputDataConfigProperty(
                    augmented_manifests=[comprehend.CfnDocumentClassifier.AugmentedManifestsListItemProperty(
                        attribute_names=["attributeNames"],
                        s3_uri="s3Uri",
                
                        # the properties below are optional
                        split="split"
                    )],
                    data_format="dataFormat",
                    document_reader_config=comprehend.CfnDocumentClassifier.DocumentReaderConfigProperty(
                        document_read_action="documentReadAction",
                
                        # the properties below are optional
                        document_read_mode="documentReadMode",
                        feature_types=["featureTypes"]
                    ),
                    documents=comprehend.CfnDocumentClassifier.DocumentClassifierDocumentsProperty(
                        s3_uri="s3Uri",
                
                        # the properties below are optional
                        test_s3_uri="testS3Uri"
                    ),
                    document_type="documentType",
                    label_delimiter="labelDelimiter",
                    s3_uri="s3Uri",
                    test_s3_uri="testS3Uri"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8453f7adcda177853e8778d17871cc98c5d202507a96232815d58242cb75d024)
                check_type(argname="argument augmented_manifests", value=augmented_manifests, expected_type=type_hints["augmented_manifests"])
                check_type(argname="argument data_format", value=data_format, expected_type=type_hints["data_format"])
                check_type(argname="argument document_reader_config", value=document_reader_config, expected_type=type_hints["document_reader_config"])
                check_type(argname="argument documents", value=documents, expected_type=type_hints["documents"])
                check_type(argname="argument document_type", value=document_type, expected_type=type_hints["document_type"])
                check_type(argname="argument label_delimiter", value=label_delimiter, expected_type=type_hints["label_delimiter"])
                check_type(argname="argument s3_uri", value=s3_uri, expected_type=type_hints["s3_uri"])
                check_type(argname="argument test_s3_uri", value=test_s3_uri, expected_type=type_hints["test_s3_uri"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if augmented_manifests is not None:
                self._values["augmented_manifests"] = augmented_manifests
            if data_format is not None:
                self._values["data_format"] = data_format
            if document_reader_config is not None:
                self._values["document_reader_config"] = document_reader_config
            if documents is not None:
                self._values["documents"] = documents
            if document_type is not None:
                self._values["document_type"] = document_type
            if label_delimiter is not None:
                self._values["label_delimiter"] = label_delimiter
            if s3_uri is not None:
                self._values["s3_uri"] = s3_uri
            if test_s3_uri is not None:
                self._values["test_s3_uri"] = test_s3_uri

        @builtins.property
        def augmented_manifests(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDocumentClassifier.AugmentedManifestsListItemProperty"]]]]:
            '''A list of augmented manifest files that provide training data for your custom model.

            An augmented manifest file is a labeled dataset that is produced by Amazon SageMaker Ground Truth.

            This parameter is required if you set ``DataFormat`` to ``AUGMENTED_MANIFEST`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentclassifierinputdataconfig.html#cfn-comprehend-documentclassifier-documentclassifierinputdataconfig-augmentedmanifests
            '''
            result = self._values.get("augmented_manifests")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDocumentClassifier.AugmentedManifestsListItemProperty"]]]], result)

        @builtins.property
        def data_format(self) -> typing.Optional[builtins.str]:
            '''The format of your training data:.

            - ``COMPREHEND_CSV`` : A two-column CSV file, where labels are provided in the first column, and documents are provided in the second. If you use this value, you must provide the ``S3Uri`` parameter in your request.
            - ``AUGMENTED_MANIFEST`` : A labeled dataset that is produced by Amazon SageMaker Ground Truth. This file is in JSON lines format. Each line is a complete JSON object that contains a training document and its associated labels.

            If you use this value, you must provide the ``AugmentedManifests`` parameter in your request.

            If you don't specify a value, Amazon Comprehend uses ``COMPREHEND_CSV`` as the default.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentclassifierinputdataconfig.html#cfn-comprehend-documentclassifier-documentclassifierinputdataconfig-dataformat
            '''
            result = self._values.get("data_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def document_reader_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDocumentClassifier.DocumentReaderConfigProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentclassifierinputdataconfig.html#cfn-comprehend-documentclassifier-documentclassifierinputdataconfig-documentreaderconfig
            '''
            result = self._values.get("document_reader_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDocumentClassifier.DocumentReaderConfigProperty"]], result)

        @builtins.property
        def documents(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDocumentClassifier.DocumentClassifierDocumentsProperty"]]:
            '''The S3 location of the training documents.

            This parameter is required in a request to create a native document model.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentclassifierinputdataconfig.html#cfn-comprehend-documentclassifier-documentclassifierinputdataconfig-documents
            '''
            result = self._values.get("documents")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDocumentClassifier.DocumentClassifierDocumentsProperty"]], result)

        @builtins.property
        def document_type(self) -> typing.Optional[builtins.str]:
            '''The type of input documents for training the model.

            Provide plain-text documents to create a plain-text model, and provide semi-structured documents to create a native document model.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentclassifierinputdataconfig.html#cfn-comprehend-documentclassifier-documentclassifierinputdataconfig-documenttype
            '''
            result = self._values.get("document_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def label_delimiter(self) -> typing.Optional[builtins.str]:
            '''Indicates the delimiter used to separate each label for training a multi-label classifier.

            The default delimiter between labels is a pipe (|). You can use a different character as a delimiter (if it's an allowed character) by specifying it under Delimiter for labels. If the training documents use a delimiter other than the default or the delimiter you specify, the labels on that line will be combined to make a single unique label, such as LABELLABELLABEL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentclassifierinputdataconfig.html#cfn-comprehend-documentclassifier-documentclassifierinputdataconfig-labeldelimiter
            '''
            result = self._values.get("label_delimiter")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_uri(self) -> typing.Optional[builtins.str]:
            '''The Amazon S3 URI for the input data.

            The S3 bucket must be in the same Region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of input files.

            For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.

            This parameter is required if you set ``DataFormat`` to ``COMPREHEND_CSV`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentclassifierinputdataconfig.html#cfn-comprehend-documentclassifier-documentclassifierinputdataconfig-s3uri
            '''
            result = self._values.get("s3_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def test_s3_uri(self) -> typing.Optional[builtins.str]:
            '''This specifies the Amazon S3 location that contains the test annotations for the document classifier.

            The URI must be in the same AWS Region as the API endpoint that you are calling.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentclassifierinputdataconfig.html#cfn-comprehend-documentclassifier-documentclassifierinputdataconfig-tests3uri
            '''
            result = self._values.get("test_s3_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DocumentClassifierInputDataConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_comprehend.CfnDocumentClassifier.DocumentClassifierOutputDataConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"kms_key_id": "kmsKeyId", "s3_uri": "s3Uri"},
    )
    class DocumentClassifierOutputDataConfigProperty:
        def __init__(
            self,
            *,
            kms_key_id: typing.Optional[builtins.str] = None,
            s3_uri: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provide the location for output data from a custom classifier job.

            This field is mandatory if you are training a native document model.

            :param kms_key_id: ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt the output results from an analysis job. The KmsKeyId can be one of the following formats: - KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"`` - Amazon Resource Name (ARN) of a KMS Key: ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`` - KMS Key Alias: ``"alias/ExampleAlias"`` - ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``
            :param s3_uri: When you use the ``OutputDataConfig`` object while creating a custom classifier, you specify the Amazon S3 location where you want to write the confusion matrix and other output files. The URI must be in the same Region as the API endpoint that you are calling. The location is used as the prefix for the actual location of this output file. When the custom classifier job is finished, the service creates the output file in a directory specific to the job. The ``S3Uri`` field contains the location of the output file, called ``output.tar.gz`` . It is a compressed archive that contains the confusion matrix.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentclassifieroutputdataconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_comprehend as comprehend
                
                document_classifier_output_data_config_property = comprehend.CfnDocumentClassifier.DocumentClassifierOutputDataConfigProperty(
                    kms_key_id="kmsKeyId",
                    s3_uri="s3Uri"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8be9905eb78b42938653d2997696c7efead62cdf90ea74df719050f8916d9ebd)
                check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
                check_type(argname="argument s3_uri", value=s3_uri, expected_type=type_hints["s3_uri"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id
            if s3_uri is not None:
                self._values["s3_uri"] = s3_uri

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt the output results from an analysis job.

            The KmsKeyId can be one of the following formats:

            - KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``
            - Amazon Resource Name (ARN) of a KMS Key: ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``
            - KMS Key Alias: ``"alias/ExampleAlias"``
            - ARN of a KMS Key Alias: ``"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentclassifieroutputdataconfig.html#cfn-comprehend-documentclassifier-documentclassifieroutputdataconfig-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_uri(self) -> typing.Optional[builtins.str]:
            '''When you use the ``OutputDataConfig`` object while creating a custom classifier, you specify the Amazon S3 location where you want to write the confusion matrix and other output files.

            The URI must be in the same Region as the API endpoint that you are calling. The location is used as the prefix for the actual location of this output file.

            When the custom classifier job is finished, the service creates the output file in a directory specific to the job. The ``S3Uri`` field contains the location of the output file, called ``output.tar.gz`` . It is a compressed archive that contains the confusion matrix.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentclassifieroutputdataconfig.html#cfn-comprehend-documentclassifier-documentclassifieroutputdataconfig-s3uri
            '''
            result = self._values.get("s3_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DocumentClassifierOutputDataConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_comprehend.CfnDocumentClassifier.DocumentReaderConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "document_read_action": "documentReadAction",
            "document_read_mode": "documentReadMode",
            "feature_types": "featureTypes",
        },
    )
    class DocumentReaderConfigProperty:
        def __init__(
            self,
            *,
            document_read_action: builtins.str,
            document_read_mode: typing.Optional[builtins.str] = None,
            feature_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Provides configuration parameters to override the default actions for extracting text from PDF documents and image files.

            By default, Amazon Comprehend performs the following actions to extract text from files, based on the input file type:

            - *Word files* - Amazon Comprehend parser extracts the text.
            - *Digital PDF files* - Amazon Comprehend parser extracts the text.
            - *Image files and scanned PDF files* - Amazon Comprehend uses the Amazon Textract ``DetectDocumentText`` API to extract the text.

            ``DocumentReaderConfig`` does not apply to plain text files or Word files.

            For image files and PDF documents, you can override these default actions using the fields listed below. For more information, see `Setting text extraction options <https://docs.aws.amazon.com/comprehend/latest/dg/idp-set-textract-options.html>`_ in the Comprehend Developer Guide.

            :param document_read_action: This field defines the Amazon Textract API operation that Amazon Comprehend uses to extract text from PDF files and image files. Enter one of the following values: - ``TEXTRACT_DETECT_DOCUMENT_TEXT`` - The Amazon Comprehend service uses the ``DetectDocumentText`` API operation. - ``TEXTRACT_ANALYZE_DOCUMENT`` - The Amazon Comprehend service uses the ``AnalyzeDocument`` API operation.
            :param document_read_mode: Determines the text extraction actions for PDF files. Enter one of the following values:. - ``SERVICE_DEFAULT`` - use the Amazon Comprehend service defaults for PDF files. - ``FORCE_DOCUMENT_READ_ACTION`` - Amazon Comprehend uses the Textract API specified by DocumentReadAction for all PDF files, including digital PDF files.
            :param feature_types: Specifies the type of Amazon Textract features to apply. If you chose ``TEXTRACT_ANALYZE_DOCUMENT`` as the read action, you must specify one or both of the following values: - ``TABLES`` - Returns information about any tables that are detected in the input document. - ``FORMS`` - Returns information and the data from any forms that are detected in the input document.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentreaderconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_comprehend as comprehend
                
                document_reader_config_property = comprehend.CfnDocumentClassifier.DocumentReaderConfigProperty(
                    document_read_action="documentReadAction",
                
                    # the properties below are optional
                    document_read_mode="documentReadMode",
                    feature_types=["featureTypes"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9a59e8bf862d2e7b6710a1f4c7b803a6d7a9ef268c7f1764739d7738ad4a2061)
                check_type(argname="argument document_read_action", value=document_read_action, expected_type=type_hints["document_read_action"])
                check_type(argname="argument document_read_mode", value=document_read_mode, expected_type=type_hints["document_read_mode"])
                check_type(argname="argument feature_types", value=feature_types, expected_type=type_hints["feature_types"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "document_read_action": document_read_action,
            }
            if document_read_mode is not None:
                self._values["document_read_mode"] = document_read_mode
            if feature_types is not None:
                self._values["feature_types"] = feature_types

        @builtins.property
        def document_read_action(self) -> builtins.str:
            '''This field defines the Amazon Textract API operation that Amazon Comprehend uses to extract text from PDF files and image files.

            Enter one of the following values:

            - ``TEXTRACT_DETECT_DOCUMENT_TEXT`` - The Amazon Comprehend service uses the ``DetectDocumentText`` API operation.
            - ``TEXTRACT_ANALYZE_DOCUMENT`` - The Amazon Comprehend service uses the ``AnalyzeDocument`` API operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentreaderconfig.html#cfn-comprehend-documentclassifier-documentreaderconfig-documentreadaction
            '''
            result = self._values.get("document_read_action")
            assert result is not None, "Required property 'document_read_action' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def document_read_mode(self) -> typing.Optional[builtins.str]:
            '''Determines the text extraction actions for PDF files. Enter one of the following values:.

            - ``SERVICE_DEFAULT`` - use the Amazon Comprehend service defaults for PDF files.
            - ``FORCE_DOCUMENT_READ_ACTION`` - Amazon Comprehend uses the Textract API specified by DocumentReadAction for all PDF files, including digital PDF files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentreaderconfig.html#cfn-comprehend-documentclassifier-documentreaderconfig-documentreadmode
            '''
            result = self._values.get("document_read_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def feature_types(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Specifies the type of Amazon Textract features to apply.

            If you chose ``TEXTRACT_ANALYZE_DOCUMENT`` as the read action, you must specify one or both of the following values:

            - ``TABLES`` - Returns information about any tables that are detected in the input document.
            - ``FORMS`` - Returns information and the data from any forms that are detected in the input document.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-documentreaderconfig.html#cfn-comprehend-documentclassifier-documentreaderconfig-featuretypes
            '''
            result = self._values.get("feature_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DocumentReaderConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_comprehend.CfnDocumentClassifier.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"security_group_ids": "securityGroupIds", "subnets": "subnets"},
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Sequence[builtins.str],
            subnets: typing.Sequence[builtins.str],
        ) -> None:
            '''Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for the job.

            For more information, see `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`_ .

            :param security_group_ids: The ID number for a security group on an instance of your private VPC. Security groups on your VPC function serve as a virtual firewall to control inbound and outbound traffic and provides security for the resources that you’ll be accessing on the VPC. This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information, see `Security Groups for your VPC <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`_ .
            :param subnets: The ID for each subnet being used in your private VPC. This subnet is a subset of the a range of IPv4 addresses used by the VPC and is specific to a given availability zone in the VPC’s Region. This ID number is preceded by "subnet-", for instance: "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-vpcconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_comprehend as comprehend
                
                vpc_config_property = comprehend.CfnDocumentClassifier.VpcConfigProperty(
                    security_group_ids=["securityGroupIds"],
                    subnets=["subnets"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4e8c9eb83a42e141603118fff6dba5cc0774a8a4602d73ce0f9caec1b86975eb)
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "security_group_ids": security_group_ids,
                "subnets": subnets,
            }

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            '''The ID number for a security group on an instance of your private VPC.

            Security groups on your VPC function serve as a virtual firewall to control inbound and outbound traffic and provides security for the resources that you’ll be accessing on the VPC. This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information, see `Security Groups for your VPC <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-vpcconfig.html#cfn-comprehend-documentclassifier-vpcconfig-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnets(self) -> typing.List[builtins.str]:
            '''The ID for each subnet being used in your private VPC.

            This subnet is a subset of the a range of IPv4 addresses used by the VPC and is specific to a given availability zone in the VPC’s Region. This ID number is preceded by "subnet-", for instance: "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-documentclassifier-vpcconfig.html#cfn-comprehend-documentclassifier-vpcconfig-subnets
            '''
            result = self._values.get("subnets")
            assert result is not None, "Required property 'subnets' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_comprehend.CfnDocumentClassifierProps",
    jsii_struct_bases=[],
    name_mapping={
        "data_access_role_arn": "dataAccessRoleArn",
        "document_classifier_name": "documentClassifierName",
        "input_data_config": "inputDataConfig",
        "language_code": "languageCode",
        "mode": "mode",
        "model_kms_key_id": "modelKmsKeyId",
        "model_policy": "modelPolicy",
        "output_data_config": "outputDataConfig",
        "tags": "tags",
        "version_name": "versionName",
        "volume_kms_key_id": "volumeKmsKeyId",
        "vpc_config": "vpcConfig",
    },
)
class CfnDocumentClassifierProps:
    def __init__(
        self,
        *,
        data_access_role_arn: builtins.str,
        document_classifier_name: builtins.str,
        input_data_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDocumentClassifier.DocumentClassifierInputDataConfigProperty, typing.Dict[builtins.str, typing.Any]]],
        language_code: builtins.str,
        mode: typing.Optional[builtins.str] = None,
        model_kms_key_id: typing.Optional[builtins.str] = None,
        model_policy: typing.Optional[builtins.str] = None,
        output_data_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDocumentClassifier.DocumentClassifierOutputDataConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        version_name: typing.Optional[builtins.str] = None,
        volume_kms_key_id: typing.Optional[builtins.str] = None,
        vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDocumentClassifier.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDocumentClassifier``.

        :param data_access_role_arn: The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.
        :param document_classifier_name: The name of the document classifier.
        :param input_data_config: Specifies the format and location of the input data for the job.
        :param language_code: The language of the input documents. You can specify any of the languages supported by Amazon Comprehend. All documents must be in the same language.
        :param mode: Indicates the mode in which the classifier will be trained. The classifier can be trained in multi-class mode, which identifies one and only one class for each document, or multi-label mode, which identifies one or more labels for each document. In multi-label mode, multiple labels for an individual document are separated by a delimiter. The default delimiter between labels is a pipe (|).
        :param model_kms_key_id: ID for the AWS KMS key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats: - KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"`` - Amazon Resource Name (ARN) of a KMS Key: ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``
        :param model_policy: The resource-based policy to attach to your custom document classifier model. You can use this policy to allow another AWS account to import your custom model. Provide your policy as a JSON body that you enter as a UTF-8 encoded string without line breaks. To provide valid JSON, enclose the attribute names and values in double quotes. If the JSON body is also enclosed in double quotes, then you must escape the double quotes that are inside the policy: ``"{\\"attribute\\": \\"value\\", \\"attribute\\": [\\"value\\"]}"`` To avoid escaping quotes, you can use single quotes to enclose the policy and double quotes to enclose the JSON names and values: ``'{"attribute": "value", "attribute": ["value"]}'``
        :param output_data_config: Provides output results configuration parameters for custom classifier jobs.
        :param tags: Tags to associate with the document classifier. A tag is a key-value pair that adds as a metadata to a resource used by Amazon Comprehend. For example, a tag with "Sales" as the key might be added to a resource to indicate its use by the sales department.
        :param version_name: The version name given to the newly created classifier. Version names can have a maximum of 256 characters. Alphanumeric characters, hyphens (-) and underscores (_) are allowed. The version name must be unique among all models with the same classifier name in the AWS account / AWS Region .
        :param volume_kms_key_id: ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats: - KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"`` - Amazon Resource Name (ARN) of a KMS Key: ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``
        :param vpc_config: Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources you are using for your custom classifier. For more information, see `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-documentclassifier.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_comprehend as comprehend
            
            cfn_document_classifier_props = comprehend.CfnDocumentClassifierProps(
                data_access_role_arn="dataAccessRoleArn",
                document_classifier_name="documentClassifierName",
                input_data_config=comprehend.CfnDocumentClassifier.DocumentClassifierInputDataConfigProperty(
                    augmented_manifests=[comprehend.CfnDocumentClassifier.AugmentedManifestsListItemProperty(
                        attribute_names=["attributeNames"],
                        s3_uri="s3Uri",
            
                        # the properties below are optional
                        split="split"
                    )],
                    data_format="dataFormat",
                    document_reader_config=comprehend.CfnDocumentClassifier.DocumentReaderConfigProperty(
                        document_read_action="documentReadAction",
            
                        # the properties below are optional
                        document_read_mode="documentReadMode",
                        feature_types=["featureTypes"]
                    ),
                    documents=comprehend.CfnDocumentClassifier.DocumentClassifierDocumentsProperty(
                        s3_uri="s3Uri",
            
                        # the properties below are optional
                        test_s3_uri="testS3Uri"
                    ),
                    document_type="documentType",
                    label_delimiter="labelDelimiter",
                    s3_uri="s3Uri",
                    test_s3_uri="testS3Uri"
                ),
                language_code="languageCode",
            
                # the properties below are optional
                mode="mode",
                model_kms_key_id="modelKmsKeyId",
                model_policy="modelPolicy",
                output_data_config=comprehend.CfnDocumentClassifier.DocumentClassifierOutputDataConfigProperty(
                    kms_key_id="kmsKeyId",
                    s3_uri="s3Uri"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                version_name="versionName",
                volume_kms_key_id="volumeKmsKeyId",
                vpc_config=comprehend.CfnDocumentClassifier.VpcConfigProperty(
                    security_group_ids=["securityGroupIds"],
                    subnets=["subnets"]
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7d72cba46a86b5cfc5fb202d8e4e9466278a4b300f044f71c8d02ce52312e20)
            check_type(argname="argument data_access_role_arn", value=data_access_role_arn, expected_type=type_hints["data_access_role_arn"])
            check_type(argname="argument document_classifier_name", value=document_classifier_name, expected_type=type_hints["document_classifier_name"])
            check_type(argname="argument input_data_config", value=input_data_config, expected_type=type_hints["input_data_config"])
            check_type(argname="argument language_code", value=language_code, expected_type=type_hints["language_code"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument model_kms_key_id", value=model_kms_key_id, expected_type=type_hints["model_kms_key_id"])
            check_type(argname="argument model_policy", value=model_policy, expected_type=type_hints["model_policy"])
            check_type(argname="argument output_data_config", value=output_data_config, expected_type=type_hints["output_data_config"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument version_name", value=version_name, expected_type=type_hints["version_name"])
            check_type(argname="argument volume_kms_key_id", value=volume_kms_key_id, expected_type=type_hints["volume_kms_key_id"])
            check_type(argname="argument vpc_config", value=vpc_config, expected_type=type_hints["vpc_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_access_role_arn": data_access_role_arn,
            "document_classifier_name": document_classifier_name,
            "input_data_config": input_data_config,
            "language_code": language_code,
        }
        if mode is not None:
            self._values["mode"] = mode
        if model_kms_key_id is not None:
            self._values["model_kms_key_id"] = model_kms_key_id
        if model_policy is not None:
            self._values["model_policy"] = model_policy
        if output_data_config is not None:
            self._values["output_data_config"] = output_data_config
        if tags is not None:
            self._values["tags"] = tags
        if version_name is not None:
            self._values["version_name"] = version_name
        if volume_kms_key_id is not None:
            self._values["volume_kms_key_id"] = volume_kms_key_id
        if vpc_config is not None:
            self._values["vpc_config"] = vpc_config

    @builtins.property
    def data_access_role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-documentclassifier.html#cfn-comprehend-documentclassifier-dataaccessrolearn
        '''
        result = self._values.get("data_access_role_arn")
        assert result is not None, "Required property 'data_access_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def document_classifier_name(self) -> builtins.str:
        '''The name of the document classifier.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-documentclassifier.html#cfn-comprehend-documentclassifier-documentclassifiername
        '''
        result = self._values.get("document_classifier_name")
        assert result is not None, "Required property 'document_classifier_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def input_data_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnDocumentClassifier.DocumentClassifierInputDataConfigProperty]:
        '''Specifies the format and location of the input data for the job.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-documentclassifier.html#cfn-comprehend-documentclassifier-inputdataconfig
        '''
        result = self._values.get("input_data_config")
        assert result is not None, "Required property 'input_data_config' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnDocumentClassifier.DocumentClassifierInputDataConfigProperty], result)

    @builtins.property
    def language_code(self) -> builtins.str:
        '''The language of the input documents.

        You can specify any of the languages supported by Amazon Comprehend. All documents must be in the same language.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-documentclassifier.html#cfn-comprehend-documentclassifier-languagecode
        '''
        result = self._values.get("language_code")
        assert result is not None, "Required property 'language_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mode(self) -> typing.Optional[builtins.str]:
        '''Indicates the mode in which the classifier will be trained.

        The classifier can be trained in multi-class mode, which identifies one and only one class for each document, or multi-label mode, which identifies one or more labels for each document. In multi-label mode, multiple labels for an individual document are separated by a delimiter. The default delimiter between labels is a pipe (|).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-documentclassifier.html#cfn-comprehend-documentclassifier-mode
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def model_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''ID for the AWS KMS key that Amazon Comprehend uses to encrypt trained custom models.

        The ModelKmsKeyId can be either of the following formats:

        - KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``
        - Amazon Resource Name (ARN) of a KMS Key: ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-documentclassifier.html#cfn-comprehend-documentclassifier-modelkmskeyid
        '''
        result = self._values.get("model_kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def model_policy(self) -> typing.Optional[builtins.str]:
        '''The resource-based policy to attach to your custom document classifier model.

        You can use this policy to allow another AWS account to import your custom model.

        Provide your policy as a JSON body that you enter as a UTF-8 encoded string without line breaks. To provide valid JSON, enclose the attribute names and values in double quotes. If the JSON body is also enclosed in double quotes, then you must escape the double quotes that are inside the policy:

        ``"{\\"attribute\\": \\"value\\", \\"attribute\\": [\\"value\\"]}"``

        To avoid escaping quotes, you can use single quotes to enclose the policy and double quotes to enclose the JSON names and values:

        ``'{"attribute": "value", "attribute": ["value"]}'``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-documentclassifier.html#cfn-comprehend-documentclassifier-modelpolicy
        '''
        result = self._values.get("model_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def output_data_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDocumentClassifier.DocumentClassifierOutputDataConfigProperty]]:
        '''Provides output results configuration parameters for custom classifier jobs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-documentclassifier.html#cfn-comprehend-documentclassifier-outputdataconfig
        '''
        result = self._values.get("output_data_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDocumentClassifier.DocumentClassifierOutputDataConfigProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags to associate with the document classifier.

        A tag is a key-value pair that adds as a metadata to a resource used by Amazon Comprehend. For example, a tag with "Sales" as the key might be added to a resource to indicate its use by the sales department.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-documentclassifier.html#cfn-comprehend-documentclassifier-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def version_name(self) -> typing.Optional[builtins.str]:
        '''The version name given to the newly created classifier.

        Version names can have a maximum of 256 characters. Alphanumeric characters, hyphens (-) and underscores (_) are allowed. The version name must be unique among all models with the same classifier name in the AWS account / AWS Region .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-documentclassifier.html#cfn-comprehend-documentclassifier-versionname
        '''
        result = self._values.get("version_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job.

        The VolumeKmsKeyId can be either of the following formats:

        - KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``
        - Amazon Resource Name (ARN) of a KMS Key: ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-documentclassifier.html#cfn-comprehend-documentclassifier-volumekmskeyid
        '''
        result = self._values.get("volume_kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDocumentClassifier.VpcConfigProperty]]:
        '''Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources you are using for your custom classifier.

        For more information, see `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-documentclassifier.html#cfn-comprehend-documentclassifier-vpcconfig
        '''
        result = self._values.get("vpc_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDocumentClassifier.VpcConfigProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDocumentClassifierProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnFlywheel(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_comprehend.CfnFlywheel",
):
    '''A flywheel is an AWS resource that orchestrates the ongoing training of a model for custom classification or custom entity recognition.

    You can create a flywheel to start with an existing trained model, or Comprehend can create and train a new model.

    When you create the flywheel, Comprehend creates a data lake in your account. The data lake holds the training data and test data for all versions of the model.

    To use a flywheel with an existing trained model, you specify the active model version. Comprehend copies the model's training data and test data into the flywheel's data lake.

    To use the flywheel with a new model, you need to provide a dataset for training data (and optional test data) when you create the flywheel.

    For more information about flywheels, see `Flywheel overview <https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html>`_ in the *Amazon Comprehend Developer Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_comprehend as comprehend
        
        cfn_flywheel = comprehend.CfnFlywheel(self, "MyCfnFlywheel",
            data_access_role_arn="dataAccessRoleArn",
            data_lake_s3_uri="dataLakeS3Uri",
            flywheel_name="flywheelName",
        
            # the properties below are optional
            active_model_arn="activeModelArn",
            data_security_config=comprehend.CfnFlywheel.DataSecurityConfigProperty(
                data_lake_kms_key_id="dataLakeKmsKeyId",
                model_kms_key_id="modelKmsKeyId",
                volume_kms_key_id="volumeKmsKeyId",
                vpc_config=comprehend.CfnFlywheel.VpcConfigProperty(
                    security_group_ids=["securityGroupIds"],
                    subnets=["subnets"]
                )
            ),
            model_type="modelType",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            task_config=comprehend.CfnFlywheel.TaskConfigProperty(
                language_code="languageCode",
        
                # the properties below are optional
                document_classification_config=comprehend.CfnFlywheel.DocumentClassificationConfigProperty(
                    mode="mode",
        
                    # the properties below are optional
                    labels=["labels"]
                ),
                entity_recognition_config=comprehend.CfnFlywheel.EntityRecognitionConfigProperty(
                    entity_types=[comprehend.CfnFlywheel.EntityTypesListItemProperty(
                        type="type"
                    )]
                )
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        data_access_role_arn: builtins.str,
        data_lake_s3_uri: builtins.str,
        flywheel_name: builtins.str,
        active_model_arn: typing.Optional[builtins.str] = None,
        data_security_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlywheel.DataSecurityConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        model_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        task_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlywheel.TaskConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param data_access_role_arn: The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend permission to access the flywheel data.
        :param data_lake_s3_uri: Amazon S3 URI of the data lake location.
        :param flywheel_name: Name for the flywheel.
        :param active_model_arn: The Amazon Resource Number (ARN) of the active model version.
        :param data_security_config: Data security configuration.
        :param model_type: Model type of the flywheel's model.
        :param tags: Tags associated with the endpoint being created. A tag is a key-value pair that adds metadata to the endpoint. For example, a tag with "Sales" as the key might be added to an endpoint to indicate its use by the sales department.
        :param task_config: Configuration about the model associated with a flywheel.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08326dbba3b3e1fbd1b7c33b09deb1212a1a2d4d763f2b2c49693b85d0558b1e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFlywheelProps(
            data_access_role_arn=data_access_role_arn,
            data_lake_s3_uri=data_lake_s3_uri,
            flywheel_name=flywheel_name,
            active_model_arn=active_model_arn,
            data_security_config=data_security_config,
            model_type=model_type,
            tags=tags,
            task_config=task_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd5e83f45c4cf44e8697ad9475aa4568fb7e46c1e55467960eb2fbba73831db0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d874e50f75c45908f76b98c03aedde4475f99a679bf11f72586d1db4114d3c56)
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
        '''The Amazon Resource Name (ARN) of the flywheel.

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
    @jsii.member(jsii_name="dataAccessRoleArn")
    def data_access_role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend permission to access the flywheel data.'''
        return typing.cast(builtins.str, jsii.get(self, "dataAccessRoleArn"))

    @data_access_role_arn.setter
    def data_access_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6321844bfb2a1d270a9c4a2ca41960fa47c97afa2d07b34a23bdabea326de4ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataAccessRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="dataLakeS3Uri")
    def data_lake_s3_uri(self) -> builtins.str:
        '''Amazon S3 URI of the data lake location.'''
        return typing.cast(builtins.str, jsii.get(self, "dataLakeS3Uri"))

    @data_lake_s3_uri.setter
    def data_lake_s3_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fff80441425e9cd64c92b9e465aff8a17d45193ef5cdfce2238dfa02368ad6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataLakeS3Uri", value)

    @builtins.property
    @jsii.member(jsii_name="flywheelName")
    def flywheel_name(self) -> builtins.str:
        '''Name for the flywheel.'''
        return typing.cast(builtins.str, jsii.get(self, "flywheelName"))

    @flywheel_name.setter
    def flywheel_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c532257e2d8a6f8744e338b4f351b10756345f6375da4dfa2cd7d6c070693a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flywheelName", value)

    @builtins.property
    @jsii.member(jsii_name="activeModelArn")
    def active_model_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Number (ARN) of the active model version.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "activeModelArn"))

    @active_model_arn.setter
    def active_model_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a83eb6aee874a71ef2102b785b12cf1d675f7af5d375d9a5440d9a3e8326938)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "activeModelArn", value)

    @builtins.property
    @jsii.member(jsii_name="dataSecurityConfig")
    def data_security_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlywheel.DataSecurityConfigProperty"]]:
        '''Data security configuration.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlywheel.DataSecurityConfigProperty"]], jsii.get(self, "dataSecurityConfig"))

    @data_security_config.setter
    def data_security_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlywheel.DataSecurityConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fd6d966515c5a7a9a270dde08d7f0431bd24b3c8ab2bf5c260c0fdd300d5b85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSecurityConfig", value)

    @builtins.property
    @jsii.member(jsii_name="modelType")
    def model_type(self) -> typing.Optional[builtins.str]:
        '''Model type of the flywheel's model.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modelType"))

    @model_type.setter
    def model_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__514af0a34ecf2e72cd065a5b350ad942f9e94663e6471b9b89fdd65f9b7916e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modelType", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags associated with the endpoint being created.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41a3b218c7e1174bfadbab052fd5bed02876b76b6078e4d6558275409d43b5ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="taskConfig")
    def task_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlywheel.TaskConfigProperty"]]:
        '''Configuration about the model associated with a flywheel.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlywheel.TaskConfigProperty"]], jsii.get(self, "taskConfig"))

    @task_config.setter
    def task_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlywheel.TaskConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0986d76e0fdf3e18c2b4c799702f67afa8cf1195e0284e9e6d264962d96deda0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskConfig", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_comprehend.CfnFlywheel.DataSecurityConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_lake_kms_key_id": "dataLakeKmsKeyId",
            "model_kms_key_id": "modelKmsKeyId",
            "volume_kms_key_id": "volumeKmsKeyId",
            "vpc_config": "vpcConfig",
        },
    )
    class DataSecurityConfigProperty:
        def __init__(
            self,
            *,
            data_lake_kms_key_id: typing.Optional[builtins.str] = None,
            model_kms_key_id: typing.Optional[builtins.str] = None,
            volume_kms_key_id: typing.Optional[builtins.str] = None,
            vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlywheel.VpcConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Data security configuration.

            :param data_lake_kms_key_id: ID for the AWS KMS key that Amazon Comprehend uses to encrypt the data in the data lake.
            :param model_kms_key_id: ID for the AWS KMS key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats: - KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"`` - Amazon Resource Name (ARN) of a KMS Key: ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``
            :param volume_kms_key_id: ID for the AWS KMS key that Amazon Comprehend uses to encrypt the volume.
            :param vpc_config: Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for the job. For more information, see `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-datasecurityconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_comprehend as comprehend
                
                data_security_config_property = comprehend.CfnFlywheel.DataSecurityConfigProperty(
                    data_lake_kms_key_id="dataLakeKmsKeyId",
                    model_kms_key_id="modelKmsKeyId",
                    volume_kms_key_id="volumeKmsKeyId",
                    vpc_config=comprehend.CfnFlywheel.VpcConfigProperty(
                        security_group_ids=["securityGroupIds"],
                        subnets=["subnets"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ff8373493505a153def3a8e5139b9d9d48859656b3e590520f078b93a19d00df)
                check_type(argname="argument data_lake_kms_key_id", value=data_lake_kms_key_id, expected_type=type_hints["data_lake_kms_key_id"])
                check_type(argname="argument model_kms_key_id", value=model_kms_key_id, expected_type=type_hints["model_kms_key_id"])
                check_type(argname="argument volume_kms_key_id", value=volume_kms_key_id, expected_type=type_hints["volume_kms_key_id"])
                check_type(argname="argument vpc_config", value=vpc_config, expected_type=type_hints["vpc_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if data_lake_kms_key_id is not None:
                self._values["data_lake_kms_key_id"] = data_lake_kms_key_id
            if model_kms_key_id is not None:
                self._values["model_kms_key_id"] = model_kms_key_id
            if volume_kms_key_id is not None:
                self._values["volume_kms_key_id"] = volume_kms_key_id
            if vpc_config is not None:
                self._values["vpc_config"] = vpc_config

        @builtins.property
        def data_lake_kms_key_id(self) -> typing.Optional[builtins.str]:
            '''ID for the AWS KMS key that Amazon Comprehend uses to encrypt the data in the data lake.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-datasecurityconfig.html#cfn-comprehend-flywheel-datasecurityconfig-datalakekmskeyid
            '''
            result = self._values.get("data_lake_kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def model_kms_key_id(self) -> typing.Optional[builtins.str]:
            '''ID for the AWS KMS key that Amazon Comprehend uses to encrypt trained custom models.

            The ModelKmsKeyId can be either of the following formats:

            - KMS Key ID: ``"1234abcd-12ab-34cd-56ef-1234567890ab"``
            - Amazon Resource Name (ARN) of a KMS Key: ``"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-datasecurityconfig.html#cfn-comprehend-flywheel-datasecurityconfig-modelkmskeyid
            '''
            result = self._values.get("model_kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def volume_kms_key_id(self) -> typing.Optional[builtins.str]:
            '''ID for the AWS KMS key that Amazon Comprehend uses to encrypt the volume.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-datasecurityconfig.html#cfn-comprehend-flywheel-datasecurityconfig-volumekmskeyid
            '''
            result = self._values.get("volume_kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vpc_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlywheel.VpcConfigProperty"]]:
            '''Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for the job.

            For more information, see `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-datasecurityconfig.html#cfn-comprehend-flywheel-datasecurityconfig-vpcconfig
            '''
            result = self._values.get("vpc_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlywheel.VpcConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataSecurityConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_comprehend.CfnFlywheel.DocumentClassificationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"mode": "mode", "labels": "labels"},
    )
    class DocumentClassificationConfigProperty:
        def __init__(
            self,
            *,
            mode: builtins.str,
            labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Configuration required for a document classification model.

            :param mode: Classification mode indicates whether the documents are ``MULTI_CLASS`` or ``MULTI_LABEL`` .
            :param labels: One or more labels to associate with the custom classifier.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-documentclassificationconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_comprehend as comprehend
                
                document_classification_config_property = comprehend.CfnFlywheel.DocumentClassificationConfigProperty(
                    mode="mode",
                
                    # the properties below are optional
                    labels=["labels"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0208591bc4eb6449ba2ec94d642467202e116283b6b07af3dcf486c7ac51e82a)
                check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
                check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "mode": mode,
            }
            if labels is not None:
                self._values["labels"] = labels

        @builtins.property
        def mode(self) -> builtins.str:
            '''Classification mode indicates whether the documents are ``MULTI_CLASS`` or ``MULTI_LABEL`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-documentclassificationconfig.html#cfn-comprehend-flywheel-documentclassificationconfig-mode
            '''
            result = self._values.get("mode")
            assert result is not None, "Required property 'mode' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def labels(self) -> typing.Optional[typing.List[builtins.str]]:
            '''One or more labels to associate with the custom classifier.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-documentclassificationconfig.html#cfn-comprehend-flywheel-documentclassificationconfig-labels
            '''
            result = self._values.get("labels")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DocumentClassificationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_comprehend.CfnFlywheel.EntityRecognitionConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"entity_types": "entityTypes"},
    )
    class EntityRecognitionConfigProperty:
        def __init__(
            self,
            *,
            entity_types: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlywheel.EntityTypesListItemProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Configuration required for an entity recognition model.

            :param entity_types: Up to 25 entity types that the model is trained to recognize.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-entityrecognitionconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_comprehend as comprehend
                
                entity_recognition_config_property = comprehend.CfnFlywheel.EntityRecognitionConfigProperty(
                    entity_types=[comprehend.CfnFlywheel.EntityTypesListItemProperty(
                        type="type"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__be861f74134a724bbb961275d90cd0dc1f9f6a80ba3ad69a6dd1d2865df480b1)
                check_type(argname="argument entity_types", value=entity_types, expected_type=type_hints["entity_types"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if entity_types is not None:
                self._values["entity_types"] = entity_types

        @builtins.property
        def entity_types(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFlywheel.EntityTypesListItemProperty"]]]]:
            '''Up to 25 entity types that the model is trained to recognize.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-entityrecognitionconfig.html#cfn-comprehend-flywheel-entityrecognitionconfig-entitytypes
            '''
            result = self._values.get("entity_types")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFlywheel.EntityTypesListItemProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EntityRecognitionConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_comprehend.CfnFlywheel.EntityTypesListItemProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type"},
    )
    class EntityTypesListItemProperty:
        def __init__(self, *, type: builtins.str) -> None:
            '''An entity type within a labeled training dataset that Amazon Comprehend uses to train a custom entity recognizer.

            :param type: An entity type within a labeled training dataset that Amazon Comprehend uses to train a custom entity recognizer. Entity types must not contain the following invalid characters: \\n (line break), \\n (escaped line break, \\r (carriage return), \\r (escaped carriage return), \\t (tab), \\t (escaped tab), space, and , (comma).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-entitytypeslistitem.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_comprehend as comprehend
                
                entity_types_list_item_property = comprehend.CfnFlywheel.EntityTypesListItemProperty(
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__92a4eeaf2d69acccc3b3d8d1d0551ae8552d2bf97966201e3ec32e4a8af8c8bf)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }

        @builtins.property
        def type(self) -> builtins.str:
            '''An entity type within a labeled training dataset that Amazon Comprehend uses to train a custom entity recognizer.

            Entity types must not contain the following invalid characters: \\n (line break), \\n (escaped line break, \\r (carriage return), \\r (escaped carriage return), \\t (tab), \\t (escaped tab), space, and , (comma).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-entitytypeslistitem.html#cfn-comprehend-flywheel-entitytypeslistitem-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EntityTypesListItemProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_comprehend.CfnFlywheel.TaskConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "language_code": "languageCode",
            "document_classification_config": "documentClassificationConfig",
            "entity_recognition_config": "entityRecognitionConfig",
        },
    )
    class TaskConfigProperty:
        def __init__(
            self,
            *,
            language_code: builtins.str,
            document_classification_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlywheel.DocumentClassificationConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            entity_recognition_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlywheel.EntityRecognitionConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Configuration about the model associated with a flywheel.

            :param language_code: Language code for the language that the model supports.
            :param document_classification_config: Configuration required for a document classification model.
            :param entity_recognition_config: Configuration required for an entity recognition model.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-taskconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_comprehend as comprehend
                
                task_config_property = comprehend.CfnFlywheel.TaskConfigProperty(
                    language_code="languageCode",
                
                    # the properties below are optional
                    document_classification_config=comprehend.CfnFlywheel.DocumentClassificationConfigProperty(
                        mode="mode",
                
                        # the properties below are optional
                        labels=["labels"]
                    ),
                    entity_recognition_config=comprehend.CfnFlywheel.EntityRecognitionConfigProperty(
                        entity_types=[comprehend.CfnFlywheel.EntityTypesListItemProperty(
                            type="type"
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8b33cd312cecdc06a8bdf8295b58c64bf16dac30f37454b9584e214a7a169c56)
                check_type(argname="argument language_code", value=language_code, expected_type=type_hints["language_code"])
                check_type(argname="argument document_classification_config", value=document_classification_config, expected_type=type_hints["document_classification_config"])
                check_type(argname="argument entity_recognition_config", value=entity_recognition_config, expected_type=type_hints["entity_recognition_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "language_code": language_code,
            }
            if document_classification_config is not None:
                self._values["document_classification_config"] = document_classification_config
            if entity_recognition_config is not None:
                self._values["entity_recognition_config"] = entity_recognition_config

        @builtins.property
        def language_code(self) -> builtins.str:
            '''Language code for the language that the model supports.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-taskconfig.html#cfn-comprehend-flywheel-taskconfig-languagecode
            '''
            result = self._values.get("language_code")
            assert result is not None, "Required property 'language_code' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def document_classification_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlywheel.DocumentClassificationConfigProperty"]]:
            '''Configuration required for a document classification model.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-taskconfig.html#cfn-comprehend-flywheel-taskconfig-documentclassificationconfig
            '''
            result = self._values.get("document_classification_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlywheel.DocumentClassificationConfigProperty"]], result)

        @builtins.property
        def entity_recognition_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlywheel.EntityRecognitionConfigProperty"]]:
            '''Configuration required for an entity recognition model.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-taskconfig.html#cfn-comprehend-flywheel-taskconfig-entityrecognitionconfig
            '''
            result = self._values.get("entity_recognition_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlywheel.EntityRecognitionConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TaskConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_comprehend.CfnFlywheel.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"security_group_ids": "securityGroupIds", "subnets": "subnets"},
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Sequence[builtins.str],
            subnets: typing.Sequence[builtins.str],
        ) -> None:
            '''Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for the job.

            For more information, see `Amazon VPC <https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html>`_ .

            :param security_group_ids: The ID number for a security group on an instance of your private VPC. Security groups on your VPC function serve as a virtual firewall to control inbound and outbound traffic and provides security for the resources that you’ll be accessing on the VPC. This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information, see `Security Groups for your VPC <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`_ .
            :param subnets: The ID for each subnet being used in your private VPC. This subnet is a subset of the a range of IPv4 addresses used by the VPC and is specific to a given availability zone in the VPC’s Region. This ID number is preceded by "subnet-", for instance: "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-vpcconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_comprehend as comprehend
                
                vpc_config_property = comprehend.CfnFlywheel.VpcConfigProperty(
                    security_group_ids=["securityGroupIds"],
                    subnets=["subnets"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6f148a8e29a057dfa8bd6a5945aaf37e92f70297900e6a35e12b4f9de104ca70)
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "security_group_ids": security_group_ids,
                "subnets": subnets,
            }

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            '''The ID number for a security group on an instance of your private VPC.

            Security groups on your VPC function serve as a virtual firewall to control inbound and outbound traffic and provides security for the resources that you’ll be accessing on the VPC. This ID number is preceded by "sg-", for instance: "sg-03b388029b0a285ea". For more information, see `Security Groups for your VPC <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-vpcconfig.html#cfn-comprehend-flywheel-vpcconfig-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnets(self) -> typing.List[builtins.str]:
            '''The ID for each subnet being used in your private VPC.

            This subnet is a subset of the a range of IPv4 addresses used by the VPC and is specific to a given availability zone in the VPC’s Region. This ID number is preceded by "subnet-", for instance: "subnet-04ccf456919e69055". For more information, see `VPCs and Subnets <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-comprehend-flywheel-vpcconfig.html#cfn-comprehend-flywheel-vpcconfig-subnets
            '''
            result = self._values.get("subnets")
            assert result is not None, "Required property 'subnets' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_comprehend.CfnFlywheelProps",
    jsii_struct_bases=[],
    name_mapping={
        "data_access_role_arn": "dataAccessRoleArn",
        "data_lake_s3_uri": "dataLakeS3Uri",
        "flywheel_name": "flywheelName",
        "active_model_arn": "activeModelArn",
        "data_security_config": "dataSecurityConfig",
        "model_type": "modelType",
        "tags": "tags",
        "task_config": "taskConfig",
    },
)
class CfnFlywheelProps:
    def __init__(
        self,
        *,
        data_access_role_arn: builtins.str,
        data_lake_s3_uri: builtins.str,
        flywheel_name: builtins.str,
        active_model_arn: typing.Optional[builtins.str] = None,
        data_security_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlywheel.DataSecurityConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        model_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        task_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlywheel.TaskConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFlywheel``.

        :param data_access_role_arn: The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend permission to access the flywheel data.
        :param data_lake_s3_uri: Amazon S3 URI of the data lake location.
        :param flywheel_name: Name for the flywheel.
        :param active_model_arn: The Amazon Resource Number (ARN) of the active model version.
        :param data_security_config: Data security configuration.
        :param model_type: Model type of the flywheel's model.
        :param tags: Tags associated with the endpoint being created. A tag is a key-value pair that adds metadata to the endpoint. For example, a tag with "Sales" as the key might be added to an endpoint to indicate its use by the sales department.
        :param task_config: Configuration about the model associated with a flywheel.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_comprehend as comprehend
            
            cfn_flywheel_props = comprehend.CfnFlywheelProps(
                data_access_role_arn="dataAccessRoleArn",
                data_lake_s3_uri="dataLakeS3Uri",
                flywheel_name="flywheelName",
            
                # the properties below are optional
                active_model_arn="activeModelArn",
                data_security_config=comprehend.CfnFlywheel.DataSecurityConfigProperty(
                    data_lake_kms_key_id="dataLakeKmsKeyId",
                    model_kms_key_id="modelKmsKeyId",
                    volume_kms_key_id="volumeKmsKeyId",
                    vpc_config=comprehend.CfnFlywheel.VpcConfigProperty(
                        security_group_ids=["securityGroupIds"],
                        subnets=["subnets"]
                    )
                ),
                model_type="modelType",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                task_config=comprehend.CfnFlywheel.TaskConfigProperty(
                    language_code="languageCode",
            
                    # the properties below are optional
                    document_classification_config=comprehend.CfnFlywheel.DocumentClassificationConfigProperty(
                        mode="mode",
            
                        # the properties below are optional
                        labels=["labels"]
                    ),
                    entity_recognition_config=comprehend.CfnFlywheel.EntityRecognitionConfigProperty(
                        entity_types=[comprehend.CfnFlywheel.EntityTypesListItemProperty(
                            type="type"
                        )]
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__354388f245744b59494c23dd6a47939e13228c4105132c6911824acf04080c64)
            check_type(argname="argument data_access_role_arn", value=data_access_role_arn, expected_type=type_hints["data_access_role_arn"])
            check_type(argname="argument data_lake_s3_uri", value=data_lake_s3_uri, expected_type=type_hints["data_lake_s3_uri"])
            check_type(argname="argument flywheel_name", value=flywheel_name, expected_type=type_hints["flywheel_name"])
            check_type(argname="argument active_model_arn", value=active_model_arn, expected_type=type_hints["active_model_arn"])
            check_type(argname="argument data_security_config", value=data_security_config, expected_type=type_hints["data_security_config"])
            check_type(argname="argument model_type", value=model_type, expected_type=type_hints["model_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument task_config", value=task_config, expected_type=type_hints["task_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_access_role_arn": data_access_role_arn,
            "data_lake_s3_uri": data_lake_s3_uri,
            "flywheel_name": flywheel_name,
        }
        if active_model_arn is not None:
            self._values["active_model_arn"] = active_model_arn
        if data_security_config is not None:
            self._values["data_security_config"] = data_security_config
        if model_type is not None:
            self._values["model_type"] = model_type
        if tags is not None:
            self._values["tags"] = tags
        if task_config is not None:
            self._values["task_config"] = task_config

    @builtins.property
    def data_access_role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend permission to access the flywheel data.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html#cfn-comprehend-flywheel-dataaccessrolearn
        '''
        result = self._values.get("data_access_role_arn")
        assert result is not None, "Required property 'data_access_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_lake_s3_uri(self) -> builtins.str:
        '''Amazon S3 URI of the data lake location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html#cfn-comprehend-flywheel-datalakes3uri
        '''
        result = self._values.get("data_lake_s3_uri")
        assert result is not None, "Required property 'data_lake_s3_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def flywheel_name(self) -> builtins.str:
        '''Name for the flywheel.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html#cfn-comprehend-flywheel-flywheelname
        '''
        result = self._values.get("flywheel_name")
        assert result is not None, "Required property 'flywheel_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def active_model_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Number (ARN) of the active model version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html#cfn-comprehend-flywheel-activemodelarn
        '''
        result = self._values.get("active_model_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_security_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlywheel.DataSecurityConfigProperty]]:
        '''Data security configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html#cfn-comprehend-flywheel-datasecurityconfig
        '''
        result = self._values.get("data_security_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlywheel.DataSecurityConfigProperty]], result)

    @builtins.property
    def model_type(self) -> typing.Optional[builtins.str]:
        '''Model type of the flywheel's model.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html#cfn-comprehend-flywheel-modeltype
        '''
        result = self._values.get("model_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags associated with the endpoint being created.

        A tag is a key-value pair that adds metadata to the endpoint. For example, a tag with "Sales" as the key might be added to an endpoint to indicate its use by the sales department.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html#cfn-comprehend-flywheel-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def task_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlywheel.TaskConfigProperty]]:
        '''Configuration about the model associated with a flywheel.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-comprehend-flywheel.html#cfn-comprehend-flywheel-taskconfig
        '''
        result = self._values.get("task_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlywheel.TaskConfigProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFlywheelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDocumentClassifier",
    "CfnDocumentClassifierProps",
    "CfnFlywheel",
    "CfnFlywheelProps",
]

publication.publish()

def _typecheckingstub__0da43afef06b62227e1171021a9a7ce43e2e481fa3c1ff8263e87fc9d8a04a11(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    data_access_role_arn: builtins.str,
    document_classifier_name: builtins.str,
    input_data_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDocumentClassifier.DocumentClassifierInputDataConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    language_code: builtins.str,
    mode: typing.Optional[builtins.str] = None,
    model_kms_key_id: typing.Optional[builtins.str] = None,
    model_policy: typing.Optional[builtins.str] = None,
    output_data_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDocumentClassifier.DocumentClassifierOutputDataConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    version_name: typing.Optional[builtins.str] = None,
    volume_kms_key_id: typing.Optional[builtins.str] = None,
    vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDocumentClassifier.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92e2c4b33fb017d2bc9b1ee4c697a9167f78647f346ac5244d2bc0fd757caafc(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__287be59af197ae51a952af63959a3e03141cb3cc954016e70bb810f820be527d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b37e87366af30e1867ccce78466a7f4c6d746af1145b7d79190f47f81c93150(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__638faf1cde59d08f5f01020564bc1e88a6cea30b7dabcd32bafb9e2a19679e22(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72e4443e99a7ca079c78d2d3e95ad08de986276725c191c60fe4bb9c079cb943(
    value: typing.Union[_IResolvable_da3f097b, CfnDocumentClassifier.DocumentClassifierInputDataConfigProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e3dc92e7423146f7bc3fa270f51b1ccf6814b377e155ee2ed7fa29304a9af1b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a57a1c717c1a0c5a74255154c12499f2db8a5c7a4fa572ddbcd498ad15f6521(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef8b3a8450ff07c6f8a82db094f1c024cdae25ff4129f6dfa51b3a56a75ba47f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04fae6cd4c58f60cada64d8d21b84531af3aa7e5eaf941164906bbef62922cdb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77e41c78333ebb35c2df89407137e02c535908d5a9507232b4191645cf0b545b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDocumentClassifier.DocumentClassifierOutputDataConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c98bb6f280f6bbf3f16d43daf50dcb88973e23a7318af37a5a3b1abcea57d5c5(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cfd73724bd487f3406d963cae58c0001de744cd65d9ffc08a8c4cbd317494ad(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__344f34dca22ae27ea74f0d21ce8353bfd4b47f3b3f4d5bbb468ee6c3d66a5bae(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abdfe2fb65b1015aa13bcd7af0d9989b0bf86879cf9af256182e344894204fd3(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDocumentClassifier.VpcConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e7be165e53934b67c373db8aca52b6ed7c0c1d73712fc19358c759cd06f6d7d(
    *,
    attribute_names: typing.Sequence[builtins.str],
    s3_uri: builtins.str,
    split: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b9a924b5e8313e96401e175a3cc69b5e202e2094cfee26902965392b9115295(
    *,
    s3_uri: builtins.str,
    test_s3_uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8453f7adcda177853e8778d17871cc98c5d202507a96232815d58242cb75d024(
    *,
    augmented_manifests: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDocumentClassifier.AugmentedManifestsListItemProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    data_format: typing.Optional[builtins.str] = None,
    document_reader_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDocumentClassifier.DocumentReaderConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    documents: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDocumentClassifier.DocumentClassifierDocumentsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    document_type: typing.Optional[builtins.str] = None,
    label_delimiter: typing.Optional[builtins.str] = None,
    s3_uri: typing.Optional[builtins.str] = None,
    test_s3_uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8be9905eb78b42938653d2997696c7efead62cdf90ea74df719050f8916d9ebd(
    *,
    kms_key_id: typing.Optional[builtins.str] = None,
    s3_uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a59e8bf862d2e7b6710a1f4c7b803a6d7a9ef268c7f1764739d7738ad4a2061(
    *,
    document_read_action: builtins.str,
    document_read_mode: typing.Optional[builtins.str] = None,
    feature_types: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e8c9eb83a42e141603118fff6dba5cc0774a8a4602d73ce0f9caec1b86975eb(
    *,
    security_group_ids: typing.Sequence[builtins.str],
    subnets: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7d72cba46a86b5cfc5fb202d8e4e9466278a4b300f044f71c8d02ce52312e20(
    *,
    data_access_role_arn: builtins.str,
    document_classifier_name: builtins.str,
    input_data_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDocumentClassifier.DocumentClassifierInputDataConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    language_code: builtins.str,
    mode: typing.Optional[builtins.str] = None,
    model_kms_key_id: typing.Optional[builtins.str] = None,
    model_policy: typing.Optional[builtins.str] = None,
    output_data_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDocumentClassifier.DocumentClassifierOutputDataConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    version_name: typing.Optional[builtins.str] = None,
    volume_kms_key_id: typing.Optional[builtins.str] = None,
    vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDocumentClassifier.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08326dbba3b3e1fbd1b7c33b09deb1212a1a2d4d763f2b2c49693b85d0558b1e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    data_access_role_arn: builtins.str,
    data_lake_s3_uri: builtins.str,
    flywheel_name: builtins.str,
    active_model_arn: typing.Optional[builtins.str] = None,
    data_security_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlywheel.DataSecurityConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    model_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    task_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlywheel.TaskConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd5e83f45c4cf44e8697ad9475aa4568fb7e46c1e55467960eb2fbba73831db0(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d874e50f75c45908f76b98c03aedde4475f99a679bf11f72586d1db4114d3c56(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6321844bfb2a1d270a9c4a2ca41960fa47c97afa2d07b34a23bdabea326de4ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fff80441425e9cd64c92b9e465aff8a17d45193ef5cdfce2238dfa02368ad6c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c532257e2d8a6f8744e338b4f351b10756345f6375da4dfa2cd7d6c070693a0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a83eb6aee874a71ef2102b785b12cf1d675f7af5d375d9a5440d9a3e8326938(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fd6d966515c5a7a9a270dde08d7f0431bd24b3c8ab2bf5c260c0fdd300d5b85(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlywheel.DataSecurityConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__514af0a34ecf2e72cd065a5b350ad942f9e94663e6471b9b89fdd65f9b7916e2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41a3b218c7e1174bfadbab052fd5bed02876b76b6078e4d6558275409d43b5ee(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0986d76e0fdf3e18c2b4c799702f67afa8cf1195e0284e9e6d264962d96deda0(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlywheel.TaskConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff8373493505a153def3a8e5139b9d9d48859656b3e590520f078b93a19d00df(
    *,
    data_lake_kms_key_id: typing.Optional[builtins.str] = None,
    model_kms_key_id: typing.Optional[builtins.str] = None,
    volume_kms_key_id: typing.Optional[builtins.str] = None,
    vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlywheel.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0208591bc4eb6449ba2ec94d642467202e116283b6b07af3dcf486c7ac51e82a(
    *,
    mode: builtins.str,
    labels: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be861f74134a724bbb961275d90cd0dc1f9f6a80ba3ad69a6dd1d2865df480b1(
    *,
    entity_types: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlywheel.EntityTypesListItemProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92a4eeaf2d69acccc3b3d8d1d0551ae8552d2bf97966201e3ec32e4a8af8c8bf(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b33cd312cecdc06a8bdf8295b58c64bf16dac30f37454b9584e214a7a169c56(
    *,
    language_code: builtins.str,
    document_classification_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlywheel.DocumentClassificationConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    entity_recognition_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlywheel.EntityRecognitionConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f148a8e29a057dfa8bd6a5945aaf37e92f70297900e6a35e12b4f9de104ca70(
    *,
    security_group_ids: typing.Sequence[builtins.str],
    subnets: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__354388f245744b59494c23dd6a47939e13228c4105132c6911824acf04080c64(
    *,
    data_access_role_arn: builtins.str,
    data_lake_s3_uri: builtins.str,
    flywheel_name: builtins.str,
    active_model_arn: typing.Optional[builtins.str] = None,
    data_security_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlywheel.DataSecurityConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    model_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    task_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlywheel.TaskConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
