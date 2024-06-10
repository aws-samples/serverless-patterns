'''
# AWS::SecurityLake Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_securitylake as securitylake
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for SecurityLake construct libraries](https://constructs.dev/search?q=securitylake)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::SecurityLake resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SecurityLake.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::SecurityLake](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SecurityLake.html).

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


@jsii.implements(_IInspectable_c2943556)
class CfnAwsLogSource(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_securitylake.CfnAwsLogSource",
):
    '''Adds a natively supported AWS service as an AWS source.

    Enables source types for member accounts in required AWS Regions, based on the parameters you specify. You can choose any source type in any Region for either accounts that are part of a trusted organization or standalone accounts. Once you add an AWS service as a source, Security Lake starts collecting logs and events from it.
    .. epigraph::

       If you want to create multiple sources using ``AWS::SecurityLake::AwsLogSource`` , you must use the ``DependsOn`` attribute to create the sources sequentially. With the ``DependsOn`` attribute you can specify that the creation of a specific ``AWSLogSource`` follows another. When you add a ``DependsOn`` attribute to a resource, that resource is created only after the creation of the resource specified in the ``DependsOn`` attribute. For an example, see `Add AWS log sources <https://docs.aws.amazon.com//AWSCloudFormation/latest/UserGuide/aws-resource-securitylake-awslogsource.html#aws-resource-securitylake-awslogsource--examples>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securitylake-awslogsource.html
    :cloudformationResource: AWS::SecurityLake::AwsLogSource
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_securitylake as securitylake
        
        cfn_aws_log_source = securitylake.CfnAwsLogSource(self, "MyCfnAwsLogSource",
            data_lake_arn="dataLakeArn",
            source_name="sourceName",
            source_version="sourceVersion",
        
            # the properties below are optional
            accounts=["accounts"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        data_lake_arn: builtins.str,
        source_name: builtins.str,
        source_version: builtins.str,
        accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param data_lake_arn: The Amazon Resource Name (ARN) used to create the data lake.
        :param source_name: The name for a AWS source. This must be a Regionally unique value. For the list of sources supported by Amazon Security Lake see `Collecting data from AWS services <https://docs.aws.amazon.com//security-lake/latest/userguide/internal-sources.html>`_ in the Amazon Security Lake User Guide.
        :param source_version: The version for a AWS source. For more details about source versions supported by Amazon Security Lake see `OCSF source identification <https://docs.aws.amazon.com//security-lake/latest/userguide/open-cybersecurity-schema-framework.html#ocsf-source-identification>`_ in the Amazon Security Lake User Guide. This must be a Regionally unique value.
        :param accounts: Specify the AWS account information where you want to enable Security Lake.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c67fc1d68d61ef9dead7d443499c1a142da192386efc06474b3758994937de6b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAwsLogSourceProps(
            data_lake_arn=data_lake_arn,
            source_name=source_name,
            source_version=source_version,
            accounts=accounts,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f493097d98865e82cabeeb80dd31577169140709170903a313d3bc579da5bcb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d4b08275c623e99b1c0cca9f7d97a78cf719804d590ae90e5af151255c42753a)
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
    @jsii.member(jsii_name="dataLakeArn")
    def data_lake_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) used to create the data lake.'''
        return typing.cast(builtins.str, jsii.get(self, "dataLakeArn"))

    @data_lake_arn.setter
    def data_lake_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed09f296c9b906f7011ea796fce3b42122e1c0490eb544e941f5953a5b0f8403)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataLakeArn", value)

    @builtins.property
    @jsii.member(jsii_name="sourceName")
    def source_name(self) -> builtins.str:
        '''The name for a AWS source.'''
        return typing.cast(builtins.str, jsii.get(self, "sourceName"))

    @source_name.setter
    def source_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__786699bc5ed670115ad16fc2d5cab658ddb4c20d9afccc0010adb67c796143ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceName", value)

    @builtins.property
    @jsii.member(jsii_name="sourceVersion")
    def source_version(self) -> builtins.str:
        '''The version for a AWS source.'''
        return typing.cast(builtins.str, jsii.get(self, "sourceVersion"))

    @source_version.setter
    def source_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2369f0ca541c99625731d8a7db77fa2a9f1346eab63190644c2695d471ddda46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceVersion", value)

    @builtins.property
    @jsii.member(jsii_name="accounts")
    def accounts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify the AWS account information where you want to enable Security Lake.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "accounts"))

    @accounts.setter
    def accounts(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1f564a49d096390f47538b02cc909d2927202e7d6b998b761aaf21810dcf11c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accounts", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_securitylake.CfnAwsLogSourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "data_lake_arn": "dataLakeArn",
        "source_name": "sourceName",
        "source_version": "sourceVersion",
        "accounts": "accounts",
    },
)
class CfnAwsLogSourceProps:
    def __init__(
        self,
        *,
        data_lake_arn: builtins.str,
        source_name: builtins.str,
        source_version: builtins.str,
        accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAwsLogSource``.

        :param data_lake_arn: The Amazon Resource Name (ARN) used to create the data lake.
        :param source_name: The name for a AWS source. This must be a Regionally unique value. For the list of sources supported by Amazon Security Lake see `Collecting data from AWS services <https://docs.aws.amazon.com//security-lake/latest/userguide/internal-sources.html>`_ in the Amazon Security Lake User Guide.
        :param source_version: The version for a AWS source. For more details about source versions supported by Amazon Security Lake see `OCSF source identification <https://docs.aws.amazon.com//security-lake/latest/userguide/open-cybersecurity-schema-framework.html#ocsf-source-identification>`_ in the Amazon Security Lake User Guide. This must be a Regionally unique value.
        :param accounts: Specify the AWS account information where you want to enable Security Lake.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securitylake-awslogsource.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_securitylake as securitylake
            
            cfn_aws_log_source_props = securitylake.CfnAwsLogSourceProps(
                data_lake_arn="dataLakeArn",
                source_name="sourceName",
                source_version="sourceVersion",
            
                # the properties below are optional
                accounts=["accounts"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56ae11383caeefb7587043503a4fd999d42e30184765bd5e736dcae60c5b3b94)
            check_type(argname="argument data_lake_arn", value=data_lake_arn, expected_type=type_hints["data_lake_arn"])
            check_type(argname="argument source_name", value=source_name, expected_type=type_hints["source_name"])
            check_type(argname="argument source_version", value=source_version, expected_type=type_hints["source_version"])
            check_type(argname="argument accounts", value=accounts, expected_type=type_hints["accounts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_lake_arn": data_lake_arn,
            "source_name": source_name,
            "source_version": source_version,
        }
        if accounts is not None:
            self._values["accounts"] = accounts

    @builtins.property
    def data_lake_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) used to create the data lake.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securitylake-awslogsource.html#cfn-securitylake-awslogsource-datalakearn
        '''
        result = self._values.get("data_lake_arn")
        assert result is not None, "Required property 'data_lake_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_name(self) -> builtins.str:
        '''The name for a AWS source.

        This must be a Regionally unique value. For the list of sources supported by Amazon Security Lake see `Collecting data from AWS services <https://docs.aws.amazon.com//security-lake/latest/userguide/internal-sources.html>`_ in the Amazon Security Lake User Guide.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securitylake-awslogsource.html#cfn-securitylake-awslogsource-sourcename
        '''
        result = self._values.get("source_name")
        assert result is not None, "Required property 'source_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_version(self) -> builtins.str:
        '''The version for a AWS source.

        For more details about source versions supported by Amazon Security Lake see `OCSF source identification <https://docs.aws.amazon.com//security-lake/latest/userguide/open-cybersecurity-schema-framework.html#ocsf-source-identification>`_ in the Amazon Security Lake User Guide. This must be a Regionally unique value.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securitylake-awslogsource.html#cfn-securitylake-awslogsource-sourceversion
        '''
        result = self._values.get("source_version")
        assert result is not None, "Required property 'source_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accounts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify the AWS account information where you want to enable Security Lake.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securitylake-awslogsource.html#cfn-securitylake-awslogsource-accounts
        '''
        result = self._values.get("accounts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAwsLogSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnDataLake(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_securitylake.CfnDataLake",
):
    '''Initializes an Amazon Security Lake instance with the provided (or default) configuration.

    You can enable Security Lake in AWS Regions with customized settings before enabling log collection in Regions. To specify particular Regions, configure these Regions using the ``configurations`` parameter. If you have already enabled Security Lake in a Region when you call this command, the command will update the Region if you provide new configuration parameters. If you have not already enabled Security Lake in the Region when you call this API, it will set up the data lake in the Region with the specified configurations.

    When you enable Security Lake , it starts ingesting security data after the ``CreateAwsLogSource`` call. This includes ingesting security data from sources, storing data, and making data accessible to subscribers. Security Lake also enables all the existing settings and resources that it stores or maintains for your AWS account in the current Region, including security log and event data. For more information, see the `Amazon Security Lake User Guide <https://docs.aws.amazon.com//security-lake/latest/userguide/what-is-security-lake.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securitylake-datalake.html
    :cloudformationResource: AWS::SecurityLake::DataLake
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_securitylake as securitylake
        
        cfn_data_lake = securitylake.CfnDataLake(self, "MyCfnDataLake",
            encryption_configuration=securitylake.CfnDataLake.EncryptionConfigurationProperty(
                kms_key_id="kmsKeyId"
            ),
            lifecycle_configuration=securitylake.CfnDataLake.LifecycleConfigurationProperty(
                expiration=securitylake.CfnDataLake.ExpirationProperty(
                    days=123
                ),
                transitions=[securitylake.CfnDataLake.TransitionsProperty(
                    days=123,
                    storage_class="storageClass"
                )]
            ),
            meta_store_manager_role_arn="metaStoreManagerRoleArn",
            replication_configuration=securitylake.CfnDataLake.ReplicationConfigurationProperty(
                regions=["regions"],
                role_arn="roleArn"
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
        encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataLake.EncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        lifecycle_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataLake.LifecycleConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        meta_store_manager_role_arn: typing.Optional[builtins.str] = None,
        replication_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataLake.ReplicationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param encryption_configuration: Provides encryption details of the Amazon Security Lake object.
        :param lifecycle_configuration: You can customize Security Lake to store data in your preferred AWS Regions for your preferred amount of time. Lifecycle management can help you comply with different compliance requirements. For more details, see `Lifecycle management <https://docs.aws.amazon.com//security-lake/latest/userguide/lifecycle-management.html>`_ in the Amazon Security Lake User Guide.
        :param meta_store_manager_role_arn: The Amazon Resource Name (ARN) used to create and update the AWS Glue table. This table contains partitions generated by the ingestion and normalization of AWS log sources and custom sources.
        :param replication_configuration: Provides replication details of Amazon Security Lake object.
        :param tags: An array of objects, one for each tag to associate with the data lake configuration. For each tag, you must specify both a tag key and a tag value. A tag value cannot be null, but it can be an empty string.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff487a50882ee11f396717fb970b445f3274af88108d1c1d390543dfb1fdf534)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDataLakeProps(
            encryption_configuration=encryption_configuration,
            lifecycle_configuration=lifecycle_configuration,
            meta_store_manager_role_arn=meta_store_manager_role_arn,
            replication_configuration=replication_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d7a1c25528114b19a22f7fe9e5b4213f46c37e16f22245bc3dc38ad34fc7ef6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__eb852df583c773c6f5d30c27afae6f598c8606ae40f25dd1885d8fbf5013661b)
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
        '''The Amazon Resource Name (ARN) of the data lake.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrS3BucketArn")
    def attr_s3_bucket_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Amazon S3 bucket.

        :cloudformationAttribute: S3BucketArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrS3BucketArn"))

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
    @jsii.member(jsii_name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataLake.EncryptionConfigurationProperty"]]:
        '''Provides encryption details of the Amazon Security Lake object.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataLake.EncryptionConfigurationProperty"]], jsii.get(self, "encryptionConfiguration"))

    @encryption_configuration.setter
    def encryption_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataLake.EncryptionConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12edf08ab82b633325fe7034b3424955ea7bff566dfa00928107723a5d0f6a72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfiguration")
    def lifecycle_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataLake.LifecycleConfigurationProperty"]]:
        '''You can customize Security Lake to store data in your preferred AWS Regions for your preferred amount of time.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataLake.LifecycleConfigurationProperty"]], jsii.get(self, "lifecycleConfiguration"))

    @lifecycle_configuration.setter
    def lifecycle_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataLake.LifecycleConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__916659d1bcdf1d6d40de689f3b334b766e1a8fb681a493926742e61ce5ba40b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="metaStoreManagerRoleArn")
    def meta_store_manager_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) used to create and update the AWS Glue table.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metaStoreManagerRoleArn"))

    @meta_store_manager_role_arn.setter
    def meta_store_manager_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23cd82335763114e4ff9c52f4ff2b4db4b4be68cc8f5b468e1325fa0e0e79558)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metaStoreManagerRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="replicationConfiguration")
    def replication_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataLake.ReplicationConfigurationProperty"]]:
        '''Provides replication details of Amazon Security Lake object.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataLake.ReplicationConfigurationProperty"]], jsii.get(self, "replicationConfiguration"))

    @replication_configuration.setter
    def replication_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataLake.ReplicationConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__647257bd68002b29a89b3128d4883d0c748e98d2c70a5b154446993271225230)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of objects, one for each tag to associate with the data lake configuration.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6654ce3b2fa02feedc8f03797f96ae7270d4bd79ef3c3791b522e8277fa3798c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securitylake.CfnDataLake.EncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"kms_key_id": "kmsKeyId"},
    )
    class EncryptionConfigurationProperty:
        def __init__(self, *, kms_key_id: typing.Optional[builtins.str] = None) -> None:
            '''Provides encryption details of the Amazon Security Lake object.

            The AWS shared responsibility model applies to data protection in Amazon Security Lake . As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. For more details, see `Data protection <https://docs.aws.amazon.com//security-lake/latest/userguide/data-protection.html>`_ in the Amazon Security Lake User Guide.

            :param kms_key_id: The ID of KMS encryption key used by Amazon Security Lake to encrypt the Security Lake object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-datalake-encryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securitylake as securitylake
                
                encryption_configuration_property = securitylake.CfnDataLake.EncryptionConfigurationProperty(
                    kms_key_id="kmsKeyId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c697088167e83d968076432c9f71877137655465afc625784270e3ba40d3f57b)
                check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''The ID of KMS encryption key used by Amazon Security Lake to encrypt the Security Lake object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-datalake-encryptionconfiguration.html#cfn-securitylake-datalake-encryptionconfiguration-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securitylake.CfnDataLake.ExpirationProperty",
        jsii_struct_bases=[],
        name_mapping={"days": "days"},
    )
    class ExpirationProperty:
        def __init__(self, *, days: typing.Optional[jsii.Number] = None) -> None:
            '''Provides data expiration details of the Amazon Security Lake object.

            You can specify your preferred Amazon S3 storage class and the time period for S3 objects to stay in that storage class before they expire. For more information about Amazon S3 Lifecycle configurations, see `Managing your storage lifecycle <https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html>`_ in the *Amazon Simple Storage Service User Guide* .

            :param days: The number of days before data expires in the Amazon Security Lake object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-datalake-expiration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securitylake as securitylake
                
                expiration_property = securitylake.CfnDataLake.ExpirationProperty(
                    days=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__676fee3c866c464d5b150fd2a1553faf30ba52129224b9869203f21574e77d9f)
                check_type(argname="argument days", value=days, expected_type=type_hints["days"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if days is not None:
                self._values["days"] = days

        @builtins.property
        def days(self) -> typing.Optional[jsii.Number]:
            '''The number of days before data expires in the Amazon Security Lake object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-datalake-expiration.html#cfn-securitylake-datalake-expiration-days
            '''
            result = self._values.get("days")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExpirationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securitylake.CfnDataLake.LifecycleConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"expiration": "expiration", "transitions": "transitions"},
    )
    class LifecycleConfigurationProperty:
        def __init__(
            self,
            *,
            expiration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataLake.ExpirationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            transitions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataLake.TransitionsProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Provides lifecycle details of Amazon Security Lake object.

            To manage your data so that it is stored cost effectively, you can configure retention settings for the data. You can specify your preferred Amazon S3 storage class and the time period for Amazon S3 objects to stay in that storage class before they transition to a different storage class or expire. For more information about Amazon S3 Lifecycle configurations, see `Managing your storage lifecycle <https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html>`_ in the *Amazon Simple Storage Service User Guide* .

            In Security Lake , you specify retention settings at the Region level. For example, you might choose to transition all S3 objects in a specific AWS Region to the ``S3 Standard-IA`` storage class 30 days after they're written to the data lake. The default Amazon S3 storage class is S3 Standard.
            .. epigraph::

               Security Lake doesn't support Amazon S3 Object Lock. When the data lake buckets are created, S3 Object Lock is disabled by default. Enabling S3 Object Lock with default retention mode interrupts the delivery of normalized log data to the data lake.

            :param expiration: Provides data expiration details of the Amazon Security Lake object.
            :param transitions: Provides data storage transition details of Amazon Security Lake object. By configuring these settings, you can specify your preferred Amazon S3 storage class and the time period for S3 objects to stay in that storage class before they transition to a different storage class.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-datalake-lifecycleconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securitylake as securitylake
                
                lifecycle_configuration_property = securitylake.CfnDataLake.LifecycleConfigurationProperty(
                    expiration=securitylake.CfnDataLake.ExpirationProperty(
                        days=123
                    ),
                    transitions=[securitylake.CfnDataLake.TransitionsProperty(
                        days=123,
                        storage_class="storageClass"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__09cd166ed037b2c00b8a44dc0e94832b0851b09edc3ca5e9ac0de67068729149)
                check_type(argname="argument expiration", value=expiration, expected_type=type_hints["expiration"])
                check_type(argname="argument transitions", value=transitions, expected_type=type_hints["transitions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if expiration is not None:
                self._values["expiration"] = expiration
            if transitions is not None:
                self._values["transitions"] = transitions

        @builtins.property
        def expiration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataLake.ExpirationProperty"]]:
            '''Provides data expiration details of the Amazon Security Lake object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-datalake-lifecycleconfiguration.html#cfn-securitylake-datalake-lifecycleconfiguration-expiration
            '''
            result = self._values.get("expiration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataLake.ExpirationProperty"]], result)

        @builtins.property
        def transitions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataLake.TransitionsProperty"]]]]:
            '''Provides data storage transition details of Amazon Security Lake object.

            By configuring these settings, you can specify your preferred Amazon S3 storage class and the time period for S3 objects to stay in that storage class before they transition to a different storage class.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-datalake-lifecycleconfiguration.html#cfn-securitylake-datalake-lifecycleconfiguration-transitions
            '''
            result = self._values.get("transitions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataLake.TransitionsProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LifecycleConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securitylake.CfnDataLake.ReplicationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"regions": "regions", "role_arn": "roleArn"},
    )
    class ReplicationConfigurationProperty:
        def __init__(
            self,
            *,
            regions: typing.Optional[typing.Sequence[builtins.str]] = None,
            role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides replication configuration details for objects stored in the Amazon Security Lake data lake.

            :param regions: Specifies one or more centralized rollup Regions. The AWS Region specified in the region parameter of the ``CreateDataLake`` or ``UpdateDataLake`` operations contributes data to the rollup Region or Regions specified in this parameter. Replication enables automatic, asynchronous copying of objects across Amazon S3 buckets. S3 buckets that are configured for object replication can be owned by the same AWS account or by different accounts. You can replicate objects to a single destination bucket or to multiple destination buckets. The destination buckets can be in different Regions or within the same Region as the source bucket.
            :param role_arn: Replication settings for the Amazon S3 buckets. This parameter uses the AWS Identity and Access Management (IAM) role you created that is managed by Security Lake , to ensure the replication setting is correct.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-datalake-replicationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securitylake as securitylake
                
                replication_configuration_property = securitylake.CfnDataLake.ReplicationConfigurationProperty(
                    regions=["regions"],
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f5e309ce471c0b5b94d10c5cf8d75ece96a70a7112aa8396372449cae02d7005)
                check_type(argname="argument regions", value=regions, expected_type=type_hints["regions"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if regions is not None:
                self._values["regions"] = regions
            if role_arn is not None:
                self._values["role_arn"] = role_arn

        @builtins.property
        def regions(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Specifies one or more centralized rollup Regions.

            The AWS Region specified in the region parameter of the ``CreateDataLake`` or ``UpdateDataLake`` operations contributes data to the rollup Region or Regions specified in this parameter.

            Replication enables automatic, asynchronous copying of objects across Amazon S3 buckets. S3 buckets that are configured for object replication can be owned by the same AWS account or by different accounts. You can replicate objects to a single destination bucket or to multiple destination buckets. The destination buckets can be in different Regions or within the same Region as the source bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-datalake-replicationconfiguration.html#cfn-securitylake-datalake-replicationconfiguration-regions
            '''
            result = self._values.get("regions")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''Replication settings for the Amazon S3 buckets.

            This parameter uses the AWS Identity and Access Management (IAM) role you created that is managed by Security Lake , to ensure the replication setting is correct.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-datalake-replicationconfiguration.html#cfn-securitylake-datalake-replicationconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReplicationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securitylake.CfnDataLake.TransitionsProperty",
        jsii_struct_bases=[],
        name_mapping={"days": "days", "storage_class": "storageClass"},
    )
    class TransitionsProperty:
        def __init__(
            self,
            *,
            days: typing.Optional[jsii.Number] = None,
            storage_class: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides transition lifecycle details of the Amazon Security Lake object.

            For more information about Amazon S3 Lifecycle configurations, see `Managing your storage lifecycle <https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html>`_ in the *Amazon Simple Storage Service User Guide* .

            :param days: The number of days before data transitions to a different S3 Storage Class in the Amazon Security Lake object.
            :param storage_class: The list of storage classes that you can choose from based on the data access, resiliency, and cost requirements of your workloads. The default storage class is S3 Standard.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-datalake-transitions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securitylake as securitylake
                
                transitions_property = securitylake.CfnDataLake.TransitionsProperty(
                    days=123,
                    storage_class="storageClass"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__aaac67133f980ed118f75aa7447b8e2c8f6a4e8d8fce97491e407d04b2924302)
                check_type(argname="argument days", value=days, expected_type=type_hints["days"])
                check_type(argname="argument storage_class", value=storage_class, expected_type=type_hints["storage_class"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if days is not None:
                self._values["days"] = days
            if storage_class is not None:
                self._values["storage_class"] = storage_class

        @builtins.property
        def days(self) -> typing.Optional[jsii.Number]:
            '''The number of days before data transitions to a different S3 Storage Class in the Amazon Security Lake object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-datalake-transitions.html#cfn-securitylake-datalake-transitions-days
            '''
            result = self._values.get("days")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def storage_class(self) -> typing.Optional[builtins.str]:
            '''The list of storage classes that you can choose from based on the data access, resiliency, and cost requirements of your workloads.

            The default storage class is S3 Standard.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-datalake-transitions.html#cfn-securitylake-datalake-transitions-storageclass
            '''
            result = self._values.get("storage_class")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TransitionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_securitylake.CfnDataLakeProps",
    jsii_struct_bases=[],
    name_mapping={
        "encryption_configuration": "encryptionConfiguration",
        "lifecycle_configuration": "lifecycleConfiguration",
        "meta_store_manager_role_arn": "metaStoreManagerRoleArn",
        "replication_configuration": "replicationConfiguration",
        "tags": "tags",
    },
)
class CfnDataLakeProps:
    def __init__(
        self,
        *,
        encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLake.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        lifecycle_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLake.LifecycleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        meta_store_manager_role_arn: typing.Optional[builtins.str] = None,
        replication_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLake.ReplicationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDataLake``.

        :param encryption_configuration: Provides encryption details of the Amazon Security Lake object.
        :param lifecycle_configuration: You can customize Security Lake to store data in your preferred AWS Regions for your preferred amount of time. Lifecycle management can help you comply with different compliance requirements. For more details, see `Lifecycle management <https://docs.aws.amazon.com//security-lake/latest/userguide/lifecycle-management.html>`_ in the Amazon Security Lake User Guide.
        :param meta_store_manager_role_arn: The Amazon Resource Name (ARN) used to create and update the AWS Glue table. This table contains partitions generated by the ingestion and normalization of AWS log sources and custom sources.
        :param replication_configuration: Provides replication details of Amazon Security Lake object.
        :param tags: An array of objects, one for each tag to associate with the data lake configuration. For each tag, you must specify both a tag key and a tag value. A tag value cannot be null, but it can be an empty string.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securitylake-datalake.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_securitylake as securitylake
            
            cfn_data_lake_props = securitylake.CfnDataLakeProps(
                encryption_configuration=securitylake.CfnDataLake.EncryptionConfigurationProperty(
                    kms_key_id="kmsKeyId"
                ),
                lifecycle_configuration=securitylake.CfnDataLake.LifecycleConfigurationProperty(
                    expiration=securitylake.CfnDataLake.ExpirationProperty(
                        days=123
                    ),
                    transitions=[securitylake.CfnDataLake.TransitionsProperty(
                        days=123,
                        storage_class="storageClass"
                    )]
                ),
                meta_store_manager_role_arn="metaStoreManagerRoleArn",
                replication_configuration=securitylake.CfnDataLake.ReplicationConfigurationProperty(
                    regions=["regions"],
                    role_arn="roleArn"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f98044af937b493e98dc654fc28cbeccbd1ee2f339cd00c1cc59056847b8fb37)
            check_type(argname="argument encryption_configuration", value=encryption_configuration, expected_type=type_hints["encryption_configuration"])
            check_type(argname="argument lifecycle_configuration", value=lifecycle_configuration, expected_type=type_hints["lifecycle_configuration"])
            check_type(argname="argument meta_store_manager_role_arn", value=meta_store_manager_role_arn, expected_type=type_hints["meta_store_manager_role_arn"])
            check_type(argname="argument replication_configuration", value=replication_configuration, expected_type=type_hints["replication_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if encryption_configuration is not None:
            self._values["encryption_configuration"] = encryption_configuration
        if lifecycle_configuration is not None:
            self._values["lifecycle_configuration"] = lifecycle_configuration
        if meta_store_manager_role_arn is not None:
            self._values["meta_store_manager_role_arn"] = meta_store_manager_role_arn
        if replication_configuration is not None:
            self._values["replication_configuration"] = replication_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataLake.EncryptionConfigurationProperty]]:
        '''Provides encryption details of the Amazon Security Lake object.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securitylake-datalake.html#cfn-securitylake-datalake-encryptionconfiguration
        '''
        result = self._values.get("encryption_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataLake.EncryptionConfigurationProperty]], result)

    @builtins.property
    def lifecycle_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataLake.LifecycleConfigurationProperty]]:
        '''You can customize Security Lake to store data in your preferred AWS Regions for your preferred amount of time.

        Lifecycle management can help you comply with different compliance requirements. For more details, see `Lifecycle management <https://docs.aws.amazon.com//security-lake/latest/userguide/lifecycle-management.html>`_ in the Amazon Security Lake User Guide.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securitylake-datalake.html#cfn-securitylake-datalake-lifecycleconfiguration
        '''
        result = self._values.get("lifecycle_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataLake.LifecycleConfigurationProperty]], result)

    @builtins.property
    def meta_store_manager_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) used to create and update the AWS Glue table.

        This table contains partitions generated by the ingestion and normalization of AWS log sources and custom sources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securitylake-datalake.html#cfn-securitylake-datalake-metastoremanagerrolearn
        '''
        result = self._values.get("meta_store_manager_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replication_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataLake.ReplicationConfigurationProperty]]:
        '''Provides replication details of Amazon Security Lake object.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securitylake-datalake.html#cfn-securitylake-datalake-replicationconfiguration
        '''
        result = self._values.get("replication_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataLake.ReplicationConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of objects, one for each tag to associate with the data lake configuration.

        For each tag, you must specify both a tag key and a tag value. A tag value cannot be null, but it can be an empty string.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securitylake-datalake.html#cfn-securitylake-datalake-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataLakeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnSubscriber(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_securitylake.CfnSubscriber",
):
    '''Creates a subscriber for accounts that are already enabled in Amazon Security Lake.

    You can create a subscriber with access to data in the current AWS Region.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securitylake-subscriber.html
    :cloudformationResource: AWS::SecurityLake::Subscriber
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_securitylake as securitylake
        
        cfn_subscriber = securitylake.CfnSubscriber(self, "MyCfnSubscriber",
            access_types=["accessTypes"],
            data_lake_arn="dataLakeArn",
            sources=[securitylake.CfnSubscriber.SourceProperty(
                aws_log_source=securitylake.CfnSubscriber.AwsLogSourceProperty(
                    source_name="sourceName",
                    source_version="sourceVersion"
                ),
                custom_log_source=securitylake.CfnSubscriber.CustomLogSourceProperty(
                    source_name="sourceName",
                    source_version="sourceVersion"
                )
            )],
            subscriber_identity=securitylake.CfnSubscriber.SubscriberIdentityProperty(
                external_id="externalId",
                principal="principal"
            ),
            subscriber_name="subscriberName",
        
            # the properties below are optional
            subscriber_description="subscriberDescription",
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
        access_types: typing.Sequence[builtins.str],
        data_lake_arn: builtins.str,
        sources: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSubscriber.SourceProperty", typing.Dict[builtins.str, typing.Any]]]]],
        subscriber_identity: typing.Union[_IResolvable_da3f097b, typing.Union["CfnSubscriber.SubscriberIdentityProperty", typing.Dict[builtins.str, typing.Any]]],
        subscriber_name: builtins.str,
        subscriber_description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param access_types: You can choose to notify subscribers of new objects with an Amazon Simple Queue Service (Amazon SQS) queue or through messaging to an HTTPS endpoint provided by the subscriber. Subscribers can consume data by directly querying AWS Lake Formation tables in your Amazon S3 bucket through services like Amazon Athena. This subscription type is defined as ``LAKEFORMATION`` .
        :param data_lake_arn: The Amazon Resource Name (ARN) used to create the data lake.
        :param sources: Amazon Security Lake supports log and event collection for natively supported AWS services . For more information, see the `Amazon Security Lake User Guide <https://docs.aws.amazon.com//security-lake/latest/userguide/source-management.html>`_ .
        :param subscriber_identity: The AWS identity used to access your data.
        :param subscriber_name: The name of your Amazon Security Lake subscriber account.
        :param subscriber_description: The subscriber descriptions for a subscriber account. The description for a subscriber includes ``subscriberName`` , ``accountID`` , ``externalID`` , and ``subscriberId`` .
        :param tags: An array of objects, one for each tag to associate with the subscriber. For each tag, you must specify both a tag key and a tag value. A tag value cannot be null, but it can be an empty string.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cfdc1f6a6f3c553e914b6e8b917c7abd1db0a1142db24f189c29526acaaea39)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSubscriberProps(
            access_types=access_types,
            data_lake_arn=data_lake_arn,
            sources=sources,
            subscriber_identity=subscriber_identity,
            subscriber_name=subscriber_name,
            subscriber_description=subscriber_description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8615499628b1f4753ef250f307567474c9df890e5c028af197e02c5372c550c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3790e1b87c269e951008aa5f293e263e93c06977e1eeed2a69dfca58c409514a)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrResourceShareArn")
    def attr_resource_share_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Amazon Security Lake subscriber.

        :cloudformationAttribute: ResourceShareArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceShareArn"))

    @builtins.property
    @jsii.member(jsii_name="attrResourceShareName")
    def attr_resource_share_name(self) -> builtins.str:
        '''The ARN name of the Amazon Security Lake subscriber.

        :cloudformationAttribute: ResourceShareName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceShareName"))

    @builtins.property
    @jsii.member(jsii_name="attrS3BucketArn")
    def attr_s3_bucket_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the S3 bucket.

        :cloudformationAttribute: S3BucketArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrS3BucketArn"))

    @builtins.property
    @jsii.member(jsii_name="attrSubscriberArn")
    def attr_subscriber_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Security Lake subscriber.

        :cloudformationAttribute: SubscriberArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSubscriberArn"))

    @builtins.property
    @jsii.member(jsii_name="attrSubscriberRoleArn")
    def attr_subscriber_role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the role used to create the Security Lake subscriber.

        :cloudformationAttribute: SubscriberRoleArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSubscriberRoleArn"))

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
    @jsii.member(jsii_name="accessTypes")
    def access_types(self) -> typing.List[builtins.str]:
        '''You can choose to notify subscribers of new objects with an Amazon Simple Queue Service (Amazon SQS) queue or through messaging to an HTTPS endpoint provided by the subscriber.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "accessTypes"))

    @access_types.setter
    def access_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f5e7268ca27d6f9f4f7235ed5dc11031e3dcfecbb97acb334a181ffa62b0550)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessTypes", value)

    @builtins.property
    @jsii.member(jsii_name="dataLakeArn")
    def data_lake_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) used to create the data lake.'''
        return typing.cast(builtins.str, jsii.get(self, "dataLakeArn"))

    @data_lake_arn.setter
    def data_lake_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b6df05258f367a78b9fe1e83d93bbb4170db63eebfcfcaf47743e3795fdea19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataLakeArn", value)

    @builtins.property
    @jsii.member(jsii_name="sources")
    def sources(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSubscriber.SourceProperty"]]]:
        '''Amazon Security Lake supports log and event collection for natively supported AWS services .'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSubscriber.SourceProperty"]]], jsii.get(self, "sources"))

    @sources.setter
    def sources(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSubscriber.SourceProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc932de85d8e0823efeb32cd9962639ee0df5d9caf72a0cc1bd8a74abd3853f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sources", value)

    @builtins.property
    @jsii.member(jsii_name="subscriberIdentity")
    def subscriber_identity(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnSubscriber.SubscriberIdentityProperty"]:
        '''The AWS identity used to access your data.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnSubscriber.SubscriberIdentityProperty"], jsii.get(self, "subscriberIdentity"))

    @subscriber_identity.setter
    def subscriber_identity(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnSubscriber.SubscriberIdentityProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__844ac1bd9005c05fc49f39ac053da7c40f778e558a2e4cf96983161b114d88a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscriberIdentity", value)

    @builtins.property
    @jsii.member(jsii_name="subscriberName")
    def subscriber_name(self) -> builtins.str:
        '''The name of your Amazon Security Lake subscriber account.'''
        return typing.cast(builtins.str, jsii.get(self, "subscriberName"))

    @subscriber_name.setter
    def subscriber_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd9beb9187d8345c4ae00d2ee6483cd5f3841d1801dffe9de561ed1934ddd965)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscriberName", value)

    @builtins.property
    @jsii.member(jsii_name="subscriberDescription")
    def subscriber_description(self) -> typing.Optional[builtins.str]:
        '''The subscriber descriptions for a subscriber account.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subscriberDescription"))

    @subscriber_description.setter
    def subscriber_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3147cb4779ff5832faddc8bdeac62a5ff6db17ddc1eddee78b4f5ca463a0ed76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscriberDescription", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of objects, one for each tag to associate with the subscriber.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8f06145c3b30c94dc03a8f547df3132c6f47f465dc815eb5282aab9542906c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securitylake.CfnSubscriber.AwsLogSourceProperty",
        jsii_struct_bases=[],
        name_mapping={"source_name": "sourceName", "source_version": "sourceVersion"},
    )
    class AwsLogSourceProperty:
        def __init__(
            self,
            *,
            source_name: typing.Optional[builtins.str] = None,
            source_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Adds a natively supported AWS service as an Amazon Security Lake source.

            Enables source types for member accounts in required AWS Regions, based on the parameters you specify. You can choose any source type in any Region for either accounts that are part of a trusted organization or standalone accounts. Once you add an AWS service as a source, Security Lake starts collecting logs and events from it.

            :param source_name: Source name of the natively supported AWS service that is supported as an Amazon Security Lake source. For the list of sources supported by Amazon Security Lake see `Collecting data from AWS services <https://docs.aws.amazon.com//security-lake/latest/userguide/internal-sources.html>`_ in the Amazon Security Lake User Guide.
            :param source_version: Source version of the natively supported AWS service that is supported as an Amazon Security Lake source. For more details about source versions supported by Amazon Security Lake see `OCSF source identification <https://docs.aws.amazon.com//security-lake/latest/userguide/open-cybersecurity-schema-framework.html#ocsf-source-identification>`_ in the Amazon Security Lake User Guide.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-subscriber-awslogsource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securitylake as securitylake
                
                aws_log_source_property = securitylake.CfnSubscriber.AwsLogSourceProperty(
                    source_name="sourceName",
                    source_version="sourceVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f7b68bdff72d0a83be28cc208139e37398a7b328722b97984e752440b8b9b167)
                check_type(argname="argument source_name", value=source_name, expected_type=type_hints["source_name"])
                check_type(argname="argument source_version", value=source_version, expected_type=type_hints["source_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if source_name is not None:
                self._values["source_name"] = source_name
            if source_version is not None:
                self._values["source_version"] = source_version

        @builtins.property
        def source_name(self) -> typing.Optional[builtins.str]:
            '''Source name of the natively supported AWS service that is supported as an Amazon Security Lake source.

            For the list of sources supported by Amazon Security Lake see `Collecting data from AWS services <https://docs.aws.amazon.com//security-lake/latest/userguide/internal-sources.html>`_ in the Amazon Security Lake User Guide.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-subscriber-awslogsource.html#cfn-securitylake-subscriber-awslogsource-sourcename
            '''
            result = self._values.get("source_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source_version(self) -> typing.Optional[builtins.str]:
            '''Source version of the natively supported AWS service that is supported as an Amazon Security Lake source.

            For more details about source versions supported by Amazon Security Lake see `OCSF source identification <https://docs.aws.amazon.com//security-lake/latest/userguide/open-cybersecurity-schema-framework.html#ocsf-source-identification>`_ in the Amazon Security Lake User Guide.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-subscriber-awslogsource.html#cfn-securitylake-subscriber-awslogsource-sourceversion
            '''
            result = self._values.get("source_version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AwsLogSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securitylake.CfnSubscriber.CustomLogSourceProperty",
        jsii_struct_bases=[],
        name_mapping={"source_name": "sourceName", "source_version": "sourceVersion"},
    )
    class CustomLogSourceProperty:
        def __init__(
            self,
            *,
            source_name: typing.Optional[builtins.str] = None,
            source_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Third-party custom log source that meets the requirements to be added to Amazon Security Lake .

            For more details, see `Custom log source <https://docs.aws.amazon.com//security-lake/latest/userguide/custom-sources.html#iam-roles-custom-sources>`_ in the *Amazon Security Lake User Guide* .

            :param source_name: The name of the custom log source.
            :param source_version: The source version of the custom log source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-subscriber-customlogsource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securitylake as securitylake
                
                custom_log_source_property = securitylake.CfnSubscriber.CustomLogSourceProperty(
                    source_name="sourceName",
                    source_version="sourceVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__be7ff1808e2250d74fc3f0286676c85a2ac63ab562fb09265ceb5138256bdb3a)
                check_type(argname="argument source_name", value=source_name, expected_type=type_hints["source_name"])
                check_type(argname="argument source_version", value=source_version, expected_type=type_hints["source_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if source_name is not None:
                self._values["source_name"] = source_name
            if source_version is not None:
                self._values["source_version"] = source_version

        @builtins.property
        def source_name(self) -> typing.Optional[builtins.str]:
            '''The name of the custom log source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-subscriber-customlogsource.html#cfn-securitylake-subscriber-customlogsource-sourcename
            '''
            result = self._values.get("source_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source_version(self) -> typing.Optional[builtins.str]:
            '''The source version of the custom log source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-subscriber-customlogsource.html#cfn-securitylake-subscriber-customlogsource-sourceversion
            '''
            result = self._values.get("source_version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomLogSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securitylake.CfnSubscriber.SourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aws_log_source": "awsLogSource",
            "custom_log_source": "customLogSource",
        },
    )
    class SourceProperty:
        def __init__(
            self,
            *,
            aws_log_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSubscriber.AwsLogSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            custom_log_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSubscriber.CustomLogSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Sources are logs and events generated from a single system that match a specific event class in the Open Cybersecurity Schema Framework (OCSF) schema.

            Amazon Security Lake can collect logs and events from a variety of sources, including natively supported AWS services and third-party custom sources.

            :param aws_log_source: The natively supported AWS service which is used a Amazon Security Lake source to collect logs and events from.
            :param custom_log_source: The custom log source AWS which is used a Amazon Security Lake source to collect logs and events from.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-subscriber-source.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securitylake as securitylake
                
                source_property = securitylake.CfnSubscriber.SourceProperty(
                    aws_log_source=securitylake.CfnSubscriber.AwsLogSourceProperty(
                        source_name="sourceName",
                        source_version="sourceVersion"
                    ),
                    custom_log_source=securitylake.CfnSubscriber.CustomLogSourceProperty(
                        source_name="sourceName",
                        source_version="sourceVersion"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__09624bc0a82e7efd60186ff6e6eeff97f2daca3d7d705b8e7e3451a7add8d126)
                check_type(argname="argument aws_log_source", value=aws_log_source, expected_type=type_hints["aws_log_source"])
                check_type(argname="argument custom_log_source", value=custom_log_source, expected_type=type_hints["custom_log_source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if aws_log_source is not None:
                self._values["aws_log_source"] = aws_log_source
            if custom_log_source is not None:
                self._values["custom_log_source"] = custom_log_source

        @builtins.property
        def aws_log_source(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSubscriber.AwsLogSourceProperty"]]:
            '''The natively supported AWS service which is used a Amazon Security Lake source to collect logs and events from.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-subscriber-source.html#cfn-securitylake-subscriber-source-awslogsource
            '''
            result = self._values.get("aws_log_source")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSubscriber.AwsLogSourceProperty"]], result)

        @builtins.property
        def custom_log_source(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSubscriber.CustomLogSourceProperty"]]:
            '''The custom log source AWS which is used a Amazon Security Lake source to collect logs and events from.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-subscriber-source.html#cfn-securitylake-subscriber-source-customlogsource
            '''
            result = self._values.get("custom_log_source")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSubscriber.CustomLogSourceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securitylake.CfnSubscriber.SubscriberIdentityProperty",
        jsii_struct_bases=[],
        name_mapping={"external_id": "externalId", "principal": "principal"},
    )
    class SubscriberIdentityProperty:
        def __init__(
            self,
            *,
            external_id: builtins.str,
            principal: builtins.str,
        ) -> None:
            '''Specify the AWS account ID and external ID that the subscriber will use to access source data.

            :param external_id: The external ID is a unique identifier that the subscriber provides to you.
            :param principal: Principals can include accounts, users, roles, federated users, or AWS services.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-subscriber-subscriberidentity.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securitylake as securitylake
                
                subscriber_identity_property = securitylake.CfnSubscriber.SubscriberIdentityProperty(
                    external_id="externalId",
                    principal="principal"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a2dd3305d7b56ebd933e9b9e7b243865a7a5c734ed08bef308334f82a70d692e)
                check_type(argname="argument external_id", value=external_id, expected_type=type_hints["external_id"])
                check_type(argname="argument principal", value=principal, expected_type=type_hints["principal"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "external_id": external_id,
                "principal": principal,
            }

        @builtins.property
        def external_id(self) -> builtins.str:
            '''The external ID is a unique identifier that the subscriber provides to you.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-subscriber-subscriberidentity.html#cfn-securitylake-subscriber-subscriberidentity-externalid
            '''
            result = self._values.get("external_id")
            assert result is not None, "Required property 'external_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def principal(self) -> builtins.str:
            '''Principals can include accounts, users, roles, federated users, or AWS services.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-subscriber-subscriberidentity.html#cfn-securitylake-subscriber-subscriberidentity-principal
            '''
            result = self._values.get("principal")
            assert result is not None, "Required property 'principal' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubscriberIdentityProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_securitylake.CfnSubscriberProps",
    jsii_struct_bases=[],
    name_mapping={
        "access_types": "accessTypes",
        "data_lake_arn": "dataLakeArn",
        "sources": "sources",
        "subscriber_identity": "subscriberIdentity",
        "subscriber_name": "subscriberName",
        "subscriber_description": "subscriberDescription",
        "tags": "tags",
    },
)
class CfnSubscriberProps:
    def __init__(
        self,
        *,
        access_types: typing.Sequence[builtins.str],
        data_lake_arn: builtins.str,
        sources: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSubscriber.SourceProperty, typing.Dict[builtins.str, typing.Any]]]]],
        subscriber_identity: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSubscriber.SubscriberIdentityProperty, typing.Dict[builtins.str, typing.Any]]],
        subscriber_name: builtins.str,
        subscriber_description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSubscriber``.

        :param access_types: You can choose to notify subscribers of new objects with an Amazon Simple Queue Service (Amazon SQS) queue or through messaging to an HTTPS endpoint provided by the subscriber. Subscribers can consume data by directly querying AWS Lake Formation tables in your Amazon S3 bucket through services like Amazon Athena. This subscription type is defined as ``LAKEFORMATION`` .
        :param data_lake_arn: The Amazon Resource Name (ARN) used to create the data lake.
        :param sources: Amazon Security Lake supports log and event collection for natively supported AWS services . For more information, see the `Amazon Security Lake User Guide <https://docs.aws.amazon.com//security-lake/latest/userguide/source-management.html>`_ .
        :param subscriber_identity: The AWS identity used to access your data.
        :param subscriber_name: The name of your Amazon Security Lake subscriber account.
        :param subscriber_description: The subscriber descriptions for a subscriber account. The description for a subscriber includes ``subscriberName`` , ``accountID`` , ``externalID`` , and ``subscriberId`` .
        :param tags: An array of objects, one for each tag to associate with the subscriber. For each tag, you must specify both a tag key and a tag value. A tag value cannot be null, but it can be an empty string.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securitylake-subscriber.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_securitylake as securitylake
            
            cfn_subscriber_props = securitylake.CfnSubscriberProps(
                access_types=["accessTypes"],
                data_lake_arn="dataLakeArn",
                sources=[securitylake.CfnSubscriber.SourceProperty(
                    aws_log_source=securitylake.CfnSubscriber.AwsLogSourceProperty(
                        source_name="sourceName",
                        source_version="sourceVersion"
                    ),
                    custom_log_source=securitylake.CfnSubscriber.CustomLogSourceProperty(
                        source_name="sourceName",
                        source_version="sourceVersion"
                    )
                )],
                subscriber_identity=securitylake.CfnSubscriber.SubscriberIdentityProperty(
                    external_id="externalId",
                    principal="principal"
                ),
                subscriber_name="subscriberName",
            
                # the properties below are optional
                subscriber_description="subscriberDescription",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48b4dffc39d9aeba296ada6ed3b12f7273758033f731faa94da735c639fb2f10)
            check_type(argname="argument access_types", value=access_types, expected_type=type_hints["access_types"])
            check_type(argname="argument data_lake_arn", value=data_lake_arn, expected_type=type_hints["data_lake_arn"])
            check_type(argname="argument sources", value=sources, expected_type=type_hints["sources"])
            check_type(argname="argument subscriber_identity", value=subscriber_identity, expected_type=type_hints["subscriber_identity"])
            check_type(argname="argument subscriber_name", value=subscriber_name, expected_type=type_hints["subscriber_name"])
            check_type(argname="argument subscriber_description", value=subscriber_description, expected_type=type_hints["subscriber_description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_types": access_types,
            "data_lake_arn": data_lake_arn,
            "sources": sources,
            "subscriber_identity": subscriber_identity,
            "subscriber_name": subscriber_name,
        }
        if subscriber_description is not None:
            self._values["subscriber_description"] = subscriber_description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def access_types(self) -> typing.List[builtins.str]:
        '''You can choose to notify subscribers of new objects with an Amazon Simple Queue Service (Amazon SQS) queue or through messaging to an HTTPS endpoint provided by the subscriber.

        Subscribers can consume data by directly querying AWS Lake Formation tables in your Amazon S3 bucket through services like Amazon Athena. This subscription type is defined as ``LAKEFORMATION`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securitylake-subscriber.html#cfn-securitylake-subscriber-accesstypes
        '''
        result = self._values.get("access_types")
        assert result is not None, "Required property 'access_types' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def data_lake_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) used to create the data lake.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securitylake-subscriber.html#cfn-securitylake-subscriber-datalakearn
        '''
        result = self._values.get("data_lake_arn")
        assert result is not None, "Required property 'data_lake_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sources(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnSubscriber.SourceProperty]]]:
        '''Amazon Security Lake supports log and event collection for natively supported AWS services .

        For more information, see the `Amazon Security Lake User Guide <https://docs.aws.amazon.com//security-lake/latest/userguide/source-management.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securitylake-subscriber.html#cfn-securitylake-subscriber-sources
        '''
        result = self._values.get("sources")
        assert result is not None, "Required property 'sources' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnSubscriber.SourceProperty]]], result)

    @builtins.property
    def subscriber_identity(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnSubscriber.SubscriberIdentityProperty]:
        '''The AWS identity used to access your data.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securitylake-subscriber.html#cfn-securitylake-subscriber-subscriberidentity
        '''
        result = self._values.get("subscriber_identity")
        assert result is not None, "Required property 'subscriber_identity' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnSubscriber.SubscriberIdentityProperty], result)

    @builtins.property
    def subscriber_name(self) -> builtins.str:
        '''The name of your Amazon Security Lake subscriber account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securitylake-subscriber.html#cfn-securitylake-subscriber-subscribername
        '''
        result = self._values.get("subscriber_name")
        assert result is not None, "Required property 'subscriber_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subscriber_description(self) -> typing.Optional[builtins.str]:
        '''The subscriber descriptions for a subscriber account.

        The description for a subscriber includes ``subscriberName`` , ``accountID`` , ``externalID`` , and ``subscriberId`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securitylake-subscriber.html#cfn-securitylake-subscriber-subscriberdescription
        '''
        result = self._values.get("subscriber_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of objects, one for each tag to associate with the subscriber.

        For each tag, you must specify both a tag key and a tag value. A tag value cannot be null, but it can be an empty string.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securitylake-subscriber.html#cfn-securitylake-subscriber-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSubscriberProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAwsLogSource",
    "CfnAwsLogSourceProps",
    "CfnDataLake",
    "CfnDataLakeProps",
    "CfnSubscriber",
    "CfnSubscriberProps",
]

publication.publish()

def _typecheckingstub__c67fc1d68d61ef9dead7d443499c1a142da192386efc06474b3758994937de6b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    data_lake_arn: builtins.str,
    source_name: builtins.str,
    source_version: builtins.str,
    accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f493097d98865e82cabeeb80dd31577169140709170903a313d3bc579da5bcb(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4b08275c623e99b1c0cca9f7d97a78cf719804d590ae90e5af151255c42753a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed09f296c9b906f7011ea796fce3b42122e1c0490eb544e941f5953a5b0f8403(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__786699bc5ed670115ad16fc2d5cab658ddb4c20d9afccc0010adb67c796143ba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2369f0ca541c99625731d8a7db77fa2a9f1346eab63190644c2695d471ddda46(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1f564a49d096390f47538b02cc909d2927202e7d6b998b761aaf21810dcf11c(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56ae11383caeefb7587043503a4fd999d42e30184765bd5e736dcae60c5b3b94(
    *,
    data_lake_arn: builtins.str,
    source_name: builtins.str,
    source_version: builtins.str,
    accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff487a50882ee11f396717fb970b445f3274af88108d1c1d390543dfb1fdf534(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLake.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    lifecycle_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLake.LifecycleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    meta_store_manager_role_arn: typing.Optional[builtins.str] = None,
    replication_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLake.ReplicationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d7a1c25528114b19a22f7fe9e5b4213f46c37e16f22245bc3dc38ad34fc7ef6(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb852df583c773c6f5d30c27afae6f598c8606ae40f25dd1885d8fbf5013661b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12edf08ab82b633325fe7034b3424955ea7bff566dfa00928107723a5d0f6a72(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataLake.EncryptionConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__916659d1bcdf1d6d40de689f3b334b766e1a8fb681a493926742e61ce5ba40b7(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataLake.LifecycleConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23cd82335763114e4ff9c52f4ff2b4db4b4be68cc8f5b468e1325fa0e0e79558(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__647257bd68002b29a89b3128d4883d0c748e98d2c70a5b154446993271225230(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataLake.ReplicationConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6654ce3b2fa02feedc8f03797f96ae7270d4bd79ef3c3791b522e8277fa3798c(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c697088167e83d968076432c9f71877137655465afc625784270e3ba40d3f57b(
    *,
    kms_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__676fee3c866c464d5b150fd2a1553faf30ba52129224b9869203f21574e77d9f(
    *,
    days: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09cd166ed037b2c00b8a44dc0e94832b0851b09edc3ca5e9ac0de67068729149(
    *,
    expiration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLake.ExpirationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    transitions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLake.TransitionsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5e309ce471c0b5b94d10c5cf8d75ece96a70a7112aa8396372449cae02d7005(
    *,
    regions: typing.Optional[typing.Sequence[builtins.str]] = None,
    role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aaac67133f980ed118f75aa7447b8e2c8f6a4e8d8fce97491e407d04b2924302(
    *,
    days: typing.Optional[jsii.Number] = None,
    storage_class: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f98044af937b493e98dc654fc28cbeccbd1ee2f339cd00c1cc59056847b8fb37(
    *,
    encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLake.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    lifecycle_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLake.LifecycleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    meta_store_manager_role_arn: typing.Optional[builtins.str] = None,
    replication_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLake.ReplicationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cfdc1f6a6f3c553e914b6e8b917c7abd1db0a1142db24f189c29526acaaea39(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    access_types: typing.Sequence[builtins.str],
    data_lake_arn: builtins.str,
    sources: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSubscriber.SourceProperty, typing.Dict[builtins.str, typing.Any]]]]],
    subscriber_identity: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSubscriber.SubscriberIdentityProperty, typing.Dict[builtins.str, typing.Any]]],
    subscriber_name: builtins.str,
    subscriber_description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8615499628b1f4753ef250f307567474c9df890e5c028af197e02c5372c550c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3790e1b87c269e951008aa5f293e263e93c06977e1eeed2a69dfca58c409514a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f5e7268ca27d6f9f4f7235ed5dc11031e3dcfecbb97acb334a181ffa62b0550(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b6df05258f367a78b9fe1e83d93bbb4170db63eebfcfcaf47743e3795fdea19(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc932de85d8e0823efeb32cd9962639ee0df5d9caf72a0cc1bd8a74abd3853f1(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnSubscriber.SourceProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__844ac1bd9005c05fc49f39ac053da7c40f778e558a2e4cf96983161b114d88a7(
    value: typing.Union[_IResolvable_da3f097b, CfnSubscriber.SubscriberIdentityProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd9beb9187d8345c4ae00d2ee6483cd5f3841d1801dffe9de561ed1934ddd965(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3147cb4779ff5832faddc8bdeac62a5ff6db17ddc1eddee78b4f5ca463a0ed76(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8f06145c3b30c94dc03a8f547df3132c6f47f465dc815eb5282aab9542906c1(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7b68bdff72d0a83be28cc208139e37398a7b328722b97984e752440b8b9b167(
    *,
    source_name: typing.Optional[builtins.str] = None,
    source_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be7ff1808e2250d74fc3f0286676c85a2ac63ab562fb09265ceb5138256bdb3a(
    *,
    source_name: typing.Optional[builtins.str] = None,
    source_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09624bc0a82e7efd60186ff6e6eeff97f2daca3d7d705b8e7e3451a7add8d126(
    *,
    aws_log_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSubscriber.AwsLogSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    custom_log_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSubscriber.CustomLogSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2dd3305d7b56ebd933e9b9e7b243865a7a5c734ed08bef308334f82a70d692e(
    *,
    external_id: builtins.str,
    principal: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48b4dffc39d9aeba296ada6ed3b12f7273758033f731faa94da735c639fb2f10(
    *,
    access_types: typing.Sequence[builtins.str],
    data_lake_arn: builtins.str,
    sources: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSubscriber.SourceProperty, typing.Dict[builtins.str, typing.Any]]]]],
    subscriber_identity: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSubscriber.SubscriberIdentityProperty, typing.Dict[builtins.str, typing.Any]]],
    subscriber_name: builtins.str,
    subscriber_description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
