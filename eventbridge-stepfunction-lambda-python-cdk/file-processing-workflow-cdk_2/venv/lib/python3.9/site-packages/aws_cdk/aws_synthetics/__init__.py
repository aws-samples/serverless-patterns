'''
# AWS::Synthetics Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_synthetics as synthetics
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Synthetics construct libraries](https://constructs.dev/search?q=synthetics)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Synthetics resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Synthetics.html) directly.

> An experimental construct library for this service is available in preview. Since it is not stable yet, it is distributed
> as a separate package so that you can pin its version independently of the rest of the CDK. See the package:
>
> <span class="package-reference">@aws-cdk/aws-synthetics-alpha</span>

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Synthetics](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Synthetics.html).

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
class CfnCanary(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_synthetics.CfnCanary",
):
    '''Creates or updates a canary.

    Canaries are scripts that monitor your endpoints and APIs from the outside-in. Canaries help you check the availability and latency of your web services and troubleshoot anomalies by investigating load time data, screenshots of the UI, logs, and metrics. You can set up a canary to run continuously or just once.

    To create canaries, you must have the ``CloudWatchSyntheticsFullAccess`` policy. If you are creating a new IAM role for the canary, you also need the the ``iam:CreateRole`` , ``iam:CreatePolicy`` and ``iam:AttachRolePolicy`` permissions. For more information, see `Necessary Roles and Permissions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Roles>`_ .

    Do not include secrets or proprietary information in your canary names. The canary name makes up part of the Amazon Resource Name (ARN) for the canary, and the ARN is included in outbound calls over the internet. For more information, see `Security Considerations for Synthetics Canaries <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/servicelens_canaries_security.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_synthetics as synthetics
        
        cfn_canary = synthetics.CfnCanary(self, "MyCfnCanary",
            artifact_s3_location="artifactS3Location",
            code=synthetics.CfnCanary.CodeProperty(
                handler="handler",
        
                # the properties below are optional
                s3_bucket="s3Bucket",
                s3_key="s3Key",
                s3_object_version="s3ObjectVersion",
                script="script",
                source_location_arn="sourceLocationArn"
            ),
            execution_role_arn="executionRoleArn",
            name="name",
            runtime_version="runtimeVersion",
            schedule=synthetics.CfnCanary.ScheduleProperty(
                expression="expression",
        
                # the properties below are optional
                duration_in_seconds="durationInSeconds"
            ),
        
            # the properties below are optional
            artifact_config=synthetics.CfnCanary.ArtifactConfigProperty(
                s3_encryption=synthetics.CfnCanary.S3EncryptionProperty(
                    encryption_mode="encryptionMode",
                    kms_key_arn="kmsKeyArn"
                )
            ),
            delete_lambda_resources_on_canary_deletion=False,
            failure_retention_period=123,
            run_config=synthetics.CfnCanary.RunConfigProperty(
                active_tracing=False,
                environment_variables={
                    "environment_variables_key": "environmentVariables"
                },
                memory_in_mb=123,
                timeout_in_seconds=123
            ),
            start_canary_after_creation=False,
            success_retention_period=123,
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            visual_reference=synthetics.CfnCanary.VisualReferenceProperty(
                base_canary_run_id="baseCanaryRunId",
        
                # the properties below are optional
                base_screenshots=[synthetics.CfnCanary.BaseScreenshotProperty(
                    screenshot_name="screenshotName",
        
                    # the properties below are optional
                    ignore_coordinates=["ignoreCoordinates"]
                )]
            ),
            vpc_config=synthetics.CfnCanary.VPCConfigProperty(
                security_group_ids=["securityGroupIds"],
                subnet_ids=["subnetIds"],
        
                # the properties below are optional
                vpc_id="vpcId"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        artifact_s3_location: builtins.str,
        code: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCanary.CodeProperty", typing.Dict[builtins.str, typing.Any]]],
        execution_role_arn: builtins.str,
        name: builtins.str,
        runtime_version: builtins.str,
        schedule: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCanary.ScheduleProperty", typing.Dict[builtins.str, typing.Any]]],
        artifact_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCanary.ArtifactConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        delete_lambda_resources_on_canary_deletion: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        failure_retention_period: typing.Optional[jsii.Number] = None,
        run_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCanary.RunConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        start_canary_after_creation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        success_retention_period: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        visual_reference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCanary.VisualReferenceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCanary.VPCConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param artifact_s3_location: The location in Amazon S3 where Synthetics stores artifacts from the runs of this canary. Artifacts include the log file, screenshots, and HAR files. Specify the full location path, including ``s3://`` at the beginning of the path.
        :param code: Use this structure to input your script code for the canary. This structure contains the Lambda handler with the location where the canary should start running the script. If the script is stored in an S3 bucket, the bucket name, key, and version are also included. If the script is passed into the canary directly, the script code is contained in the value of ``Script`` .
        :param execution_role_arn: The ARN of the IAM role to be used to run the canary. This role must already exist, and must include ``lambda.amazonaws.com`` as a principal in the trust policy. The role must also have the following permissions: - ``s3:PutObject`` - ``s3:GetBucketLocation`` - ``s3:ListAllMyBuckets`` - ``cloudwatch:PutMetricData`` - ``logs:CreateLogGroup`` - ``logs:CreateLogStream`` - ``logs:PutLogEvents``
        :param name: The name for this canary. Be sure to give it a descriptive name that distinguishes it from other canaries in your account. Do not include secrets or proprietary information in your canary names. The canary name makes up part of the canary ARN, and the ARN is included in outbound calls over the internet. For more information, see `Security Considerations for Synthetics Canaries <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/servicelens_canaries_security.html>`_ .
        :param runtime_version: Specifies the runtime version to use for the canary. For more information about runtime versions, see `Canary Runtime Versions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html>`_ .
        :param schedule: A structure that contains information about how often the canary is to run, and when these runs are to stop.
        :param artifact_config: A structure that contains the configuration for canary artifacts, including the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3.
        :param delete_lambda_resources_on_canary_deletion: (deprecated) Deletes associated lambda resources created by Synthetics if set to True. Default is False
        :param failure_retention_period: The number of days to retain data about failed runs of this canary. If you omit this field, the default of 31 days is used. The valid range is 1 to 455 days.
        :param run_config: A structure that contains input information for a canary run. If you omit this structure, the frequency of the canary is used as canary's timeout value, up to a maximum of 900 seconds.
        :param start_canary_after_creation: Specify TRUE to have the canary start making runs immediately after it is created. A canary that you create using CloudFormation can't be used to monitor the CloudFormation stack that creates the canary or to roll back that stack if there is a failure.
        :param success_retention_period: The number of days to retain data about successful runs of this canary. If you omit this field, the default of 31 days is used. The valid range is 1 to 455 days.
        :param tags: The list of key-value pairs that are associated with the canary.
        :param visual_reference: If this canary performs visual monitoring by comparing screenshots, this structure contains the ID of the canary run to use as the baseline for screenshots, and the coordinates of any parts of the screen to ignore during the visual monitoring comparison.
        :param vpc_config: If this canary is to test an endpoint in a VPC, this structure contains information about the subnet and security groups of the VPC endpoint. For more information, see `Running a Canary in a VPC <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_VPC.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8fcb3f48eca9399b4d1d31a5ef709e22f9fa52ad1e174b75d8313ef2b971663)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCanaryProps(
            artifact_s3_location=artifact_s3_location,
            code=code,
            execution_role_arn=execution_role_arn,
            name=name,
            runtime_version=runtime_version,
            schedule=schedule,
            artifact_config=artifact_config,
            delete_lambda_resources_on_canary_deletion=delete_lambda_resources_on_canary_deletion,
            failure_retention_period=failure_retention_period,
            run_config=run_config,
            start_canary_after_creation=start_canary_after_creation,
            success_retention_period=success_retention_period,
            tags=tags,
            visual_reference=visual_reference,
            vpc_config=vpc_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc166bab0fcf177897c1dbb233203e39458428064bc6ff7215b01b2b3ec6f3a2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__65410bca39459dd8b2ef582ab37870de468cb765034b9600759877910b340355)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCodeSourceLocationArn")
    def attr_code_source_location_arn(self) -> builtins.str:
        '''``Ref`` returns the ARN of the Lambda layer where Synthetics stores the canary script code.

        :cloudformationAttribute: Code.SourceLocationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCodeSourceLocationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the canary.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''The state of the canary.

        For example, ``RUNNING`` .

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

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
    @jsii.member(jsii_name="artifactS3Location")
    def artifact_s3_location(self) -> builtins.str:
        '''The location in Amazon S3 where Synthetics stores artifacts from the runs of this canary.'''
        return typing.cast(builtins.str, jsii.get(self, "artifactS3Location"))

    @artifact_s3_location.setter
    def artifact_s3_location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdaba4ac1ed08cbb682b002e6d07aabeaccadbe7c5a6d4bbbc1aaaa15bb4831c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "artifactS3Location", value)

    @builtins.property
    @jsii.member(jsii_name="code")
    def code(self) -> typing.Union[_IResolvable_da3f097b, "CfnCanary.CodeProperty"]:
        '''Use this structure to input your script code for the canary.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCanary.CodeProperty"], jsii.get(self, "code"))

    @code.setter
    def code(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnCanary.CodeProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__940d05df3a63f7ad05e985fa05317d4b896a6a845409a8d700cbf186fd8e49d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "code", value)

    @builtins.property
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> builtins.str:
        '''The ARN of the IAM role to be used to run the canary.'''
        return typing.cast(builtins.str, jsii.get(self, "executionRoleArn"))

    @execution_role_arn.setter
    def execution_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21989f82228cbbd4b8df02c1285ab8cf3635cf4eb894f4a4c999e6b763e92ded)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name for this canary.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02a5568fdb7b5da09cb493a9883d04e695a0b6375532601c26ea6ba719fd869a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="runtimeVersion")
    def runtime_version(self) -> builtins.str:
        '''Specifies the runtime version to use for the canary.'''
        return typing.cast(builtins.str, jsii.get(self, "runtimeVersion"))

    @runtime_version.setter
    def runtime_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64f9d8326de93a51cdd4ab89bc4c5431c218c9b46372d81f4fe7a8961b26fa2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtimeVersion", value)

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnCanary.ScheduleProperty"]:
        '''A structure that contains information about how often the canary is to run, and when these runs are to stop.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCanary.ScheduleProperty"], jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnCanary.ScheduleProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e387628a17b84461f77d8fdc851f2b16bcda58e50d8e9279d02062270a5516f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedule", value)

    @builtins.property
    @jsii.member(jsii_name="artifactConfig")
    def artifact_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCanary.ArtifactConfigProperty"]]:
        '''A structure that contains the configuration for canary artifacts, including the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCanary.ArtifactConfigProperty"]], jsii.get(self, "artifactConfig"))

    @artifact_config.setter
    def artifact_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCanary.ArtifactConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5946ee35eff32e4581a6d2e3e0c69d62cdc3c17f079123211f7251bc1a10d878)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "artifactConfig", value)

    @builtins.property
    @jsii.member(jsii_name="deleteLambdaResourcesOnCanaryDeletion")
    def delete_lambda_resources_on_canary_deletion(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''(deprecated) Deletes associated lambda resources created by Synthetics if set to True.

        :deprecated: this property has been deprecated

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "deleteLambdaResourcesOnCanaryDeletion"))

    @delete_lambda_resources_on_canary_deletion.setter
    def delete_lambda_resources_on_canary_deletion(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__442577c2c36e4274dca25b3d866e1aeec3f4ffc18732e01050131a31f768f2b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteLambdaResourcesOnCanaryDeletion", value)

    @builtins.property
    @jsii.member(jsii_name="failureRetentionPeriod")
    def failure_retention_period(self) -> typing.Optional[jsii.Number]:
        '''The number of days to retain data about failed runs of this canary.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "failureRetentionPeriod"))

    @failure_retention_period.setter
    def failure_retention_period(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02a7e43f45419c4cb8e909f309f8848d4ced91d17b01d14e5ea0b8cec28aab1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failureRetentionPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="runConfig")
    def run_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCanary.RunConfigProperty"]]:
        '''A structure that contains input information for a canary run.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCanary.RunConfigProperty"]], jsii.get(self, "runConfig"))

    @run_config.setter
    def run_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCanary.RunConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e65fb80249e43aebfe46950832be73ed0795003be5d74ca1ef7cd12bb2408557)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runConfig", value)

    @builtins.property
    @jsii.member(jsii_name="startCanaryAfterCreation")
    def start_canary_after_creation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specify TRUE to have the canary start making runs immediately after it is created.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "startCanaryAfterCreation"))

    @start_canary_after_creation.setter
    def start_canary_after_creation(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a98feaf45022b36ef5c9888f87b978029d5e1fde70599e1972543b1778adfad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startCanaryAfterCreation", value)

    @builtins.property
    @jsii.member(jsii_name="successRetentionPeriod")
    def success_retention_period(self) -> typing.Optional[jsii.Number]:
        '''The number of days to retain data about successful runs of this canary.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "successRetentionPeriod"))

    @success_retention_period.setter
    def success_retention_period(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8bbba327f646025c54903ccf2c19cedc26cf07f79658c389f65ef40b263130f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "successRetentionPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The list of key-value pairs that are associated with the canary.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__212d1e59a4bd96a18f447b1c742abcfeb7c668063c8e1670fa0770e339ac4077)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="visualReference")
    def visual_reference(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCanary.VisualReferenceProperty"]]:
        '''If this canary performs visual monitoring by comparing screenshots, this structure contains the ID of the canary run to use as the baseline for screenshots, and the coordinates of any parts of the screen to ignore during the visual monitoring comparison.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCanary.VisualReferenceProperty"]], jsii.get(self, "visualReference"))

    @visual_reference.setter
    def visual_reference(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCanary.VisualReferenceProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21e93a70969fa03a3f0aa85f6b1615a26d9a0afef8a0cf27f0888fc59aef420b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "visualReference", value)

    @builtins.property
    @jsii.member(jsii_name="vpcConfig")
    def vpc_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCanary.VPCConfigProperty"]]:
        '''If this canary is to test an endpoint in a VPC, this structure contains information about the subnet and security groups of the VPC endpoint.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCanary.VPCConfigProperty"]], jsii.get(self, "vpcConfig"))

    @vpc_config.setter
    def vpc_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCanary.VPCConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be63ed6816e3043aef63f6e7c0d0dfcc35f1249735acd4eff8530f8c2253b747)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcConfig", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_synthetics.CfnCanary.ArtifactConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_encryption": "s3Encryption"},
    )
    class ArtifactConfigProperty:
        def __init__(
            self,
            *,
            s3_encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCanary.S3EncryptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A structure that contains the configuration for canary artifacts, including the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3 .

            :param s3_encryption: A structure that contains the configuration of the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3 . Artifact encryption functionality is available only for canaries that use Synthetics runtime version syn-nodejs-puppeteer-3.3 or later. For more information, see `Encrypting canary artifacts <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_artifact_encryption.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-artifactconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_synthetics as synthetics
                
                artifact_config_property = synthetics.CfnCanary.ArtifactConfigProperty(
                    s3_encryption=synthetics.CfnCanary.S3EncryptionProperty(
                        encryption_mode="encryptionMode",
                        kms_key_arn="kmsKeyArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9c456e72742651aec26b46a7fbd663821284d03931fd10859243079b815dad28)
                check_type(argname="argument s3_encryption", value=s3_encryption, expected_type=type_hints["s3_encryption"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if s3_encryption is not None:
                self._values["s3_encryption"] = s3_encryption

        @builtins.property
        def s3_encryption(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCanary.S3EncryptionProperty"]]:
            '''A structure that contains the configuration of the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3 .

            Artifact encryption functionality is available only for canaries that use Synthetics runtime version syn-nodejs-puppeteer-3.3 or later. For more information, see `Encrypting canary artifacts <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_artifact_encryption.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-artifactconfig.html#cfn-synthetics-canary-artifactconfig-s3encryption
            '''
            result = self._values.get("s3_encryption")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCanary.S3EncryptionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ArtifactConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_synthetics.CfnCanary.BaseScreenshotProperty",
        jsii_struct_bases=[],
        name_mapping={
            "screenshot_name": "screenshotName",
            "ignore_coordinates": "ignoreCoordinates",
        },
    )
    class BaseScreenshotProperty:
        def __init__(
            self,
            *,
            screenshot_name: builtins.str,
            ignore_coordinates: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''A structure representing a screenshot that is used as a baseline during visual monitoring comparisons made by the canary.

            :param screenshot_name: The name of the screenshot. This is generated the first time the canary is run after the ``UpdateCanary`` operation that specified for this canary to perform visual monitoring.
            :param ignore_coordinates: Coordinates that define the part of a screen to ignore during screenshot comparisons. To obtain the coordinates to use here, use the CloudWatch console to draw the boundaries on the screen. For more information, see `Edit or delete a canary <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/synthetics_canaries_deletion.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-basescreenshot.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_synthetics as synthetics
                
                base_screenshot_property = synthetics.CfnCanary.BaseScreenshotProperty(
                    screenshot_name="screenshotName",
                
                    # the properties below are optional
                    ignore_coordinates=["ignoreCoordinates"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8d401a2416919aef18322e23fb875fc37ad8f90f34f8f5708a245f22f9d3208f)
                check_type(argname="argument screenshot_name", value=screenshot_name, expected_type=type_hints["screenshot_name"])
                check_type(argname="argument ignore_coordinates", value=ignore_coordinates, expected_type=type_hints["ignore_coordinates"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "screenshot_name": screenshot_name,
            }
            if ignore_coordinates is not None:
                self._values["ignore_coordinates"] = ignore_coordinates

        @builtins.property
        def screenshot_name(self) -> builtins.str:
            '''The name of the screenshot.

            This is generated the first time the canary is run after the ``UpdateCanary`` operation that specified for this canary to perform visual monitoring.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-basescreenshot.html#cfn-synthetics-canary-basescreenshot-screenshotname
            '''
            result = self._values.get("screenshot_name")
            assert result is not None, "Required property 'screenshot_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def ignore_coordinates(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Coordinates that define the part of a screen to ignore during screenshot comparisons.

            To obtain the coordinates to use here, use the CloudWatch console to draw the boundaries on the screen. For more information, see `Edit or delete a canary <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/synthetics_canaries_deletion.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-basescreenshot.html#cfn-synthetics-canary-basescreenshot-ignorecoordinates
            '''
            result = self._values.get("ignore_coordinates")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BaseScreenshotProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_synthetics.CfnCanary.CodeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "handler": "handler",
            "s3_bucket": "s3Bucket",
            "s3_key": "s3Key",
            "s3_object_version": "s3ObjectVersion",
            "script": "script",
            "source_location_arn": "sourceLocationArn",
        },
    )
    class CodeProperty:
        def __init__(
            self,
            *,
            handler: builtins.str,
            s3_bucket: typing.Optional[builtins.str] = None,
            s3_key: typing.Optional[builtins.str] = None,
            s3_object_version: typing.Optional[builtins.str] = None,
            script: typing.Optional[builtins.str] = None,
            source_location_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Use this structure to input your script code for the canary.

            This structure contains the Lambda handler with the location where the canary should start running the script. If the script is stored in an S3 bucket, the bucket name, key, and version are also included. If the script is passed into the canary directly, the script code is contained in the value of ``Script`` .

            :param handler: The entry point to use for the source code when running the canary. For canaries that use the ``syn-python-selenium-1.0`` runtime or a ``syn-nodejs.puppeteer`` runtime earlier than ``syn-nodejs.puppeteer-3.4`` , the handler must be specified as ``*fileName* .handler`` . For ``syn-python-selenium-1.1`` , ``syn-nodejs.puppeteer-3.4`` , and later runtimes, the handler can be specified as ``*fileName* . *functionName*`` , or you can specify a folder where canary scripts reside as ``*folder* / *fileName* . *functionName*`` .
            :param s3_bucket: If your canary script is located in S3, specify the bucket name here. The bucket must already exist.
            :param s3_key: The S3 key of your script. For more information, see `Working with Amazon S3 Objects <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingObjects.html>`_ .
            :param s3_object_version: The S3 version ID of your script.
            :param script: If you input your canary script directly into the canary instead of referring to an S3 location, the value of this parameter is the script in plain text. It can be up to 5 MB.
            :param source_location_arn: The ARN of the Lambda layer where Synthetics stores the canary script code.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_synthetics as synthetics
                
                code_property = synthetics.CfnCanary.CodeProperty(
                    handler="handler",
                
                    # the properties below are optional
                    s3_bucket="s3Bucket",
                    s3_key="s3Key",
                    s3_object_version="s3ObjectVersion",
                    script="script",
                    source_location_arn="sourceLocationArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3d403372a613babc1ab10717d050ec9a7f4055961f3545f2d0600d89c7b3dcc3)
                check_type(argname="argument handler", value=handler, expected_type=type_hints["handler"])
                check_type(argname="argument s3_bucket", value=s3_bucket, expected_type=type_hints["s3_bucket"])
                check_type(argname="argument s3_key", value=s3_key, expected_type=type_hints["s3_key"])
                check_type(argname="argument s3_object_version", value=s3_object_version, expected_type=type_hints["s3_object_version"])
                check_type(argname="argument script", value=script, expected_type=type_hints["script"])
                check_type(argname="argument source_location_arn", value=source_location_arn, expected_type=type_hints["source_location_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "handler": handler,
            }
            if s3_bucket is not None:
                self._values["s3_bucket"] = s3_bucket
            if s3_key is not None:
                self._values["s3_key"] = s3_key
            if s3_object_version is not None:
                self._values["s3_object_version"] = s3_object_version
            if script is not None:
                self._values["script"] = script
            if source_location_arn is not None:
                self._values["source_location_arn"] = source_location_arn

        @builtins.property
        def handler(self) -> builtins.str:
            '''The entry point to use for the source code when running the canary.

            For canaries that use the ``syn-python-selenium-1.0`` runtime or a ``syn-nodejs.puppeteer`` runtime earlier than ``syn-nodejs.puppeteer-3.4`` , the handler must be specified as ``*fileName* .handler`` . For ``syn-python-selenium-1.1`` , ``syn-nodejs.puppeteer-3.4`` , and later runtimes, the handler can be specified as ``*fileName* . *functionName*`` , or you can specify a folder where canary scripts reside as ``*folder* / *fileName* . *functionName*`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html#cfn-synthetics-canary-code-handler
            '''
            result = self._values.get("handler")
            assert result is not None, "Required property 'handler' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_bucket(self) -> typing.Optional[builtins.str]:
            '''If your canary script is located in S3, specify the bucket name here.

            The bucket must already exist.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html#cfn-synthetics-canary-code-s3bucket
            '''
            result = self._values.get("s3_bucket")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_key(self) -> typing.Optional[builtins.str]:
            '''The S3 key of your script.

            For more information, see `Working with Amazon S3 Objects <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingObjects.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html#cfn-synthetics-canary-code-s3key
            '''
            result = self._values.get("s3_key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_object_version(self) -> typing.Optional[builtins.str]:
            '''The S3 version ID of your script.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html#cfn-synthetics-canary-code-s3objectversion
            '''
            result = self._values.get("s3_object_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def script(self) -> typing.Optional[builtins.str]:
            '''If you input your canary script directly into the canary instead of referring to an S3 location, the value of this parameter is the script in plain text.

            It can be up to 5 MB.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html#cfn-synthetics-canary-code-script
            '''
            result = self._values.get("script")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source_location_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the Lambda layer where Synthetics stores the canary script code.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html#cfn-synthetics-canary-code-sourcelocationarn
            '''
            result = self._values.get("source_location_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CodeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_synthetics.CfnCanary.RunConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "active_tracing": "activeTracing",
            "environment_variables": "environmentVariables",
            "memory_in_mb": "memoryInMb",
            "timeout_in_seconds": "timeoutInSeconds",
        },
    )
    class RunConfigProperty:
        def __init__(
            self,
            *,
            active_tracing: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            environment_variables: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
            memory_in_mb: typing.Optional[jsii.Number] = None,
            timeout_in_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''A structure that contains input information for a canary run.

            This structure is required.

            :param active_tracing: Specifies whether this canary is to use active AWS X-Ray tracing when it runs. Active tracing enables this canary run to be displayed in the ServiceLens and X-Ray service maps even if the canary does not hit an endpoint that has X-Ray tracing enabled. Using X-Ray tracing incurs charges. For more information, see `Canaries and X-Ray tracing <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_tracing.html>`_ . You can enable active tracing only for canaries that use version ``syn-nodejs-2.0`` or later for their canary runtime.
            :param environment_variables: Specifies the keys and values to use for any environment variables used in the canary script. Use the following format: { "key1" : "value1", "key2" : "value2", ...} Keys must start with a letter and be at least two characters. The total size of your environment variables cannot exceed 4 KB. You can't specify any Lambda reserved environment variables as the keys for your environment variables. For more information about reserved keys, see `Runtime environment variables <https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-runtime>`_ .
            :param memory_in_mb: The maximum amount of memory that the canary can use while running. This value must be a multiple of 64. The range is 960 to 3008.
            :param timeout_in_seconds: How long the canary is allowed to run before it must stop. You can't set this time to be longer than the frequency of the runs of this canary. If you omit this field, the frequency of the canary is used as this value, up to a maximum of 900 seconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-runconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_synthetics as synthetics
                
                run_config_property = synthetics.CfnCanary.RunConfigProperty(
                    active_tracing=False,
                    environment_variables={
                        "environment_variables_key": "environmentVariables"
                    },
                    memory_in_mb=123,
                    timeout_in_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fa148862e82948accbbe951e7afcee721aa7014754c81106d2648fe1c5cf28e2)
                check_type(argname="argument active_tracing", value=active_tracing, expected_type=type_hints["active_tracing"])
                check_type(argname="argument environment_variables", value=environment_variables, expected_type=type_hints["environment_variables"])
                check_type(argname="argument memory_in_mb", value=memory_in_mb, expected_type=type_hints["memory_in_mb"])
                check_type(argname="argument timeout_in_seconds", value=timeout_in_seconds, expected_type=type_hints["timeout_in_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if active_tracing is not None:
                self._values["active_tracing"] = active_tracing
            if environment_variables is not None:
                self._values["environment_variables"] = environment_variables
            if memory_in_mb is not None:
                self._values["memory_in_mb"] = memory_in_mb
            if timeout_in_seconds is not None:
                self._values["timeout_in_seconds"] = timeout_in_seconds

        @builtins.property
        def active_tracing(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether this canary is to use active AWS X-Ray tracing when it runs.

            Active tracing enables this canary run to be displayed in the ServiceLens and X-Ray service maps even if the canary does not hit an endpoint that has X-Ray tracing enabled. Using X-Ray tracing incurs charges. For more information, see `Canaries and X-Ray tracing <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_tracing.html>`_ .

            You can enable active tracing only for canaries that use version ``syn-nodejs-2.0`` or later for their canary runtime.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-runconfig.html#cfn-synthetics-canary-runconfig-activetracing
            '''
            result = self._values.get("active_tracing")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def environment_variables(
            self,
        ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
            '''Specifies the keys and values to use for any environment variables used in the canary script.

            Use the following format:

            { "key1" : "value1", "key2" : "value2", ...}

            Keys must start with a letter and be at least two characters. The total size of your environment variables cannot exceed 4 KB. You can't specify any Lambda reserved environment variables as the keys for your environment variables. For more information about reserved keys, see `Runtime environment variables <https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-runtime>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-runconfig.html#cfn-synthetics-canary-runconfig-environmentvariables
            '''
            result = self._values.get("environment_variables")
            return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], result)

        @builtins.property
        def memory_in_mb(self) -> typing.Optional[jsii.Number]:
            '''The maximum amount of memory that the canary can use while running.

            This value must be a multiple of 64. The range is 960 to 3008.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-runconfig.html#cfn-synthetics-canary-runconfig-memoryinmb
            '''
            result = self._values.get("memory_in_mb")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''How long the canary is allowed to run before it must stop.

            You can't set this time to be longer than the frequency of the runs of this canary.

            If you omit this field, the frequency of the canary is used as this value, up to a maximum of 900 seconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-runconfig.html#cfn-synthetics-canary-runconfig-timeoutinseconds
            '''
            result = self._values.get("timeout_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RunConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_synthetics.CfnCanary.S3EncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={"encryption_mode": "encryptionMode", "kms_key_arn": "kmsKeyArn"},
    )
    class S3EncryptionProperty:
        def __init__(
            self,
            *,
            encryption_mode: typing.Optional[builtins.str] = None,
            kms_key_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A structure that contains the configuration of the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3 .

            Artifact encryption functionality is available only for canaries that use Synthetics runtime version syn-nodejs-puppeteer-3.3 or later. For more information, see `Encrypting canary artifacts <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_artifact_encryption.html>`_ .

            :param encryption_mode: The encryption method to use for artifacts created by this canary. Specify ``SSE_S3`` to use server-side encryption (SSE) with an Amazon S3-managed key. Specify ``SSE-KMS`` to use server-side encryption with a customer-managed AWS KMS key. If you omit this parameter, an AWS -managed AWS KMS key is used.
            :param kms_key_arn: The ARN of the customer-managed AWS KMS key to use, if you specify ``SSE-KMS`` for ``EncryptionMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-s3encryption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_synthetics as synthetics
                
                s3_encryption_property = synthetics.CfnCanary.S3EncryptionProperty(
                    encryption_mode="encryptionMode",
                    kms_key_arn="kmsKeyArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__551aad28104a61040e1d9e12e77c77ae47c6e19a45d15bfa94e441c5d297d3ab)
                check_type(argname="argument encryption_mode", value=encryption_mode, expected_type=type_hints["encryption_mode"])
                check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if encryption_mode is not None:
                self._values["encryption_mode"] = encryption_mode
            if kms_key_arn is not None:
                self._values["kms_key_arn"] = kms_key_arn

        @builtins.property
        def encryption_mode(self) -> typing.Optional[builtins.str]:
            '''The encryption method to use for artifacts created by this canary.

            Specify ``SSE_S3`` to use server-side encryption (SSE) with an Amazon S3-managed key. Specify ``SSE-KMS`` to use server-side encryption with a customer-managed AWS KMS key.

            If you omit this parameter, an AWS -managed AWS KMS key is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-s3encryption.html#cfn-synthetics-canary-s3encryption-encryptionmode
            '''
            result = self._values.get("encryption_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def kms_key_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the customer-managed AWS KMS key to use, if you specify ``SSE-KMS`` for ``EncryptionMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-s3encryption.html#cfn-synthetics-canary-s3encryption-kmskeyarn
            '''
            result = self._values.get("kms_key_arn")
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
        jsii_type="aws-cdk-lib.aws_synthetics.CfnCanary.ScheduleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "expression": "expression",
            "duration_in_seconds": "durationInSeconds",
        },
    )
    class ScheduleProperty:
        def __init__(
            self,
            *,
            expression: builtins.str,
            duration_in_seconds: typing.Optional[builtins.str] = None,
        ) -> None:
            '''This structure specifies how often a canary is to make runs and the date and time when it should stop making runs.

            :param expression: A ``rate`` expression or a ``cron`` expression that defines how often the canary is to run. For a rate expression, The syntax is ``rate( *number unit* )`` . *unit* can be ``minute`` , ``minutes`` , or ``hour`` . For example, ``rate(1 minute)`` runs the canary once a minute, ``rate(10 minutes)`` runs it once every 10 minutes, and ``rate(1 hour)`` runs it once every hour. You can specify a frequency between ``rate(1 minute)`` and ``rate(1 hour)`` . Specifying ``rate(0 minute)`` or ``rate(0 hour)`` is a special value that causes the canary to run only once when it is started. Use ``cron( *expression* )`` to specify a cron expression. You can't schedule a canary to wait for more than a year before running. For information about the syntax for cron expressions, see `Scheduling canary runs using cron <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_cron.html>`_ .
            :param duration_in_seconds: How long, in seconds, for the canary to continue making regular runs according to the schedule in the ``Expression`` value. If you specify 0, the canary continues making runs until you stop it. If you omit this field, the default of 0 is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-schedule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_synthetics as synthetics
                
                schedule_property = synthetics.CfnCanary.ScheduleProperty(
                    expression="expression",
                
                    # the properties below are optional
                    duration_in_seconds="durationInSeconds"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e4999288d0e0c5de04c56a3436208778026602dfdca27710aee93f9f4e034c29)
                check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
                check_type(argname="argument duration_in_seconds", value=duration_in_seconds, expected_type=type_hints["duration_in_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "expression": expression,
            }
            if duration_in_seconds is not None:
                self._values["duration_in_seconds"] = duration_in_seconds

        @builtins.property
        def expression(self) -> builtins.str:
            '''A ``rate`` expression or a ``cron`` expression that defines how often the canary is to run.

            For a rate expression, The syntax is ``rate( *number unit* )`` . *unit* can be ``minute`` , ``minutes`` , or ``hour`` .

            For example, ``rate(1 minute)`` runs the canary once a minute, ``rate(10 minutes)`` runs it once every 10 minutes, and ``rate(1 hour)`` runs it once every hour. You can specify a frequency between ``rate(1 minute)`` and ``rate(1 hour)`` .

            Specifying ``rate(0 minute)`` or ``rate(0 hour)`` is a special value that causes the canary to run only once when it is started.

            Use ``cron( *expression* )`` to specify a cron expression. You can't schedule a canary to wait for more than a year before running. For information about the syntax for cron expressions, see `Scheduling canary runs using cron <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_cron.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-schedule.html#cfn-synthetics-canary-schedule-expression
            '''
            result = self._values.get("expression")
            assert result is not None, "Required property 'expression' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def duration_in_seconds(self) -> typing.Optional[builtins.str]:
            '''How long, in seconds, for the canary to continue making regular runs according to the schedule in the ``Expression`` value.

            If you specify 0, the canary continues making runs until you stop it. If you omit this field, the default of 0 is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-schedule.html#cfn-synthetics-canary-schedule-durationinseconds
            '''
            result = self._values.get("duration_in_seconds")
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
        jsii_type="aws-cdk-lib.aws_synthetics.CfnCanary.VPCConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
            "vpc_id": "vpcId",
        },
    )
    class VPCConfigProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Sequence[builtins.str],
            subnet_ids: typing.Sequence[builtins.str],
            vpc_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''If this canary is to test an endpoint in a VPC, this structure contains information about the subnet and security groups of the VPC endpoint.

            For more information, see `Running a Canary in a VPC <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_VPC.html>`_ .

            :param security_group_ids: The IDs of the security groups for this canary.
            :param subnet_ids: The IDs of the subnets where this canary is to run.
            :param vpc_id: The ID of the VPC where this canary is to run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-vpcconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_synthetics as synthetics
                
                v_pCConfig_property = synthetics.CfnCanary.VPCConfigProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"],
                
                    # the properties below are optional
                    vpc_id="vpcId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__eccfde82eb2354e9c416fba506f2ff8e4fb1a86792529f65e2d8eafbc8415074)
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
                check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "security_group_ids": security_group_ids,
                "subnet_ids": subnet_ids,
            }
            if vpc_id is not None:
                self._values["vpc_id"] = vpc_id

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            '''The IDs of the security groups for this canary.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-vpcconfig.html#cfn-synthetics-canary-vpcconfig-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnet_ids(self) -> typing.List[builtins.str]:
            '''The IDs of the subnets where this canary is to run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-vpcconfig.html#cfn-synthetics-canary-vpcconfig-subnetids
            '''
            result = self._values.get("subnet_ids")
            assert result is not None, "Required property 'subnet_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def vpc_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the VPC where this canary is to run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-vpcconfig.html#cfn-synthetics-canary-vpcconfig-vpcid
            '''
            result = self._values.get("vpc_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VPCConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_synthetics.CfnCanary.VisualReferenceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "base_canary_run_id": "baseCanaryRunId",
            "base_screenshots": "baseScreenshots",
        },
    )
    class VisualReferenceProperty:
        def __init__(
            self,
            *,
            base_canary_run_id: builtins.str,
            base_screenshots: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCanary.BaseScreenshotProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Defines the screenshots to use as the baseline for comparisons during visual monitoring comparisons during future runs of this canary.

            If you omit this parameter, no changes are made to any baseline screenshots that the canary might be using already.

            Visual monitoring is supported only on canaries running the *syn-puppeteer-node-3.2* runtime or later. For more information, see `Visual monitoring <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_SyntheticsLogger_VisualTesting.html>`_ and `Visual monitoring blueprint <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Blueprints_VisualTesting.html>`_

            :param base_canary_run_id: Specifies which canary run to use the screenshots from as the baseline for future visual monitoring with this canary. Valid values are ``nextrun`` to use the screenshots from the next run after this update is made, ``lastrun`` to use the screenshots from the most recent run before this update was made, or the value of ``Id`` in the `CanaryRun <https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryRun.html>`_ from any past run of this canary.
            :param base_screenshots: An array of screenshots that are used as the baseline for comparisons during visual monitoring.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-visualreference.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_synthetics as synthetics
                
                visual_reference_property = synthetics.CfnCanary.VisualReferenceProperty(
                    base_canary_run_id="baseCanaryRunId",
                
                    # the properties below are optional
                    base_screenshots=[synthetics.CfnCanary.BaseScreenshotProperty(
                        screenshot_name="screenshotName",
                
                        # the properties below are optional
                        ignore_coordinates=["ignoreCoordinates"]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f52b6b7318141dc99f6bd36c21b91cda286b67d7dea805791a6132a2cd794526)
                check_type(argname="argument base_canary_run_id", value=base_canary_run_id, expected_type=type_hints["base_canary_run_id"])
                check_type(argname="argument base_screenshots", value=base_screenshots, expected_type=type_hints["base_screenshots"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "base_canary_run_id": base_canary_run_id,
            }
            if base_screenshots is not None:
                self._values["base_screenshots"] = base_screenshots

        @builtins.property
        def base_canary_run_id(self) -> builtins.str:
            '''Specifies which canary run to use the screenshots from as the baseline for future visual monitoring with this canary.

            Valid values are ``nextrun`` to use the screenshots from the next run after this update is made, ``lastrun`` to use the screenshots from the most recent run before this update was made, or the value of ``Id`` in the `CanaryRun <https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryRun.html>`_ from any past run of this canary.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-visualreference.html#cfn-synthetics-canary-visualreference-basecanaryrunid
            '''
            result = self._values.get("base_canary_run_id")
            assert result is not None, "Required property 'base_canary_run_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def base_screenshots(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCanary.BaseScreenshotProperty"]]]]:
            '''An array of screenshots that are used as the baseline for comparisons during visual monitoring.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-visualreference.html#cfn-synthetics-canary-visualreference-basescreenshots
            '''
            result = self._values.get("base_screenshots")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCanary.BaseScreenshotProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VisualReferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_synthetics.CfnCanaryProps",
    jsii_struct_bases=[],
    name_mapping={
        "artifact_s3_location": "artifactS3Location",
        "code": "code",
        "execution_role_arn": "executionRoleArn",
        "name": "name",
        "runtime_version": "runtimeVersion",
        "schedule": "schedule",
        "artifact_config": "artifactConfig",
        "delete_lambda_resources_on_canary_deletion": "deleteLambdaResourcesOnCanaryDeletion",
        "failure_retention_period": "failureRetentionPeriod",
        "run_config": "runConfig",
        "start_canary_after_creation": "startCanaryAfterCreation",
        "success_retention_period": "successRetentionPeriod",
        "tags": "tags",
        "visual_reference": "visualReference",
        "vpc_config": "vpcConfig",
    },
)
class CfnCanaryProps:
    def __init__(
        self,
        *,
        artifact_s3_location: builtins.str,
        code: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.CodeProperty, typing.Dict[builtins.str, typing.Any]]],
        execution_role_arn: builtins.str,
        name: builtins.str,
        runtime_version: builtins.str,
        schedule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.ScheduleProperty, typing.Dict[builtins.str, typing.Any]]],
        artifact_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.ArtifactConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        delete_lambda_resources_on_canary_deletion: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        failure_retention_period: typing.Optional[jsii.Number] = None,
        run_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.RunConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        start_canary_after_creation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        success_retention_period: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        visual_reference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.VisualReferenceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.VPCConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCanary``.

        :param artifact_s3_location: The location in Amazon S3 where Synthetics stores artifacts from the runs of this canary. Artifacts include the log file, screenshots, and HAR files. Specify the full location path, including ``s3://`` at the beginning of the path.
        :param code: Use this structure to input your script code for the canary. This structure contains the Lambda handler with the location where the canary should start running the script. If the script is stored in an S3 bucket, the bucket name, key, and version are also included. If the script is passed into the canary directly, the script code is contained in the value of ``Script`` .
        :param execution_role_arn: The ARN of the IAM role to be used to run the canary. This role must already exist, and must include ``lambda.amazonaws.com`` as a principal in the trust policy. The role must also have the following permissions: - ``s3:PutObject`` - ``s3:GetBucketLocation`` - ``s3:ListAllMyBuckets`` - ``cloudwatch:PutMetricData`` - ``logs:CreateLogGroup`` - ``logs:CreateLogStream`` - ``logs:PutLogEvents``
        :param name: The name for this canary. Be sure to give it a descriptive name that distinguishes it from other canaries in your account. Do not include secrets or proprietary information in your canary names. The canary name makes up part of the canary ARN, and the ARN is included in outbound calls over the internet. For more information, see `Security Considerations for Synthetics Canaries <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/servicelens_canaries_security.html>`_ .
        :param runtime_version: Specifies the runtime version to use for the canary. For more information about runtime versions, see `Canary Runtime Versions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html>`_ .
        :param schedule: A structure that contains information about how often the canary is to run, and when these runs are to stop.
        :param artifact_config: A structure that contains the configuration for canary artifacts, including the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3.
        :param delete_lambda_resources_on_canary_deletion: (deprecated) Deletes associated lambda resources created by Synthetics if set to True. Default is False
        :param failure_retention_period: The number of days to retain data about failed runs of this canary. If you omit this field, the default of 31 days is used. The valid range is 1 to 455 days.
        :param run_config: A structure that contains input information for a canary run. If you omit this structure, the frequency of the canary is used as canary's timeout value, up to a maximum of 900 seconds.
        :param start_canary_after_creation: Specify TRUE to have the canary start making runs immediately after it is created. A canary that you create using CloudFormation can't be used to monitor the CloudFormation stack that creates the canary or to roll back that stack if there is a failure.
        :param success_retention_period: The number of days to retain data about successful runs of this canary. If you omit this field, the default of 31 days is used. The valid range is 1 to 455 days.
        :param tags: The list of key-value pairs that are associated with the canary.
        :param visual_reference: If this canary performs visual monitoring by comparing screenshots, this structure contains the ID of the canary run to use as the baseline for screenshots, and the coordinates of any parts of the screen to ignore during the visual monitoring comparison.
        :param vpc_config: If this canary is to test an endpoint in a VPC, this structure contains information about the subnet and security groups of the VPC endpoint. For more information, see `Running a Canary in a VPC <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_VPC.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_synthetics as synthetics
            
            cfn_canary_props = synthetics.CfnCanaryProps(
                artifact_s3_location="artifactS3Location",
                code=synthetics.CfnCanary.CodeProperty(
                    handler="handler",
            
                    # the properties below are optional
                    s3_bucket="s3Bucket",
                    s3_key="s3Key",
                    s3_object_version="s3ObjectVersion",
                    script="script",
                    source_location_arn="sourceLocationArn"
                ),
                execution_role_arn="executionRoleArn",
                name="name",
                runtime_version="runtimeVersion",
                schedule=synthetics.CfnCanary.ScheduleProperty(
                    expression="expression",
            
                    # the properties below are optional
                    duration_in_seconds="durationInSeconds"
                ),
            
                # the properties below are optional
                artifact_config=synthetics.CfnCanary.ArtifactConfigProperty(
                    s3_encryption=synthetics.CfnCanary.S3EncryptionProperty(
                        encryption_mode="encryptionMode",
                        kms_key_arn="kmsKeyArn"
                    )
                ),
                delete_lambda_resources_on_canary_deletion=False,
                failure_retention_period=123,
                run_config=synthetics.CfnCanary.RunConfigProperty(
                    active_tracing=False,
                    environment_variables={
                        "environment_variables_key": "environmentVariables"
                    },
                    memory_in_mb=123,
                    timeout_in_seconds=123
                ),
                start_canary_after_creation=False,
                success_retention_period=123,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                visual_reference=synthetics.CfnCanary.VisualReferenceProperty(
                    base_canary_run_id="baseCanaryRunId",
            
                    # the properties below are optional
                    base_screenshots=[synthetics.CfnCanary.BaseScreenshotProperty(
                        screenshot_name="screenshotName",
            
                        # the properties below are optional
                        ignore_coordinates=["ignoreCoordinates"]
                    )]
                ),
                vpc_config=synthetics.CfnCanary.VPCConfigProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"],
            
                    # the properties below are optional
                    vpc_id="vpcId"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d869d56ce0d1d2e2add2f80bf39b28abbec2752c719e03194ee540bf1949e423)
            check_type(argname="argument artifact_s3_location", value=artifact_s3_location, expected_type=type_hints["artifact_s3_location"])
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
            check_type(argname="argument execution_role_arn", value=execution_role_arn, expected_type=type_hints["execution_role_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument runtime_version", value=runtime_version, expected_type=type_hints["runtime_version"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument artifact_config", value=artifact_config, expected_type=type_hints["artifact_config"])
            check_type(argname="argument delete_lambda_resources_on_canary_deletion", value=delete_lambda_resources_on_canary_deletion, expected_type=type_hints["delete_lambda_resources_on_canary_deletion"])
            check_type(argname="argument failure_retention_period", value=failure_retention_period, expected_type=type_hints["failure_retention_period"])
            check_type(argname="argument run_config", value=run_config, expected_type=type_hints["run_config"])
            check_type(argname="argument start_canary_after_creation", value=start_canary_after_creation, expected_type=type_hints["start_canary_after_creation"])
            check_type(argname="argument success_retention_period", value=success_retention_period, expected_type=type_hints["success_retention_period"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument visual_reference", value=visual_reference, expected_type=type_hints["visual_reference"])
            check_type(argname="argument vpc_config", value=vpc_config, expected_type=type_hints["vpc_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "artifact_s3_location": artifact_s3_location,
            "code": code,
            "execution_role_arn": execution_role_arn,
            "name": name,
            "runtime_version": runtime_version,
            "schedule": schedule,
        }
        if artifact_config is not None:
            self._values["artifact_config"] = artifact_config
        if delete_lambda_resources_on_canary_deletion is not None:
            self._values["delete_lambda_resources_on_canary_deletion"] = delete_lambda_resources_on_canary_deletion
        if failure_retention_period is not None:
            self._values["failure_retention_period"] = failure_retention_period
        if run_config is not None:
            self._values["run_config"] = run_config
        if start_canary_after_creation is not None:
            self._values["start_canary_after_creation"] = start_canary_after_creation
        if success_retention_period is not None:
            self._values["success_retention_period"] = success_retention_period
        if tags is not None:
            self._values["tags"] = tags
        if visual_reference is not None:
            self._values["visual_reference"] = visual_reference
        if vpc_config is not None:
            self._values["vpc_config"] = vpc_config

    @builtins.property
    def artifact_s3_location(self) -> builtins.str:
        '''The location in Amazon S3 where Synthetics stores artifacts from the runs of this canary.

        Artifacts include the log file, screenshots, and HAR files. Specify the full location path, including ``s3://`` at the beginning of the path.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-artifacts3location
        '''
        result = self._values.get("artifact_s3_location")
        assert result is not None, "Required property 'artifact_s3_location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def code(self) -> typing.Union[_IResolvable_da3f097b, CfnCanary.CodeProperty]:
        '''Use this structure to input your script code for the canary.

        This structure contains the Lambda handler with the location where the canary should start running the script. If the script is stored in an S3 bucket, the bucket name, key, and version are also included. If the script is passed into the canary directly, the script code is contained in the value of ``Script`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-code
        '''
        result = self._values.get("code")
        assert result is not None, "Required property 'code' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnCanary.CodeProperty], result)

    @builtins.property
    def execution_role_arn(self) -> builtins.str:
        '''The ARN of the IAM role to be used to run the canary.

        This role must already exist, and must include ``lambda.amazonaws.com`` as a principal in the trust policy. The role must also have the following permissions:

        - ``s3:PutObject``
        - ``s3:GetBucketLocation``
        - ``s3:ListAllMyBuckets``
        - ``cloudwatch:PutMetricData``
        - ``logs:CreateLogGroup``
        - ``logs:CreateLogStream``
        - ``logs:PutLogEvents``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-executionrolearn
        '''
        result = self._values.get("execution_role_arn")
        assert result is not None, "Required property 'execution_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name for this canary.

        Be sure to give it a descriptive name that distinguishes it from other canaries in your account.

        Do not include secrets or proprietary information in your canary names. The canary name makes up part of the canary ARN, and the ARN is included in outbound calls over the internet. For more information, see `Security Considerations for Synthetics Canaries <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/servicelens_canaries_security.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def runtime_version(self) -> builtins.str:
        '''Specifies the runtime version to use for the canary.

        For more information about runtime versions, see `Canary Runtime Versions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-runtimeversion
        '''
        result = self._values.get("runtime_version")
        assert result is not None, "Required property 'runtime_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schedule(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnCanary.ScheduleProperty]:
        '''A structure that contains information about how often the canary is to run, and when these runs are to stop.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-schedule
        '''
        result = self._values.get("schedule")
        assert result is not None, "Required property 'schedule' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnCanary.ScheduleProperty], result)

    @builtins.property
    def artifact_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCanary.ArtifactConfigProperty]]:
        '''A structure that contains the configuration for canary artifacts, including the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-artifactconfig
        '''
        result = self._values.get("artifact_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCanary.ArtifactConfigProperty]], result)

    @builtins.property
    def delete_lambda_resources_on_canary_deletion(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''(deprecated) Deletes associated lambda resources created by Synthetics if set to True.

        Default is False

        :deprecated: this property has been deprecated

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-deletelambdaresourcesoncanarydeletion
        :stability: deprecated
        '''
        result = self._values.get("delete_lambda_resources_on_canary_deletion")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def failure_retention_period(self) -> typing.Optional[jsii.Number]:
        '''The number of days to retain data about failed runs of this canary.

        If you omit this field, the default of 31 days is used. The valid range is 1 to 455 days.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-failureretentionperiod
        '''
        result = self._values.get("failure_retention_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def run_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCanary.RunConfigProperty]]:
        '''A structure that contains input information for a canary run.

        If you omit this structure, the frequency of the canary is used as canary's timeout value, up to a maximum of 900 seconds.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-runconfig
        '''
        result = self._values.get("run_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCanary.RunConfigProperty]], result)

    @builtins.property
    def start_canary_after_creation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specify TRUE to have the canary start making runs immediately after it is created.

        A canary that you create using CloudFormation can't be used to monitor the CloudFormation stack that creates the canary or to roll back that stack if there is a failure.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-startcanaryaftercreation
        '''
        result = self._values.get("start_canary_after_creation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def success_retention_period(self) -> typing.Optional[jsii.Number]:
        '''The number of days to retain data about successful runs of this canary.

        If you omit this field, the default of 31 days is used. The valid range is 1 to 455 days.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-successretentionperiod
        '''
        result = self._values.get("success_retention_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The list of key-value pairs that are associated with the canary.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def visual_reference(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCanary.VisualReferenceProperty]]:
        '''If this canary performs visual monitoring by comparing screenshots, this structure contains the ID of the canary run to use as the baseline for screenshots, and the coordinates of any parts of the screen to ignore during the visual monitoring comparison.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-visualreference
        '''
        result = self._values.get("visual_reference")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCanary.VisualReferenceProperty]], result)

    @builtins.property
    def vpc_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCanary.VPCConfigProperty]]:
        '''If this canary is to test an endpoint in a VPC, this structure contains information about the subnet and security groups of the VPC endpoint.

        For more information, see `Running a Canary in a VPC <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_VPC.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-vpcconfig
        '''
        result = self._values.get("vpc_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCanary.VPCConfigProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCanaryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_synthetics.CfnGroup",
):
    '''Creates or updates a group which you can use to associate canaries with each other, including cross-Region canaries.

    Using groups can help you with managing and automating your canaries, and you can also view aggregated run results and statistics for all canaries in a group.

    Groups are global resources. When you create a group, it is replicated across all AWS Regions, and you can add canaries from any Region to it, and view it in any Region. Although the group ARN format reflects the Region name where it was created, a group is not constrained to any Region. This means that you can put canaries from multiple Regions into the same group, and then use that group to view and manage all of those canaries in a single view.

    Each group can contain as many as 10 canaries. You can have as many as 20 groups in your account. Any single canary can be a member of up to 10 groups.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-group.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_synthetics as synthetics
        
        cfn_group = synthetics.CfnGroup(self, "MyCfnGroup",
            name="name",
        
            # the properties below are optional
            resource_arns=["resourceArns"],
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
        resource_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: A name for the group. It can include any Unicode characters. The names for all groups in your account, across all Regions, must be unique.
        :param resource_arns: The ARNs of the canaries that you want to associate with this group.
        :param tags: The list of key-value pairs that are associated with the group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__973b5b11ee0c26a7aa94d55785d1a025e0c569700b7877564d84ae1447c2af09)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGroupProps(name=name, resource_arns=resource_arns, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c02721081747307dfd2212f0ae4958cfbad3dc1ec5b0667712fb08ebd5d7e65)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c4dd500824b1b77e386dc3d0eca110f83c00176cc9ac0861387258adf2b7914e)
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
        '''The Id of the group.

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A name for the group.

        It can include any Unicode characters.
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6401b033d62b6cede0e2328e1f7c75c5607ed33e285fb529afce4814a3551bee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceArns")
    def resource_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ARNs of the canaries that you want to associate with this group.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceArns"))

    @resource_arns.setter
    def resource_arns(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__078802d6cab1e35c6ba04d10e648f52314cd74f1c2d198563fb8a7d6435999ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArns", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The list of key-value pairs that are associated with the group.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d85cd0ddf465884c3990e0492b92e22606ecfb33b8127bf42d0c344b78427aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_synthetics.CfnGroupProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "resource_arns": "resourceArns", "tags": "tags"},
)
class CfnGroupProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        resource_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnGroup``.

        :param name: A name for the group. It can include any Unicode characters. The names for all groups in your account, across all Regions, must be unique.
        :param resource_arns: The ARNs of the canaries that you want to associate with this group.
        :param tags: The list of key-value pairs that are associated with the group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-group.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_synthetics as synthetics
            
            cfn_group_props = synthetics.CfnGroupProps(
                name="name",
            
                # the properties below are optional
                resource_arns=["resourceArns"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ab100d4133b5b7bd6483c4c3bcf827df685974681f592679f7de8f8ea64b33f)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_arns", value=resource_arns, expected_type=type_hints["resource_arns"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if resource_arns is not None:
            self._values["resource_arns"] = resource_arns
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''A name for the group. It can include any Unicode characters.

        The names for all groups in your account, across all Regions, must be unique.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-group.html#cfn-synthetics-group-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ARNs of the canaries that you want to associate with this group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-group.html#cfn-synthetics-group-resourcearns
        '''
        result = self._values.get("resource_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The list of key-value pairs that are associated with the group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-group.html#cfn-synthetics-group-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCanary",
    "CfnCanaryProps",
    "CfnGroup",
    "CfnGroupProps",
]

