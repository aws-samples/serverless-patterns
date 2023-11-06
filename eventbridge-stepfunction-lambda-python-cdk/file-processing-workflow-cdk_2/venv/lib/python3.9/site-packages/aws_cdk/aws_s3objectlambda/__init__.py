'''
# AWS::S3ObjectLambda Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_s3objectlambda as s3objectlambda
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for S3ObjectLambda construct libraries](https://constructs.dev/search?q=s3objectlambda)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::S3ObjectLambda resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_S3ObjectLambda.html) directly.

> An experimental construct library for this service is available in preview. Since it is not stable yet, it is distributed
> as a separate package so that you can pin its version independently of the rest of the CDK. See the package:
>
> <span class="package-reference">@aws-cdk/aws-s3objectlambda-alpha</span>

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::S3ObjectLambda](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_S3ObjectLambda.html).

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
class CfnAccessPoint(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3objectlambda.CfnAccessPoint",
):
    '''The ``AWS::S3ObjectLambda::AccessPoint`` resource specifies an Object Lambda Access Point used to access a bucket.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspoint.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_s3objectlambda as s3objectlambda
        
        # content_transformation: Any
        
        cfn_access_point = s3objectlambda.CfnAccessPoint(self, "MyCfnAccessPoint",
            object_lambda_configuration=s3objectlambda.CfnAccessPoint.ObjectLambdaConfigurationProperty(
                supporting_access_point="supportingAccessPoint",
                transformation_configurations=[s3objectlambda.CfnAccessPoint.TransformationConfigurationProperty(
                    actions=["actions"],
                    content_transformation=content_transformation
                )],
        
                # the properties below are optional
                allowed_features=["allowedFeatures"],
                cloud_watch_metrics_enabled=False
            ),
        
            # the properties below are optional
            name="name"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        object_lambda_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAccessPoint.ObjectLambdaConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param object_lambda_configuration: A configuration used when creating an Object Lambda Access Point.
        :param name: The name of this access point.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc24858ef1979ca1cb8fba3d4a06956342322b232c5594f16f11ee6c380ea43b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAccessPointProps(
            object_lambda_configuration=object_lambda_configuration, name=name
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de086f7124fab776ebe585a8278086a48c54ce0f9432344e7ead7888d183a2af)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f4bdd3b4c3dcd57f23413630ff374499bdd114af0eb3d609502c3ce8c4384c2f)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAlias")
    def attr_alias(self) -> _IResolvable_da3f097b:
        '''The alias of the Object Lambda Access Point.

        :cloudformationAttribute: Alias
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrAlias"))

    @builtins.property
    @jsii.member(jsii_name="attrAliasStatus")
    def attr_alias_status(self) -> builtins.str:
        '''The status of the Object Lambda Access Point alias.

        Valid Values: ``PROVISIONING`` | ``READY`` .

        :cloudformationAttribute: Alias.Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAliasStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrAliasValue")
    def attr_alias_value(self) -> builtins.str:
        '''The alias name value of the Object Lambda Access Point.

        For example: ``myolap-1a4n8yjrb3kda96f67zwrwiiuse1a--ol-s3`` .

        :cloudformationAttribute: Alias.Value
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAliasValue"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''Specifies the ARN for the Object Lambda Access Point.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationDate")
    def attr_creation_date(self) -> builtins.str:
        '''The date and time when the specified Object Lambda Access Point was created.

        :cloudformationAttribute: CreationDate
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationDate"))

    @builtins.property
    @jsii.member(jsii_name="attrPolicyStatus")
    def attr_policy_status(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: PolicyStatus
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrPolicyStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrPolicyStatusIsPublic")
    def attr_policy_status_is_public(self) -> _IResolvable_da3f097b:
        '''Specifies whether the Object lambda Access Point Policy is Public or not.

        Object lambda Access Points are private by default.

        :cloudformationAttribute: PolicyStatus.IsPublic
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrPolicyStatusIsPublic"))

    @builtins.property
    @jsii.member(jsii_name="attrPublicAccessBlockConfiguration")
    def attr_public_access_block_configuration(self) -> _IResolvable_da3f097b:
        '''The Public Access Block Configuration is used to block policies that would allow public access to this Object lambda Access Point.

        All public access to Object lambda Access Points are blocked by default, and any policy that would give public access to them will be also blocked. This behavior cannot be changed for Object lambda Access Points.

        :cloudformationAttribute: PublicAccessBlockConfiguration
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrPublicAccessBlockConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="attrPublicAccessBlockConfigurationBlockPublicAcls")
    def attr_public_access_block_configuration_block_public_acls(
        self,
    ) -> _IResolvable_da3f097b:
        '''Specifies whether Amazon S3 should block public access control lists (ACLs) to this object lambda access point.

        Setting this element to TRUE causes the following behavior:

        - PUT Bucket acl and PUT Object acl calls fail if the specified ACL is public.
        - PUT Object calls fail if the request includes a public ACL.
          . - PUT Bucket calls fail if the request includes a public ACL.
          Enabling this setting doesn't affect existing policies or ACLs.

        :cloudformationAttribute: PublicAccessBlockConfiguration.BlockPublicAcls
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrPublicAccessBlockConfigurationBlockPublicAcls"))

    @builtins.property
    @jsii.member(jsii_name="attrPublicAccessBlockConfigurationBlockPublicPolicy")
    def attr_public_access_block_configuration_block_public_policy(
        self,
    ) -> _IResolvable_da3f097b:
        '''Specifies whether Amazon S3 should block public bucket policies for buckets in this account.

        Setting this element to TRUE causes Amazon S3 to reject calls to PUT Bucket policy if the specified bucket policy allows public access. Enabling this setting doesn't affect existing bucket policies.

        :cloudformationAttribute: PublicAccessBlockConfiguration.BlockPublicPolicy
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrPublicAccessBlockConfigurationBlockPublicPolicy"))

    @builtins.property
    @jsii.member(jsii_name="attrPublicAccessBlockConfigurationIgnorePublicAcls")
    def attr_public_access_block_configuration_ignore_public_acls(
        self,
    ) -> _IResolvable_da3f097b:
        '''Specifies whether Amazon S3 should ignore public ACLs for buckets in this account.

        Setting this element to TRUE causes Amazon S3 to ignore all public ACLs on buckets in this account and any objects that they contain. Enabling this setting doesn't affect the persistence of any existing ACLs and doesn't prevent new public ACLs from being set.

        :cloudformationAttribute: PublicAccessBlockConfiguration.IgnorePublicAcls
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrPublicAccessBlockConfigurationIgnorePublicAcls"))

    @builtins.property
    @jsii.member(jsii_name="attrPublicAccessBlockConfigurationRestrictPublicBuckets")
    def attr_public_access_block_configuration_restrict_public_buckets(
        self,
    ) -> _IResolvable_da3f097b:
        '''Specifies whether Amazon S3 should restrict public bucket policies for this bucket.

        Setting this element to TRUE restricts access to this bucket to only AWS services and authorized users within this account if the bucket has a public policy.
        Enabling this setting doesn't affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked.

        :cloudformationAttribute: PublicAccessBlockConfiguration.RestrictPublicBuckets
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrPublicAccessBlockConfigurationRestrictPublicBuckets"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="objectLambdaConfiguration")
    def object_lambda_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnAccessPoint.ObjectLambdaConfigurationProperty"]:
        '''A configuration used when creating an Object Lambda Access Point.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAccessPoint.ObjectLambdaConfigurationProperty"], jsii.get(self, "objectLambdaConfiguration"))

    @object_lambda_configuration.setter
    def object_lambda_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnAccessPoint.ObjectLambdaConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72235765a4ddbec3dfa520018313ca825a0eee0d6620fbbc57d8d6942cd266e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectLambdaConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of this access point.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1ec3bbadc1fe6d1688dbe3361b2c99aaf74daa3cbcc3c9006d8c862eee8b9f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3objectlambda.CfnAccessPoint.AliasProperty",
        jsii_struct_bases=[],
        name_mapping={"status": "status", "value": "value"},
    )
    class AliasProperty:
        def __init__(self, *, status: builtins.str, value: builtins.str) -> None:
            '''The alias of an Object Lambda Access Point.

            For more information, see `How to use a bucket-style alias for your S3 bucket Object Lambda Access Point <https://docs.aws.amazon.com/AmazonS3/latest/userguide/olap-use.html#ol-access-points-alias>`_ .

            :param status: The status of the Object Lambda Access Point alias. If the status is ``PROVISIONING`` , the Object Lambda Access Point is provisioning the alias and the alias is not ready for use yet. If the status is ``READY`` , the Object Lambda Access Point alias is successfully provisioned and ready for use.
            :param value: The alias value of the Object Lambda Access Point.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-alias.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3objectlambda as s3objectlambda
                
                alias_property = s3objectlambda.CfnAccessPoint.AliasProperty(
                    status="status",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__057ad3aa353f20aafa8045ccead72b77f424a0108cc0869f56410bb930ad4959)
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "status": status,
                "value": value,
            }

        @builtins.property
        def status(self) -> builtins.str:
            '''The status of the Object Lambda Access Point alias.

            If the status is ``PROVISIONING`` , the Object Lambda Access Point is provisioning the alias and the alias is not ready for use yet. If the status is ``READY`` , the Object Lambda Access Point alias is successfully provisioned and ready for use.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-alias.html#cfn-s3objectlambda-accesspoint-alias-status
            '''
            result = self._values.get("status")
            assert result is not None, "Required property 'status' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The alias value of the Object Lambda Access Point.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-alias.html#cfn-s3objectlambda-accesspoint-alias-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AliasProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3objectlambda.CfnAccessPoint.AwsLambdaProperty",
        jsii_struct_bases=[],
        name_mapping={
            "function_arn": "functionArn",
            "function_payload": "functionPayload",
        },
    )
    class AwsLambdaProperty:
        def __init__(
            self,
            *,
            function_arn: builtins.str,
            function_payload: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param function_arn: 
            :param function_payload: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-awslambda.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3objectlambda as s3objectlambda
                
                aws_lambda_property = s3objectlambda.CfnAccessPoint.AwsLambdaProperty(
                    function_arn="functionArn",
                
                    # the properties below are optional
                    function_payload="functionPayload"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9ee3118c2b111c6807c152b3884192374a50ef95bf6b87dbf9a0a05bc33c38fd)
                check_type(argname="argument function_arn", value=function_arn, expected_type=type_hints["function_arn"])
                check_type(argname="argument function_payload", value=function_payload, expected_type=type_hints["function_payload"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "function_arn": function_arn,
            }
            if function_payload is not None:
                self._values["function_payload"] = function_payload

        @builtins.property
        def function_arn(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-awslambda.html#cfn-s3objectlambda-accesspoint-awslambda-functionarn
            '''
            result = self._values.get("function_arn")
            assert result is not None, "Required property 'function_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def function_payload(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-awslambda.html#cfn-s3objectlambda-accesspoint-awslambda-functionpayload
            '''
            result = self._values.get("function_payload")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AwsLambdaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3objectlambda.CfnAccessPoint.ContentTransformationProperty",
        jsii_struct_bases=[],
        name_mapping={"aws_lambda": "awsLambda"},
    )
    class ContentTransformationProperty:
        def __init__(
            self,
            *,
            aws_lambda: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAccessPoint.AwsLambdaProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''
            :param aws_lambda: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-contenttransformation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3objectlambda as s3objectlambda
                
                content_transformation_property = s3objectlambda.CfnAccessPoint.ContentTransformationProperty(
                    aws_lambda=s3objectlambda.CfnAccessPoint.AwsLambdaProperty(
                        function_arn="functionArn",
                
                        # the properties below are optional
                        function_payload="functionPayload"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f2a3c7654e406c9a13790e67d3850f1b300c2434f25e8d6a2a17d16cb8ddbcc0)
                check_type(argname="argument aws_lambda", value=aws_lambda, expected_type=type_hints["aws_lambda"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "aws_lambda": aws_lambda,
            }

        @builtins.property
        def aws_lambda(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnAccessPoint.AwsLambdaProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-contenttransformation.html#cfn-s3objectlambda-accesspoint-contenttransformation-awslambda
            '''
            result = self._values.get("aws_lambda")
            assert result is not None, "Required property 'aws_lambda' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAccessPoint.AwsLambdaProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContentTransformationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3objectlambda.CfnAccessPoint.ObjectLambdaConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "supporting_access_point": "supportingAccessPoint",
            "transformation_configurations": "transformationConfigurations",
            "allowed_features": "allowedFeatures",
            "cloud_watch_metrics_enabled": "cloudWatchMetricsEnabled",
        },
    )
    class ObjectLambdaConfigurationProperty:
        def __init__(
            self,
            *,
            supporting_access_point: builtins.str,
            transformation_configurations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAccessPoint.TransformationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]],
            allowed_features: typing.Optional[typing.Sequence[builtins.str]] = None,
            cloud_watch_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''A configuration used when creating an Object Lambda Access Point.

            :param supporting_access_point: Standard access point associated with the Object Lambda Access Point.
            :param transformation_configurations: A container for transformation configurations for an Object Lambda Access Point.
            :param allowed_features: A container for allowed features. Valid inputs are ``GetObject-Range`` , ``GetObject-PartNumber`` , ``HeadObject-Range`` , and ``HeadObject-PartNumber`` .
            :param cloud_watch_metrics_enabled: A container for whether the CloudWatch metrics configuration is enabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-objectlambdaconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3objectlambda as s3objectlambda
                
                # content_transformation: Any
                
                object_lambda_configuration_property = s3objectlambda.CfnAccessPoint.ObjectLambdaConfigurationProperty(
                    supporting_access_point="supportingAccessPoint",
                    transformation_configurations=[s3objectlambda.CfnAccessPoint.TransformationConfigurationProperty(
                        actions=["actions"],
                        content_transformation=content_transformation
                    )],
                
                    # the properties below are optional
                    allowed_features=["allowedFeatures"],
                    cloud_watch_metrics_enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d802fe046f5597b4cf6ab6c81e09859cbab4304022fbba60a7a7493d751a7537)
                check_type(argname="argument supporting_access_point", value=supporting_access_point, expected_type=type_hints["supporting_access_point"])
                check_type(argname="argument transformation_configurations", value=transformation_configurations, expected_type=type_hints["transformation_configurations"])
                check_type(argname="argument allowed_features", value=allowed_features, expected_type=type_hints["allowed_features"])
                check_type(argname="argument cloud_watch_metrics_enabled", value=cloud_watch_metrics_enabled, expected_type=type_hints["cloud_watch_metrics_enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "supporting_access_point": supporting_access_point,
                "transformation_configurations": transformation_configurations,
            }
            if allowed_features is not None:
                self._values["allowed_features"] = allowed_features
            if cloud_watch_metrics_enabled is not None:
                self._values["cloud_watch_metrics_enabled"] = cloud_watch_metrics_enabled

        @builtins.property
        def supporting_access_point(self) -> builtins.str:
            '''Standard access point associated with the Object Lambda Access Point.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-objectlambdaconfiguration.html#cfn-s3objectlambda-accesspoint-objectlambdaconfiguration-supportingaccesspoint
            '''
            result = self._values.get("supporting_access_point")
            assert result is not None, "Required property 'supporting_access_point' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def transformation_configurations(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAccessPoint.TransformationConfigurationProperty"]]]:
            '''A container for transformation configurations for an Object Lambda Access Point.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-objectlambdaconfiguration.html#cfn-s3objectlambda-accesspoint-objectlambdaconfiguration-transformationconfigurations
            '''
            result = self._values.get("transformation_configurations")
            assert result is not None, "Required property 'transformation_configurations' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAccessPoint.TransformationConfigurationProperty"]]], result)

        @builtins.property
        def allowed_features(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A container for allowed features.

            Valid inputs are ``GetObject-Range`` , ``GetObject-PartNumber`` , ``HeadObject-Range`` , and ``HeadObject-PartNumber`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-objectlambdaconfiguration.html#cfn-s3objectlambda-accesspoint-objectlambdaconfiguration-allowedfeatures
            '''
            result = self._values.get("allowed_features")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def cloud_watch_metrics_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A container for whether the CloudWatch metrics configuration is enabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-objectlambdaconfiguration.html#cfn-s3objectlambda-accesspoint-objectlambdaconfiguration-cloudwatchmetricsenabled
            '''
            result = self._values.get("cloud_watch_metrics_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ObjectLambdaConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3objectlambda.CfnAccessPoint.PolicyStatusProperty",
        jsii_struct_bases=[],
        name_mapping={"is_public": "isPublic"},
    )
    class PolicyStatusProperty:
        def __init__(
            self,
            *,
            is_public: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Indicates whether this access point policy is public.

            For more information about how Amazon S3 evaluates policies to determine whether they are public, see `The Meaning of "Public" <https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status>`_ in the *Amazon S3 User Guide* .

            :param is_public: Specifies whether the Object lambda Access Point Policy is Public or not. Object lambda Access Points are private by default.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-policystatus.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3objectlambda as s3objectlambda
                
                policy_status_property = s3objectlambda.CfnAccessPoint.PolicyStatusProperty(
                    is_public=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__567589e9b5b2f6e953182f1aec5f7104ad468c6abdba9a78102c5d1c446ab3cc)
                check_type(argname="argument is_public", value=is_public, expected_type=type_hints["is_public"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if is_public is not None:
                self._values["is_public"] = is_public

        @builtins.property
        def is_public(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether the Object lambda Access Point Policy is Public or not.

            Object lambda Access Points are private by default.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-policystatus.html#cfn-s3objectlambda-accesspoint-policystatus-ispublic
            '''
            result = self._values.get("is_public")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PolicyStatusProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3objectlambda.CfnAccessPoint.PublicAccessBlockConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "block_public_acls": "blockPublicAcls",
            "block_public_policy": "blockPublicPolicy",
            "ignore_public_acls": "ignorePublicAcls",
            "restrict_public_buckets": "restrictPublicBuckets",
        },
    )
    class PublicAccessBlockConfigurationProperty:
        def __init__(
            self,
            *,
            block_public_acls: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            block_public_policy: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            ignore_public_acls: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            restrict_public_buckets: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The ``PublicAccessBlock`` configuration that you want to apply to this Amazon S3 account.

            You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see `The Meaning of "Public" <https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status>`_ in the *Amazon S3 User Guide* .

            This data type is not supported for Amazon S3 on Outposts.

            :param block_public_acls: Specifies whether Amazon S3 should block public access control lists (ACLs) for buckets in this account. Setting this element to ``TRUE`` causes the following behavior: - ``PutBucketAcl`` and ``PutObjectAcl`` calls fail if the specified ACL is public. - PUT Object calls fail if the request includes a public ACL. - PUT Bucket calls fail if the request includes a public ACL. Enabling this setting doesn't affect existing policies or ACLs. This property is not supported for Amazon S3 on Outposts.
            :param block_public_policy: Specifies whether Amazon S3 should block public bucket policies for buckets in this account. Setting this element to ``TRUE`` causes Amazon S3 to reject calls to PUT Bucket policy if the specified bucket policy allows public access. Enabling this setting doesn't affect existing bucket policies. This property is not supported for Amazon S3 on Outposts.
            :param ignore_public_acls: Specifies whether Amazon S3 should ignore public ACLs for buckets in this account. Setting this element to ``TRUE`` causes Amazon S3 to ignore all public ACLs on buckets in this account and any objects that they contain. Enabling this setting doesn't affect the persistence of any existing ACLs and doesn't prevent new public ACLs from being set. This property is not supported for Amazon S3 on Outposts.
            :param restrict_public_buckets: Specifies whether Amazon S3 should restrict public bucket policies for buckets in this account. Setting this element to ``TRUE`` restricts access to buckets with public policies to only AWS service principals and authorized users within this account. Enabling this setting doesn't affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked. This property is not supported for Amazon S3 on Outposts.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-publicaccessblockconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3objectlambda as s3objectlambda
                
                public_access_block_configuration_property = s3objectlambda.CfnAccessPoint.PublicAccessBlockConfigurationProperty(
                    block_public_acls=False,
                    block_public_policy=False,
                    ignore_public_acls=False,
                    restrict_public_buckets=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__12c04bac03609eea5e08bddece37a8aca57faed68fc43e07a3a742f9ab0974f8)
                check_type(argname="argument block_public_acls", value=block_public_acls, expected_type=type_hints["block_public_acls"])
                check_type(argname="argument block_public_policy", value=block_public_policy, expected_type=type_hints["block_public_policy"])
                check_type(argname="argument ignore_public_acls", value=ignore_public_acls, expected_type=type_hints["ignore_public_acls"])
                check_type(argname="argument restrict_public_buckets", value=restrict_public_buckets, expected_type=type_hints["restrict_public_buckets"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if block_public_acls is not None:
                self._values["block_public_acls"] = block_public_acls
            if block_public_policy is not None:
                self._values["block_public_policy"] = block_public_policy
            if ignore_public_acls is not None:
                self._values["ignore_public_acls"] = ignore_public_acls
            if restrict_public_buckets is not None:
                self._values["restrict_public_buckets"] = restrict_public_buckets

        @builtins.property
        def block_public_acls(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether Amazon S3 should block public access control lists (ACLs) for buckets in this account.

            Setting this element to ``TRUE`` causes the following behavior:

            - ``PutBucketAcl`` and ``PutObjectAcl`` calls fail if the specified ACL is public.
            - PUT Object calls fail if the request includes a public ACL.
            - PUT Bucket calls fail if the request includes a public ACL.

            Enabling this setting doesn't affect existing policies or ACLs.

            This property is not supported for Amazon S3 on Outposts.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-publicaccessblockconfiguration.html#cfn-s3objectlambda-accesspoint-publicaccessblockconfiguration-blockpublicacls
            '''
            result = self._values.get("block_public_acls")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def block_public_policy(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether Amazon S3 should block public bucket policies for buckets in this account.

            Setting this element to ``TRUE`` causes Amazon S3 to reject calls to PUT Bucket policy if the specified bucket policy allows public access.

            Enabling this setting doesn't affect existing bucket policies.

            This property is not supported for Amazon S3 on Outposts.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-publicaccessblockconfiguration.html#cfn-s3objectlambda-accesspoint-publicaccessblockconfiguration-blockpublicpolicy
            '''
            result = self._values.get("block_public_policy")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def ignore_public_acls(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether Amazon S3 should ignore public ACLs for buckets in this account.

            Setting this element to ``TRUE`` causes Amazon S3 to ignore all public ACLs on buckets in this account and any objects that they contain.

            Enabling this setting doesn't affect the persistence of any existing ACLs and doesn't prevent new public ACLs from being set.

            This property is not supported for Amazon S3 on Outposts.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-publicaccessblockconfiguration.html#cfn-s3objectlambda-accesspoint-publicaccessblockconfiguration-ignorepublicacls
            '''
            result = self._values.get("ignore_public_acls")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def restrict_public_buckets(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether Amazon S3 should restrict public bucket policies for buckets in this account.

            Setting this element to ``TRUE`` restricts access to buckets with public policies to only AWS service principals and authorized users within this account.

            Enabling this setting doesn't affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked.

            This property is not supported for Amazon S3 on Outposts.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-publicaccessblockconfiguration.html#cfn-s3objectlambda-accesspoint-publicaccessblockconfiguration-restrictpublicbuckets
            '''
            result = self._values.get("restrict_public_buckets")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PublicAccessBlockConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3objectlambda.CfnAccessPoint.TransformationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "actions": "actions",
            "content_transformation": "contentTransformation",
        },
    )
    class TransformationConfigurationProperty:
        def __init__(
            self,
            *,
            actions: typing.Sequence[builtins.str],
            content_transformation: typing.Any,
        ) -> None:
            '''A configuration used when creating an Object Lambda Access Point transformation.

            :param actions: A container for the action of an Object Lambda Access Point configuration. Valid inputs are ``GetObject`` , ``HeadObject`` , ``ListObject`` , and ``ListObjectV2`` .
            :param content_transformation: A container for the content transformation of an Object Lambda Access Point configuration. Can include the FunctionArn and FunctionPayload. For more information, see `AwsLambdaTransformation <https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_AwsLambdaTransformation.html>`_ in the *Amazon S3 API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-transformationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3objectlambda as s3objectlambda
                
                # content_transformation: Any
                
                transformation_configuration_property = s3objectlambda.CfnAccessPoint.TransformationConfigurationProperty(
                    actions=["actions"],
                    content_transformation=content_transformation
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d813fa32fb650257882ca805d56459cab0e118595c1aa53f20603c3da7aab305)
                check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
                check_type(argname="argument content_transformation", value=content_transformation, expected_type=type_hints["content_transformation"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "actions": actions,
                "content_transformation": content_transformation,
            }

        @builtins.property
        def actions(self) -> typing.List[builtins.str]:
            '''A container for the action of an Object Lambda Access Point configuration.

            Valid inputs are ``GetObject`` , ``HeadObject`` , ``ListObject`` , and ``ListObjectV2`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-transformationconfiguration.html#cfn-s3objectlambda-accesspoint-transformationconfiguration-actions
            '''
            result = self._values.get("actions")
            assert result is not None, "Required property 'actions' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def content_transformation(self) -> typing.Any:
            '''A container for the content transformation of an Object Lambda Access Point configuration.

            Can include the FunctionArn and FunctionPayload. For more information, see `AwsLambdaTransformation <https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_AwsLambdaTransformation.html>`_ in the *Amazon S3 API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-transformationconfiguration.html#cfn-s3objectlambda-accesspoint-transformationconfiguration-contenttransformation
            '''
            result = self._values.get("content_transformation")
            assert result is not None, "Required property 'content_transformation' is missing"
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TransformationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnAccessPointPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3objectlambda.CfnAccessPointPolicy",
):
    '''The ``AWS::S3ObjectLambda::AccessPointPolicy`` resource specifies the Object Lambda Access Point resource policy document.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspointpolicy.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_s3objectlambda as s3objectlambda
        
        # policy_document: Any
        
        cfn_access_point_policy = s3objectlambda.CfnAccessPointPolicy(self, "MyCfnAccessPointPolicy",
            object_lambda_access_point="objectLambdaAccessPoint",
            policy_document=policy_document
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        object_lambda_access_point: builtins.str,
        policy_document: typing.Any,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param object_lambda_access_point: An access point with an attached AWS Lambda function used to access transformed data from an Amazon S3 bucket.
        :param policy_document: Object Lambda Access Point resource policy document.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38c2d34f6523c616e1afc407dc2231b5dcb990e107b03282b05407873f5abafb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAccessPointPolicyProps(
            object_lambda_access_point=object_lambda_access_point,
            policy_document=policy_document,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__476b48c6b590eb6900b185218ec9086959f09cb3a1ff210d00076950dc7d510a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b2b022ca3e974fbdb8a20d57f47c6b5a43ccee02cd200210e1064b5e6c82949f)
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
    @jsii.member(jsii_name="objectLambdaAccessPoint")
    def object_lambda_access_point(self) -> builtins.str:
        '''An access point with an attached AWS Lambda function used to access transformed data from an Amazon S3 bucket.'''
        return typing.cast(builtins.str, jsii.get(self, "objectLambdaAccessPoint"))

    @object_lambda_access_point.setter
    def object_lambda_access_point(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40f558fc15d35e909e4982b57f0cb15aac48aef92d7578cdf38fd49590b9353d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectLambdaAccessPoint", value)

    @builtins.property
    @jsii.member(jsii_name="policyDocument")
    def policy_document(self) -> typing.Any:
        '''Object Lambda Access Point resource policy document.'''
        return typing.cast(typing.Any, jsii.get(self, "policyDocument"))

    @policy_document.setter
    def policy_document(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1efc67ebff8549be6ada402864d14d3f20c1a9eb0a85a3c67f4b18a6e16a0c7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyDocument", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_s3objectlambda.CfnAccessPointPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "object_lambda_access_point": "objectLambdaAccessPoint",
        "policy_document": "policyDocument",
    },
)
class CfnAccessPointPolicyProps:
    def __init__(
        self,
        *,
        object_lambda_access_point: builtins.str,
        policy_document: typing.Any,
    ) -> None:
        '''Properties for defining a ``CfnAccessPointPolicy``.

        :param object_lambda_access_point: An access point with an attached AWS Lambda function used to access transformed data from an Amazon S3 bucket.
        :param policy_document: Object Lambda Access Point resource policy document.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspointpolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_s3objectlambda as s3objectlambda
            
            # policy_document: Any
            
            cfn_access_point_policy_props = s3objectlambda.CfnAccessPointPolicyProps(
                object_lambda_access_point="objectLambdaAccessPoint",
                policy_document=policy_document
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e74559fc14955323f1b747cf5a2176c72b35f214ab3c372190cb4bccfc72c73)
            check_type(argname="argument object_lambda_access_point", value=object_lambda_access_point, expected_type=type_hints["object_lambda_access_point"])
            check_type(argname="argument policy_document", value=policy_document, expected_type=type_hints["policy_document"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "object_lambda_access_point": object_lambda_access_point,
            "policy_document": policy_document,
        }

    @builtins.property
    def object_lambda_access_point(self) -> builtins.str:
        '''An access point with an attached AWS Lambda function used to access transformed data from an Amazon S3 bucket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspointpolicy.html#cfn-s3objectlambda-accesspointpolicy-objectlambdaaccesspoint
        '''
        result = self._values.get("object_lambda_access_point")
        assert result is not None, "Required property 'object_lambda_access_point' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_document(self) -> typing.Any:
        '''Object Lambda Access Point resource policy document.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspointpolicy.html#cfn-s3objectlambda-accesspointpolicy-policydocument
        '''
        result = self._values.get("policy_document")
        assert result is not None, "Required property 'policy_document' is missing"
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAccessPointPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_s3objectlambda.CfnAccessPointProps",
    jsii_struct_bases=[],
    name_mapping={
        "object_lambda_configuration": "objectLambdaConfiguration",
        "name": "name",
    },
)
class CfnAccessPointProps:
    def __init__(
        self,
        *,
        object_lambda_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAccessPoint.ObjectLambdaConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnAccessPoint``.

        :param object_lambda_configuration: A configuration used when creating an Object Lambda Access Point.
        :param name: The name of this access point.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspoint.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_s3objectlambda as s3objectlambda
            
            # content_transformation: Any
            
            cfn_access_point_props = s3objectlambda.CfnAccessPointProps(
                object_lambda_configuration=s3objectlambda.CfnAccessPoint.ObjectLambdaConfigurationProperty(
                    supporting_access_point="supportingAccessPoint",
                    transformation_configurations=[s3objectlambda.CfnAccessPoint.TransformationConfigurationProperty(
                        actions=["actions"],
                        content_transformation=content_transformation
                    )],
            
                    # the properties below are optional
                    allowed_features=["allowedFeatures"],
                    cloud_watch_metrics_enabled=False
                ),
            
                # the properties below are optional
                name="name"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66de11e6e5191035e65409608a7f83aecaaa29de4379ba833b4b4a340ffa4ecd)
            check_type(argname="argument object_lambda_configuration", value=object_lambda_configuration, expected_type=type_hints["object_lambda_configuration"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "object_lambda_configuration": object_lambda_configuration,
        }
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def object_lambda_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnAccessPoint.ObjectLambdaConfigurationProperty]:
        '''A configuration used when creating an Object Lambda Access Point.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspoint.html#cfn-s3objectlambda-accesspoint-objectlambdaconfiguration
        '''
        result = self._values.get("object_lambda_configuration")
        assert result is not None, "Required property 'object_lambda_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnAccessPoint.ObjectLambdaConfigurationProperty], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of this access point.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspoint.html#cfn-s3objectlambda-accesspoint-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAccessPointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAccessPoint",
    "CfnAccessPointPolicy",
    "CfnAccessPointPolicyProps",
    "CfnAccessPointProps",
]

publication.publish()

def _typecheckingstub__fc24858ef1979ca1cb8fba3d4a06956342322b232c5594f16f11ee6c380ea43b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    object_lambda_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAccessPoint.ObjectLambdaConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de086f7124fab776ebe585a8278086a48c54ce0f9432344e7ead7888d183a2af(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4bdd3b4c3dcd57f23413630ff374499bdd114af0eb3d609502c3ce8c4384c2f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72235765a4ddbec3dfa520018313ca825a0eee0d6620fbbc57d8d6942cd266e1(
    value: typing.Union[_IResolvable_da3f097b, CfnAccessPoint.ObjectLambdaConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1ec3bbadc1fe6d1688dbe3361b2c99aaf74daa3cbcc3c9006d8c862eee8b9f7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__057ad3aa353f20aafa8045ccead72b77f424a0108cc0869f56410bb930ad4959(
    *,
    status: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ee3118c2b111c6807c152b3884192374a50ef95bf6b87dbf9a0a05bc33c38fd(
    *,
    function_arn: builtins.str,
    function_payload: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2a3c7654e406c9a13790e67d3850f1b300c2434f25e8d6a2a17d16cb8ddbcc0(
    *,
    aws_lambda: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAccessPoint.AwsLambdaProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d802fe046f5597b4cf6ab6c81e09859cbab4304022fbba60a7a7493d751a7537(
    *,
    supporting_access_point: builtins.str,
    transformation_configurations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAccessPoint.TransformationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    allowed_features: typing.Optional[typing.Sequence[builtins.str]] = None,
    cloud_watch_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__567589e9b5b2f6e953182f1aec5f7104ad468c6abdba9a78102c5d1c446ab3cc(
    *,
    is_public: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12c04bac03609eea5e08bddece37a8aca57faed68fc43e07a3a742f9ab0974f8(
    *,
    block_public_acls: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    block_public_policy: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ignore_public_acls: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    restrict_public_buckets: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d813fa32fb650257882ca805d56459cab0e118595c1aa53f20603c3da7aab305(
    *,
    actions: typing.Sequence[builtins.str],
    content_transformation: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38c2d34f6523c616e1afc407dc2231b5dcb990e107b03282b05407873f5abafb(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    object_lambda_access_point: builtins.str,
    policy_document: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__476b48c6b590eb6900b185218ec9086959f09cb3a1ff210d00076950dc7d510a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2b022ca3e974fbdb8a20d57f47c6b5a43ccee02cd200210e1064b5e6c82949f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40f558fc15d35e909e4982b57f0cb15aac48aef92d7578cdf38fd49590b9353d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1efc67ebff8549be6ada402864d14d3f20c1a9eb0a85a3c67f4b18a6e16a0c7b(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e74559fc14955323f1b747cf5a2176c72b35f214ab3c372190cb4bccfc72c73(
    *,
    object_lambda_access_point: builtins.str,
    policy_document: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66de11e6e5191035e65409608a7f83aecaaa29de4379ba833b4b4a340ffa4ecd(
    *,
    object_lambda_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAccessPoint.ObjectLambdaConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
