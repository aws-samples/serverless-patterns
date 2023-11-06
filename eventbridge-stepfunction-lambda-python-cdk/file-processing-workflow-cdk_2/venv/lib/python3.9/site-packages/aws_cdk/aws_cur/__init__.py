'''
# AWS::CUR Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_cur as cur
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for CUR construct libraries](https://constructs.dev/search?q=cur)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::CUR resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CUR.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::CUR](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CUR.html).

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
class CfnReportDefinition(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cur.CfnReportDefinition",
):
    '''The definition of AWS Cost and Usage Report.

    You can specify the report name, time unit, report format, compression format, S3 bucket, additional artifacts, and schema elements in the definition.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cur as cur
        
        cfn_report_definition = cur.CfnReportDefinition(self, "MyCfnReportDefinition",
            compression="compression",
            format="format",
            refresh_closed_reports=False,
            report_name="reportName",
            report_versioning="reportVersioning",
            s3_bucket="s3Bucket",
            s3_prefix="s3Prefix",
            s3_region="s3Region",
            time_unit="timeUnit",
        
            # the properties below are optional
            additional_artifacts=["additionalArtifacts"],
            additional_schema_elements=["additionalSchemaElements"],
            billing_view_arn="billingViewArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        compression: builtins.str,
        format: builtins.str,
        refresh_closed_reports: typing.Union[builtins.bool, _IResolvable_da3f097b],
        report_name: builtins.str,
        report_versioning: builtins.str,
        s3_bucket: builtins.str,
        s3_prefix: builtins.str,
        s3_region: builtins.str,
        time_unit: builtins.str,
        additional_artifacts: typing.Optional[typing.Sequence[builtins.str]] = None,
        additional_schema_elements: typing.Optional[typing.Sequence[builtins.str]] = None,
        billing_view_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param compression: The compression format that Amazon Web Services uses for the report.
        :param format: The format that Amazon Web Services saves the report in.
        :param refresh_closed_reports: Whether you want AWS to update your reports after they have been finalized if AWS detects charges related to previous months. These charges can include refunds, credits, or support fees.
        :param report_name: The name of the report that you want to create. The name must be unique, is case sensitive, and can't include spaces.
        :param report_versioning: Whether you want AWS to overwrite the previous version of each report or to deliver the report in addition to the previous versions.
        :param s3_bucket: The S3 bucket where Amazon Web Services delivers the report.
        :param s3_prefix: The prefix that Amazon Web Services adds to the report name when Amazon Web Services delivers the report. Your prefix can't include spaces.
        :param s3_region: The Region of the S3 bucket that Amazon Web Services delivers the report into.
        :param time_unit: The granularity of the line items in the report.
        :param additional_artifacts: A list of manifests that you want AWS to create for this report.
        :param additional_schema_elements: A list of strings that indicate additional content that AWS includes in the report, such as individual resource IDs.
        :param billing_view_arn: The Amazon Resource Name (ARN) of the billing view. You can get this value by using the billing view service public APIs.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa6a90098f39859b607fa8b8453bf94b62703cdf41682ff1f90c565abdedbb57)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnReportDefinitionProps(
            compression=compression,
            format=format,
            refresh_closed_reports=refresh_closed_reports,
            report_name=report_name,
            report_versioning=report_versioning,
            s3_bucket=s3_bucket,
            s3_prefix=s3_prefix,
            s3_region=s3_region,
            time_unit=time_unit,
            additional_artifacts=additional_artifacts,
            additional_schema_elements=additional_schema_elements,
            billing_view_arn=billing_view_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e753195458a5ffa83a48c74959905c1f01ecb8fa907ac7bcbac64b0a6d68dd47)
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
            type_hints = typing.get_type_hints(_typecheckingstub__49a34de71362513b65d671ed5a8cc4f1256846af64b8723539bee23178d4a74e)
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
    @jsii.member(jsii_name="compression")
    def compression(self) -> builtins.str:
        '''The compression format that Amazon Web Services uses for the report.'''
        return typing.cast(builtins.str, jsii.get(self, "compression"))

    @compression.setter
    def compression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cafa41fab07d965c2b4cd4f220b0815bee4bbbc73aeb0b1701ff27fe2221def)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compression", value)

    @builtins.property
    @jsii.member(jsii_name="format")
    def format(self) -> builtins.str:
        '''The format that Amazon Web Services saves the report in.'''
        return typing.cast(builtins.str, jsii.get(self, "format"))

    @format.setter
    def format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d7f82d91b0fb169b460470cde1ce29f66d5f2bcfe68c47c86ad3318c4aa6d6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "format", value)

    @builtins.property
    @jsii.member(jsii_name="refreshClosedReports")
    def refresh_closed_reports(
        self,
    ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Whether you want AWS to update your reports after they have been finalized if AWS detects charges related to previous months.'''
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], jsii.get(self, "refreshClosedReports"))

    @refresh_closed_reports.setter
    def refresh_closed_reports(
        self,
        value: typing.Union[builtins.bool, _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ccec559f362c0e5cc75f65e0abbd93286b4e471ccf2c07bd050c10afc226d26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "refreshClosedReports", value)

    @builtins.property
    @jsii.member(jsii_name="reportName")
    def report_name(self) -> builtins.str:
        '''The name of the report that you want to create.'''
        return typing.cast(builtins.str, jsii.get(self, "reportName"))

    @report_name.setter
    def report_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f2e431f6887ff705738ea0e6e2eb792a7b45801bb7d4cc2ec2210dc8eaf8abc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reportName", value)

    @builtins.property
    @jsii.member(jsii_name="reportVersioning")
    def report_versioning(self) -> builtins.str:
        '''Whether you want AWS to overwrite the previous version of each report or to deliver the report in addition to the previous versions.'''
        return typing.cast(builtins.str, jsii.get(self, "reportVersioning"))

    @report_versioning.setter
    def report_versioning(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c89251c983f93a0e40bd215a47173541010324050a11e2311469e065ab0b17c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reportVersioning", value)

    @builtins.property
    @jsii.member(jsii_name="s3Bucket")
    def s3_bucket(self) -> builtins.str:
        '''The S3 bucket where Amazon Web Services delivers the report.'''
        return typing.cast(builtins.str, jsii.get(self, "s3Bucket"))

    @s3_bucket.setter
    def s3_bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ef6cce4061a41668bba78905c8f1dc058df59d7f7070debb5af44a0e4296533)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3Bucket", value)

    @builtins.property
    @jsii.member(jsii_name="s3Prefix")
    def s3_prefix(self) -> builtins.str:
        '''The prefix that Amazon Web Services adds to the report name when Amazon Web Services delivers the report.'''
        return typing.cast(builtins.str, jsii.get(self, "s3Prefix"))

    @s3_prefix.setter
    def s3_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b12b36c345387f3327726fae5967e371eb7c12a662df0a9f06d97b9b3f514acb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3Prefix", value)

    @builtins.property
    @jsii.member(jsii_name="s3Region")
    def s3_region(self) -> builtins.str:
        '''The Region of the S3 bucket that Amazon Web Services delivers the report into.'''
        return typing.cast(builtins.str, jsii.get(self, "s3Region"))

    @s3_region.setter
    def s3_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b68bd9a7c727e9f615699f7f7e4122093cb79d4f703c486f605c986ca0507a35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3Region", value)

    @builtins.property
    @jsii.member(jsii_name="timeUnit")
    def time_unit(self) -> builtins.str:
        '''The granularity of the line items in the report.'''
        return typing.cast(builtins.str, jsii.get(self, "timeUnit"))

    @time_unit.setter
    def time_unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d98ca474f2a8df98b310362b6786a2669ffd62a5759ae59af1c951a85ff8fd75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeUnit", value)

    @builtins.property
    @jsii.member(jsii_name="additionalArtifacts")
    def additional_artifacts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of manifests that you want AWS to create for this report.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "additionalArtifacts"))

    @additional_artifacts.setter
    def additional_artifacts(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8677929221d62b86e6210e7554bfbc901b8ce66550b2d1cad5fe6c465961299)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalArtifacts", value)

    @builtins.property
    @jsii.member(jsii_name="additionalSchemaElements")
    def additional_schema_elements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of strings that indicate additional content that AWS includes in the report, such as individual resource IDs.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "additionalSchemaElements"))

    @additional_schema_elements.setter
    def additional_schema_elements(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d002f185c62fde709bf248b43cc6ed35a66954f07c4dd2bb5c26dd74334dc7e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalSchemaElements", value)

    @builtins.property
    @jsii.member(jsii_name="billingViewArn")
    def billing_view_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the billing view.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "billingViewArn"))

    @billing_view_arn.setter
    def billing_view_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebad8351aece0a3ddcb05b9d4f522316d4c0fa1aeef4e8017b839b424f98ff7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "billingViewArn", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cur.CfnReportDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={
        "compression": "compression",
        "format": "format",
        "refresh_closed_reports": "refreshClosedReports",
        "report_name": "reportName",
        "report_versioning": "reportVersioning",
        "s3_bucket": "s3Bucket",
        "s3_prefix": "s3Prefix",
        "s3_region": "s3Region",
        "time_unit": "timeUnit",
        "additional_artifacts": "additionalArtifacts",
        "additional_schema_elements": "additionalSchemaElements",
        "billing_view_arn": "billingViewArn",
    },
)
class CfnReportDefinitionProps:
    def __init__(
        self,
        *,
        compression: builtins.str,
        format: builtins.str,
        refresh_closed_reports: typing.Union[builtins.bool, _IResolvable_da3f097b],
        report_name: builtins.str,
        report_versioning: builtins.str,
        s3_bucket: builtins.str,
        s3_prefix: builtins.str,
        s3_region: builtins.str,
        time_unit: builtins.str,
        additional_artifacts: typing.Optional[typing.Sequence[builtins.str]] = None,
        additional_schema_elements: typing.Optional[typing.Sequence[builtins.str]] = None,
        billing_view_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnReportDefinition``.

        :param compression: The compression format that Amazon Web Services uses for the report.
        :param format: The format that Amazon Web Services saves the report in.
        :param refresh_closed_reports: Whether you want AWS to update your reports after they have been finalized if AWS detects charges related to previous months. These charges can include refunds, credits, or support fees.
        :param report_name: The name of the report that you want to create. The name must be unique, is case sensitive, and can't include spaces.
        :param report_versioning: Whether you want AWS to overwrite the previous version of each report or to deliver the report in addition to the previous versions.
        :param s3_bucket: The S3 bucket where Amazon Web Services delivers the report.
        :param s3_prefix: The prefix that Amazon Web Services adds to the report name when Amazon Web Services delivers the report. Your prefix can't include spaces.
        :param s3_region: The Region of the S3 bucket that Amazon Web Services delivers the report into.
        :param time_unit: The granularity of the line items in the report.
        :param additional_artifacts: A list of manifests that you want AWS to create for this report.
        :param additional_schema_elements: A list of strings that indicate additional content that AWS includes in the report, such as individual resource IDs.
        :param billing_view_arn: The Amazon Resource Name (ARN) of the billing view. You can get this value by using the billing view service public APIs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cur as cur
            
            cfn_report_definition_props = cur.CfnReportDefinitionProps(
                compression="compression",
                format="format",
                refresh_closed_reports=False,
                report_name="reportName",
                report_versioning="reportVersioning",
                s3_bucket="s3Bucket",
                s3_prefix="s3Prefix",
                s3_region="s3Region",
                time_unit="timeUnit",
            
                # the properties below are optional
                additional_artifacts=["additionalArtifacts"],
                additional_schema_elements=["additionalSchemaElements"],
                billing_view_arn="billingViewArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cc3d7babce4dfa37a62fc4d0d9b1b67c9fdccfaa09ca549a32d3aab0aee31ed)
            check_type(argname="argument compression", value=compression, expected_type=type_hints["compression"])
            check_type(argname="argument format", value=format, expected_type=type_hints["format"])
            check_type(argname="argument refresh_closed_reports", value=refresh_closed_reports, expected_type=type_hints["refresh_closed_reports"])
            check_type(argname="argument report_name", value=report_name, expected_type=type_hints["report_name"])
            check_type(argname="argument report_versioning", value=report_versioning, expected_type=type_hints["report_versioning"])
            check_type(argname="argument s3_bucket", value=s3_bucket, expected_type=type_hints["s3_bucket"])
            check_type(argname="argument s3_prefix", value=s3_prefix, expected_type=type_hints["s3_prefix"])
            check_type(argname="argument s3_region", value=s3_region, expected_type=type_hints["s3_region"])
            check_type(argname="argument time_unit", value=time_unit, expected_type=type_hints["time_unit"])
            check_type(argname="argument additional_artifacts", value=additional_artifacts, expected_type=type_hints["additional_artifacts"])
            check_type(argname="argument additional_schema_elements", value=additional_schema_elements, expected_type=type_hints["additional_schema_elements"])
            check_type(argname="argument billing_view_arn", value=billing_view_arn, expected_type=type_hints["billing_view_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "compression": compression,
            "format": format,
            "refresh_closed_reports": refresh_closed_reports,
            "report_name": report_name,
            "report_versioning": report_versioning,
            "s3_bucket": s3_bucket,
            "s3_prefix": s3_prefix,
            "s3_region": s3_region,
            "time_unit": time_unit,
        }
        if additional_artifacts is not None:
            self._values["additional_artifacts"] = additional_artifacts
        if additional_schema_elements is not None:
            self._values["additional_schema_elements"] = additional_schema_elements
        if billing_view_arn is not None:
            self._values["billing_view_arn"] = billing_view_arn

    @builtins.property
    def compression(self) -> builtins.str:
        '''The compression format that Amazon Web Services uses for the report.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-compression
        '''
        result = self._values.get("compression")
        assert result is not None, "Required property 'compression' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def format(self) -> builtins.str:
        '''The format that Amazon Web Services saves the report in.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-format
        '''
        result = self._values.get("format")
        assert result is not None, "Required property 'format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def refresh_closed_reports(
        self,
    ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Whether you want AWS to update your reports after they have been finalized if AWS detects charges related to previous months.

        These charges can include refunds, credits, or support fees.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-refreshclosedreports
        '''
        result = self._values.get("refresh_closed_reports")
        assert result is not None, "Required property 'refresh_closed_reports' is missing"
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

    @builtins.property
    def report_name(self) -> builtins.str:
        '''The name of the report that you want to create.

        The name must be unique, is case sensitive, and can't include spaces.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-reportname
        '''
        result = self._values.get("report_name")
        assert result is not None, "Required property 'report_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def report_versioning(self) -> builtins.str:
        '''Whether you want AWS to overwrite the previous version of each report or to deliver the report in addition to the previous versions.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-reportversioning
        '''
        result = self._values.get("report_versioning")
        assert result is not None, "Required property 'report_versioning' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def s3_bucket(self) -> builtins.str:
        '''The S3 bucket where Amazon Web Services delivers the report.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-s3bucket
        '''
        result = self._values.get("s3_bucket")
        assert result is not None, "Required property 's3_bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def s3_prefix(self) -> builtins.str:
        '''The prefix that Amazon Web Services adds to the report name when Amazon Web Services delivers the report.

        Your prefix can't include spaces.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-s3prefix
        '''
        result = self._values.get("s3_prefix")
        assert result is not None, "Required property 's3_prefix' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def s3_region(self) -> builtins.str:
        '''The Region of the S3 bucket that Amazon Web Services delivers the report into.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-s3region
        '''
        result = self._values.get("s3_region")
        assert result is not None, "Required property 's3_region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def time_unit(self) -> builtins.str:
        '''The granularity of the line items in the report.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-timeunit
        '''
        result = self._values.get("time_unit")
        assert result is not None, "Required property 'time_unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_artifacts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of manifests that you want AWS to create for this report.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-additionalartifacts
        '''
        result = self._values.get("additional_artifacts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def additional_schema_elements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of strings that indicate additional content that AWS includes in the report, such as individual resource IDs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-additionalschemaelements
        '''
        result = self._values.get("additional_schema_elements")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def billing_view_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the billing view.

        You can get this value by using the billing view service public APIs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html#cfn-cur-reportdefinition-billingviewarn
        '''
        result = self._values.get("billing_view_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnReportDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnReportDefinition",
    "CfnReportDefinitionProps",
]

publication.publish()

def _typecheckingstub__fa6a90098f39859b607fa8b8453bf94b62703cdf41682ff1f90c565abdedbb57(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    compression: builtins.str,
    format: builtins.str,
    refresh_closed_reports: typing.Union[builtins.bool, _IResolvable_da3f097b],
    report_name: builtins.str,
    report_versioning: builtins.str,
    s3_bucket: builtins.str,
    s3_prefix: builtins.str,
    s3_region: builtins.str,
    time_unit: builtins.str,
    additional_artifacts: typing.Optional[typing.Sequence[builtins.str]] = None,
    additional_schema_elements: typing.Optional[typing.Sequence[builtins.str]] = None,
    billing_view_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e753195458a5ffa83a48c74959905c1f01ecb8fa907ac7bcbac64b0a6d68dd47(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49a34de71362513b65d671ed5a8cc4f1256846af64b8723539bee23178d4a74e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cafa41fab07d965c2b4cd4f220b0815bee4bbbc73aeb0b1701ff27fe2221def(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d7f82d91b0fb169b460470cde1ce29f66d5f2bcfe68c47c86ad3318c4aa6d6c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ccec559f362c0e5cc75f65e0abbd93286b4e471ccf2c07bd050c10afc226d26(
    value: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f2e431f6887ff705738ea0e6e2eb792a7b45801bb7d4cc2ec2210dc8eaf8abc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c89251c983f93a0e40bd215a47173541010324050a11e2311469e065ab0b17c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ef6cce4061a41668bba78905c8f1dc058df59d7f7070debb5af44a0e4296533(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b12b36c345387f3327726fae5967e371eb7c12a662df0a9f06d97b9b3f514acb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b68bd9a7c727e9f615699f7f7e4122093cb79d4f703c486f605c986ca0507a35(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d98ca474f2a8df98b310362b6786a2669ffd62a5759ae59af1c951a85ff8fd75(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8677929221d62b86e6210e7554bfbc901b8ce66550b2d1cad5fe6c465961299(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d002f185c62fde709bf248b43cc6ed35a66954f07c4dd2bb5c26dd74334dc7e2(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebad8351aece0a3ddcb05b9d4f522316d4c0fa1aeef4e8017b839b424f98ff7d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cc3d7babce4dfa37a62fc4d0d9b1b67c9fdccfaa09ca549a32d3aab0aee31ed(
    *,
    compression: builtins.str,
    format: builtins.str,
    refresh_closed_reports: typing.Union[builtins.bool, _IResolvable_da3f097b],
    report_name: builtins.str,
    report_versioning: builtins.str,
    s3_bucket: builtins.str,
    s3_prefix: builtins.str,
    s3_region: builtins.str,
    time_unit: builtins.str,
    additional_artifacts: typing.Optional[typing.Sequence[builtins.str]] = None,
    additional_schema_elements: typing.Optional[typing.Sequence[builtins.str]] = None,
    billing_view_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
