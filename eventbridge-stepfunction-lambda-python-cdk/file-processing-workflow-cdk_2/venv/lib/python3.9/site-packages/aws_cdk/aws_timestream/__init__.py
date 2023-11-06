'''
# AWS::Timestream Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_timestream as timestream
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Timestream construct libraries](https://constructs.dev/search?q=timestream)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Timestream resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Timestream.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Timestream](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Timestream.html).

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
class CfnDatabase(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_timestream.CfnDatabase",
):
    '''Creates a new Timestream database.

    If the AWS KMS key is not specified, the database will be encrypted with a Timestream managed AWS KMS key located in your account. Refer to `AWS managed AWS KMS keys <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk>`_ for more info. `Service quotas apply <https://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html>`_ . See `code sample <https://docs.aws.amazon.com/timestream/latest/developerguide/code-samples.create-db.html>`_ for details.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-database.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_timestream as timestream
        
        cfn_database = timestream.CfnDatabase(self, "MyCfnDatabase",
            database_name="databaseName",
            kms_key_id="kmsKeyId",
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
        database_name: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param database_name: The name of the Timestream database. *Length Constraints* : Minimum length of 3 bytes. Maximum length of 256 bytes.
        :param kms_key_id: The identifier of the AWS KMS key used to encrypt the data stored in the database.
        :param tags: The tags to add to the database.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df267d6c98734bb503e076f315371b3537a6654cdfd5246386d41db61b38fa31)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDatabaseProps(
            database_name=database_name, kms_key_id=kms_key_id, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9baaa3cf10dd12d7584c82547f4f62f6168d3a70bb84280e11437c6f39e056e8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__38f97f8e45b06461dc33c410476a8c6ab5fd5787cafd00019e0a1873cdf9996b)
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
        '''The ``arn`` of the database.

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
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> typing.Optional[builtins.str]:
        '''The name of the Timestream database.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cbde3c6f76ec33728e8896f7456e86f8a746129259457fcb60defa5e1d7bdf3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of the AWS KMS key used to encrypt the data stored in the database.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a88a8e589058995e4c9588f4cb113f823707014eb42119b90c9719e50cb390e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to add to the database.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c161fd44298031bcce0863494a5d3a09a73703fe8c50ee977b03cbe4cab5d4a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_timestream.CfnDatabaseProps",
    jsii_struct_bases=[],
    name_mapping={
        "database_name": "databaseName",
        "kms_key_id": "kmsKeyId",
        "tags": "tags",
    },
)
class CfnDatabaseProps:
    def __init__(
        self,
        *,
        database_name: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDatabase``.

        :param database_name: The name of the Timestream database. *Length Constraints* : Minimum length of 3 bytes. Maximum length of 256 bytes.
        :param kms_key_id: The identifier of the AWS KMS key used to encrypt the data stored in the database.
        :param tags: The tags to add to the database.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-database.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_timestream as timestream
            
            cfn_database_props = timestream.CfnDatabaseProps(
                database_name="databaseName",
                kms_key_id="kmsKeyId",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fffb8befe8374295020dd254ed0c77820bb26fc0d94c59e0a34f89d6fb3f295c)
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if database_name is not None:
            self._values["database_name"] = database_name
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def database_name(self) -> typing.Optional[builtins.str]:
        '''The name of the Timestream database.

        *Length Constraints* : Minimum length of 3 bytes. Maximum length of 256 bytes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-database.html#cfn-timestream-database-databasename
        '''
        result = self._values.get("database_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of the AWS KMS key used to encrypt the data stored in the database.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-database.html#cfn-timestream-database-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to add to the database.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-database.html#cfn-timestream-database-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDatabaseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnScheduledQuery(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_timestream.CfnScheduledQuery",
):
    '''Create a scheduled query that will be run on your behalf at the configured schedule.

    Timestream assumes the execution role provided as part of the ``ScheduledQueryExecutionRoleArn`` parameter to run the query. You can use the ``NotificationConfiguration`` parameter to configure notification for your scheduled query operations.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-scheduledquery.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_timestream as timestream
        
        cfn_scheduled_query = timestream.CfnScheduledQuery(self, "MyCfnScheduledQuery",
            error_report_configuration=timestream.CfnScheduledQuery.ErrorReportConfigurationProperty(
                s3_configuration=timestream.CfnScheduledQuery.S3ConfigurationProperty(
                    bucket_name="bucketName",
        
                    # the properties below are optional
                    encryption_option="encryptionOption",
                    object_key_prefix="objectKeyPrefix"
                )
            ),
            notification_configuration=timestream.CfnScheduledQuery.NotificationConfigurationProperty(
                sns_configuration=timestream.CfnScheduledQuery.SnsConfigurationProperty(
                    topic_arn="topicArn"
                )
            ),
            query_string="queryString",
            schedule_configuration=timestream.CfnScheduledQuery.ScheduleConfigurationProperty(
                schedule_expression="scheduleExpression"
            ),
            scheduled_query_execution_role_arn="scheduledQueryExecutionRoleArn",
        
            # the properties below are optional
            client_token="clientToken",
            kms_key_id="kmsKeyId",
            scheduled_query_name="scheduledQueryName",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            target_configuration=timestream.CfnScheduledQuery.TargetConfigurationProperty(
                timestream_configuration=timestream.CfnScheduledQuery.TimestreamConfigurationProperty(
                    database_name="databaseName",
                    dimension_mappings=[timestream.CfnScheduledQuery.DimensionMappingProperty(
                        dimension_value_type="dimensionValueType",
                        name="name"
                    )],
                    table_name="tableName",
                    time_column="timeColumn",
        
                    # the properties below are optional
                    measure_name_column="measureNameColumn",
                    mixed_measure_mappings=[timestream.CfnScheduledQuery.MixedMeasureMappingProperty(
                        measure_value_type="measureValueType",
        
                        # the properties below are optional
                        measure_name="measureName",
                        multi_measure_attribute_mappings=[timestream.CfnScheduledQuery.MultiMeasureAttributeMappingProperty(
                            measure_value_type="measureValueType",
                            source_column="sourceColumn",
        
                            # the properties below are optional
                            target_multi_measure_attribute_name="targetMultiMeasureAttributeName"
                        )],
                        source_column="sourceColumn",
                        target_measure_name="targetMeasureName"
                    )],
                    multi_measure_mappings=timestream.CfnScheduledQuery.MultiMeasureMappingsProperty(
                        multi_measure_attribute_mappings=[timestream.CfnScheduledQuery.MultiMeasureAttributeMappingProperty(
                            measure_value_type="measureValueType",
                            source_column="sourceColumn",
        
                            # the properties below are optional
                            target_multi_measure_attribute_name="targetMultiMeasureAttributeName"
                        )],
        
                        # the properties below are optional
                        target_multi_measure_name="targetMultiMeasureName"
                    )
                )
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        error_report_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnScheduledQuery.ErrorReportConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        notification_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnScheduledQuery.NotificationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        query_string: builtins.str,
        schedule_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnScheduledQuery.ScheduleConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        scheduled_query_execution_role_arn: builtins.str,
        client_token: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        scheduled_query_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        target_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnScheduledQuery.TargetConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param error_report_configuration: Configuration for error reporting. Error reports will be generated when a problem is encountered when writing the query results.
        :param notification_configuration: Notification configuration for the scheduled query. A notification is sent by Timestream when a query run finishes, when the state is updated or when you delete it.
        :param query_string: The query string to run. Parameter names can be specified in the query string ``@`` character followed by an identifier. The named Parameter ``@scheduled_runtime`` is reserved and can be used in the query to get the time at which the query is scheduled to run. The timestamp calculated according to the ScheduleConfiguration parameter, will be the value of ``@scheduled_runtime`` paramater for each query run. For example, consider an instance of a scheduled query executing on 2021-12-01 00:00:00. For this instance, the ``@scheduled_runtime`` parameter is initialized to the timestamp 2021-12-01 00:00:00 when invoking the query.
        :param schedule_configuration: Schedule configuration.
        :param scheduled_query_execution_role_arn: The ARN for the IAM role that Timestream will assume when running the scheduled query.
        :param client_token: Using a ClientToken makes the call to CreateScheduledQuery idempotent, in other words, making the same request repeatedly will produce the same result. Making multiple identical CreateScheduledQuery requests has the same effect as making a single request. - If CreateScheduledQuery is called without a ``ClientToken`` , the Query SDK generates a ``ClientToken`` on your behalf. - After 8 hours, any request with the same ``ClientToken`` is treated as a new request.
        :param kms_key_id: The Amazon KMS key used to encrypt the scheduled query resource, at-rest. If the Amazon KMS key is not specified, the scheduled query resource will be encrypted with a Timestream owned Amazon KMS key. To specify a KMS key, use the key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix the name with *alias/* If ErrorReportConfiguration uses ``SSE_KMS`` as encryption type, the same KmsKeyId is used to encrypt the error report at rest.
        :param scheduled_query_name: A name for the query. Scheduled query names must be unique within each Region.
        :param tags: A list of key-value pairs to label the scheduled query.
        :param target_configuration: Scheduled query target store configuration.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17cb9c0ebf2969eb32b3d5921e02d6b922a461b4f7becdb1bf28f83cb9407cfa)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnScheduledQueryProps(
            error_report_configuration=error_report_configuration,
            notification_configuration=notification_configuration,
            query_string=query_string,
            schedule_configuration=schedule_configuration,
            scheduled_query_execution_role_arn=scheduled_query_execution_role_arn,
            client_token=client_token,
            kms_key_id=kms_key_id,
            scheduled_query_name=scheduled_query_name,
            tags=tags,
            target_configuration=target_configuration,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42e5a389d6d8bd3d1ce3b11086466e67d628325755910bd1a3c548b00ffcfe93)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8bc8011b2365888fe7a380f1ba5a36fb7ed1f8000d3f7bb10b1d7f0cea6ee8ce)
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
        '''The ``ARN`` of the scheduled query.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrSqErrorReportConfiguration")
    def attr_sq_error_report_configuration(self) -> builtins.str:
        '''The scheduled query error reporting configuration.

        :cloudformationAttribute: SQErrorReportConfiguration
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSqErrorReportConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="attrSqKmsKeyId")
    def attr_sq_kms_key_id(self) -> builtins.str:
        '''The KMS key used to encrypt the query resource, if a customer managed KMS key was provided.

        :cloudformationAttribute: SQKmsKeyId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSqKmsKeyId"))

    @builtins.property
    @jsii.member(jsii_name="attrSqName")
    def attr_sq_name(self) -> builtins.str:
        '''The scheduled query name.

        :cloudformationAttribute: SQName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSqName"))

    @builtins.property
    @jsii.member(jsii_name="attrSqNotificationConfiguration")
    def attr_sq_notification_configuration(self) -> builtins.str:
        '''The scheduled query notification configuration.

        :cloudformationAttribute: SQNotificationConfiguration
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSqNotificationConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="attrSqQueryString")
    def attr_sq_query_string(self) -> builtins.str:
        '''The scheduled query string..

        :cloudformationAttribute: SQQueryString
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSqQueryString"))

    @builtins.property
    @jsii.member(jsii_name="attrSqScheduleConfiguration")
    def attr_sq_schedule_configuration(self) -> builtins.str:
        '''The scheduled query schedule configuration.

        :cloudformationAttribute: SQScheduleConfiguration
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSqScheduleConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="attrSqScheduledQueryExecutionRoleArn")
    def attr_sq_scheduled_query_execution_role_arn(self) -> builtins.str:
        '''The ARN of the IAM role that will be used by Timestream to run the query.

        :cloudformationAttribute: SQScheduledQueryExecutionRoleArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSqScheduledQueryExecutionRoleArn"))

    @builtins.property
    @jsii.member(jsii_name="attrSqTargetConfiguration")
    def attr_sq_target_configuration(self) -> builtins.str:
        '''The configuration for query output.

        :cloudformationAttribute: SQTargetConfiguration
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSqTargetConfiguration"))

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
    @jsii.member(jsii_name="errorReportConfiguration")
    def error_report_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnScheduledQuery.ErrorReportConfigurationProperty"]:
        '''Configuration for error reporting.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnScheduledQuery.ErrorReportConfigurationProperty"], jsii.get(self, "errorReportConfiguration"))

    @error_report_configuration.setter
    def error_report_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnScheduledQuery.ErrorReportConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb7defeed6aa22df8fac8ffd2a8a11911c1c98afe084e662220ea2d6b749cf6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "errorReportConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="notificationConfiguration")
    def notification_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnScheduledQuery.NotificationConfigurationProperty"]:
        '''Notification configuration for the scheduled query.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnScheduledQuery.NotificationConfigurationProperty"], jsii.get(self, "notificationConfiguration"))

    @notification_configuration.setter
    def notification_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnScheduledQuery.NotificationConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6ac8f7698b5772e1a500b55701a8ec9f78516f145d63622ae68a8e5545f29e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="queryString")
    def query_string(self) -> builtins.str:
        '''The query string to run.'''
        return typing.cast(builtins.str, jsii.get(self, "queryString"))

    @query_string.setter
    def query_string(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__350bef101d4375adfdded124038da261adba0b0cd8ff0163079f9a3e4ab2fa36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryString", value)

    @builtins.property
    @jsii.member(jsii_name="scheduleConfiguration")
    def schedule_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnScheduledQuery.ScheduleConfigurationProperty"]:
        '''Schedule configuration.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnScheduledQuery.ScheduleConfigurationProperty"], jsii.get(self, "scheduleConfiguration"))

    @schedule_configuration.setter
    def schedule_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnScheduledQuery.ScheduleConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__879b9ea129031bffd99904fa4ee3a65eea8e9b9983d6d2765f67314bbc2a58e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduleConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="scheduledQueryExecutionRoleArn")
    def scheduled_query_execution_role_arn(self) -> builtins.str:
        '''The ARN for the IAM role that Timestream will assume when running the scheduled query.'''
        return typing.cast(builtins.str, jsii.get(self, "scheduledQueryExecutionRoleArn"))

    @scheduled_query_execution_role_arn.setter
    def scheduled_query_execution_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9604d93296dd77d676d4aaee7f32cfff5d41a5a5ddea40af8a47241cc11bc24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduledQueryExecutionRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="clientToken")
    def client_token(self) -> typing.Optional[builtins.str]:
        '''Using a ClientToken makes the call to CreateScheduledQuery idempotent, in other words, making the same request repeatedly will produce the same result.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientToken"))

    @client_token.setter
    def client_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b0dd0e140b14315dea4d20b97d7e43e67078325c22af76b9335246185be1bf2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientToken", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The Amazon KMS key used to encrypt the scheduled query resource, at-rest.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e3fb74e7cb6c02c6c793efc3b537bfb39626eef1e4b767afbb9f9aefb9b9609)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="scheduledQueryName")
    def scheduled_query_name(self) -> typing.Optional[builtins.str]:
        '''A name for the query.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduledQueryName"))

    @scheduled_query_name.setter
    def scheduled_query_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1d37c1a239896519d1c42b63f110aa1c29f1bf41df02b83bbe8b432c63d000a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduledQueryName", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs to label the scheduled query.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce0d7d8459caf5a03fcbc9365acf392dda9e2785efecf27982e7378d5a93921b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="targetConfiguration")
    def target_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScheduledQuery.TargetConfigurationProperty"]]:
        '''Scheduled query target store configuration.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScheduledQuery.TargetConfigurationProperty"]], jsii.get(self, "targetConfiguration"))

    @target_configuration.setter
    def target_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScheduledQuery.TargetConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b44979dc34f6dc90d3fdf79577b6e0af6fc57980ca3d0760ff21b0db7ea27c39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetConfiguration", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_timestream.CfnScheduledQuery.DimensionMappingProperty",
        jsii_struct_bases=[],
        name_mapping={"dimension_value_type": "dimensionValueType", "name": "name"},
    )
    class DimensionMappingProperty:
        def __init__(
            self,
            *,
            dimension_value_type: builtins.str,
            name: builtins.str,
        ) -> None:
            '''This type is used to map column(s) from the query result to a dimension in the destination table.

            :param dimension_value_type: Type for the dimension: VARCHAR.
            :param name: Column name from query result.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-dimensionmapping.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_timestream as timestream
                
                dimension_mapping_property = timestream.CfnScheduledQuery.DimensionMappingProperty(
                    dimension_value_type="dimensionValueType",
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__777d29ff1772204d748efd0bdbbc3a0cc79f8df893bb747ef6f3ff489ce7b0a8)
                check_type(argname="argument dimension_value_type", value=dimension_value_type, expected_type=type_hints["dimension_value_type"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "dimension_value_type": dimension_value_type,
                "name": name,
            }

        @builtins.property
        def dimension_value_type(self) -> builtins.str:
            '''Type for the dimension: VARCHAR.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-dimensionmapping.html#cfn-timestream-scheduledquery-dimensionmapping-dimensionvaluetype
            '''
            result = self._values.get("dimension_value_type")
            assert result is not None, "Required property 'dimension_value_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''Column name from query result.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-dimensionmapping.html#cfn-timestream-scheduledquery-dimensionmapping-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DimensionMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_timestream.CfnScheduledQuery.ErrorReportConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_configuration": "s3Configuration"},
    )
    class ErrorReportConfigurationProperty:
        def __init__(
            self,
            *,
            s3_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnScheduledQuery.S3ConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Configuration required for error reporting.

            :param s3_configuration: The S3 configuration for the error reports.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-errorreportconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_timestream as timestream
                
                error_report_configuration_property = timestream.CfnScheduledQuery.ErrorReportConfigurationProperty(
                    s3_configuration=timestream.CfnScheduledQuery.S3ConfigurationProperty(
                        bucket_name="bucketName",
                
                        # the properties below are optional
                        encryption_option="encryptionOption",
                        object_key_prefix="objectKeyPrefix"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7fe12737c843bf8018d182ab621e156cd06646166dd75ee81f8ef4a09be3743a)
                check_type(argname="argument s3_configuration", value=s3_configuration, expected_type=type_hints["s3_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "s3_configuration": s3_configuration,
            }

        @builtins.property
        def s3_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnScheduledQuery.S3ConfigurationProperty"]:
            '''The S3 configuration for the error reports.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-errorreportconfiguration.html#cfn-timestream-scheduledquery-errorreportconfiguration-s3configuration
            '''
            result = self._values.get("s3_configuration")
            assert result is not None, "Required property 's3_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnScheduledQuery.S3ConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ErrorReportConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_timestream.CfnScheduledQuery.MixedMeasureMappingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "measure_value_type": "measureValueType",
            "measure_name": "measureName",
            "multi_measure_attribute_mappings": "multiMeasureAttributeMappings",
            "source_column": "sourceColumn",
            "target_measure_name": "targetMeasureName",
        },
    )
    class MixedMeasureMappingProperty:
        def __init__(
            self,
            *,
            measure_value_type: builtins.str,
            measure_name: typing.Optional[builtins.str] = None,
            multi_measure_attribute_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnScheduledQuery.MultiMeasureAttributeMappingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            source_column: typing.Optional[builtins.str] = None,
            target_measure_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''MixedMeasureMappings are mappings that can be used to ingest data into a mixture of narrow and multi measures in the derived table.

            :param measure_value_type: Type of the value that is to be read from sourceColumn. If the mapping is for MULTI, use MeasureValueType.MULTI.
            :param measure_name: Refers to the value of measure_name in a result row. This field is required if MeasureNameColumn is provided.
            :param multi_measure_attribute_mappings: Required when measureValueType is MULTI. Attribute mappings for MULTI value measures.
            :param source_column: This field refers to the source column from which measure-value is to be read for result materialization.
            :param target_measure_name: Target measure name to be used. If not provided, the target measure name by default would be measure-name if provided, or sourceColumn otherwise.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-mixedmeasuremapping.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_timestream as timestream
                
                mixed_measure_mapping_property = timestream.CfnScheduledQuery.MixedMeasureMappingProperty(
                    measure_value_type="measureValueType",
                
                    # the properties below are optional
                    measure_name="measureName",
                    multi_measure_attribute_mappings=[timestream.CfnScheduledQuery.MultiMeasureAttributeMappingProperty(
                        measure_value_type="measureValueType",
                        source_column="sourceColumn",
                
                        # the properties below are optional
                        target_multi_measure_attribute_name="targetMultiMeasureAttributeName"
                    )],
                    source_column="sourceColumn",
                    target_measure_name="targetMeasureName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__86791c8890b0bf1d095da076392a23e4f575ec15705a623918aae1c043d36c5b)
                check_type(argname="argument measure_value_type", value=measure_value_type, expected_type=type_hints["measure_value_type"])
                check_type(argname="argument measure_name", value=measure_name, expected_type=type_hints["measure_name"])
                check_type(argname="argument multi_measure_attribute_mappings", value=multi_measure_attribute_mappings, expected_type=type_hints["multi_measure_attribute_mappings"])
                check_type(argname="argument source_column", value=source_column, expected_type=type_hints["source_column"])
                check_type(argname="argument target_measure_name", value=target_measure_name, expected_type=type_hints["target_measure_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "measure_value_type": measure_value_type,
            }
            if measure_name is not None:
                self._values["measure_name"] = measure_name
            if multi_measure_attribute_mappings is not None:
                self._values["multi_measure_attribute_mappings"] = multi_measure_attribute_mappings
            if source_column is not None:
                self._values["source_column"] = source_column
            if target_measure_name is not None:
                self._values["target_measure_name"] = target_measure_name

        @builtins.property
        def measure_value_type(self) -> builtins.str:
            '''Type of the value that is to be read from sourceColumn.

            If the mapping is for MULTI, use MeasureValueType.MULTI.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-mixedmeasuremapping.html#cfn-timestream-scheduledquery-mixedmeasuremapping-measurevaluetype
            '''
            result = self._values.get("measure_value_type")
            assert result is not None, "Required property 'measure_value_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def measure_name(self) -> typing.Optional[builtins.str]:
            '''Refers to the value of measure_name in a result row.

            This field is required if MeasureNameColumn is provided.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-mixedmeasuremapping.html#cfn-timestream-scheduledquery-mixedmeasuremapping-measurename
            '''
            result = self._values.get("measure_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def multi_measure_attribute_mappings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnScheduledQuery.MultiMeasureAttributeMappingProperty"]]]]:
            '''Required when measureValueType is MULTI.

            Attribute mappings for MULTI value measures.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-mixedmeasuremapping.html#cfn-timestream-scheduledquery-mixedmeasuremapping-multimeasureattributemappings
            '''
            result = self._values.get("multi_measure_attribute_mappings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnScheduledQuery.MultiMeasureAttributeMappingProperty"]]]], result)

        @builtins.property
        def source_column(self) -> typing.Optional[builtins.str]:
            '''This field refers to the source column from which measure-value is to be read for result materialization.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-mixedmeasuremapping.html#cfn-timestream-scheduledquery-mixedmeasuremapping-sourcecolumn
            '''
            result = self._values.get("source_column")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_measure_name(self) -> typing.Optional[builtins.str]:
            '''Target measure name to be used.

            If not provided, the target measure name by default would be measure-name if provided, or sourceColumn otherwise.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-mixedmeasuremapping.html#cfn-timestream-scheduledquery-mixedmeasuremapping-targetmeasurename
            '''
            result = self._values.get("target_measure_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MixedMeasureMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_timestream.CfnScheduledQuery.MultiMeasureAttributeMappingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "measure_value_type": "measureValueType",
            "source_column": "sourceColumn",
            "target_multi_measure_attribute_name": "targetMultiMeasureAttributeName",
        },
    )
    class MultiMeasureAttributeMappingProperty:
        def __init__(
            self,
            *,
            measure_value_type: builtins.str,
            source_column: builtins.str,
            target_multi_measure_attribute_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Attribute mapping for MULTI value measures.

            :param measure_value_type: Type of the attribute to be read from the source column.
            :param source_column: Source column from where the attribute value is to be read.
            :param target_multi_measure_attribute_name: Custom name to be used for attribute name in derived table. If not provided, source column name would be used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-multimeasureattributemapping.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_timestream as timestream
                
                multi_measure_attribute_mapping_property = timestream.CfnScheduledQuery.MultiMeasureAttributeMappingProperty(
                    measure_value_type="measureValueType",
                    source_column="sourceColumn",
                
                    # the properties below are optional
                    target_multi_measure_attribute_name="targetMultiMeasureAttributeName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ee03ab7385a70723437ab533f3015a5bf3d91b15c5a09b8c34da5d1ea264dc65)
                check_type(argname="argument measure_value_type", value=measure_value_type, expected_type=type_hints["measure_value_type"])
                check_type(argname="argument source_column", value=source_column, expected_type=type_hints["source_column"])
                check_type(argname="argument target_multi_measure_attribute_name", value=target_multi_measure_attribute_name, expected_type=type_hints["target_multi_measure_attribute_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "measure_value_type": measure_value_type,
                "source_column": source_column,
            }
            if target_multi_measure_attribute_name is not None:
                self._values["target_multi_measure_attribute_name"] = target_multi_measure_attribute_name

        @builtins.property
        def measure_value_type(self) -> builtins.str:
            '''Type of the attribute to be read from the source column.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-multimeasureattributemapping.html#cfn-timestream-scheduledquery-multimeasureattributemapping-measurevaluetype
            '''
            result = self._values.get("measure_value_type")
            assert result is not None, "Required property 'measure_value_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source_column(self) -> builtins.str:
            '''Source column from where the attribute value is to be read.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-multimeasureattributemapping.html#cfn-timestream-scheduledquery-multimeasureattributemapping-sourcecolumn
            '''
            result = self._values.get("source_column")
            assert result is not None, "Required property 'source_column' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def target_multi_measure_attribute_name(self) -> typing.Optional[builtins.str]:
            '''Custom name to be used for attribute name in derived table.

            If not provided, source column name would be used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-multimeasureattributemapping.html#cfn-timestream-scheduledquery-multimeasureattributemapping-targetmultimeasureattributename
            '''
            result = self._values.get("target_multi_measure_attribute_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MultiMeasureAttributeMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_timestream.CfnScheduledQuery.MultiMeasureMappingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "multi_measure_attribute_mappings": "multiMeasureAttributeMappings",
            "target_multi_measure_name": "targetMultiMeasureName",
        },
    )
    class MultiMeasureMappingsProperty:
        def __init__(
            self,
            *,
            multi_measure_attribute_mappings: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnScheduledQuery.MultiMeasureAttributeMappingProperty", typing.Dict[builtins.str, typing.Any]]]]],
            target_multi_measure_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Only one of MixedMeasureMappings or MultiMeasureMappings is to be provided.

            MultiMeasureMappings can be used to ingest data as multi measures in the derived table.

            :param multi_measure_attribute_mappings: Required. Attribute mappings to be used for mapping query results to ingest data for multi-measure attributes.
            :param target_multi_measure_name: The name of the target multi-measure name in the derived table. This input is required when measureNameColumn is not provided. If MeasureNameColumn is provided, then value from that column will be used as multi-measure name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-multimeasuremappings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_timestream as timestream
                
                multi_measure_mappings_property = timestream.CfnScheduledQuery.MultiMeasureMappingsProperty(
                    multi_measure_attribute_mappings=[timestream.CfnScheduledQuery.MultiMeasureAttributeMappingProperty(
                        measure_value_type="measureValueType",
                        source_column="sourceColumn",
                
                        # the properties below are optional
                        target_multi_measure_attribute_name="targetMultiMeasureAttributeName"
                    )],
                
                    # the properties below are optional
                    target_multi_measure_name="targetMultiMeasureName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__62c61c58c8fd4b88c107b94c840d9e4d63330934b833fb6af43a9907c476779f)
                check_type(argname="argument multi_measure_attribute_mappings", value=multi_measure_attribute_mappings, expected_type=type_hints["multi_measure_attribute_mappings"])
                check_type(argname="argument target_multi_measure_name", value=target_multi_measure_name, expected_type=type_hints["target_multi_measure_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "multi_measure_attribute_mappings": multi_measure_attribute_mappings,
            }
            if target_multi_measure_name is not None:
                self._values["target_multi_measure_name"] = target_multi_measure_name

        @builtins.property
        def multi_measure_attribute_mappings(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnScheduledQuery.MultiMeasureAttributeMappingProperty"]]]:
            '''Required.

            Attribute mappings to be used for mapping query results to ingest data for multi-measure attributes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-multimeasuremappings.html#cfn-timestream-scheduledquery-multimeasuremappings-multimeasureattributemappings
            '''
            result = self._values.get("multi_measure_attribute_mappings")
            assert result is not None, "Required property 'multi_measure_attribute_mappings' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnScheduledQuery.MultiMeasureAttributeMappingProperty"]]], result)

        @builtins.property
        def target_multi_measure_name(self) -> typing.Optional[builtins.str]:
            '''The name of the target multi-measure name in the derived table.

            This input is required when measureNameColumn is not provided. If MeasureNameColumn is provided, then value from that column will be used as multi-measure name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-multimeasuremappings.html#cfn-timestream-scheduledquery-multimeasuremappings-targetmultimeasurename
            '''
            result = self._values.get("target_multi_measure_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MultiMeasureMappingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_timestream.CfnScheduledQuery.NotificationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"sns_configuration": "snsConfiguration"},
    )
    class NotificationConfigurationProperty:
        def __init__(
            self,
            *,
            sns_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnScheduledQuery.SnsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Notification configuration for a scheduled query.

            A notification is sent by Timestream when a scheduled query is created, its state is updated or when it is deleted.

            :param sns_configuration: Details on SNS configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-notificationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_timestream as timestream
                
                notification_configuration_property = timestream.CfnScheduledQuery.NotificationConfigurationProperty(
                    sns_configuration=timestream.CfnScheduledQuery.SnsConfigurationProperty(
                        topic_arn="topicArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0b4558fe9ddfa929e6b87d7e1fa0cd9d8b94dfa883bdac1bd63d056e227f35f0)
                check_type(argname="argument sns_configuration", value=sns_configuration, expected_type=type_hints["sns_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "sns_configuration": sns_configuration,
            }

        @builtins.property
        def sns_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnScheduledQuery.SnsConfigurationProperty"]:
            '''Details on SNS configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-notificationconfiguration.html#cfn-timestream-scheduledquery-notificationconfiguration-snsconfiguration
            '''
            result = self._values.get("sns_configuration")
            assert result is not None, "Required property 'sns_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnScheduledQuery.SnsConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NotificationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_timestream.CfnScheduledQuery.S3ConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_name": "bucketName",
            "encryption_option": "encryptionOption",
            "object_key_prefix": "objectKeyPrefix",
        },
    )
    class S3ConfigurationProperty:
        def __init__(
            self,
            *,
            bucket_name: builtins.str,
            encryption_option: typing.Optional[builtins.str] = None,
            object_key_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Details on S3 location for error reports that result from running a query.

            :param bucket_name: Name of the S3 bucket under which error reports will be created.
            :param encryption_option: Encryption at rest options for the error reports. If no encryption option is specified, Timestream will choose SSE_S3 as default.
            :param object_key_prefix: Prefix for the error report key. Timestream by default adds the following prefix to the error report path.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-s3configuration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_timestream as timestream
                
                s3_configuration_property = timestream.CfnScheduledQuery.S3ConfigurationProperty(
                    bucket_name="bucketName",
                
                    # the properties below are optional
                    encryption_option="encryptionOption",
                    object_key_prefix="objectKeyPrefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a2cd5f818ee1def696fbf7cfe15d2b108e29ea53bf63e3a782e441942af00835)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument encryption_option", value=encryption_option, expected_type=type_hints["encryption_option"])
                check_type(argname="argument object_key_prefix", value=object_key_prefix, expected_type=type_hints["object_key_prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_name": bucket_name,
            }
            if encryption_option is not None:
                self._values["encryption_option"] = encryption_option
            if object_key_prefix is not None:
                self._values["object_key_prefix"] = object_key_prefix

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''Name of the S3 bucket under which error reports will be created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-s3configuration.html#cfn-timestream-scheduledquery-s3configuration-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def encryption_option(self) -> typing.Optional[builtins.str]:
            '''Encryption at rest options for the error reports.

            If no encryption option is specified, Timestream will choose SSE_S3 as default.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-s3configuration.html#cfn-timestream-scheduledquery-s3configuration-encryptionoption
            '''
            result = self._values.get("encryption_option")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def object_key_prefix(self) -> typing.Optional[builtins.str]:
            '''Prefix for the error report key.

            Timestream by default adds the following prefix to the error report path.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-s3configuration.html#cfn-timestream-scheduledquery-s3configuration-objectkeyprefix
            '''
            result = self._values.get("object_key_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3ConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_timestream.CfnScheduledQuery.ScheduleConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"schedule_expression": "scheduleExpression"},
    )
    class ScheduleConfigurationProperty:
        def __init__(self, *, schedule_expression: builtins.str) -> None:
            '''Configuration of the schedule of the query.

            :param schedule_expression: An expression that denotes when to trigger the scheduled query run. This can be a cron expression or a rate expression.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-scheduleconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_timestream as timestream
                
                schedule_configuration_property = timestream.CfnScheduledQuery.ScheduleConfigurationProperty(
                    schedule_expression="scheduleExpression"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__123e13337f60109858734f464accee4f30c7120ff2f0233289d3556f45d70095)
                check_type(argname="argument schedule_expression", value=schedule_expression, expected_type=type_hints["schedule_expression"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "schedule_expression": schedule_expression,
            }

        @builtins.property
        def schedule_expression(self) -> builtins.str:
            '''An expression that denotes when to trigger the scheduled query run.

            This can be a cron expression or a rate expression.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-scheduleconfiguration.html#cfn-timestream-scheduledquery-scheduleconfiguration-scheduleexpression
            '''
            result = self._values.get("schedule_expression")
            assert result is not None, "Required property 'schedule_expression' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScheduleConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_timestream.CfnScheduledQuery.SnsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"topic_arn": "topicArn"},
    )
    class SnsConfigurationProperty:
        def __init__(self, *, topic_arn: builtins.str) -> None:
            '''Details on SNS that are required to send the notification.

            :param topic_arn: SNS topic ARN that the scheduled query status notifications will be sent to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-snsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_timestream as timestream
                
                sns_configuration_property = timestream.CfnScheduledQuery.SnsConfigurationProperty(
                    topic_arn="topicArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__05872c0f7f29313fe53bfce1afb4034a8b29bd5729076a86910e55eebc988286)
                check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "topic_arn": topic_arn,
            }

        @builtins.property
        def topic_arn(self) -> builtins.str:
            '''SNS topic ARN that the scheduled query status notifications will be sent to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-snsconfiguration.html#cfn-timestream-scheduledquery-snsconfiguration-topicarn
            '''
            result = self._values.get("topic_arn")
            assert result is not None, "Required property 'topic_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SnsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_timestream.CfnScheduledQuery.TargetConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"timestream_configuration": "timestreamConfiguration"},
    )
    class TargetConfigurationProperty:
        def __init__(
            self,
            *,
            timestream_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnScheduledQuery.TimestreamConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Configuration used for writing the output of a query.

            :param timestream_configuration: Configuration needed to write data into the Timestream database and table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-targetconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_timestream as timestream
                
                target_configuration_property = timestream.CfnScheduledQuery.TargetConfigurationProperty(
                    timestream_configuration=timestream.CfnScheduledQuery.TimestreamConfigurationProperty(
                        database_name="databaseName",
                        dimension_mappings=[timestream.CfnScheduledQuery.DimensionMappingProperty(
                            dimension_value_type="dimensionValueType",
                            name="name"
                        )],
                        table_name="tableName",
                        time_column="timeColumn",
                
                        # the properties below are optional
                        measure_name_column="measureNameColumn",
                        mixed_measure_mappings=[timestream.CfnScheduledQuery.MixedMeasureMappingProperty(
                            measure_value_type="measureValueType",
                
                            # the properties below are optional
                            measure_name="measureName",
                            multi_measure_attribute_mappings=[timestream.CfnScheduledQuery.MultiMeasureAttributeMappingProperty(
                                measure_value_type="measureValueType",
                                source_column="sourceColumn",
                
                                # the properties below are optional
                                target_multi_measure_attribute_name="targetMultiMeasureAttributeName"
                            )],
                            source_column="sourceColumn",
                            target_measure_name="targetMeasureName"
                        )],
                        multi_measure_mappings=timestream.CfnScheduledQuery.MultiMeasureMappingsProperty(
                            multi_measure_attribute_mappings=[timestream.CfnScheduledQuery.MultiMeasureAttributeMappingProperty(
                                measure_value_type="measureValueType",
                                source_column="sourceColumn",
                
                                # the properties below are optional
                                target_multi_measure_attribute_name="targetMultiMeasureAttributeName"
                            )],
                
                            # the properties below are optional
                            target_multi_measure_name="targetMultiMeasureName"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__08bb6d784035ed51b729ccce188db2e8804c4da2d66a7486549f9e0eb57bd928)
                check_type(argname="argument timestream_configuration", value=timestream_configuration, expected_type=type_hints["timestream_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "timestream_configuration": timestream_configuration,
            }

        @builtins.property
        def timestream_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnScheduledQuery.TimestreamConfigurationProperty"]:
            '''Configuration needed to write data into the Timestream database and table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-targetconfiguration.html#cfn-timestream-scheduledquery-targetconfiguration-timestreamconfiguration
            '''
            result = self._values.get("timestream_configuration")
            assert result is not None, "Required property 'timestream_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnScheduledQuery.TimestreamConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_timestream.CfnScheduledQuery.TimestreamConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "database_name": "databaseName",
            "dimension_mappings": "dimensionMappings",
            "table_name": "tableName",
            "time_column": "timeColumn",
            "measure_name_column": "measureNameColumn",
            "mixed_measure_mappings": "mixedMeasureMappings",
            "multi_measure_mappings": "multiMeasureMappings",
        },
    )
    class TimestreamConfigurationProperty:
        def __init__(
            self,
            *,
            database_name: builtins.str,
            dimension_mappings: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnScheduledQuery.DimensionMappingProperty", typing.Dict[builtins.str, typing.Any]]]]],
            table_name: builtins.str,
            time_column: builtins.str,
            measure_name_column: typing.Optional[builtins.str] = None,
            mixed_measure_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnScheduledQuery.MixedMeasureMappingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            multi_measure_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnScheduledQuery.MultiMeasureMappingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Configuration to write data into Timestream database and table.

            This configuration allows the user to map the query result select columns into the destination table columns.

            :param database_name: Name of Timestream database to which the query result will be written.
            :param dimension_mappings: This is to allow mapping column(s) from the query result to the dimension in the destination table.
            :param table_name: Name of Timestream table that the query result will be written to. The table should be within the same database that is provided in Timestream configuration.
            :param time_column: Column from query result that should be used as the time column in destination table. Column type for this should be TIMESTAMP.
            :param measure_name_column: Name of the measure column. Also see ``MultiMeasureMappings`` and ``MixedMeasureMappings`` for how measure name properties on those relate to ``MeasureNameColumn`` .
            :param mixed_measure_mappings: Specifies how to map measures to multi-measure records.
            :param multi_measure_mappings: Multi-measure mappings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-timestreamconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_timestream as timestream
                
                timestream_configuration_property = timestream.CfnScheduledQuery.TimestreamConfigurationProperty(
                    database_name="databaseName",
                    dimension_mappings=[timestream.CfnScheduledQuery.DimensionMappingProperty(
                        dimension_value_type="dimensionValueType",
                        name="name"
                    )],
                    table_name="tableName",
                    time_column="timeColumn",
                
                    # the properties below are optional
                    measure_name_column="measureNameColumn",
                    mixed_measure_mappings=[timestream.CfnScheduledQuery.MixedMeasureMappingProperty(
                        measure_value_type="measureValueType",
                
                        # the properties below are optional
                        measure_name="measureName",
                        multi_measure_attribute_mappings=[timestream.CfnScheduledQuery.MultiMeasureAttributeMappingProperty(
                            measure_value_type="measureValueType",
                            source_column="sourceColumn",
                
                            # the properties below are optional
                            target_multi_measure_attribute_name="targetMultiMeasureAttributeName"
                        )],
                        source_column="sourceColumn",
                        target_measure_name="targetMeasureName"
                    )],
                    multi_measure_mappings=timestream.CfnScheduledQuery.MultiMeasureMappingsProperty(
                        multi_measure_attribute_mappings=[timestream.CfnScheduledQuery.MultiMeasureAttributeMappingProperty(
                            measure_value_type="measureValueType",
                            source_column="sourceColumn",
                
                            # the properties below are optional
                            target_multi_measure_attribute_name="targetMultiMeasureAttributeName"
                        )],
                
                        # the properties below are optional
                        target_multi_measure_name="targetMultiMeasureName"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__49a5caa804573ad68d3177dfcc603fd8d8930af6649634eb4f6d1c6c7ceb19eb)
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument dimension_mappings", value=dimension_mappings, expected_type=type_hints["dimension_mappings"])
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
                check_type(argname="argument time_column", value=time_column, expected_type=type_hints["time_column"])
                check_type(argname="argument measure_name_column", value=measure_name_column, expected_type=type_hints["measure_name_column"])
                check_type(argname="argument mixed_measure_mappings", value=mixed_measure_mappings, expected_type=type_hints["mixed_measure_mappings"])
                check_type(argname="argument multi_measure_mappings", value=multi_measure_mappings, expected_type=type_hints["multi_measure_mappings"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "database_name": database_name,
                "dimension_mappings": dimension_mappings,
                "table_name": table_name,
                "time_column": time_column,
            }
            if measure_name_column is not None:
                self._values["measure_name_column"] = measure_name_column
            if mixed_measure_mappings is not None:
                self._values["mixed_measure_mappings"] = mixed_measure_mappings
            if multi_measure_mappings is not None:
                self._values["multi_measure_mappings"] = multi_measure_mappings

        @builtins.property
        def database_name(self) -> builtins.str:
            '''Name of Timestream database to which the query result will be written.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-timestreamconfiguration.html#cfn-timestream-scheduledquery-timestreamconfiguration-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dimension_mappings(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnScheduledQuery.DimensionMappingProperty"]]]:
            '''This is to allow mapping column(s) from the query result to the dimension in the destination table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-timestreamconfiguration.html#cfn-timestream-scheduledquery-timestreamconfiguration-dimensionmappings
            '''
            result = self._values.get("dimension_mappings")
            assert result is not None, "Required property 'dimension_mappings' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnScheduledQuery.DimensionMappingProperty"]]], result)

        @builtins.property
        def table_name(self) -> builtins.str:
            '''Name of Timestream table that the query result will be written to.

            The table should be within the same database that is provided in Timestream configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-timestreamconfiguration.html#cfn-timestream-scheduledquery-timestreamconfiguration-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def time_column(self) -> builtins.str:
            '''Column from query result that should be used as the time column in destination table.

            Column type for this should be TIMESTAMP.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-timestreamconfiguration.html#cfn-timestream-scheduledquery-timestreamconfiguration-timecolumn
            '''
            result = self._values.get("time_column")
            assert result is not None, "Required property 'time_column' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def measure_name_column(self) -> typing.Optional[builtins.str]:
            '''Name of the measure column.

            Also see ``MultiMeasureMappings`` and ``MixedMeasureMappings`` for how measure name properties on those relate to ``MeasureNameColumn`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-timestreamconfiguration.html#cfn-timestream-scheduledquery-timestreamconfiguration-measurenamecolumn
            '''
            result = self._values.get("measure_name_column")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def mixed_measure_mappings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnScheduledQuery.MixedMeasureMappingProperty"]]]]:
            '''Specifies how to map measures to multi-measure records.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-timestreamconfiguration.html#cfn-timestream-scheduledquery-timestreamconfiguration-mixedmeasuremappings
            '''
            result = self._values.get("mixed_measure_mappings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnScheduledQuery.MixedMeasureMappingProperty"]]]], result)

        @builtins.property
        def multi_measure_mappings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScheduledQuery.MultiMeasureMappingsProperty"]]:
            '''Multi-measure mappings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-timestreamconfiguration.html#cfn-timestream-scheduledquery-timestreamconfiguration-multimeasuremappings
            '''
            result = self._values.get("multi_measure_mappings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScheduledQuery.MultiMeasureMappingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimestreamConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_timestream.CfnScheduledQueryProps",
    jsii_struct_bases=[],
    name_mapping={
        "error_report_configuration": "errorReportConfiguration",
        "notification_configuration": "notificationConfiguration",
        "query_string": "queryString",
        "schedule_configuration": "scheduleConfiguration",
        "scheduled_query_execution_role_arn": "scheduledQueryExecutionRoleArn",
        "client_token": "clientToken",
        "kms_key_id": "kmsKeyId",
        "scheduled_query_name": "scheduledQueryName",
        "tags": "tags",
        "target_configuration": "targetConfiguration",
    },
)
class CfnScheduledQueryProps:
    def __init__(
        self,
        *,
        error_report_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScheduledQuery.ErrorReportConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
        notification_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScheduledQuery.NotificationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
        query_string: builtins.str,
        schedule_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScheduledQuery.ScheduleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
        scheduled_query_execution_role_arn: builtins.str,
        client_token: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        scheduled_query_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        target_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScheduledQuery.TargetConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnScheduledQuery``.

        :param error_report_configuration: Configuration for error reporting. Error reports will be generated when a problem is encountered when writing the query results.
        :param notification_configuration: Notification configuration for the scheduled query. A notification is sent by Timestream when a query run finishes, when the state is updated or when you delete it.
        :param query_string: The query string to run. Parameter names can be specified in the query string ``@`` character followed by an identifier. The named Parameter ``@scheduled_runtime`` is reserved and can be used in the query to get the time at which the query is scheduled to run. The timestamp calculated according to the ScheduleConfiguration parameter, will be the value of ``@scheduled_runtime`` paramater for each query run. For example, consider an instance of a scheduled query executing on 2021-12-01 00:00:00. For this instance, the ``@scheduled_runtime`` parameter is initialized to the timestamp 2021-12-01 00:00:00 when invoking the query.
        :param schedule_configuration: Schedule configuration.
        :param scheduled_query_execution_role_arn: The ARN for the IAM role that Timestream will assume when running the scheduled query.
        :param client_token: Using a ClientToken makes the call to CreateScheduledQuery idempotent, in other words, making the same request repeatedly will produce the same result. Making multiple identical CreateScheduledQuery requests has the same effect as making a single request. - If CreateScheduledQuery is called without a ``ClientToken`` , the Query SDK generates a ``ClientToken`` on your behalf. - After 8 hours, any request with the same ``ClientToken`` is treated as a new request.
        :param kms_key_id: The Amazon KMS key used to encrypt the scheduled query resource, at-rest. If the Amazon KMS key is not specified, the scheduled query resource will be encrypted with a Timestream owned Amazon KMS key. To specify a KMS key, use the key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix the name with *alias/* If ErrorReportConfiguration uses ``SSE_KMS`` as encryption type, the same KmsKeyId is used to encrypt the error report at rest.
        :param scheduled_query_name: A name for the query. Scheduled query names must be unique within each Region.
        :param tags: A list of key-value pairs to label the scheduled query.
        :param target_configuration: Scheduled query target store configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-scheduledquery.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_timestream as timestream
            
            cfn_scheduled_query_props = timestream.CfnScheduledQueryProps(
                error_report_configuration=timestream.CfnScheduledQuery.ErrorReportConfigurationProperty(
                    s3_configuration=timestream.CfnScheduledQuery.S3ConfigurationProperty(
                        bucket_name="bucketName",
            
                        # the properties below are optional
                        encryption_option="encryptionOption",
                        object_key_prefix="objectKeyPrefix"
                    )
                ),
                notification_configuration=timestream.CfnScheduledQuery.NotificationConfigurationProperty(
                    sns_configuration=timestream.CfnScheduledQuery.SnsConfigurationProperty(
                        topic_arn="topicArn"
                    )
                ),
                query_string="queryString",
                schedule_configuration=timestream.CfnScheduledQuery.ScheduleConfigurationProperty(
                    schedule_expression="scheduleExpression"
                ),
                scheduled_query_execution_role_arn="scheduledQueryExecutionRoleArn",
            
                # the properties below are optional
                client_token="clientToken",
                kms_key_id="kmsKeyId",
                scheduled_query_name="scheduledQueryName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                target_configuration=timestream.CfnScheduledQuery.TargetConfigurationProperty(
                    timestream_configuration=timestream.CfnScheduledQuery.TimestreamConfigurationProperty(
                        database_name="databaseName",
                        dimension_mappings=[timestream.CfnScheduledQuery.DimensionMappingProperty(
                            dimension_value_type="dimensionValueType",
                            name="name"
                        )],
                        table_name="tableName",
                        time_column="timeColumn",
            
                        # the properties below are optional
                        measure_name_column="measureNameColumn",
                        mixed_measure_mappings=[timestream.CfnScheduledQuery.MixedMeasureMappingProperty(
                            measure_value_type="measureValueType",
            
                            # the properties below are optional
                            measure_name="measureName",
                            multi_measure_attribute_mappings=[timestream.CfnScheduledQuery.MultiMeasureAttributeMappingProperty(
                                measure_value_type="measureValueType",
                                source_column="sourceColumn",
            
                                # the properties below are optional
                                target_multi_measure_attribute_name="targetMultiMeasureAttributeName"
                            )],
                            source_column="sourceColumn",
                            target_measure_name="targetMeasureName"
                        )],
                        multi_measure_mappings=timestream.CfnScheduledQuery.MultiMeasureMappingsProperty(
                            multi_measure_attribute_mappings=[timestream.CfnScheduledQuery.MultiMeasureAttributeMappingProperty(
                                measure_value_type="measureValueType",
                                source_column="sourceColumn",
            
                                # the properties below are optional
                                target_multi_measure_attribute_name="targetMultiMeasureAttributeName"
                            )],
            
                            # the properties below are optional
                            target_multi_measure_name="targetMultiMeasureName"
                        )
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2caf5d9713b0dd130de3eaf553fcdda6f169bfdde6f8f293349239a734d19010)
            check_type(argname="argument error_report_configuration", value=error_report_configuration, expected_type=type_hints["error_report_configuration"])
            check_type(argname="argument notification_configuration", value=notification_configuration, expected_type=type_hints["notification_configuration"])
            check_type(argname="argument query_string", value=query_string, expected_type=type_hints["query_string"])
            check_type(argname="argument schedule_configuration", value=schedule_configuration, expected_type=type_hints["schedule_configuration"])
            check_type(argname="argument scheduled_query_execution_role_arn", value=scheduled_query_execution_role_arn, expected_type=type_hints["scheduled_query_execution_role_arn"])
            check_type(argname="argument client_token", value=client_token, expected_type=type_hints["client_token"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument scheduled_query_name", value=scheduled_query_name, expected_type=type_hints["scheduled_query_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument target_configuration", value=target_configuration, expected_type=type_hints["target_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "error_report_configuration": error_report_configuration,
            "notification_configuration": notification_configuration,
            "query_string": query_string,
            "schedule_configuration": schedule_configuration,
            "scheduled_query_execution_role_arn": scheduled_query_execution_role_arn,
        }
        if client_token is not None:
            self._values["client_token"] = client_token
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if scheduled_query_name is not None:
            self._values["scheduled_query_name"] = scheduled_query_name
        if tags is not None:
            self._values["tags"] = tags
        if target_configuration is not None:
            self._values["target_configuration"] = target_configuration

    @builtins.property
    def error_report_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnScheduledQuery.ErrorReportConfigurationProperty]:
        '''Configuration for error reporting.

        Error reports will be generated when a problem is encountered when writing the query results.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-scheduledquery.html#cfn-timestream-scheduledquery-errorreportconfiguration
        '''
        result = self._values.get("error_report_configuration")
        assert result is not None, "Required property 'error_report_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnScheduledQuery.ErrorReportConfigurationProperty], result)

    @builtins.property
    def notification_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnScheduledQuery.NotificationConfigurationProperty]:
        '''Notification configuration for the scheduled query.

        A notification is sent by Timestream when a query run finishes, when the state is updated or when you delete it.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-scheduledquery.html#cfn-timestream-scheduledquery-notificationconfiguration
        '''
        result = self._values.get("notification_configuration")
        assert result is not None, "Required property 'notification_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnScheduledQuery.NotificationConfigurationProperty], result)

    @builtins.property
    def query_string(self) -> builtins.str:
        '''The query string to run.

        Parameter names can be specified in the query string ``@`` character followed by an identifier. The named Parameter ``@scheduled_runtime`` is reserved and can be used in the query to get the time at which the query is scheduled to run.

        The timestamp calculated according to the ScheduleConfiguration parameter, will be the value of ``@scheduled_runtime`` paramater for each query run. For example, consider an instance of a scheduled query executing on 2021-12-01 00:00:00. For this instance, the ``@scheduled_runtime`` parameter is initialized to the timestamp 2021-12-01 00:00:00 when invoking the query.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-scheduledquery.html#cfn-timestream-scheduledquery-querystring
        '''
        result = self._values.get("query_string")
        assert result is not None, "Required property 'query_string' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schedule_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnScheduledQuery.ScheduleConfigurationProperty]:
        '''Schedule configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-scheduledquery.html#cfn-timestream-scheduledquery-scheduleconfiguration
        '''
        result = self._values.get("schedule_configuration")
        assert result is not None, "Required property 'schedule_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnScheduledQuery.ScheduleConfigurationProperty], result)

    @builtins.property
    def scheduled_query_execution_role_arn(self) -> builtins.str:
        '''The ARN for the IAM role that Timestream will assume when running the scheduled query.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-scheduledquery.html#cfn-timestream-scheduledquery-scheduledqueryexecutionrolearn
        '''
        result = self._values.get("scheduled_query_execution_role_arn")
        assert result is not None, "Required property 'scheduled_query_execution_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_token(self) -> typing.Optional[builtins.str]:
        '''Using a ClientToken makes the call to CreateScheduledQuery idempotent, in other words, making the same request repeatedly will produce the same result.

        Making multiple identical CreateScheduledQuery requests has the same effect as making a single request.

        - If CreateScheduledQuery is called without a ``ClientToken`` , the Query SDK generates a ``ClientToken`` on your behalf.
        - After 8 hours, any request with the same ``ClientToken`` is treated as a new request.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-scheduledquery.html#cfn-timestream-scheduledquery-clienttoken
        '''
        result = self._values.get("client_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The Amazon KMS key used to encrypt the scheduled query resource, at-rest.

        If the Amazon KMS key is not specified, the scheduled query resource will be encrypted with a Timestream owned Amazon KMS key. To specify a KMS key, use the key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix the name with *alias/*

        If ErrorReportConfiguration uses ``SSE_KMS`` as encryption type, the same KmsKeyId is used to encrypt the error report at rest.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-scheduledquery.html#cfn-timestream-scheduledquery-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scheduled_query_name(self) -> typing.Optional[builtins.str]:
        '''A name for the query.

        Scheduled query names must be unique within each Region.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-scheduledquery.html#cfn-timestream-scheduledquery-scheduledqueryname
        '''
        result = self._values.get("scheduled_query_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs to label the scheduled query.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-scheduledquery.html#cfn-timestream-scheduledquery-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def target_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnScheduledQuery.TargetConfigurationProperty]]:
        '''Scheduled query target store configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-scheduledquery.html#cfn-timestream-scheduledquery-targetconfiguration
        '''
        result = self._values.get("target_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnScheduledQuery.TargetConfigurationProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnScheduledQueryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnTable(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_timestream.CfnTable",
):
    '''The CreateTable operation adds a new table to an existing database in your account.

    In an AWS account, table names must be at least unique within each Region if they are in the same database. You may have identical table names in the same Region if the tables are in separate databases. While creating the table, you must specify the table name, database name, and the retention properties. `Service quotas apply <https://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html>`_ . See `code sample <https://docs.aws.amazon.com/timestream/latest/developerguide/code-samples.create-table.html>`_ for details.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-table.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_timestream as timestream
        
        # magnetic_store_write_properties: Any
        # retention_properties: Any
        
        cfn_table = timestream.CfnTable(self, "MyCfnTable",
            database_name="databaseName",
        
            # the properties below are optional
            magnetic_store_write_properties=magnetic_store_write_properties,
            retention_properties=retention_properties,
            table_name="tableName",
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
        database_name: builtins.str,
        magnetic_store_write_properties: typing.Any = None,
        retention_properties: typing.Any = None,
        table_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param database_name: The name of the Timestream database that contains this table. *Length Constraints* : Minimum length of 3 bytes. Maximum length of 256 bytes.
        :param magnetic_store_write_properties: Contains properties to set on the table when enabling magnetic store writes. This object has the following attributes: - *EnableMagneticStoreWrites* : A ``boolean`` flag to enable magnetic store writes. - *MagneticStoreRejectedDataLocation* : The location to write error reports for records rejected, asynchronously, during magnetic store writes. Only ``S3Configuration`` objects are allowed. The ``S3Configuration`` object has the following attributes: - *BucketName* : The name of the S3 bucket. - *EncryptionOption* : The encryption option for the S3 location. Valid values are S3 server-side encryption with an S3 managed key ( ``SSE_S3`` ) or AWS managed key ( ``SSE_KMS`` ). - *KmsKeyId* : The AWS KMS key ID to use when encrypting with an AWS managed key. - *ObjectKeyPrefix* : The prefix to use option for the objects stored in S3. Both ``BucketName`` and ``EncryptionOption`` are *required* when ``S3Configuration`` is specified. If you specify ``SSE_KMS`` as your ``EncryptionOption`` then ``KmsKeyId`` is *required* . ``EnableMagneticStoreWrites`` attribute is *required* when ``MagneticStoreWriteProperties`` is specified. ``MagneticStoreRejectedDataLocation`` attribute is *required* when ``EnableMagneticStoreWrites`` is set to ``true`` . See the following examples: *JSON:: { "Type" : AWS::Timestream::Table", "Properties":{ "DatabaseName":"TestDatabase", "TableName":"TestTable", "MagneticStoreWriteProperties":{ "EnableMagneticStoreWrites":true, "MagneticStoreRejectedDataLocation":{ "S3Configuration":{ "BucketName":"testbucket", "EncryptionOption":"SSE_KMS", "KmsKeyId":"1234abcd-12ab-34cd-56ef-1234567890ab", "ObjectKeyPrefix":"prefix" } } } } } *YAML:: Type: AWS::Timestream::Table DependsOn: TestDatabase Properties: TableName: "TestTable" DatabaseName: "TestDatabase" MagneticStoreWriteProperties: EnableMagneticStoreWrites: true MagneticStoreRejectedDataLocation: S3Configuration: BucketName: "testbucket" EncryptionOption: "SSE_KMS" KmsKeyId: "1234abcd-12ab-34cd-56ef-1234567890ab" ObjectKeyPrefix: "prefix"
        :param retention_properties: The retention duration for the memory store and magnetic store. This object has the following attributes:. - *MemoryStoreRetentionPeriodInHours* : Retention duration for memory store, in hours. - *MagneticStoreRetentionPeriodInDays* : Retention duration for magnetic store, in days. Both attributes are of type ``string`` . Both attributes are *required* when ``RetentionProperties`` is specified. See the following examples: *JSON* ``{ "Type" : AWS::Timestream::Table", "Properties" : { "DatabaseName" : "TestDatabase", "TableName" : "TestTable", "RetentionProperties" : { "MemoryStoreRetentionPeriodInHours": "24", "MagneticStoreRetentionPeriodInDays": "7" } } }`` *YAML:: Type: AWS::Timestream::Table DependsOn: TestDatabase Properties: TableName: "TestTable" DatabaseName: "TestDatabase" RetentionProperties: MemoryStoreRetentionPeriodInHours: "24" MagneticStoreRetentionPeriodInDays: "7"
        :param table_name: The name of the Timestream table. *Length Constraints* : Minimum length of 3 bytes. Maximum length of 256 bytes.
        :param tags: The tags to add to the table.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aad96eaee00841ee49968da22b6ed13b3777f265d71c1981b2f1b217cf0db5fd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTableProps(
            database_name=database_name,
            magnetic_store_write_properties=magnetic_store_write_properties,
            retention_properties=retention_properties,
            table_name=table_name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e1f672b6c3046841d69f96c6b256cf927db52e0b4f4cd165e7022a893b539b1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bce41cd8d4cbef6b9eee9051e83083ebfd8194941c7349171e844f0c59db0f78)
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
        '''The ``arn`` of the table.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''The name of the table.

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

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
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        '''The name of the Timestream database that contains this table.'''
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e86eb21a358133850347dfd746769a6d1446d47d303f3a0491f2235ed3136b11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="magneticStoreWriteProperties")
    def magnetic_store_write_properties(self) -> typing.Any:
        '''Contains properties to set on the table when enabling magnetic store writes.'''
        return typing.cast(typing.Any, jsii.get(self, "magneticStoreWriteProperties"))

    @magnetic_store_write_properties.setter
    def magnetic_store_write_properties(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58178ccb289368b799599c9ec47acf86a335f70eaf713c6562b4b5714d8354e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "magneticStoreWriteProperties", value)

    @builtins.property
    @jsii.member(jsii_name="retentionProperties")
    def retention_properties(self) -> typing.Any:
        '''The retention duration for the memory store and magnetic store.

        This object has the following attributes:.
        '''
        return typing.cast(typing.Any, jsii.get(self, "retentionProperties"))

    @retention_properties.setter
    def retention_properties(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7ed60d3a1390fe9d904e5be80332e4919f8cc331f6a9c78e2c46569bb125df6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionProperties", value)

    @builtins.property
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> typing.Optional[builtins.str]:
        '''The name of the Timestream table.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableName"))

    @table_name.setter
    def table_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd18b0f7dd5d02d260ec7f2eaec2e2b9b2ab172a6763f2f391fc93ea1f562de6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableName", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to add to the table.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b21aea3e87d0ba84d4dcca0e9c65c1478588d9aacadd5d365ad9d63d17b025f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_timestream.CfnTable.MagneticStoreRejectedDataLocationProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_configuration": "s3Configuration"},
    )
    class MagneticStoreRejectedDataLocationProperty:
        def __init__(
            self,
            *,
            s3_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTable.S3ConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The location to write error reports for records rejected, asynchronously, during magnetic store writes.

            :param s3_configuration: Configuration of an S3 location to write error reports for records rejected, asynchronously, during magnetic store writes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-magneticstorerejecteddatalocation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_timestream as timestream
                
                magnetic_store_rejected_data_location_property = timestream.CfnTable.MagneticStoreRejectedDataLocationProperty(
                    s3_configuration=timestream.CfnTable.S3ConfigurationProperty(
                        bucket_name="bucketName",
                        encryption_option="encryptionOption",
                
                        # the properties below are optional
                        kms_key_id="kmsKeyId",
                        object_key_prefix="objectKeyPrefix"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3715f3b01c0f5179420758f44caa8c4febf57c507d65c9222714b52bbdfc3cf4)
                check_type(argname="argument s3_configuration", value=s3_configuration, expected_type=type_hints["s3_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if s3_configuration is not None:
                self._values["s3_configuration"] = s3_configuration

        @builtins.property
        def s3_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTable.S3ConfigurationProperty"]]:
            '''Configuration of an S3 location to write error reports for records rejected, asynchronously, during magnetic store writes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-magneticstorerejecteddatalocation.html#cfn-timestream-table-magneticstorerejecteddatalocation-s3configuration
            '''
            result = self._values.get("s3_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTable.S3ConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MagneticStoreRejectedDataLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_timestream.CfnTable.MagneticStoreWritePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enable_magnetic_store_writes": "enableMagneticStoreWrites",
            "magnetic_store_rejected_data_location": "magneticStoreRejectedDataLocation",
        },
    )
    class MagneticStoreWritePropertiesProperty:
        def __init__(
            self,
            *,
            enable_magnetic_store_writes: typing.Union[builtins.bool, _IResolvable_da3f097b],
            magnetic_store_rejected_data_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTable.MagneticStoreRejectedDataLocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The set of properties on a table for configuring magnetic store writes.

            :param enable_magnetic_store_writes: A flag to enable magnetic store writes.
            :param magnetic_store_rejected_data_location: The location to write error reports for records rejected asynchronously during magnetic store writes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-magneticstorewriteproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_timestream as timestream
                
                magnetic_store_write_properties_property = timestream.CfnTable.MagneticStoreWritePropertiesProperty(
                    enable_magnetic_store_writes=False,
                
                    # the properties below are optional
                    magnetic_store_rejected_data_location=timestream.CfnTable.MagneticStoreRejectedDataLocationProperty(
                        s3_configuration=timestream.CfnTable.S3ConfigurationProperty(
                            bucket_name="bucketName",
                            encryption_option="encryptionOption",
                
                            # the properties below are optional
                            kms_key_id="kmsKeyId",
                            object_key_prefix="objectKeyPrefix"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__73eb42c14a8651455e1beb5676ed25ea12aff08495097fc56c3d8adcf38dc77d)
                check_type(argname="argument enable_magnetic_store_writes", value=enable_magnetic_store_writes, expected_type=type_hints["enable_magnetic_store_writes"])
                check_type(argname="argument magnetic_store_rejected_data_location", value=magnetic_store_rejected_data_location, expected_type=type_hints["magnetic_store_rejected_data_location"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "enable_magnetic_store_writes": enable_magnetic_store_writes,
            }
            if magnetic_store_rejected_data_location is not None:
                self._values["magnetic_store_rejected_data_location"] = magnetic_store_rejected_data_location

        @builtins.property
        def enable_magnetic_store_writes(
            self,
        ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''A flag to enable magnetic store writes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-magneticstorewriteproperties.html#cfn-timestream-table-magneticstorewriteproperties-enablemagneticstorewrites
            '''
            result = self._values.get("enable_magnetic_store_writes")
            assert result is not None, "Required property 'enable_magnetic_store_writes' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def magnetic_store_rejected_data_location(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTable.MagneticStoreRejectedDataLocationProperty"]]:
            '''The location to write error reports for records rejected asynchronously during magnetic store writes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-magneticstorewriteproperties.html#cfn-timestream-table-magneticstorewriteproperties-magneticstorerejecteddatalocation
            '''
            result = self._values.get("magnetic_store_rejected_data_location")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTable.MagneticStoreRejectedDataLocationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MagneticStoreWritePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_timestream.CfnTable.RetentionPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "magnetic_store_retention_period_in_days": "magneticStoreRetentionPeriodInDays",
            "memory_store_retention_period_in_hours": "memoryStoreRetentionPeriodInHours",
        },
    )
    class RetentionPropertiesProperty:
        def __init__(
            self,
            *,
            magnetic_store_retention_period_in_days: typing.Optional[builtins.str] = None,
            memory_store_retention_period_in_hours: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Retention properties contain the duration for which your time-series data must be stored in the magnetic store and the memory store.

            :param magnetic_store_retention_period_in_days: The duration for which data must be stored in the magnetic store.
            :param memory_store_retention_period_in_hours: The duration for which data must be stored in the memory store.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-retentionproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_timestream as timestream
                
                retention_properties_property = timestream.CfnTable.RetentionPropertiesProperty(
                    magnetic_store_retention_period_in_days="magneticStoreRetentionPeriodInDays",
                    memory_store_retention_period_in_hours="memoryStoreRetentionPeriodInHours"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0d96ad0456f88b9bdc9094b197d35b5a25aebf85c67723143187828e4d58ee78)
                check_type(argname="argument magnetic_store_retention_period_in_days", value=magnetic_store_retention_period_in_days, expected_type=type_hints["magnetic_store_retention_period_in_days"])
                check_type(argname="argument memory_store_retention_period_in_hours", value=memory_store_retention_period_in_hours, expected_type=type_hints["memory_store_retention_period_in_hours"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if magnetic_store_retention_period_in_days is not None:
                self._values["magnetic_store_retention_period_in_days"] = magnetic_store_retention_period_in_days
            if memory_store_retention_period_in_hours is not None:
                self._values["memory_store_retention_period_in_hours"] = memory_store_retention_period_in_hours

        @builtins.property
        def magnetic_store_retention_period_in_days(
            self,
        ) -> typing.Optional[builtins.str]:
            '''The duration for which data must be stored in the magnetic store.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-retentionproperties.html#cfn-timestream-table-retentionproperties-magneticstoreretentionperiodindays
            '''
            result = self._values.get("magnetic_store_retention_period_in_days")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def memory_store_retention_period_in_hours(
            self,
        ) -> typing.Optional[builtins.str]:
            '''The duration for which data must be stored in the memory store.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-retentionproperties.html#cfn-timestream-table-retentionproperties-memorystoreretentionperiodinhours
            '''
            result = self._values.get("memory_store_retention_period_in_hours")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RetentionPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_timestream.CfnTable.S3ConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_name": "bucketName",
            "encryption_option": "encryptionOption",
            "kms_key_id": "kmsKeyId",
            "object_key_prefix": "objectKeyPrefix",
        },
    )
    class S3ConfigurationProperty:
        def __init__(
            self,
            *,
            bucket_name: builtins.str,
            encryption_option: builtins.str,
            kms_key_id: typing.Optional[builtins.str] = None,
            object_key_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration that specifies an S3 location.

            :param bucket_name: The bucket name of the customer S3 bucket.
            :param encryption_option: The encryption option for the customer S3 location. Options are S3 server-side encryption with an S3 managed key or AWS managed key.
            :param kms_key_id: The AWS KMS key ID for the customer S3 location when encrypting with an AWS managed key.
            :param object_key_prefix: The object key preview for the customer S3 location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-s3configuration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_timestream as timestream
                
                s3_configuration_property = timestream.CfnTable.S3ConfigurationProperty(
                    bucket_name="bucketName",
                    encryption_option="encryptionOption",
                
                    # the properties below are optional
                    kms_key_id="kmsKeyId",
                    object_key_prefix="objectKeyPrefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b50e041ecb4eab9fe02a29c9d1c8c5a1325b090b4a8e835dd2f0242b6754d868)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument encryption_option", value=encryption_option, expected_type=type_hints["encryption_option"])
                check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
                check_type(argname="argument object_key_prefix", value=object_key_prefix, expected_type=type_hints["object_key_prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_name": bucket_name,
                "encryption_option": encryption_option,
            }
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id
            if object_key_prefix is not None:
                self._values["object_key_prefix"] = object_key_prefix

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''The bucket name of the customer S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-s3configuration.html#cfn-timestream-table-s3configuration-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def encryption_option(self) -> builtins.str:
            '''The encryption option for the customer S3 location.

            Options are S3 server-side encryption with an S3 managed key or AWS managed key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-s3configuration.html#cfn-timestream-table-s3configuration-encryptionoption
            '''
            result = self._values.get("encryption_option")
            assert result is not None, "Required property 'encryption_option' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''The AWS KMS key ID for the customer S3 location when encrypting with an AWS managed key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-s3configuration.html#cfn-timestream-table-s3configuration-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def object_key_prefix(self) -> typing.Optional[builtins.str]:
            '''The object key preview for the customer S3 location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-s3configuration.html#cfn-timestream-table-s3configuration-objectkeyprefix
            '''
            result = self._values.get("object_key_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3ConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_timestream.CfnTableProps",
    jsii_struct_bases=[],
    name_mapping={
        "database_name": "databaseName",
        "magnetic_store_write_properties": "magneticStoreWriteProperties",
        "retention_properties": "retentionProperties",
        "table_name": "tableName",
        "tags": "tags",
    },
)
class CfnTableProps:
    def __init__(
        self,
        *,
        database_name: builtins.str,
        magnetic_store_write_properties: typing.Any = None,
        retention_properties: typing.Any = None,
        table_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTable``.

        :param database_name: The name of the Timestream database that contains this table. *Length Constraints* : Minimum length of 3 bytes. Maximum length of 256 bytes.
        :param magnetic_store_write_properties: Contains properties to set on the table when enabling magnetic store writes. This object has the following attributes: - *EnableMagneticStoreWrites* : A ``boolean`` flag to enable magnetic store writes. - *MagneticStoreRejectedDataLocation* : The location to write error reports for records rejected, asynchronously, during magnetic store writes. Only ``S3Configuration`` objects are allowed. The ``S3Configuration`` object has the following attributes: - *BucketName* : The name of the S3 bucket. - *EncryptionOption* : The encryption option for the S3 location. Valid values are S3 server-side encryption with an S3 managed key ( ``SSE_S3`` ) or AWS managed key ( ``SSE_KMS`` ). - *KmsKeyId* : The AWS KMS key ID to use when encrypting with an AWS managed key. - *ObjectKeyPrefix* : The prefix to use option for the objects stored in S3. Both ``BucketName`` and ``EncryptionOption`` are *required* when ``S3Configuration`` is specified. If you specify ``SSE_KMS`` as your ``EncryptionOption`` then ``KmsKeyId`` is *required* . ``EnableMagneticStoreWrites`` attribute is *required* when ``MagneticStoreWriteProperties`` is specified. ``MagneticStoreRejectedDataLocation`` attribute is *required* when ``EnableMagneticStoreWrites`` is set to ``true`` . See the following examples: *JSON:: { "Type" : AWS::Timestream::Table", "Properties":{ "DatabaseName":"TestDatabase", "TableName":"TestTable", "MagneticStoreWriteProperties":{ "EnableMagneticStoreWrites":true, "MagneticStoreRejectedDataLocation":{ "S3Configuration":{ "BucketName":"testbucket", "EncryptionOption":"SSE_KMS", "KmsKeyId":"1234abcd-12ab-34cd-56ef-1234567890ab", "ObjectKeyPrefix":"prefix" } } } } } *YAML:: Type: AWS::Timestream::Table DependsOn: TestDatabase Properties: TableName: "TestTable" DatabaseName: "TestDatabase" MagneticStoreWriteProperties: EnableMagneticStoreWrites: true MagneticStoreRejectedDataLocation: S3Configuration: BucketName: "testbucket" EncryptionOption: "SSE_KMS" KmsKeyId: "1234abcd-12ab-34cd-56ef-1234567890ab" ObjectKeyPrefix: "prefix"
        :param retention_properties: The retention duration for the memory store and magnetic store. This object has the following attributes:. - *MemoryStoreRetentionPeriodInHours* : Retention duration for memory store, in hours. - *MagneticStoreRetentionPeriodInDays* : Retention duration for magnetic store, in days. Both attributes are of type ``string`` . Both attributes are *required* when ``RetentionProperties`` is specified. See the following examples: *JSON* ``{ "Type" : AWS::Timestream::Table", "Properties" : { "DatabaseName" : "TestDatabase", "TableName" : "TestTable", "RetentionProperties" : { "MemoryStoreRetentionPeriodInHours": "24", "MagneticStoreRetentionPeriodInDays": "7" } } }`` *YAML:: Type: AWS::Timestream::Table DependsOn: TestDatabase Properties: TableName: "TestTable" DatabaseName: "TestDatabase" RetentionProperties: MemoryStoreRetentionPeriodInHours: "24" MagneticStoreRetentionPeriodInDays: "7"
        :param table_name: The name of the Timestream table. *Length Constraints* : Minimum length of 3 bytes. Maximum length of 256 bytes.
        :param tags: The tags to add to the table.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-table.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_timestream as timestream
            
            # magnetic_store_write_properties: Any
            # retention_properties: Any
            
            cfn_table_props = timestream.CfnTableProps(
                database_name="databaseName",
            
                # the properties below are optional
                magnetic_store_write_properties=magnetic_store_write_properties,
                retention_properties=retention_properties,
                table_name="tableName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9edb9a2aaa51342f4db373e24edd938478a52c96340bde2bc89fe7b86eb4431)
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument magnetic_store_write_properties", value=magnetic_store_write_properties, expected_type=type_hints["magnetic_store_write_properties"])
            check_type(argname="argument retention_properties", value=retention_properties, expected_type=type_hints["retention_properties"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database_name": database_name,
        }
        if magnetic_store_write_properties is not None:
            self._values["magnetic_store_write_properties"] = magnetic_store_write_properties
        if retention_properties is not None:
            self._values["retention_properties"] = retention_properties
        if table_name is not None:
            self._values["table_name"] = table_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def database_name(self) -> builtins.str:
        '''The name of the Timestream database that contains this table.

        *Length Constraints* : Minimum length of 3 bytes. Maximum length of 256 bytes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-table.html#cfn-timestream-table-databasename
        '''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def magnetic_store_write_properties(self) -> typing.Any:
        '''Contains properties to set on the table when enabling magnetic store writes.

        This object has the following attributes:

        - *EnableMagneticStoreWrites* : A ``boolean`` flag to enable magnetic store writes.
        - *MagneticStoreRejectedDataLocation* : The location to write error reports for records rejected, asynchronously, during magnetic store writes. Only ``S3Configuration`` objects are allowed. The ``S3Configuration`` object has the following attributes:
        - *BucketName* : The name of the S3 bucket.
        - *EncryptionOption* : The encryption option for the S3 location. Valid values are S3 server-side encryption with an S3 managed key ( ``SSE_S3`` ) or AWS managed key ( ``SSE_KMS`` ).
        - *KmsKeyId* : The AWS KMS key ID to use when encrypting with an AWS managed key.
        - *ObjectKeyPrefix* : The prefix to use option for the objects stored in S3.

        Both ``BucketName`` and ``EncryptionOption`` are *required* when ``S3Configuration`` is specified. If you specify ``SSE_KMS`` as your ``EncryptionOption`` then ``KmsKeyId`` is *required* .

        ``EnableMagneticStoreWrites`` attribute is *required* when ``MagneticStoreWriteProperties`` is specified. ``MagneticStoreRejectedDataLocation`` attribute is *required* when ``EnableMagneticStoreWrites`` is set to ``true`` .

        See the following examples:

        *JSON::

           { "Type" : AWS::Timestream::Table", "Properties":{ "DatabaseName":"TestDatabase", "TableName":"TestTable", "MagneticStoreWriteProperties":{ "EnableMagneticStoreWrites":true, "MagneticStoreRejectedDataLocation":{ "S3Configuration":{ "BucketName":"testbucket", "EncryptionOption":"SSE_KMS", "KmsKeyId":"1234abcd-12ab-34cd-56ef-1234567890ab", "ObjectKeyPrefix":"prefix" } } } }
           }

        *YAML::

           Type: AWS::Timestream::Table
           DependsOn: TestDatabase
           Properties: TableName: "TestTable" DatabaseName: "TestDatabase" MagneticStoreWriteProperties: EnableMagneticStoreWrites: true MagneticStoreRejectedDataLocation: S3Configuration: BucketName: "testbucket" EncryptionOption: "SSE_KMS" KmsKeyId: "1234abcd-12ab-34cd-56ef-1234567890ab" ObjectKeyPrefix: "prefix"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-table.html#cfn-timestream-table-magneticstorewriteproperties
        '''
        result = self._values.get("magnetic_store_write_properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def retention_properties(self) -> typing.Any:
        '''The retention duration for the memory store and magnetic store. This object has the following attributes:.

        - *MemoryStoreRetentionPeriodInHours* : Retention duration for memory store, in hours.
        - *MagneticStoreRetentionPeriodInDays* : Retention duration for magnetic store, in days.

        Both attributes are of type ``string`` . Both attributes are *required* when ``RetentionProperties`` is specified.

        See the following examples:

        *JSON*

        ``{ "Type" : AWS::Timestream::Table", "Properties" : { "DatabaseName" : "TestDatabase", "TableName" : "TestTable", "RetentionProperties" : { "MemoryStoreRetentionPeriodInHours": "24", "MagneticStoreRetentionPeriodInDays": "7" } } }``

        *YAML::

           Type: AWS::Timestream::Table
           DependsOn: TestDatabase
           Properties: TableName: "TestTable" DatabaseName: "TestDatabase" RetentionProperties: MemoryStoreRetentionPeriodInHours: "24" MagneticStoreRetentionPeriodInDays: "7"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-table.html#cfn-timestream-table-retentionproperties
        '''
        result = self._values.get("retention_properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def table_name(self) -> typing.Optional[builtins.str]:
        '''The name of the Timestream table.

        *Length Constraints* : Minimum length of 3 bytes. Maximum length of 256 bytes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-table.html#cfn-timestream-table-tablename
        '''
        result = self._values.get("table_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to add to the table.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-table.html#cfn-timestream-table-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTableProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDatabase",
    "CfnDatabaseProps",
    "CfnScheduledQuery",
    "CfnScheduledQueryProps",
    "CfnTable",
    "CfnTableProps",
]

publication.publish()

def _typecheckingstub__df267d6c98734bb503e076f315371b3537a6654cdfd5246386d41db61b38fa31(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    database_name: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9baaa3cf10dd12d7584c82547f4f62f6168d3a70bb84280e11437c6f39e056e8(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38f97f8e45b06461dc33c410476a8c6ab5fd5787cafd00019e0a1873cdf9996b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cbde3c6f76ec33728e8896f7456e86f8a746129259457fcb60defa5e1d7bdf3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a88a8e589058995e4c9588f4cb113f823707014eb42119b90c9719e50cb390e5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c161fd44298031bcce0863494a5d3a09a73703fe8c50ee977b03cbe4cab5d4a2(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fffb8befe8374295020dd254ed0c77820bb26fc0d94c59e0a34f89d6fb3f295c(
    *,
    database_name: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17cb9c0ebf2969eb32b3d5921e02d6b922a461b4f7becdb1bf28f83cb9407cfa(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    error_report_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScheduledQuery.ErrorReportConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    notification_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScheduledQuery.NotificationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    query_string: builtins.str,
    schedule_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScheduledQuery.ScheduleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    scheduled_query_execution_role_arn: builtins.str,
    client_token: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    scheduled_query_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    target_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScheduledQuery.TargetConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42e5a389d6d8bd3d1ce3b11086466e67d628325755910bd1a3c548b00ffcfe93(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bc8011b2365888fe7a380f1ba5a36fb7ed1f8000d3f7bb10b1d7f0cea6ee8ce(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb7defeed6aa22df8fac8ffd2a8a11911c1c98afe084e662220ea2d6b749cf6b(
    value: typing.Union[_IResolvable_da3f097b, CfnScheduledQuery.ErrorReportConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6ac8f7698b5772e1a500b55701a8ec9f78516f145d63622ae68a8e5545f29e6(
    value: typing.Union[_IResolvable_da3f097b, CfnScheduledQuery.NotificationConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__350bef101d4375adfdded124038da261adba0b0cd8ff0163079f9a3e4ab2fa36(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__879b9ea129031bffd99904fa4ee3a65eea8e9b9983d6d2765f67314bbc2a58e8(
    value: typing.Union[_IResolvable_da3f097b, CfnScheduledQuery.ScheduleConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9604d93296dd77d676d4aaee7f32cfff5d41a5a5ddea40af8a47241cc11bc24(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b0dd0e140b14315dea4d20b97d7e43e67078325c22af76b9335246185be1bf2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e3fb74e7cb6c02c6c793efc3b537bfb39626eef1e4b767afbb9f9aefb9b9609(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1d37c1a239896519d1c42b63f110aa1c29f1bf41df02b83bbe8b432c63d000a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce0d7d8459caf5a03fcbc9365acf392dda9e2785efecf27982e7378d5a93921b(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b44979dc34f6dc90d3fdf79577b6e0af6fc57980ca3d0760ff21b0db7ea27c39(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnScheduledQuery.TargetConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__777d29ff1772204d748efd0bdbbc3a0cc79f8df893bb747ef6f3ff489ce7b0a8(
    *,
    dimension_value_type: builtins.str,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fe12737c843bf8018d182ab621e156cd06646166dd75ee81f8ef4a09be3743a(
    *,
    s3_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScheduledQuery.S3ConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86791c8890b0bf1d095da076392a23e4f575ec15705a623918aae1c043d36c5b(
    *,
    measure_value_type: builtins.str,
    measure_name: typing.Optional[builtins.str] = None,
    multi_measure_attribute_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScheduledQuery.MultiMeasureAttributeMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    source_column: typing.Optional[builtins.str] = None,
    target_measure_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee03ab7385a70723437ab533f3015a5bf3d91b15c5a09b8c34da5d1ea264dc65(
    *,
    measure_value_type: builtins.str,
    source_column: builtins.str,
    target_multi_measure_attribute_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62c61c58c8fd4b88c107b94c840d9e4d63330934b833fb6af43a9907c476779f(
    *,
    multi_measure_attribute_mappings: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScheduledQuery.MultiMeasureAttributeMappingProperty, typing.Dict[builtins.str, typing.Any]]]]],
    target_multi_measure_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b4558fe9ddfa929e6b87d7e1fa0cd9d8b94dfa883bdac1bd63d056e227f35f0(
    *,
    sns_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScheduledQuery.SnsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2cd5f818ee1def696fbf7cfe15d2b108e29ea53bf63e3a782e441942af00835(
    *,
    bucket_name: builtins.str,
    encryption_option: typing.Optional[builtins.str] = None,
    object_key_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__123e13337f60109858734f464accee4f30c7120ff2f0233289d3556f45d70095(
    *,
    schedule_expression: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05872c0f7f29313fe53bfce1afb4034a8b29bd5729076a86910e55eebc988286(
    *,
    topic_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08bb6d784035ed51b729ccce188db2e8804c4da2d66a7486549f9e0eb57bd928(
    *,
    timestream_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScheduledQuery.TimestreamConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49a5caa804573ad68d3177dfcc603fd8d8930af6649634eb4f6d1c6c7ceb19eb(
    *,
    database_name: builtins.str,
    dimension_mappings: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScheduledQuery.DimensionMappingProperty, typing.Dict[builtins.str, typing.Any]]]]],
    table_name: builtins.str,
    time_column: builtins.str,
    measure_name_column: typing.Optional[builtins.str] = None,
    mixed_measure_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScheduledQuery.MixedMeasureMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    multi_measure_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScheduledQuery.MultiMeasureMappingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2caf5d9713b0dd130de3eaf553fcdda6f169bfdde6f8f293349239a734d19010(
    *,
    error_report_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScheduledQuery.ErrorReportConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    notification_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScheduledQuery.NotificationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    query_string: builtins.str,
    schedule_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScheduledQuery.ScheduleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    scheduled_query_execution_role_arn: builtins.str,
    client_token: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    scheduled_query_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    target_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScheduledQuery.TargetConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aad96eaee00841ee49968da22b6ed13b3777f265d71c1981b2f1b217cf0db5fd(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    database_name: builtins.str,
    magnetic_store_write_properties: typing.Any = None,
    retention_properties: typing.Any = None,
    table_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e1f672b6c3046841d69f96c6b256cf927db52e0b4f4cd165e7022a893b539b1(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bce41cd8d4cbef6b9eee9051e83083ebfd8194941c7349171e844f0c59db0f78(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e86eb21a358133850347dfd746769a6d1446d47d303f3a0491f2235ed3136b11(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58178ccb289368b799599c9ec47acf86a335f70eaf713c6562b4b5714d8354e0(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7ed60d3a1390fe9d904e5be80332e4919f8cc331f6a9c78e2c46569bb125df6(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd18b0f7dd5d02d260ec7f2eaec2e2b9b2ab172a6763f2f391fc93ea1f562de6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b21aea3e87d0ba84d4dcca0e9c65c1478588d9aacadd5d365ad9d63d17b025f6(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3715f3b01c0f5179420758f44caa8c4febf57c507d65c9222714b52bbdfc3cf4(
    *,
    s3_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.S3ConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73eb42c14a8651455e1beb5676ed25ea12aff08495097fc56c3d8adcf38dc77d(
    *,
    enable_magnetic_store_writes: typing.Union[builtins.bool, _IResolvable_da3f097b],
    magnetic_store_rejected_data_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.MagneticStoreRejectedDataLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d96ad0456f88b9bdc9094b197d35b5a25aebf85c67723143187828e4d58ee78(
    *,
    magnetic_store_retention_period_in_days: typing.Optional[builtins.str] = None,
    memory_store_retention_period_in_hours: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b50e041ecb4eab9fe02a29c9d1c8c5a1325b090b4a8e835dd2f0242b6754d868(
    *,
    bucket_name: builtins.str,
    encryption_option: builtins.str,
    kms_key_id: typing.Optional[builtins.str] = None,
    object_key_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9edb9a2aaa51342f4db373e24edd938478a52c96340bde2bc89fe7b86eb4431(
    *,
    database_name: builtins.str,
    magnetic_store_write_properties: typing.Any = None,
    retention_properties: typing.Any = None,
    table_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
