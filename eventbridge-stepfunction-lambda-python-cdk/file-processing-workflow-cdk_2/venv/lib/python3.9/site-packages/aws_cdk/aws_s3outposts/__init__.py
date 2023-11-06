'''
# AWS::S3Outposts Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_s3outposts as s3outposts
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for S3Outposts construct libraries](https://constructs.dev/search?q=s3outposts)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::S3Outposts resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_S3Outposts.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::S3Outposts](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_S3Outposts.html).

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
class CfnAccessPoint(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3outposts.CfnAccessPoint",
):
    '''The AWS::S3Outposts::AccessPoint resource specifies an access point and associates it with the specified Amazon S3 on Outposts bucket.

    For more information, see `Managing data access with Amazon S3 access points <https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html>`_ .
    .. epigraph::

       S3 on Outposts supports only VPC-style access points.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_s3outposts as s3outposts
        
        # policy: Any
        
        cfn_access_point = s3outposts.CfnAccessPoint(self, "MyCfnAccessPoint",
            bucket="bucket",
            name="name",
            vpc_configuration=s3outposts.CfnAccessPoint.VpcConfigurationProperty(
                vpc_id="vpcId"
            ),
        
            # the properties below are optional
            policy=policy
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        bucket: builtins.str,
        name: builtins.str,
        vpc_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAccessPoint.VpcConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        policy: typing.Any = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param bucket: The Amazon Resource Name (ARN) of the S3 on Outposts bucket that is associated with this access point.
        :param name: The name of this access point.
        :param vpc_configuration: The virtual private cloud (VPC) configuration for this access point, if one exists.
        :param policy: The access point policy associated with this access point.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49ce0f4ffe62c399adc97a97059924fb12bb82ce4aee91b030e12a91c6e7e762)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAccessPointProps(
            bucket=bucket,
            name=name,
            vpc_configuration=vpc_configuration,
            policy=policy,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7779eb15d81bd813ec5d30e13c9aedb76154b61675e7d4bc65e58f9db6ddce79)
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
            type_hints = typing.get_type_hints(_typecheckingstub__28911394a383f22624188434089c8ff9d451f267f5c014153d42fa62157d9248)
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
        '''This resource contains the details of the S3 on Outposts bucket access point ARN.

        This resource is read-only.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the S3 on Outposts bucket that is associated with this access point.'''
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c65b8a25cb487d8c0393f3b844eb5ace314a436d88fbfdef93d5df1f215327ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of this access point.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8021398797d252dec5a923723349cc7067b5d1b7eb8e0583b457262fbdd7660a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="vpcConfiguration")
    def vpc_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnAccessPoint.VpcConfigurationProperty"]:
        '''The virtual private cloud (VPC) configuration for this access point, if one exists.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAccessPoint.VpcConfigurationProperty"], jsii.get(self, "vpcConfiguration"))

    @vpc_configuration.setter
    def vpc_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnAccessPoint.VpcConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55812ce12eee7d4ecd641b7985f48f98d2a1667857eae24a92f028f85a0a79a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> typing.Any:
        '''The access point policy associated with this access point.'''
        return typing.cast(typing.Any, jsii.get(self, "policy"))

    @policy.setter
    def policy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fe8d23b1da317c18e81dcb763cd502a86a78fbe1cf3b94eabdb297243d29f70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policy", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3outposts.CfnAccessPoint.VpcConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"vpc_id": "vpcId"},
    )
    class VpcConfigurationProperty:
        def __init__(self, *, vpc_id: typing.Optional[builtins.str] = None) -> None:
            '''Contains the virtual private cloud (VPC) configuration for the specified access point.

            :param vpc_id: The ID of the VPC configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-accesspoint-vpcconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3outposts as s3outposts
                
                vpc_configuration_property = s3outposts.CfnAccessPoint.VpcConfigurationProperty(
                    vpc_id="vpcId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6373f239cd33cf735848ce0486ac6581bfc5991eec9f4021c51d60abb6373929)
                check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if vpc_id is not None:
                self._values["vpc_id"] = vpc_id

        @builtins.property
        def vpc_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the VPC configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-accesspoint-vpcconfiguration.html#cfn-s3outposts-accesspoint-vpcconfiguration-vpcid
            '''
            result = self._values.get("vpc_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_s3outposts.CfnAccessPointProps",
    jsii_struct_bases=[],
    name_mapping={
        "bucket": "bucket",
        "name": "name",
        "vpc_configuration": "vpcConfiguration",
        "policy": "policy",
    },
)
class CfnAccessPointProps:
    def __init__(
        self,
        *,
        bucket: builtins.str,
        name: builtins.str,
        vpc_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAccessPoint.VpcConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
        policy: typing.Any = None,
    ) -> None:
        '''Properties for defining a ``CfnAccessPoint``.

        :param bucket: The Amazon Resource Name (ARN) of the S3 on Outposts bucket that is associated with this access point.
        :param name: The name of this access point.
        :param vpc_configuration: The virtual private cloud (VPC) configuration for this access point, if one exists.
        :param policy: The access point policy associated with this access point.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_s3outposts as s3outposts
            
            # policy: Any
            
            cfn_access_point_props = s3outposts.CfnAccessPointProps(
                bucket="bucket",
                name="name",
                vpc_configuration=s3outposts.CfnAccessPoint.VpcConfigurationProperty(
                    vpc_id="vpcId"
                ),
            
                # the properties below are optional
                policy=policy
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__502dc2c537076304a47cf0b8c88787bfe3b392befb36e1fd4e4308ab73f93f58)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument vpc_configuration", value=vpc_configuration, expected_type=type_hints["vpc_configuration"])
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket": bucket,
            "name": name,
            "vpc_configuration": vpc_configuration,
        }
        if policy is not None:
            self._values["policy"] = policy

    @builtins.property
    def bucket(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the S3 on Outposts bucket that is associated with this access point.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html#cfn-s3outposts-accesspoint-bucket
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of this access point.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html#cfn-s3outposts-accesspoint-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnAccessPoint.VpcConfigurationProperty]:
        '''The virtual private cloud (VPC) configuration for this access point, if one exists.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html#cfn-s3outposts-accesspoint-vpcconfiguration
        '''
        result = self._values.get("vpc_configuration")
        assert result is not None, "Required property 'vpc_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnAccessPoint.VpcConfigurationProperty], result)

    @builtins.property
    def policy(self) -> typing.Any:
        '''The access point policy associated with this access point.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html#cfn-s3outposts-accesspoint-policy
        '''
        result = self._values.get("policy")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAccessPointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnBucket(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3outposts.CfnBucket",
):
    '''The AWS::S3Outposts::Bucket resource specifies a new Amazon S3 on Outposts bucket.

    To create an S3 on Outposts bucket, you must have S3 on Outposts capacity provisioned on your Outpost. For more information, see `Using Amazon S3 on Outposts <https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html>`_ .

    S3 on Outposts buckets support the following:

    - Tags
    - Lifecycle configuration rules for deleting expired objects

    For a complete list of restrictions and Amazon S3 feature limitations on S3 on Outposts, see `Amazon S3 on Outposts Restrictions and Limitations <https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OnOutpostsRestrictionsLimitations.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_s3outposts as s3outposts
        
        # filter: Any
        
        cfn_bucket = s3outposts.CfnBucket(self, "MyCfnBucket",
            bucket_name="bucketName",
            outpost_id="outpostId",
        
            # the properties below are optional
            lifecycle_configuration=s3outposts.CfnBucket.LifecycleConfigurationProperty(
                rules=[s3outposts.CfnBucket.RuleProperty(
                    status="status",
        
                    # the properties below are optional
                    abort_incomplete_multipart_upload=s3outposts.CfnBucket.AbortIncompleteMultipartUploadProperty(
                        days_after_initiation=123
                    ),
                    expiration_date="expirationDate",
                    expiration_in_days=123,
                    filter=filter,
                    id="id"
                )]
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
        bucket_name: builtins.str,
        outpost_id: builtins.str,
        lifecycle_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBucket.LifecycleConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param bucket_name: A name for the S3 on Outposts bucket. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the bucket name. The bucket name must contain only lowercase letters, numbers, periods (.), and dashes (-) and must follow `Amazon S3 bucket restrictions and limitations <https://docs.aws.amazon.com/AmazonS3/latest/userguide/BucketRestrictions.html>`_ . For more information, see `Bucket naming rules <https://docs.aws.amazon.com/AmazonS3/latest/userguide/BucketRestrictions.html#bucketnamingrules>`_ . .. epigraph:: If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you need to replace the resource, specify a new name.
        :param outpost_id: The ID of the Outpost of the specified bucket.
        :param lifecycle_configuration: Creates a new lifecycle configuration for the S3 on Outposts bucket or replaces an existing lifecycle configuration. Outposts buckets only support lifecycle configurations that delete/expire objects after a certain period of time and abort incomplete multipart uploads.
        :param tags: Sets the tags for an S3 on Outposts bucket. For more information, see `Using Amazon S3 on Outposts <https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html>`_ . Use tags to organize your AWS bill to reflect your own cost structure. To do this, sign up to get your AWS account bill with tag key values included. Then, to see the cost of combined resources, organize your billing information according to resources with the same tag key values. For example, you can tag several resources with a specific application name, and then organize your billing information to see the total cost of that application across several services. For more information, see `Cost allocation and tags <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`_ . .. epigraph:: Within a bucket, if you add a tag that has the same key as an existing tag, the new value overwrites the old value. For more information, see `Using cost allocation and bucket tags <https://docs.aws.amazon.com/AmazonS3/latest/userguide/CostAllocTagging.html>`_ . To use this resource, you must have permissions to perform the ``s3-outposts:PutBucketTagging`` . The S3 on Outposts bucket owner has this permission by default and can grant this permission to others. For more information about permissions, see `Permissions Related to Bucket Subresource Operations <https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources>`_ and `Managing access permissions to your Amazon S3 resources <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf1d42fbcf6bb5a0f5e890280a2441a347ecd7dab8da3eb19e1350f3c14556a2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBucketProps(
            bucket_name=bucket_name,
            outpost_id=outpost_id,
            lifecycle_configuration=lifecycle_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f5478e773800c0e3a9e46e5359a04e609da7a57b57d4c20e3856f64524a0ecb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4ef9aa822f380ab4bf22a4f517a759bff0a4fb217dcc8cde43d48e5fcabfd009)
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
        '''Returns the ARN of the specified bucket.

        Example: ``arn:aws:s3Outposts:::DOC-EXAMPLE-BUCKET``

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
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        '''A name for the S3 on Outposts bucket.'''
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2180edde9d93d3019e5731108884add564fe77fabc6c08824e2245584b5b612a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="outpostId")
    def outpost_id(self) -> builtins.str:
        '''The ID of the Outpost of the specified bucket.'''
        return typing.cast(builtins.str, jsii.get(self, "outpostId"))

    @outpost_id.setter
    def outpost_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b304fffc77597e8560e34a222cb9354db0a5c85ba773db6493c92cf699f2bd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outpostId", value)

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfiguration")
    def lifecycle_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBucket.LifecycleConfigurationProperty"]]:
        '''Creates a new lifecycle configuration for the S3 on Outposts bucket or replaces an existing lifecycle configuration.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBucket.LifecycleConfigurationProperty"]], jsii.get(self, "lifecycleConfiguration"))

    @lifecycle_configuration.setter
    def lifecycle_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBucket.LifecycleConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1fafcae096376ac7aa48be114497eb8862c193af5a8157a978b9d9f1706bfb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Sets the tags for an S3 on Outposts bucket.

        For more information, see `Using Amazon S3 on Outposts <https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html>`_ .
        '''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81e8ae0c57b3dd52dd1453514c9b8759d4f840cef51f71bf06e13f51ba93590b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3outposts.CfnBucket.AbortIncompleteMultipartUploadProperty",
        jsii_struct_bases=[],
        name_mapping={"days_after_initiation": "daysAfterInitiation"},
    )
    class AbortIncompleteMultipartUploadProperty:
        def __init__(self, *, days_after_initiation: jsii.Number) -> None:
            '''Specifies the days since the initiation of an incomplete multipart upload that Amazon S3 on Outposts waits before permanently removing all parts of the upload.

            For more information, see `Aborting Incomplete Multipart Uploads Using a Bucket Lifecycle Policy <https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html#mpu-abort-incomplete-mpu-lifecycle-config>`_ .

            :param days_after_initiation: Specifies the number of days after initiation that Amazon S3 on Outposts aborts an incomplete multipart upload.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-abortincompletemultipartupload.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3outposts as s3outposts
                
                abort_incomplete_multipart_upload_property = s3outposts.CfnBucket.AbortIncompleteMultipartUploadProperty(
                    days_after_initiation=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__be2d2b572eeed3b97bba5f8b872acc83868b8f58781bb8d7901b64d7460b99a2)
                check_type(argname="argument days_after_initiation", value=days_after_initiation, expected_type=type_hints["days_after_initiation"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "days_after_initiation": days_after_initiation,
            }

        @builtins.property
        def days_after_initiation(self) -> jsii.Number:
            '''Specifies the number of days after initiation that Amazon S3 on Outposts aborts an incomplete multipart upload.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-abortincompletemultipartupload.html#cfn-s3outposts-bucket-abortincompletemultipartupload-daysafterinitiation
            '''
            result = self._values.get("days_after_initiation")
            assert result is not None, "Required property 'days_after_initiation' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AbortIncompleteMultipartUploadProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3outposts.CfnBucket.FilterAndOperatorProperty",
        jsii_struct_bases=[],
        name_mapping={"tags": "tags", "prefix": "prefix"},
    )
    class FilterAndOperatorProperty:
        def __init__(
            self,
            *,
            tags: typing.Sequence[typing.Union["CfnBucket.FilterTagProperty", typing.Dict[builtins.str, typing.Any]]],
            prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param tags: 
            :param prefix: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-filterandoperator.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3outposts as s3outposts
                
                filter_and_operator_property = s3outposts.CfnBucket.FilterAndOperatorProperty(
                    tags=[s3outposts.CfnBucket.FilterTagProperty(
                        key="key",
                        value="value"
                    )],
                
                    # the properties below are optional
                    prefix="prefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9d63ac5199ea9d78c5d66c09d78f4090bae2b2e111c754607530030f1c65df13)
                check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
                check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "tags": tags,
            }
            if prefix is not None:
                self._values["prefix"] = prefix

        @builtins.property
        def tags(self) -> typing.List["CfnBucket.FilterTagProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-filterandoperator.html#cfn-s3outposts-bucket-filterandoperator-tags
            '''
            result = self._values.get("tags")
            assert result is not None, "Required property 'tags' is missing"
            return typing.cast(typing.List["CfnBucket.FilterTagProperty"], result)

        @builtins.property
        def prefix(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-filterandoperator.html#cfn-s3outposts-bucket-filterandoperator-prefix
            '''
            result = self._values.get("prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FilterAndOperatorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3outposts.CfnBucket.FilterProperty",
        jsii_struct_bases=[],
        name_mapping={"and_operator": "andOperator", "prefix": "prefix", "tag": "tag"},
    )
    class FilterProperty:
        def __init__(
            self,
            *,
            and_operator: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBucket.FilterAndOperatorProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            prefix: typing.Optional[builtins.str] = None,
            tag: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBucket.FilterTagProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param and_operator: 
            :param prefix: 
            :param tag: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-filter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3outposts as s3outposts
                
                filter_property = s3outposts.CfnBucket.FilterProperty(
                    and_operator=s3outposts.CfnBucket.FilterAndOperatorProperty(
                        tags=[s3outposts.CfnBucket.FilterTagProperty(
                            key="key",
                            value="value"
                        )],
                
                        # the properties below are optional
                        prefix="prefix"
                    ),
                    prefix="prefix",
                    tag=s3outposts.CfnBucket.FilterTagProperty(
                        key="key",
                        value="value"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8e106be77cf3a2b5f0cbf1b0c943ba7fca0b1a44e38db2a47467eaae9801bfa1)
                check_type(argname="argument and_operator", value=and_operator, expected_type=type_hints["and_operator"])
                check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
                check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if and_operator is not None:
                self._values["and_operator"] = and_operator
            if prefix is not None:
                self._values["prefix"] = prefix
            if tag is not None:
                self._values["tag"] = tag

        @builtins.property
        def and_operator(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBucket.FilterAndOperatorProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-filter.html#cfn-s3outposts-bucket-filter-andoperator
            '''
            result = self._values.get("and_operator")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBucket.FilterAndOperatorProperty"]], result)

        @builtins.property
        def prefix(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-filter.html#cfn-s3outposts-bucket-filter-prefix
            '''
            result = self._values.get("prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tag(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBucket.FilterTagProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-filter.html#cfn-s3outposts-bucket-filter-tag
            '''
            result = self._values.get("tag")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBucket.FilterTagProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3outposts.CfnBucket.FilterTagProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class FilterTagProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''
            :param key: 
            :param value: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-filtertag.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3outposts as s3outposts
                
                filter_tag_property = s3outposts.CfnBucket.FilterTagProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__68451c3f1315d3fcdc640e3ffbcebfd32cdf69f88403a9045997e68b1969e031)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-filtertag.html#cfn-s3outposts-bucket-filtertag-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-filtertag.html#cfn-s3outposts-bucket-filtertag-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FilterTagProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3outposts.CfnBucket.LifecycleConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"rules": "rules"},
    )
    class LifecycleConfigurationProperty:
        def __init__(
            self,
            *,
            rules: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBucket.RuleProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''The container for the lifecycle configuration for the objects stored in an S3 on Outposts bucket.

            :param rules: The container for the lifecycle configuration rules for the objects stored in the S3 on Outposts bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-lifecycleconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3outposts as s3outposts
                
                # filter: Any
                
                lifecycle_configuration_property = s3outposts.CfnBucket.LifecycleConfigurationProperty(
                    rules=[s3outposts.CfnBucket.RuleProperty(
                        status="status",
                
                        # the properties below are optional
                        abort_incomplete_multipart_upload=s3outposts.CfnBucket.AbortIncompleteMultipartUploadProperty(
                            days_after_initiation=123
                        ),
                        expiration_date="expirationDate",
                        expiration_in_days=123,
                        filter=filter,
                        id="id"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ac9a6b7fa0d9b75b982f85c93773335ccad253ead21a004109aa36456f4e13dd)
                check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "rules": rules,
            }

        @builtins.property
        def rules(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBucket.RuleProperty"]]]:
            '''The container for the lifecycle configuration rules for the objects stored in the S3 on Outposts bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-lifecycleconfiguration.html#cfn-s3outposts-bucket-lifecycleconfiguration-rules
            '''
            result = self._values.get("rules")
            assert result is not None, "Required property 'rules' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBucket.RuleProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LifecycleConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3outposts.CfnBucket.RuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "status": "status",
            "abort_incomplete_multipart_upload": "abortIncompleteMultipartUpload",
            "expiration_date": "expirationDate",
            "expiration_in_days": "expirationInDays",
            "filter": "filter",
            "id": "id",
        },
    )
    class RuleProperty:
        def __init__(
            self,
            *,
            status: builtins.str,
            abort_incomplete_multipart_upload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBucket.AbortIncompleteMultipartUploadProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            expiration_date: typing.Optional[builtins.str] = None,
            expiration_in_days: typing.Optional[jsii.Number] = None,
            filter: typing.Any = None,
            id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A container for an Amazon S3 on Outposts bucket lifecycle rule.

            :param status: If ``Enabled`` , the rule is currently being applied. If ``Disabled`` , the rule is not currently being applied.
            :param abort_incomplete_multipart_upload: The container for the abort incomplete multipart upload rule.
            :param expiration_date: Specifies the expiration for the lifecycle of the object by specifying an expiry date.
            :param expiration_in_days: Specifies the expiration for the lifecycle of the object in the form of days that the object has been in the S3 on Outposts bucket.
            :param filter: The container for the filter of the lifecycle rule.
            :param id: The unique identifier for the lifecycle rule. The value can't be longer than 255 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3outposts as s3outposts
                
                # filter: Any
                
                rule_property = s3outposts.CfnBucket.RuleProperty(
                    status="status",
                
                    # the properties below are optional
                    abort_incomplete_multipart_upload=s3outposts.CfnBucket.AbortIncompleteMultipartUploadProperty(
                        days_after_initiation=123
                    ),
                    expiration_date="expirationDate",
                    expiration_in_days=123,
                    filter=filter,
                    id="id"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8e8643c47c6975c1b47c46b1e71cdfefd65aae1c18d477854613819b2c727449)
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
                check_type(argname="argument abort_incomplete_multipart_upload", value=abort_incomplete_multipart_upload, expected_type=type_hints["abort_incomplete_multipart_upload"])
                check_type(argname="argument expiration_date", value=expiration_date, expected_type=type_hints["expiration_date"])
                check_type(argname="argument expiration_in_days", value=expiration_in_days, expected_type=type_hints["expiration_in_days"])
                check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "status": status,
            }
            if abort_incomplete_multipart_upload is not None:
                self._values["abort_incomplete_multipart_upload"] = abort_incomplete_multipart_upload
            if expiration_date is not None:
                self._values["expiration_date"] = expiration_date
            if expiration_in_days is not None:
                self._values["expiration_in_days"] = expiration_in_days
            if filter is not None:
                self._values["filter"] = filter
            if id is not None:
                self._values["id"] = id

        @builtins.property
        def status(self) -> builtins.str:
            '''If ``Enabled`` , the rule is currently being applied.

            If ``Disabled`` , the rule is not currently being applied.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html#cfn-s3outposts-bucket-rule-status
            '''
            result = self._values.get("status")
            assert result is not None, "Required property 'status' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def abort_incomplete_multipart_upload(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBucket.AbortIncompleteMultipartUploadProperty"]]:
            '''The container for the abort incomplete multipart upload rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html#cfn-s3outposts-bucket-rule-abortincompletemultipartupload
            '''
            result = self._values.get("abort_incomplete_multipart_upload")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBucket.AbortIncompleteMultipartUploadProperty"]], result)

        @builtins.property
        def expiration_date(self) -> typing.Optional[builtins.str]:
            '''Specifies the expiration for the lifecycle of the object by specifying an expiry date.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html#cfn-s3outposts-bucket-rule-expirationdate
            '''
            result = self._values.get("expiration_date")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def expiration_in_days(self) -> typing.Optional[jsii.Number]:
            '''Specifies the expiration for the lifecycle of the object in the form of days that the object has been in the S3 on Outposts bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html#cfn-s3outposts-bucket-rule-expirationindays
            '''
            result = self._values.get("expiration_in_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def filter(self) -> typing.Any:
            '''The container for the filter of the lifecycle rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html#cfn-s3outposts-bucket-rule-filter
            '''
            result = self._values.get("filter")
            return typing.cast(typing.Any, result)

        @builtins.property
        def id(self) -> typing.Optional[builtins.str]:
            '''The unique identifier for the lifecycle rule.

            The value can't be longer than 255 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-bucket-rule.html#cfn-s3outposts-bucket-rule-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnBucketPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3outposts.CfnBucketPolicy",
):
    '''This resource applies a bucket policy to an Amazon S3 on Outposts bucket.

    If you are using an identity other than the root user of the AWS account that owns the S3 on Outposts bucket, the calling identity must have the ``s3-outposts:PutBucketPolicy`` permissions on the specified Outposts bucket and belong to the bucket owner's account in order to use this resource.

    If you don't have ``s3-outposts:PutBucketPolicy`` permissions, S3 on Outposts returns a ``403 Access Denied`` error.
    .. epigraph::

       The root user of the AWS account that owns an Outposts bucket can *always* use this resource, even if the policy explicitly denies the root user the ability to perform actions on this resource.

    For more information, see the AWS::IAM::Policy `PolicyDocument <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html#cfn-iam-policy-policydocument>`_ resource description in this guide and `Access Policy Language Overview <https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-policy-language-overview.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucketpolicy.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_s3outposts as s3outposts
        
        # policy_document: Any
        
        cfn_bucket_policy = s3outposts.CfnBucketPolicy(self, "MyCfnBucketPolicy",
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
        :param bucket: The name of the Amazon S3 Outposts bucket to which the policy applies.
        :param policy_document: A policy document containing permissions to add to the specified bucket. In IAM, you must provide policy documents in JSON format. However, in CloudFormation, you can provide the policy in JSON or YAML format because CloudFormation converts YAML to JSON before submitting it to IAM. For more information, see the AWS::IAM::Policy `PolicyDocument <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html#cfn-iam-policy-policydocument>`_ resource description in this guide and `Access Policy Language Overview <https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-policy-language-overview.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53f953365552955c7ee2d2061c15cae6076889714399ed780e2e277c3663cfe9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ea0a5820a06d21a28fd87edf9cc3f5f80428504e14b65cdba397b3c9780fbc1b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a70a5cdf2ee8b96e1e2e37831e42dec48d83624f09fd3dc3bdc53dc325dd7526)
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
        '''The name of the Amazon S3 Outposts bucket to which the policy applies.'''
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__741de84e481a14821974a14f1888b5702ab089b6519d500d09e7dbd551b1fd18)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4ffad2ccdd340afaf3b9f3e5724d20005a21c4915036ad7585f74447865c04cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyDocument", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_s3outposts.CfnBucketPolicyProps",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket", "policy_document": "policyDocument"},
)
class CfnBucketPolicyProps:
    def __init__(self, *, bucket: builtins.str, policy_document: typing.Any) -> None:
        '''Properties for defining a ``CfnBucketPolicy``.

        :param bucket: The name of the Amazon S3 Outposts bucket to which the policy applies.
        :param policy_document: A policy document containing permissions to add to the specified bucket. In IAM, you must provide policy documents in JSON format. However, in CloudFormation, you can provide the policy in JSON or YAML format because CloudFormation converts YAML to JSON before submitting it to IAM. For more information, see the AWS::IAM::Policy `PolicyDocument <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html#cfn-iam-policy-policydocument>`_ resource description in this guide and `Access Policy Language Overview <https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-policy-language-overview.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucketpolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_s3outposts as s3outposts
            
            # policy_document: Any
            
            cfn_bucket_policy_props = s3outposts.CfnBucketPolicyProps(
                bucket="bucket",
                policy_document=policy_document
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__464384deacb9b2f89cb8023b99378a89537e525526e6aed164958feab20ce13d)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument policy_document", value=policy_document, expected_type=type_hints["policy_document"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket": bucket,
            "policy_document": policy_document,
        }

    @builtins.property
    def bucket(self) -> builtins.str:
        '''The name of the Amazon S3 Outposts bucket to which the policy applies.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucketpolicy.html#cfn-s3outposts-bucketpolicy-bucket
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_document(self) -> typing.Any:
        '''A policy document containing permissions to add to the specified bucket.

        In IAM, you must provide policy documents in JSON format. However, in CloudFormation, you can provide the policy in JSON or YAML format because CloudFormation converts YAML to JSON before submitting it to IAM. For more information, see the AWS::IAM::Policy `PolicyDocument <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html#cfn-iam-policy-policydocument>`_ resource description in this guide and `Access Policy Language Overview <https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-policy-language-overview.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucketpolicy.html#cfn-s3outposts-bucketpolicy-policydocument
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


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_s3outposts.CfnBucketProps",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "outpost_id": "outpostId",
        "lifecycle_configuration": "lifecycleConfiguration",
        "tags": "tags",
    },
)
class CfnBucketProps:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        outpost_id: builtins.str,
        lifecycle_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBucket.LifecycleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnBucket``.

        :param bucket_name: A name for the S3 on Outposts bucket. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the bucket name. The bucket name must contain only lowercase letters, numbers, periods (.), and dashes (-) and must follow `Amazon S3 bucket restrictions and limitations <https://docs.aws.amazon.com/AmazonS3/latest/userguide/BucketRestrictions.html>`_ . For more information, see `Bucket naming rules <https://docs.aws.amazon.com/AmazonS3/latest/userguide/BucketRestrictions.html#bucketnamingrules>`_ . .. epigraph:: If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you need to replace the resource, specify a new name.
        :param outpost_id: The ID of the Outpost of the specified bucket.
        :param lifecycle_configuration: Creates a new lifecycle configuration for the S3 on Outposts bucket or replaces an existing lifecycle configuration. Outposts buckets only support lifecycle configurations that delete/expire objects after a certain period of time and abort incomplete multipart uploads.
        :param tags: Sets the tags for an S3 on Outposts bucket. For more information, see `Using Amazon S3 on Outposts <https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html>`_ . Use tags to organize your AWS bill to reflect your own cost structure. To do this, sign up to get your AWS account bill with tag key values included. Then, to see the cost of combined resources, organize your billing information according to resources with the same tag key values. For example, you can tag several resources with a specific application name, and then organize your billing information to see the total cost of that application across several services. For more information, see `Cost allocation and tags <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`_ . .. epigraph:: Within a bucket, if you add a tag that has the same key as an existing tag, the new value overwrites the old value. For more information, see `Using cost allocation and bucket tags <https://docs.aws.amazon.com/AmazonS3/latest/userguide/CostAllocTagging.html>`_ . To use this resource, you must have permissions to perform the ``s3-outposts:PutBucketTagging`` . The S3 on Outposts bucket owner has this permission by default and can grant this permission to others. For more information about permissions, see `Permissions Related to Bucket Subresource Operations <https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources>`_ and `Managing access permissions to your Amazon S3 resources <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_s3outposts as s3outposts
            
            # filter: Any
            
            cfn_bucket_props = s3outposts.CfnBucketProps(
                bucket_name="bucketName",
                outpost_id="outpostId",
            
                # the properties below are optional
                lifecycle_configuration=s3outposts.CfnBucket.LifecycleConfigurationProperty(
                    rules=[s3outposts.CfnBucket.RuleProperty(
                        status="status",
            
                        # the properties below are optional
                        abort_incomplete_multipart_upload=s3outposts.CfnBucket.AbortIncompleteMultipartUploadProperty(
                            days_after_initiation=123
                        ),
                        expiration_date="expirationDate",
                        expiration_in_days=123,
                        filter=filter,
                        id="id"
                    )]
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__683fc987670f90a28e1010c8937c6cb1351f51f7df54c1c1514e859e524938d7)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument outpost_id", value=outpost_id, expected_type=type_hints["outpost_id"])
            check_type(argname="argument lifecycle_configuration", value=lifecycle_configuration, expected_type=type_hints["lifecycle_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_name": bucket_name,
            "outpost_id": outpost_id,
        }
        if lifecycle_configuration is not None:
            self._values["lifecycle_configuration"] = lifecycle_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''A name for the S3 on Outposts bucket.

        If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the bucket name. The bucket name must contain only lowercase letters, numbers, periods (.), and dashes (-) and must follow `Amazon S3 bucket restrictions and limitations <https://docs.aws.amazon.com/AmazonS3/latest/userguide/BucketRestrictions.html>`_ . For more information, see `Bucket naming rules <https://docs.aws.amazon.com/AmazonS3/latest/userguide/BucketRestrictions.html#bucketnamingrules>`_ .
        .. epigraph::

           If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you need to replace the resource, specify a new name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html#cfn-s3outposts-bucket-bucketname
        '''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def outpost_id(self) -> builtins.str:
        '''The ID of the Outpost of the specified bucket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html#cfn-s3outposts-bucket-outpostid
        '''
        result = self._values.get("outpost_id")
        assert result is not None, "Required property 'outpost_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lifecycle_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBucket.LifecycleConfigurationProperty]]:
        '''Creates a new lifecycle configuration for the S3 on Outposts bucket or replaces an existing lifecycle configuration.

        Outposts buckets only support lifecycle configurations that delete/expire objects after a certain period of time and abort incomplete multipart uploads.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html#cfn-s3outposts-bucket-lifecycleconfiguration
        '''
        result = self._values.get("lifecycle_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBucket.LifecycleConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Sets the tags for an S3 on Outposts bucket. For more information, see `Using Amazon S3 on Outposts <https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html>`_ .

        Use tags to organize your AWS bill to reflect your own cost structure. To do this, sign up to get your AWS account bill with tag key values included. Then, to see the cost of combined resources, organize your billing information according to resources with the same tag key values. For example, you can tag several resources with a specific application name, and then organize your billing information to see the total cost of that application across several services. For more information, see `Cost allocation and tags <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`_ .
        .. epigraph::

           Within a bucket, if you add a tag that has the same key as an existing tag, the new value overwrites the old value. For more information, see `Using cost allocation and bucket tags <https://docs.aws.amazon.com/AmazonS3/latest/userguide/CostAllocTagging.html>`_ .

        To use this resource, you must have permissions to perform the ``s3-outposts:PutBucketTagging`` . The S3 on Outposts bucket owner has this permission by default and can grant this permission to others. For more information about permissions, see `Permissions Related to Bucket Subresource Operations <https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources>`_ and `Managing access permissions to your Amazon S3 resources <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html#cfn-s3outposts-bucket-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBucketProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnEndpoint(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3outposts.CfnEndpoint",
):
    '''This AWS::S3Outposts::Endpoint resource specifies an endpoint and associates it with the specified Outpost.

    Amazon S3 on Outposts access points simplify managing data access at scale for shared datasets in S3 on Outposts. S3 on Outposts uses endpoints to connect to S3 on Outposts buckets so that you can perform actions within your virtual private cloud (VPC). For more information, see `Accessing S3 on Outposts using VPC-only access points <https://docs.aws.amazon.com/AmazonS3/latest/userguide/AccessingS3Outposts.html>`_ .
    .. epigraph::

       It can take up to 5 minutes for this resource to be created.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_s3outposts as s3outposts
        
        cfn_endpoint = s3outposts.CfnEndpoint(self, "MyCfnEndpoint",
            outpost_id="outpostId",
            security_group_id="securityGroupId",
            subnet_id="subnetId",
        
            # the properties below are optional
            access_type="accessType",
            customer_owned_ipv4_pool="customerOwnedIpv4Pool",
            failed_reason=s3outposts.CfnEndpoint.FailedReasonProperty(
                error_code="errorCode",
                message="message"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        outpost_id: builtins.str,
        security_group_id: builtins.str,
        subnet_id: builtins.str,
        access_type: typing.Optional[builtins.str] = None,
        customer_owned_ipv4_pool: typing.Optional[builtins.str] = None,
        failed_reason: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEndpoint.FailedReasonProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param outpost_id: The ID of the Outpost.
        :param security_group_id: The ID of the security group to use with the endpoint.
        :param subnet_id: The ID of the subnet.
        :param access_type: The container for the type of connectivity used to access the Amazon S3 on Outposts endpoint. To use the Amazon VPC , choose ``Private`` . To use the endpoint with an on-premises network, choose ``CustomerOwnedIp`` . If you choose ``CustomerOwnedIp`` , you must also provide the customer-owned IP address pool (CoIP pool). .. epigraph:: ``Private`` is the default access type value. Default: - "Private"
        :param customer_owned_ipv4_pool: The ID of the customer-owned IPv4 address pool (CoIP pool) for the endpoint. IP addresses are allocated from this pool for the endpoint.
        :param failed_reason: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__318ea1d78b8b7ecc9087263403bda92a5fe62c88a967ba59a389878a95c540d2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEndpointProps(
            outpost_id=outpost_id,
            security_group_id=security_group_id,
            subnet_id=subnet_id,
            access_type=access_type,
            customer_owned_ipv4_pool=customer_owned_ipv4_pool,
            failed_reason=failed_reason,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f72a7b32f829abc1ef9826f937cda6c873bf4629a0eaf0dbce234c5845a4dda0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b1ab340ba912f823e4a6a3fecca7139c7e2bd8d531e573d054720e9695642007)
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
        '''The ARN of the endpoint.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCidrBlock")
    def attr_cidr_block(self) -> builtins.str:
        '''The VPC CIDR block committed by this endpoint.

        :cloudformationAttribute: CidrBlock
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCidrBlock"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''The time the endpoint was created.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the endpoint.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrNetworkInterfaces")
    def attr_network_interfaces(self) -> _IResolvable_da3f097b:
        '''The network interface of the endpoint.

        :cloudformationAttribute: NetworkInterfaces
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrNetworkInterfaces"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the endpoint.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="outpostId")
    def outpost_id(self) -> builtins.str:
        '''The ID of the Outpost.'''
        return typing.cast(builtins.str, jsii.get(self, "outpostId"))

    @outpost_id.setter
    def outpost_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f64fbe05fc52db7518c2b49b2447a29f7d6c035a079f160283b3ec578f126945)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outpostId", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroupId")
    def security_group_id(self) -> builtins.str:
        '''The ID of the security group to use with the endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "securityGroupId"))

    @security_group_id.setter
    def security_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ada6e5ad611d687272c2ae24ee27f4f10ad9a6551af1400b1cfb36a0878d83c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        '''The ID of the subnet.'''
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a4fe87732bb7c9003a3e91c651a931b7cb2ed9f09a1d503b246f519b4bb174a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="accessType")
    def access_type(self) -> typing.Optional[builtins.str]:
        '''The container for the type of connectivity used to access the Amazon S3 on Outposts endpoint.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessType"))

    @access_type.setter
    def access_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a46c368db5f4fea107997ef85bff0897aa39b9179933dfb8326a94c11501854)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessType", value)

    @builtins.property
    @jsii.member(jsii_name="customerOwnedIpv4Pool")
    def customer_owned_ipv4_pool(self) -> typing.Optional[builtins.str]:
        '''The ID of the customer-owned IPv4 address pool (CoIP pool) for the endpoint.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customerOwnedIpv4Pool"))

    @customer_owned_ipv4_pool.setter
    def customer_owned_ipv4_pool(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a04835a28042c16dff78d6ee722ced2b173f1d3db1db6c32099847ebb0ed3bc4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customerOwnedIpv4Pool", value)

    @builtins.property
    @jsii.member(jsii_name="failedReason")
    def failed_reason(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.FailedReasonProperty"]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.FailedReasonProperty"]], jsii.get(self, "failedReason"))

    @failed_reason.setter
    def failed_reason(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.FailedReasonProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f52e5e14ec2f40630ed72fb53578bc8a6cbe6c59dcbb031096376848ff1acad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failedReason", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3outposts.CfnEndpoint.FailedReasonProperty",
        jsii_struct_bases=[],
        name_mapping={"error_code": "errorCode", "message": "message"},
    )
    class FailedReasonProperty:
        def __init__(
            self,
            *,
            error_code: typing.Optional[builtins.str] = None,
            message: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param error_code: The failure code, if any, for a create or delete endpoint operation.
            :param message: Additional error details describing the endpoint failure and recommended action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-endpoint-failedreason.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3outposts as s3outposts
                
                failed_reason_property = s3outposts.CfnEndpoint.FailedReasonProperty(
                    error_code="errorCode",
                    message="message"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cefcf0227ba3f5441cbda4abb28ee44e8ed7a6036bee1479dcf2b9bcb6dc3081)
                check_type(argname="argument error_code", value=error_code, expected_type=type_hints["error_code"])
                check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if error_code is not None:
                self._values["error_code"] = error_code
            if message is not None:
                self._values["message"] = message

        @builtins.property
        def error_code(self) -> typing.Optional[builtins.str]:
            '''The failure code, if any, for a create or delete endpoint operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-endpoint-failedreason.html#cfn-s3outposts-endpoint-failedreason-errorcode
            '''
            result = self._values.get("error_code")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def message(self) -> typing.Optional[builtins.str]:
            '''Additional error details describing the endpoint failure and recommended action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-endpoint-failedreason.html#cfn-s3outposts-endpoint-failedreason-message
            '''
            result = self._values.get("message")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FailedReasonProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3outposts.CfnEndpoint.NetworkInterfaceProperty",
        jsii_struct_bases=[],
        name_mapping={"network_interface_id": "networkInterfaceId"},
    )
    class NetworkInterfaceProperty:
        def __init__(self, *, network_interface_id: builtins.str) -> None:
            '''The container for the network interface.

            :param network_interface_id: The ID for the network interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-endpoint-networkinterface.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3outposts as s3outposts
                
                network_interface_property = s3outposts.CfnEndpoint.NetworkInterfaceProperty(
                    network_interface_id="networkInterfaceId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__716f324c013a03cb5114197c4289096c6cfb4b86efb957ed96da99423bb4e82a)
                check_type(argname="argument network_interface_id", value=network_interface_id, expected_type=type_hints["network_interface_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "network_interface_id": network_interface_id,
            }

        @builtins.property
        def network_interface_id(self) -> builtins.str:
            '''The ID for the network interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3outposts-endpoint-networkinterface.html#cfn-s3outposts-endpoint-networkinterface-networkinterfaceid
            '''
            result = self._values.get("network_interface_id")
            assert result is not None, "Required property 'network_interface_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkInterfaceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_s3outposts.CfnEndpointProps",
    jsii_struct_bases=[],
    name_mapping={
        "outpost_id": "outpostId",
        "security_group_id": "securityGroupId",
        "subnet_id": "subnetId",
        "access_type": "accessType",
        "customer_owned_ipv4_pool": "customerOwnedIpv4Pool",
        "failed_reason": "failedReason",
    },
)
class CfnEndpointProps:
    def __init__(
        self,
        *,
        outpost_id: builtins.str,
        security_group_id: builtins.str,
        subnet_id: builtins.str,
        access_type: typing.Optional[builtins.str] = None,
        customer_owned_ipv4_pool: typing.Optional[builtins.str] = None,
        failed_reason: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.FailedReasonProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEndpoint``.

        :param outpost_id: The ID of the Outpost.
        :param security_group_id: The ID of the security group to use with the endpoint.
        :param subnet_id: The ID of the subnet.
        :param access_type: The container for the type of connectivity used to access the Amazon S3 on Outposts endpoint. To use the Amazon VPC , choose ``Private`` . To use the endpoint with an on-premises network, choose ``CustomerOwnedIp`` . If you choose ``CustomerOwnedIp`` , you must also provide the customer-owned IP address pool (CoIP pool). .. epigraph:: ``Private`` is the default access type value. Default: - "Private"
        :param customer_owned_ipv4_pool: The ID of the customer-owned IPv4 address pool (CoIP pool) for the endpoint. IP addresses are allocated from this pool for the endpoint.
        :param failed_reason: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_s3outposts as s3outposts
            
            cfn_endpoint_props = s3outposts.CfnEndpointProps(
                outpost_id="outpostId",
                security_group_id="securityGroupId",
                subnet_id="subnetId",
            
                # the properties below are optional
                access_type="accessType",
                customer_owned_ipv4_pool="customerOwnedIpv4Pool",
                failed_reason=s3outposts.CfnEndpoint.FailedReasonProperty(
                    error_code="errorCode",
                    message="message"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e86072181b15ea735510a9a25cc41f7969d6075b4e3a14868638c9fbbe0cdd56)
            check_type(argname="argument outpost_id", value=outpost_id, expected_type=type_hints["outpost_id"])
            check_type(argname="argument security_group_id", value=security_group_id, expected_type=type_hints["security_group_id"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            check_type(argname="argument access_type", value=access_type, expected_type=type_hints["access_type"])
            check_type(argname="argument customer_owned_ipv4_pool", value=customer_owned_ipv4_pool, expected_type=type_hints["customer_owned_ipv4_pool"])
            check_type(argname="argument failed_reason", value=failed_reason, expected_type=type_hints["failed_reason"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "outpost_id": outpost_id,
            "security_group_id": security_group_id,
            "subnet_id": subnet_id,
        }
        if access_type is not None:
            self._values["access_type"] = access_type
        if customer_owned_ipv4_pool is not None:
            self._values["customer_owned_ipv4_pool"] = customer_owned_ipv4_pool
        if failed_reason is not None:
            self._values["failed_reason"] = failed_reason

    @builtins.property
    def outpost_id(self) -> builtins.str:
        '''The ID of the Outpost.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#cfn-s3outposts-endpoint-outpostid
        '''
        result = self._values.get("outpost_id")
        assert result is not None, "Required property 'outpost_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_group_id(self) -> builtins.str:
        '''The ID of the security group to use with the endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#cfn-s3outposts-endpoint-securitygroupid
        '''
        result = self._values.get("security_group_id")
        assert result is not None, "Required property 'security_group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_id(self) -> builtins.str:
        '''The ID of the subnet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#cfn-s3outposts-endpoint-subnetid
        '''
        result = self._values.get("subnet_id")
        assert result is not None, "Required property 'subnet_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_type(self) -> typing.Optional[builtins.str]:
        '''The container for the type of connectivity used to access the Amazon S3 on Outposts endpoint.

        To use the Amazon VPC , choose ``Private`` . To use the endpoint with an on-premises network, choose ``CustomerOwnedIp`` . If you choose ``CustomerOwnedIp`` , you must also provide the customer-owned IP address pool (CoIP pool).
        .. epigraph::

           ``Private`` is the default access type value.

        :default: - "Private"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#cfn-s3outposts-endpoint-accesstype
        '''
        result = self._values.get("access_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def customer_owned_ipv4_pool(self) -> typing.Optional[builtins.str]:
        '''The ID of the customer-owned IPv4 address pool (CoIP pool) for the endpoint.

        IP addresses are allocated from this pool for the endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#cfn-s3outposts-endpoint-customerownedipv4pool
        '''
        result = self._values.get("customer_owned_ipv4_pool")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def failed_reason(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.FailedReasonProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-endpoint.html#cfn-s3outposts-endpoint-failedreason
        '''
        result = self._values.get("failed_reason")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.FailedReasonProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEndpointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAccessPoint",
    "CfnAccessPointProps",
    "CfnBucket",
    "CfnBucketPolicy",
    "CfnBucketPolicyProps",
    "CfnBucketProps",
    "CfnEndpoint",
    "CfnEndpointProps",
]