publication.publish()

def _typecheckingstub__b8fcb3f48eca9399b4d1d31a5ef709e22f9fa52ad1e174b75d8313ef2b971663(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    artifact_s3_location: builtins.str,
    code: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.CodeProperty, typing.Dict[builtins.str, typing.Any]]],
    execution_role_arn: builtins.str,
    name: builtins.str,
    runtime_version: builtins.str,
    schedule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.ScheduleProperty, typing.Dict[builtins.str, typing.Any]]],
    artifact_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.ArtifactConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    delete_lambda_resources_on_canary_deletion: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    failure_retention_period: typing.Optional[jsii.Number] = None,
    run_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.RunConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    start_canary_after_creation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    success_retention_period: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    visual_reference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.VisualReferenceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.VPCConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc166bab0fcf177897c1dbb233203e39458428064bc6ff7215b01b2b3ec6f3a2(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65410bca39459dd8b2ef582ab37870de468cb765034b9600759877910b340355(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdaba4ac1ed08cbb682b002e6d07aabeaccadbe7c5a6d4bbbc1aaaa15bb4831c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__940d05df3a63f7ad05e985fa05317d4b896a6a845409a8d700cbf186fd8e49d5(
    value: typing.Union[_IResolvable_da3f097b, CfnCanary.CodeProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21989f82228cbbd4b8df02c1285ab8cf3635cf4eb894f4a4c999e6b763e92ded(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02a5568fdb7b5da09cb493a9883d04e695a0b6375532601c26ea6ba719fd869a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64f9d8326de93a51cdd4ab89bc4c5431c218c9b46372d81f4fe7a8961b26fa2c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e387628a17b84461f77d8fdc851f2b16bcda58e50d8e9279d02062270a5516f0(
    value: typing.Union[_IResolvable_da3f097b, CfnCanary.ScheduleProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5946ee35eff32e4581a6d2e3e0c69d62cdc3c17f079123211f7251bc1a10d878(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCanary.ArtifactConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__442577c2c36e4274dca25b3d866e1aeec3f4ffc18732e01050131a31f768f2b3(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02a7e43f45419c4cb8e909f309f8848d4ced91d17b01d14e5ea0b8cec28aab1b(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e65fb80249e43aebfe46950832be73ed0795003be5d74ca1ef7cd12bb2408557(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCanary.RunConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a98feaf45022b36ef5c9888f87b978029d5e1fde70599e1972543b1778adfad(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8bbba327f646025c54903ccf2c19cedc26cf07f79658c389f65ef40b263130f(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__212d1e59a4bd96a18f447b1c742abcfeb7c668063c8e1670fa0770e339ac4077(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21e93a70969fa03a3f0aa85f6b1615a26d9a0afef8a0cf27f0888fc59aef420b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCanary.VisualReferenceProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be63ed6816e3043aef63f6e7c0d0dfcc35f1249735acd4eff8530f8c2253b747(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCanary.VPCConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c456e72742651aec26b46a7fbd663821284d03931fd10859243079b815dad28(
    *,
    s3_encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.S3EncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d401a2416919aef18322e23fb875fc37ad8f90f34f8f5708a245f22f9d3208f(
    *,
    screenshot_name: builtins.str,
    ignore_coordinates: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d403372a613babc1ab10717d050ec9a7f4055961f3545f2d0600d89c7b3dcc3(
    *,
    handler: builtins.str,
    s3_bucket: typing.Optional[builtins.str] = None,
    s3_key: typing.Optional[builtins.str] = None,
    s3_object_version: typing.Optional[builtins.str] = None,
    script: typing.Optional[builtins.str] = None,
    source_location_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa148862e82948accbbe951e7afcee721aa7014754c81106d2648fe1c5cf28e2(
    *,
    active_tracing: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    environment_variables: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    memory_in_mb: typing.Optional[jsii.Number] = None,
    timeout_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__551aad28104a61040e1d9e12e77c77ae47c6e19a45d15bfa94e441c5d297d3ab(
    *,
    encryption_mode: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4999288d0e0c5de04c56a3436208778026602dfdca27710aee93f9f4e034c29(
    *,
    expression: builtins.str,
    duration_in_seconds: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eccfde82eb2354e9c416fba506f2ff8e4fb1a86792529f65e2d8eafbc8415074(
    *,
    security_group_ids: typing.Sequence[builtins.str],
    subnet_ids: typing.Sequence[builtins.str],
    vpc_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f52b6b7318141dc99f6bd36c21b91cda286b67d7dea805791a6132a2cd794526(
    *,
    base_canary_run_id: builtins.str,
    base_screenshots: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.BaseScreenshotProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d869d56ce0d1d2e2add2f80bf39b28abbec2752c719e03194ee540bf1949e423(
    *,
    artifact_s3_location: builtins.str,
    code: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.CodeProperty, typing.Dict[builtins.str, typing.Any]]],
    execution_role_arn: builtins.str,
    name: builtins.str,
    runtime_version: builtins.str,
    schedule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.ScheduleProperty, typing.Dict[builtins.str, typing.Any]]],
    artifact_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.ArtifactConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    delete_lambda_resources_on_canary_deletion: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    failure_retention_period: typing.Optional[jsii.Number] = None,
    run_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.RunConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    start_canary_after_creation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    success_retention_period: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    visual_reference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.VisualReferenceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.VPCConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__973b5b11ee0c26a7aa94d55785d1a025e0c569700b7877564d84ae1447c2af09(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    resource_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c02721081747307dfd2212f0ae4958cfbad3dc1ec5b0667712fb08ebd5d7e65(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4dd500824b1b77e386dc3d0eca110f83c00176cc9ac0861387258adf2b7914e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6401b033d62b6cede0e2328e1f7c75c5607ed33e285fb529afce4814a3551bee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__078802d6cab1e35c6ba04d10e648f52314cd74f1c2d198563fb8a7d6435999ba(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d85cd0ddf465884c3990e0492b92e22606ecfb33b8127bf42d0c344b78427aa(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ab100d4133b5b7bd6483c4c3bcf827df685974681f592679f7de8f8ea64b33f(
    *,
    name: builtins.str,
    resource_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
