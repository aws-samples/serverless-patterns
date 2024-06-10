'''
# AWS::S3Express Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_s3express as s3express
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for S3Express construct libraries](https://constructs.dev/search?q=s3express)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::S3Express resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_S3Express.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::S3Express](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_S3Express.html).

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
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnBucketPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3express.CfnBucketPolicy",
):
    '''Applies an Amazon S3 bucket policy to an Amazon S3 directory bucket.

    - **Permissions** - If you are using an identity other than the root user of the AWS account that owns the bucket, the calling identity must both have the required permissions on the specified bucket and belong to the bucket owner's account in order to use this operation. For more information about directory bucket policies and permissions, see `AWS Identity and Access Management (IAM) for S3 Express One Zone <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-iam.html>`_ in the *Amazon S3 User Guide* .

    .. epigraph::

       To ensure that bucket owners don't inadvertently lock themselves out of their own buckets, the root principal in a bucket owner's AWS account can perform the ``GetBucketPolicy`` , ``PutBucketPolicy`` , and ``DeleteBucketPolicy`` API actions, even if their bucket policy explicitly denies the root principal's access. Bucket owner root principals can only be blocked from performing these API actions by VPC endpoint policies and AWS Organizations policies.

    The required permissions for CloudFormation to use are based on the operations that are performed on the stack.

    - Create
    - s3express:GetBucketPolicy
    - s3express:PutBucketPolicy
    - Read
    - s3express:GetBucketPolicy
    - Update
    - s3express:GetBucketPolicy
    - s3express:PutBucketPolicy
    - Delete
    - s3express:GetBucketPolicy
    - s3express:DeleteBucketPolicy
    - List
    - s3express:GetBucketPolicy
    - s3express:ListAllMyDirectoryBuckets

    For more information about example bucket policies, see `Example bucket policies for S3 Express One Zone <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-iam-example-bucket-policies.html>`_ in the *Amazon S3 User Guide* .

    The following operations are related to ``AWS::S3Express::BucketPolicy`` :

    - `PutBucketPolicy <https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketPolicy.html>`_
    - `GetBucketPolicy <https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicy.html>`_
    - `DeleteBucketPolicy <https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketPolicy.html>`_
    - `ListDirectoryBuckets <https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListDirectoryBuckets.html>`_

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3express-bucketpolicy.html
    :cloudformationResource: AWS::S3Express::BucketPolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_s3express as s3express
        
        # policy_document: Any
        
        cfn_bucket_policy = s3express.CfnBucketPolicy(self, "MyCfnBucketPolicy",
            bucket="bucket",
            policy_document=policy_document
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        bucket: builtins.str,
        policy_document: typing.Any,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param bucket: The name of the S3 directory bucket to which the policy applies.
        :param policy_document: A policy document containing permissions to add to the specified bucket. In IAM, you must provide policy documents in JSON format. However, in CloudFormation you can provide the policy in JSON or YAML format because CloudFormation converts YAML to JSON before submitting it to IAM. For more information, see the AWS::IAM::Policy `PolicyDocument <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html#cfn-iam-policy-policydocument>`_ resource description in this guide and `Policies and Permissions in Amazon S3 <https://docs.aws.amazon.com/AmazonS3/latest/dev/access-policy-language-overview.html>`_ in the *Amazon S3 User Guide* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7ae0c19fbf2c7c716bc3304458f2695912d196d3e7439999f721b69fdbfc5a0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBucketPolicyProps(bucket=bucket, policy_document=policy_document)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0da69b8aee8ed367e63ca61c9ad9c6ce2b5fd2aff3c02cb553118847c89867c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a427439734058e5e6251cd5c0aaeed7ade47e92954992912236d939d3b496350)
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
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        '''The name of the S3 directory bucket to which the policy applies.'''
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dedf6ffab37d96f5ca0d97fbcb6904b8dc185fd26912baba5f2b683aec30a5e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="policyDocument")
    def policy_document(self) -> typing.Any:
        '''A policy document containing permissions to add to the specified bucket.'''
        return typing.cast(typing.Any, jsii.get(self, "policyDocument"))

    @policy_document.setter
    def policy_document(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__575ca46990b1014411a210bab87827014d15a4bd9119ec2a06a134d0e642cfff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyDocument", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_s3express.CfnBucketPolicyProps",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket", "policy_document": "policyDocument"},
)
class CfnBucketPolicyProps:
    def __init__(self, *, bucket: builtins.str, policy_document: typing.Any) -> None:
        '''Properties for defining a ``CfnBucketPolicy``.

        :param bucket: The name of the S3 directory bucket to which the policy applies.
        :param policy_document: A policy document containing permissions to add to the specified bucket. In IAM, you must provide policy documents in JSON format. However, in CloudFormation you can provide the policy in JSON or YAML format because CloudFormation converts YAML to JSON before submitting it to IAM. For more information, see the AWS::IAM::Policy `PolicyDocument <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html#cfn-iam-policy-policydocument>`_ resource description in this guide and `Policies and Permissions in Amazon S3 <https://docs.aws.amazon.com/AmazonS3/latest/dev/access-policy-language-overview.html>`_ in the *Amazon S3 User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3express-bucketpolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_s3express as s3express
            
            # policy_document: Any
            
            cfn_bucket_policy_props = s3express.CfnBucketPolicyProps(
                bucket="bucket",
                policy_document=policy_document
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7978963298afc97ec8564e6e114bf73c7797f21fb71f9d0a187dd5852499f423)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument policy_document", value=policy_document, expected_type=type_hints["policy_document"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket": bucket,
            "policy_document": policy_document,
        }

    @builtins.property
    def bucket(self) -> builtins.str:
        '''The name of the S3 directory bucket to which the policy applies.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3express-bucketpolicy.html#cfn-s3express-bucketpolicy-bucket
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_document(self) -> typing.Any:
        '''A policy document containing permissions to add to the specified bucket.

        In IAM, you must provide policy documents in JSON format. However, in CloudFormation you can provide the policy in JSON or YAML format because CloudFormation converts YAML to JSON before submitting it to IAM. For more information, see the AWS::IAM::Policy `PolicyDocument <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html#cfn-iam-policy-policydocument>`_ resource description in this guide and `Policies and Permissions in Amazon S3 <https://docs.aws.amazon.com/AmazonS3/latest/dev/access-policy-language-overview.html>`_ in the *Amazon S3 User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3express-bucketpolicy.html#cfn-s3express-bucketpolicy-policydocument
        '''
        result = self._values.get("policy_document")
        assert result is not None, "Required property 'policy_document' is missing"
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBucketPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnDirectoryBucket(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3express.CfnDirectoryBucket",
):
    '''The ``AWS::S3Express::DirectoryBucket`` resource creates an Amazon S3 directory bucket in the same AWS Region where you create the AWS CloudFormation stack.

    To control how AWS CloudFormation handles the bucket when the stack is deleted, you can set a deletion policy for your bucket. You can choose to *retain* the bucket or to *delete* the bucket. For more information, see `DeletionPolicy attribute <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html>`_ .
    .. epigraph::

       You can only delete empty buckets. Deletion fails for buckets that have contents.

    - **Permissions** - The required permissions for CloudFormation to use are based on the operations that are performed on the stack.
    - Create
    - s3express:CreateBucket
    - s3express:ListAllMyDirectoryBuckets
    - Read
    - s3express:ListAllMyDirectoryBuckets
    - Delete
    - s3express:DeleteBucket
    - s3express:ListAllMyDirectoryBuckets
    - List
    - s3express:ListAllMyDirectoryBuckets

    The following operations are related to ``AWS::S3Express::DirectoryBucket`` :

    - `CreateBucket <https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html>`_
    - `ListDirectoryBuckets <https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListDirectoryBuckets.html>`_
    - `DeleteBucket <https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucket.html>`_

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3express-directorybucket.html
    :cloudformationResource: AWS::S3Express::DirectoryBucket
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_s3express as s3express
        
        cfn_directory_bucket = s3express.CfnDirectoryBucket(self, "MyCfnDirectoryBucket",
            data_redundancy="dataRedundancy",
            location_name="locationName",
        
            # the properties below are optional
            bucket_name="bucketName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        data_redundancy: builtins.str,
        location_name: builtins.str,
        bucket_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param data_redundancy: The number of Availability Zone that's used for redundancy for the bucket.
        :param location_name: The name of the location where the bucket will be created. For directory buckets, the name of the location is the AZ ID of the Availability Zone where the bucket will be created. An example AZ ID value is ``usw2-az1`` .
        :param bucket_name: A name for the bucket. The bucket name must contain only lowercase letters, numbers, and hyphens (-). A directory bucket name must be unique in the chosen Availability Zone. The bucket name must also follow the format ``*bucket_base_name* -- *az_id* --x-s3`` (for example, ``*DOC-EXAMPLE-BUCKET* -- *usw2-az1* --x-s3`` ). If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the bucket name. For information about bucket naming restrictions, see `Directory bucket naming rules <https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html>`_ in the *Amazon S3 User Guide* . .. epigraph:: If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you need to replace the resource, specify a new name.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea5a1e5897b0467fb93393ad6ea2dbcd3916f27713079e8bef3badf71ce2bb20)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDirectoryBucketProps(
            data_redundancy=data_redundancy,
            location_name=location_name,
            bucket_name=bucket_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61d4c01a14f34a0546048356b166c111adde5de129e3d0580f9ce73d26da1587)
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
            type_hints = typing.get_type_hints(_typecheckingstub__09d4f293955716375e6177306d2bdfa8106614896e901a12247190cc871e9e61)
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
        '''Returns the Amazon Resource Name (ARN) of the specified bucket.

        Example: ``arn:aws:s3express: *us-west-2* : *account_id* :bucket/ *DOC-EXAMPLE-BUCKET* -- *usw2-az1* --x-s3``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="dataRedundancy")
    def data_redundancy(self) -> builtins.str:
        '''The number of Availability Zone that's used for redundancy for the bucket.'''
        return typing.cast(builtins.str, jsii.get(self, "dataRedundancy"))

    @data_redundancy.setter
    def data_redundancy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9234d8f5c9448b0bb44f48a13430731436331b4ef073722b1511600f9484ff5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataRedundancy", value)

    @builtins.property
    @jsii.member(jsii_name="locationName")
    def location_name(self) -> builtins.str:
        '''The name of the location where the bucket will be created.'''
        return typing.cast(builtins.str, jsii.get(self, "locationName"))

    @location_name.setter
    def location_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__352b4b43cbbf4d81310eac7a66fd236d34a92a5af6e8099d48e6ec1e7c90c7a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locationName", value)

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''A name for the bucket.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__678dc679eb1daf10bbced208f7ef85b8fe01f1ae8ea62c5354ac80b289edc1ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_s3express.CfnDirectoryBucketProps",
    jsii_struct_bases=[],
    name_mapping={
        "data_redundancy": "dataRedundancy",
        "location_name": "locationName",
        "bucket_name": "bucketName",
    },
)
class CfnDirectoryBucketProps:
    def __init__(
        self,
        *,
        data_redundancy: builtins.str,
        location_name: builtins.str,
        bucket_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnDirectoryBucket``.

        :param data_redundancy: The number of Availability Zone that's used for redundancy for the bucket.
        :param location_name: The name of the location where the bucket will be created. For directory buckets, the name of the location is the AZ ID of the Availability Zone where the bucket will be created. An example AZ ID value is ``usw2-az1`` .
        :param bucket_name: A name for the bucket. The bucket name must contain only lowercase letters, numbers, and hyphens (-). A directory bucket name must be unique in the chosen Availability Zone. The bucket name must also follow the format ``*bucket_base_name* -- *az_id* --x-s3`` (for example, ``*DOC-EXAMPLE-BUCKET* -- *usw2-az1* --x-s3`` ). If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the bucket name. For information about bucket naming restrictions, see `Directory bucket naming rules <https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html>`_ in the *Amazon S3 User Guide* . .. epigraph:: If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you need to replace the resource, specify a new name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3express-directorybucket.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_s3express as s3express
            
            cfn_directory_bucket_props = s3express.CfnDirectoryBucketProps(
                data_redundancy="dataRedundancy",
                location_name="locationName",
            
                # the properties below are optional
                bucket_name="bucketName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__997b2abc28c849393aef2f13f43682b271277998e07114f1b224078949985e6e)
            check_type(argname="argument data_redundancy", value=data_redundancy, expected_type=type_hints["data_redundancy"])
            check_type(argname="argument location_name", value=location_name, expected_type=type_hints["location_name"])
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_redundancy": data_redundancy,
            "location_name": location_name,
        }
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name

    @builtins.property
    def data_redundancy(self) -> builtins.str:
        '''The number of Availability Zone that's used for redundancy for the bucket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3express-directorybucket.html#cfn-s3express-directorybucket-dataredundancy
        '''
        result = self._values.get("data_redundancy")
        assert result is not None, "Required property 'data_redundancy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location_name(self) -> builtins.str:
        '''The name of the location where the bucket will be created.

        For directory buckets, the name of the location is the AZ ID of the Availability Zone where the bucket will be created. An example AZ ID value is ``usw2-az1`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3express-directorybucket.html#cfn-s3express-directorybucket-locationname
        '''
        result = self._values.get("location_name")
        assert result is not None, "Required property 'location_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''A name for the bucket.

        The bucket name must contain only lowercase letters, numbers, and hyphens (-). A directory bucket name must be unique in the chosen Availability Zone. The bucket name must also follow the format ``*bucket_base_name* -- *az_id* --x-s3`` (for example, ``*DOC-EXAMPLE-BUCKET* -- *usw2-az1* --x-s3`` ). If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the bucket name. For information about bucket naming restrictions, see `Directory bucket naming rules <https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html>`_ in the *Amazon S3 User Guide* .
        .. epigraph::

           If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you need to replace the resource, specify a new name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3express-directorybucket.html#cfn-s3express-directorybucket-bucketname
        '''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDirectoryBucketProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnBucketPolicy",
    "CfnBucketPolicyProps",
    "CfnDirectoryBucket",
    "CfnDirectoryBucketProps",
]

publication.publish()

def _typecheckingstub__c7ae0c19fbf2c7c716bc3304458f2695912d196d3e7439999f721b69fdbfc5a0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    bucket: builtins.str,
    policy_document: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0da69b8aee8ed367e63ca61c9ad9c6ce2b5fd2aff3c02cb553118847c89867c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a427439734058e5e6251cd5c0aaeed7ade47e92954992912236d939d3b496350(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dedf6ffab37d96f5ca0d97fbcb6904b8dc185fd26912baba5f2b683aec30a5e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__575ca46990b1014411a210bab87827014d15a4bd9119ec2a06a134d0e642cfff(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7978963298afc97ec8564e6e114bf73c7797f21fb71f9d0a187dd5852499f423(
    *,
    bucket: builtins.str,
    policy_document: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea5a1e5897b0467fb93393ad6ea2dbcd3916f27713079e8bef3badf71ce2bb20(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    data_redundancy: builtins.str,
    location_name: builtins.str,
    bucket_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61d4c01a14f34a0546048356b166c111adde5de129e3d0580f9ce73d26da1587(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09d4f293955716375e6177306d2bdfa8106614896e901a12247190cc871e9e61(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9234d8f5c9448b0bb44f48a13430731436331b4ef073722b1511600f9484ff5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__352b4b43cbbf4d81310eac7a66fd236d34a92a5af6e8099d48e6ec1e7c90c7a5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__678dc679eb1daf10bbced208f7ef85b8fe01f1ae8ea62c5354ac80b289edc1ed(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__997b2abc28c849393aef2f13f43682b271277998e07114f1b224078949985e6e(
    *,
    data_redundancy: builtins.str,
    location_name: builtins.str,
    bucket_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