publication.publish()

def _typecheckingstub__49ce0f4ffe62c399adc97a97059924fb12bb82ce4aee91b030e12a91c6e7e762(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    bucket: builtins.str,
    name: builtins.str,
    vpc_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAccessPoint.VpcConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    policy: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7779eb15d81bd813ec5d30e13c9aedb76154b61675e7d4bc65e58f9db6ddce79(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28911394a383f22624188434089c8ff9d451f267f5c014153d42fa62157d9248(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c65b8a25cb487d8c0393f3b844eb5ace314a436d88fbfdef93d5df1f215327ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8021398797d252dec5a923723349cc7067b5d1b7eb8e0583b457262fbdd7660a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55812ce12eee7d4ecd641b7985f48f98d2a1667857eae24a92f028f85a0a79a8(
    value: typing.Union[_IResolvable_da3f097b, CfnAccessPoint.VpcConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fe8d23b1da317c18e81dcb763cd502a86a78fbe1cf3b94eabdb297243d29f70(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6373f239cd33cf735848ce0486ac6581bfc5991eec9f4021c51d60abb6373929(
    *,
    vpc_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__502dc2c537076304a47cf0b8c88787bfe3b392befb36e1fd4e4308ab73f93f58(
    *,
    bucket: builtins.str,
    name: builtins.str,
    vpc_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAccessPoint.VpcConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    policy: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf1d42fbcf6bb5a0f5e890280a2441a347ecd7dab8da3eb19e1350f3c14556a2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    bucket_name: builtins.str,
    outpost_id: builtins.str,
    lifecycle_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBucket.LifecycleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f5478e773800c0e3a9e46e5359a04e609da7a57b57d4c20e3856f64524a0ecb(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ef9aa822f380ab4bf22a4f517a759bff0a4fb217dcc8cde43d48e5fcabfd009(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2180edde9d93d3019e5731108884add564fe77fabc6c08824e2245584b5b612a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b304fffc77597e8560e34a222cb9354db0a5c85ba773db6493c92cf699f2bd6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1fafcae096376ac7aa48be114497eb8862c193af5a8157a978b9d9f1706bfb8(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBucket.LifecycleConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81e8ae0c57b3dd52dd1453514c9b8759d4f840cef51f71bf06e13f51ba93590b(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be2d2b572eeed3b97bba5f8b872acc83868b8f58781bb8d7901b64d7460b99a2(
    *,
    days_after_initiation: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d63ac5199ea9d78c5d66c09d78f4090bae2b2e111c754607530030f1c65df13(
    *,
    tags: typing.Sequence[typing.Union[CfnBucket.FilterTagProperty, typing.Dict[builtins.str, typing.Any]]],
    prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e106be77cf3a2b5f0cbf1b0c943ba7fca0b1a44e38db2a47467eaae9801bfa1(
    *,
    and_operator: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBucket.FilterAndOperatorProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    prefix: typing.Optional[builtins.str] = None,
    tag: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBucket.FilterTagProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68451c3f1315d3fcdc640e3ffbcebfd32cdf69f88403a9045997e68b1969e031(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac9a6b7fa0d9b75b982f85c93773335ccad253ead21a004109aa36456f4e13dd(
    *,
    rules: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBucket.RuleProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e8643c47c6975c1b47c46b1e71cdfefd65aae1c18d477854613819b2c727449(
    *,
    status: builtins.str,
    abort_incomplete_multipart_upload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBucket.AbortIncompleteMultipartUploadProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    expiration_date: typing.Optional[builtins.str] = None,
    expiration_in_days: typing.Optional[jsii.Number] = None,
    filter: typing.Any = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53f953365552955c7ee2d2061c15cae6076889714399ed780e2e277c3663cfe9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    bucket: builtins.str,
    policy_document: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea0a5820a06d21a28fd87edf9cc3f5f80428504e14b65cdba397b3c9780fbc1b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a70a5cdf2ee8b96e1e2e37831e42dec48d83624f09fd3dc3bdc53dc325dd7526(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__741de84e481a14821974a14f1888b5702ab089b6519d500d09e7dbd551b1fd18(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ffad2ccdd340afaf3b9f3e5724d20005a21c4915036ad7585f74447865c04cf(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__464384deacb9b2f89cb8023b99378a89537e525526e6aed164958feab20ce13d(
    *,
    bucket: builtins.str,
    policy_document: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__683fc987670f90a28e1010c8937c6cb1351f51f7df54c1c1514e859e524938d7(
    *,
    bucket_name: builtins.str,
    outpost_id: builtins.str,
    lifecycle_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBucket.LifecycleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__318ea1d78b8b7ecc9087263403bda92a5fe62c88a967ba59a389878a95c540d2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    outpost_id: builtins.str,
    security_group_id: builtins.str,
    subnet_id: builtins.str,
    access_type: typing.Optional[builtins.str] = None,
    customer_owned_ipv4_pool: typing.Optional[builtins.str] = None,
    failed_reason: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.FailedReasonProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f72a7b32f829abc1ef9826f937cda6c873bf4629a0eaf0dbce234c5845a4dda0(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1ab340ba912f823e4a6a3fecca7139c7e2bd8d531e573d054720e9695642007(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f64fbe05fc52db7518c2b49b2447a29f7d6c035a079f160283b3ec578f126945(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ada6e5ad611d687272c2ae24ee27f4f10ad9a6551af1400b1cfb36a0878d83c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a4fe87732bb7c9003a3e91c651a931b7cb2ed9f09a1d503b246f519b4bb174a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a46c368db5f4fea107997ef85bff0897aa39b9179933dfb8326a94c11501854(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a04835a28042c16dff78d6ee722ced2b173f1d3db1db6c32099847ebb0ed3bc4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f52e5e14ec2f40630ed72fb53578bc8a6cbe6c59dcbb031096376848ff1acad(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.FailedReasonProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cefcf0227ba3f5441cbda4abb28ee44e8ed7a6036bee1479dcf2b9bcb6dc3081(
    *,
    error_code: typing.Optional[builtins.str] = None,
    message: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__716f324c013a03cb5114197c4289096c6cfb4b86efb957ed96da99423bb4e82a(
    *,
    network_interface_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e86072181b15ea735510a9a25cc41f7969d6075b4e3a14868638c9fbbe0cdd56(
    *,
    outpost_id: builtins.str,
    security_group_id: builtins.str,
    subnet_id: builtins.str,
    access_type: typing.Optional[builtins.str] = None,
    customer_owned_ipv4_pool: typing.Optional[builtins.str] = None,
    failed_reason: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.FailedReasonProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
